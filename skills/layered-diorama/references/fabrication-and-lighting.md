# From approved geometry to tested parts

Collected September 23, 2026 from continued Dale and Moria work. These are reusable procedures with dated case evidence, not a release checklist claiming that either whole diorama is finished. No geometry, slicer, or physical checks were rerun for this documentation update. Local source paths below identify evidence outside this repository.

## Separate parts by function and assembly needs

Distinguish an assembly joint from a cut made only to fit a printer. Removable object carriers, support caps, service trays, and light inserts can preserve a whole character and the assembled appearance while making installation or maintenance possible. Honor the user's chosen responsibility for plate-size cuts; do not add arbitrary seams when they intend to handle those in the slicer.

Plan assembly with every fixed component present. Record which parts move together, which supports are absent at each stage, and which fragile accessories install last. Check the assembled pose and intermediate motion, including modifiers/evaluated geometry where relevant. A carrier-only check cannot qualify clearance against the surrounding bridge, landing, or scenery. Keep numerical contact thresholds and excluded geometry explicit.

**Dale evidence:** A fixed wing seat trapped the creature. A removable rear support and cap preserved its assembled surfaces while allowing a compound rigid motion. The mouth flame installs afterward because it crosses that route. Finite path checks supported this staged plan; a cropped receiver, full rear support/cap, and actual wing-tip sample subsequently passed local physical fit. Full-character handling and adhesive loading were not established by that kit.

**Moria evidence:** Paving carriers let figures remain undrilled. Including the full bridge exposed tail/landing and carrier/core contacts missed by an earlier partial screen. Local receiver and paving relief opened the approach without reshaping the accepted figures. Latest FDM carrier/bridge receiver tests are distinct from the already-passed resin sole/carrier tests.

Sources: `v3_layered/staged_mount_r1/README.md`, `v3_layered/mount_fit_r1/README.md`, `moria_layered/assembly_r1/README.md`, `moria_layered/balrog_regeneration_r1/print_study_r1/README.md`, `moria_layered/structure_print_r1/README.md`.

## Test the real interface, then protect the result

Use small representative pieces cut from current mating geometry before a large print. Include both halves, actual hardware where applicable, and the intended material/process/orientation. Label variations so feedback maps unambiguously to a dimension. Ask whether parts fully seat, rock, bind, snag during removal, or require force. Keep test scale explicit and preserve contact surfaces through cropping and export.

Record interface identity, file revision, settings actually known, hardware, and result. A good generic tolerance coupon is useful evidence, but it does not qualify an untested interface. A result from resin does not automatically apply to PLA; an unchanged board pocket does not qualify a new carrier's cap or wired installation. Where a revision changes mating dimensions, deliver the matching pair and identify incompatible old parts.

After a pass, protect the tested surfaces and dimensions during later sculpting, repair, consolidation, and export. Compare against the tested artifact, not merely the most recent scene. If a necessary change reaches that interface, identify the changed region and determine which test must be repeated. Do not silently improve a working fit.

**Dale evidence:** The first gate LED pocket and slide were physically tight despite digital checks. Revised pocket/slide clearances and entry bevels passed the user's local fit test; both revised mating parts were required. The wing-support kit also passed. Early PLA fin tests accepted 1.0/1.2/1.6 mm and rejected 0.8 mm, but did not qualify a full wing or its root.

**Moria evidence:** The user reported passes for the selected wire bore, root joint, foot interface, and wing sample. A two-notch coupon identified the 1.0 mm nominal bore for 0.8 mm nominal wire. These dimensions are case results, not universal clearances or proof of full-whip strength. FDM carrier-to-bridge tests remain pending.

Sources: `v3_layered/CHECKPOINT.md`, `v3_layered/gate_led_r2/README.md`, `v3_layered/mount_fit_r1/README.md`, `moria_layered/balrog_regeneration_r1/print_exports_r1/README.md`, `moria_layered/structure_print_r1/README.md`.

## Glued joints: printed male/female tabs

David set this on 2026-11-15: wherever two printed faces are glued together, align them with a male tab or plug printed on one face and a matching female socket printed in the other. Do not use loose dowels, filament pins or pin holes for a glued joint unless one of the exceptions below applies. Loose pins are extra parts to cut, count and lose, small holes print undersize, and a printed pair locates the joint in one move. This supersedes the dowel scheme of the early Smaug `assembly_r1` study (see [mounting points](mounting-points.md)) for any new glued joint.

**Shape.** Use plain straight cylinders or prisms, built as exact solid CSG after any remesh, repair or smoothing, which round and flare them. Put a 0.3–0.5 mm chamfer on the male's tip as a lead-in and leave its sides straight. Keep the cutters editable, generate both halves together, and record each feature's position and size with the cut.

**Starting sizes.** These come from sibling projects, not from a diorama print, so the first joint that uses them gets a two-piece coupon cut from the real mating geometry.
- Clearance for a glued alignment fit: 0.2 mm all round for tabs (bookwyrm-boxes' teardrop foot tab, printed and fitted) and about 0.1 mm per side for round plugs (Doré lantern v1.4: 5.0 mm plugs in 5.2 mm sockets, not yet printed). A removable carrier or service part needs a looser, tested fit instead.
- Depth: make the socket 0.2–0.5 mm deeper than the male stands proud, so glue has somewhere to go and the faces close fully.
- Size: at least 5 mm across, standing out no more than about 1.5 × its width, with at least 1.5 mm of material around the socket. Check that no socket breaks through a visible surface or a thin feature.

**Keying.** A glued joint should go together only one way. Use one non-round tab (a teardrop or D shape) or two features placed asymmetrically; one round plug can rotate.

**Print orientation.** Put the male on the part where it prints well, standing up from a face printed top-up or sideways on a part lying flat. A long thin peg printed upright snaps at a layer line, so keep it stubby or make it a wider tab. Never put a male on a face that prints against the bed.

**Cuts the user makes in the slicer.** When David splits a part for the plate in Bambu Studio himself, suggest the cut tool's plug connector (a printed male/female pair) rather than its dowel connector.

**Exceptions.** Say which one applies, and why, in the working record.
- A shaped mounting seat that already locates the object (feet in an adhesive seat, a cradle) is the female half; it needs no extra tab.
- The joint is not glued: removable carriers, support caps, service trays, light inserts, magnets and screws.
- Moving joints: hinges, pivots and axles.
- The material is too thin to hold a socket without breaking through. Add a hidden lug or boss behind the seam to carry the pair; use a pin only when that does not fit.

Accepted and physically passed interfaces keep the joints they passed with.

## Repair defects without discarding working geometry

Establish the pre-edit defect state and protected surfaces. Localize actual defects before trying broad repair. Inspect a repair's silhouette, contact geometry, connectivity, collapsed faces, and intersections; a lower count in one checker does not establish overall improvement. Preserve rejected outputs as clearly excluded diagnostics where appropriate.

Select repair methods by the mesh and protected region. Broad remeshing may lose rock masses, alter soles/sockets, or create collapsed geometry. Local relaxation, retriangulation, seam closure, or selective remeshing may be more controllable. Do not promote one tool as universally safe or universally unsuitable based on a failed case. When consolidation is needed, include only current intended parts, exclude hidden historical geometry and hardware placeholders, and retain editable originals reversibly.

Distinguish exact coordinate/connectivity preservation, sampled surface agreement, and visual similarity. If a tiny fitted-region patch must change, report it precisely instead of claiming the entire interface remains exact. Recheck relevant movement paths when repaired surfaces border them.

**Evidence:** Dale's targeted mountain cleanup reached zero flags in the recorded intersection screen while retaining its tested receiver plane. A near-foot sliver required a small, measured surface change. Moria rejected broad repairs that changed visible rock or tested soles/sockets; selective structural cleanup reduced flags but left unresolved ones. These outcomes do not justify claiming every final part is defect-free.

Sources: `v3_layered/mountain_intersections_r3/README.md`, `moria_layered/structure_print_r1/README.md`, `moria_layered/balrog_regeneration_r1/print_exports_r1/README.md`.

## Solid construction does not eliminate every thin feature

Follow the active manufacturing decision, including the user's solid-volume FDM rule and intentional functional voids. Treat other processes and individual parts according to their current instructions; do not infer automatic hollowing from resin use. Moria's current figures are explicitly solid too.

A filled body can still have thin projecting cloth, membranes, tips, and bridges between details. Use failure photographs to identify the physical problem. Where authorized, add support material behind the feature or bridge an internal gap while preserving the visible sculpt and tested contacts. Compare actual sections and multiple exterior views. Directional material spans are not exact minimum wall thickness, and filling an underside may become visible through openings.

**Evidence:** Gandalf printed with recurring cape holes in both hollow and solid versions. The user requested a connected cape-to-robe underside fill. The candidate preserved main visible folds and sampled sole contacts, but its new physical outcome remains pending. Broad fills that obscured folds were rejected. Dale's corrected solid dragon export supersedes its hollow reinforcement export; its new one-piece result is not yet reported.

Sources: `moria_layered/gandalf_cape_fill_r1/README.md`, `moria_layered/solid_characters_r1/README.md`, `v3_layered/dragon_solid_r1/README.md`.

## Validate the delivered artifact and native slicer interpretation

Check the exact exported file after reopening: units, scale, transforms, object count, bounds, connectivity, and topology as applicable. Record export-only centering separately from scene placement. Explain whether files share assembly coordinates or each has its own print origin; independently centered objects imported at one origin do not reconstruct the scene.

Keep source-mesh checks, exported-file checks, native import, repair reports, layer/support review, and physical results separate. If they disagree, investigate and report the disagreement. Do not dismiss native warnings because another library says watertight. Likewise, an import marked manifold does not resolve an independent intersection report.

An indexed 3MF may preserve connectivity that coordinate-welded STL export changes. Verify its roundtrip rather than assuming the format fixes geometry. Distinguish geometry-only 3MF, a native slicer project, and machine output; the extension alone does not establish embedded settings, supports, or readiness.

If the user repairs the model in a slicer, record that as a separate artifact. Until that exact file is received and compared, do not reissue the unrepaired local export as the repaired version or overwrite the user's result. Native repair can change tested interfaces and needs appropriate revalidation.

Recheck plate centering and the complete raft/support envelope after orientation and support generation. Label the frame for angles and whether scale is already baked in. Recheck layers, islands, contact damage, and removal access after geometry changes; an old slice does not update itself.

**Evidence:** Balrog's indexed 3MF preserved geometry after STL welding exposed defects; the user subsequently reported clean native import and body fit. Gandalf's cape STL passed local topology checks but triggered SatelLite repair. The user-repaired copy is not available locally; the local STL remains pre-repair. Moria's large FDM files import as manifold while independent intersection flags remain. An earlier Gandalf import also needed centering, repeated after supports.

Sources: `moria_layered/balrog_regeneration_r1/print_exports_r1/README.md`, `moria_layered/gandalf_cape_fill_r1/README.md`, `moria_layered/structure_print_r1/README.md`, `moria_layered/CHECKPOINT.md` (Gandalf print-test record), `v3_layered/dragon_solid_r1/README.md`.

## Test lighting as hardware, access, and optics

Establish the selected hardware and verified dimensions before cutting production pockets. Keep unverified controller/connector envelopes labeled as reserves. Distinguish uncut route guides from real openings and list which exported scene revision includes them.

Design installation and removal for the wired part: board orientation, solder pads, leads, connectors, bend space, slack, retention, and service cover. Passing a nominal bare-board path or wire centerline does not establish that the soldered assembly can be installed. Keep functional cavities and routes accessible in the intended order, and check that new cuts avoid tested mounts.

Check source visibility and optical delivery separately. Hiding an LED behind a bend can conceal it while reducing light reaching the target. Render glow, clear bores, and blocked sightline rays do not establish brightness or diffusion.

Before repeating a holder or committing a large illuminated part, make representative short/long or bent-path tests with the actual LED, intended interior material/color, and removable diffuser samples. Hold drive settings and ambient light constant; change one optical variable at a time. If delivery is poor, reconsider emitter position or light guides rather than assuming greater brightness will fix it. Keep new fit and optics results pending until measured or reported.

**Dale evidence:** The gate holder's local printed fit passed. Building wells borrowed its pocket size but introduced new carriers, cap seats, and long/bent light paths. A two-house short/long test was prepared; actual wired access and brightness are still pending. No final house holder population or optical success is established by that kit.

Sources: `v3_layered/lighting_access_r1/README.md`, `v3_layered/gate_led_r2/README.md`, `v3_layered/building_led_test_r1/PRINT_AND_TEST.md`, `v3_layered/CHECKPOINT.md`.

## Keep the handoff shorter than the history

Maintain a concise active-state summary with the latest authoritative files, current approvals, tested interfaces, superseded exports, active print jobs, and next unresolved test. Archive completed stages and link to their evidence instead of retaining many conflicting “current” sections. A print underway is not a completed pass; independent work must preserve its geometry and interfaces or clearly identify a new revision. Never regenerate or resend a job merely because its result has not arrived.
