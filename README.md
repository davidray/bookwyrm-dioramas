# bookwyrm-dioramas

Project text for David's layered dioramas: generator scripts, parameters, design notes, checkpoints and review notes, one folder per product under `projects/<slug>/`.

## Where things live

- **How to build a diorama:** the layered diorama skill in [davidray/bookwyrm-skills](https://github.com/davidray/bookwyrm-skills), `families/layered-diorama/SKILL.md`. Attach bookwyrm-skills to a build project beside this repo.
- **Saving and promoting a build:** `workshop/SKILL.md` in bookwyrm-skills. A build saves its files to The Hoard as a draft change set, and David promotes it there. Promotion sets the version (`v<N>`) and status.
- **Meshes, Blender files, renders and print files** live in The Hoard's store, never in this repo. `.gitignore` keeps them out.

## Locked versions already here

`projects/crossroads-inn/v2`, `isle-of-berk/v8`, `lichs-sunken-temple/v6` and `victorian-christmas-village/v14` and `v15` stay as they were locked: `piece.json`, `print/SHA256SUMS`, `print/parts.json` and the source notes. Their print files are in The Hoard (all 78 listed files, 75 distinct, checked by hash on 2026-11-16). New versions are not locked as folders here any more, so new versions have no `SHA256SUMS` and no `sources/files` step; the store records every file's hash.

The `piece.json` check in `.github/workflows` still runs over these folders, using `tools/check_piece_json.py`.
