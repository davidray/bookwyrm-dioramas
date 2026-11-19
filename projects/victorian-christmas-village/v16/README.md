# Victorian Christmas village, v16

A snowy Victorian Christmas village. Eight magnet-jointed tiles make an 840 x 420 mm base. A one-piece stone church stands at the end of the ring of buildings, with its bell tower in front of the nave. It's hollowed underneath for a puck light, and its tower is hollow so a battery tea light lights it. Around it are an inn, a bakery, cottages and houses. A 160 mm Christmas tree, lamps, firs and figures go on top.

v16 is v15 with one change: David wanted to light the church tower with simple battery tea lights.

- A 28 x 28 mm shaft runs up inside the tower from the puck-light cavity (ceiling at 73 mm) to 184 mm, with a 45° pointed ceiling to 198 mm, so it prints upright without internal supports.
- The lancet window above the door is cut through, and each of the four belfry louvres has seven 1 mm slits, one under each slat, so light leaks out in bars.
- The thinnest wall is about 2.8 mm, behind the louvres.
- A 38-40 mm tea light is wider than the tower, so it stands on the tile inside the nave cavity, under the back half of the tower (about 52 mm behind the front edge of the steps, on the church's centre line), with about 6 mm clearance all round.
- Everything below 65 mm is identical to v15c, so the footprint and notches still fit the printed v12 tiles. The other six buildings, the tiles, props, figures and magnet positions are unchanged.
- The cut is a boolean into the generated church mesh (interior, window and louvre gaps only), done with David's approval; the sculpted surface is otherwise untouched.

## Files

- `piece.json`: the library record for this version.
- `print/PRINT-AND-TEST.md`: what's in each 3MF, the printers, the tea light, the magnet fitting steps and the test plan.
- `print/magnet-facts.json`: the magnet pocket positions for the 29 tile joints. Unchanged since v12.
- `print/SHA256SUMS`: the hashes of the three locked 3MFs.
- `source/scene.json`: where each piece is placed (unchanged since v15 apart from the church's file and note).

**The 3MFs and renders are not in git**, because this repo ignores meshes. The locked set is on David's Mac in `~/code/bookwyrm-rpg-lantern-art/christmas-village-diorama/print-v14/` (the folder name dates from v14). Use the three files listed in `print/SHA256SUMS`; the v14, v15, v15b and v15c buildings files there are superseded. Tower previews (cutaway and night render) are in `church-v16-led-preview/` in that folder.

| File | Printer | Contents |
|---|---|---|
| `christmas-village-v12-base-tiles.3mf` | Bambu (FDM), white PLA | 8 tiles with magnet pockets (already printed) |
| `christmas-village-v16-buildings.3mf` | Bambu H2D class (FDM), white PLA | One-piece church with lit tower (105 x 172 x 263 mm), B3 house body and roof, bakery, inn, B1 and B6 cottages |
| `christmas-village-v12-props-figures.3mf` | Elegoo Saturn 4 Ultra 12K, resin | 10 objects, 12 prints (the lamp and fir twice each), including the 160 mm tree |

- **Claim level:** prototype. The base tiles have been printed. The church and its tower lighting are checked digitally only.
- **Printing the church:** it needs more than 256 mm of build height. Slice it upright with supports touching the build plate only.
- **Spend:** 1041 Meshy credits, $0 (v16 used no credits).

## Known gaps

- The belfry glow from a single tea light at the base will be soft; painting the shaft white helps. Not yet tested in a print.
- No lithophane window panels yet.
- The props and figures haven't been test printed in resin.
- The stretched belfry and spire stones are taller than the stones elsewhere on the church.
