# Christmas village, print set v20 (toy shop roof refit)

v20 is v19 with a smaller toy shop roof that nests on the body. Everything else is unchanged from v19.

- **Toy shop (B3) roof:** scaled to 0.907 x 0.827 x 0.78, now 122 x 97 x 98 mm. The eave sits on the wall top, a 1.8 mm locating ridge 4 mm deep drops inside the walls with 0.4 mm clearance, and the bottom is open inside the ridge so light from the shop reaches the attic and dormers. Print it upright, ridge down, with supports under the eaves and icicles.
- **Bakery (B4) and timber cottage (B6):** the v19 Meshy buildings.

This folder holds four 3MFs, split by printer:
- `christmas-village-v12-base-tiles.3mf`: the 8 tiles with magnet pockets (FDM), unchanged.
- `christmas-village-v20-buildings.3mf`: 7 objects (FDM, white PLA): the v16 church, the B3 toy shop body and v20 roof (`05-B3-roof-v20-nesting`), the v19 bakery, the inn, the B1 cottage and the v19 B6 cottage. The roof, bakery (`06-B4-bakery-v19-gables`) and cottage (`09-B6-cottage-v19-porch`) differ from v16. Slice the cottage with supports under the porch roof, garland and icicles. The church needs more than 256 mm of build height and supports touching the build plate, as in v16.
- `christmas-village-v17-window-frames.3mf` (unchanged from v17): the two toy shop bow window frames (resin). Print them upright on their bottom edge with light supports, or tilt them about 30° back. If a frame is tight in the opening, sand its ends; it should sit on the sill and touch the underside of the head.
- `christmas-village-v12-props-figures.3mf`: 10 objects, 12 pieces, resin, unchanged.

Sha-256: tiles `7f822c13…`, buildings `3fb897b5…6658a410`, window frames `68bc404c…7834`, props/figures `310a1df0…3ae5d`.

Test first: print the toy shop roof and check it drops onto the printed body and sits flat. Print one window frame and dry-fit it in the toy shop's left bow window before printing the second.

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
