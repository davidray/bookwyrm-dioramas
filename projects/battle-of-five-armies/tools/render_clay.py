"""Scale a raw Meshy GLB to real size and render neutral clay review views.

Usage (container, headless bpy):
  python3 render_clay.py MESH.glb OUT_DIR --height-mm 150 [--art ART.png] [--name LABEL]

Writes OUT_DIR/<name>_scaled.stl (mm, Z-up, base on z=0, centred), clay renders
(<name>_front34.png, _back34.png, _front.png, _side.png, _close.png) and
<name>_review.png: approved art | front 3/4 clay | back 3/4 clay | close-up.
Prints a JSON line with bounds (mm), face count and file paths.
"""
import argparse, json, math, os, sys

import bpy
from mathutils import Vector

ap = argparse.ArgumentParser()
ap.add_argument("mesh"); ap.add_argument("out")
ap.add_argument("--height-mm", type=float, required=True)
ap.add_argument("--art"); ap.add_argument("--name")
ap.add_argument("--res", type=int, default=900)
ap.add_argument("--rot", type=float, default=0.0, help="deg about z applied before scaling, so the art front faces -y")
ap.add_argument("--only-front", action="store_true")
a = ap.parse_args(sys.argv[1:])
name = a.name or os.path.splitext(os.path.basename(a.mesh))[0]
os.makedirs(a.out, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=a.mesh)
meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
bpy.ops.object.select_all(action="DESELECT")
for o in meshes:
    o.select_set(True)
bpy.context.view_layer.objects.active = meshes[0]
if len(meshes) > 1:
    bpy.ops.object.join()
ob = bpy.context.view_layer.objects.active
ob.parent = None
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
# Meshy GLB is Y-up; the glTF importer already converts to Blender Z-up.
for m in list(ob.data.materials):
    pass
ob.data.materials.clear()
if a.rot:
    import math as _m
    ob.rotation_mode = "XYZ"; ob.rotation_euler = (0, 0, _m.radians(a.rot)); bpy.ops.object.transform_apply(rotation=True)
vs = [ob.matrix_world @ v.co for v in ob.data.vertices]
mn = Vector((min(v.x for v in vs), min(v.y for v in vs), min(v.z for v in vs)))
mx = Vector((max(v.x for v in vs), max(v.y for v in vs), max(v.z for v in vs)))
s = (a.height_mm / 1000.0) / (mx.z - mn.z)  # work in metres = mm/1000 for Blender
ob.location = (-(mn.x + mx.x) / 2, -(mn.y + mx.y) / 2, -mn.z)
bpy.ops.object.transform_apply(location=True)
ob.scale = (s, s, s)
bpy.ops.object.transform_apply(scale=True)
vs = [v.co for v in ob.data.vertices]
dims = [max(v[i] for v in vs) - min(v[i] for v in vs) for i in range(3)]
dims_mm = [round(d * 1000, 1) for d in dims]

# STL in mm
stl = os.path.join(a.out, name + "_scaled.stl")
ob.scale = (1000, 1000, 1000)
bpy.ops.object.transform_apply(scale=True)
bpy.ops.wm.stl_export(filepath=stl, export_selected_objects=True, global_scale=1.0)
ob.scale = (0.001, 0.001, 0.001)
bpy.ops.object.transform_apply(scale=True)

mat = bpy.data.materials.new("clay")
mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs["Base Color"].default_value = (0.62, 0.6, 0.57, 1)
bsdf.inputs["Roughness"].default_value = 0.65
ob.data.materials.append(mat)
for p in ob.data.polygons:
    p.use_smooth = False

sc = bpy.context.scene
sc.render.engine = "CYCLES"
sc.cycles.device = "CPU"
sc.cycles.samples = 32
sc.cycles.use_denoising = True
sc.render.resolution_x = sc.render.resolution_y = a.res
sc.render.film_transparent = False
w = bpy.data.worlds.new("w"); sc.world = w
w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.30, 0.31, 0.33, 1)
w.node_tree.nodes["Background"].inputs[1].default_value = 0.6

H = dims[2]; R = max(dims) * 1.0
def light(name, loc, energy, size):
    ld = bpy.data.lights.new(name, "AREA"); ld.energy = energy; ld.size = size
    lo = bpy.data.objects.new(name, ld); sc.collection.objects.link(lo); lo.location = loc
    d = Vector((0, 0, H * 0.4)) - Vector(loc); lo.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
k = (R / 0.15) ** 2
light("key", (R * 1.6, -R * 2.0, R * 2.2), 4 * k, R * 0.6)
light("fill", (-R * 2.0, -R * 1.0, R * 1.0), 1.2 * k, R * 1.2)
light("rim", (0, R * 2.2, R * 1.8), 2 * k, R * 0.8)

cam_d = bpy.data.cameras.new("cam"); cam_d.lens = 85; cam_d.clip_start = 0.0002; cam_d.clip_end = 100
sc.view_settings.exposure = -0.8
cam = bpy.data.objects.new("cam", cam_d); sc.collection.objects.link(cam); sc.camera = cam
def shot(tag, direction, target_z=0.45, dist=3.0, lens=85, tz=None):
    cam_d.lens = lens
    t = Vector((0, 0, H * target_z))
    d = Vector(direction).normalized()
    cam.location = t + d * (max(dims) * dist)
    cam.rotation_euler = (t - cam.location).to_track_quat("-Z", "Y").to_euler()
    p = os.path.join(a.out, f"{name}_{tag}.png")
    sc.render.filepath = p; bpy.ops.render.render(write_still=True); return p

if a.only_front:
    print("RESULT " + json.dumps({"front": shot("front", (0, -1, 0.12)), "dims_mm_xyz": dims_mm})); raise SystemExit
shots = {
    "front34": shot("front34", (0.55, -1.0, 0.55)),
    "back34": shot("back34", (-0.55, 1.0, 0.55)),
    "front": shot("front", (0, -1, 0.12)),
    "side": shot("side", (1, 0, 0.12)),
    "close": shot("close", (0.45, -1.0, 0.35), target_z=0.6, dist=1.1),
}
out = {"name": name, "dims_mm_xyz": dims_mm, "faces": len(ob.data.polygons), "stl": stl, "renders": shots}

try:
    from PIL import Image, ImageDraw
    tiles = []
    if a.art and os.path.exists(a.art):
        tiles.append(("approved art", a.art))
    tiles += [("clay front 3/4", shots["front34"]), ("clay back 3/4", shots["back34"]), ("clay close-up", shots["close"])]
    T = 600
    sheet = Image.new("RGB", (T * len(tiles), T + 30), (25, 25, 25)); dr = ImageDraw.Draw(sheet)
    for i, (lab, p) in enumerate(tiles):
        im = Image.open(p).convert("RGB"); im.thumbnail((T, T))
        sheet.paste(im, (i * T + (T - im.width) // 2, 30 + (T - im.height) // 2)); dr.text((i * T + 6, 8), lab, fill=(255, 255, 255))
    dr.text((sheet.width - 330, 8), f"{name}  {dims_mm[0]}x{dims_mm[1]}x{dims_mm[2]} mm", fill=(255, 220, 120))
    rp = os.path.join(a.out, name + "_review.png"); sheet.save(rp); out["review"] = rp
except Exception as e:
    out["review_error"] = str(e)
print("RESULT " + json.dumps(out))
