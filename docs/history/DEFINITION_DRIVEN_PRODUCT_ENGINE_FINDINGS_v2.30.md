# APC v2.30 — Definition-Driven Product Engine Findings

## Intent

The compiled package should behave like a domain-specific engine/toolkit, not a list of individually hardcoded examples.

A repeatable product type should normally follow:

```text
Owner/System
→ Capability/Contract
→ Archetype/Blueprint
→ Definition/Profile/Composition
→ generic runtime/surface consumer
→ runtime instance/output
```

This is domain-neutral. The same principle applies to catalog items, workflows, reports, policies, integrations, UI/content types, interactive entities, generated artifacts and other repeatable concepts.

## Key invariants

1. Adding a same-type variant should normally be definition/composition work.
2. Variant-specific values do not create new owners.
3. Reusable new behavior extends the lowest correct Capability first.
4. Modifiers target declared seams and never become parallel owners.
5. Generic consumers render/execute definitions; they are not duplicated per instance.
6. Definition/Profile data stays separate from mutable runtime instance state.
7. Placeholder content/presentation uses the final production slots/contracts.
8. The early skeleton is production-survivable when representative substitutions/extensions keep canonical ownership intact.

## Representative proof

A project claiming reusable/domain-authored variants should prove:
- second materially different definition;
- normal generic consumption;
- modifier/profile resolution;
- base-change propagation where relative;
- placeholder→production replacement through the same seam.

If every new instance requires copying controllers/pages/runtimes or state owners, the compiled architecture is not yet acting like a reusable product engine.
