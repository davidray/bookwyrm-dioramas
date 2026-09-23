# Bookwyrm Skills and Workflows

A shared home for how Bookwyrm work gets done: reusable skills, supporting instructions, practical tools, and lessons learned across projects.

The repository began with the layered diorama workflow and retains the `bookwyrm-dioramas` repository name. Its scope can grow to include other Bookwyrm-related skills and the resources they share.

## Current contents

- [Layered Diorama skill](skills/layered-diorama/SKILL.md): develop 3D dioramas from concept art through element breakdown, bottom-up construction, component development, integration, and print engineering.
- [Diorama lessons log](skills/layered-diorama/references/lessons.md): observations from the first Smaug/Dale attempt, the layered Dale restart, and Moria, including evidence and remaining uncertainties.
- [Working records](skills/layered-diorama/references/working-records.md): checkpoints, attempt boundaries, focused-reference requests, and new lesson entries.
- [Payload management](skills/layered-diorama/references/payload-management.md): compact visual reviews, bounded tool output, and recovery from oversized requests.
- [Mounting points](skills/layered-diorama/references/mounting-points.md): shaped receiving supports derived from any object’s contact geometry, feature relief, assembly clearance, and a historical Smaug example.
- [Fabrication and lighting](skills/layered-diorama/references/fabrication-and-lighting.md): representative physical tests, protected interfaces, local repairs, export/slicer validation, and serviceable lighting.

The diorama skill is a working draft. It includes user-reported local print/fit successes alongside unresolved mesh, full-assembly, strength, and lighting questions. These local results do not establish complete diorama print readiness. Storing a skill here does not install it automatically.

## Organization

Only `skills/` exists today. Add other directories when there is concrete content for them; empty placeholders are unnecessary.

| Directory | Purpose |
| --- | --- |
| `skills/` | Individual skills, each in a named folder with a `SKILL.md` entry point and its supporting resources. |
| `templates/` | Formats shared by multiple skills, such as project briefs, checkpoints, review records, and handoffs. |
| `scripts/` | Shared utilities for validation, contact sheets, file checks, and other repeated tasks. |
| `docs/` | Cross-project principles, workflow explanations, and repository maintenance guidance. |
| `examples/` | Small, curated examples of useful inputs and outputs, without large project assets. |
| `evaluations/` | Representative tasks and review criteria for checking whether skills produce the intended behavior. |

Keep resources used by one skill inside that skill's folder. Move a resource into a shared directory only when multiple skills actually use it, and update their references. Avoid maintaining duplicate copies.

## What belongs here

Include reusable instructions, distilled lessons, supporting reference documents, small examples, and utilities that improve repeated work. Record the scope and evidence behind a lesson, and distinguish observed results from assumptions or practices still being tested.

Keep artwork, models, renders, generated project outputs, credentials, raw audits, and individual project histories with their original projects. Project-specific scripts also stay there unless deliberately adapted into reusable utilities. Carry useful technical learning across projects while keeping design decisions tied to their active project and approved references.

Local source paths in the diorama lessons log identify historical evidence outside this repository. They are provenance notes, not repository links or required runtime files.

## Maintaining the collection

- Give each skill a clear purpose and scope. Keep its main instructions concise and place detailed supporting material alongside it.
- Add or revise guidance when actual work reveals a useful lesson. Preserve its evidence and limitations instead of turning every local preference into a universal rule.
- When changing files, check relative links and applicable skill metadata. Run relevant utilities or evaluations when their behavior changes.
- Review the staged files before committing so unrelated project assets and generated outputs do not enter the repository.
