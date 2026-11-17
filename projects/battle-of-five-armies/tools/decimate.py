"""Decimate the scaled leaf STLs (render_clay output) for assembly reviews.
Usage: python3 decimate.py LEAVES_DIR OUT_DIR [target_faces]"""
import os, sys
import trimesh, fast_simplification as fs
src, out = sys.argv[1], sys.argv[2]; tgt = int(sys.argv[3]) if len(sys.argv) > 3 else 120000
os.makedirs(out, exist_ok=True)
for d in sorted(os.listdir(src)):
    for f in os.listdir(os.path.join(src, d)):
        if f.endswith("_scaled.stl"):
            m = trimesh.load(os.path.join(src, d, f))
            r = max(0.0, 1 - tgt / max(1, len(m.faces)))
            v, fc = fs.simplify(m.vertices, m.faces, target_reduction=r)
            o = trimesh.Trimesh(v, fc); o.export(os.path.join(out, d + ".stl"))
            print(d, len(m.faces), "->", len(fc), [round(x, 1) for x in o.extents])
