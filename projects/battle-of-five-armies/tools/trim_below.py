"""Cut a leaf mesh with a horizontal plane and keep what is above it (capped), then
re-seat it on z=0.  Usage: python3 trim_below.py IN.stl OUT.stl Z_MM"""
import sys, trimesh
m = trimesh.load(sys.argv[1]); z = float(sys.argv[3])
t = m.slice_plane([0, 0, z], [0, 0, 1], cap=True)
parts = t.split(only_watertight=False); t = max(parts, key=lambda p: len(p.faces)) if len(parts) > 1 else t
t.apply_translation([0, 0, -t.bounds[0][2]]); t.export(sys.argv[2])
print(len(m.faces), "->", len(t.faces), [round(x, 1) for x in t.extents], "pieces", len(parts))
