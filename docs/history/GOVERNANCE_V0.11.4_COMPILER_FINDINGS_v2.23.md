# APC v2.23 — Core-First Governance v0.11.4 Compiler Findings

## Source delta adopted
Core-First Governance v0.11.4 adds one bounded invariant for project-defined approval/admission workflows:

```text
An approval/admission gate blocks the gated state transition,
not authorized reversible preparation before it.

A broader implementation request does not implicitly authorize
crossing that transition.
```

## Compiler interpretation
Governance later enforces/consumes project truth. APC must therefore compile the **exact transition boundary** when the user's/project's workflow materially contains an approval gate.

APC now distinguishes:

```text
authorized reversible preparation
→ exact gated transition
→ downstream state/work
```

and records, through existing authorities:
- what preparation may occur before approval;
- the exact state change/side effect that is gated;
- who/what is the approval authority/source;
- what evidence counts as approval;
- what downstream work requires the transition;
- what independent work can continue while approval is pending.

## Important non-conflations

```text
technical readiness/admission evidence != human/project approval
broad implementation intent != approval
approval pending != all preparation blocked
```

The system/runtime owner still owns and performs the transition. Approval authorizes the transition; it does not become a second runtime owner.

## Existing authorities used
No new mandatory project file or approval engine is added.

- `COMPILER_GUIDE.md` — compiler decision/policy.
- workflow/system/state authorities + `SYSTEM_INTEGRATION.yaml` — exact transition semantics and owner trace.
- `PROJECT_PLAN.md` — timing, preparation, gate and downstream dependency.
- Acceptance/evidence — approval evidence scope vs technical readiness evidence.
- `STATE.json` — optional derived current transition-gate slice.
- project-native executable gate — rejects unauthorized transition while allowing declared reversible preparation.
- Fresh-Agent Reconstruction — tests both auto-cross and freeze-all failure directions.

## Deliberately not imported from Governance
v0.11.4 also records an empirically unsuccessful attempt to strengthen generic producer/store anti-bypass prompting and explicitly does not add it to portable Governance. APC does not copy that failed prompt intervention. Existing APC producer-convergence/project-specific executable-gate semantics remain because they are compiled project truth, not extra portable Governance prompt weight.
