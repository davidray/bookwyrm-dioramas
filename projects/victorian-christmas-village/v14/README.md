# Victorian Christmas village, v14

A snowy Victorian Christmas village. A one-piece church sits on a tiled base of 8 magnet-jointed tiles (840 x 420 mm), hollowed underneath for a puck light. Around it are an inn, a bakery, cottages and houses. A 160 mm Christmas tree, lamps, firs and figures go on top.

It was built with the scene workflow: a concept, element art, sculpt images, Meshy image-to-3D meshes, then Blender assembly and print engineering. v14 is the v12 print set with a new one-piece church. The church's underside is notched to sit on the v12 tiles, which David has already printed. A redone church is in progress and will become v15.

## Files

- `piece.json`: the library record for this version.
- `print/PRINT-AND-TEST.md`: what's in each 3MF, the printers, the magnet fitting steps and the test plan.
- `print/magnet-facts.json`: the magnet pocket positions for the 29 tile joints.
- `print/SHA256SUMS`: the hashes of the three locked 3MFs.
- `source/scene.json`: where each piece is placed in assembly v14.

**The 3MFs and renders are not in git**, because this repo ignores meshes. The locked set is on David's Mac in `~/code/bookwyrm-rpg-lantern-art/christmas-village-diorama/print-v14/` (three 3MFs, 359 MB). To check a copy, run `shasum -a 256 -c print/SHA256SUMS` from a folder that holds `print/*.3mf`. Tools, renders and the decision log are in the Claude project folder `christmas-village/`.

| File | Printer | Contents |
|---|---|---|
| `christmas-village-v12-base-tiles.3mf` | Bambu (FDM), white PLA | 8 tiles with magnet pockets |
| `christmas-village-v14-buildings.3mf` | Bambu (FDM), white PLA | One-piece church (106 x 154 x 217 mm), B3 house body and roof, bakery, inn, B1 and B6 cottages |
| `christmas-village-v12-props-figures.3mf` | Elegoo Saturn 4 Ultra 12K, resin | 10 objects, 12 prints (the lamp and fir twice each), including the 160 mm tree |

- **Claim level:** prototype. The base tiles have been printed, but the full assembly hasn't been printed yet.
- **Scene review:** the last cold review scored v4 at about 70% faithful to the concept. Later versions applied David's layout pins and the church changes, and weren't rescored.
- **Spend:** 1012 Meshy credits, $0.

## Known gaps

- The church is being redone as v15.
- No lithophane window panels yet.
- The props and figures haven't been test printed in resin.
