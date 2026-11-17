"""Blockout of the five-armies scene: base slab with valley rise, a box per element at its
planned size, position and facing (front marker = yellow), rendered from a camera close to the
concept view and from above.  Usage: python3 blockout.py OUT_DIR"""
import json, math, os, sys
import bpy, bmesh
from mathutils import Vector

T = os.path.dirname(os.path.abspath(__file__))
L = json.load(open(os.path.join(T, "..", "L1-elements", "layout.json")))
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene

def mat(n, rgb):
    m = bpy.data.materials.new(n); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (*rgb, 1); return m

M = {k: mat(k, v) for k, v in dict(rock=(.4,.39,.37), ground=(.35,.33,.25), dwarf=(.75,.5,.15), elf=(.15,.5,.2),
     men=(.15,.25,.7), gob=(.25,.25,.25), eagle=(.45,.3,.15), tree=(.1,.3,.12), smoke=(.6,.6,.6),
     water=(.2,.35,.55), mark=(1,.9,0), arch=(.55,.55,.55)).items()}

def box(n, cx, cy, w, d, h, yaw, m, z0=0.0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(cx, cy, z0 + h / 2))
    o = bpy.context.object; o.name = n; o.scale = (w, d, h); o.rotation_euler.z = math.radians(yaw)
    o.data.materials.append(M[m])
    # front marker
    bpy.ops.mesh.primitive_cube_add(size=1)
    f = bpy.context.object; f.scale = (w * .6, 2, 2); f.data.materials.append(M["mark"])
    a = math.radians(yaw); off = Vector((0, -d / 2 - 1, h * .5 - 1)); off.rotate(o.rotation_euler)
    f.location = Vector((cx, cy, z0 + h / 2)) + off; f.rotation_euler.z = a
    return o

def zground(x, y):
    r = L["valley_rise"]; t = min(1, max(0, (y - r["from_y"]) / (r["to_y"] - r["from_y"]))); return r["z0"] + t * (r["z1"] - r["z0"])

# base slab with a valley rise (simple wedge)
W = L["base"]["w"]; s = L["base"]["slab"]
bm = bmesh.new(); h = W / 2
pts = [(-h, -h), (h, -h), (h, h), (-h, h)]
bot = [bm.verts.new((x, y, -s)) for x, y in pts]; top = [bm.verts.new((x, y, zground(x, y))) for x, y in pts]
bm.faces.new(bot[::-1]); bm.faces.new(top)
for i in range(4):
    bm.faces.new([bot[i], bot[(i + 1) % 4], top[(i + 1) % 4], top[i]])
me = bpy.data.meshes.new("base"); bm.to_mesh(me); o = bpy.data.objects.new("base", me); sc.collection.objects.link(o); o.data.materials.append(M["ground"])
# water
sp = L["terrain"][-1]["poly"]; bm = bmesh.new(); vs = [bm.verts.new((x, y, 1.5)) for x, y in sp]; bm.faces.new(vs)
me = bpy.data.meshes.new("water"); bm.to_mesh(me); o = bpy.data.objects.new("water", me); sc.collection.objects.link(o); o.data.materials.append(M["water"])

col = {"M1": "rock", "G1": "arch", "R1": "rock", "H1": "arch"}
for t in L["terrain"]:
    if "box" in t:
        cx, cy, w, d, hh, yaw = t["box"]; box(t["id"], cx, cy, w, d, hh, yaw, col[t["id"][:2]], zground(cx, cy))

def elev(x, y):  # standing height: on a spur top if inside one
    z = zground(x, y)
    for t in L["terrain"]:
        if t["id"].startswith("R1"):
            cx, cy, w, d, hh, _ = t["box"]
            if abs(x - cx) < w / 2 and abs(y - cy) < d / 2: z = zground(cx, cy) + hh
    return z

army = {"A1": "dwarf", "A2": "dwarf", "A3": "elf", "A4": "elf", "A5": "men", "A6": "men", "A7": "gob", "A8": "gob", "A9": "gob"}
for i, r in enumerate(L["regiments"]):
    x, y, yaw = r["at"]; k = r["el"][:2]; w, d, hh = L["regiment_box"]["goblin" if army[k] == "gob" else "A"]
    box("%s.%d" % (r["el"], i), x, y, w, d, hh, yaw, army[k], elev(x, y))
for i, e in enumerate(L["eagles"]):
    x, y, z, yaw = e["at"]; w, d, hh = L["eagle_box"]; box("%s.%d" % (e["el"], i), x, y, w, d, hh, yaw, "eagle", z)
    rx, ry = e["rod_to"]; z0 = elev(rx, ry)
    a = Vector((rx, ry, z0)); b = Vector((x, y, z)); v = b - a
    bpy.ops.mesh.primitive_cylinder_add(radius=1.5, depth=v.length, location=(a + b) / 2)
    c = bpy.context.object; c.rotation_mode = "QUATERNION"; c.rotation_quaternion = v.to_track_quat("Z", "Y"); c.data.materials.append(M["mark"])
for i, p in enumerate(L["props"]):
    x, y = p["at"]; tr = p["el"].startswith("T1")
    box("%s.%d" % (p["el"], i), x, y, 60 if tr else 60, 40 if tr else 60, 60 if tr else 110, 0, "tree" if tr else "smoke", elev(x, y))

# tile seams
for (x0, y0, x1, y1) in [(-h, 0, h, 0), (0, -h, 0, h)]:
    bpy.ops.mesh.primitive_cube_add(size=1, location=((x0 + x1) / 2, (y0 + y1) / 2, 40))
    c = bpy.context.object; c.scale = (max(1.5, x1 - x0), max(1.5, y1 - y0), 0.5); c.data.materials.append(M["mark"])

# render
sc.render.engine = "CYCLES"; sc.cycles.samples = 16; sc.cycles.device = "CPU"
sc.render.resolution_x, sc.render.resolution_y = 1400, 930
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True; w.node_tree.nodes["Background"].inputs[0].default_value = (.5, .5, .52, 1)
bpy.ops.object.light_add(type="SUN", rotation=(math.radians(40), math.radians(15), math.radians(-30))); bpy.context.object.data.energy = 3.5
cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam")); sc.collection.objects.link(cam); sc.camera = cam
cam.data.clip_end = 10000
def shoot(loc, tgt, lens, name, ortho=None):
    cam.location = loc; cam.rotation_mode = "QUATERNION"; cam.rotation_quaternion = (Vector(tgt) - Vector(loc)).to_track_quat("-Z", "Y")
    cam.data.type = "ORTHO" if ortho else "PERSP"; cam.data.lens = lens
    if ortho: cam.data.ortho_scale = ortho
    sc.render.filepath = os.path.join(OUT, name); bpy.ops.render.render(write_still=True)
c = L["camera"]; shoot(c["loc"], c["target"], c["lens"], "blockout_concept.png")
shoot((0, -0.01, 1500), (0, 0, 0), 50, "blockout_top.png", ortho=880)
print("ok", OUT)
