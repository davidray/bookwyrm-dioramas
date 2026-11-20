# Victorian Christmas village, v19

A snowy Victorian Christmas village. Eight magnet-jointed tiles make an 840 x 420 mm base. A one-piece stone church stands at the end of the ring of buildings, with its bell tower in front of the nave, lit by a puck light and a battery tea light. Around it are an inn, a bakery, a toy shop and cottages. A 160 mm Christmas tree, lamps, firs and figures go on top.

v19 is v17 (Shannon's changes) with the bakery and timber cottage regenerated with Meshy, the same art, sculpt and image-to-3D pipeline the rest of the village was built with. A hand-edited v18 was reviewed and replaced by this version before it was locked.

- **Bakery (B4): gables at both ends.** New Meshy art from the original bakery art: a plain pitched slate roof with stone gables at both ends, green scalloped bargeboards and a finial on each gable, a scalloped trim along the front eave, and one brick chimney. Snow sits on the roof slopes only.
- **Timber cottage (B6): an open, decorated front porch.** New Meshy art from the original cottage art: the porch is open at both ends on oak posts, with a plank deck and step, a plank door with a wreath, a half-timbered back wall with two mullioned windows, garland swags with bows along the beam, two potted Christmas trees, and soft, uneven snow on both roofs. The stone chimney now stands on the right gable end.
- **Toy shop (B3):** the glue-on resin bow window frames from v17, unchanged.

Both new meshes are scaled to the old buildings' footprints (the bakery is 1.3 mm shorter, the cottage 14 mm lower) and their bases are trimmed flat to sit on the tiles.

## Files

- `piece.json`: the library record for this version.
- `print/PRINT-AND-TEST.md`: what's in each 3MF, what changed, the printers, the tea light, the magnet fitting steps and the test plan.
- `print/magnet-facts.json`: the magnet pocket positions for the 29 tile joints. Unchanged since v12.
- `print/SHA256SUMS`: the hashes of the four locked 3MFs.
- `source/scene.json`: where each piece is placed (unchanged since v16 apart from the bakery's and cottage's file, bounds and note).

**The 3MFs and renders are not in git**, because this repo ignores meshes. The locked set is on David's Mac in `~/code/bookwyrm-rpg-lantern-art/christmas-village-diorama/print-v14/` (the folder name dates from v14). Use the four files listed in `print/SHA256SUMS`; earlier buildings files there are superseded. Preview sheets are in `v17-preview/` and `v19-preview/` in that folder; the Meshy art, sculpt images and meshes are in `../v19-gen/`.

| File | Printer | Contents |
|---|---|---|
| `christmas-village-v12-base-tiles.3mf` | Bambu (FDM), white PLA | 8 tiles with magnet pockets (already printed) |
| `christmas-village-v19-buildings.3mf` | Bambu H2D class (FDM), white PLA | One-piece church with lit tower (105 x 172 x 263 mm), B3 toy shop body and roof, bakery (v19), inn, B1 cottage, B6 cottage (v19) |
| `christmas-village-v17-window-frames.3mf` (from v17) | Elegoo Saturn 4 Ultra 12K, resin | 2 curved bow window frames for the toy shop |
| `christmas-village-v12-props-figures.3mf` | Elegoo Saturn 4 Ultra 12K, resin | 10 objects, 12 prints (the lamp and fir twice each), including the 160 mm tree |

- **Claim level:** prototype. The village has been printed (v16 buildings). The v19 bakery and cottage and the v17 window frames are checked digitally only.
- **Printing the church:** it needs more than 256 mm of build height. Slice it upright with supports touching the build plate only.
- **Spend:** 1135 Meshy credits (v19 used 94: 4 art images, 2 sculpt images, 2 meshes).

## Known gaps

- The porch roof, garland and icicles overhang and need slicer supports.
- The cottage's back wall (the side Meshy didn't see in the art) is plain half-timbering with no windows.
- The window frames are sized from the model, not from the printed shop; dry-fit one first.
- The belfry glow from a single tea light at the base will be soft; painting the shaft white helps.
- No lithophane window panels yet.
- The stretched belfry and spire stones are taller than the stones elsewhere on the church.
