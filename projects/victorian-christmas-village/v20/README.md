# Victorian Christmas village, v20

A snowy Victorian Christmas village. Eight magnet-jointed tiles make an 840 x 420 mm base. A one-piece stone church stands at the end of the ring of buildings, with its bell tower in front of the nave, lit by a puck light and a battery tea light. Around it are an inn, a bakery, a toy shop and cottages. A 160 mm Christmas tree, lamps, firs and figures go on top.

v20 is v19 with a refitted toy shop roof, from David's review of the whole-village render:

- **Toy shop (B3) roof: smaller, and it nests on the body.** The roof was as tall as the building and overhung it by 10 to 26 mm. It's now scaled to 0.907 wide, 0.827 deep and 0.78 tall, so it overhangs the walls by about 6 mm at the sides, 5 mm at the back and 8 mm at the front, and stands 98 mm tall instead of 126 mm. Its eave sits flat on the wall top. A 1.8 mm locating ridge, 4 mm deep, hangs from the underside just inside the walls (0.4 mm clearance), so the roof drops into place and can't slide. The solid plate that closed the bottom of the roof is cut open inside the ridge, so light from the lower floors shines up into the attic and out of the dormers.

From v19: the bakery and timber cottage were regenerated with Meshy (stone gables at both ends with scalloped bargeboards; an open-ended decorated porch). From v17: glue-on resin frames for the toy shop bow windows.

## Files

- `piece.json`: the library record for this version.
- `print/PRINT-AND-TEST.md`: what's in each 3MF, what changed, the printers, the tea light, the magnet fitting steps and the test plan.
- `print/magnet-facts.json`: the magnet pocket positions for the 29 tile joints. Unchanged since v12.
- `print/SHA256SUMS`: the hashes of the four locked 3MFs.
- `source/scene.json`: where each piece is placed (since v16 the bakery, cottage and toy shop roof have new files, bounds and notes).

**The 3MFs and renders are not in git**, because this repo ignores meshes. The locked set is on David's Mac in `~/code/bookwyrm-rpg-lantern-art/christmas-village-diorama/print-v14/` (the folder name dates from v14). Use the four files listed in `print/SHA256SUMS`; earlier buildings files there are superseded. Preview sheets are in `v17-preview/` `v19-preview/` and `v20-preview/` in that folder; the Meshy art, sculpt images and meshes are in `../v19-gen/`.

| File | Printer | Contents |
|---|---|---|
| `christmas-village-v12-base-tiles.3mf` | Bambu (FDM), white PLA | 8 tiles with magnet pockets (already printed) |
| `christmas-village-v20-buildings.3mf` | Bambu H2D class (FDM), white PLA | One-piece church with lit tower (105 x 172 x 263 mm), B3 toy shop body and roof (v20), bakery (v19), inn, B1 cottage, B6 cottage (v19) |
| `christmas-village-v17-window-frames.3mf` (from v17) | Elegoo Saturn 4 Ultra 12K, resin | 2 curved bow window frames for the toy shop |
| `christmas-village-v12-props-figures.3mf` | Elegoo Saturn 4 Ultra 12K, resin | 10 objects, 12 prints (the lamp and fir twice each), including the 160 mm tree |

- **Claim level:** prototype. The village has been printed (v16 buildings). The v19 bakery and cottage, the v20 toy shop roof and the v17 window frames are checked digitally only.
- **Printing the church:** it needs more than 256 mm of build height. Slice it upright with supports touching the build plate only.
- **Spend:** 1135 Meshy credits (v19 used 94: 4 art images, 2 sculpt images, 2 meshes; v20 used none).

## Known gaps

- The porch roof, garland and icicles overhang and need slicer supports.
- Print the toy shop roof upright with supports under the eaves; the locating ridge is on the build plate side. Dry-fit it on the printed body: if the ridge binds, sand its outer face.
- The cottage's back wall (the side Meshy didn't see in the art) is plain half-timbering with no windows.
- The window frames are sized from the model, not from the printed shop; dry-fit one first.
- The belfry glow from a single tea light at the base will be soft; painting the shaft white helps.
- No lithophane window panels yet.
- The stretched belfry and spire stones are taller than the stones elsewhere on the church.
