"""Write L1-elements/assembly.json: terrain placements plus regiments scattered in army zones
(min spacing, seeded), trees, smoke, eagles.  Usage: python3 make_assembly.py [seed]"""
import json, math, os, random, sys
T = os.path.dirname(os.path.abspath(__file__)); R = random.Random(7)
FS = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0  # figure scale: 1.0 = 15 mm figures
OUTN = sys.argv[2] if len(sys.argv) > 2 else "assembly.json"
A = {"ground": {"w": 580, "slab": 12, "rise_from": -290, "rise_to": 120, "z0": 0, "z1": 28},
 "terrain": [
  {"el": "M1-mountain", "at": [0, 178, 0], "sc": [1.38, 0.6, 1.0], "z": 0},
  {"el": "G1-gate-statues", "at": [8, 100, 0], "sc": [1, 1, 1], "z": 20},
  {"el": "R1-rock-spur", "at": [-180, 5, 0], "sc": [1.8, 1.8, 1.9], "z": 0},
  {"el": "R1-rock-spur", "at": [168, 25, 0], "sc": [1.3, 1.2, 1.0], "z": 0, "mirror": True},
  {"el": "H1-ruined-hamlet", "at": [200, -175, -20], "sc": [0.75, 0.75, 0.75], "z": 0}],
 "patches": [], "placed": [], "eagles": [
  {"el": "E1-eagle-dive", "at": [-175, 150, 250, 150], "s": 1.25, "rod_to": [-150, 190]},
  {"el": "E2-eagle-strike", "at": [175, 150, 245, 210], "s": 1.25, "rod_to": [150, 190]},
  {"el": "E1-eagle-dive", "at": [-135, -150, 150, 160], "s": 1.15, "rod_to": [-135, -150]},
  {"el": "E2-eagle-strike", "at": [110, -60, 165, 200], "s": 1.15, "rod_to": [110, -60]}],
 "cameras": [
  {"name": "concept", "loc": [-150, -1150, 800], "target": [0, 30, 70], "lens": 42},
  {"name": "top", "loc": [0, -1, 1600], "target": [0, 0, 0], "lens": 32},
  {"name": "close_valley", "loc": [-60, -520, 260], "target": [20, -60, 30], "lens": 40},
  {"name": "side_left", "loc": [-900, -350, 450], "target": [0, 20, 60], "lens": 45}]}
# battlefield floor patches (K1, ~140 mm square) tiled over the open ground, rotated and mirrored
RP = random.Random(11)  # own stream, so regiment placement stays as reviewed in v3
for j, y in enumerate((-215, -85, 40)):
    for i, x in enumerate((-205, -70, 65, 200)):
        if x > 130 and y < -60:
            continue  # the hamlet sits there
        A["patches"].append({"el": "K1-battlefield-floor", "at": [x + RP.uniform(-8, 8), y + RP.uniform(-8, 8), RP.choice((0, 90, 180, 270)) + RP.uniform(-6, 6)], "mirror": (i + j) % 2 == 1})
zones = [  # (elements, max n, xrange, yrange, yaw, spacing at 15 mm): packed until full
 (["A1-dwarf-shieldwall", "A2-dwarf-charge"], 999, (-75, 95), (-25, 60), 0, 23),
 (["A3-elf-archers", "A4-elf-spears"], 999, (-245, -115), (-85, 90), 60, 24),
 (["A5-men-spears", "A6-men-swords"], 999, (110, 225), (-35, 85), -60, 27),
 (["A7-goblin-horde-a", "A8-goblin-horde-b", "A9-goblin-horde-c"], 999, (-150, 160), (-285, -40), 180, 25)]
pts = []
for els, n, xr, yr, yaw, sp in zones:
    k = tries = 0
    sp = sp * FS
    while k < n and tries < 20000:
        tries += 1; x = R.uniform(*xr); y = R.uniform(*yr)
        if all(math.hypot(x - a, y - b) > sp for a, b in pts):
            pts.append((x, y)); A["placed"].append({"el": els[k % len(els)], "at": [round(x, 1), round(y, 1), round(yaw + R.uniform(-20, 20))], "s": FS}); k += 1
    print(els[0][:2], k)
for x, y in [(-270, 130), (-275, -60), (-95, 125), (245, 125), (110, 120), (-262, -262), (-215, -268), (-268, -205), (270, 40), (-185, -150)]:
    A["placed"].append({"el": "T1-pine-cluster", "at": [x, y, R.randint(0, 359)], "sink": 1.5})
A["placed"].append({"el": "X1-smoke-plume", "at": [235, -150, 0], "s": 0.8, "sink": 2})
json.dump(A, open(os.path.join(T, "..", "L1-elements", OUTN), "w"), indent=1)
