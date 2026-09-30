# APC v2.27 — Product / Realization / Verification Truth Findings

## Trigger

A self-review of the compiler plus the Browser-Physics-TD implementation run showed that Product Truth and Realization Truth had become strong, while the remaining weak point was Verification Truth during long autonomous implementation.

## v2.27 architecture

```text
PRODUCT TRUTH
= intended product/scope/experience

REALIZATION TRUTH
= complete required PR outcomes + flows + responsibilities + stages

VERIFICATION TRUTH
= what current revision evidence actually proves
```

## New bounded authority

`contracts/PRODUCT_REALIZATION.yaml` is the canonical required-outcome inventory. It does not own transitions (APP_FLOW), sequencing/admission (PROJECT_PLAN), or verification status (Acceptance/Evidence).

`verification/PRODUCT_REALIZATION_COVERAGE.yaml` is derived coverage evidence.

## Key hardenings

- project_gate re-derives admission from Plan + PR outcomes + Acceptance + evidence; STATE cannot self-authorize progression;
- evidence declares class, boundary, scope, representativeness, revision and invalidation inputs; sufficiency is criterion-specific;
- Product Complete = all required master-outcome PR nodes Verified; Release Ready adds explicit release-only gates;
- persistence/Continue may use conditional complete runtime-state coverage + differential restore equivalence;
- content dispositions separate production/prototype/test_fixture/debug_only/deprecated and block test leakage;
- consumer adapters receive explicit read/command/write rights; commands do not confer domain ownership;
- implementation agents retain delegated reversible technical freedom while Product/Realization/Acceptance truth stays fixed;
- milestone PASS automatically advances to derived next admission instead of becoming a natural stop point.

## Regression mutants

- false admission;
- E2E status drift;
- partial persistence promoted to Continue;
- test/debug content leakage;
- consumer foreign write;
- green test volume promoted to Product Complete.

## Calibration

Fresh-Agent Reconstruction, Atlas freshness and authority reachability remain essential package/governance integrity checks, but they are not silently conflated with the user-facing semantic meaning of Product Complete. Claim scopes stay explicit.
