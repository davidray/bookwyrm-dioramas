---
name: layered-diorama
description: Develop 3D dioramas from concept art through element decomposition, bottom-up modeling, isolated character development, scene integration, and print engineering. Use for staged diorama builds, revisions, and capturing lessons from them.
---

# Layered diorama — working draft

Draft collected on 2026-09-22 from the first Smaug/Dale attempt, the layered Dale restart, and layered Moria. The layered workflow shows useful visual and editing progress; an end-to-end manufactured result is not yet demonstrated. This repository maintains the working draft and its learning record. Storing it here does not install it as a personal skill.

Read the project's current checkpoint before modeling, and identify the active design attempt and its source boundaries. For reasons behind this workflow and specific failures, consult [the lessons log](references/lessons.md). Use [the working records](references/working-records.md) when starting a project, recording a review, or adding a lesson. Project-specific design choices remain in project checkpoints.

## The pipeline

Concept, story, and printer constraints → element breakdown and dependency map → whole-scene blockout → bottom-up environment → individual elements → assembly and composition → effects and finish → physical engineering → slicing, test parts, and assembly.

This is a revisitable sequence. Use simple reserves for later elements early so that the foundation leaves room for them. Investigate risky interfaces early; finish their engineering once scale, composition, and manufacturing choices are stable. “Layer” means an independently editable scene element or system, not a printer layer or a promise to print every element separately.

### 1. Establish the visual target and story

- Preserve the original concept locally. Record the principal viewing angle, focal point, story moment, important silhouettes, negative space, provisional dimensions, and explicit user constraints.
- Separate composition references, character/anatomy references, surface references, and lighting references. A later character reference can replace a character's style without replacing the environment composition.
- Treat labels in concept sheets as reference content; dimensions, electronics, materials, and assembly features become requirements only through the user's actual instructions.
- Extract focused crops or create element studies where they resolve ambiguity. Preserve prompts and sources. Label AI studies as art direction; they are neither recovered geometry nor authoritative multi-view projections.
- Turn ambiguous descriptions into observable shape decisions: where something originates, what it touches, which way it moves, its outline, openings, and what must remain visible. Carry later clarifications forward and retire superseded assumptions.

### Establish printer constraints before committing to scale

Ask early which printer the user intends to use, unless the active brief already establishes it. Get the exact model and intended process/configuration, not just a brand or “resin/FDM.” Ask about desired finished dimensions where unknown. For example: “Which printer and setup will you use, and do you have a preferred finished size? I’ll size the components to fit while keeping them whole wherever practical.” Do not assume a printer from an abandoned attempt remains the target.

Verify usable X/Y/Z build dimensions from current manufacturer documentation and the selected slicer/machine profile. Record the source, configuration, and any applicable restricted areas. Account for orientation and the space required by supports, brim/raft, or other process necessities; advertised volume and model-only fit are preliminary checks. Avoid inventing a universal clearance margin.

The user's default preference is to avoid splitting individual parts merely to fit the build plate. Use that preference when establishing the initial overall scale: check the limiting components in plausible print orientations and choose a coherent scene scale that lets them fit whole where practical. Separate scene elements do not need to become one fused print. Do not independently shrink a character or building and break established proportions just to make it fit.

If whole-part fit conflicts with the requested size, detail, strength, or a feasible print orientation, present the concrete tradeoff before changing an established scale or cutting parts. Consider practical reorientation and a smaller overall scale first; propose a split only when those options are unsuitable, with its location and assembly implications. Honor an explicit preference for larger size or modular construction. If the printer is unknown, continue concept work at a clearly provisional scale and resolve it before scale-dependent detailing. Recheck fit after changes to poses, wings, effects, or dimensions, and confirm the full supported arrangement in the slicer before printing.

### When a local revision stops converging

If the same area has needed multiple corrections without resolving the mismatch, the user repeats the same concern, or successive revisions merely trade one guess for another, request a focused screenshot/crop of the concept art before another speculative pass. Two unsuccessful passes are a useful signal, not a mandatory wait; ask sooner when the intended shape or spatial relationship is unclear. Ordinary productive refinement does not need an extra interruption.

Explain the specific uncertainty and ask for the smallest useful region, retaining enough neighboring context to show contact, direction, and scale. For example: “We have revised this flame twice, but I am still uncertain where it meets the ground. Could you share a screenshot of that part of the concept art, including the nearby wall, and point out the relationship to match?” Use a channel that accepts image attachments, not a text-only question tool.

If the relevant crop is already supplied, inspect it rather than asking again. If the full reference is available locally and the region is clear, use a focused crop and ask only about the unresolved interpretation. Do not substitute a new AI-generated study for the user's intended evidence. While awaiting essential clarification, continue independent work and leave the disputed area stable.

Save the crop as a new reference without overwriting the original, record its source and the property it clarifies, and translate the user's response into concrete modeling constraints. Compare the next actual-model detail against that crop, then check the whole scene for side effects. The crop's authority is local to that feature; it does not silently replace the overall composition or other accepted choices.

### Keep design attempts separate

At a restart, establish whether the user is replacing the whole design or only a named element. Record the active attempt, current references, allowed starting files, explicitly retained choices, and excluded attempts/components in the checkpoint. Use existing user instructions to establish this scope; ask only if a consequential carryover remains ambiguous.

For the restarted scope, inherited design choices from an abandoned attempt are excluded unless the user has retained or re-adopted them. Availability on disk, a familiar filename, an old approval, or a historical summary is not sufficient authority. Trace each retained design choice to the current brief/reference or an explicit carryover decision. Preserve unaffected layers when the user requested only an element restart.

Reusable technical lessons can cross attempts: camera-comparison methods, compact review generation, audits, or a suitable repair technique. Reusing code requires checking for embedded old design defaults, geometry imports, poses, dimensions, materials, cameras, and source paths. Reuse the method only after those assumptions are removed or justified for the active attempt. Do not load an abandoned scene as the new baseline simply because it is convenient.

Before rendering a restarted build or handing it off, check the source paths and design decisions against this record. Flag unsupported carryovers and correct them before further detailing. Mark old notes as historical in the active checkpoint; preserve files unless deletion is requested. A fresh task continuing the same attempt retains its accepted decisions; a design restart resets only the stated scope. Neither a fresh conversation nor shared project storage decides design lineage by itself.

### 2. Decompose before detailed modeling

Make an element register: purpose in the story, reference, parent/support surface, dependencies, bounding reserve, intended construction method, interfaces, and current status. Typical groups are plinth, terrain/backdrop, architecture, characters/creatures, effects, and hardware.

Create a cheap whole-scene blockout with all important volumes. Establish units, axes, scale, and repeatable cameras. Reserve figure feet, wing spans, tail sweep, flame routes, bridge crossings, sightlines, and likely mounts. Show actual environment geometry both with and without clearly labeled placeholders when useful.

Review the large composition before refining it. An attractive isolated component can still be wrong for the scene. Do not let placeholder geometry become the final sculpture by inertia.

### 3. Build the environment from the bottom up

Develop the plinth and terrain/backdrop, then dependent structures such as buildings, paths, bridges, and landings. Fit new work to the established surfaces using actual scene coordinates and contact measurements.

Resolve silhouette, large masses, proportions, hierarchy, and open spaces first. Then add medium forms, followed by selective surface detail. Broad cliffs need distinct masses and recesses; repeated spikes plus noise do not substitute for geology. Settlements need varied placement and landmarks before roof tiles and window ornament.

Use named collections and separate source masses/recipes. Preserve the existing baseline and write revisions separately. Delay irreversible scene-wide fusion; retain editable sources even when a local union is useful.

### 4. Develop demanding elements independently

Choose a method per element. Procedural modeling is useful for controlled terrain, masonry, paths, layout, and localized edits. For recognizable organic subjects, evaluate reference-driven sculpting or image-to-3D early if procedural forms are missing likeness or anatomy.

Use this sub-pipeline where appropriate:

Focused reference/study → isolated model or reconstruction → multi-angle form review → surface cleanup → scene-scale fitting → integration review.

- Establish anatomy, gesture, equipment, and major folds before fine texture. Check limb count, left/right identity, wing attachments, palms/thumbs, grips, and load-bearing contacts in actual views.
- Compare neutral material renders as well as the intended presentation. Color, glowing effects, and dramatic lights cannot establish that geometry is right.
- Keep the raw reconstruction and input image unchanged. Record generation tool, environment, input preparation, settings, scale, and outputs. Check installed local capabilities before assuming missing cloud/MCP access blocks generation.
- Judge cleanup by retained silhouette and detail as well as topology. Apply and measure changes at a known processing scale, then reassess thickness at final scale. Classify separate components by meaning; do not remove an accessory merely to get one component.
- If iterations keep polishing the wrong style or structure, revisit the reference and method for that element. Preserve useful surrounding layers. A praised intermediate improvement does not permanently approve its style.

### 5. Integrate without undoing established work

During tweaking, prefer one independently reviewable change per iteration, especially when it requires interpretation or design judgment. State the intended change, preserve unrelated properties, and compare its result with the baseline before proceeding to the next change. Avoid adding unsolicited improvements to the same pass. One change can require several coupled edits—for example, moving a hand and maintaining its grip on the staff—when they serve the same outcome.

Give brief, constructive feedback before editing when a refinement prompt bundles enough independent or ambiguous design decisions that focus or review clarity is likely to suffer. Judge complexity, coupling, and uncertainty rather than enforcing a fixed number of changes. Name the separate tweaks, explain why splitting them would help, and recommend the first one and an order for the rest. For example: “This combines three separate design decisions: wing pose, flame shape, and village layout. I recommend tackling the wing pose first, then the flame, then the village, so each result gets a focused comparison. I’ll keep all three in the queue.”

Make this useful guidance, not a reprimand or a requirement to rewrite the prompt. If the order is clear, proceed with the first authorized change and keep the rest recorded. Ask which to prioritize only when the choice materially affects the result and cannot be inferred. Skip this feedback for straightforward coordinated edits or productive multi-step build requests; honor the user's explicit preference for a combined pass.

If the user requests several changes together, retain the full request and work through a short ordered queue, validating each change separately. Continue authorized independent changes without forcing the user to resubmit them or approve every step. When the next change depends on an unresolved visual decision, request review of that concrete result before dependent work. Honor an explicit request for a combined pass, and describe the combined scope clearly.

Separate shape changes from placement changes. Record transform, scale, contact surfaces, and attachment intent. Fit feet to the actual sloped surface, inspect character-to-character and environment clearance, and preserve the upper pose where only a local stance adjustment is needed.

For a local edit, identify protected objects and properties before changing anything. Verify the saved/reopened result against that baseline using appropriate geometry, connectivity, transform, visibility, material, and camera checks. Report the scope: a transform-only edit need not claim a fresh topology audit.

Use the same cameras and neutral lighting for comparisons. If framing must widen, render both versions at the new framing. Include a diagnostic angle for hidden contacts or anatomy; the hero view alone is insufficient.

User acceptance is scoped to the reviewed artifact and property: image direction, sculpture, placement, effects, and engineering have separate statuses. Continue within existing authorization; do not invent an approval stop at every stage. Ask for review when an unresolved design choice materially affects dependent work, and never infer acceptance from silence.

### 6. Add effects, wear, and presentation in service of the scene

Route effects from the story and actual contact surfaces. Check origin, path, impact, aftermath, depth, and architectural visibility before adding turbulence or texture. Keep effects separately editable.

Preserve negative space and readable silhouettes. Add damage selectively, avoiding essential seating/support surfaces unless intentionally redesigning them. Maintain a neutral form view alongside a presentation-lighting view of the same geometry. Describe render lighting as illustrative until physical hardware and materials have been engineered.

### 7. Qualify the physical design separately

Plan mounting, access, material changes, and any necessary segmentation while composing, using the established printer envelope and preference for whole parts. Once the design is stable, use the actual printer/process, final scale, materials, and any requested hardware to engineer thickness, structural load paths, joints, tolerances, supports, access, and assembly order. Revisit appearance if those requirements change visible geometry.

For any mounted character or object, read [shaped mounting seats and assembly clearance](references/mounting-points.md). Preserve the accepted object, adapt its receiving support locally, and subtract a solid copy of the exterior contact region with adjustable mating allowance. Refine unwanted interlocking and the insertion passage separately. Check the whole object's path across all contacts, including any staged assembly or service removal. Terrain, feet, and toes are case examples; apply the same reasoning to props, architecture, bases, walls, and other interfaces. Preserve editable tools and protected geometry; local fit does not establish a complete load-bearing mount.

For the user's current FDM workflow, construct solid material volumes and leave infill to the slicer, while retaining intentional functional voids such as sockets, lighting chambers, wire routes, and tunnels. Historical thin-shell cleanup or reinforcement studies do not override that rule. Preserve accepted exteriors and tested interfaces when changing internal construction; establish process-specific requirements separately for other manufacturing methods.

Keep these claims distinct:

- Visual review: silhouette, anatomy, placement, and story read correctly.
- Geometry checks: finite coordinates, topology, orientation, components, intersections, and measured contacts, stating exactly what was checked.
- Manufacturing review: minimum features/walls, strength, joints, print orientation, supports, process-specific needs, and complete layer preview.
- Physical evidence: printed coupons/parts, fit, assembly, stability, and any lighting test.

A closed mesh, one connected component, successful STL export, or model-only build-volume fit does not establish the later claims. Sampled distances are not exact global clearance bounds. Use representative test pieces for uncertain joints or thin features before committing a large assembly. Record outcomes; do not assume this draft's source projects have completed that stage.

## Review, continuity, and learning

### Keep review payloads small and make recovery possible

Keep originals, full-resolution renders, detailed logs, and mesh audits on disk. Inspect one compressed contact sheet per iteration, preferably 1,200–1,600 pixels on its longest edge and under 500 KB when practical. Load a detail crop only for a specific unresolved question; avoid repeatedly loading unchanged references. These are review targets, not service-limit guarantees.

Filter large tool results before emitting them: paths, selected measurements, counts, and concise audit/error summaries. Never print base64 images, mesh arrays, full scene dumps, or entire historical task transcripts. Read the checkpoint and relevant excerpts instead of reloading the whole project history.

For prevention details and a size-error recovery procedure, read [payload management](references/payload-management.md). If an oversized request blocks progress, stop unchanged retries, preserve local state and job status, and prepare a small handoff. A fresh task should read the checkpoint and selected assets rather than inherit the full transcript; create it only on the user's explicit request. Do not assume context compaction fixes a request-body byte limit.

### Preserve decisions and collect lessons

After a meaningful change, update the checkpoint with the active editable file, reference authority, accepted decisions, candidate status, changed/protected scope, validation and its limits, unresolved issues, and next step. Distinguish checks run now from historical checks. Preserve rejected work only as history where appropriate; respect explicit deletions and never quietly reintroduce rejected baselines.

When adding or revising guidance, write the reusable method in terms of roles, constraints, and decisions; keep named characters, anatomy, materials, dimensions, and project-specific choices in clearly labeled worked examples. Generalize the principle only as far as its evidence supports, and distinguish a transferable method from a physically proven result.

Add a lesson when evidence changes how the next attempt should proceed. Record observation → consequence → changed practice → evidence → remaining uncertainty. Keep case-specific preferences in the lessons log or project checkpoint; promote them into general instructions only when the broader rule is justified.
