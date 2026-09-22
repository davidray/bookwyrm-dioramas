# Shaped mounting seats and assembly clearance

Use when fitting a fixed figure or creature to terrain, particularly when a discreet adhesive seat could preserve an accepted composition. This procedure records the Smaug foot-seat experiments and generalizes their workflow. It is not a qualified structural design or a requirement to use glue for every mount.

## Start from the accepted assembly and selected mount approach

Identify the exact scene, fixed figure pose/scale, permitted terrain-edit region, and intended retention method. Record which earlier mount alternatives are excluded. In Smaug's case, the user selected a small experiment with shaped adhesive seats: slightly expand rock around the feet and subtract the feet's shapes while leaving Smaug fixed. The separate pin-sleeve prototype was not incorporated; old pin guides were hidden.

Keep source files intact. Save a revision with editable construction tools and a baseline for geometry/transform comparisons. Inspect the support mesh before modifying it so existing defects are distinguishable from new ones. A visually accepted terrain mesh may still be unsuitable for manufacturing.

## Build and refine the seats incrementally

1. **Find the actual contact regions.** Use the figure in its accepted world-space placement. Inspect each foot and nearby rock from useful angles; identify gaps, overlaps, the likely approach direction, and surfaces that can remain visible. Keep changes inside the authorized region.
2. **Bring support material to the figure.** Expand nearby rock with smooth local falloff rather than moving the figure to meet it. Add only the material needed for the current seat study. Preserve the surrounding terrain silhouette and all unrelated scene elements. A small seat may be an appropriate first visual experiment without being sufficient to support the load.
3. **Make solid tools from the exterior contact shape.** Extract the outer foot surface into a separate copy, trim it above the contact region, close the cut boundary, orient it, and check that the cutter is a valid solid. Subtracting a thin hollow character shell directly can leave unwanted rock inside it. Keep the visible character untouched.
4. **Add adjustable mating allowance to the tool.** Offset the hidden cutter, then subtract it from the local rock. Record whether the allowance is a normal/vertex offset, measured gap, or another construction parameter; these are not interchangeable guarantees. Choose final allowances through the intended process and fit tests rather than copying this case's numbers.
5. **Inspect and repair the local result.** Check for failed cuts, new seams, trapped material, detached chips, and narrow stone projections between toes. Compare defect locations before/after; do not mistake a local repair for a watertight entire mountain. Preserve the original support, expanded pre-cut support, and cutters in hidden construction collections.
6. **Relieve gaps that create unwanted interlocking.** If a detailed negative leaves stone fingers between toes, subtract a shared outer toe envelope where needed. Preserve the intended connected upper/rear support and avoid trimming the other foot's seat as an incidental change. Keep this as a focused revision with its own comparison.
7. **Open the insertion approach.** A matching final pocket is not sufficient. Define how the part enters and remove obstructing lips/undercuts using a cutter representing its swept volume. For a straight translation, Smaug's study used a convex envelope of foot points at the approach and seated endpoints. This conservative envelope may remove more rock than the exact sweep; inspect the retained seat. Rotational or curved approaches need an appropriately constructed sweep rather than blindly reusing the endpoint hull.
8. **Test movement as well as the final pose.** Test the actual part surface through intermediate positions, record collisions and sampled clearance, and show the exposed seat as well as the assembled view. Use additional sampling where close approaches occur; discrete checks do not prove continuous collision-free motion. Keep the figure in its accepted final position in the saved review scene.

Before considering assembly feasible, extend the test to the whole rigid figure and every interacting scene component. Both feet must follow one compatible assembly path; a clear local foot approach does not prove clearance for its ankle, other foot, tail, wings, or nearby structures. Account for any intended assembly sequence explicitly.

## What the Smaug studies actually established

The following are historical case parameters and recorded results, not default settings for another model. No geometry or physical tests were rerun while writing this guide.

| Revision | Method and recorded result | Remaining limitation |
| --- | --- | --- |
| `foot_seats_r1` | Smooth rock expansions reached approximately 4.804 mm near the near foot and 2.194 mm near the far foot. Capped exterior-foot cutters used a provisional 0.10 mm offset. Local seams were repaired; 409 protected object signatures matched. | Small contact areas; no load, adhesive, insertion, or production qualification. |
| `foot_seats_r2` | A shared distal-toe envelope with a 0.65 mm offset removed stone between the far toes; five detached chips were removed. Upper/rear seat and near-foot seat were retained; 419 protected signatures matched. | Final-pose clearance still did not provide a usable entry. |
| `foot_seats_r3` | A straight approach began 40 mm toward the village/front and 1.5 mm above the final position. An endpoint hull with a 0.50 mm vertex margin opened the passage. Actual outer foot below z98.8 mm had zero triangle intersections at 41 tested poses, with approximately 0.498 mm minimum sampled clearance. 420 protected signatures matched. | Only that local foot region was tested. Whole-dragon insertion and structural suitability remain unqualified; visual review pending in the source checkpoint. |

Smaug's geometry and final placement remained unchanged. Recorded terrain samples outside the edited regions showed zero measured deviation; that is sampled evidence, not a global exact-surface proof. The r3 mountain remained one connected component but had 105 boundary and 407 overused edges, so it was not a production-ready mesh.

## Keep the pin prototype separate

The earlier `assembly_r1` study used two parallel pin axes, contoured rock sleeves, separate bored body inserts, nominal 4 mm dowels, provisional 4.4 mm bores, and 4.2/4.4/4.6 mm hole coupons. Those values remained under test. The approved dragon surface was retained exactly; inserts were hidden and separate, and body apertures were deferred. Pins crossing the uncut reference shell were layout guides, not completed joints.

Full-body Boolean integration produced edge defects and was rejected. The useful lesson is to prototype inserts and fit separately, preserve the accepted shell, and integrate only after its manufacturing construction is established. Do not resume rejected fused geometry or switch from adhesive seats back to pins without direction. Neither prototype establishes a complete mount.

## Review and qualification record

Record the fixed figure baseline, permitted support changes, mount method, cutter source and limits, allowance definition, retained contact regions, assembly approach, protected-object checks, new versus pre-existing defects, and precise collision-test scope. Use one compact comparison showing before/after, an exposed seat, and enough of the assembly to judge visibility.

Keep visual acceptance, local fit, whole-assembly access, and load/adhesive performance separate. Before production, resolve wall thickness and topology, evaluate contact area and load path, test fit and bonding with the actual materials, and check the complete assembly sequence. Do not enlarge contacts or add other supports merely because a preliminary seat exists; stay within the requested design scope and present unresolved support needs.

## Local evidence

These paths are relative to the original Dioramas workspace and are not repository dependencies:

- `v3_layered/CHECKPOINT.md`: active choice, protected design, recorded checks, and limitations at collection time.
- `v3_layered/foot_seats_r1/README.md` and `v3_layered/scripts/build_foot_seats_r1.py`: solid foot cutters, local rock expansion, subtraction, and preservation checks.
- `v3_layered/foot_seats_r2/README.md` and `v3_layered/scripts/trim_far_foot_seat_r2.py`: toe-envelope relief.
- `v3_layered/foot_seats_r3/README.md` and `v3_layered/scripts/open_far_foot_entry_r3.py`: swept entry envelope and sampled path checks.
- `v3_layered/assembly_r1/README.md`: separate pin prototype and rejected full-body Boolean integration.

Only this distilled documentation belongs in the skill repository. Scene files, cutters, numerical arrays, renders, and project-specific scripts remain with the source project. Read its current checkpoint before resuming modeling; the historical values here are not an alternative active-state record.
