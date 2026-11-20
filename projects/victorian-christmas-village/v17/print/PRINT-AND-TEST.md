# Christmas village, print set v17 (Shannon's changes)

v17 is the v16 print set with three changes Shannon asked for. Everything else (church, tiles, props, figures, magnets) is unchanged, so only the changed pieces need printing.

- **Bakery (B4):** the hipped end is now a gable, so it has gables at both ends. Only the roof above 116 mm changed; it still has its one chimney.
- **Timber cottage (B6):** the blank plank walls of the front lean-to are now an open porch: two posts, a deck, and a plank door with a frame, lintel, knob and step on the house wall. The lean-to roof and its end walls are unchanged. The posts are 4 x 4 mm and 31.5 mm tall.
- **Toy shop (B3) window frames:** two curved glue-on frames (33 x 10 x 38 mm each, 1.2 mm bars, 4 x 4 panes matching the model's original glazing bars) for the bow windows, whose bars didn't print. They sit on the window sill just outside the old bar line and are glued at the sill and head.

This folder holds four 3MFs, split by printer:
- `christmas-village-v12-base-tiles.3mf`: the 8 tiles with magnet pockets (FDM), unchanged.
- `christmas-village-v17-buildings.3mf`: 7 objects (FDM, white PLA): the v16 church, the B3 toy shop body and roof, the v17 bakery, the inn, the B1 cottage and the v17 B6 cottage. Only the bakery (`06-B4-bakery-v17-gable-ends`) and cottage (`09-B6-cottage-v17-porch`) differ from v16. The church needs more than 256 mm of build height and supports touching the build plate, as in v16.
- `christmas-village-v17-window-frames.3mf`: the two toy shop bow window frames (resin). Print them upright on their bottom edge with light supports, or tilt them about 30° back. If a frame is tight in the opening, sand its ends; it should sit on the sill and touch the underside of the head.
- `christmas-village-v12-props-figures.3mf`: 10 objects, 12 pieces, resin, unchanged.

Sha-256: tiles `7f822c13…`, buildings `c5d8da8e…139ef`, window frames `68bc404c…7834`, props/figures `310a1df0…3ae5d`.

Test first: print one window frame and dry-fit it in the toy shop's left bow window before printing the second.

## Tea light

- Use a standard battery LED tea light (about 38-40 mm across). It's wider than the tower, so it stands on the tile inside the nave cavity, centred under the back half of the tower: about 52 mm behind the front edge of the steps, on the church's centre line. There's about 6 mm of clearance all round. Lift the church off to switch it on.
- The lancet window glows strongly; the belfry slits give a softer glow. Paint the inside of the shaft white (pour in and drain) to brighten them.

## Magnets

- **What to buy:** 58 disc magnets, 10 mm × 2 mm (N35 or stronger), plus a little superglue or epoxy.
- **Pockets:** 29 joints, each with one pocket on each tile. The pockets are 10.4 mm wide and 2.2 mm deep, set into the vertical joint faces with their centres 9 mm above the underside. Positions are listed in `../G1-ground-v12/magnet-facts.json`.
- **Polarity:** put the tiles in their layout first: F1–F4 along the front, left to right, then B1–B4 behind them. Then fit one joint at a time.
  1. Glue a magnet into one tile's pocket.
  2. Before gluing the matching magnet, offer it up to the first one so that they attract, and mark its outward face.
  3. Glue it into the facing pocket with the marked face out.
- **Glue tip:** the magnet should sit flush or very slightly below the face. If a magnet stands proud, the tiles won't close.
- **Print orientation:** print the tiles flat, as in the file. The pockets are small horizontal holes and print without supports.

Test first: print F1 and F2, fit the three magnets on their shared joint, and check the fit and pull before printing the other six tiles. If the magnets are loose, glue them. If they won't go in, add 0.1–0.2 mm of XY hole compensation in the slicer.
