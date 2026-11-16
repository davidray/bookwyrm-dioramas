# Isle of Berk, v8

A summer Viking village on a rocky island, inspired by How to Train Your Dragon (fan piece, personal use only). Mead hall, five longhouses, cliff house, watchtower, two warrior statues, stables, fish racks and a harbour with two longships. Dragons from the film: a Night Fury on top of the chain-domed arena, a Monstrous Nightmare on a longhouse roof, and a Deadly Nadder and a Gronckle flying on clear rods. 24 Vikings and 10 sheep.

Built with the scene workflow (concept, element art, sculpt images, Meshy image-to-3D meshes, Blender/trimesh assembly and print engineering). `v8` is the assembly version David approved and locked on 2026-11-16 ("Lock it").

## Files

- `piece.json`: the library record for this version.
- `print/parts.json`: every print file with size, face count, watertight check, bed check and how many to print.
- `print/SHA256SUMS`: hashes of the locked STL set.
- `source/`: `assembly.json` (piece placement), `scene.json` (final placed bounds) and `layout.json` (base, terraces, element layout).

**STLs and renders are not in git** (this repo ignores meshes). The locked set is on David's Mac in `~/code/bookwyrm-rpg-lantern-art/berk-diorama/print-v8/` (37 files, 921 MB). Check a copy with `shasum -a 256 -c print/SHA256SUMS` from a folder holding `print/*.stl`. Tools, renders and the decision log are in the Claude project folder `berk/`.

**Claim level:** digitally validated only. Nothing has been test printed. Scene review about 62 % against the concept (the review loop stopped on its plateau rule; later changes were David's own requests).
**Footprint:** 840 x 600 mm island in 4 x 3 tiles (each up to 210 x 200 mm), about 400 mm tall to the flying dragons; the summit tile is 250 mm.
**Spend:** 923 Meshy credits, $0.

## Bambu A1 (white PLA, hand painted)

| Part | Count | Notes |
|---|---|---|
| G1-ground-tile F1-F4, M1-M4, B1-B4 | 12 | Heightfield tiles, sea level at 12 mm. 0.2 mm layers, 2 walls, 5-8 % infill. Tall summit tiles take about a day. |
| G1-tile-clip | 34 | Two per internal seam, in the underside slots. Glue if loose. |
| B1-B6 buildings, W1 watchtower, S1/S2 statues, V1 longship (x2) | 10 | Meshy meshes decimated to 800k faces. 0.12 mm layers, tree supports under eaves and finials. |
| D1 Monstrous Nightmare | 1 | 148 x 113 x 86 mm. Glue its beam along the ridge of the B2 longhouse. |
| D2 Deadly Nadder, D3 Gronckle | 1 each | 3.2 mm socket in the belly for a 3 mm clear acrylic or brass rod; drill the terrain to match. |
| D4 Night Fury | 1 | 58 x 47 x 35 mm. Glue on the flat pad at the top of the chain dome. |
| A1 chain dome, B7 stables, K1 fish racks and barrels | 1 + 1 + 3 + 5 | Modelled in code, watertight. The dome prints upright with tree supports. |
| F1 Vikings (4 poses) | 6 each | About 25 mm. 0.08 mm layers. |
| K2 sheep (standing, grazing) | 5 each | About 13 mm tall. |

Every part fits the 256 mm bed and has no open edges. The decimated meshes have a few pinched edges, which Bambu Studio repairs on import.

## Known gaps

- Harbour reads empty; piers are solid; no crane gantry from the concept.
- Sea stacks and the summit still read as cones, and the sea doesn't wrap the back and right edges.
- Stables read as flat slabs; the arena ring wall is thin.
- The B6 cliff house sits nearly level with the arena.
- No test print yet; tile clips untested.

## Test plan

1. Print tile F1 and two clips. Check the clip fit.
2. Print one Viking, one sheep and the Night Fury. Check the thin parts.
3. Then the tiles, buildings and dragons.
