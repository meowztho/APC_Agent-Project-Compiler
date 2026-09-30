# APC v2.26 — Whole-Product Realization Graph Findings

## Trigger

A generated browser action/tower-defense package had a strong GOAL and detailed Core-First gameplay plan, but the implementation plan was still skeleton-centric.

Observed package shape:
- START strongly emphasized the first canonical walking skeleton;
- PROJECT_PLAN modeled gameplay/core milestones in detail;
- visual product work appeared much later as one "visual first-map product slice";
- despite being a multi-screen game, the package did not contain `contracts/APP_FLOW.yaml`;
- normal product lifecycle such as Home → setup/match start → arena → pause/results → progression/save → replay/return was therefore not a first-class planned/accepted graph.

This can cause an implementation agent to finish the core runtime and reasonably misread the remaining product scope.

## v2.26 correction

Before `PROJECT_PLAN`, compile a Whole-Product Realization Graph.

Two axes must both be complete:

```text
Architecture axis:
Responsibility → Owner → Capability → Contract → maturity

Product realization axis:
Entry → setup → primary experience → interruption/recovery
→ completion/results → persistence/progression → replay/return/resume
```

Use actual project nodes; do not impose this taxonomy when not applicable.

Every required realization node must map to:
- canonical owner/authority;
- plan stage;
- Acceptance IDs;
- design/reference authority when material;
- reachable transition or explicit independent-entry rationale.

The walking skeleton proves one canonical vertical path. It never substitutes for unbuilt nodes elsewhere in the realization graph.

## Machine-checkable improvement

For multi-screen/multi-state/workflow products, APP_FLOW (or an equivalent canonical workflow graph) becomes required.

`project_gate` should reject:
- required flow node with no plan stage;
- required flow node with no Acceptance mapping;
- unreachable required node;
- product flow that stops at first runnable core experience while required completion/return/resume nodes are declared elsewhere.

This adds product-scope convergence without adding another architecture owner.
