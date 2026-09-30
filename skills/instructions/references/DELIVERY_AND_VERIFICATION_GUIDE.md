# Delivery and Verification Guide

# Current Precedence — v2.29 Verification Truth, Representative Product Paths and Review Projections

Delivery is blocked when material interview answers are preserved only in the Ledger/chat but not materialized into canonical destinations, or when required source-ingest/reference mappings do not reconcile.

Evidence must prove the claim at the scope required by Acceptance/phase admission. When downstream conclusions depend on representative product inputs/pathways, explicitly distinguish synthetic fixtures/mocks/unit/contract exercises, partial/nonrepresentative integrations, and representative canonical product data/content/configuration + real user/external paths.

Synthetic evidence remains useful but keeps its true scope. It can prove technical execution/integration; it does **not automatically** prove representative product-path behavior or authorize downstream tuning/balance/performance/usability/release conclusions. Re-run or supplement at the stronger scope when required.


## Approval evidence keeps its own authority scope
Where a project requires human/project approval for an exact transition, technical evidence and approval evidence are different things. Build/test/runtime success may prove readiness for the transition; it does not prove permission to cross it. Approval evidence must identify the approving authority and be scoped/current enough for the transition/revision required by project truth.

Likewise, absence of approval does not invalidate evidence from authorized reversible preparation. Report the real state precisely: preparation/readiness may be verified while the gated transition remains pending. Do not promote `ready` to `approved/crossed`, and do not downgrade legitimate preparation to `blocked` merely because the later transition still awaits approval.

Core rules: `TECHNICALLY EXECUTABLE != ADMITTED FOR PRODUCT CONCLUSIONS`; `NEXT ATTRACTIVE TASK != NEXT ADMISSIBLE TASK`. For reusable architecture claims also distinguish `INTEGRATION PROVEN` from `REUSE/COMPOSITION PROVEN` and from `PRODUCT BREADTH`; consumer count alone never upgrades the architecture claim.

---


## Purpose

A detailed specification can still fail if the coding agent:
- builds subsystems before the user-facing path;
- never wires those subsystems into the normal UI;
- hard-codes setup that was meant to be selectable;
- marks acceptance criteria verified using weaker evidence than the criterion requires;
- forgets required screens/actions after context loss.

This guide converts product requirements into machine-readable execution and verification contracts.

---

## 1. Walking-Skeleton Rule

For interactive applications, games, and vertical slices:

**Establish the complete normal-user route early, using placeholders where necessary.**

Example:

```text
Boot
→ Main Menu
→ Setup
→ Selection
→ Rules
→ Match/Primary Experience
→ Pause
→ Results
→ Replay/Return
```

Before deep subsystem work is considered product progress, the agent should be able to traverse the intended top-level route in a running build.

Placeholder content is acceptable during the skeleton phase.
Missing required route nodes are not.

This prevents a technically rich backend from being mistaken for a usable vertical slice.

---

## 2. Machine-Readable Contracts

For nontrivial projects generate:

### `ACCEPTANCE_MATRIX.yaml`
Required unless the goal is trivially small.

Purpose:
Map each acceptance criterion to:
- authoritative sources;
- required user-visible capability;
- dependencies;
- required evidence types;
- forbidden insufficient evidence;
- current verification state.

### `contracts/SYSTEM_INTEGRATION.yaml`
Generate when important rules/state/configuration cross system boundaries.

Purpose:
Record authoritative rule/state ownership, producer-contract-consumer runtime paths, configuration traces and operational extension/data-driven boundaries. It prevents modular-looking files from hiding duplicate ownership or dead contracts.

### `contracts/APP_FLOW.yaml`
Generate for every nontrivial multi-screen, multi-state, lifecycle- or workflow-driven product unless an equivalent canonical workflow graph already exists.

Purpose:
Represent the **complete required product/user lifecycle**, not only the first runnable path. Nodes may be screens, modes, workflow states or externally observable lifecycle states. It must cover normal entry, setup/configuration, primary experience, interruption/recovery, completion/result, persistence/resume/progression and return/replay paths when applicable.

### `contracts/INPUT_ACTIONS.yaml`
Generate when keyboard/device/touch/shortcuts/remapping matter.

Purpose:
Define the complete semantic action registry and required defaults/contexts.

### `contracts/CONTENT_REGISTRY.yaml`
Generate when user-selectable or data-driven content matters.

Examples:
entities, stages, rulesets, products, document types, workflows, modules.

Purpose:
Prevent hard-coded test content from masquerading as a selectable/data-driven feature.

### `verification/AUTHORITY_REACHABILITY.yaml`
Generate for every nontrivial compiled package.

Purpose:
Prove that every active normative authority/required Blueprint is discoverable from the guaranteed bootstrap/JIT router graph. The report is generated evidence from `PROJECT_INDEX.yaml` + registries, never a second routing authority. Any unreachable normative node makes the package incomplete.

### `verification/FRESH_AGENT_RECONSTRUCTION.yaml`
Generate for nontrivial compiled packages before implementation task decomposition/final delivery.

Purpose:
Prove that an agent without the original chat can reconstruct the intended product model, system rationale, guardrails, example/reference semantics, representative flow and authority routing. Detailed policy lives in `FRESH_AGENT_RECONSTRUCTION_GUIDE.md`. Include `AC-PACKAGE-RECONSTRUCTION` (or equivalent stable ID) as a required package-quality criterion.

### `verification/ABSTRACTION_TESTS.yaml`
Generate when modularity/data-driven/extensibility claims require representative/adversarial architecture-expression tests. These examples are not automatically shipping content.

When reuse is an acceptance claim, record the **Representative Proof Set**: the canonical walking-skeleton/reference case that proves integration, the minimum heterogeneous cases that cover material variation axes, and why additional similar consumers are not required for architecture acceptance. Reuse proof is complete when those cases exercise the same canonical owners/capabilities without consumer-local rule duplication/bypass. More similar consumers then provide product/content breadth or scale evidence unless they introduce a new semantic variation axis.

### `verification/INTEGRATION_AUDIT.yaml`
Generate when material cross-system ownership/runtime traces are implemented or changed and the audit result must be durable/release-gating.

Purpose:
Record revision-bound results for ownership conflicts, producer-contract-consumer closure, parallel/bypass paths, dead contracts/configuration, data-driven runtime consumption and feature maturity. It is evidence only; `SYSTEM_INTEGRATION.yaml` remains the semantic authority.

### `verification/E2E_SCENARIOS.yaml`
Generate when completion requires multi-step runtime behavior.

Purpose:
Define exact end-to-end scenarios that prove user/external-visible success.

These files are compact contracts. Detailed explanations remain in `docs/`.

---

## 3. APP_FLOW Contract

Each required screen/state should have a stable ID.

Recommended fields:

```yaml
screens:
  main_menu:
    required: true
    purpose: Entry point
    authority_ids: [DOC-DESIGN]
    authority_section: Main Menu
    implementation_ref: null
    reads: []
    writes: []
    actions:
      play:
        to: player_setup
      options:
        to: options
      quit:
        to: exit

  player_setup:
    required: true
    actions:
      continue:
        to: character_select
      back:
        to: main_menu
```

Also define:
- entry state;
- terminal/completion states;
- normal-user setup/configuration path;
- primary experience states;
- interruption/pause/cancel/back semantics;
- result/completion and replay/return routes;
- persistence/resume/progression transitions where applicable;
- error/recovery routes;
- persistent navigation/workflow owner;
- which state/data survives each transition;
- `plan_stage` for every required node;
- `acceptance_ids` for every required node;
- governing design/reference authority IDs for material user surfaces;
- owning System/Capability IDs where applicable.

### Navigation invariant

Individual screens must not own independent hidden copies of global navigation/setup state.

The implementation must have one coherent navigation/state owner or equivalent architecture.

Every required APP_FLOW transition must be exercised in runtime verification.

---

## 4. INPUT_ACTIONS Contract

Do not represent a complete remapping system with two example bindings.

Define the semantic registry:

```yaml
actions:
  ui_confirm:
    contexts: [ui]
    required: true
    remappable: true
    defaults:
      keyboard: Enter
      device: primary_action

  light_attack:
    contexts: [primary_flow]
    required: true
    remappable: true
    defaults:
      keyboard: J
      device: secondary_action
```

Recommended fields:
- stable action ID;
- display label;
- contexts;
- required/optional;
- default keyboard/device/touch bindings where applicable;
- remappable;
- conflict policy;
- persistence requirement;
- acceptance criteria.

UI should be generated from or validated against the registry where practical.

A remapping feature is incomplete if required semantic actions are missing from the user-facing configuration path.

---

## 5. CONTENT_REGISTRY Contract

When the product claims selectable/data-driven content, define it explicitly:

```yaml
items:
  standard:
    required_for_slice: true
    source: data/items/standard
  alternate:
    required_for_slice: true
    source: data/items/alternate

providers:
  primary:
    required_for_slice: true
    source: config/providers/primary

profiles:
  default:
    required_for_slice: true
```

The normal UI must consume the registry/data source.

A hard-coded runtime choice does not satisfy "selectable" or "data-driven".

---

## 6. ACCEPTANCE_MATRIX Contract

Example:

```yaml
criteria:
  AC-15:
    title: User-facing shell and navigation
    status: unverified
    sources:
      - docs/GAME_FLOW.md
      - docs/UI_AND_MENUS.md
      - contracts/APP_FLOW.yaml
    depends_on: []
    evidence_required:
      - type: runtime_flow
        environment: exported_build
        input: keyboard
      - type: runtime_flow
        environment: exported_build
        input: primary_input_device
      - type: visual_review
    insufficient_evidence:
      - code_inspection
      - scene_exists
      - build_compiles

  AC-22:
    title: Shareable build
    status: unverified
    depends_on: [AC-14, AC-15, AC-16, AC-18]
    evidence_required:
      - type: e2e_scenario
        scenario: primary_full_match
        environment: exported_build
```

Statuses:
- `unverified`
- `in_progress`
- `verified`
- `needs_recheck`
- `blocked`

Do not use `verified` without recorded qualifying evidence.

---

## 7. Evidence Strength Rule

Evidence must be at least as strong as the criterion.

Examples:

```text
"code exists"
≠ feature reachable

"scene loads"
≠ full flow works

"binary launches"
≠ match completes through Results

"headless interaction tests pass"
≠ menus or visuals work

"placeholder boxes exist in code"
≠ coherent visual quality

"one remap control works"
≠ complete remapping UI
```

Code inspection may verify structural criteria.
It cannot verify user-visible runtime or visual criteria unless the criterion explicitly requires only structure.

---


## 7A. Feature Maturity and Runtime Trace

For material features distinguish:

```text
specified -> declared -> connected -> exercised -> verified
```

A parameter, setting, API, schema field, service or data definition at `declared` is not evidence that the feature works. `connected` requires a real consumer/runtime path; `exercised` requires execution; `verified` requires qualifying observed evidence.

For important options/rules/configuration, bind Acceptance to a runtime trace:

```text
Requirement/Setting
-> authority
-> producer/reader/consumer
-> decision/state owner
-> observable effect
-> evidence
```

Use `SYSTEM_INTEGRATION_AND_RUNTIME_TRACE_GUIDE.md` for ownership, dead-contract detection and integration audit rules.

---

## 8. Contradiction / Invalidation Rule

New stronger evidence overrides old weaker evidence.

If:
- the user reports a reproducible failure;
- a runtime scenario fails;
- a required screen is missing;
- a later integration change breaks a previously verified route;

then:
1. mark the directly affected criterion `needs_recheck` or `unverified`;
2. invalidate dependent completion criteria;
3. return to the highest-priority broken requirement;
4. do not preserve a stale "goal complete" state.

Example:

`Start Local Match` is broken.

Therefore a previous claim that:
- full menu flow works;
- end-to-end slice works;
- exported build completes a match;

cannot remain verified.

---

## 9. E2E Scenarios

For interactive products, scenarios should describe observable steps.

Example:

```yaml
scenarios:
  primary_full_match:
    environment: exported_build
    steps:
      - launch_application
      - assert_screen: main_menu
      - action: start_local_match
      - assert_screen: player_setup
      - select_participants
      - select_entitys
      - select_stage
      - configure_rules
      - start_match
      - assert_active_participants_visible
      - assert_stage_stable_and_visible
      - complete_match
      - assert_screen: results
      - rematch
      - return_main_menu
    proves: [AC-14, AC-15, AC-16, AC-18, AC-22]
```

For games, include runtime sanity checks where relevant:
- intended stage/level remains in correct position;
- expected participants spawn;
- primary participants/content are visible within the intended viewport;
- input controls intended participant;
- status/presentation reflects selected setup;
- no debug command is required.

---

## 10. Final Completion Gate

Before an implementation agent may report the master goal complete, derive the claim from the **current canonical state plus actual evidence**, never from code volume, filenames, modules/functions existing, or prior milestone prose.

Required final reconciliation:

0. reread the canonical current-state authority (`STATE` or project equivalent);
1. reread `GOAL.md`, `PROJECT_PLAN.md` admission/completion rules and `ACCEPTANCE_MATRIX.yaml`;
2. enumerate every required criterion/outcome and its required evidence;
3. execute the required evidence on the current intended final worktree/revision — do not substitute existence checks;
4. verify every required criterion is actually `verified` and no dependency/admission condition contradicts the claim;
5. confirm release-relevant integration audit evidence is current/passed when cross-system semantic integrity is in scope;
6. run all release-gating E2E scenarios on the final build/commit;
7. for required browser/app/user-surface/runtime claims, actually exercise that boundary and record current evidence;
8. perform required visual checks using actual runtime output/screenshots;
9. ensure no known user report or contradictory runtime evidence invalidates the claim;
10. ensure required APP_FLOW / INPUT_ACTIONS / canonical content-data paths are reachable through the normal product;
11. reconcile the final report with current STATE/admission/evidence before emitting `COMPLETE`.

Hard invariants:

```text
FILE / MODULE / FUNCTION EXISTS
!= BEHAVIOR VERIFIED

PROJECT_GATE / M0 / FOUNDATION PASS
!= PRODUCT COMPLETE

REQUIRED RUNTIME/BROWSER EVIDENCE NOT EXERCISED
= CORRESPONDING OUTCOME UNVERIFIED

THE FINAL REPORT
= CANONICAL CURRENT STATE + ACTUAL CURRENT EVIDENCE
!= AMOUNT OF CODE PRODUCED
```

If a required check was not actually run, it remains unverified.

---

## 11. PROJECT_INDEX Routing

Machine contracts must be first-class routed sources.

Example:

```yaml
bootstrap:
  must_read:
    - DOC-CONTEXT-HANDOFF
    - DOC-DECISION-COMPENDIUM
    - CONTRACT-SYSTEM-MAP

domains:
  app_flow:
    authority_ids: [CONTRACT-APP-FLOW]
    read_when: [navigation_task, screen_task, end_to_end_task]

  input_actions:
    authority_ids: [CONTRACT-INPUT-ACTIONS]
    read_when: [input_task, options_task, remapping_task]

  acceptance:
    authority_ids: [DOC-GOAL, CONTRACT-ACCEPTANCE-MATRIX]
    read_when: [planning_task, requirement_selection, verification_task, completion_audit]
```

For an active acceptance criterion, the agent should derive the exact required authority IDs from these routes, resolve them through registries, and load them before dependent source edits. The generated reachability validator must also prove that every active normative authority has an incoming bootstrap/JIT route (Blueprint call reachability may extend a routed Blueprint).

This is stronger than asking the agent to infer documents from filenames, folder contents, chat memory, or another prose file.


---

# Stable-ID Routing Note

When `PROJECT_REGISTRY.yaml` and Project Blueprints are enabled, treat raw paths in older examples as illustrative only.

Prefer:
- `authority_ids`
- `implementation_ids`
- Blueprint IDs
- artifact IDs

Resolve the current path through the canonical registries.

This prevents path duplication and stale references after moves/renames.


---

## 12. Reality / User-Surface Verification

For visible or interactive criteria, also apply `USER_SURFACE_VERIFICATION_GUIDE.md`.

Where practical:
- verify affected user-facing slices incrementally after the relevant task;
- interact with the real running product, not only tests/logs;
- inspect screenshots/rendered output for visual requirements;
- keep screenshot evidence sparse and indexed;
- run a fresh final black-box user journey before declaring the goal complete.

A technically correct internal state does not prove the final rendered/interactive state.


## Generated Orientation View Freshness

For every nontrivial compiled project, final delivery/handoff requires a current `PROJECT_ATLAS.html` plus its registered regeneration path. Validate `verification/GENERATED_VIEW_FRESHNESS.yaml`; `stale`, `missing`, or `generator_missing` means the package is not ready for fresh-agent orientation. The Atlas remains non-authoritative and cannot substitute for canonical evidence or source reads.

# Validator negative-control evidence

If the compiler generates a project validator/gate, evidence that it prints PASS on the valid package is insufficient by itself.

The package must retain existing validation evidence showing that the gate also rejects representative intentionally broken temporary cases for the invariants it claims to enforce. Typical negative controls include parse failure, broken ID/reference, orphan authority, registry/file mismatch, stale fingerprint and unmet admission evidence.

A validator that has never demonstrated failure on a known-bad case is `Declared` tooling, not verified project validation.


# v2.24 Walking-skeleton and product-realization distinction

For product implementation:

```text
walking skeleton
= smallest real path proving major architecture/integration assumptions

product completion
= all required product outcomes + acceptance + final user/external evidence
```

Never let a skeleton milestone consume or replace later product outcomes.

When visual identity is material, the early meaningful skeleton should include at least one representative normal-user surface/path using the intended Presentation/Design Core and product-specific visual direction. A generic debug/default UI may accompany it for diagnostics but cannot be the only surface proof.

# Progress truth separation

Use the existing authorities with non-overlapping ownership:

- `PROJECT_PLAN` — stage order, prerequisites and admission rules;
- `STATE` — current execution/admission pointer;
- `ACCEPTANCE_MATRIX` + evidence — maturity/verification truth;
- START/GOAL/CONTINUE/Handoff/Atlas — derived orientation only.

A completion/milestone claim must be rejected when required build/evidence/admission checks contradict it.


# v2.25 Completion-claim provenance

The final completion report itself is a derived view. It must not introduce stronger status than the canonical state/evidence supports.

For every reported material outcome, the implementation runtime should be able to answer:

```text
reported outcome
→ acceptance / outcome ID
→ required evidence IDs/types
→ actual current evidence
→ current revision/worktree
→ verdict
```

If this mapping cannot be produced for a required outcome, report it as `UNVERIFIED`, `PARTIAL`, `BLOCKED` or another project-defined non-complete state rather than inferring success from implementation volume.

A package-validation/project-gate PASS proves only the scope that gate exercised. It must never be promoted into product/runtime/user-surface success unless that scope is itself the required acceptance evidence.


# v2.26 Product-realization coverage verification

Package validation must reject an incomplete realization plan when a required product node is orphaned.

For each required APP_FLOW/workflow node verify:

```text
required node
→ reachable from entry or explicitly independent
→ plan_stage exists
→ Acceptance mapping exists
→ governing owner/authority resolves
```

For the final product verdict additionally require every required node to be `Verified` through its Acceptance evidence or explicitly removed/deferred by canonical authority.

A release-gating E2E scenario should traverse the representative normal-user chain across the whole product, not merely enter the primary runtime. Depending on the product this can include:

```text
launch
→ home/shell
→ setup/configuration
→ primary experience
→ interruption/recovery
→ completion/results
→ persistence/progression
→ replay/return/resume
```

Use project-specific nodes; never force this exact taxonomy when not applicable.


# v2.27 Product Realization authority and coverage

Generate `contracts/PRODUCT_REALIZATION.yaml` for nontrivial products. It is the canonical inventory of required `PR-*` outcomes and may reference APP_FLOW nodes for flow-based outcomes instead of copying transitions.

A generated `verification/PRODUCT_REALIZATION_COVERAGE.yaml` reconciles:

```text
PR outcome
→ source/provenance
→ Responsibility/System/Capability/Contract
→ producer / consumer / surface / content path where material
→ plan stage
→ Acceptance IDs
→ required evidence semantics
→ derived current maturity/verdict from Acceptance/Evidence
```

Coverage fails when a required PR outcome lacks a plan stage, Acceptance mapping, resolvable owner/contract or required flow/content/persistence mapping.

# v2.27 Evidence semantics

Evidence sufficiency is **criterion-specific**, not a universal numeric hierarchy. Evidence records should declare when material:

- `evidence_class`: static inspection | unit test | contract test | fixture integration | synthetic simulation | runtime integration | browser integration | representative scenario | visual inspection | endurance/performance run | differential test | human product judgment | project-specific;
- `boundary`: source | module | contract | process/runtime | browser/app | external system | human judgment;
- `scope`: exact claim/outcome IDs;
- `representative`: true/false/qualified;
- `revision/worktree` and relevant input/config/content fingerprint;
- produced artifact/log/screenshot/trace reference;
- invalidation inputs/triggers.

Acceptance criteria define the required classes/boundaries/representativeness rather than saying merely `test_passed`.

Examples:

```text
fixture integration PASS
!= representative product-path VERIFIED

serialize/deserialize selected fields PASS
!= full Continue/Resume VERIFIED
```

# v2.27 Derived admission engine

`STATE.current_admission` is a cached/current pointer, never authority to create admission.

For a requested/current stage, project_gate derives admission from:

```text
PROJECT_PLAN dependencies + required maturity
→ required PR outcomes / Acceptance IDs
→ current Acceptance verification
→ evidence existence/freshness/scope/representativeness
→ required build/runtime gates
→ DERIVED ADMITTED / BLOCKED
```

If STATE claims a later stage than this derivation permits, fail with a precise contradiction. Do not silently trust or auto-upgrade STATE.

# v2.27 Product Complete vs Release Ready

Use explicit semantics:

- `Implementation Complete` — implementation scope for a bounded item exists; says nothing about final verification unless specified;
- `Product Complete` — every required master-outcome `PR-*` realization outcome is `Verified` with sufficient current evidence;
- `Release Ready` — Product Complete plus project-defined release-only requirements (packaging, deployment, migration, compliance, endurance, release sign-off, etc.).

Do not universally make package-maintenance checks such as Atlas freshness or Fresh-Agent Reconstruction part of **Product Complete**. They are required for compiler/handoff/governance integrity and may be Release Ready gates when the project contract says so. Keep claim scopes explicit.


# Blueprint/code modularity evidence

When modular subsystem boundaries are a material architecture claim, acceptance should prove more than Blueprint files existing.

Representative evidence may include:
- two consumers use the same public module/capability boundary;
- internal source decomposition can change without consumer contract changes;
- a forbidden direct-internal dependency is rejected by static/project-gate validation where feasible;
- runtime/integration trace reaches the canonical implementation boundary;
- consumer-local duplicate domain rules are absent.

A clean Blueprint document without corresponding implementation-boundary conformance is `Declared`, not `Verified`.


# v2.29 Representative product-path heartbeat

When Acceptance contains a representative cross-boundary path, an existing E2E/integration scenario may declare:

```yaml
regression_heartbeat: true
affected_by:
  - "[responsibility/system/capability/change category]"
```

Semantics:
- first prove the scenario normally;
- after a material change that intersects `affected_by`, rerun the narrowest applicable heartbeat before relying on downstream/product-wide claims;
- a heartbeat PASS protects integration continuity but does not prove unrelated Product Realization outcomes;
- do not rerun expensive product-wide scenarios after every trivial edit when dependency/impact information allows a narrower check.

Representative paths are project-neutral: they may be UI/user journeys, API/CLI workflows, jobs, automations, data pipelines, generation pipelines, device/runtime flows or any other observable cross-boundary path.

# v2.29 Deterministic review projections

Where Acceptance requires qualitative/opaque review, define a reproducible observation recipe using existing verification authorities. The recipe should specify, as applicable:
- canonical input/state/artifact/source revision;
- fixed setup/query/view/viewport/fixture;
- generated observation/artifact;
- comparison target or expected traits;
- evidence class and required reviewer/automation;
- invalidation triggers.

The projection is derived evidence, never Product Truth. A failed projection sends repair back through the canonical owner/producer path.

# v2.29 Finish/fidelity verification

Material finish/fidelity requirements belong in Product Realization + Acceptance exactly like functional requirements. They are not satisfied by "implementation exists" or a generic late cleanup pass.

Require evidence appropriate to the criterion: deterministic checks where meaningful, real-surface/output review where observable quality matters, and explicit human product judgment only when the criterion genuinely requires it.


# v2.30 Definition-driven product-engine verification

Where the product claims repeatable/data-driven variants, verification should distinguish:

```text
one example works
!=
the project is reusable as a product engine
```

Preferred representative checks:

1. create/register a second materially different same-type definition;
2. observe it through the normal generic runtime/surface without copied product logic;
3. apply a declared modifier/profile and verify deterministic resolution;
4. change a canonical base/default and prove relative modifiers/consumers inherit the intended change;
5. replace placeholder content/presentation through the declared slot without changing owner/runtime architecture.

When an authoring/admin/builder path is part of the product, the strongest proof creates the new definition through that canonical producer path and observes it in the normal consumer.

If these checks require a new parallel implementation for every instance, mark the claimed reusable Definition-Type/engine seam unverified.


# v2.31 Composition-coherence verification

For each material Composition Invariant, Acceptance should state the observable relationship and adequate evidence boundary.

Preferred pattern:

```text
establish canonical source state
→ exercise representative source change/state
→ allow declared propagation/recompute/regeneration
→ inspect all required dependent projections
→ verify one coherent result
```

A local consumer PASS does not prove the invariant if another required projection was not exercised.

# v2.31 Production-skeleton survivability gate

`Production-Admitted Skeleton` is an evidence-derived claim.

The Plan declares the representative survivability cases; Acceptance defines pass/fail; Evidence records actual results. The gate should reject production admission when any required representative substitution/extension still requires replacing/bypassing the intended canonical owner/runtime path.

Do not require broad production content. The goal is to prove the **shape survives**, not to finish product breadth early.
