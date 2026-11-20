# Victorian Christmas village, v18

A snowy Victorian Christmas village. Eight magnet-jointed tiles make an 840 x 420 mm base. A one-piece stone church stands at the end of the ring of buildings, with its bell tower in front of the nave, lit by a puck light and a battery tea light. Around it are an inn, a bakery, a toy shop and cottages. A 160 mm Christmas tree, lamps, firs and figures go on top.

v18 is v17 (Shannon's changes) with David's review fixes:

- **Bakery (B4): stone gables with eaves and trim.** v17's gable faces (and the original chimney-end gable) were smooth snow on a vertical wall. Both are now cut back to stone, copied from the window-free part of the bakery's own wall, under a roof overhang with a bargeboard along each rake. The chimney breast is kept at the chimney end.
- **Timber cottage (B6): a finished, decorated porch.** Both porch ends are open with corner posts. The roof seams are buried under an irregular snow cover with a draped front lip and icicles. The back wall has half-timbering to match the cottage and two lit mullioned windows. It's decorated with a wreath on the door, garland swags with bows, and two small potted Christmas trees.

From v17: the bakery has gables at both ends (one chimney), the cottage's blank lean-to walls are a porch with a plank door, and the toy shop has glue-on resin frames for its bow windows. All edits are boolean edits of the existing meshes; no Meshy credits were spent.

## Files

- `piece.json`: the library record for this version.
- `print/PRINT-AND-TEST.md`: what's in each 3MF, what changed, the printers, the tea light, the magnet fitting steps and the test plan.
- `print/magnet-facts.json`: the magnet pocket positions for the 29 tile joints. Unchanged since v12.
- `print/SHA256SUMS`: the hashes of the four locked 3MFs.
- `source/scene.json`: where each piece is placed (unchanged since v16 apart from the bakery's and cottage's file and note).

**The 3MFs and renders are not in git**, because this repo ignores meshes. The locked set is on David's Mac in `~/code/bookwyrm-rpg-lantern-art/christmas-village-diorama/print-v14/` (the folder name dates from v14). Use the four files listed in `print/SHA256SUMS`; earlier buildings files there are superseded. Preview sheets are in `v17-preview/` and `v18-preview/` in that folder.

| File | Printer | Contents |
|---|---|---|
| `christmas-village-v12-base-tiles.3mf` | Bambu (FDM), white PLA | 8 tiles with magnet pockets (already printed) |
| `christmas-village-v18-buildings.3mf` | Bambu H2D class (FDM), white PLA | One-piece church with lit tower (105 x 172 x 263 mm), B3 toy shop body and roof, bakery (v18), inn, B1 cottage, B6 cottage (v18) |
| `christmas-village-v17-window-frames.3mf` (from v17) | Elegoo Saturn 4 Ultra 12K, resin | 2 curved bow window frames for the toy shop |
| `christmas-village-v12-props-figures.3mf` | Elegoo Saturn 4 Ultra 12K, resin | 10 objects, 12 prints (the lamp and fir twice each), including the 160 mm tree |

- **Claim level:** prototype. The village has been printed (v16 buildings). The v18 bakery and porch and the v17 window frames are checked digitally only.
- **Printing the church:** it needs more than 256 mm of build height. Slice it upright with supports touching the build plate only.
- **Spend:** 1041 Meshy credits, $0 (v17 and v18 used no credits).

## Known gaps

- The bakery's stone gables are tiled from one patch of wall, so faint vertical seams show between copies, and the ridge where the second chimney was removed has faint seams; paint hides them.
- The porch garland and the underside of the porch roof need slicer supports.
- The window frames are sized from the model, not from the printed shop; dry-fit one first.
- The belfry glow from a single tea light at the base will be soft; painting the shaft white helps.
- No lithophane window panels yet.
- The stretched belfry and spire stones are taller than the stones elsewhere on the church.
