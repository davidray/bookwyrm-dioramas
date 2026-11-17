# Battle Below the Mountain Gate: print notes (print r1)

Overall about 572 x 572 mm, about 350 mm tall with the eagles. Matte PLA white throughout. Status: **unproven**; nothing has been printed yet.

## Parts

| Part | Qty | Size (mm) | Printer | Notes |
|---|---|---|---|---|
| tile-tl (mountain left) | 1 | 289.8 x 285.8 x 272 | A2L (0.6) | gate seat, eagle rod hole |
| tile-tr (mountain right) | 1 | 285.8 x 289.8 x 248.9 | A2L (0.6) | gate seat, eagle rod hole |
| tile-bl (valley left) | 1 | 285.8 x 289.8 x 96.4 | A2L (0.6) | regiment seats, eagle rod hole |
| tile-br (valley right, hamlet) | 1 | 289.8 x 285.8 x 118.5 | A2L (0.6) | regiment seats, eagle rod hole |
| gate-statues | 1 | 171 x 97 x 180 | A1 or X2D (0.4) | drops into the gate seat across the TL/TR join |
| eagle-1 .. eagle-4 | 1 each | about 110-120 wide | A1 or X2D (0.4) | 8 mm rod socket in the body |
| regiment a1 dwarf shield-wall | 6 | 35 x 29 x 30 | A1 or X2D (0.4) | |
| regiment a2 dwarf charge | 5 | 36 x 37 x 32 | A1 or X2D (0.4) | |
| regiment a3 elf archers | 7 | 40 x 35 x 38 | A1 or X2D (0.4) | |
| regiment a4 elf spears | 6 | 42 x 26 x 42 | A1 or X2D (0.4) | |
| regiment a5 men spears | 5 | | A1 or X2D (0.4) | |
| regiment a6 men swords | 4 | | A1 or X2D (0.4) | |
| regiment a7-a9 goblin hordes | 12 each | | A1 or X2D (0.4) | |

69 regiment prints in all. Regiments and eagles need supports; tiles print flat side down.

## Joints and seats
- Tiles: 0.25 mm gap, flat bottom. Alignment tabs per the house rule (male 4.0 dia x 4.0, socket 4.2 x 4.2), three per shared edge. Each tile has one male edge: TL x, TR y, BR x, BL y.
- Regiment seats: each regiment's base footprint (convex hull + 0.4 mm), 1.5 mm deep.
- Gate seat: the gate's footprint + 0.4 mm, open to the front so the gate slides in.

## Eagle rods (purchased 3 mm rod, not printed)
Rod holes in the tiles are 3.6 mm dia x 10 mm deep (generous clearance). Cut lengths: eagle-1 140, eagle-2 177, eagle-3 168, eagle-4 195 mm.

## Tools
`tools/make_assembly.py 1.6` -> `elements/assembly.json`; `tools/assemble.py` -> `elements/placements.json`; `tools/export_print.py MESH_DIR elements/placements.json OUT` writes the tiles and parts (voxel 0.4 mm). Meshes, renders and 3MFs live in The Hoard as a draft change set, not in git.
