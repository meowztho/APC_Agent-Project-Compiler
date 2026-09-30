# Execution Runtime Guide

# Current Precedence — Provider-Safe Runtime, Derived Admission, Product Continuity and Verification Truth

Fresh/session recovery order: Portable Operating Kernel → root instructions if available → `PROJECT_INDEX` bootstrap/lifecycle route → refresh/inspect Atlas when required → derive exact `required_source_ids` → actually read normative authorities → record current-session `loaded_source_ids` → context/read gate → classify current change → implementation.

`loaded_source_ids` is ephemeral; reset/re-resolve after fresh session, major context loss/compaction, relevant authority revision or domain/requirement switch. START/Atlas summaries never satisfy normative reads.

Before selecting the next material requirement/work item, evaluate dependency/admission conditions routed from `PROJECT_PLAN`, Acceptance and relevant System/Capability/Integration authorities:
`unmet/reopened outcomes → resolve prerequisites → evaluate required maturity/evidence → ADMISSIBLE WORK SET → priority/risk/value selection`.

Do not choose a task merely because it is runnable, easy to measure, already has a harness or appears next/interesting. If downstream work is not admitted, only explicitly allowed exploratory synthetic/unit/integration/spike work may run; label its evidence non-authorizing for product conclusions. After prerequisite evidence changes, recompute admission.

After local fixes reconcile the original requested outcome and current evidence before moving on; nearby symptoms or test volume do not redefine the goal.


## Exact transition-gate execution
When current project authorities define an approval/admission gate around a specific transition, do not treat `awaiting approval` as a global stop unless the authorities explicitly say so. Continue authorized reversible preparation and other admissible work up to the boundary. Immediately before the gated state change/side effect, resolve the exact gate authority and require current scoped approval evidence. A broad implementation request, completed preparation, passing tests or technical admission does not substitute for that approval.

If approval is absent, preserve the transition as not crossed, record the real state, and continue other admissible work when available. Ask the user only when that approval is genuinely the next blocking user-owned decision/transition. After explicit approval, record it at the scope required by the project and cross only the transition it authorizes; do not silently reuse approval for a different revision/transition unless the authority permits it.

---


## Purpose

The project package must tell the coding agent not only WHAT the project is,
but WHEN to inspect, blueprint, implement, verify, clean up, review, commit,
and perform real-user testing.

Use a phase machine instead of an undifferentiated "work until done" loop.

---

# 1. Runtime Phases

Recommended phase order:

```text
BOOTSTRAP_REPOSITORY
→ DISCOVER_CAPABILITIES
→ BIND_AGENT_RUNTIME
→ LOAD_BOOTSTRAP_CONTEXT
→ VERIFY_AUTHORITY_REACHABILITY     # package discoverability gate
→ VERIFY_ATLAS_FRESHNESS             # nontrivial generated-view validity
→ INSPECT_ATLAS_ORIENTATION          # whole-project orientation, not authority
→ VALIDATE_PROJECT_RECONSTRUCTION   # fresh compiled project/agent when required
→ SELECT_REQUIREMENT
→ RESOLVE_REQUIRED_AUTHORITIES
→ LOAD_JIT_CONTEXT
→ VERIFY_CONTEXT_LOAD_GATE
→ CLASSIFY_CHANGE_ARCHITECTURE
→ RESOLVE_SKILLS_FOR_REQUIREMENT
→ BLUEPRINT_OR_REUSE
→ IMPLEMENT_UNIT
→ VERIFY_UNIT
→ INTEGRATE
→ VERIFY_INTEGRATION
→ AUDIT_SYSTEM_INTEGRATION          # when cross-system behavior changed
→ VERIFY_USER_SURFACE               # when observable
→ HYGIENE
→ RECORD_MILESTONE
→ repeat SELECT_REQUIREMENT
→ FINAL_CONTRACT_AUDIT
→ FINAL_BUILD_TEST
→ FINAL_USER_SURFACE_GATE           # when applicable
→ INDEPENDENT_REVIEW                # when triggered
→ FINAL_GIT_CHECK
→ COMPLETE
```

A failure returns to the earliest phase capable of fixing the root cause.

---

# 2. BOOTSTRAP_REPOSITORY

For coding projects:

1. identify the intended project/repository root;
2. inspect applicable instructions;
3. determine whether Git exists;
4. if no Git repository exists:
   - initialize Git unless explicit project/user policy forbids it;
   - create/update an appropriate `.gitignore` before staging;
   - never stage obvious secrets, credentials, build caches, generated binaries,
     temporary evidence, or tool-specific junk unless intentionally versioned;
5. inspect branch/HEAD when available;
6. inspect `git status`;
7. inspect relevant existing diffs;
8. preserve unrelated changes.

`git init` is repository setup, not permission to rewrite user files.

For a new agent-owned project, create a recoverable baseline/verified milestone commit
when project policy permits it.

For an existing/shared project, follow `contracts/VERSION_CONTROL.yaml`.

---

# 3. DISCOVER_CAPABILITIES

Before planning verification, determine what the current harness can actually do. User-surface tools are recorded here; agent-loop/customization primitives are bound separately in `AGENT_RUNTIME_PROFILE.yaml`.

Generate/update:

```text
verification/TOOL_CAPABILITIES.yaml
```

Example:

```yaml
capabilities:
  interactive_desktop:
    available: true
    adapter: computer_use
    verified_by: tool_exposed

  browser_interaction:
    available: false

  screenshot_capture:
    available: true
    adapter: computer_use

  engine_runtime:
    available: true
    adapter: unreal_editor

  shell:
    available: true

selected:
  user_surface_adapter: computer_use
  screenshot_adapter: computer_use
```

Do not assume a model/provider capability implies the current harness exposes it.

If a suitable tool is exposed, a user-facing final gate MUST actually invoke it.
"Available but unused" is a verification failure.

If unavailable, choose the strongest real alternative:
- headed browser automation;
- editor/runtime automation;
- OS screenshot utility;
- engine screenshot/frame capture;
- rendered artifact capture;
- real CLI/client.

If required user-surface evidence cannot be produced by any available method,
the affected criterion stays unverified/blocked. Do not claim completion.

---

# 4. BIND_AGENT_RUNTIME

For a nontrivial autonomous project, discover the actual agent/client/harness customization primitives and generate/update:

```text
contracts/AGENT_RUNTIME_PROFILE.yaml
```

Record actual support and selected bindings for persistent instructions, Agent Skills, lifecycle hooks, subagents/fresh contexts, MCP/external tools, provider memory, workflows/commands, and worktrees/sandboxes.

Rules:
- project authorities remain provider-neutral;
- use one canonical instruction kernel plus thin provider adapters when needed;
- bind deterministic completion/integration/policy validators to blocking lifecycle hooks when available;
- otherwise preserve the same validators as explicit phase gates;
- use isolated subagents/fresh sessions for reconstruction/review/noisy exploration when available;
- never require provider memory or session history to reconstruct the project.

Use `AGENT_RUNTIME_PORTABILITY_GUIDE.md`. Refresh the profile when the harness/provider/session capabilities materially change.

---

# 5. LOAD_BOOTSTRAP_CONTEXT

On a fresh implementation turn, consume the generated context-rich `START_PROMPT` orientation first. It should state the product/master outcome, material decision context, systems/compositions/guardrails and execution intent directly.

Then read `PROJECT_INDEX.yaml` and every direct `bootstrap.must_read` authority declared there before the first material source edit. Also load the compact routing/state layer:

- root/applicable `AGENTS.md`;
- `PROJECT_REGISTRY.yaml`;
- `ACCEPTANCE_MATRIX.yaml`;
- `STATE.json`;
- Blueprint registry;
- execution/verification policies.

`PROJECT_INDEX.yaml` is the canonical discoverability router. Do not replace it with prose chains such as "read A, then A tells you to read B". Do not preload every JIT authority after bootstrap; initial understanding is context-rich, exact repeated execution is routed JIT.

---

# 6. VERIFY_AUTHORITY_REACHABILITY

Run the generated project contract/reachability validator before trusting the package structure on a fresh compiled project, after structural documentation/registry changes, and before final completion.

The validator must compute reachability from:
- `PROJECT_INDEX.bootstrap.must_read`;
- every `PROJECT_INDEX.domains.*.authority_ids` route;
- `PROJECT_REGISTRY.yaml` artifact identity/`normative` metadata;
- routed Blueprint IDs plus registered Blueprint `call` edges.

It must reject:
- unresolved route IDs;
- active normative/discoverability-required artifacts that have no incoming bootstrap/JIT route;
- active normative Blueprints that are neither routed nor reachable from a routed Blueprint;
- deprecated/superseded artifacts still used as active routes.

Write generated evidence to `verification/AUTHORITY_REACHABILITY.yaml`. That report is diagnostic evidence, not a second routing authority.

If reachability fails, fix the canonical router/registries first. Do not compensate by manually reading the orphan file and continuing.

---

# 7. VERIFY_ATLAS_FRESHNESS

For every nontrivial compiled project, resolve `VIEW-PROJECT-ATLAS` and its registered generator/source metadata. Recompute whether the generated view matches the current canonical Atlas inputs.

If stale or missing:
- regenerate it from canonical sources;
- update its generated source fingerprint/revision metadata;
- do not manually edit project truth into the HTML;
- fail/block bootstrap if a required Atlas cannot be regenerated and no honest stale status is recorded.

The Atlas remains `normative: false`. Freshness is a generated-view validity property, not authority precedence.

---

# 8. INSPECT_ATLAS_ORIENTATION

On a fresh implementation session, major context recovery, or Fresh-Agent Reconstruction, actually inspect the fresh Atlas once before task-local JIT work. Record `VIEW-PROJECT-ATLAS` in `STATE.context.inspected_view_ids` when the harness can track/attest it.

Use it to restore the whole-product picture: vision capsule, decisions/guardrails, systems/capabilities/compositions, user flow, current acceptance state, blockers and canonical IDs. Then use `PROJECT_INDEX.yaml` for exact authorities.

The Atlas cannot satisfy `required_source_ids`; orientation-view inspection and normative-source loading are separate gates.

---

# 9. VALIDATE_PROJECT_RECONSTRUCTION

For a fresh nontrivial compiled project, inspect `verification/FRESH_AGENT_RECONSTRUCTION.yaml` before implementation work. Read `CONTEXT_HANDOFF.md` + `docs/DECISION_COMPENDIUM.md` once for the holistic product model.

If the reconstruction criterion is already passed with valid package-level evidence, do not rerun it on every resume. If it is missing/pending/stale after material specification changes, run the reconstruction procedure defined in `FRESH_AGENT_RECONSTRUCTION_GUIDE.md` before task implementation. Prefer an independent fresh agent/subagent when the harness exposes one; otherwise record the weaker self-isolated fallback honestly.

A material misconception is a specification/package defect or bootstrap-context defect. Fix/clarify canonical authorities and regenerate the Start/Goal orientation snapshot; ask the user only for genuinely unresolved product intent. Do not compensate with undocumented private explanation.

---

# 10. SELECT_REQUIREMENT

Choose the highest-priority required criterion that is:

- unverified;
- reopened;
- stale;
- blocked by work the agent can now resolve.

Prefer requirements that restore the walking skeleton / normal user flow.

Do not optimize for easiest-to-complete criteria if a broken core route blocks the
actual product.

---

# 11. RESOLVE_REQUIRED_AUTHORITIES

For the active criterion/change:

1. classify the relevant `PROJECT_INDEX.yaml` domain route(s);
2. expand declared route dependencies only as needed;
3. collect authority IDs and any routed Blueprint IDs;
4. resolve current paths through `PROJECT_REGISTRY.yaml` / Blueprint registry;
5. write the exact set to `STATE.json.context.required_source_ids`;
6. if a required normative authority is missing/unrouted, stop implementation and repair package routing.

Do not infer the source set from filenames, old chat, or memory when the router exists.

---

# 12. LOAD_JIT_CONTEXT

For the active criterion:

1. read the criterion entry;
2. read every `STATE.context.required_source_ids` authority needed for the dependent change;
3. load only relevant behavior/data/implementation Blueprints reached by the route/call graph;
4. inspect current implementation and call sites;
5. load applicable local `AGENTS.md` for target paths;
6. inspect relevant tests/evidence;
7. record current-session loaded-source evidence when possible;
8. do not reread unrelated stable context.

---

# 13. VERIFY_CONTEXT_LOAD_GATE

Before the first material source edit, compare `STATE.context.required_source_ids` with the authorities actually loaded in the current context/session.

PASS requires every required source to be current enough for the change. If the harness exposes file-read/tool hooks, derive `loaded_source_ids` from observed reads. Otherwise record explicit runtime attestation after actual reads; do not mark sources loaded merely because they exist.

Reset/re-evaluate this gate after:
- a fresh session;
- major compaction/context loss;
- material authority changes;
- switching to a requirement/domain whose required-source set differs.

A missing required authority blocks source edits. Reading an implementation file is not a substitute for reading its project authority.

---

# 14. CLASSIFY_CHANGE_ARCHITECTURE

Before the first source edit for each material new user/requirement delta, apply `CAPABILITY_HIERARCHY_AND_CHANGE_GATE_GUIDE.md`.

1. identify the visible consumer/surface the request appears to target;
2. resolve the canonical master system and current capability path;
3. classify the change as data/asset, value modifier, compose existing capability, extend existing capability, new reusable capability, adapter/surface, core-rule change, or explicit justified one-off;
4. record the existing-path reuse check and, when reuse/new capability is plausible, the counterfactual second-consumer test;
5. update `STATE.json.current_change` (or the scoped ExecPlan for complex work);
6. update `CAPABILITY_GRAPH.yaml`/contracts before consumer implementation when a new reusable capability is required;
7. only then proceed to implementation routing.

A direct user request to "just add" behavior does not bypass this gate. For trivial value/content edits the gate may be a concise classification and immediate continuation.

If the active Acceptance/plan stage claims reusable architecture, resolve its **Representative Proof Set** before broad consumer/content scale: canonical walking-skeleton/reference case for integration plus the minimum heterogeneous cases covering material variation axes. Once that proof passes, do not keep creating similar consumers merely to accumulate architecture evidence; return to the next admissible product outcome. A new case reopens architecture proof only when it introduces a genuinely new semantic variation axis or exposes a bypass/duplicate owner.

If a blocking pre-tool/write hook is available, require a valid current-change classification before source edits; otherwise enforce this as a phase gate.

---

# 15. RESOLVE_SKILLS_FOR_REQUIREMENT

After the active requirement and its relevant systems are known:

1. read only matching entries from `contracts/SKILL_REQUIREMENTS.yaml`;
2. inspect actually available global/project/harness skills when state may have changed;
3. select the minimum matching skill set for the requirement;
4. load selected skill instructions/references JIT;
5. if a high-value capability gap remains, follow the external/project-local discovery rules in `SKILL_NATIVE_COMPILER_GUIDE.md`;
6. record new resolution/rejection/version information when material;
7. continue without optional skills when the work remains safely executable.

Do not load every installed skill. Do not treat a skill as authority over `SYSTEM_MAP`, design, behavior, content, or acceptance contracts.

---

# 16. BLUEPRINT_OR_REUSE

Before code changes:

1. derive responsibility key;
2. check artifact/Blueprint registries;
3. inspect existing code;
4. reuse/repair/extend/simplify/supersede when possible;
5. create a new implementation/data Blueprint only if a new bounded responsibility
   genuinely exists.

When behavior or implementation structure is material, update the Blueprint BEFORE
or WITH the code so the graph remains a usable implementation map.

Do not allow implementation to drift silently away from the active Blueprint.

---

# 17. IMPLEMENT_UNIT

Implement the smallest coherent unit that can be independently reasoned about and tested.

Typical units:
- class;
- module;
- service;
- component;
- screen controller;
- state machine;
- domain object;
- shared registry/store;
- meaningful data structure/schema;
- integration adapter.

Do not create separate Blueprints for trivial local variables, tiny helper functions,
or incidental arrays with no independent semantics.

---

# 18. VERIFY_UNIT

Verify the implementation unit before broad integration when practical.

Use the narrowest suitable evidence:
- unit test;
- schema/config validation;
- deterministic behavior test;
- compile/typecheck;
- debug probe;
- serialization round trip;
- invariant check.

Each implementation/data Blueprint should declare its own verification hooks.

A unit test proves only the unit contract, not the user flow.

---

# 19. INTEGRATE / VERIFY_INTEGRATION

Wire the unit into its canonical caller/router/registry and intended producer-contract-consumer path.

Then verify:
- calls/contracts resolve;
- state/rule ownership matches System Map/Integration contracts;
- no parallel owner/bypass exists;
- expected events/data reach the declared consumer;
- configuration/data is actually consumed where claimed;
- relevant integration tests pass;
- project-contract validator passes after structural changes.

An implementation that is never reached through the intended runtime/product path is not complete.

---

# 20. AUDIT_SYSTEM_INTEGRATION

Run after material cross-system changes and before a requirement that depends on them is marked green. Use `SYSTEM_INTEGRATION_AND_RUNTIME_TRACE_GUIDE.md`.

Check applicable items:
1. one authoritative decision owner per material rule;
2. one authoritative state owner per material mutable state;
3. producer -> contract/data -> consumer -> owner path closes;
4. cross-system writes use declared mutation paths;
5. no parallel/bypass implementation exists;
6. declared fields/settings/contracts have live consumers;
7. config actually controls the claimed behavior;
8. data-driven/configurable claims pass their extension boundary test;
9. no implementation unit accidentally owns unrelated system domains;
10. changed requirement/config runtime traces reach qualifying evidence.

Inspect runtime/call/data graphs rather than inferring modularity from filenames. Search for dead parameters/config, ignored results, duplicate writes, hard-coded overrides and unconsumed definitions where relevant.

When this audit is release-relevant or must survive context loss, record/update `verification/INTEGRATION_AUDIT.yaml` with the current revision, scope, findings, feature maturity and result. The audit record is evidence; ownership remains authoritative in `SYSTEM_INTEGRATION.yaml`.

Failure returns to the earliest owner/contract/implementation phase capable of fixing the root cause.

---

# 21. VERIFY_USER_SURFACE

If the change is visible or interactive and the relevant route is runnable:

1. invoke the selected real-user adapter;
2. perform the smallest relevant interaction;
3. capture/inspect the required screenshot/rendered checkpoint;
4. record evidence IDs;
5. fix observed required failures before leaving the requirement.

This phase is mandatory when the criterion requires user-surface evidence and a
capability is available.

Do not replace tool invocation with a statement that the code "should work".

---

# 22. HYGIENE

After a requirement/milestone is green, perform scoped hygiene.

Check only project-related consequences of the work:
- duplicate responsibility owners;
- obsolete/superseded menus/screens/services;
- dead navigation routes;
- stale Blueprint/registry entries;
- orphan generated files;
- temporary debug scenes/files accidentally left in project paths;
- stale path references;
- orphan/unrouted normative authorities or Blueprints introduced by structural changes;
- untracked build/tool junk that belongs in `.gitignore`;
- obsolete compatibility copies no longer required.

Do not perform unrelated cleanup.

Update registries and documentation transactionally.

Run contract validation after structural cleanup.

---

# 23. RECORD_MILESTONE

After updating canonical decisions/systems/flows/acceptance/state, evaluate whether registered Atlas inputs changed. If yes, mark `VIEW-PROJECT-ATLAS` stale and regenerate it before the milestone is handed off or used for a fresh/context-recovery orientation.


Update:
- acceptance evidence/status;
- `STATE.json`;
- registry paths/ownership;
- Blueprint implementation/test references;
- relevant revision/worktree evidence.

When version-control policy permits:
- create a verified milestone commit;
- keep commits coherent and recoverable;
- never hide failing/unverified work behind a "done" commit message.

---

# 24. FINAL_CONTRACT_AUDIT

Require all mandatory generated views to be current. For nontrivial projects, `PROJECT_ATLAS.html` must exist, be reproducibly generated from registered canonical inputs, and have a current source fingerprint before final completion.


Before final build/user testing:

- no required AC remains unverified/reopened/stale;
- registries resolve;
- `verification/AUTHORITY_REACHABILITY.yaml` is current/passed with zero unreachable normative authorities/required Blueprints;
- Blueprint calls resolve;
- required implementation Blueprints map to real implementation;
- required tests/evidence mappings exist;
- no duplicate active responsibility owner;
- normal-user flow graph is complete;
- material SYSTEM_INTEGRATION ownership/runtime traces are coherent and current;
- release-relevant `verification/INTEGRATION_AUDIT.yaml` is current/passed when required;
- no known dead required config/contract or parallel authoritative path remains;
- final surface verification contract is satisfiable.

If this audit fails, return to SELECT_REQUIREMENT.

---

# 25. FINAL_BUILD_TEST

Build/package the actual target from the current intended final worktree.

Run:
- full relevant automated test suite;
- contract validator;
- build/package checks;
- artifact checks.

Do not declare complete yet for a user-facing product.

---

# 26. FINAL_USER_SURFACE_GATE

For user-facing products this is a hard release gate.

The agent MUST:

1. launch the actual final target from the normal user entry point;
2. invoke the selected interactive user-surface tool/adapter;
3. complete every release-gating E2E scenario;
4. capture the required screenshots/rendered checkpoints;
5. visually inspect them;
6. record non-stale evidence;
7. confirm no required obvious visual/runtime defect exists.

If `TOOL_CAPABILITIES.yaml` says an applicable tool is available but the evidence
index shows it was not invoked, the goal is NOT complete.

The contract validator should fail completion when required final evidence artifacts
or evidence IDs are missing/stale.

---

# 27. INDEPENDENT_REVIEW

Run only when triggered by project policy:
- consequential;
- high-risk;
- difficult to verify;
- materially blocked.

The review is read-only and independent.

Resolve material findings before completion.

Review does not replace final user-surface verification.

---

# 28. FINAL_GIT_CHECK

Before COMPLETE:

1. inspect `git status`;
2. inspect final relevant diff;
3. ensure no accidental temp/debug/secret/build junk is staged or tracked;
4. ensure registries point to current paths;
5. ensure final verification evidence corresponds to current code/worktree;
6. commit final verified project state when policy permits.

If relevant source changed after final release-gating evidence, invalidate that evidence
and rerun the affected final gate.

---

# 29. FINAL_CLAIM_RECONCILIATION

Immediately before any final completion report:

1. reread the canonical current-state authority;
2. reread the current Plan admission/completion rules and Acceptance Matrix;
3. enumerate the requested/master outcomes and required criteria;
4. bind each required criterion to evidence actually produced on the current revision;
5. execute any still-required build/runtime/browser/user-surface evidence — never replace it with a file/existence check;
6. reject stale evidence invalidated by later source/config/data changes;
7. confirm current admission/state is compatible with the claimed final status;
8. derive the report from that reconciliation.

Do not infer completion from:
- amount of code produced;
- file/module/function names;
- a green package/project-gate whose scope is narrower than product acceptance;
- an earlier milestone marked complete in prose;
- a foundation/M0/architecture gate;
- tests that do not exercise the required observable boundary.

If required runtime/browser evidence was never actually exercised, the corresponding outcome remains unverified.

# 30. COMPLETE

Only report completion when FINAL_CLAIM_RECONCILIATION and every applicable gate pass.

For user-facing products:

```text
canonical current state reconciled
+ every required AC mapped to current evidence
+ automated/build/integration gates complete
+ user-surface/runtime evidence actually exercised
+ required visual evidence complete
+ final black-box flow complete
+ repository state checked
= eligible for COMPLETE
```

The final report is a **derived view**, not a new status authority.

---

# Compiled-context bootstrap note

For projects produced by the compiler, a fresh implementation agent consumes the context-rich START snapshot, then reads `PROJECT_INDEX.yaml` and its direct `bootstrap.must_read` authorities (normally including `CONTEXT_HANDOFF.md` + `docs/DECISION_COMPENDIUM.md`) before source edits. Confirm authority-reachability and reconstruction gates are passed/current. `INTERVIEW_LEDGER.md` remains JIT provenance unless the current decision needs exact history. If `INTERVIEW_COVERAGE.yaml` is partial and a material unresolved user decision blocks correct implementation, ask it before committing to the affected behavior; do not silently infer it.

# Executable preflight and validator-quality gate

For a generated project that includes the project-native gate, insert it into execution rather than leaving it as an unused utility.

Required sequence for material work:

```text
fresh / resume / major compaction
→ reload bound Core-First Governance procedure if actually available
→ project gate: validate/preflight
→ resolve current admission + required authority/reference IDs
→ actually read/inspect them
→ classify Core-First change
→ material implementation
```

A failing gate blocks the dependent material edit until project truth or validation itself is repaired. Do not bypass it because unit/build/runtime code happens to execute.

Before moving to another material plan stage:
1. rerun admission evaluation;
2. verify required upstream maturity/evidence;
3. update current `STATE.current_admission` from the existing canonical Plan/Acceptance authorities;
4. only then select within the admissible work set.

After material authority/validator changes, run the gate's negative self-test. A validator change is incomplete until at least one known-bad mutant is rejected. Path existence alone is never sufficient structural validation for structured authorities.

After context compaction, an old green preflight/loaded-source record is stale session cache. Re-run preflight and reconsume the exact currently required inputs before more material edits.


# v2.24 Product-continuity checkpoint

At bootstrap, context recovery, and every material milestone transition:

```text
reconcile actual repository/runtime/evidence
→ read current STATE execution/admission pointer
→ read PROJECT_PLAN admission rules
→ read Acceptance/Evidence verification truth
→ compute admissible work
→ restate remaining master-product outcomes
→ choose next admissible stage/task
```

Do not allow a completed foundation/scaffold/walking skeleton to collapse the master goal.

`STATE` is the single current execution/admission pointer authority. It does not own product canon or verification truth. Derived views (`CONTINUE`, Handoff, Atlas, status prose) must be regenerated/reconciled from STATE + Plan + Acceptance/Evidence and must not disagree about current stage.

## Surface-fidelity routing before surface work

When the selected stage materially affects the user-visible surface:

1. resolve applicable User-Surface Authority/reference IDs through `PROJECT_INDEX`;
2. inspect the underlying visual references with an available capable tool before material styling/layout work;
3. load the shared Presentation/Design Core contracts and parent/slot composition rules;
4. carry the current visual target/baseline into the bounded work context;
5. after the smallest runnable change, inspect the whole relevant rendered surface, not only isolated controls.

If the project has material visual identity and only a generic/debug surface exists, treat that as connectivity evidence, not product-surface completion.

## Milestone convergence gate

Before `RECORD_MILESTONE` or admission advance, run the project-native convergence checks that exist for the project:

- prerequisite maturity/admission;
- required build/typecheck/test commands;
- required current evidence;
- canonical current-state consistency;
- project-specific canonical data/runtime probes where declared;
- registered active-owner uniqueness;
- milestone-boundary hygiene for disposable scratch/patch artifacts.

An interrupted session may contain temporary artifacts. Do not classify them as durable architecture until they are registered/consumed/claimed as such; however, do not carry unexplained scratch/shadow implementations across a clean milestone/handoff boundary.


# v2.26 Realization-graph driven continuation

After each verified milestone, do not select the next task only from architecture dependencies.

Reconcile:

```text
current verified flow nodes
+ remaining required APP_FLOW/workflow nodes
+ architecture admission/dependencies
+ Acceptance gaps
→ next admissible product-realization stage
```

A runnable primary experience does not authorize stopping while required shell/setup/result/persistence/replay/other lifecycle nodes remain unverified.

When several architecture tasks are possible, prefer work that unlocks the next required normal-user flow node unless risk/dependency evidence justifies another order.

At context recovery, restate the remaining required product-flow nodes before resuming implementation.


# v2.27 Derived admission / autonomous continuation

The implementation agent does not create admission by editing STATE.

At every milestone boundary:

```text
produce/update evidence
→ project_gate derives current maturity/admission
→ reconcile STATE pointer to the derived result
→ choose next admissible realization stage
→ continue automatically
```

Stop only for:
- Product Complete / requested terminal status;
- a genuine blocking USER_DECISION;
- a demonstrated external dependency/capability blocker that cannot be resolved within authorization;
- explicit user stop.

Do not stop merely because one milestone passed.

When `STATE` disagrees with derived admission, the gate wins the **validation verdict**; correct the pointer/derived views, do not weaken Plan/Acceptance.

# v2.27 Shipping-content and consumer-rights runtime checks

Where the relevant contracts exist:
- reject `test_fixture`/`debug_only` content reachable from production defaults, progression or normal user flow;
- require explicit promotion before `prototype` becomes production;
- verify consumer/adapter mutations travel through allowed commands/contracts rather than direct foreign writes.

# v2.27 Persistence verification

When Continue/Resume is a required product outcome, load the persistence coverage contract and verify every material runtime state owner is classified as persisted, deterministically reconstructed, intentionally transient or forbidden to persist. Use the strongest project-required restore equivalence test; do not inflate a partial snapshot roundtrip into full Continue verification.


# v2.29 Review-driven continuation

When the compiled project declares representative product-path heartbeats or deterministic review projections:

1. identify whether the current material change can invalidate any declared heartbeat/projection;
2. rerun the narrowest affected heartbeat after the change reaches a runnable state;
3. regenerate/re-exercise affected review projections from canonical sources/state;
4. repair failures at canonical owners/producers rather than patching derived review/generated outputs;
5. continue through the Product Realization roadmap after evidence is reconciled.

Do not turn this into unconditional full-regression-after-every-edit behavior.

Finish/fidelity `PR-*` outcomes are ordinary product obligations. Do not defer them automatically to a final cleanup phase, and do not treat them as complete merely because the underlying feature is functional.


# v2.31 Repair-by-Invariant runtime loop

For a reported defect, do not begin with the nearest implementation file.

Use:

```text
REPRODUCE
→ identify failed observable/Acceptance
→ determine LOCAL_DEFECT vs COHERENCE_DEFECT
→ resolve applicable SYSTEM_INTEGRATION invariant/trace
→ inspect canonical source/owner and dependent consumers
→ repair the highest correct owner/derivation seam
→ rerun affected invariant evidence
→ rerun affected Product Heartbeat / Review Projection
```

A bounded local repair is correct when the owning implementation itself is wrong and no shared relationship is violated.

A consumer-local patch is suspect when:
- the same corrective value/rule appears in multiple consumers;
- the fix compensates for stale/duplicated canonical data;
- changing the canonical source would re-break the consumer;
- another projection remains inconsistent after the patch.

Do not turn a symptom workaround into permanent architecture.

# v2.31 Skeleton survivability admission

A runnable skeleton may be used for learning before production admission.

Before advancing a stage whose claim is `production foundation/skeleton ready`, require the project-declared survivability Acceptance evidence. Re-derive the claim from Plan + Acceptance/Evidence; never infer it from `STATE`, a green build, or the fact that the path runs.

If the survivability challenge fails, keep the current path classified as exploratory/provisional, correct the owner/contract/composition seam, and repeat the smallest representative challenge before widening production breadth.
