# Battle of Five Armies diorama: checkpoint

Slug `battle-of-five-armies` (kept for every version), kind `diorama`. Built with the layered-diorama skill (bookwyrm-skills `families/layered-diorama/SKILL.md`), saved to The Hoard as draft change sets through `workshop/SKILL.md`. David promotes; no draft is promoted unless he names it.

## Brief (David, 2026-11-16)

> A really complex fantasy battle scene involving five different armies - dwarves, men, elves, eagles, and goblins

Intended use: to sell.

## Decisions (agreed by David, 2026-11-17 00:26 UTC: "Agreed on all")

1. **Generic fantasy, not Middle-earth.** Selling rules out `ip: middle-earth` (The Hoard requires `personal-use-only` for any third-party ip, and Tolkien designs need a licence). Five original armies (mountain dwarves, human soldiers, wood elves, giant eagles, goblins), an original mountain-gate backdrop, no Tolkien names, characters or landmarks. Rights: design `ai-assisted`, ip `none`, licence `all-rights-reserved`. The slug stays; the title and listing drop the Tolkien name.
2. **Footprint 580 x 580 mm**, four 290 x 290 mm tiles (usable A2L bed), backdrop peak about 260 mm. Tiles on the A2L; anything over 256 mm tall on David's taller printer.
3. **About 15 mm figures as regiment blocks** of 6 to 10, 20 to 30 figures per army; eagles as 3 or 4 large birds in flight on rods. Tripo budget cap 700 credits.
4. **No electronics.** Fire, smoke and dust are sculpted and paintable.
5. **Sections:** four tiles joined with alignment tabs (male 4.0 mm dia x 4.0 mm, female 4.2 x 4.2 mm); regiments, eagles and backdrop are separate pieces in shaped seats. Whole scene approved as one sculpt before any split.

## Standing rules
- Decorative and sculpted pieces come from the 3D generator (Tripo), never hand-built in code; code only for structure, tabs and seats.
- No dowels. Generous clearance for any purchased part.

## Working files
- Mac: `~/code/bookwyrm-rpg-lantern-art/battle-of-five-armies/` (`tp.py` spend-guarded helper, run inside Blender; ledger `tripo_ledger.json`, CAP 700).
- `tools/`: `tp.py` (Tripo and image calls), `blockout.py` and `render_clay.py` (headless bpy). `elements/`: element register, layout reserves, sculpt-art prompts. `concept/prompts.json`: concept prompts.
- Project files: `battle-of-five-armies/` (concepts, review images).

## Status
- 2026-11-17 04:55 UTC: David picked concept A (Mountain Gate), the one that looks most like a Tolkien scene; decision 1 still applies, so the generated statues, gate and ruins are generic (no stilt lake-town, no named landmarks).
- Element register: 17 generated elements, 640 of 700 credits planned, 60 reserve; 21 regiment blocks placed (about 44 dwarves, 32 elves, 34 men, 75 goblins) and 4 eagles. Blockout v1 rendered. Sculpt art for every element done ($3.40 + $0.60 concepts).
- Pilot: A1 dwarf shield-wall generated (40 credits) to check 15 mm readability before the rest.
- 2026-11-17 05:25 UTC: all 17 leaves generated (Tripo v3.1, detailed except pines and smoke): 640 of 700 credits, no failures. Clay reviews all usable (eagle E1 carries a small rock perch to trim).
- Assembly: `tools/make_assembly.py <figure scale>` packs regiments into the four army zones; `tools/assemble.py` builds and renders the scene from decimated leaves (`tools/decimate.py`). 15 mm needs 142 regiment prints, 25 mm (scale 1.6) needs 61; recommended 25 mm, awaiting David. Assembly v3 (25 mm): left hill raised, goblins reach the front edge, eagles spread out and off the gate.
- 2026-11-17 12:41 UTC: David chose 25 mm figures (61 regiment prints). 13:00 UTC: he OK'd the recommended changes: added K1 battlefield-floor leaf (40 credits; 680 of 700 used), 10 copies tiled flush over the open ground; diving eagle's rock perch cut off at 10 mm (`tools/trim_below.py`). Assembly v4 posted for whole-scene sculpt approval.
