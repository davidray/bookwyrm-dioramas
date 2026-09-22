# Working records

Use only the sections needed for the current task. These are lightweight record formats, not additional approval gates. Keep the project checkpoint authoritative; link to detailed audits rather than copying them.

## Project brief and element register

Record concept/reference paths, story moment, hero view, focal hierarchy, units/axes, target dimensions and their authority, explicit constraints, and unresolved manufacturing choices.

| Element | Story/visual role | Governing reference | Depends on / contacts | Reserved envelope | Method | Current artifact and status |
| --- | --- | --- | --- | --- | --- | --- |
| Base/terrain | Foundation and negative space | Composition reference | Overall scale | Footprint / heights | Editable masses | Path; provisional or accepted scope |
| Structure | Route, setting, support | Architectural crop | Terrain/landings | Placement reserve | Procedural or modeled | Path; status |
| Character | Focal action | Anatomy/style reference | Footing, sightlines, wing clearance | Pose and span | Sculpt or reconstruction | Path; status |
| Effect | Action and aftermath | Story plus effect crop | Source, impact, visibility | Route reserve | Separate sculpt | Path; status |

These rows are examples. Add a backdrop, hardware, or other systems only when the project calls for them. A dependency map can be a short sentence: terrain supports bridge; bridge determines foot contacts; figure placement determines whip route.

## Printer and scale record

```text
Printer: exact model, process, and selected configuration/profile
Usable build envelope: X/Y/Z, units, source, date verified, restricted areas
Intended material and applicable nozzle/process details: known or unresolved
Preferred finished scene dimensions: requested or provisional
Whole-part preference: avoid cuts for plate fit unless a tradeoff is accepted
Limiting components: dimensions at scene scale and candidate print orientations
Support/adhesion space: estimated during layout; checked in slicer before printing
Chosen coherent scene scale: reason, status, and any accepted tradeoff
Fit evidence: model-only estimate / supported slicer arrangement / physical test
Recheck triggers: scale, pose, component dimensions, printer/profile changes
```

Record unknowns explicitly and ask for the printer early. Do not treat a nominal build envelope as proof of printable fit or an old project's printer as the current selection.

## Active attempt and carryover record

Complete this at a whole-design or element restart, then keep it in the project checkpoint.

```text
Active attempt ID and root:
Restart scope: whole design or named elements
Current governing brief/references:
Allowed scene/component starting files:
Explicit carryovers: choice or artifact → user decision/current reference
Protected unaffected layers:
Excluded attempts/components/decisions:
Reusable technical methods: source → assumptions removed or revalidated
Unresolved carryover questions:
```

An empty carryover list for a restarted element means no old design choices have been adopted for that element. It does not erase standing user requirements or protected layers outside the restart scope. Do not infer carryover from file presence, old praise, or a generic “continue” message referring to the active attempt. Read the current checkpoint before searching historical files.

## Focused-reference request and result

- **Area and unresolved mismatch:** What remains wrong after the recent revisions?
- **Existing evidence checked:** Relevant full reference or crop already available.
- **Request:** One specific screenshot/crop request and the relationship to clarify.
- **Reference received:** Saved path, original source, and applicable element/property.
- **User clarification:** Concrete form, contact, direction, scale, or visibility constraint.
- **Next comparison:** Actual-model detail alongside the crop plus a scene check.

Do not request the same image again when it is already available. If no new image is available, use the existing reference to isolate the uncertainty and ask for a description or annotation; do not label your interpretation confirmed.

## Iteration record

- **Decision being tested:** One clear visual or technical question.
- **Current tweak:** One independently reviewable outcome; note any coupled edits it requires.
- **Remaining requested changes:** Ordered queue, including dependencies; retain items until completed or explicitly dropped.
- **Scope feedback, when needed:** Separate decisions identified, reason to split them, and recommended first change/order; record any user preference for a combined pass.
- **Starting artifact:** Exact scene/component path and relevant reference.
- **Change:** What changed and why; shape, placement, material, or lighting.
- **Protected scope:** Objects/properties that should remain established.
- **Result:** New editable file and compact actual-model comparison path.
- **Evidence:** User response and/or checks, with scope and method.
- **Status:** Candidate; accepted for the specified property; rejected; superseded.
- **Uncertainty and next step:** What the result does not establish and what resolves it.

Example: an accepted dragon translation establishes placement. It does not establish mount strength, and a subsequent flame study does not reopen the dragon pose by default.

## Project checkpoint

```text
Updated: date and change
Active attempt and restart scope:
Allowed sources / explicit carryovers / excluded prior attempts:
Current editable candidate: path
Last accepted baseline: path and accepted scope
Visual authority: original concept, element references, later clarifications
Constraints: active user decisions, printer/profile and usable envelope, whole-part preference, units/scale, protected layers
Completed: changes and inspected review artifact
Checks run this iteration: method, result, scope, audit path
Historical checks relied on: source and continued applicability
Not yet qualified: specific remaining visual/engineering questions
Superseded/rejected sources: identities and restrictions
Next step: one concrete action
Reproduction: scripts/environment; running jobs if any
```

Do not copy a historical document's “current-session” wording into a new checkpoint as if the checks just ran.

## Payload incident record

For an oversized-request failure, record the exact error, failed operation, last successful checkpoint, and whether any local jobs continued. Include observable image dimensions/file sizes or output sizes; do not guess total request size. Record recovery attempted and whether a minimal restart succeeded. Follow [payload management](payload-management.md) and its small restart-message format.

## New lesson entry

```text
ID / title / date:
Attempt and artifact:
Observation or user correction:
Consequence for this build:
Practice to change next time:
Evidence path and exact scope:
Status: observed failure / observed improvement / established constraint /
        working hypothesis / physically demonstrated
Limitations or counterexamples:
Next evidence needed:
```

Promote a lesson into SKILL.md when it changes future decisions across relevant projects. Keep exact poses, preferred fire styles, hardware choices, and repair parameters with their source project. If a later result changes the lesson, explain the change and keep the evidence trail.

## Draft handoff — 2026-09-22

Current draft: `../SKILL.md`; collected evidence: `lessons.md`.
Sources reviewed: the first build's accuracy/print notes, both layered project checkpoints, selected stage/reconstruction READMEs, and recent relevant task reviews. No new geometry or print checks were performed. No scene files changed.

Completed: reusable staged workflow, 17 sourced lessons, status distinctions, working record formats, and open physical-validation questions. Expanded L13 with the recorded request-size failure, prevention/recovery guidance, and a minimal restart message; checked official compaction documentation to distinguish context handling from request-size recovery. Added a focused-crop request trigger for stalled iterations and an explicit attempt/carryover record to prevent abandoned designs influencing restarts. Added one-change refinement guidance and a queue for preserving multi-change requests while validating each tweak separately. Added early printer/envelope discovery, coherent scale planning, and the preference to avoid splitting parts for plate fit. The maintained draft now lives in `skills/layered-diorama` in the `davidray/bookwyrm-dioramas` repository. It has not been installed into personal skills. Only skill documents and metadata were copied; original project evidence remains outside this repository.

Validation: bundled skill validator passed using the existing TRELLIS Python environment; repository Markdown links resolved. Original project evidence is recorded as local source identifiers rather than broken external-workspace links. Behavioral use of the draft has not yet been tested on a new build.

Next: refine the draft as reviews and physical tests produce new evidence. Before promoting/installing it, review which case-supported practices deserve to remain general instructions. Locate original project evidence separately when needed; the skill does not require that workspace to be present.
