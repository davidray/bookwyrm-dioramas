# Victorian Christmas village, v15

A snowy Victorian Christmas village. Eight magnet-jointed tiles make an 840 x 420 mm base. A one-piece stone church stands at the end of the ring of buildings, with its bell tower in front of the nave. It's hollowed underneath for a puck light. Around it are an inn, a bakery, cottages and houses. A 160 mm Christmas tree, lamps, firs and figures go on top.

It was built with the scene workflow: a concept, element art, sculpt images, Meshy image-to-3D meshes, then Blender assembly and print engineering.

v15 is the v12 print set with a new church, which replaces v14's church. David wanted it bigger, closer to the original two-part church (272 mm), and still sitting on the v12 tiles he has already printed.

- The new church art puts the tower in front of a narrower nave, matching the original church's flat pads on the tiles. It was generated as one mesh (29 credits).
- The church is scaled to 0.9 and its snow apron is trimmed to the walls plus 3 mm. It's hollowed with a 82 x 146 mm cavity under the nave.
- After David's pins, the belfry and spire were stretched taller: +10 mm in v15b, then +4 mm above and +4 mm below the belfry window in v15c. The church is now 105 x 172 x 263 mm.
- Its underside is notched to the printed tiles' snow, with 0.3 mm clearance. 87% of the base sits on the old flat pad, and the notches are up to 4 mm deep. It's 4.4 mm from the neighbouring pads and 15.5 mm from the road.

## Files

- `piece.json`: the library record for this version.
- `print/PRINT-AND-TEST.md`: what's in each 3MF, the printers, the magnet fitting steps and the test plan.
- `print/magnet-facts.json`: the magnet pocket positions for the 29 tile joints. These are unchanged since v12.
- `print/SHA256SUMS`: the hashes of the three locked 3MFs.
- `source/scene.json`: where each piece is placed in assembly v15.

**The 3MFs and renders are not in git**, because this repo ignores meshes. The locked set is on David's Mac in `~/code/bookwyrm-rpg-lantern-art/christmas-village-diorama/print-v14/`. That folder name dates from v14. Use the three files listed in `print/SHA256SUMS`, and ignore the superseded v14, v15 and v15b buildings files. To check a copy, run `shasum -a 256 -c print/SHA256SUMS` from a folder that holds `print/*.3mf`. Renders (`assembly-v15/`) and the decision log are in the Claude project folder `christmas-village/`.

| File | Printer | Contents |
|---|---|---|
| `christmas-village-v12-base-tiles.3mf` | Bambu (FDM), white PLA | 8 tiles with magnet pockets (already printed) |
| `christmas-village-v15c-buildings.3mf` | Bambu H2D class (FDM), white PLA | One-piece church (105 x 172 x 263 mm), B3 house body and roof, bakery, inn, B1 and B6 cottages |
| `christmas-village-v12-props-figures.3mf` | Elegoo Saturn 4 Ultra 12K, resin | 10 objects, 12 prints (the lamp and fir twice each), including the 160 mm tree |

- **Claim level:** prototype. The base tiles have been printed. The church fit on them is checked digitally, against a heightfield that matches the printed tiles' 3MF exactly, but hasn't been printed.
- **Printing the church:** it needs more than 256 mm of build height. Slice it with supports touching the build plate, because the notches under the base overhang slightly.
- **Spend:** 1041 Meshy credits, $0.

## Known gaps

- No lithophane window panels yet.
- The props and figures haven't been test printed in resin.
- The stretched belfry and spire stones are taller than the stones elsewhere on the church.
