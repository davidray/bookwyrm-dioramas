"""Print export for the five-armies diorama (headless bpy).
Usage: python3 export_print.py MESH_DIR PLACEMENTS.json OUT_DIR [--tiles TL,TR,BL,BR] [--voxel 0.4]

MESH_DIR holds one STL per element id (leaf STLs, Z-up, base z=0, front -y).
Base: four tiles 289.5 mm square (0.25 mm seam clearance per side), flat bottom at z=-12.
Each tile = ground solid + floor patches + terrain + trees + smoke in that tile, voxel-remeshed
into one solid, cut to the tile, then:
  - regiment seats: 2D hull of each regiment's base (+0.4 mm), 1.5 mm below its base, open above;
  - gate seat: hull of the gate (+0.4 mm), swept to the front so the gate slides in, up to its top;
  - eagle rod holes: 3.6 mm dia, 10 mm deep, along each rod (3 mm rod, purchased);
  - alignment tabs on internal seams: male 4.0 dia x 4.0 on one tile, female 4.2 x 4.2 on the other.
Separate prints: gate, eagles (with an 8 mm rod hole), one STL per regiment design (lowered 1.5 mm).
"""
import argparse, json, math, os, sys
import bpy, bmesh
from mathutils import Vector, Matrix

ap = argparse.ArgumentParser()
ap.add_argument("mesh"); ap.add_argument("placements"); ap.add_argument("out")
ap.add_argument("--tiles", default="TL,TR,BL,BR"); ap.add_argument("--voxel", type=float, default=0.4)
ap.add_argument("--max-faces", type=int, default=2500000)
a = ap.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:])
os.makedirs(a.out, exist_ok=True)
T = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(T, "..", "L1-elements", "assembly.json")))
PL = json.load(open(a.placements))
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
H = 286.0; GAP = 0.25; BOT = -12.0   # outer rim trimmed 4 mm so a tile plus its 4 mm tabs fits the 290 mm A2L bed
TILES = {"TL": (-H, 0, 0, H), "TR": (0, H, 0, H), "BL": (-H, 0, -H, 0), "BR": (0, H, -H, 0)}
# one male edge per tile, round the centre: TL->TR, TR->BR, BR->BL, BL->TL
MALE = {"TL": "x", "TR": "y", "BR": "x", "BL": "y"}
TAB_R, TAB_L, SOC_R, SOC_D = 2.0, 4.0, 2.1, 4.2
ROD_HOLE_R, ROD_TILE_D, ROD_EAGLE_D = 1.8, 10.0, 8.0
SEAT_OFF, SEAT_DEPTH = 0.4, 1.5
_data = {}

def mesh_of(el):
    if el not in _data:
        bpy.ops.wm.stl_import(filepath=os.path.join(a.mesh, el + ".stl"))
        o = bpy.context.selected_objects[0]; _data[el] = o.data; bpy.data.objects.remove(o)
    return _data[el]

def obj(name, me, M=None):
    o = bpy.data.objects.new(name, me); sc.collection.objects.link(o)
    if M is not None: o.matrix_world = M
    return o

def baked(name, el, M):
    """A world-space copy (transform applied) of an element."""
    me = mesh_of(el).copy(); me.transform(M)
    if M.determinant() < 0: me.flip_normals()
    return obj(name, me)

def mat(rows): return Matrix(rows)

def box(name, x0, x1, y0, y1, z0, z1):
    bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1)
    for v in bm.verts:
        v.co = Vector(((x0 + x1) / 2 + v.co.x * (x1 - x0), (y0 + y1) / 2 + v.co.y * (y1 - y0), (z0 + z1) / 2 + v.co.z * (z1 - z0)))
    me = bpy.data.meshes.new(name); bm.to_mesh(me); return obj(name, me)

def cyl(name, a3, b3, r, seg=32):
    v = b3 - a3; bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=seg, radius1=r, radius2=r, depth=v.length)
    me = bpy.data.meshes.new(name); bm.to_mesh(me)
    q = v.to_track_quat("Z", "Y"); me.transform(Matrix.Translation((a3 + b3) / 2) @ q.to_matrix().to_4x4())
    return obj(name, me)

def prism(name, poly, z0, z1):
    bm = bmesh.new(); vs = [bm.verts.new((x, y, z0)) for x, y in poly]; f = bm.faces.new(vs)
    r = bmesh.ops.extrude_face_region(bm, geom=[f])
    for v in [g for g in r["geom"] if isinstance(g, bmesh.types.BMVert)]: v.co.z = z1
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(name); bm.to_mesh(me); return obj(name, me)

def boolean(o, cutter, op):
    m = o.modifiers.new("b", "BOOLEAN"); m.operation = op; m.solver = "MANIFOLD" if "MANIFOLD" in [i.identifier for i in bpy.types.BooleanModifier.bl_rna.properties["solver"].enum_items] else "EXACT"
    m.object = cutter
    bpy.context.view_layer.objects.active = o; bpy.ops.object.modifier_apply(modifier=m.name)
    bpy.data.objects.remove(cutter)

def join(objs, name):
    bpy.ops.object.select_all(action="DESELECT")
    for o in objs: o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]; bpy.ops.object.join(); objs[0].name = name; return objs[0]

def hull2d(pts):
    pts = sorted(set(pts))
    if len(pts) < 3: return pts
    def cr(o, p, q): return (p[0] - o[0]) * (q[1] - o[1]) - (p[1] - o[1]) * (q[0] - o[0])
    lo, hi = [], []
    for p in pts:
        while len(lo) >= 2 and cr(lo[-2], lo[-1], p) <= 0: lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi) >= 2 and cr(hi[-2], hi[-1], p) <= 0: hi.pop()
        hi.append(p)
    return lo[:-1] + hi[:-1]

def offset(poly, d):
    cx = sum(p[0] for p in poly) / len(poly); cy = sum(p[1] for p in poly) / len(poly)
    out = []
    for x, y in poly:
        dx, dy = x - cx, y - cy; L = math.hypot(dx, dy) or 1; out.append((x + dx / L * d, y + dy / L * d))
    return out

def export(o, path):
    bpy.ops.object.select_all(action="DESELECT"); o.select_set(True); bpy.context.view_layer.objects.active = o
    bpy.ops.wm.stl_export(filepath=path, export_selected_objects=True, apply_modifiers=True)

def decimate(o, maxf):
    n = len(o.data.polygons)
    if n > maxf:
        m = o.modifiers.new("d", "DECIMATE"); m.ratio = maxf / n
        bpy.context.view_layer.objects.active = o; bpy.ops.object.modifier_apply(modifier="d")

def voxel(o, size):
    o.data.remesh_voxel_size = size; o.data.use_remesh_preserve_volume = False
    bpy.context.view_layer.objects.active = o; bpy.ops.object.voxel_remesh()

kind = lambda p: p["el"][:2]
Pm = [(p, mat(p["matrix"])) for p in PL]
regs = [(p, M) for p, M in Pm if kind(p)[0] == "A"]
gate = [(p, M) for p, M in Pm if kind(p) == "G1"][0]
eagles = [(p, M) for p, M in Pm if kind(p) in ("E1", "E2")]
rods = []
for (p, M), e in zip([(p, M) for p, M in Pm if p["name"].startswith("Cylinder")], A["eagles"]):
    c = M.to_translation(); x, y, z, _ = e["at"]; b = Vector((x, y, z + 8)); rods.append((2 * c - b, b))
G = A["ground"]

def ground_z(x, y):
    t = min(1, max(0, (y - G["rise_from"]) / (G["rise_to"] - G["rise_from"]))); return G["z0"] + t * (G["z1"] - G["z0"])

def ground_solid(x0, x1, y0, y1, n=30):
    bm = bmesh.new(); top = []; bot = []
    for j in range(n + 1):
        for i in range(n + 1):
            x = x0 + (x1 - x0) * i / n; y = y0 + (y1 - y0) * j / n
            top.append(bm.verts.new((x, y, ground_z(x, y)))); bot.append(bm.verts.new((x, y, BOT)))
    idx = lambda i, j: j * (n + 1) + i
    for j in range(n):
        for i in range(n):
            bm.faces.new([top[idx(i, j)], top[idx(i + 1, j)], top[idx(i + 1, j + 1)], top[idx(i, j + 1)]])
            bm.faces.new([bot[idx(i, j + 1)], bot[idx(i + 1, j + 1)], bot[idx(i + 1, j)], bot[idx(i, j)]])
    ring = [idx(i, 0) for i in range(n + 1)] + [idx(n, j) for j in range(1, n + 1)] + [idx(i, n) for i in range(n - 1, -1, -1)] + [idx(0, j) for j in range(n - 1, 0, -1)]
    for k in range(len(ring)):
        p, q = ring[k], ring[(k + 1) % len(ring)]; bm.faces.new([top[p], top[q], bot[q], bot[p]])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new("ground"); bm.to_mesh(me); return obj("ground", me)

def world_bbox(el, M):
    me = mesh_of(el); st = max(1, len(me.vertices) // 4000); vs = [M @ me.vertices[i].co for i in range(0, len(me.vertices), st)]
    return [min(v[i] for v in vs) for i in range(3)], [max(v[i] for v in vs) for i in range(3)]

def seam_tabs(tile):
    """(kind, a, b) cylinders for this tile's two internal edges: male tabs (4.0 x 4.0) on the
    edge MALE names, sockets (4.2 x 4.2) on the other. Tabs sit 6 mm above the flat bottom,
    three per edge."""
    x0, x1, y0, y1 = TILES[tile]; out = []; zc = BOT + 6
    sx = 1 if x1 == 0 else -1          # direction from this tile across its x=0 edge
    sy = 1 if y1 == 0 else -1          # direction across its y=0 edge
    ys = (40, 145, 250) if y0 == 0 else (-40, -145, -250)
    xs = (40, 145, 250) if x0 == 0 else (-40, -145, -250)
    for yy in ys:
        e = Vector((-sx * GAP, yy, zc)); d = Vector((sx, 0, 0))
        out.append(("m", e - d * 0.01, e + d * TAB_L) if MALE[tile] == "x" else ("f", e + d * 0.01, e - d * SOC_D))
    for xx in xs:
        e = Vector((xx, -sy * GAP, zc)); d = Vector((0, sy, 0))
        out.append(("m", e - d * 0.01, e + d * TAB_L) if MALE[tile] == "y" else ("f", e + d * 0.01, e - d * SOC_D))
    return out

REPORT = {"tiles": {}, "parts": {}}
for tile in [t for t in a.tiles.split(",") if t]:
    x0, x1, y0, y1 = TILES[tile]
    bx = (x0 + (GAP if x0 == 0 else 0), x1 - (GAP if x1 == 0 else 0), y0 + (GAP if y0 == 0 else 0), y1 - (GAP if y1 == 0 else 0))
    parts = [ground_solid(x0 - 2, x1 + 2, y0 - 2, y1 + 2)]
    for p, M in Pm:
        if kind(p) in ("K1", "M1", "R1", "H1", "T1", "X1"):
            lo, hi = world_bbox(p["el"], M)
            if hi[0] > x0 and lo[0] < x1 and hi[1] > y0 and lo[1] < y1:
                parts.append(baked(p["name"], p["el"], M))
    t = join(parts, "tile_" + tile)
    voxel(t, a.voxel)
    boolean(t, box("cut", bx[0], bx[1], bx[2], bx[3], BOT - 0.01, 600), "INTERSECT")
    # floor-level clean-up: nothing below the flat bottom
    # regiment seats
    for p, M in regs:
        me = mesh_of(p["el"]); zmin = min(v.co.z for v in me.vertices)
        foot = [(M @ v.co) for v in me.vertices if v.co.z < zmin + 1.0]
        poly = offset(hull2d([(round(v.x, 2), round(v.y, 2)) for v in foot]), SEAT_OFF)
        if not any(bx[0] - 5 < x < bx[1] + 5 and bx[2] - 5 < y < bx[3] + 5 for x, y in poly): continue
        zb = (M @ Vector((0, 0, zmin))).z
        boolean(t, prism("seat", poly, zb - SEAT_DEPTH, zb + 60), "DIFFERENCE")
    # gate seat
    p, M = gate; me = mesh_of(p["el"]); zg = (M @ Vector((0, 0, min(v.co.z for v in me.vertices)))).z
    gw = [(M @ v.co) for v in list(me.vertices)[::20]]; gh = max(v.z for v in gw) - zg
    # the gate slides in from the front: its hull swept 120 mm toward the viewer, up to its own top
    gpoly = offset(hull2d([(round(v.x, 1), round(v.y + dy, 1)) for v in gw for dy in (0, -120)]), SEAT_OFF)
    if any(bx[0] < x < bx[1] and bx[2] < y < bx[3] for x, y in gpoly):
        boolean(t, prism("gseat", gpoly, zg, zg + gh + SEAT_OFF), "DIFFERENCE")
    # rod holes
    for ra, rb in rods:
        if bx[0] < ra.x < bx[1] and bx[2] < ra.y < bx[3]:
            d = (rb - ra).normalized(); boolean(t, cyl("rod", ra - d * ROD_TILE_D, ra + d * 40, ROD_HOLE_R), "DIFFERENCE")
    # tabs
    for kind_, p0, p1 in seam_tabs(tile):
        if kind_ == "m":
            c = cyl("tab", p0, p1, TAB_R); boolean(t, c, "UNION")
        else:
            boolean(t, cyl("soc", p0, p1, SOC_R), "DIFFERENCE")
    decimate(t, a.max_faces)
    path = os.path.join(a.out, "tile-%s.stl" % tile.lower()); export(t, path)
    REPORT["tiles"][tile] = {"faces": len(t.data.polygons), "dims": [round(d, 1) for d in t.dimensions], "file": os.path.basename(path)}
    print("tile", tile, REPORT["tiles"][tile], flush=True)
    bpy.data.objects.remove(t)

if os.environ.get("PARTS", "1") == "1":
    # gate
    p, M = gate; g = baked("gate", p["el"], Matrix.Diagonal(M.to_scale().to_4d()))
    export(g, os.path.join(a.out, "gate-statues.stl")); REPORT["parts"]["gate-statues"] = {"qty": 1, "dims": [round(d, 1) for d in g.dimensions]}
    bpy.data.objects.remove(g)
    # eagles: rod hole from the rod's top end, in the eagle's own frame
    for k, (p, M) in enumerate(eagles):
        ra, rb = min(rods, key=lambda r: (r[1] - M.to_translation()).length)  # the rod under this eagle
        e = baked("eagle", p["el"], M); d = (rb - ra).normalized()
        zs = [v.co.z for v in e.data.vertices]; zb = min(zs) + 0.35 * (max(zs) - min(zs))
        rb = ra + d * ((zb - ra.z) / d.z)   # run the rod up into the body, not the talons
        boolean(e, cyl("rod", rb - d * ROD_EAGLE_D, rb + d * 2, ROD_HOLE_R), "DIFFERENCE")
        zmin = min(v.co.z for v in e.data.vertices); c = M.to_translation()
        e.data.transform(Matrix.Translation((-c.x, -c.y, -zmin))); export(e, os.path.join(a.out, "eagle-%d-%s.stl" % (k + 1, p["el"][:2].lower())))
        REPORT["parts"]["eagle-%d-%s" % (k + 1, p["el"][:2].lower())] = {"qty": 1, "rod_mm": round((rb - ra).length + ROD_TILE_D + ROD_EAGLE_D - 2, 0), "dims": [round(d, 1) for d in e.dimensions]}
        bpy.data.objects.remove(e)
    # regiments: one file per design, scaled like the scene
    from collections import Counter
    cnt = Counter(p["el"] for p, M in regs)
    for el, q in sorted(cnt.items()):
        M = [M for p, M in regs if p["el"] == el][0]; s = M.to_scale()
        r = baked(el, el, Matrix.Diagonal(s.to_4d())); export(r, os.path.join(a.out, "regiment-%s.stl" % el.lower()))
        REPORT["parts"]["regiment-" + el.lower()] = {"qty": q, "dims": [round(d, 1) for d in r.dimensions]}
        bpy.data.objects.remove(r)
json.dump(REPORT, open(os.path.join(a.out, "report-%s.json" % a.tiles.replace(",", "")), "w"), indent=1)
print("done")
