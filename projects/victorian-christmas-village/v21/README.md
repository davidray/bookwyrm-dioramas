# Victorian Christmas village, v21

A snowy Victorian Christmas village. Eight magnet-jointed tiles make an 840 x 420 mm base. A one-piece stone church stands at the end of the ring of buildings, with its bell tower in front of the nave, lit by a puck light and a battery tea light. Around it are an inn, a bakery, a toy shop and cottages. A 160 mm Christmas tree, lamps, firs and figures go on top.

v21 is v20 with the tile pads synced to the current buildings, from David's review of the whole-village render. The buildings are unchanged.

- **Church pad (tiles B1, B2, F1, F2):** the pads were cut for the v12 church. The one-piece church sat up to 4 mm onto snow on its right side and left up to 19 mm of bare pad showing on its left. The pad is now the church's footprint plus 0.6 mm, flat at 28.5 mm, and the leftover pad is filled with snow that rises from the church's walls.
- **Timber cottage pad (tile F4):** the v19 cottage ran past its pad at the front and sat on up to 5 mm of snow at one side. Its pad is recut and filled the same way.
- The other four buildings already fit their pads. Tiles F3, B3 and B4, the magnet pockets and every joint face are unchanged, so the five new tiles join the three printed ones.

From v20: the smaller toy shop roof that nests on the body. From v19: the Meshy bakery and timber cottage. From v17: glue-on resin frames for the toy shop bow windows.

## Files

- `piece.json`: the library record for this version.
- `print/PRINT-AND-TEST.md`: what's in each 3MF, what changed, the printers, the tea light, the magnet fitting steps and the test plan.
- `print/magnet-facts.json`: the magnet pocket positions for the 29 tile joints. Unchanged since v12.
- `print/SHA256SUMS`: the hashes of the four locked 3MFs.
- `source/scene.json`: where each piece is placed (since v16 the bakery, cottage and toy shop roof have new files, bounds and notes).

**The 3MFs and renders are not in git**, because this repo ignores meshes. The locked set is on David's Mac in `~/code/bookwyrm-rpg-lantern-art/christmas-village-diorama/print-v14/` (the folder name dates from v14). Use the four files listed in `print/SHA256SUMS`; earlier buildings files there are superseded. Preview sheets are in `v17-preview/` `v19-preview/` and `v20-preview/` and `v21-preview/` in that folder; the Meshy art, sculpt images and meshes are in `../v19-gen/`.

| File | Printer | Contents |
|---|---|---|
| `christmas-village-v21-base-tiles.3mf` | Bambu (FDM), white PLA | 8 tiles with magnet pockets; reprint F1, F2, B1, B2 and F4 (F3, B3 and B4 are the printed v12 tiles) |
| `christmas-village-v20-buildings.3mf` (from v20) | Bambu H2D class (FDM), white PLA | One-piece church with lit tower (105 x 172 x 263 mm), B3 toy shop body and roof (v20), bakery (v19), inn, B1 cottage, B6 cottage (v19) |
| `christmas-village-v17-window-frames.3mf` (from v17) | Elegoo Saturn 4 Ultra 12K, resin | 2 curved bow window frames for the toy shop |
| `christmas-village-v12-props-figures.3mf` | Elegoo Saturn 4 Ultra 12K, resin | 10 objects, 12 prints (the lamp and fir twice each), including the 160 mm tree |

- **Claim level:** prototype. The village has been printed (v16 buildings). The v19 bakery and cottage, the v20 toy shop roof and the v17 window frames are checked digitally only.
- **Printing the church:** it needs more than 256 mm of build height. Slice it upright with supports touching the build plate only.
- **Spend:** 1135 Meshy credits (v19 used 94: 4 art images, 2 sculpt images, 2 meshes; v20 and v21 used none).

## Known gaps

- The porch roof, garland and icicles overhang and need slicer supports.
- Print the toy shop roof upright with supports under the eaves; the locating ridge is on the build plate side. Dry-fit it on the printed body: if the ridge binds, sand its outer face.
- The cottage's back wall (the side Meshy didn't see in the art) is plain half-timbering with no windows.
- The window frames are sized from the model, not from the printed shop; dry-fit one first.
- The belfry glow from a single tea light at the base will be soft; painting the shaft white helps.
- No lithophane window panels yet.
- The stretched belfry and spire stones are taller than the stones elsewhere on the church.
