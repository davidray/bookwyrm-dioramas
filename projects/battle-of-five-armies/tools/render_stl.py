"""Quick clay render of STL files: python3 render_stl.py OUT.png A.stl [B.stl ...] [--az 30 --el 40]"""
import math, sys, os
import bpy
from mathutils import Vector
args = sys.argv[1:]; az = el = None
if "--az" in args: i = args.index("--az"); az = float(args[i + 1]); del args[i:i + 2]
if "--el" in args: i = args.index("--el"); el = float(args[i + 1]); del args[i:i + 2]
az = 30 if az is None else az; el = 40 if el is None else el
out, files = args[0], args[1:]
bpy.ops.wm.read_factory_settings(use_empty=True); sc = bpy.context.scene
m = bpy.data.materials.new("c"); m.use_nodes = True
m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (.8, .78, .74, 1)
lo = Vector((1e9,) * 3); hi = Vector((-1e9,) * 3)
for f in files:
    bpy.ops.wm.stl_import(filepath=f); o = bpy.context.selected_objects[0]; o.data.materials.append(m)
    for c in o.bound_box:
        v = o.matrix_world @ Vector(c); lo = Vector(map(min, lo, v)); hi = Vector(map(max, hi, v))
ctr = (lo + hi) / 2; r = (hi - lo).length
cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam")); sc.collection.objects.link(cam); sc.camera = cam
d = Vector((math.cos(math.radians(el)) * math.sin(math.radians(az)), -math.cos(math.radians(el)) * math.cos(math.radians(az)), math.sin(math.radians(el))))
cam.location = ctr + d * r * 1.25; cam.rotation_mode = "QUATERNION"; cam.rotation_quaternion = (-d).to_track_quat("-Z", "Y"); cam.data.lens = 50; cam.data.clip_end = 1e5
bpy.ops.object.light_add(type="SUN", rotation=(math.radians(45), math.radians(10), math.radians(-35))); bpy.context.object.data.energy = 3
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True; w.node_tree.nodes["Background"].inputs[0].default_value = (.35, .36, .38, 1)
sc.render.engine = "CYCLES"; sc.cycles.samples = 16; sc.render.resolution_x, sc.render.resolution_y = 1400, 1000
sc.render.filepath = out; bpy.ops.render.render(write_still=True)
