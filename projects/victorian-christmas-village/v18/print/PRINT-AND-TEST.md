# Christmas village, print set v18 (David's review of v17)

v18 is v17 with David's review fixes to the bakery and the timber cottage. The toy shop window frames, church, tiles, props, figures and magnets are unchanged.

- **Bakery (B4):** both gable faces were smooth snow, which can't cling to a vertical wall. They're now stone, copied from the bakery's own walls, set back under a roof overhang with a plain bargeboard along each rake. At the chimney end, the brick chimney breast stands proud of the stone.
- **Timber cottage (B6) porch:** both ends are open, with a 4 mm corner post at each front corner. The porch roof has an irregular snow cover with a draped front lip and a few icicles, replacing the straight, evenly spaced seams. The back wall has half-timbering (plates, studs, rails and braces) and two mullioned windows, cut through so they glow. It's decorated with a wreath on the door, garland swags with bows along the front beam, and a small potted Christmas tree each side of the door.

This folder holds four 3MFs, split by printer:
- `christmas-village-v12-base-tiles.3mf`: the 8 tiles with magnet pockets (FDM), unchanged.
- `christmas-village-v18-buildings.3mf`: 7 objects (FDM, white PLA): the v16 church, the B3 toy shop body and roof, the v18 bakery, the inn, the B1 cottage and the v18 B6 cottage. Only the bakery (`06-B4-bakery-v18-stone-gables`) and cottage (`09-B6-cottage-v18-porch`) differ from v16. The porch garland hangs under the porch roof, so slice the cottage with supports under the porch ceiling and garland. The church needs more than 256 mm of build height and supports touching the build plate, as in v16.
- `christmas-village-v17-window-frames.3mf` (unchanged from v17): the two toy shop bow window frames (resin). Print them upright on their bottom edge with light supports, or tilt them about 30° back. If a frame is tight in the opening, sand its ends; it should sit on the sill and touch the underside of the head.
- `christmas-village-v12-props-figures.3mf`: 10 objects, 12 pieces, resin, unchanged.

Sha-256: tiles `7f822c13…`, buildings `c2979f05…145e75`, window frames `68bc404c…7834`, props/figures `310a1df0…3ae5d`.

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
