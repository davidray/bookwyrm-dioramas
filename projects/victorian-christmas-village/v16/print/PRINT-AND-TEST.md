# Christmas village, print set v16 (locked, church with lit tower)

v16 is the v15 print set with the church tower hollowed so a battery tea light can light it. Earlier buildings files (v14, v15, v15b, v15c) are superseded. The church is now one piece, generated from the church art. It replaces the old nave, tower and spire, which didn't fit together. Its underside is notched to sit on the v12 tiles you've already printed, so the tiles are unchanged. The magnet notes below still apply. The locked v11 release (`../LOCK-v11.md`) is kept for reference.

This folder holds the three 3MFs, split by printer:
- `christmas-village-v12-base-tiles.3mf`: the 8 tiles with magnet pockets (FDM). They're the same tiles you've already printed.
- `christmas-village-v16-buildings.3mf`: 7 objects. That's the v16 church (105 × 172 × 263 mm: the tower stands in front of the nave, with a taller belfry and spire; it needs more than 256 mm of build height, e.g. a Bambu H2D), the B3 house (body and roof), the bakery, the inn, and the B1 and B6 cottages (FDM). The church's underside has shallow notches where it sits over the snow drift, so slice it with supports touching the build plate. It's hollow under the nave so a puck light fits inside, and its tower is hollow (a 28 x 28 mm shaft up to the belfry) with the lancet window and the belfry louvre slits cut through. The 1 mm slits are short bridges and need no support.
- `christmas-village-v12-props-figures.3mf`: 10 objects, 12 pieces (the lamp and fir twice each), meant for resin. Everything fits a Saturn 4 Ultra 12K, including the 160 mm tree. Hollow and drain the tree, lamps and firs.

Sha-256: tiles `7f822c13…`, buildings `5a67523e…6e980`, props/figures `310a1df0…3ae5d`.

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
