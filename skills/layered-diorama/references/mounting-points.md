# Shaped mounting seats and assembly clearance

Use when mounting any character, prop, building, scenic element, or other object to a support such as terrain, a base, a wall, or another object. Preserve the accepted object and derive the mating support from its contact geometry. Smaug is a worked example, not the required subject or anatomy. Choose retention for the actual object and intended use; this workflow does not require adhesive or establish structural adequacy by itself.

## Start from the accepted assembly and selected mount approach

Identify the mounted object, receiving support, fixed placement/scale, permitted edit region, intended retention method, and assembly sequence. Record excluded alternatives. Keep the accepted exterior and tested interfaces fixed unless their change is authorized. Adapt the support locally where possible rather than changing the object to make a convenient mount.

Keep source files intact. Save a revision with editable construction tools and a baseline for geometry/transform comparisons. Inspect the support mesh before modifying it so existing defects are distinguishable from new ones. A visually accepted support may still be unsuitable for manufacturing.

For the user's current FDM workflow, model parts as solid material volumes and let the slicer control infill. Keep intentional functional voids such as sockets, LED chambers, wire routes, and tunnels. Historical hollow-shell examples below do not authorize hollowing a new part or restoring a superseded manufacturing choice. For other processes, establish the appropriate construction from the active brief.

## Build and refine the seats incrementally

1. **Find the actual contact regions.** Use the object in its accepted world-space placement. Inspect its intended contact patches and nearby support from useful angles; identify gaps, overlaps, likely entry/removal directions, and surfaces that must remain visible. Stay inside the authorized edit region.
2. **Bring support material to the object.** Add or expand the receiving support locally, using a transition appropriate to its material and form. Smooth rock expansion is one option; a shaped ledge, cradle, or socket may suit another support. Preserve the surrounding silhouette and unrelated elements. A small contact can be a useful visual experiment without providing enough structural support.
3. **Make a solid tool from the exterior contact shape.** Copy the relevant exterior region, trim it to the intended interface extent, cap any open cut boundaries, orient it, and verify a valid solid cutter. Work in a consistent coordinate frame. If the source is thin or hollow, do not assume subtracting its shell removes the enclosed space: use the exterior envelope to avoid trapped support material. Keep the visible object unchanged.
4. **Add adjustable mating allowance to the tool.** Offset the hidden cutter, then subtract it from the receiving support. Record whether the allowance is a normal/vertex offset, measured gap, or another construction parameter; these are not interchangeable guarantees. Choose final allowances for the intended process and retention method through fit tests, rather than copying the case's numbers.
5. **Inspect and repair the local result.** Check failed cuts, new seams, trapped material, detached fragments, and fragile projections between object details. Compare defect locations before/after; local repairs do not establish that the entire support is watertight. Retain the original support, pre-cut revision, and cutters in hidden construction collections.
6. **Relieve unwanted interlocking.** If an exact negative creates obstructing fingers or catches between adjacent features, subtract a shared clearance envelope where needed. Examples include gaps between toes, projections on a prop, or an overhanging edge. Retain useful seating surfaces and intentional locating keys; do not erase required retention or alter other mounts incidentally. Review the relief as a focused change.
7. **Open the insertion approach.** A matching final pocket is not sufficient. Define how the object enters and remove obstructing lips/undercuts using a tool representing its swept volume. A convex envelope of endpoint geometry can conservatively approximate a straight translational passage, as in the Smaug example, but may remove excess support. Rotational or curved approaches need an appropriate sweep. If no practical route preserves the accepted interface, consider an authorized removable support section or staged assembly rather than automatically widening every seat.
8. **Test movement as well as the final pose.** Test the actual object surface through intermediate positions, record collisions and sampled clearance, and show the exposed seat alongside the assembly. Add sampling at close approaches; discrete checks do not prove continuous collision-free motion. Keep the object in its accepted final placement in the saved review scene.

Before considering assembly feasible, test the whole rigid object against every interacting component. All its contact regions must follow one compatible path; clearance for one patch does not prove clearance for another or for protrusions elsewhere. For staged assemblies, test each part in order against the parts already installed, and test removal when serviceability is required. A local contact study, a complete digital path check, and a physical fit test are separate evidence.

## Worked example: Smaug

The initial adhesive-seat experiment adapted nearby rock around fixed feet. Capped outer-foot copies formed the negative seats; later envelopes relieved toe gaps and opened a local approach. These are instances of the general contact, relief, and passage steps above. The separate pin-sleeve prototype was not incorporated, and old pin guides were hidden.

## What the Smaug studies actually established

The following records the early foot-seat experiments as collected on September 22, 2026. It is a historical snapshot, not the current project checkpoint or default settings for another object. No geometry or physical tests were rerun for this documentation update. Later user instructions report acceptance of the foot slots and further assembly/fit work; consult the active project checkpoint for that subsequent evidence.

| Revision | Method and recorded result | Remaining limitation |
| --- | --- | --- |
| `foot_seats_r1` | Smooth rock expansions reached approximately 4.804 mm near the near foot and 2.194 mm near the far foot. Capped exterior-foot cutters used a provisional 0.10 mm offset. Local seams were repaired; 409 protected object signatures matched. | Small contact areas; no load, adhesive, insertion, or production qualification. |
| `foot_seats_r2` | A shared distal-toe envelope with a 0.65 mm offset removed stone between the far toes; five detached chips were removed. Upper/rear seat and near-foot seat were retained; 419 protected signatures matched. | Final-pose clearance still did not provide a usable entry. |
| `foot_seats_r3` | A straight approach began 40 mm toward the village/front and 1.5 mm above the final position. An endpoint hull with a 0.50 mm vertex margin opened the passage. Actual outer foot below z98.8 mm had zero triangle intersections at 41 tested poses, with approximately 0.498 mm minimum sampled clearance. 420 protected signatures matched. | Only that local foot region was tested. At this stage, whole-dragon insertion and structural suitability were unqualified, and visual review was pending. |

Smaug's geometry and final placement remained unchanged. Recorded terrain samples outside the edited regions showed zero measured deviation; that is sampled evidence, not a global exact-surface proof. The r3 mountain remained one connected component but had 105 boundary and 407 overused edges, so it was not a production-ready mesh.

## Keep the pin prototype separate

The earlier `assembly_r1` study used two parallel pin axes, contoured rock sleeves, separate bored body inserts, nominal 4 mm dowels, provisional 4.4 mm bores, and 4.2/4.4/4.6 mm hole coupons. Those values remained under test. The approved dragon surface was retained exactly; inserts were hidden and separate, and body apertures were deferred. Pins crossing the uncut reference shell were layout guides, not completed joints.

Full-body Boolean integration produced edge defects and was rejected. The useful lesson is to prototype inserts and fit separately, preserve the accepted exterior, and integrate only after manufacturing construction is established. This historical thin-shell failure is not a reason to keep the object hollow; the September 23 user instruction explicitly supersedes that construction for FDM. Do not resume rejected fused geometry or switch from adhesive seats back to pins without direction. Neither prototype establishes a complete mount.

## Later assembly and physical-fit evidence — September 23 update

Dale progressed beyond the early foot-only study. Removable rear support and cap sections retained the approved assembled contact shapes while permitting a stored compound rigid object motion; the mouth flame fits afterward. A small kit using the actual receiver, full support/cap, and a cropped wing region passed the user's local physical fit test. Preserve those tested interfaces; this result does not prove full-object installation, adhesive loading, or a successful full print.

Moria provides a second example: removable paving carriers preserve figure geometry, but carrier-only checks missed surrounding bridge and landing contacts. Later receiver/paving relief resolved the checked path while keeping the figures fixed. Passed resin foot/carrier samples do not qualify the distinct FDM carrier/bridge connection; those receiver tests are pending.

See [fabrication and lighting](fabrication-and-lighting.md) for the generalized staged-assembly and actual-interface testing procedure, evidence paths, and export limitations. Keep functional support separation distinct from cutting the mounted object solely for build-plate fit.

## Review and qualification record

Record the fixed object and receiving-support baselines, permitted support changes, mount method, cutter source and limits, allowance definition, retained contact regions, assembly approach, protected-object checks, new versus pre-existing defects, and precise collision-test scope. Use one compact comparison showing before/after, an exposed seat, and enough of the assembly to judge visibility.

Keep visual acceptance, local fit, whole-assembly access, and load and retention performance separate. Before production, resolve wall thickness and topology, evaluate contact area and load path, test fit and the chosen retention method with the actual materials, and check the complete assembly sequence. Do not enlarge contacts or add other supports merely because a preliminary seat exists; stay within the requested design scope and present unresolved support needs.

## Local evidence

These paths are relative to the original Dioramas workspace and are not repository dependencies:

- `v3_layered/CHECKPOINT.md`: active choice, protected design, recorded checks, and limitations at collection time.
- `v3_layered/foot_seats_r1/README.md` and `v3_layered/scripts/build_foot_seats_r1.py`: solid foot cutters, local rock expansion, subtraction, and preservation checks.
- `v3_layered/foot_seats_r2/README.md` and `v3_layered/scripts/trim_far_foot_seat_r2.py`: toe-envelope relief.
- `v3_layered/foot_seats_r3/README.md` and `v3_layered/scripts/open_far_foot_entry_r3.py`: swept entry envelope and sampled path checks.
- `v3_layered/assembly_r1/README.md`: separate pin prototype and rejected full-body Boolean integration.

Only this distilled documentation belongs in the skill repository. Scene files, cutters, numerical arrays, renders, and project-specific scripts remain with the source project. Read its current checkpoint before resuming modeling; the historical values here are not an alternative active-state record.
