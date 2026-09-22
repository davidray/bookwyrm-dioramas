# Diorama lessons — living evidence log

Collected 2026-09-22. This records existing project notes and selected conversation reviews; no meshes were regenerated, rerendered, or reaudited for this draft. The first attempt includes its original and V2 revisions. The other two attempts are the layered Dale restart and Moria, rather than three revisions of Dale.

Evidence labeled “local source” names a path relative to the original Dioramas workspace. Those project files, artwork, models, and task histories are intentionally not included in this repository. The observations and their limits are summarized here so the skill remains useful independently; source paths are provenance identifiers, not repository links or runtime dependencies. Read the active project checkpoint when resuming a build; this dated log is not an alternative active-state tracker.

## Where we stand

| Attempt | Evidence so far | Limit of the conclusion |
| --- | --- | --- |
| First Smaug/Dale build, including V2 | User describes it as a total failure. Recorded accuracy review found major composition, anatomy, and shape-language problems despite added detail and a fused manifold export. | Its technical checks are historical evidence of mesh properties, not evidence of artistic success or a physical print. |
| Layered Dale (`v3_layered`) | Terrain and village were developed separately; village edits preserved building geometry. Wing-armed dragon image and placement were accepted. Local reconstruction and surface cleanup produced usable candidates. | Dragon thickness/supports and complete assembly remain unqualified; latest turbulent fire is awaiting review. |
| Layered Moria (`moria_layered`) | Environment survived many local passes and replacement of both characters. User liked the new film-inspired character direction and authorized cleanup/fitting. | Current cleaned/fitted scene awaits review. Manufacturing and physical illumination remain unresolved. |

The user's present assessment is that the layered approach is working well. The narrower evidence supports controllable iteration, preservation, and better visual direction; it does not yet establish a finished fabrication pipeline.

## L01 — More detail cannot repair the wrong structure

**Observation:** The first Dale revision added scales, shingles, masonry, and surface relief, yet the dragon remained tubular, wings presented as broad fans, houses climbed too high, and the mountain read as narrow crystalline spires. The accuracy review identified these as larger errors than texture.

**Changed practice:** Review major masses, anatomy, silhouette, proportions, and component relationships before detailing. Diagnose whether a defect is geometry or viewpoint; a camera change cannot repair misplaced wing joints.

**Evidence:** Accuracy review (local source: `ACCURACY_REVIEW_V2.md`), especially overall judgment and correction order. Historical print notes (local source: `PRINT_NOTES_V2.md`) record successful topology/import checks alongside untested physical printing.

**Confidence:** Strong case-supported lesson. The review diagnoses V2; the user's total-failure assessment covers the first attempt more broadly.

## L02 — Layering contains the cost of a wrong turn

**Observation:** Dale's village revision preserved house bodies, roofs, terrain, and cameras while changing the dry ground, lane, and surface differentiation. Moria could replace both figures while retaining its developed environment. Saved/reopened fitting checks recorded preservation of 661 source objects.

**Changed practice:** Keep independently editable collections and source revisions. Identify the scope of an edit and compare protected geometry and scene properties afterward. Rebuild a rejected component without rebuilding the whole scene.

**Evidence:** Village revision 2 (local source: `v3_layered/village_r2/README.md`), Moria character restart (local source: `moria_layered/character_restart/README.md`), Moria checkpoint (local source: `moria_layered/CHECKPOINT.md`).

**Confidence:** Repeated technical evidence for preservation; a preserved environment does not by itself make a new character successful.

## L03 — Bottom-up needs a whole-scene reserve plan

**Observation:** Both layered starts kept simple reserves for later figures and effects. Moria's bridge then fitted its landings to the terrain and adjusted the deck height; figure reserves followed the new surface. Dale's mountain left shelves for the settlement.

**Changed practice:** Block out the complete composition early, then develop dependent elements from their support surfaces upward. Preserve room for late elements and interfaces. Clearly label placeholders so they cannot be mistaken for final sculpture.

**Evidence:** Dale layered start (local source: `v3_layered/README.md`), Moria foundation (local source: `moria_layered/stage1/README.md`), Moria bridge (local source: `moria_layered/stage2/README.md`).

**Confidence:** Promising repeated workflow; neither final assembly has been physically tested.

## L04 — Large and medium forms matter more than indiscriminate roughness

**Observation:** Dale's first layered mountain still had triangular slopes and weak cliffs. Revision 2 introduced unequal explicit masses, recesses, broken planes, and shelves while reducing fine displacement. Moria used selective stone wear and protected occupied paving and structural surfaces.

**Changed practice:** Build hierarchical form and purposeful variation. Keep quiet areas around focal subjects. Use surface damage where it clarifies material and history, not as uniform noise.

**Evidence:** Mountain revision 2 (local source: `v3_layered/mountain_r2/README.md`), Moria selective stone wear (local source: `moria_layered/stage9/README.md`).

**Confidence:** Documented visual-development improvements, not a universal recipe for every geology or style.

## L05 — Choose the construction method by the subject

**Observation:** Repeated procedural character refinements did not satisfy the eventual realism target. Both Moria character styles were rejected. A restart used film-design references, isolated AI studies, and local image-to-3D; the user liked the new direction. Dale also moved to an accepted isolated dragon study and reconstruction.

**Changed practice:** Consider reference-driven organic modeling early. If likeness and anatomy remain fundamentally wrong, change that component's source or method instead of adding more procedural detail. Procedural control remains useful for architecture, environment, fitting, and targeted edits.

**Evidence:** Moria restart (local source: `moria_layered/character_restart/README.md`), Dragon reconstruction (local source: `v3_layered/dragon_r2/reconstruction/README.md`).

**Confidence:** Promising route for these subjects, not proof that all procedural characters fail or that image-to-3D yields finished sculpture. Current cleanup/fitting is still under review.

## L06 — Review anatomy explicitly, including hidden attachments

**Observation:** Superseded dragon prompts/candidates had extra walking limbs. User clarification established that the wings ARE the arms: two wing-arms plus two hind legs. A separate shoulder stump must not become a new limb. Moria's old Balrog hands looked twisted backward even after earlier geometry checks passed.

**Changed practice:** Record subject-specific anatomy and inspect count, attachment, handedness, palms, thumbs, grips, and pose from multiple angles before decoration. A topology pass cannot validate anatomy.

**Evidence:** Workspace instructions (local source: `AGENTS.md`), Dale checkpoint (local source: `v3_layered/CHECKPOINT.md`), Historical Balrog hand correction (local source: `moria_layered/stage15/README.md`).

**Confidence:** Direct user corrections. The hand-correction record is diagnostic history; that old character style is superseded. Wing-arm anatomy is this dragon's requirement, not a rule for every creature.

## L07 — Source authority and approval have scope

**Observation:** Moria's original concept still governs environment composition, while later film references govern character style. The user replaced a lit lithophane idea with an opaque, unlit backdrop. Dale's accepted dragon image is not a mesh, and accepted placement does not qualify its mounts. Intermediate praise of fire did not approve roof-rooted placement after the ground-route correction.

**Changed practice:** Track which reference governs which property. Record acceptance separately for reference, shape, placement, and engineering. A new clarification supersedes an old assumption; art-sheet annotations do not automatically become requirements.

**Evidence:** Moria overview (local source: `moria_layered/README.md`), Moria restart (local source: `moria_layered/character_restart/README.md`), Dale checkpoint (local source: `v3_layered/CHECKPOINT.md`).

**Confidence:** Direct project decisions. Do not generalize “opaque backdrop,” “dry town,” or “two hind legs” into universal diorama requirements.

## L08 — Consistent views expose errors that attractive renders conceal

**Observation:** The layered builds saved repeatable camera rigs and used actual multi-angle model renders. Moria separated neutral form reviews from illustrative lighting. Dale's larger placement shift needed wider framing, so both comparison versions were rendered at the same span.

**Changed practice:** Keep comparable cameras, materials, and lighting when judging geometry. Inspect full composition and targeted detail. Distinguish generated reference views, actual mesh rotations, and lighting studies; they provide different evidence.

**Evidence:** Dale start (local source: `v3_layered/README.md`), Moria neutral figure comparison (local source: `moria_layered/stage3_r2/README.md`), Dragon placement r4 (local source: `v3_layered/dragon_r2/placement_r4/README.md`).

**Confidence:** Established review practice. Seven views are a useful local convention, not a mandatory count for every edit.

## L09 — Story and spatial relationships must drive effects

**Observation:** Smaug is finishing his attack, so residual fire belongs along the path behind him. Earlier studies put fire on roofs; the user clarified ground-spreading fire between houses. Later corrections broadened impact, connected it to the ground without covering the building, and replaced a gelatinous appearance with burning-gasoline direction: turbulent folds, expansion, and splash.

**Changed practice:** Resolve effect origin, route, supporting surface, chronology, and occlusion before micro-shape. Use reference crops to settle uncertain depth/contact. Keep the effect independent of established architecture and character placement.

**Evidence:** Current Dale checkpoint (local source: `v3_layered/CHECKPOINT.md`), Turbulent fire study (local source: `v3_layered/dragon_r2/mount_flame_r7/README.md`). Recent user corrections in “Avoid decompressed request errors” confirm the sequence.

**Confidence:** Direct corrections; the r7 response remains a candidate. Its sheets are a sculpt study, not fluid simulation, and the six other village fire meshes retain the older style.

## L10 — Inspect local capabilities before declaring a generation blocker

**Observation:** Installed local TRELLIS.2 produced the dragon and both new Moria figures. Missing cloud credentials or Blender MCP access did not imply that generation was unavailable. Exact inputs and generation settings were preserved.

**Changed practice:** Inspect available local tools and environments first. Record the actual route and input preparation; keep generated studies, raw geometry, repair, and placement as separate artifacts.

**Evidence:** Dragon reconstruction (local source: `v3_layered/dragon_r2/reconstruction/README.md`), Moria restart (local source: `moria_layered/character_restart/README.md`). The recorded installation was a local `trellis-mac` checkout with its own `.venv` and `spike_geometry.py`; discover and verify the appropriate path on the current machine.

**Confidence:** Recorded successful local runs. Tool settings and timings are provenance, not guaranteed defaults for a new subject or machine.

## L11 — Surface repair needs shape evidence and semantic component decisions

**Observation:** MeshFix, signed-voxel, and merged-contact diagnostics were rejected for the dragon. An unsigned-distance reconstruction without merging nearby vertices yielded a closed, consistently oriented surface while retaining recognizable anatomy. An adapted method cleaned Moria's figures. The Balrog's separate grip/whip accessory was intentionally retained.

**Changed practice:** Diagnose the source's surface ambiguity, preserve raw geometry, bound smoothing/displacement, inspect the result, and record sampled shape differences. Do not blindly merge near contacts, fill every visible gap, remove every disconnected component, or chase one-component counts. Re-evaluate the technique per mesh.

**Evidence:** Dragon cleanup r2 (local source: `v3_layered/dragon_r2/reconstruction/cleanup_r2/README.md`), Moria cleanup (local source: `moria_layered/character_restart/cleanup_r1/README.md`).

**Confidence:** Recorded topology and sampled-proximity success across three subjects. This log does not diagnose every rejected algorithm's general suitability. Repair shell parameters are scale-dependent; closed thin skins remain unqualified for printing.

## L12 — Separate visual success, valid topology, and a manufacturable object

**Observation:** First-attempt V2 imported as manifold and one part while failing the visual target. Current dragon and character repairs are closed but still lack thickness, strength, self-intersection, mounts, supports, and slicing qualification. Moria's sampled contacts and clearances have explicit measurement limits.

**Changed practice:** State which question each check answers. Engineer at final scale and verify physical interfaces with representative prints. Inspect the complete support/layer arrangement, not only the object's bounding box. Keep engineering work visible in the remaining-work list.

**Evidence:** Historical print notes (local source: `PRINT_NOTES_V2.md`), Dragon cleanup (local source: `v3_layered/dragon_r2/reconstruction/cleanup_r2/README.md`), Moria checkpoint (local source: `moria_layered/CHECKPOINT.md`).

**Confidence:** Strong distinction; actual manufacture remains an open stage. Printer facts in the old notes are historical, not current recommendations in this draft.

## L13 — Prompt size is a workflow constraint; design for a small, restartable conversation

**Observation:** The user identifies an oversized-prompt incident in the second Dale attempt. The earlier task **Fix oversized session error** records `decompressed request body exceeds 67108864 bytes`. That is an observed request-size rejection; the relative contribution of images, tool outputs, and other history was not measured. Workspace instructions subsequently require local originals, compact contact sheets, bounded output, and checkpoints.

**Changed practice:** Create compact review derivatives before loading images; avoid repeated ingestion of unchanged views. Keep heavy data on disk and filter tool/history results before returning them. Maintain a checkpoint that permits continuation without the old transcript. After a failure, stop unchanged retries, verify saved work/jobs, and prepare a minimal fresh-task handoff when needed. Do not assume token compaction or a history-carrying fork solves the byte limit.

**Evidence:** Exact incident and scoped technical interpretation are recorded in [payload management](payload-management.md); operating constraints are in workspace instructions (local source: `AGENTS.md`). Dale checkpoint (local source: `v3_layered/CHECKPOINT.md`) and Moria checkpoint (local source: `moria_layered/CHECKPOINT.md`) demonstrate the on-disk continuity pattern.

**Confidence:** Observed failure and established operating requirement. Prevention/recovery are practical workflow guidance, not a measured guarantee against recurrence. See the [recovery procedure and restart message](payload-management.md) for handling a session that can no longer summarize itself.

## L14 — Ask for a focused concept crop when local iterations stop converging

**Observation:** The user reports better results after supplying a screenshot of the exact concept-art region to model, and asks that the assistant proactively request one when an area needs repeated corrections or the work goes in circles. Dale's ground-fire, impact-base, and wall-clearance corrections provide recorded examples of localized reference use.

**Changed practice:** Recognize repeated unresolved corrections as a reference/interpretation problem before attempting another variation. Ask for a small crop with enough context and the specific relationship to match; inspect an existing suitable crop first. Record the clarified constraint and review the next actual model against it. Continue independent work while waiting instead of further guessing at that feature.

**Evidence:** User guidance in **Draft diorama pipeline skill**, 2026-09-22; Dale checkpoint (local source: `v3_layered/CHECKPOINT.md`) records the supplied ground-fire and flame-base crops and their corrections.

**Confidence:** Direct user-reported improvement and requested working practice. The trigger is lack of convergence, not a universal maximum number of revisions. A crop clarifies intent but cannot supply hidden geometry or guarantee a correct reconstruction.

## L15 — Preserve technical learning without importing abandoned design decisions

**Observation:** The user reports that design choices from the abandoned Dale attempt bled into the second attempt. This is an unwanted continuity failure. This report does not establish every affected choice or the precise mechanism that imported it.

**Changed practice:** Record an active attempt and explicit design-source boundaries. Within a restarted scope, allow only current references and retained/re-adopted choices to guide the design. Reuse technical methods after inspecting embedded assumptions; exclude abandoned geometry and design defaults unless explicitly brought forward. Check source paths and decision provenance before review and handoff. Distinguish a new conversation continuing a design from a new design attempt.

**Evidence:** Direct user report and requested prevention in **Draft diorama pipeline skill**, 2026-09-22. Workspace instructions (local source: `AGENTS.md`) already exclude specific superseded/deleted sources; the new rule extends that protection to decision provenance. See the [attempt record](working-records.md) for the practical format.

**Confidence:** User-confirmed failure; the prevention procedure is newly added and not yet demonstrated on another restart. Apply it to the user's stated restart scope so it does not discard valid environment work or standing requirements.

## Questions the next attempts should answer

- Does earlier isolated character development avoid long cycles of environment/figure mismatch? Reserve scale and contact locations while testing it.
- Can mounts, thin wings, small equipment, and flame sheets survive printing, support removal, handling, and assembly at the accepted scale?
- What joint tolerances and segmentation work for the chosen process/material? Record physical test dimensions and outcomes.
- Can physical lights reproduce the desired focal hierarchy without obscuring sculpture? Render emission alone does not answer this.
- When must a visually accepted layer change for engineering reasons, and how much rework does the layered structure prevent?

Use the lesson-entry form in [working records](working-records.md) for new evidence. Update or retire a lesson when results contradict it; avoid turning every local correction into a universal prohibition.
