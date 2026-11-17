"""Assemble the five-armies scene from decimated leaves and render review views.
Usage: python3 assemble.py DEC_DIR OUT_DIR [--seed N]
Reads ../L1-elements/assembly.json (placements). Leaves are Z-up, base on z=0, centred, front -y.
Regiments and props are dropped onto whatever lies below them (ray cast)."""
import json, math, os, sys, random
import bpy
from mathutils import Vector, Matrix

T = os.path.dirname(os.path.abspath(__file__))
DEC, OUT = sys.argv[1], sys.argv[2]
A = json.load(open(os.path.join(T, "..", "L1-elements", sys.argv[3] if len(sys.argv) > 3 else "assembly.json"))); os.makedirs(OUT, exist_ok=True)
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
clay = bpy.data.materials.new("clay"); clay.use_nodes = True
clay.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (.78, .76, .72, 1)
clay.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = .8
_cache = {}

def leaf(el):
    if el not in _cache:
        bpy.ops.wm.stl_import(filepath=os.path.join(DEC, el + ".stl"))
        o = bpy.context.selected_objects[0]; o.data.materials.append(clay)
        _cache[el] = o.data; bpy.data.objects.remove(o)
    o = bpy.data.objects.new(el, _cache[el]); sc.collection.objects.link(o); return o

def place(el, x, y, z, yaw=0, s=1.0, sx=None):
    o = leaf(el); o.location = (x, y, z); o.rotation_euler = (0, 0, math.radians(yaw))
    o.scale = (sx if sx is not None else s, s, s); return o

def drop(x, y, top=2000):
    dg = bpy.context.evaluated_depsgraph_get()
    hit, loc, *_ = sc.ray_cast(dg, Vector((x, y, top)), Vector((0, 0, -1)))
    return loc.z if hit else 0.0

# ground slab with valley rise (structure, code)
import bmesh
G = A["ground"]; h = G["w"] / 2; n = 24
bm = bmesh.new(); grid = []
for j in range(n + 1):
    row = []
    for i in range(n + 1):
        x = -h + 2 * h * i / n; y = -h + 2 * h * j / n
        t = min(1, max(0, (y - G["rise_from"]) / (G["rise_to"] - G["rise_from"])))
        row.append(bm.verts.new((x, y, G["z0"] + t * (G["z1"] - G["z0"]))))
    grid.append(row)
for j in range(n):
    for i in range(n):
        bm.faces.new([grid[j][i], grid[j][i + 1], grid[j + 1][i + 1], grid[j + 1][i]])
me = bpy.data.meshes.new("ground"); bm.to_mesh(me)
g = bpy.data.objects.new("ground", me); sc.collection.objects.link(g); g.data.materials.append(clay)
sl = g.modifiers.new("slab", "SOLIDIFY"); sl.thickness = G["slab"]; sl.offset = -1

for t in A.get("patches", []):
    x, y, yaw = t["at"]; o = place(t["el"], x, y, drop(x, y) - 7.5, yaw)  # surface flush with the ground
    sx, sy, sz = t.get("sc", (1.4, 1.4, 0.85)); o.scale = (-sx if t.get("mirror") else sx, sy, sz)

for t in A["terrain"]:
    x, y, yaw = t["at"]; z = t.get("z", drop(x, y) - t.get("sink", 0))
    o = place(t["el"], x, y, z, yaw)
    sx, sy, sz = t["sc"]; o.scale = (-sx if t.get("mirror") else sx, sy, sz)

for p in A["placed"]:
    x, y, yaw = p["at"]; s = p.get("s", 1.0)
    place(p["el"], x, y, drop(x, y) - p.get("sink", 0.6), yaw, s)

# eagles on 3 mm rods (structure)
for e in A["eagles"]:
    x, y, z, yaw = e["at"]; place(e["el"], x, y, z, yaw, e["s"])
    rx, ry = e["rod_to"]; a = Vector((rx, ry, drop(rx, ry))); b = Vector((x, y, z + 8)); v = b - a
    bpy.ops.mesh.primitive_cylinder_add(radius=1.5, depth=v.length, location=(a + b) / 2)
    c = bpy.context.object; c.rotation_mode = "QUATERNION"; c.rotation_quaternion = v.to_track_quat("Z", "Y"); c.data.materials.append(clay)

sc.render.engine = "CYCLES"; sc.cycles.samples = 24; sc.cycles.device = "CPU"
sc.render.resolution_x, sc.render.resolution_y = 1536, 1024
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True; w.node_tree.nodes["Background"].inputs[0].default_value = (.35, .36, .38, 1)
bpy.ops.object.light_add(type="SUN", rotation=(math.radians(45), math.radians(10), math.radians(-35))); bpy.context.object.data.energy = 3.0
bpy.ops.object.light_add(type="SUN", rotation=(math.radians(60), 0, math.radians(140))); bpy.context.object.data.energy = 0.8
cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam")); sc.collection.objects.link(cam); sc.camera = cam; cam.data.clip_end = 10000
for c in A["cameras"]:
    cam.location = c["loc"]; cam.rotation_mode = "QUATERNION"
    cam.rotation_quaternion = (Vector(c["target"]) - Vector(c["loc"])).to_track_quat("-Z", "Y"); cam.data.lens = c["lens"]
    sc.render.filepath = os.path.join(OUT, c["name"] + ".png"); bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "assembly.blend"))
print("ok", len(A["placed"]), "placed")
