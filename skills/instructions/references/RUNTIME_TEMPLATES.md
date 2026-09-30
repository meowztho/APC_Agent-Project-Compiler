# Runtime Template Library

# Current Precedence — v2.27 Product / Realization / Verification Truth Templates

The following shapes supersede conflicting earlier template examples. Scale them to project complexity; do not create unused files merely to satisfy a template.

## `contracts/PRODUCT_REALIZATION.yaml` Template

Canonical scope/outcome inventory; do not store mutable verification truth here.

```yaml
product_realization:
  PR-001:
    title: "[required observable/cross-cutting product outcome]"
    disposition: required            # required|optional|deferred|out_of_scope
    provenance:
      authority_class: USER          # USER|COMPILER|RESEARCHED|DELEGATED
      source_ids: [DEC-..., Q-...]
    flow_node_ids: [FLOW-...]         # empty for non-flow outcomes
    system_ids: [SYS-...]
    capability_ids: [CAP-...]
    contract_ids: [CONTRACT-...]
    producer_ids: []
    consumer_ids: []
    surface_ids: []
    content_ids: []
    plan_stage: M...
    acceptance_ids: [AC-...]
```

Rules:
- every required master-outcome property appears in exactly one canonical PR entry or is explicitly represented by a referenced grouped authority with a unique mapping;
- APP_FLOW owns transitions and may be referenced from PR outcomes;
- current verification state is derived from Acceptance/Evidence, not written here as an independent truth;
- cross-cutting outcomes such as persistence/performance/authoring/compatibility belong here even when they are not a screen/flow node.

## `verification/PRODUCT_REALIZATION_COVERAGE.yaml` Template

Generated/derived evidence view:

```yaml
source_fingerprints:
  product_realization: "..."
  project_plan: "..."
  acceptance: "..."
coverage:
  PR-001:
    plan_stage_resolves: true
    owners_resolve: true
    acceptance_ids_resolve: true
    derived_maturity: Verified
    evidence_ids: [EVID-...]
    evidence_sufficient: true
summary:
  required_total: 1
  verified: 1
  unverified: 0
  verdict: PASS
```

This file never owns product scope, stage rules or verification status.

## Whole-product realization coverage before `PROJECT_PLAN`

Before writing milestone order, enumerate the required product lifecycle/flow using the project's actual domain language.

```markdown
## Whole-product realization coverage
| Node / Outcome ID | User-visible purpose | Owner/System/Capability | Flow predecessors | Plan stage | Acceptance IDs | Surface/reference IDs | Disposition |
|---|---|---|---|---|---|---|---|
| FLOW-... | ... | ... | ... | M... | AC-... | REF-... | required |
```

This table is a readable view. Machine-checkable mappings belong in `APP_FLOW`/workflow contracts and Acceptance.

No required node may be left with an empty plan stage or Acceptance mapping.

## `docs/PROJECT_PLAN.md` material dependency-bound stage
```markdown
## Phase / Milestone — [Name]
- Outcome: [...]
- Product-realization node/outcome IDs: [...]
- System/Capability/Blueprint IDs: [...]
- depends_on:
  - id: [SYS/CAP/AC/...]
    required_maturity: [existing project maturity/acceptance state]
- entry_evidence: [...]
- admission_condition: [...]
- why_now: [...]
- implementation_objective: [...]
- integration_objective: [...]
- exploratory_before_admission:
    allowed: [...]
    may_support: [...]
    must_not_authorize: [...]
- completion_condition: [...]
- unlocks: [...]
- reuse_obligations: [...]
- deferred_not_now: [...]
- replan_triggers: [...]
- approval_boundary: # optional; only when project truth defines a human/project gate
    reversible_preparation_allowed: [...]
    gated_transition: [...]
    approval_authority: [...]
    approval_evidence: [...]
    downstream_requires_transition: [...]
    broad_request_counts_as_approval: false
```
Not every trivial stage needs every field. Use the richer shape where downstream validity materially depends on upstream maturity/evidence. An approval boundary blocks its exact transition, not authorized reversible preparation before it.

## `provenance/SOURCE_INGEST_MANIFEST.yaml`
```yaml
sources:
  SRC-001:
    identity: "..."
    hash: "..."
    extracted_question_ids: []
    material_reference_ids: []
reconciliation:
  expected: 0
  materialized: 0
  unresolved: []
```

## `verification/INTERVIEW_MATERIALIZATION.yaml`
```yaml
questions:
  Q-001:
    ledger_present: true
    verbatim_present: true
    material: true
    canonical_destinations: [DEC-001, SYS-001, AC-001]
    materialized: true
unresolved_material: []
```

## `docs/REFERENCE_REGISTER.md` / reference map
For each material reference record stable ID, source identity/URL/date/version, provenance, adopt|adapt|reject|inspiration-only traits, rationale, non-implied traits/exclusions and affected System/Capability/Acceptance IDs.

## `contracts/EXTENSION_POINTS.yaml` (conditional only)
Record public seam ID, owner System/Capability, accepted definition/module/provider types, registration/validation, dependencies, allowed variation/substitution, forbidden writes/bypasses, runtime trace IDs, version/schema/migration behavior and acceptance evidence.

## Runtime/read state additions
`STATE.context` supports `required_source_ids`, current-session `loaded_source_ids`, Atlas `inspected_view_ids`, current change classification and admission status/pointers where material. Generated evidence records prove reachability/freshness/read behavior but never become a second architecture truth.

---


## AGENTS.md Template

# AGENTS.md

## Architecture Law — Read First

> Before any material behavior change: resolve/classify the canonical capability. Implement reusable behavior at the lowest reusable semantic owner, then compose/configure the consumer. Do not fork shared behavior for delivery speed.

## Engineering Behavior

- Work as a pragmatic senior software engineer who minimizes total work and maintenance, not merely immediate effort.
- At the start of a session, after context loss, or when the working directory changes, identify the project/repository root, follow applicable instructions, initialize Git if this is a coding project with no repository and policy does not forbid it, then inspect Git status and relevant diffs. Reconstruct only the context needed for the current task; do not repeatedly scan or reread unchanged parts of the repository.
- Scale investigation to the change: for clearly local, low-risk edits, inspect only the directly affected file and nearby context; broaden the investigation only when behavior, contracts, data flow, generated sources, or cross-cutting dependencies may be affected.
- Before adding or rewriting anything, determine whether the requirement is already satisfied or can be solved through reuse, simplification, configuration, correction, or removal. Prefer the smallest robust and reversible change that fully satisfies the requirement. Preserve existing architecture, behavior, conventions, and user changes unless the task requires otherwise. Avoid speculative abstractions, unnecessary files or dependencies, unrelated cleanup, and changes that create more future maintenance than they remove.
- Fix root causes rather than symptoms. Inspect the relevant implementation, call sites, interfaces, state transitions, side effects, and tests before editing. Use tools to make progress rather than repeatedly describing intended actions. After each result, update your understanding and take the next useful step; if an approach fails, change it instead of repeating it unchanged.
- Use Git for recoverability and keep unrelated changes untouched. Verify changes with the narrowest relevant tests, builds, type checks, runtime evidence, and contract validation, expanding verification only when justified. Never claim to have read, changed, executed, tested, or verified something unless it actually happened.
- For long work, keep runtime/resume pointers concise, but do not compress or discard canonical project authorities, interview provenance, or context handoff. Do not create process documents for small tasks.
- Ask questions only when unresolved ambiguity could materially affect behavior, data, security, architecture, cost, destructive actions, product/design intent, or scope. Otherwise state the assumption and proceed.
- Prefer minimally sufficient responses. Do not optimize brevity at the expense of correctness. Keep relevant context active, but do not repeat it unless it changes the answer.
- Use the `independent-review` skill for consequential, high-risk, difficult-to-verify, or materially blocked work when available; it supplements, never replaces, your own investigation and verification.

## Execution

- Follow the phase gates in the project's execution policy/runtime contract; work toward the complete objective in `GOAL.md`, not merely the current task.
- When `contracts/AGENT_RUNTIME_PROFILE.yaml` exists, use its actual runtime bindings for skills/hooks/subagents/external tools; never move project truth into provider-specific memory or adapters.
- On first implementation of a nontrivial compiled package, ensure authority reachability, Atlas freshness/orientation, and Fresh-Agent Reconstruction gates are passed/current before task work; unreachable normative authorities, stale/uninspected required Atlas orientation, or material misunderstanding are package defects, not reasons to improvise privately.
- Continue while useful work toward the goal remains.
- Do not ask the user to continue or choose the next task.

## Context

- Project files are authoritative; conversational memory is not.
- Do not preload project documentation.
- `PROJECT_INDEX.yaml` is the canonical discoverability router. Every active normative authority must be reachable from its bootstrap/domain routes; an orphan authority is invalid. For nontrivial projects it also routes the required non-authoritative `PROJECT_ATLAS.html` view and its regeneration tool separately.
- On a fresh session/context recovery, validate/regenerate and inspect the routed Project Atlas once for whole-project orientation; record it separately from authority reads. For the active requirement, derive `STATE.context.required_source_ids` from `PROJECT_INDEX.yaml`, resolve them through registries, and actually read them before material source edits. A file existing in the repository is not evidence that it was loaded.
- Before modifying target paths, resolve any applicable registered/local `AGENTS.md` or `AGENTS.override.md` files along those target paths and read only newly applicable local instructions.
- Do not preload instruction files from unrelated subtrees.
- When Project Blueprints are used, use `blueprints/REGISTRY.yaml` to resolve behavior ownership and calls.
- Read only sources required for the current requirement.
- Reread exact/canonical information from its source when it matters.
- A partial read is not proof that the relevant section was fully read.

## Creation / Paths / Duplicates

- Before any material new behavior is implemented, classify the delta against `SYSTEM_MAP`/`CAPABILITY_GRAPH`: data/modifier, compose existing capability, extend/new reusable capability, adapter/surface, core-rule change, or explicit one-off exception. Search for an existing canonical path first; when reuse is plausible, run the counterfactual second-consumer test. Implement reusable behavior at the lowest canonical capability first, then compose the consumer. Delivery speed does not authorize a consumer-local parallel core; a one-off exception requires explicit semantic rationale.
- Before creating or changing a durable behavior path, inspect the registries, applicable System Map/Capability Graph/Integration contracts, runtime call/data path, and relevant repository area for the authoritative owner.
- Prefer `reuse -> extend -> correct -> intentional replace`; never build a parallel path around an existing owner/contract merely because it is locally easier.
- Shared reusable behavior belongs to its canonical master system/module. Consumers compose it through declared contracts/data/profiles/modifiers rather than copying it. For material value variation, use explicit merge semantics; relative modifiers inherit future base changes, while absolute replacement is intentional and explicit.
- When a reusable Definition Type/generic consumer already exists, add same-type variants through definitions/profiles/capability composition/modifiers. Do not create per-instance pages/controllers/runtimes merely because the new variant has different content or values.
- Important mutable state and product/domain rules must have one authoritative owner. Cross-system mutation must use declared contracts/owners; do not write another system's state through an incidental shortcut.
- A field/API/config/schema existing is only declaration evidence. Trace producer -> contract/data -> consumer -> owner -> effect and prove the relevant runtime path before treating the feature as implemented.
- Treat create/move/rename/delete as incomplete until registries, references, generated-source declarations, tests, and contract validation are updated.

## Verification

- Do not mark work complete without appropriate evidence. Before a final completion claim, reread canonical STATE + Plan/Acceptance, map every required outcome to current actual evidence, execute missing required gates, and derive the final report from that reconciliation rather than implementation volume.
- A file/module/function name, project-gate PASS, M0/foundation PASS, or code quantity is never evidence that broader product behavior works.
- If a change affects user-visible or interactive behavior, invoke the selected real-user verification adapter and run the smallest practical surface check once it is runnable.
- Before master-goal completion, capability discovery and fresh release-gating black-box verification are mandatory for applicable user-facing surfaces. If an applicable interactive/screenshot tool is exposed but not actually invoked, the goal is not complete.
- Prefer real UI/browser/app interaction plus visual inspection for visual/interactive criteria; static inspection cannot substitute.
- Task completion does not imply requirement or goal completion.
- New contradictory runtime/user evidence reopens affected criteria.
- Final release-gating verification must run on the current worktree/revision.
- After each meaningful task, reevaluate the current requirement and `GOAL.md`, then select the next unmet requirement.

## Resume

- Reconstruct execution state from the context-rich prompt plus `PROJECT_INDEX.bootstrap`, registries, `STATE.json`, and current required authorities.
- Reset/rebuild session `loaded_source_ids` and `inspected_view_ids` after fresh session/major context loss; validate Atlas freshness before re-inspection; do not reconstruct project facts from old chat summaries when authorities exist.
---

## PROJECT_CORE.md Template

# PROJECT_CORE.md

## Project Identity
[What is being built.]

## Compilation Scale
[simple | moderate | complex/nontrivial] — controls documentation/gate formality only; core-first composition and single-authority rules still apply at every scale.

## Intended User / Audience
[Who uses or experiences it.]

## Intended Experience / Outcome
[What it should feel like or accomplish.]

## Product Direction
- [...]
- [...]

## Non-Negotiable Principles
- [...]
- [...]

## Major Scope Boundaries

### Included
- [...]

### Excluded / Deferred
- [...]

## Authority
This file is global orientation only. Detailed behavior, design, assets, architecture, content, and domain rules are defined by sources routed through `PROJECT_INDEX.yaml`.

---

## PROJECT_INDEX.yaml Template

`PROJECT_INDEX.yaml` is the **single canonical discoverability/retrieval router**. Every active normative authority must be reachable from either `bootstrap.must_read` or a domain route. Required generated views/tools are routed separately through explicit view/tool IDs. Do not maintain a second authority graph.

```yaml
schema_version: 1

project:
  core_id: DOC-PROJECT-CORE
  goal_id: DOC-GOAL
  state_id: STATE-RUNTIME
  registry: PROJECT_REGISTRY.yaml
  blueprint_registry: blueprints/REGISTRY.yaml
  acceptance_id: CONTRACT-ACCEPTANCE-MATRIX

bootstrap:
  # A fresh implementation agent loads these after the context-rich START snapshot
  # and before the first material source edit.
  must_read:
    - DOC-CONTEXT-HANDOFF
    - DOC-DECISION-COMPENDIUM
    - CONTRACT-SYSTEM-MAP
    - CONTRACT-SYSTEM-INTEGRATION
    - DOC-PROJECT-PLAN
  when_present:
    - CONTRACT-CAPABILITY-GRAPH
    - CONTRACT-ARCHITECTURE-GUARDRAILS
    - CONTRACT-AGENT-RUNTIME-PROFILE
  routers:
    - PROJECT_REGISTRY.yaml
    - blueprints/REGISTRY.yaml
    - ACCEPTANCE_MATRIX.yaml
  inspect_view_ids:
    - VIEW-PROJECT-ATLAS
  maintenance_tool_ids:
    - TOOL-GENERATE-PROJECT-ATLAS

domains:
  interview_provenance:
    authority_ids:
      - DOC-USER-VISION
      - DOC-INTERVIEW-LEDGER
      - CONTRACT-INTERVIEW-COVERAGE
    read_when:
      - product_decision_trace
      - ambiguity_resolution
      - user_intent_change
    dependencies: []

  design:
    authority_ids:
      - DOC-DESIGN
    read_when:
      - ui_task
      - ux_task
      - visual_task
    sections:
      DOC-DESIGN:
        principles: "Design Principles"
        screens: "Screens and States"
    dependencies: []

  navigation:
    authority_ids:
      - CONTRACT-APP-FLOW
      - BP-FLOW-PRIMARY
    read_when:
      - navigation_task
      - screen_task
      - end_to_end_task
    dependencies:
      - design

  capability_hierarchy:
    authority_ids:
      - CONTRACT-SYSTEM-MAP
      - CONTRACT-CAPABILITY-GRAPH
    read_when:
      - new_feature_task
      - consumer_change_task
      - architecture_task
    dependencies: []

  example_system:
    authority_ids:
      - DOC-SYSTEM-EXAMPLE
      - BP-SYSTEM-EXAMPLE
    read_when:
      - example_system_task
    dependencies:
      - capability_hierarchy

  verification:
    authority_ids:
      - CONTRACT-USER-SURFACE-VERIFICATION
      - VERIFICATION-E2E-SCENARIOS
      - VERIFICATION-FRESH-AGENT-RECONSTRUCTION
    read_when:
      - verification_task
      - completion_audit
      - release_gate
    dependencies: []

# Resolve artifact IDs through PROJECT_REGISTRY.yaml.
# Resolve Blueprint IDs through blueprints/REGISTRY.yaml.
# Every active normative artifact must be routed here directly, or (for a Blueprint)
# reachable from a routed Blueprint through registered call edges.
# Generated prompts/Atlas/evidence binaries/support files remain non-normative.
# Required generated views/tools are nevertheless explicitly routed and freshness-validated.
# Keep paths out where stable IDs can be used. Add project-specific domains; remove unused examples.
```
---

## GOAL.md Template

# GOAL.md

## Master Outcome
[Complete observable result.]

## User-Visible Success State
A user can:
1. [...]
2. [...]

## In Scope
- [...]

## Out of Scope
- [...]

## Evidence record semantics

```yaml
evidence:
  EVID-001:
    evidence_class: representative_scenario
    boundary: browser_app
    scope_ids: [PR-001, AC-001]
    representative: true
    revision: "<commit/worktree fingerprint>"
    input_fingerprints:
      - "<config/content/data fingerprint>"
    artifact_refs: ["verification/...png", "verification/...json"]
    invalidated_by:
      - source_paths: ["src/...", "content/..."]
```

Acceptance defines required evidence semantics explicitly, for example:

```yaml
required_evidence:
  - classes: [representative_scenario]
    boundary: browser_app
    representative: true
  - classes: [visual_inspection]
    boundary: browser_app
```

Do not use one global evidence-strength ranking when different evidence kinds prove different claim dimensions.

## Acceptance Criteria

### AC-01 — [Title]
[Observable condition.]

Verification:
- [...]

### AC-02 — [Title]
[Observable condition.]

Verification:
- [...]

## Completion Condition
The goal is complete only when every required acceptance criterion is satisfied by current actual evidence and required end-to-end verification succeeds.

The final completion report must be derived from canonical current state + actual evidence. File/module/function existence, code volume, a project-gate/M0 pass, or completion of an individual task/component/milestone/blueprint/delegated assignment does not complete this goal.

---

## STATE.json Template

`STATE` is the single canonical **current execution/admission pointer**. It must not duplicate product rules or Acceptance verification truth. `PROJECT_PLAN` owns transition/admission rules; Acceptance/Evidence owns verified maturity. CONTINUE/Handoff/Atlas/status prose are derived views and must reconcile to these authorities.


```json
{
  "goal_artifact_id": "DOC-GOAL",
  "current_requirement": null,
  "current_task": null,
  "current_change": {
    "id": null,
    "request": null,
    "classification": null,
    "target_consumers": [],
    "master_system": null,
    "capability_path": [],
    "existing_owner": null,
    "new_owner": null,
    "reuse_check": {
      "searched_existing_paths": false,
      "result": null
    },
    "second_consumer_test": {
      "applicable": null,
      "candidate_capability": null,
      "plausible_consumers": [],
      "shared_semantics": null,
      "variation_axes": [],
      "result": null,
      "rationale": null
    },
    "representative_proof_set_id": null,
    "one_off_exception_rationale": null,
    "status": null
  },
  "current_blueprint_ids": [],
  "verified": [],
  "in_progress": [],
  "blocked": [],
  "relevant_implementation_ids": [],
  "context": {
    "session_id": null,
    "required_source_ids": [],
    "loaded_source_ids": [],
    "required_view_ids": ["VIEW-PROJECT-ATLAS"],
    "inspected_view_ids": [],
    "view_gate_status": "not_evaluated",
    "load_evidence_mode": null,
    "load_gate_status": "not_evaluated"
  },
  "workspace": {
    "repo_root": null,
    "branch": null,
    "baseline_head": null,
    "baseline_dirty_paths": []
  },
  "next_action": null,
  "last_verification": null
}
```

Use stable IDs instead of duplicated paths when possible. Keep runtime pointers here, not project canon.
---

## START_PROMPT.md Template

The generated Start Prompt is a **context-rich denormalized orientation snapshot**, not a pointer chain. It may be long. Populate it from canonical authorities and mark it non-authoritative.

```markdown
GENERATED ORIENTATION SNAPSHOT — canonical details live in the referenced project authorities. Regenerate this prompt when those authorities materially change.

# PROJECT MISSION
[Write the actual complete product outcome in direct natural language. Do not say merely "read GOAL.md". Explain what is being built, for whom, and what observable result constitutes success.]

# USER VISION / INTENT
[High-signal vision, desired feel/outcome, product identity, important non-goals, and selected verbatim wording where paraphrase loses meaning.]

# MATERIAL INTERVIEW CONTEXT
[Group material compiler questions + verbatim user answers that define behavior, architecture, terminology, extension semantics, negative requirements, or otherwise prevent plausible misunderstanding. For large interviews include all architecturally/behaviorally material Q/A, not only one-line summaries.]

# DECISIONS THAT DEFINE THE PRODUCT
[Readable normalized decisions/rationale/rejected alternatives from DECISION_COMPENDIUM.]

# MASTER SYSTEM / CAPABILITY / COMPOSITION MODEL
[Inline the core systems, reusable capability hierarchy, what they own, how consumers compose them, important producer→contract→consumer paths, authoring/content model, value-resolution semantics, and relevant ordinary-product responsibilities/dispositions whose omission would mislead.]

# CORE-FIRST ARCHITECTURE LAW
[Classify later user deltas before source edits. Missing reusable behavior is added at the lowest canonical capability first, then composed into consumers. Local differences are data/profiles/modifiers unless an intentional new capability is required.]

# CRITICAL USER / SYSTEM FLOWS
[Normal-user journey(s), important lifecycle/failure/recovery paths, and cross-system behavior that must remain coherent.]

# ARCHITECTURE GUARDRAILS
[Important forbidden implementations / negative requirements.]

# ACCEPTANCE / REALITY MODEL
[Explain what must actually be connected, exercised and verified; include key release-gating outcomes.]

# PRODUCT REALIZATION ROADMAP
[List the complete recommended product stages/outcomes at useful granularity. Mark foundation/walking-skeleton stages as proofs, not product completion. Show the required outcomes that remain afterward.]

# VISUAL / USER-SURFACE TARGET
[When material: compact product-specific gestalt, applicable reference/baseline IDs, essential hierarchy/layout/style constraints and anti-generic-default traits. Exact work still requires inspecting the registered references.]

# CURRENT PROJECT STATE / FIRST EXECUTION TARGET
[Greenfield: first admitted coherent walking skeleton, what it proves, and what later stages it unlocks. Existing project: current admitted stage, verified state, unmet/reopened outcomes, blockers, current revision.]

# REQUIRED BOOTSTRAP AUTHORITIES
[List `PROJECT_INDEX.yaml` plus the direct `bootstrap.must_read` authority IDs/files. These MUST be loaded after this orientation and before the first material source edit. Do not make the agent discover them through multi-hop prose.]

# REQUIRED WHOLE-PROJECT ORIENTATION VIEW
[For nontrivial projects: `VIEW-PROJECT-ATLAS` / `PROJECT_ATLAS.html`. Validate/regenerate if stale, then inspect once for whole-project orientation. It is generated and non-authoritative; exact rules still require canonical source reads.]

# AUTHORITIES FOR PRECISION
[List current-domain canonical files/sections/IDs. `PROJECT_INDEX.yaml` remains the canonical JIT router for every other normative authority.]

# EXECUTION RULES
- The project mission above is the goal. Reading/validating project files is an execution step, not the goal.
- Identify repository root, applicable instructions, Git state/relevant diffs, actual runtime/verification capabilities and current evidence.
- Before creating behavior, inspect canonical system/semantic owner and existing implementation path. Reuse → Extend → Correct → intentionally Replace before creating another path.
- Load the required bootstrap authorities. For nontrivial projects validate/regenerate and inspect the routed Atlas once, then derive the active requirement's `required_source_ids` from `PROJECT_INDEX.yaml`; material source edits wait until those authorities were actually read in the current context/session.
- Resolve/load only additional JIT exact authorities/skills needed for the active requirement after this orientation.
- Treat a current task as one step toward the master outcome, never as product completion.
- Verify units, integration, value/config propagation, user-surface behavior and final release gates with the evidence required by Acceptance.
- Ask only unresolved material user-owned product/content/design questions. Do not re-ask answered interview questions or ask for reversible technical choices.
- A foundation/scaffold/walking skeleton is an early proof, not product completion. After each milestone reconcile the remaining product-realization roadmap and continue through the next admissible stage.
- For material user-surface work, load/inspect the registered visual authorities and preserve the product-specific visual target; generic/default styling is not completion when a specific visual identity exists.
- Continue autonomously while useful work remains.
```

After the direct orientation above, the agent may consult `CONTEXT_HANDOFF.md`, `docs/DECISION_COMPENDIUM.md`, `contracts/SYSTEM_MAP.yaml`, `contracts/CAPABILITY_GRAPH.yaml`, `contracts/SYSTEM_INTEGRATION.yaml`, `ACCEPTANCE_MATRIX.yaml`, registries and detailed system authorities for precision.

Before implementation, ensure `verification/AUTHORITY_REACHABILITY.yaml` is passed/current, then inspect `contracts/INTERVIEW_COVERAGE.yaml` and `verification/FRESH_AGENT_RECONSTRUCTION.yaml`. A COMPLETE package should not need new product questions; PARTIAL packages ask only unresolved material user-owned items.

---

## CONTINUE_PROMPT.md Template

`CONTINUE_PROMPT` rehydrates product + state; it must not be only a list of files.

```markdown
GENERATED CONTINUATION SNAPSHOT — canonical details remain in project authorities.

# PRODUCT / MASTER OUTCOME
[One compact but concrete paragraph describing the actual product outcome.]

# VERIFIED STATE
[What is currently proven on this worktree/revision.]

# REMAINING PRODUCT REALIZATION
[Current admitted stage + concise remaining roadmap/outcomes. A completed foundation/skeleton must not look like master completion.]

# VISUAL / USER-SURFACE TARGET
[When the current/next stage affects the user surface, rehydrate the applicable gestalt/reference IDs/baseline.]

# CURRENT UNMET REQUIREMENT
[Requirement + why it matters to the full product. Explicitly label it as a step, not the goal.]

# RELEVANT SYSTEM / CAPABILITY / OWNERSHIP CONTEXT
[Systems, capability path, canonical owner/runtime path, composition/value-resolution context and current-change classification required for this work.]

# REQUIRED SOURCES TO REREAD
[Authority IDs/files/sections derived from `PROJECT_INDEX.yaml` for this requirement. These form the current context-load gate.]

# NEXT USEFUL ACTION
[Concrete next action from durable state.]

Resume from actual repository/Git/evidence state. Preserve unrelated changes. Do not recreate verified work or infer project truth from old conversation memory. Load only JIT context/skills after this rehydration, verify the affected unit/integration/user-surface slice, update evidence/state, then select the next unmet requirement. Continue until the full master outcome is verified or a genuine user-only product decision blocks useful work.
```

If the implementation agent is genuinely fresh or suffered major context loss, use START-level orientation again, including Atlas freshness/inspection for nontrivial projects, before the normal continuation loop.

---

## GOAL_PROMPT.md Template

A Goal Prompt must **state the goal directly**. Do not make `GOAL.md` inspection the apparent objective.

```markdown
/goal

# MASTER OUTCOME
[Inline the complete observable product outcome from GOAL.md in direct natural language.]

# NON-NEGOTIABLE PRODUCT + ARCHITECTURE CONSTRAINTS
[Key system/capability/composition/behavior/negative constraints, including the core-first change law.]

# CURRENT VERIFIED STATE
[Fresh summary generated from durable Acceptance/Evidence/STATE, not conversation memory.]

# REMAINING / REOPENED REQUIREMENTS
[List the actual unmet product requirements. A document-read/validation task may support them but is never itself the master goal unless the product really is that artifact.]

# COMPLETION CONDITION
[Inline the required acceptance/evidence/end-to-end condition. State that the final report is derived from canonical current state + actual evidence, never code/file existence.]

Reading `GOAL.md`, contracts, Blueprints, source and evidence is an execution step for precision, not the goal. The current task is one step toward the master outcome. Continue autonomously through successive unmet/reopened requirements until the master outcome above is verified on the current final worktree.

Before creating/changing behavior, classify the request against the canonical system/capability hierarchy; add missing reusable capability first, then compose the consumer. Reuse/extend/correct before parallel implementation. Treat field/API/config existence only as declaration; trace and exercise its live consumer/effect. For user-facing work, completion requires applicable real-surface interaction/visual evidence. If a blocking finish hook exists, its validator verdict governs eligibility to stop.
```

The generated Goal Prompt should directly include current master outcome/state each time it is issued. It may then point to `GOAL.md`, `ACCEPTANCE_MATRIX.yaml`, `SYSTEM_MAP`, `CAPABILITY_GRAPH`, `SYSTEM_INTEGRATION`, registries and exact authorities for detail.

---

## ACCEPTANCE_MATRIX.yaml Template

```yaml
goal: GOAL.md

criteria:
  AC-01:
    title: "[Criterion title]"
    required: true
    status: unverified
    authority_ids:
      - "DOC-..."
      - "BP-..."
    depends_on: []
    evidence_required:
      - type: "[unit_test|runtime_flow|e2e_scenario|visual_review|build|artifact_inspection]"
    insufficient_evidence:
      - code_inspection
    evidence: []
```

Rules:
- `verified` requires evidence matching `evidence_required`.
- New contradictory evidence changes status to `needs_recheck` or `unverified`.
- Dependent completion criteria must not remain verified after a dependency is invalidated.


---

## contracts/APP_FLOW.yaml Template

Use the project's actual nodes. They may represent user surfaces, workflow states, lifecycle states, processing stages or other externally meaningful states; do not impose a domain-specific taxonomy.

```yaml
entry: FLOW-ENTRY
workflow_owner: SYS-APPLICATION-FLOW

nodes:
  FLOW-ENTRY:
    kind: surface_or_state
    required: true
    purpose: "[normal product entry]"
    system_ids: [SYS-...]
    capability_ids: [CAP-...]
    authority_ids: [DOC-..., REF-...]
    design_authority_ids: []
    plan_stage: M1
    acceptance_ids: [AC-...]
    actions:
      primary:
        to: FLOW-SETUP

  FLOW-SETUP:
    kind: surface_or_state
    required: true
    purpose: "[required setup/configuration before primary experience]"
    system_ids: [SYS-...]
    authority_ids: [DOC-...]
    design_authority_ids: [DOC-DESIGN]
    plan_stage: M2
    acceptance_ids: [AC-...]
    actions:
      continue:
        to: FLOW-PRIMARY
      back:
        to: FLOW-ENTRY

  FLOW-PRIMARY:
    kind: primary_experience
    required: true
    purpose: "[core normal-user experience]"
    system_ids: [SYS-...]
    plan_stage: M3
    acceptance_ids: [AC-...]
    actions:
      interrupt:
        to: FLOW-INTERRUPT
      complete:
        to: FLOW-RESULT

  FLOW-INTERRUPT:
    kind: interruption_recovery
    required: true
    purpose: "[pause/cancel/recovery state when applicable]"
    plan_stage: M3
    acceptance_ids: [AC-...]
    actions:
      resume:
        to: FLOW-PRIMARY
      exit:
        to: FLOW-ENTRY

  FLOW-RESULT:
    kind: completion_result
    required: true
    purpose: "[result/completion state]"
    plan_stage: M4
    acceptance_ids: [AC-...]
    actions:
      continue:
        to: FLOW-PROGRESSION
      replay:
        to: FLOW-PRIMARY
      home:
        to: FLOW-ENTRY

  FLOW-PROGRESSION:
    kind: persistence_progression
    required: "[true when product requires it]"
    purpose: "[save/unlock/progression/resume behavior]"
    plan_stage: M4
    acceptance_ids: [AC-...]
    actions:
      home:
        to: FLOW-ENTRY
      next:
        to: FLOW-SETUP

terminal_states: []
global_rules:
  one_canonical_flow_owner: true
  required_nodes_must_have_plan_stage: true
  required_nodes_must_have_acceptance: true
  derived_surfaces_do_not_own_global_flow_state: true
```

Required checks:
- every required node is reachable from `entry` or explicitly marked as an intentional independent entry;
- every required node maps to a plan stage and Acceptance;
- every material user surface maps to its design/reference authority;
- normal user completion has a coherent return/replay/resume path where the product requires one.

Do not stop the flow graph at the first runnable primary-experience node.

---

## contracts/INPUT_ACTIONS.yaml Template

```yaml
actions:
  ui_confirm:
    label: Confirm
    contexts: [ui]
    required: true
    remappable: true
    defaults:
      keyboard: Enter
      device: primary_action

  ui_back:
    label: Back
    contexts: [ui]
    required: true
    remappable: true
    defaults:
      keyboard: Escape
      device: secondary_action

  example_gameplay_action:
    label: "[Display label]"
    contexts: [primary_flow]
    required: true
    remappable: true
    defaults:
      keyboard: null
      device: null

conflict_policy: "[project rule]"
persistence_required: true
```

Enumerate the complete required semantic action set. Do not use a couple of example bindings as a substitute for the registry.


---

## contracts/CONTENT_REGISTRY.yaml Template

Every content definition that can enter runtime should declare a shipping disposition when material:

```yaml
content:
  CONTENT-EXAMPLE:
    disposition: production   # production|prototype|test_fixture|debug_only|deprecated
```

Rules:
- `test_fixture` / `debug_only` must be unreachable from normal shipping compositions/defaults/progression/user flows;
- `prototype` is not silently promoted to production; promotion is an explicit authority change;
- project_gate may traverse default compositions/registries/APP_FLOW load paths to reject leakage.


```yaml
content_types:
  example_type:
    entries:
      example_id:
        required_for_current_goal: true
        definition_artifact_id: "DATA-..."
        selectable_through_normal_ui: true
        acceptance:
          - AC-XX
```

Use for entities, stages, rulesets, templates, modes, products, modules, or other data-driven/selectable content.


---

## verification/E2E_SCENARIOS.yaml Template

```yaml
scenarios:
  primary_flow:
    release_gate: true
    environment: exported_or_production_like_build
    steps:
      - launch_application
      - assert_state: entry
      - perform_normal_user_setup
      - enter_primary_experience
      - assert_required_runtime_entities_visible
      - complete_primary_experience
      - assert_state: results_or_success
      - exercise_replay_or_return
    proves:
      - AC-XX
```

For visual/interactive applications add concrete layout/viewport/stability checks where relevant.

---

## PROJECT_REGISTRY.yaml Template

```yaml
schema_version: 1

artifacts:
  DOC-PROJECT-CORE:
    kind: document
    path: PROJECT_CORE.md
    responsibility_key: DOC.PROJECT.CORE
    status: active
    owner: project
    normative: true
    discoverability_required: true

  CONTRACT-ACCEPTANCE-MATRIX:
    kind: contract
    path: ACCEPTANCE_MATRIX.yaml
    responsibility_key: CONTRACT.ACCEPTANCE.MATRIX
    status: active
    owner: project
    normative: true
    discoverability_required: true

  CONTRACT-APP-FLOW:
    kind: contract
    path: contracts/APP_FLOW.yaml
    responsibility_key: CONTRACT.APP_FLOW
    status: active
    owner: application
    normative: true
    discoverability_required: true

  VERIFICATION-AUTHORITY-REACHABILITY:
    kind: verification_report
    path: verification/AUTHORITY_REACHABILITY.yaml
    responsibility_key: VERIFICATION.AUTHORITY.REACHABILITY
    status: active
    owner: project
    normative: false
    discoverability_required: false
    generated:
      source_artifact_ids: [PROJECT-INDEX, PROJECT-REGISTRY, BP-REGISTRY]
      generator_artifact_id: TOOL-VALIDATE-PROJECT-CONTRACTS
      edit_policy: generated_only

  TOOL-GENERATE-PROJECT-ATLAS:
    kind: generator_tool
    path: tools/generate_project_atlas.py
    responsibility_key: TOOL.GENERATE.PROJECT.ATLAS
    status: active
    owner: project
    normative: false
    discoverability_required: true

  VIEW-PROJECT-ATLAS:
    kind: generated_view
    path: PROJECT_ATLAS.html
    responsibility_key: VIEW.PROJECT.ATLAS
    status: active
    owner: project
    normative: false
    discoverability_required: true
    generated:
      source_selector: atlas_v1
      source_artifact_ids: [DOC-PROJECT-CORE, DOC-USER-VISION, DOC-DECISION-COMPENDIUM, CONTRACT-SYSTEM-MAP, CONTRACT-ACCEPTANCE-MATRIX]
      generator_artifact_id: TOOL-GENERATE-PROJECT-ATLAS
      source_fingerprint: null
      generated_at_revision: null
      edit_policy: generated_only

  VERIFICATION-GENERATED-VIEW-FRESHNESS:
    kind: verification_report
    path: verification/GENERATED_VIEW_FRESHNESS.yaml
    responsibility_key: VERIFICATION.GENERATED.VIEW.FRESHNESS
    status: active
    owner: project
    normative: false
    discoverability_required: false
    generated:
      source_artifact_ids: [PROJECT-REGISTRY, VIEW-PROJECT-ATLAS]
      generator_artifact_id: TOOL-VALIDATE-PROJECT-CONTRACTS
      edit_policy: generated_only

# Artifact IDs are stable across path moves.
# Active responsibility_key values are unique.
# Use supersedes/aliases only for deliberate migrations.
# Mark generated/transformed artifacts with canonical source/recipe + generator; durable fixes go upstream, then regenerate and verify consumers.
# Active normative/discoverability_required artifacts must be reachable from PROJECT_INDEX.
# Generated views/prompts/evidence binaries/support files and ordinary implementation entries are normally normative: false.
# `owner` here is artifact maintenance/domain metadata, not rule/state decision authority.
```

---

## blueprints/REGISTRY.yaml Template

```yaml
schema_version: 1

blueprints:
  BP-EXAMPLE:
    responsibility_key: SYSTEM.EXAMPLE
    type: system
    artifact_id: BPFILE-EXAMPLE
    status: active
    owner: example_domain
    calls: []
    supersedes: null

# Exactly one active blueprint owns each Blueprint responsibility_key.
# This does not replace SYSTEM_INTEGRATION rule/state ownership.
```

---

## Reusable Definition Type / Definition composition template

Use when the product has repeatable variants realized by shared runtime/surface consumers.

This is a semantic template, not a required new file. Place it in the existing canonical domain/content/definition/Blueprint authority; do not invent a universal `ARCHETYPES.yaml`/`DEFINITION_TYPES.yaml` unless the project actually needs a dedicated owner.

```yaml
definition_types:
  TYPE-EXAMPLE:
    owner_system_id: SYS-...
    capability_contract_ids: [CAP-...]
    definition_schema_id: DATA-...
    generic_runtime_consumer_id: MOD-...
    generic_surface_consumer_id: MOD-...   # optional
    instance_state_owner_id: SYS-...
    allowed_modifier_ids: [MOD-...]
    authoring_path_id: TRACE-...

definitions:
  DEF-EXAMPLE-A:
    definition_type_id: TYPE-EXAMPLE
    profile_ids: [PROFILE-...]
    capability_ids: [CAP-...]
    modifier_ids: []
    presentation:
      slot_a: ASSET-...
    parameters:
      example_value: 1
```

Acceptance should prove that another materially different `DEF-*` of the same archetype can reach the same generic consumer/runtime without a copied owner or per-instance implementation path.

## Project Blueprint `*.bp.yaml` Template

```yaml
blueprint:
  id: BP-EXAMPLE
  responsibility_key: SYSTEM.EXAMPLE
  type: system
  version: 1
  authority_ids: []
  implementation_ids: []

interface:
  inputs: []
  outputs: []

state:
  owned: []
  reads: []
  writes: []

nodes:
  N001:
    type: event
    op: entry
  N010:
    type: action
    op: example_action
  N999:
    type: exit
    op: success

edges:
  - from: N001
    to: N010
  - from: N010
    to: N999

invariants: []
acceptance: []
```

Use `call` nodes with stable Blueprint IDs for reusable behavior instead of copying graphs.

---

## contracts/VERSION_CONTROL.yaml Template

```yaml
git:
  required: true
  initialize_if_missing: true
  create_gitignore_before_first_stage: true
  inspect_on_session_start: true
  preserve_unrelated_changes: true
  destructive_cleanup_without_user_request: false

commits:
  policy: verified_milestone
  auto_commit_greenfield_agent_owned_repo: true
  auto_commit_existing_or_shared_repo: false

verification:
  record_revision: true
  final_release_gates_must_run_on_current_worktree: true
```

Adapt to explicit user/repository policy.

---

## `.agents/skills/independent-review/SKILL.md` Template

Generate this only when an equivalent applicable skill is not already available.

```markdown
---
name: independent-review
description: Run an unbiased read-only implementation review for consequential, high-risk, difficult-to-verify, or materially blocked coding work. Do not use for routine low-risk changes.
---

# Independent Review

Run a narrowly scoped read-only reviewer only for consequential, high-risk, difficult-to-verify, or materially blocked work.

The reviewer may be an isolated subagent or an available external model through an approved provider. Do not wait for rate-limited providers or duplicate routine investigation. Review supplements, never replaces, the primary agent's own investigation and verification.

To avoid anchoring, give the reviewer:
- the original requirements;
- complete applicable instructions;
- relevant raw diffs and files;
- verification commands and their actual output.

Do not pass:
- the implementation agent's narrative;
- its conclusions;
- its confidence;
- its justification.

The reviewer must independently derive expected behavior from the original requirements and verify material claims directly when necessary and feasible.

Require evidence-based findings that materially affect correctness, stated requirements, regressions, security, or maintainability. Exclude style-only, speculative, and unnecessary-hardening suggestions.

The primary agent must fix each material finding, reject it with evidence, or explicitly accept it, with at most one challenge-response round.

Use a different model for additional review only when a high-risk issue remains unresolved.
```

---

## Contract Validator Requirements

When the generated project uses registries/Blueprint contracts, generate a small deterministic validation tool appropriate to the project's language/tooling.

Validate applicable invariants:
- unique artifact IDs;
- every active artifact with `discoverability_required: true` is reachable from the appropriate `PROJECT_INDEX` bootstrap/domain/view/tool route, regardless of whether it is normative;
- every routed authority/Bootstrap ID resolves;
- every active normative Blueprint is directly routed or reachable through registered `call` edges from a routed Blueprint;
- generated/non-normative artifacts never satisfy normative authority coverage; required generated views/tools are validated through their separate explicit routes;
- zero unreachable normative authorities/required Blueprints; emit `verification/AUTHORITY_REACHABILITY.yaml`;
- unique artifact IDs;
- unique active responsibility keys;
- unique active Blueprint responsibility ownership;
- every implemented active Blueprint resolves to registered implementation anchor(s);
- implementation boundaries do not claim duplicate durable responsibilities;
- known internal implementation artifacts are not used as public cross-system entry points when the Blueprint declares a public boundary;
- registry paths exist;
- artifact references resolve;
- Blueprint `call` targets resolve;
- definitions referencing a reusable Definition Type resolve its owner/capabilities/generic consumer;
- same-type production definitions do not register conflicting active runtime/surface owners;
- modifier definitions target declared seams and do not claim target ownership;
- CAPABILITY_GRAPH parent systems/capabilities/consumers/Acceptance IDs resolve and has no cycles where cycles are forbidden;
- SYSTEM_INTEGRATION referenced systems/artifacts/contracts/Acceptance IDs resolve;
- ARCHITECTURE_GUARDRAILS referenced decisions/systems/Acceptance IDs resolve when present;
- ABSTRACTION_TESTS case/system references resolve when present;
- FRESH_AGENT_RECONSTRUCTION references a real required Acceptance ID and has an allowed evidence mode/status;
- duplicate active decision/state owners are rejected where ownership is declared;
- APP_FLOW states/transitions resolve;
- Acceptance IDs referenced by Blueprints/contracts exist;
- deprecated artifacts are not active route targets;
- generated artifacts declare source/generator when required;
- required generated views have current source fingerprints/revisions; stale required views fail generated-view freshness;
- `VIEW-PROJECT-ATLAS` exists/is fresh for nontrivial projects and its generator resolves.

Run after structural changes and before milestone/final verification.

### Runtime convergence/progress checks

Where the compiled project can express them deterministically, the project-native gate should support progress checks in addition to package-structure checks:

- current `STATE` stage/admission pointer is valid under `PROJECT_PLAN`;
- claimed stage completion has required Acceptance/Evidence;
- required build/typecheck/test commands for that gate currently pass;
- generated/derived views do not claim a conflicting current stage;
- registered active implementation owners remain unique;
- affected material Composition Invariants have current evidence when their canonical source/relationship changed;
- a `production_admitted` skeleton has all declared survivability Acceptance evidence satisfied;
- project-specific producer→canonical data/store/query→runtime probes pass where data-driven behavior is a material claim;
- every required product-flow/workflow node has a valid plan stage + Acceptance mapping;
- required flow nodes are reachable from entry or intentionally declared independent;
- the realization graph includes required completion/result/return/resume paths rather than stopping at the first runnable core experience.

Do not hard-fail arbitrary unregistered files solely from filename heuristics. Suspicious `*_corrected`, `*_full`, `*_new`, `*_v2`, etc. may be surfaced for review, but semantic duplicate ownership requires stronger project-specific evidence.

### Reference authority-reachability algorithm

The generated validator should implement the equivalent of:

```text
artifact_roots =
  PROJECT_INDEX.project.core_id
  + PROJECT_INDEX.project.goal_id
  + PROJECT_INDEX.project.acceptance_id
  + PROJECT_INDEX.bootstrap.must_read
  + existing PROJECT_INDEX.bootstrap.when_present
  + PROJECT_INDEX.bootstrap.inspect_view_ids
  + PROJECT_INDEX.bootstrap.maintenance_tool_ids
  + all PROJECT_INDEX.domains.*.authority_ids that are artifact IDs

blueprint_roots =
  all routed Blueprint IDs from bootstrap/domain routes

reachable_blueprints =
  DFS/BFS(blueprint_roots, blueprints/REGISTRY.yaml calls)

required_discoverable_artifacts =
  active PROJECT_REGISTRY artifacts
  where discoverability_required == true

required_normative_artifacts =
  active PROJECT_REGISTRY artifacts
  where normative == true and discoverability_required != false

required_blueprints =
  active normative Blueprints

FAIL if:
  any route/root ID is unresolved
  OR required_discoverable_artifacts - artifact_roots is non-empty
  OR required_normative_artifacts - artifact_roots is non-empty
  OR required_blueprints - reachable_blueprints is non-empty
```

Do not infer reachability merely from a filename appearing in arbitrary prose. Explicit router/registry graph edges are the machine contract.

---

## Nested `AGENTS.md` Template

Generate this only for a coherent subtree with shared local engineering rules that materially refine repository-root behavior.

```markdown
# [Scope Name] Instructions

- [Only subtree-wide working rule that differs from/refines root behavior.]
- [Reference stable artifact/contract IDs when useful.]
- [Require local validation relevant to this subtree.]

# Do not duplicate root rules.
# Do not put concrete feature behavior here; keep it in Blueprints/specs/contracts.
```

Also register the scope in `PROJECT_REGISTRY.yaml`.

Before delivery, compare local rules against root `AGENTS.md` and remove semantic duplicates.

---

## `verification/AUTHORITY_REACHABILITY.yaml` Template

This is generated validation evidence, **not a second routing authority**. Recompute it from `PROJECT_INDEX.yaml`, registries, active Blueprint calls, and artifact metadata.

```yaml
schema_version: 1
generated_from:
  - PROJECT_INDEX.yaml
  - PROJECT_REGISTRY.yaml
  - blueprints/REGISTRY.yaml

bootstrap_roots:
  - DOC-CONTEXT-HANDOFF
  - DOC-DECISION-COMPENDIUM
  - CONTRACT-SYSTEM-MAP

counts:
  active_normative_artifacts: 0
  routed_normative_artifacts: 0
  active_normative_blueprints: 0
  reachable_normative_blueprints: 0

unreachable_artifact_ids: []
unreachable_blueprint_ids: []
unresolved_route_ids: []
status: passed
```

Rules:
- `status: passed` requires zero unreachable/unresolved required nodes;
- report paths may be included for diagnostics but stable IDs determine identity;
- do not hand-edit this report to make validation pass; correct `PROJECT_INDEX`/registries and regenerate it.

---

## Project Atlas Generator Contract

For every nontrivial project, generate/register a reproducible command (for example `tools/generate_project_atlas.py`; use an equivalent project-native tool when more appropriate). It must:

1. resolve canonical input IDs through `PROJECT_REGISTRY.yaml`/`PROJECT_INDEX.yaml`;
2. read only canonical/project-state sources selected for Atlas presentation;
3. compute a stable source-set fingerprint that changes when a selected source is added, removed, moved through registry metadata, or materially changed;
4. render `PROJECT_ATLAS.html` from `PROJECT_ATLAS_TEMPLATE.html` or an equivalent generated template;
5. embed source fingerprint + current repository/project revision + generator command in the HTML metadata/banner;
6. never parse the previous Atlas as an input or preserve manual edits;
7. fail loudly on unresolved required inputs instead of emitting a deceptively fresh view.

Register the generator as `TOOL-GENERATE-PROJECT-ATLAS` (or a stable project-equivalent ID) and the view as `VIEW-PROJECT-ATLAS`. The generator is tooling, not project truth.

## `verification/GENERATED_VIEW_FRESHNESS.yaml` Template

Generated validation evidence, never project truth.

```yaml
schema_version: 1
views:
  VIEW-PROJECT-ATLAS:
    path: PROJECT_ATLAS.html
    required_for_nontrivial_project: true
    generator_artifact_id: TOOL-GENERATE-PROJECT-ATLAS
    source_artifact_ids: []
    expected_source_fingerprint: "sha256:..."
    embedded_source_fingerprint: "sha256:..."
    generated_at_revision: "..."
    status: fresh  # fresh | stale | missing | generator_missing

status: passed
```

Rules:
- recompute the source set/fingerprint from registry/router metadata;
- any source addition/removal/change covered by the Atlas selector makes the view stale;
- a required stale/missing Atlas blocks fresh-session orientation, handoff and final completion until regenerated;
- never hand-edit fingerprint/status to pass.

## `verification/VISUAL_CHECKPOINTS.yaml` Template

Generate for projects with meaningful visual/UI state.

```yaml
checkpoints:

  example_state:
    surface: "[project-specific user/rendered surface type]"
    route:
      - "[normal user steps to reach state]"
    proves:
      - AC-XX

    expectations:
      - "[specific visible requirement]"
      - "[specific absence of failure/duplication/overlap]"

    interaction:
      - action: "[user action]"
        expect_state: "[next state]"

    evidence:
      interaction_required: true
      screenshot: true
```

Expectations must come from authoritative design/goal/flow sources.

---

## `verification/EVIDENCE_INDEX.yaml` Template

```yaml
evidence:

  EV-EXAMPLE-001:
    criterion: AC-XX
    type: screenshot_review
    checkpoint: example_state
    artifact: verification/evidence/EV-EXAMPLE-001.png
    revision: "git:<revision-or-worktree-id>"
    result: pass
    observations:
      - "[short factual observation]"
    review_projection_id: null  # optional stable observation recipe
    stale: false
```

Use this index to keep raw screenshots/videos out of routine context.

Reload raw evidence only when a current task/criterion requires it.

---

## `contracts/USER_SURFACE_VERIFICATION.yaml` Template

```yaml
policy:
  incremental_check_after_observable_change: true
  final_black_box_required: true
  final_black_box_on_current_revision: true

surfaces:
  primary:
    type: "[project-specific surface/interface/artifact type]"
    launch_method: "[normal user entry point]"
    preferred_interaction: "[computer_use|browser|playwright|engine_automation|real_cli|real_client]"
    visual_evidence: "[required|optional|not_applicable]"

evidence_budget:
  checkpoint_screenshots_only: true
  capture_on_failure: true
  summarize_immediately: true
  store_raw_artifacts_outside_active_context: true
```

---

## Representative Product Path / Heartbeat fields

Use inside the existing project-appropriate E2E/integration scenario authority; do not create a new product authority solely for this.

```yaml
scenario_id: PATH-REPRESENTATIVE-001
representative_product_path: true
regression_heartbeat: true
affected_by:
  - SYS-...
  - CAP-...
  - "[change category]"
proves: [AC-...]
notes: "Heartbeat protects only the claims/scopes mapped above."
```

## Deterministic Review Projection fields

Attach to the existing Acceptance/checkpoint/scenario/evidence mechanism that owns the criterion.

```yaml
review_projection:
  id: RPJ-001
  canonical_source_ids: [PR-..., SYS-..., DATA-...]
  fixed_setup: "[stable input/state/query/view/fixture]"
  observation: "[screenshot|render|report|diff|sample output|trace|project-specific]"
  comparison_target_ids: []
  invalidated_by: ["[relevant source/state/config changes]"]
  derived_not_authoritative: true
```

## Final Black-Box Scenario Template

Add one or more release-gating scenarios to `verification/E2E_SCENARIOS.yaml`:

```yaml
scenarios:

  final_primary_user_journey:
    release_gate: true
    regression_heartbeat: true
    affected_by: ["[project-specific responsibilities/change categories]"]
    evidence_type: user_surface_black_box
    run_on_current_revision: true

    steps:
      - build_or_package_target
      - launch_from_normal_user_entry_point
      - assert_initial_visible_state
      - perform_primary_setup_flow
      - exercise_required_interactions
      - inspect_visual_checkpoints
      - complete_primary_user_goal
      - exercise_required_interruption_recovery_completion_return_paths

    screenshots:
      checkpoints:
        - "[important stable state]"
        - "[important final state]"

    fail_if:
      - unexpected_black_screen
      - duplicate_required_ui
      - required_visible_element_missing
      - navigation_break
      - runtime_entity_missing
      - obvious_layout_failure
```


---

## `contracts/EXECUTION_POLICY.yaml` Template

```yaml
schema_version: 1

phases:
  - BOOTSTRAP_REPOSITORY
  - DISCOVER_CAPABILITIES
  - BIND_AGENT_RUNTIME
  - LOAD_BOOTSTRAP_CONTEXT
  - VERIFY_AUTHORITY_REACHABILITY
  - VALIDATE_PROJECT_RECONSTRUCTION   # once for fresh compiled projects when required
  - SELECT_REQUIREMENT
  - RESOLVE_REQUIRED_AUTHORITIES
  - LOAD_JIT_CONTEXT
  - VERIFY_CONTEXT_LOAD_GATE
  - CLASSIFY_CHANGE_ARCHITECTURE
  - RESOLVE_SKILLS_FOR_REQUIREMENT
  - BLUEPRINT_OR_REUSE
  - IMPLEMENT_UNIT
  - VERIFY_UNIT
  - INTEGRATE
  - VERIFY_INTEGRATION
  - AUDIT_SYSTEM_INTEGRATION      # when material cross-system behavior changed
  - VERIFY_USER_SURFACE
  - HYGIENE
  - RECORD_MILESTONE

finalization:
  - FINAL_CONTRACT_AUDIT
  - FINAL_BUILD_TEST
  - FINAL_USER_SURFACE_GATE
  - INDEPENDENT_REVIEW_IF_TRIGGERED
  - FINAL_GIT_CHECK

rules:
  walking_skeleton_priority: true
  user_surface_after_observable_change: true
  user_surface_tool_invocation_required_when_available: true
  final_black_box_required_for_user_facing_product: true
  scoped_hygiene_after_green_requirement: true
  authority_reachability_gate: true
  required_authority_load_gate_before_source_edit: true
  reconstruction_gate_before_first_implementation: true
  core_first_change_classification_before_source_edit: true
```


---

## `contracts/AGENT_RUNTIME_PROFILE.yaml` Template

Generate for nontrivial autonomous projects when the execution harness offers customizable agent primitives. Populate from actual discovery, not model-name assumptions.

```yaml
schema_version: 1

runtime:
  provider: null
  client_or_harness: null
  version: null

capabilities:
  hierarchical_instructions:
    available: false
    mechanism: null
  agent_skills:
    available: false
    standard_compatible: null
    project_path: null
    supports_multi_skill_composition: null
  lifecycle_hooks:
    available: false
    session_start_context: null
    user_prompt_context: null
    pre_tool_gate: null
    post_tool_observer: null
    pre_compact: null
    post_compact: null
    stop_or_finish_gate: null
  subagents:
    available: false
    isolated_context: null
    parallel: null
  mcp_or_external_tools:
    available: false
    mechanism: null
    permission_model: null
    read_only_mode_available: null
    trust_reviewed: false
  persistent_memory:
    available: false
    canonical_project_truth_allowed: false
  workflows_or_commands:
    available: false
  worktrees_or_sandboxes:
    available: false

bindings:
  instruction_kernel: AGENTS.md
  provider_adapter: null
  skill_router: null
  architecture_law_context_hook: null
  authority_reachability_validator: null
  required_source_load_observer: null
  required_source_gate_hook: null
  change_classification_gate_hook: null
  context_rehydration_hook: null
  completion_gate_hook: null
  integration_audit_hook: null
  reconstruction_executor: null
  independent_review_executor: null
  external_tool_adapter: null

fallbacks: []
```

Rules:
- product truth never lives only in this profile or a provider customization;
- provider-specific instruction files are thin generated adapters;
- semantic lifecycle events map to provider-specific hook names here;
- if hooks are unavailable, deterministic validators remain explicit runtime gates;
- memory is non-canonical and must not be required for reconstruction.

---

## `verification/TOOL_CAPABILITIES.yaml` Template

```yaml
schema_version: 1

capabilities:
  interactive_desktop:
    available: false
    adapter: null
    verified_by: null

  browser_interaction:
    available: false
    adapter: null
    verified_by: null

  screenshot_capture:
    available: false
    adapter: null
    verified_by: null

  engine_runtime:
    available: false
    adapter: null
    verified_by: null

selected:
  user_surface_adapter: null
  screenshot_adapter: null
  fallback_adapter: null

surface_gate:
  required: false
  final_scenario: null
  require_interactive_invocation: false
  require_visual_artifacts: false
  status: not_evaluated
```

Populate from tools actually exposed by the current harness/session, not from assumptions about the model/provider.


---

## Implementation Blueprint `*.impl.bp.yaml` Template

```yaml
blueprint:
  id: BP-IMPL-EXAMPLE
  responsibility_key: IMPL.EXAMPLE
  type: implementation_boundary
  version: 1
  implements: []
  artifact_ids:
    - IMPL-EXAMPLE-FACADE
  internal_artifact_ids: []

boundary:
  kind: module_or_component
  public_entry_artifact_id: IMPL-EXAMPLE-FACADE
  consumers_must_not_import_internal_artifacts: true

interface:
  public_operations: []
  inputs: []
  outputs: []

state:
  owns: []
  must_not_own: []

dependencies:
  reads: []
  calls_public_boundaries: []
  forbidden_internal_dependencies: []

operations:
  example_operation:
    preconditions: []
    postconditions: []
    failure_behavior: []

invariants: []

verification:
  unit: []
  integration: []
  debug_probes: []
```

Use for a nontrivial module/service/component/controller/adapter or cohesive code boundary with an independently meaningful responsibility. One Blueprint may anchor multiple internal source files; do not force one Blueprint per class/function.


---

## Data Blueprint `*.data.bp.yaml` Template

```yaml
blueprint:
  id: BP-DATA-EXAMPLE
  responsibility_key: DATA.EXAMPLE
  type: data_structure
  version: 1
  artifact_id: DATA-EXAMPLE

schema:
  fields: []

collection_invariants: []

operations:
  - create
  - lookup
  - update

serialization:
  required: false

verification:
  tests: []
  debug_probes: []
```

Use for shared/stateful/invariant-rich schemas, registries, stores, queues, catalogs, or collections. Do not Blueprint trivial local arrays/lists.

---

## `contracts/CAPABILITY_GRAPH.yaml` Template

Generate when reusable semantic hierarchy below/among master systems matters.

```yaml
schema_version: 1

capabilities:
  CAP-EXAMPLE:
    parent_system: SYS-EXAMPLE
    parent_capability: null
    kind: reusable_capability
    responsibility: "[semantic reusable behavior]"
    owns: []
    parameters: []
    consumers: []
    authority_ids: []
    acceptance: []
```

Rules:
- top-level domain ownership remains in `SYSTEM_MAP.yaml`;
- hierarchy is semantic, not a class/folder tree;
- consumer values/modifiers do not become capability ownership;
- runtime edges must agree with `SYSTEM_INTEGRATION.yaml`;
- new behavior requested for a consumer is classified before implementation and descends to the lowest reusable capability that should own it.

---

## `contracts/SYSTEM_INTEGRATION.yaml` Template

Generate for nontrivial projects when material rules/state/configuration cross system boundaries. Keep detailed behavior in system authorities; this contract records semantic ownership and cross-system runtime edges.

```yaml
schema_version: 1

ownership:
  RULE-EXAMPLE:
    kind: rule
    decision_owner: SYS-EXAMPLE-A
    state_owner: SYS-EXAMPLE-B
    producers: [SYS-EXAMPLE-C]
    allowed_writers: [SYS-EXAMPLE-B]
    readers: [SYS-EXAMPLE-D]
    forbidden_owners: []

  STATE-EXAMPLE:
    kind: mutable_state
    state_owner: SYS-EXAMPLE-B
    mutation_contracts: [DATA-EXAMPLE-RESULT]
    mutation_producers: [SYS-EXAMPLE-A]
    allowed_writers: [SYS-EXAMPLE-B]
    readers: [SYS-EXAMPLE-A, SYS-EXAMPLE-D]

runtime_paths:
  TRACE-EXAMPLE:
    requirement_ids: [REQ-EXAMPLE]
    producer: SYS-EXAMPLE-C
    contract: DATA-EXAMPLE-COMMAND
    consumer: SYS-EXAMPLE-A
    decision_owner: SYS-EXAMPLE-A
    state_owner: SYS-EXAMPLE-B
    side_effects:
      - effect: EFFECT-EXAMPLE
        owner: SYS-EXAMPLE-B
    failure_or_invalid_path: []
    acceptance_ids: [AC-EXAMPLE]

composition_invariants:
  INV-EXAMPLE:
    statement: "[relationship that must remain coherent]"
    canonical_source_owner: SYS-EXAMPLE-A
    source_ids: [STATE-EXAMPLE]
    dependent_projections:
      - consumer: SYS-EXAMPLE-B
        relation: "[derived/read/propagated relationship]"
        update_semantics: deterministic_derivation
      - consumer: SYS-EXAMPLE-D
        relation: "[second required projection]"
        update_semantics: live_read
    forbidden_local_overrides: []
    acceptance_ids: [AC-EXAMPLE]

configuration_traces:
  CFG-EXAMPLE:
    source: SETTING-EXAMPLE
    consumed_by: SYS-EXAMPLE-A
    affects: RULE-EXAMPLE
    observable_effect: "[required runtime effect]"
    acceptance_ids: [AC-EXAMPLE]

value_resolution_traces:
  VALUE-EXAMPLE:
    base_source: DATA-MASTER-DEFINITION
    layers:
      - source: DATA-MASTER-DEFINITION
        op: replace_base
      - source: PROFILE-EXAMPLE
        op: add
      - source: CONSUMER-EXAMPLE
        op: add
    consumer: SYS-EXAMPLE-A
    base_change_should_propagate: true
    acceptance_ids: [AC-EXAMPLE]

extension_tests:
  EXT-EXAMPLE:
    claim: data_driven
    operation: "[add/change content/config]"
    must_not_require_changes_to: [IMPL-CORE-EXAMPLE]
    acceptance_ids: [AC-EXAMPLE]
```

Rules:
- one active decision owner per material rule and one active state owner per material mutable state unless an explicit coordinated-ownership model exists;
- producers do not gain write authority merely because they detect/emit a condition;
- a declared setting/field/API is not connected until a runtime consumer/path is identified;
- important traces bind to Acceptance/evidence;
- relative modifier traces must prove that canonical base changes propagate; explicit replacement is used only when intentional independence is required;
- local implementation may vary, but bypass/parallel paths that duplicate the authoritative semantic responsibility are forbidden.
- Composition Invariants own no state; they reference existing owners and required relationships;
- when a canonical source changes, every affected required projection must remain coherent through its declared update semantics;
- consumer-local compensating values/rules are forbidden when they merely mask a broken shared invariant.

---

## `contracts/SKILL_REQUIREMENTS.yaml` v2 Template

```yaml
schema_version: 2

policy:
  installed_does_not_mean_active: true
  minimal_jit_routing: true
  inspect_installed_before_external_search: true
  review_external_source_before_install: true
  global_install_requires_policy_or_user_permission: true
  project_local_skills_may_be_generated_when_justified: true

requirements:
  SKILLREQ-EXAMPLE:
    capability: "[vendor-neutral capability]"
    needed_by: [SYS-EXAMPLE]
    load_when: ["[task/requirement class]"]
    priority: medium
    discovery_terms: ["..."]
    resolution:
      status: unresolved
      skill: null
      source: null
      scope: null                 # global | project | harness
      version_or_commit: null
      content_hash: null
      license: null
      reviewed: false
      rejection_reason: null
```

Rules:
- requirements describe capabilities first, not preferred vendor names;
- concrete resolution is recorded after discovery/review;
- do not repeatedly rediscover a recorded rejected candidate unless relevant facts changed;
- route only skills needed by the current requirement/system context;
- skills never replace project authorities;
- correctness must not require simultaneous multi-skill activation.

---

## Project-local `.agents/skills/<name>/SKILL.md` Template

Generate only for a repeated repository procedure not adequately covered by an existing skill.

```markdown
---
name: [project-workflow-name]
description: [Narrow trigger, repository scope, and useful boundary/negative trigger.]
---

# Purpose
[Repeated project workflow.]

## Required authorities
- [SYSTEM/CONTRACT/ARTIFACT IDs to resolve/read before work]

## Procedure
1. Inspect an existing representative implementation/content item.
2. Use the canonical master systems and declared extension points.
3. [Workflow-specific steps.]
4. Run the mapped validation/evidence checks.

## Must not
- Do not duplicate canonical behavior or data into this skill.
- Do not create a parallel owner for an existing master-system responsibility.
- [Workflow-specific guardrail.]

## Verification
- [Deterministic/interactive evidence expected.]
```

The description is a routing surface. Make it concrete enough to trigger for the intended workflow and narrow enough to avoid unrelated tasks.


---


---

## `docs/USER_VISION.md` Template

```markdown
# User Vision

## Authority Metadata
- Artifact ID: `DOC-USER-VISION`
- Routed by: `PROJECT_INDEX.yaml` interview-provenance/bootstrap route(s)
- Provenance: `VQ-*` / `Q-*`

This file preserves high-signal user intent in the user's original wording. Normalized behavior remains authoritative in the routed system/design/contracts.

## VQ-001 — [Anchor title]

Source / context:
[where/when this wording occurred]

Verbatim user wording:
> [exact quote in original language]

Compiled intent:
- [...]

Authority scope:
- [product/design/system domains this anchor constrains]

Destination authorities:
- [stable artifact/system/contract IDs]

Status: active
```

Do not turn the complete interview into vision anchors; use `INTERVIEW_LEDGER.md` for full Q/A provenance.

---

## `docs/DECISION_COMPENDIUM.md` Template

```markdown
# Decision Compendium

## Authority Metadata
- Artifact ID: `DOC-DECISION-COMPENDIUM`
- Routed by: `PROJECT_INDEX.yaml` bootstrap/domain routes
- Provenance: `DEC-*` → `Q-*` / `VQ-*`

This is the readable normalized product model between verbatim interview provenance and exact system/contracts. Exact behavior stays authoritative in routed system/design/content/contracts.

## Product model in one page
[Concrete explanation of what is being built, how the major parts relate, and why the architecture is shaped this way.]

## DEC-001 — [Decision title]
- decision: [...]
- rationale: [...]
- authority_class: [USER|COMPILER|RESEARCHED_FACT|DELEGATED_TECHNICAL|DEFERRED]
- source_ids: [Q-..., VQ-..., REF-...]
- affected_systems: [SYS-...]
- rejected_alternatives: []
- example_ids: []
- canonical_destinations: [DOC-..., CONTRACT-...]

## Cross-system / capability mental model
[Readable master-system + reusable-capability hierarchy, composition relationships and why consumer behavior is implemented core-first. Do not duplicate exact contract fields.]

## Important guardrails / non-goals
- GR-... — [short statement + pointer]

## Example semantics
- EX-... — [required|illustrative|adversarial|reference-derived] — [what the example proves]

## Open / deferred
- [...]
```

Update after substantial interview rounds. Do not compress away the source Q/A and do not become a second exact system authority.

---

## `contracts/ARCHITECTURE_GUARDRAILS.yaml` Template

Generate when explicit negative requirements prevent plausible but wrong implementations.

```yaml
schema_version: 1

guardrails:
  GR-001:
    statement: "[what must not exist/become]"
    reason: "[why this would violate intent/architecture]"
    source_ids: [DEC-001]
    applies_to: [SYS-EXAMPLE]
    forbidden_patterns:
      - "[semantic pattern, not brittle filename regex]"
    verification:
      - "[architecture/integration audit check]"
```

Guardrails are product/compiler architecture constraints, not generic style rules. When reusable compositions are a core project principle, include semantic guardrails against consumer-local copies of shared systems and against copied resolved values that should remain relative to a canonical base.

---

## `verification/ABSTRACTION_TESTS.yaml` Template

Generate when modularity/data-driven/extensibility claims need representative or adversarial proof. Use the **smallest representative proof set that covers materially different composition paths**; architecture proof scales with semantic diversity, not consumer count.

```yaml
schema_version: 1

tests:
  ABS-001:
    title: "[reusable architecture challenge]"
    systems: [SYS-EXAMPLE]
    proof_claim: reuse_and_composition
    representative_proof_set:
      integration_case: CASE-BASELINE
      variation_axes_required:
        - "[material composition/modifier/provider/mapping axis]"
      stopping_rule: "all material variation axes covered; additional similar consumers are product/content breadth"
    cases:
      - id: CASE-BASELINE
        proof_role: canonical_walking_skeleton
        semantic_role: illustrative
        evidence_mode: real_or_required_case
        covers:
          - canonical_runtime_path
        description: "[...]"
      - id: CASE-A
        proof_role: representative_consumer
        semantic_role: illustrative
        evidence_mode: real_or_required_case
        covers:
          - "[variation axis A]"
        description: "[...]"
      - id: CASE-B
        proof_role: representative_consumer
        semantic_role: adversarial
        evidence_mode: "[real_required_case|adversarial_fixture|fresh_agent_challenge]"
        covers:
          - "[variation axis B]"
        description: "[...]"
    pass_conditions:
      - "baseline proves the canonical owner/contract/runtime integration path"
      - "representative cases use the same canonical master systems/capabilities"
      - "material differences are expressed through declared composition/data/modifier/provider seams unless a genuine new reusable capability is identified"
      - "no consumer-local duplicate rule owner, bypass or parallel runtime path is required"
      - "all required semantic variation axes are covered without speculative production-content count"
    architecture_proof_status: pending
```

These cases test expressiveness/reuse; they are not automatically shipping content. Once the representative proof set passes, additional similar consumers are product/content/scale work unless a new semantic variation axis appears.

---

## `verification/FRESH_AGENT_RECONSTRUCTION.yaml` Template

Generate for nontrivial compiled packages before implementation task decomposition/final delivery.

```yaml
schema_version: 1
criterion: AC-PACKAGE-RECONSTRUCTION
required: true
mode: "[independent_agent|self_isolated_reconstruction]"
status: pending

required_concepts:
  start_prompt_orientation: pending
  product_vision: pending
  major_workflows: pending
  system_model_and_rationale: pending
  ownership_and_integration: pending
  rejected_alternatives_and_guardrails: pending
  example_semantics: pending
  reference_traits: pending
  representative_flow_trace: pending
  representative_proof_set_reasoning: pending
  authoring_extension_model: pending
  open_decisions: pending
  authority_routing: pending
  deep_authority_discovery: pending
  authority_reachability_report: pending

material_misconceptions: []
missing_context: []
evidence: []
```

Pass only when a fresh agent with no original chat first forms the correct product/master-outcome model from the generated Start Prompt and then resolves exact rules from package authorities without material misconceptions. Prefer an independent agent/subagent when available; record fallback evidence honestly.

Add a required Acceptance Matrix entry, for example:

```yaml
AC-PACKAGE-RECONSTRUCTION:
  title: Fresh agent reconstructs the intended product model
  required: true
  status: unverified
  authority_ids:
    - DOC-USER-VISION
    - DOC-DECISION-COMPENDIUM
    - DOC-CONTEXT-HANDOFF
    - CONTRACT-SYSTEM-MAP
  evidence_required:
    - type: authority_reachability
    - type: fresh_agent_reconstruction
  evidence: []
```

---

## `contracts/SYSTEM_MAP.yaml` Template

```yaml
schema_version: 1

systems:
  SYS-EXAMPLE:
    responsibility_key: SYSTEM.EXAMPLE
    responsibility_scope:
      - "[durable responsibility]"
    must_not_own:
      - "[neighbor responsibility]"
    authority_ids: [DOC-SYSTEM-EXAMPLE]
    provides: [CONTRACT-EXAMPLE-OUTPUT]
    depends_on: []
    consumed_by: []
    configuration_inputs: []
    extension_points: []
    acceptance_ids: [AC-EXAMPLE]

composition_policy:
  values:
    default_resolution_order:
      - master_default
      - content_or_module_definition
      - reusable_profile
      - consumer_modifier
      - runtime_modifier
    merge_operator_must_be_explicit_when_material: true
    prefer_relative_modifier_when_base_should_propagate: true
    absolute_replace_requires_intent: true

compositions:
  COMPOSITION-EXAMPLE:
    consumer_shell: "[generic entity/page/bot/workflow host]"
    uses: [SYS-EXAMPLE]
    data_ids: []
    profile_ids: []
    modifiers:
      example_numeric_field:
        op: add
        value: 0
    explicit_replacements: []
    forbidden_local_ownership: []
```

`SYSTEM_MAP.yaml` owns topology/responsibility scope. Put material per-rule decision owners, mutable-state owners, allowed writers, and cross-system runtime edges in `SYSTEM_INTEGRATION.yaml` rather than duplicating them here.

---

## `verification/INTEGRATION_AUDIT.yaml` Template

Generate when `SYSTEM_INTEGRATION.yaml` is material to the current project/work.

```yaml
schema_version: 1
revision: "git:<revision-or-worktree-id>"
scope:
  changed_systems: [SYS-EXAMPLE]
  changed_requirement_ids: [REQ-EXAMPLE]

checks:
  single_decision_owner: pass
  single_state_owner: pass
  core_first_change_classification: pass
  requested_behavior_maps_to_canonical_capability: pass
  producer_contract_consumer_paths: pass
  no_parallel_or_bypass_paths: pass
  live_configuration_consumers: pass
  composition_value_resolution: pass
  base_change_propagation_for_relative_modifiers: pass
  explicit_cross_system_writes: pass
  composition_coherence_invariants: pass
  runtime_data_driven_claims: pass
  cross_domain_god_objects: pass
  dead_contracts: pass
  architecture_guardrails: pass

feature_maturity:
  FEATURE-EXAMPLE:
    specified: true
    declared: true
    connected: true
    exercised_evidence: [EV-EXAMPLE]
    verified_by: [AC-EXAMPLE]

findings: []
result: pass
```

This is revision-bound audit evidence, not a second ownership authority. Findings must point back to `SYSTEM_INTEGRATION`, implementation IDs, or Acceptance IDs.

---

## `contracts/VISUAL_DESIGN_CONTRACT.yaml` Template

Generate for design-heavy products when whole-screen/page composition must remain stable across local implementation work.

```yaml
schema_version: 1

surfaces:
  SURFACE-EXAMPLE:
    authority_ids: [DOC-DESIGN]
    vision_anchor_ids: [VQ-001]
    approved_reference_ids: []
    focal_priority: []
    persistent_regions: []
    layout_relationships: []
    invariants: []
    allowed_deviations: []
    acceptance_ids: [AC-UI-EXAMPLE]
```

Use visual checkpoint/runtime evidence to verify it; do not infer fidelity from component existence.

---

## `docs/PROJECT_PLAN.md` Template

```markdown
# Project Plan

## Authority Metadata
- Artifact ID: `DOC-PROJECT-PLAN`
- Routed by: `PROJECT_INDEX.yaml` bootstrap/planning routes
- System/Acceptance refs: [SYS-... / AC-...]

Status: `[draft_before_reconstruction|final_after_reconstruction]`

## Planning Basis
- User vision: DOC-USER-VISION
- Decision model: DOC-DECISION-COMPENDIUM
- Context handoff: DOC-CONTEXT-HANDOFF
- System topology: CONTRACT-SYSTEM-MAP
- Reconstruction gate: VERIFY-FRESH-AGENT-RECONSTRUCTION
- Acceptance: DOC/CONTRACT-ACCEPTANCE

## Delivery Strategy
[How the complete product will be assembled without losing the walking skeleton.]

## Phase 0 — Walking Skeleton
- systems/flows involved: [...]
- observable outcome: [...]
- placeholders allowed: [...]
- skeleton_classification: [exploratory|production_candidate|production_admitted]
- required_survivability_acceptance_ids: [AC-...]
- gate: [...]

## Phase / Milestone — [Name]
- System IDs: [...]
- Blueprint IDs: [...]
- depends_on: [...]
- implementation objective: [...]
- integration objective: [...]
- skills/capabilities: [...]
- acceptance/evidence: [...]

## Integration Order
[Dependency-aware order and why.]

## Independent Work Units
[Systems/components that can be implemented and tested independently.]

## Deferred / Future
[Future work preserved without pretending it is current scope.]
```

---

## `docs/INTERVIEW_LEDGER.md` Template

```markdown
# Interview Ledger

## Authority Metadata
- Artifact ID: `DOC-INTERVIEW-LEDGER`
- Routed by: `PROJECT_INDEX.yaml` interview-provenance route
- Purpose: verbatim material Q/A provenance

This is the durable provenance record for material compiler questions and user answers. Exact behavior remains authoritative in routed project contracts/specs.

## Q-001 — [Topic]

Question:
> [exact question as asked]

User answer:
> [verbatim answer in original language]

Compiled meaning:
- [...]

Classification:
- confirmed_user_decision

Example semantics (when applicable):
- null # required | illustrative | adversarial | reference-derived

Affected systems/domains:
- SYS-...

Canonical destinations:
- DOC-...#...
- CONTRACT-...

Status:
- active

Supersedes / clarified by:
- null
```

Do not omit material Q/A merely because its conclusion also exists in a system spec.

---

## `contracts/INTERVIEW_COVERAGE.yaml` Template

```yaml
schema_version: 1
project: PROJECT-ID

product_capability_envelope:
  inference_basis:
    product_archetype: "[compiler hypothesis, not USER authority]"
    sources: [VQ-..., REF-...]
  expected_responsibilities:
    - key: RESPONSIBILITY-EXAMPLE
      rationale: "ordinary responsibility implied by the requested product"
      provenance: compiler_inference
      disposition: modeled # modeled|covered_by_existing_owner|not_applicable|intentionally_deferred|delegated_technical|needs_user_decision
      owner_or_destination: SYS-EXAMPLE
      notes: []
  unconsidered_material: 0

status_values:
  - confirmed
  - research_resolved
  - delegated_technical
  - intentionally_deferred
  - not_applicable
  - unresolved_user
  - contradiction

systems:
  SYS-EXAMPLE:
    fields:
      purpose: confirmed
      user_visible_behavior: confirmed
      states_rules: confirmed
      inputs_triggers: delegated_technical
      outputs_feedback: confirmed
      content_configuration: confirmed
      dependencies: confirmed
      variants_overrides: not_applicable
      value_resolution_propagation: not_applicable
      failure_recovery: not_applicable
      design_ux: confirmed
      future_constraints: confirmed
      acceptance: confirmed
    question_ids: []
    notes: []

completion_gate:
  unresolved_user: 0
  contradictions: 0
  unconsidered_material_responsibilities: 0
  status: passed
```

Add/remove fields per domain. The gate concerns user-owned material decisions, not implementation trivia.

---

## `CONTEXT_HANDOFF.md` Template

```markdown
# Project Context Handoff

## Authority Metadata
- Artifact ID: `DOC-CONTEXT-HANDOFF`
- Routed by: `PROJECT_INDEX.yaml` bootstrap
- Purpose: rich fresh-agent/context-loss onboarding; exact rules remain in canonical authorities

## What the user is trying to create
[Rich product description, not a one-line summary.]

## Intended experience / gestalt
[What it should feel like and what must remain recognizable.]

## Important original wording
- VQ-... — "..."

## References and why they matter
### [Reference]
- cited for: [...]
- adopted traits: [...]
- explicitly not implied: [...]

## How the concept evolved
[Chronological/thematic narrative of important discussions and clarifications.]

## Major decisions and rationale
### [Decision]
- decision: [...]
- why: [...]
- source: Q-... / VQ-...
- canonical authority: [...]

## Rejected / changed alternatives
- [...]

## Product archetype / expected capability envelope
[Compiler-inferred coverage hypothesis plus dispositions: modeled / covered elsewhere / not applicable / deferred / delegated / user decision. This is not USER authority.]

## Master systems, capability hierarchy and composition model
[Readable overview + pointers to SYSTEM_MAP/CAPABILITY_GRAPH. Include the core-first law and examples that prevent later consumer-local bypasses.]

## How later user requests must extend the architecture
[Explain that follow-up requests are deltas: classify data/modifier vs composition vs existing/new reusable capability before source edits. Record known extension examples.]

## Future constraints that matter now
- [...]

## Open / deferred decisions
- [...]

## Prior drift/failure lessons
[Only project-relevant lessons that a new agent must not repeat.]

## Canonical source map
- discoverability/JIT router: `PROJECT_INDEX.yaml`
- artifact path/identity resolution: `PROJECT_REGISTRY.yaml`
- authority reachability evidence: `verification/AUTHORITY_REACHABILITY.yaml`
- exact vision: `docs/USER_VISION.md`
- interview provenance: `docs/INTERVIEW_LEDGER.md`
- readable decision model: `docs/DECISION_COMPENDIUM.md`
- completeness state: `contracts/INTERVIEW_COVERAGE.yaml`
- package reconstruction: `verification/FRESH_AGENT_RECONSTRUCTION.yaml`
- systems: `contracts/SYSTEM_MAP.yaml`
- reusable capability hierarchy: `contracts/CAPABILITY_GRAPH.yaml` when present
- negative architecture constraints: `contracts/ARCHITECTURE_GUARDRAILS.yaml` when present
- abstraction/reconstruction evidence: `verification/ABSTRACTION_TESTS.yaml`, `verification/FRESH_AGENT_RECONSTRUCTION.yaml`
- [...]
```

Keep this detailed enough to onboard an agent after context loss. Do not replace precise contracts with the handoff.

# Template — project-native executable gate

For nontrivial projects with structured project truth, emit an **actual executable** `tools/project_gate.<ext>` in an available runtime. The filename/runtime may differ; keep one canonical gate entry point.

Do not ship the following as uninstantiated pseudocode. The compiler must specialize it to the concrete generated contracts and dependency environment.

## Required command semantics

```text
project_gate validate
  parse + shape + ID/reference + reachability + freshness checks

project_gate preflight
  validate
  print current admitted stage/outcome
  print exact required authority/reference IDs
  print Core-First reminder / optional Governance binding reminder
  fail if current stage prerequisites encoded by existing Plan/Acceptance/State are not satisfied
  reject production-skeleton admission when required survivability Acceptance evidence is absent

project_gate self-test
  run validator against temporary known-bad mutants
  require every declared negative control to be rejected

project_gate handoff
  validate + require applicable State/Handoff/Atlas/verification reconciliation/freshness

project_gate completion
  handoff checks
  + reread/reconcile canonical current State + Plan + Acceptance
  + require all completion-critical evidence IDs/artifacts current
  + run/require declared final build/runtime/browser gates
  + reject claims based only on file existence, M0/foundation/project-gate success, or code volume
```

## Generated validator requirements

Use a real parser for each structured format. If a required parser dependency is unavailable, report a hard validation capability failure; do not fall back to regex and claim PASS.

Generate project-specific validation tables/functions for the concrete package, such as:

```python
STRUCTURED_AUTHORITIES = [
    "PROJECT_INDEX.yaml",
    "PROJECT_REGISTRY.yaml",
    "ACCEPTANCE_MATRIX.yaml",
    "contracts/SYSTEM_MAP.yaml",
    "contracts/CAPABILITY_GRAPH.yaml",
    "contracts/SYSTEM_INTEGRATION.yaml",
    "blueprints/REGISTRY.yaml",
]

# Generated from this project's real shapes; examples only.
REQUIRED_MAPPING_KEYS = {
    "PROJECT_REGISTRY.yaml": ["artifacts"],
    "contracts/SYSTEM_MAP.yaml": ["systems"],
    "contracts/CAPABILITY_GRAPH.yaml": ["capabilities"],
}
```

Then validate referential integrity across the actual package IDs and paths. A regex search for `path:` + filesystem existence is explicitly insufficient.

## Negative-control self-test

The generated gate should exercise its validation functions against temporary/copy-on-write mutations instead of corrupting the working repository. Include only cases relevant to the generated package, but normally at least:

```text
MUTANT-INVALID-STRUCTURE
  break YAML/JSON syntax or a required mapping shape
  expected: FAIL

MUTANT-BROKEN-REFERENCE
  replace one known System/Capability/Blueprint/Acceptance reference with UNKNOWN-ID
  expected: FAIL

MUTANT-ORPHAN-AUTHORITY
  create/register a normative authority that PROJECT_INDEX cannot reach
  expected: FAIL

MUTANT-REGISTRY-MISMATCH
  make Blueprint/registry identity disagree with its file metadata
  expected: FAIL

MUTANT-STALE-VIEW-OR-STATE   # when freshness is encoded
  alter a fingerprinted source without refreshing derived evidence
  expected: FAIL

MUTANT-UNMET-ADMISSION       # when staged admission is material
  mark/select a downstream stage while prerequisite evidence is absent
  expected: FAIL

MUTANT-GATED-TRANSITION-WITHOUT-APPROVAL  # when approval gate is material
  mark/cross the exact gated transition without required approval evidence
  expected: FAIL

CONTROL-ALLOWED-PREPARATION-BEFORE-APPROVAL
  exercise explicitly authorized reversible preparation while approval is absent
  expected: PASS

MUTANT-FOUNDATION-PASS-AS-PRODUCT-COMPLETE
  leave one or more required product Acceptance outcomes/evidence absent while package/M0/foundation gate passes
  expected: FAIL

MUTANT-FILE-EXISTS-AS-RUNTIME-EVIDENCE
  satisfy a required runtime/browser criterion only by creating/naming the expected implementation artifact without exercising the boundary
  expected: FAIL

MUTANT-STALE-FINAL-EVIDENCE
  change relevant source/config/data after final evidence without rerunning affected verification
  expected: FAIL
```

Store the PASS/FAIL summary in the project's existing contract/package-validation evidence.


MUTANT-FALSE-ADMISSION
  set STATE.current_admission to a stage whose required predecessor maturity/Acceptance is not currently verified
  expected: FAIL

MUTANT-E2E-STATE-DRIFT
  mark a stage/PR outcome Verified while one of its required E2E scenarios remains pending/not exercised
  expected: FAIL

MUTANT-PARTIAL-PERSISTENCE-AS-CONTINUE
  provide a narrow serialize/deserialize field roundtrip while full Continue/Resume Acceptance requires state coverage/equivalence
  expected: FAIL

MUTANT-COMPOSITION-DRIFT
  change a canonical source/relation while leaving a required dependent projection stale/inconsistent
  expected: FAIL

MUTANT-LOCAL-SYMPTOM-PATCH
  patch one dependent consumer so a local symptom disappears while the declared shared invariant remains violated
  expected: FAIL

MUTANT-PREMATURE-SKELETON-ADMISSION
  claim production-admitted skeleton while required survivability substitution/extension evidence is absent or failing
  expected: FAIL

MUTANT-INSTANCE-LOCAL-RUNTIME
  add a second same-archetype definition but route it through a copied/per-instance runtime or surface instead of the registered generic consumer
  expected: FAIL

MUTANT-MODIFIER-COPIES-OWNER
  implement a modifier by copying or directly owning the target capability/state instead of using its declared modifier seam
  expected: FAIL

MUTANT-PLACEHOLDER-REQUIRES-ARCHITECTURE-REPLACEMENT
  replace a declared placeholder with production content only by bypassing/replacing the canonical owner/consumer path
  expected: FAIL

MUTANT-TEST-CONTENT-LEAKAGE
  route test_fixture/debug_only content into a normal shipping/default/progression/user flow
  expected: FAIL

MUTANT-CONSUMER-FOREIGN-WRITE
  allow a consumer/adapter to directly mutate state owned by another Responsibility Owner outside its declared command contract
  expected: FAIL

MUTANT-BLUEPRINT-INTERNAL-BYPASS
  route a cross-system consumer directly to a known internal implementation artifact while a canonical public Blueprint/module boundary exists
  expected: FAIL

MUTANT-TEST-VOLUME-AS-PRODUCT-COMPLETE
  leave a required PR outcome unverified while many unit/integration tests pass
  expected: FAIL

## `STATE.json` admission/context extension

When stage admission is material, prefer a machine-checkable current slice of the canonical plan rather than asking the gate to infer prose:

```json
{
  "current_admission": {
    "stage_id": "STAGE-...",
    "plan_source_id": "DOC-PROJECT-PLAN",
    "plan_fingerprint": "...",
    "prerequisites": [
      {
        "id": "AC-OR-CAP-...",
        "required_maturity": "Exercised",
        "required_evidence_ids": ["EVID-..."]
      }
    ],
    "allowed_exploration": ["..."],
    "forbidden_conclusions": ["..."],
    "exit_evidence_ids": ["..."],
    "status": "admitted|blocked|complete"
  },
  "transition_gate": {
    "gate_id": "GATE-...",
    "gated_transition": "...",
    "reversible_preparation_allowed": true,
    "approval_authority_source_id": "...",
    "approval_evidence_ids": [],
    "transition_status": "waiting|approved|crossed"
  },
  "context": {
    "required_source_ids": [],
    "loaded_source_ids": [],
    "required_reference_ids": [],
    "inspected_reference_ids": [],
    "inspected_view_ids": []
  }
}
```

`STATE.current_admission` and optional `transition_gate` are runtime slices derived from existing Plan/Workflow/Acceptance authorities, not a second planner or approval engine. `project_gate preflight/completion` must independently re-derive admissibility from Plan + Product Realization + Acceptance + current evidence and fail when STATE claims a stage/status that the derivation does not permit. Omit `transition_gate` when the project has no material human/project gate.

## Root `AGENTS.md` / START kernel addition

```text
Before material work and after fresh/compacted context:
1. load/apply bound Core-First Governance if actually available;
2. otherwise use the declared project-native fallback;
3. run the project gate preflight;
4. read/inspect every required authority/reference it reports;
5. implement only within the current admitted stage and canonical owner path.
Never claim a plugin/tool ran unless it actually did.
```

## Reference-routing extension

For material visual work, `PROJECT_INDEX` routes actual reference assets with stable IDs, and `STATE.context.required_reference_ids` / `inspected_reference_ids` track task-local consumption. A file in `references/` that lacks routing/inspection does not satisfy design-source consumption.


## FINAL_REPORT.md / final response template

The final report is a generated/derived view. It does not own status.

```markdown
# Final Verification Report

## Canonical current state
- State source/revision: [...]
- Current admission/final status: [...]

## Requested outcomes and evidence
| Outcome / AC | Required evidence | Actual current evidence | Verdict |
|---|---|---|---|
| ... | ... | ... | VERIFIED / UNVERIFIED / BLOCKED |

## Final gates actually executed
- build/typecheck: [command + result]
- integration: [...]
- runtime/browser/user-surface: [...]
- visual/black-box: [...]
- project_gate completion: [...]

## Reconciliation
- contradictory/stale evidence: [...]
- remaining unmet/deferred outcomes: [...]

## Verdict
`COMPLETE` only if every required row and gate above supports it.
```

Do not populate this report from filenames, code-count summaries, old milestone prose or project-gate/package validation beyond the claim scope those checks actually exercised.


## `contracts/PERSISTENCE_COVERAGE.yaml` Template (conditional)

Generate when save/resume/continue/restart recovery is material.

```yaml
runtime_state_coverage:
  STATE-EXAMPLE:
    owner: SYS-...
    disposition: persisted    # persisted|deterministically_reconstructed|intentionally_transient|forbidden_to_persist
    schema_or_reconstruction_contract: CONTRACT-...
    acceptance_ids: [AC-...]

continue_equivalence:
  required: true
  checkpoint_definition: "..."
  comparison_horizon: "N deterministic steps/ticks/actions"
  tolerances: {}
```

Preferred strong Continue/Resume evidence when deterministic behavior is expected:

```text
State A
→ persist → restore → N deterministic steps

vs

same State A
→ no reload → N deterministic steps

compare declared observable/state outputs within project tolerances
```

A selected-field serialize/deserialize roundtrip proves only those fields unless Acceptance explicitly scopes the claim that narrowly.
