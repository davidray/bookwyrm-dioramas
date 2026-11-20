# Victorian Christmas village, v17

A snowy Victorian Christmas village. Eight magnet-jointed tiles make an 840 x 420 mm base. A one-piece stone church stands at the end of the ring of buildings, with its bell tower in front of the nave, lit by a puck light and a battery tea light. Around it are an inn, a bakery, a toy shop and cottages. A 160 mm Christmas tree, lamps, firs and figures go on top.

v17 is v16 with three changes Shannon asked for after seeing the printed village:

- **Bakery (B4): gables at both ends.** It had a gable at its chimney end and a hip at the other. The chimney-end gable (everything above 116 mm, just over the upper windows) was mirrored onto the hipped end. The mirrored chimney was then removed and the snowy ridge continued over where it stood. The walls, windows and footprint are unchanged.
- **Timber cottage (B6): a porch and a door.** The front lean-to's three blank plank walls were opened into a porch: two 4 x 4 mm posts at the old panel joints, a 2.5 mm deck, and a 15 x 25.5 mm plank door with frame, lintel, knob and step, centred on the house wall behind. The lean-to roof and end walls are unchanged.
- **Toy shop (B3): glue-on window frames.** The bow windows' glazing bars are too thin to print, so the shop windows came out open. Two new curved frames (1.2 mm bars, 4 x 4 panes, matching the original bar positions) are cut to the windows' measured curve and height, for resin, to glue into the printed shop.

All three are boolean edits of the existing meshes, with David's approval in the thread; no Meshy credits were spent. The church, inn, B1 cottage, tiles, props, figures and magnet positions are unchanged.

## Files

- `piece.json`: the library record for this version.
- `print/PRINT-AND-TEST.md`: what's in each 3MF, what changed, the printers, the tea light, the magnet fitting steps and the test plan.
- `print/magnet-facts.json`: the magnet pocket positions for the 29 tile joints. Unchanged since v12.
- `print/SHA256SUMS`: the hashes of the four locked 3MFs.
- `source/scene.json`: where each piece is placed (unchanged since v16 apart from the bakery's and cottage's file and note).

**The 3MFs and renders are not in git**, because this repo ignores meshes. The locked set is on David's Mac in `~/code/bookwyrm-rpg-lantern-art/christmas-village-diorama/print-v14/` (the folder name dates from v14). Use the four files listed in `print/SHA256SUMS`; earlier buildings files there are superseded. A before/after sheet is in `v17-preview/` in that folder.

| File | Printer | Contents |
|---|---|---|
| `christmas-village-v12-base-tiles.3mf` | Bambu (FDM), white PLA | 8 tiles with magnet pockets (already printed) |
| `christmas-village-v17-buildings.3mf` | Bambu H2D class (FDM), white PLA | One-piece church with lit tower (105 x 172 x 263 mm), B3 toy shop body and roof, bakery (v17), inn, B1 cottage, B6 cottage (v17) |
| `christmas-village-v17-window-frames.3mf` | Elegoo Saturn 4 Ultra 12K, resin | 2 curved bow window frames for the toy shop |
| `christmas-village-v12-props-figures.3mf` | Elegoo Saturn 4 Ultra 12K, resin | 10 objects, 12 prints (the lamp and fir twice each), including the 160 mm tree |

- **Claim level:** prototype. The village has been printed (v16 buildings). The v17 bakery, porch and window frames are checked digitally only.
- **Printing the church:** it needs more than 256 mm of build height. Slice it upright with supports touching the build plate only.
- **Spend:** 1041 Meshy credits, $0 (v17 used no credits).

## Known gaps

- The bakery's new gable has a plain smooth panel above the brick chimney breast where the chimney was removed, and faint seams where the ridge was continued; paint hides them.
- The porch's back wall is plain apart from the door.
- The window frames are sized from the model, not from the printed shop; dry-fit one first.
- The belfry glow from a single tea light at the base will be soft; painting the shaft white helps.
- No lithophane window panels yet.
- The stretched belfry and spire stones are taller than the stones elsewhere on the church.
