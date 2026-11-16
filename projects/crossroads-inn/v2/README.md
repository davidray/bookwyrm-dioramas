# Crossroads Inn, v2

A fantasy waystation on a cobbled crossroads at the edge of the wilds: a timber-framed inn, a leaning wizard's tower with an observatory dome, an open forge, a cage wagon with a removable owl-beaked bear, a well, quest board, signpost and two oaks, with five 32 mm adventurers, a pony and small props. Original D&D-themed design (concept B of the D&D trio), built with the scene workflow: Tripo image-to-model meshes for 14 generated elements, Blender assembly and print engineering.

`v2` is the version imported into the library as `crossroads-inn` revision 2. It changes only the resin group from v1: the cage wagon is now a body plus a lift-off cage roof, and the cage floor has a 20 mm base socket, so the beast can be taken out or swapped.

## Files

- `piece.json`: the library record for this version.
- `print/parts.json`: every part inside the three 3MFs, with printer, count and size.
- `print/SHA256SUMS`: hashes of the reviewed 3MF set.
- `source/library-seed.json`: the mapping used to import it into the library.

**3MFs and renders are not in git** (this repo ignores meshes and images). The reviewed set lives on David's Mac in `~/code/bookwyrm-rpg-lantern-art/dnd-crossroads-inn/`: the ground tiles and A1 buildings in `print-v1/` (unchanged since v1), the resin group in `print-v2/`. Check a copy with `shasum -a 256 -c print/SHA256SUMS` from a folder holding the three files under `print/`.

**Claim level:** digitally validated only. Nothing has been test printed.
**Footprint:** 440 x 300 mm base (4 magnet-jointed tiles of 220 x 150), about 242 mm tall to the tower top.
**Spend:** 540 of 580 Tripo credits (14 meshes), $3.00 of OpenAI images. 40 credits unused. The v2 wagon split was geometric and cost nothing.

## Bambu A1 (PLA, 0.4 nozzle)

| Part | Size (mm) | Notes |
|---|---|---|
| Ground tiles F1, F2, B1, B2 | 220 x 150 x 15 | 0.12 mm layers for the cobbles. 16 magnets, 6 x 2 mm, in the joint-face pockets (4 per joint). Check polarity before gluing. |
| B1 inn | 123 x 137 x 190 | Tree supports under the porch roofs and eaves. |
| B2 wizard's tower | 134 x 96 x 230 | Supports under the balcony ring and telescope. |
| B3 forge (88 %) | 154 x 99 x 92 | Open front: supports under the roof beams. |
| T1 oak x 2 (80 % and 72 %) | 150 x 93 x 160, 135 x 83 x 144 | Organic tree supports. Could go to resin for crisper leaves (hollow it). |
| Q2 well | 40 x 36 x 48 | Supports under the roof. |

## Elegoo Saturn 4 Ultra 12K (resin)

| Part | Size (mm) | Notes |
|---|---|---|
| F1-F5 adventurers | 30-42 tall | Dwarf fighter, halfling bard, tiefling warlock, paladin, elf wizard. Tilt 30-45 degrees, light supports. |
| C2 pony | 39 x 26 x 34 | Pulls the wagon. |
| W1 cage wagon body | 124 x 48 x 62 | Cage floor has a 20.6 mm round socket, 0.8 mm deep. |
| W1 cage roof | 26 x 28 x 5.5 | Lifts off; a 0.8 mm skirt drops inside the bars to locate it. No glue. |
| C1 owl-beaked bear (58 %) | 19 mm base, 20 tall | Sits in the socket. Any beast on a 20 mm base, under 26 mm tall and through the 22.6 x 21.6 roof opening, fits. |
| Quest board, signpost, barrels (x2), crates, inn sign | small | Inn sign glues to the inn's front-right corner post, about 70 mm up. |

## Known gaps (for a v3)

- The inn's ground floor is soft in detail compared with the upper storeys.
- The forge roof has a small step gap where two roof planes meet.
- Check that the cage roof skirt clears the bars before painting.

## Test plan

1. Print one ground tile pair and test magnet polarity and joint fit.
2. Print the wagon body, cage roof and bear on resin. Check that the roof lifts on and off and the bear seats in the socket.
3. Print a figure and check that thin parts survive.
4. Then the buildings (tower is the longest print) and the rest.
