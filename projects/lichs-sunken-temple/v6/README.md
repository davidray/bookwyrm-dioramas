# The Lich's Sunken Temple, v6

A lich stands atop a skull-carved ziggurat sinking into a swamp, while four adventurers (paladin, dwarf cleric, ranger, sorceress) advance along a broken causeway past wading skeletons, toppled priest statues and two dead trees. Original D&D-themed design, built with the scene workflow: Tripo image-to-model meshes for the 12 generated elements (460 credits), Blender assembly and print engineering.

`v6` is the assembly version that was approved and imported into the library as `lichs-sunken-temple` revision 1.

## Files

- `piece.json`: the library record for this version.
- `print/parts.json`: every print file with printer, count, size, face count and open-edge count.
- `print/SHA256SUMS`: hashes of the reviewed STL set.
- `source/library-seed.json`: the mapping used to import it into the library.

**STLs and renders are not in git** (this repo ignores meshes and images). The reviewed set lives on David's Mac in `~/code/bookwyrm-rpg-lantern-art/dnd-lich-temple/print-v1/` and in the library. Check a copy with `shasum -a 256 -c print/SHA256SUMS` from a folder holding `print/*.stl`.

**Claim level:** digitally validated only. Nothing has been test printed. Scene review score about 74 % against the concept (the review loop stopped on its plateau rule).
**Footprint:** 510 x 440 mm base (2 x 2 A1 tiles of 255 x 220, front corners chamfered), about 250 mm tall to the tree tops.
**Spend:** 460 of 580 Tripo credits (12 meshes, all passed first time), $3.80 of OpenAI images. 120 credits unused.
**Files:** STLs and `parts.json` are on the Mac in `~/code/bookwyrm-rpg-lantern-art/dnd-lich-temple/print-v1/` (654 MB). 95 prints in total.

## Bambu A1 (PLA, 0.4 nozzle)

| Part | Count | Size (mm) | Notes |
|---|---|---|---|
| G1-swamp-tile-F1, F2, B1, B2 | 4 | 255 x 220 x 22-26 | Water surface at 12 mm with ripples, mud banks to 26. Print flat, 0.16-0.2 mm layers, 2 walls, 10 % infill. Join with the 8 clips in the underside slots. Paint the water, then gloss varnish or a thin coat of resin water. |
| G1-tile-clip | 8 | 19.6 x 7.6 x 2.8 | Dog-bone joiners; glue if loose. |
| Z1-ziggurat | 1 | 230 x 230 x 162 | Summit cut flat at 165 for the lich and obelisk. Stair faces +x in the file. 0.12-0.16 mm layers, 2-3 walls, sparse infill, tree supports for the skull alcoves. |
| C1-causeway-a, -b | 2 | 146 and 123 long | Flat ends and bottom; sits on the water at 12 mm. a starts at the front-left landing, b runs to the stair foot. |
| T1-dead-tree, T2 (mirrored, 0.95x) | 2 | about 125 x 195 x 205 | Tree supports. Moss strands print beaded: clean up, or swap for real lichen/flock. |
| O1-obelisk | 1 | 24 x 24 x 72.7 | Has a 1.1 mm pin hole for the crystal. |
| P1 pillars (h60, h40, h25, fallen column) | 4 | 18-26 wide | Tripo standard meshes with 166-278 non-manifold edges; Bambu Studio's repair fixes them. |

## Elegoo Saturn 4 Ultra 12k (resin)

| Part | Count | Height (mm) | Notes |
|---|---|---|---|
| L1-lich | 1 | 68.8 | Scaled 1.25x as the centrepiece. Hollow not needed. |
| F1 paladin, F2 dwarf cleric, F3 ranger, F4 sorceress | 4 | 48 / 30 / 38 / 38 | Adventurers on the causeway. Replace the ranger's bowstring with fishing line or wire. Thicken or pin thin blades and staffs if they snap (see leaf reviews). |
| K1/K2 skeletons | 5 | 33-42 | Four wading (cut at the waterline, sit on the water), one on the stair. |
| S1 priest statue, S3 leaning statue, S2 fallen statue a/b | 4 | 95 / 91 / 13 | S1 stands at the causeway; the fallen halves lie in the water. |
| X1-brazier | 4 | 22.5 | Two on the summit, two on the stair landings. Good spot for a tea light/LED. |
| R1-reeds | 54 | 29.4 | Print in a batch on the plate. |
| O1-crystal | 1 | 17.2 | Clear resin, 1.1 mm pin into the obelisk. |

Minis have 0-4 open edges (normal for the slicer). Use light supports and 0.05 mm layers.

## Known gaps (for a v2)

- The causeway has only its built-in culvert, not the extra arches in the concept.
- The mud banks read as gravel in the preview renders; paint will decide this.
- The leaning statue reads nearly upright.
- The reviewer thinks the concept camera may be front-left rather than front-right. Placement is mirrored-safe, so this only affects the hero shot.
- Tree moss is beaded (see above).

## Test plan

1. Print one tile (F1) and two clips. Check the clip fit and the water height against the causeway.
2. Print the paladin and one skeleton on resin. Check thin parts and how the wading cut sits on the tile.
3. Then print the ziggurat (the longest print, about 1.5-2 days) and the rest.
