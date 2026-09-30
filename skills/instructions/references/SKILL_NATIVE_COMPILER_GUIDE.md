# Skill-Native Compiler and Project Skill Guide

# Current Precedence — v2.34 Plugin-First Compiler + JIT Companion Procedures

The Prompt Compiler is plugin/Skill-native. The 20 detailed compiler guides are exposed beneath the Skill as JIT references; there is one active runtime model, not a second compatibility runtime.

When `core-first-governance` is available, resolve its procedures JIT rather than embedding a second copy of Governance. Architecture/ownership/reuse materiality requires the primary agent to load and apply `core-first-extension-architecture` before freezing the change boundary; use `core-first-orchestration` for current routing semantics when needed. Verification/review procedures remain separately triggered. Project correctness must still degrade safely when the companion plugin is absent.

Skill selection remains capability-driven and provider-neutral. Review external source/version/commit/hash, scripts, dependencies, license, permissions, trigger scope and overlap. Skills are procedures; project authorities are truth. Do not require multiple simultaneously active skills for correctness.

---


## Purpose

The Project Compiler is plugin/Skill-native. The same compiler workflow must remain usable by any sufficiently capable Agent-Skills-compatible coding agent; provider-specific behavior belongs in runtime adapters, not the compiler model.

Use three distinct skill layers:

```text
1. COMPILER SKILL
   reusable meta-workflow that converts user vision into project authorities

2. EXTERNAL EXPERTISE SKILLS
   engine/framework/domain workflows maintained outside the project

3. PROJECT-LOCAL SKILLS
   small repeated authoring/verification workflows specific to this repository
```

Skills are execution guidance. They are never the canonical source of product behavior.

---

# 1. Compiler as the primary plugin Skill

Ship the compact compiler Skill as the runtime interface. Package the detailed compiler guides beneath it as JIT `references/`; do not paste them into the always-loaded Skill body.

Recommended portable/plugin layout:

```text
skills/instructions/
  SKILL.md
  references/
    COMPILER_GUIDE.md
    INTERVIEW_COMPLETENESS_AND_HANDOFF_GUIDE.md
    VISION_AND_REFERENCE_PRESERVATION_GUIDE.md
    FRESH_AGENT_RECONSTRUCTION_GUIDE.md
    SYSTEM_COMPOSITION_AND_ATLAS_GUIDE.md
    CAPABILITY_HIERARCHY_AND_CHANGE_GATE_GUIDE.md
    SYSTEM_INTEGRATION_AND_RUNTIME_TRACE_GUIDE.md
    SKILL_NATIVE_COMPILER_GUIDE.md
    AGENT_RUNTIME_PORTABILITY_GUIDE.md
    BLUEPRINT_GUIDE.md
    BLUEPRINT_REPOSITORY_GUIDE.md
    HIERARCHICAL_INSTRUCTIONS_GUIDE.md
    DELIVERY_AND_VERIFICATION_GUIDE.md
    EXECUTION_RUNTIME_GUIDE.md
    USER_SURFACE_VERIFICATION_GUIDE.md
    RUNTIME_GUIDE.md
    BOOTSTRAP_PROMPT_AND_GOAL_GUIDE.md
    RUNTIME_TEMPLATES.md
    BLUEPRINT_TEMPLATES.md
  assets/
    PROJECT_ATLAS_TEMPLATE.html
    PROJECT_SKILL_TEMPLATE.md
  evals/                         # optional structured skill evals
    evals.json
```

`SKILL.md` should be compact and route to references JIT. Do not paste the entire reference pack into its always-loaded body. In a plugin host, invocation may load this kernel automatically; that does not authorize preloading its references.

The skill supports:
- compiling a new project from natural-language intent;
- updating an existing compiled project after new user decisions;
- auditing a project package for vision/system/coverage/discoverability drift;
- deriving external and project-local skill requirements;
- producing context-rich Start/Goal/Continue prompts and project authorities.

It does **not** automatically mean "implement the product now". Compilation and implementation remain separate unless the user explicitly asks for both.

---

# 2. Skill discovery is a routed capability

Derive skill needs from:

```text
CURRENT REQUIREMENT
+ relevant SYSTEM_MAP systems
+ product surface
+ framework/engine/language
+ asset workflow
+ required verification evidence
```

Then resolve in this order:

1. inspect already installed/global skills;
2. inspect repository-local `.agents/skills/`;
3. inspect harness/plugin-provided skills;
4. search curated known collections when relevant;
5. search GitHub/web for a missing capability when external search is available;
6. only then consider generating a project-local skill.

Prefer the open Agent Skills structure and `.agents/skills/` as a portable repository location when the selected harness supports it. Treat discovery paths and provider-specific metadata as version-sensitive runtime facts: verify the current target harness and record them in `AGENT_RUNTIME_PROFILE.yaml` instead of freezing them into product truth.

Do not search for skills merely because a project is large. Search when a recurring workflow or specialist capability can materially improve reliability.

---

# 3. Minimal active skill set

Installed does not mean loaded. Discovery metadata still consumes context and broad catalogs increase trigger ambiguity, so keep enabled/global catalogs curated even though full skill bodies load JIT.

For each task select only the minimum relevant skills. Preferred routing shape:

```text
requirement
  -> system IDs
  -> capability needs
  -> router/skill metadata
  -> 1..N minimal matching skills
  -> task execution
```

Examples:

```text
target framework screen/layout requirement
-> SYS-UI-SHELL + target framework/language
-> framework-ui + accessibility/design-system
```

```text
external provider integration requirement
-> SYS-INTEGRATION + provider contract
-> framework-integration + API/testing skill
```

Do not load an entire domain catalog into active task context.

---

# 4. External skill review gate

A GitHub skill is executable/instructional supply-chain input. Before installing or adopting it, inspect enough to establish:

- scope matches the actual capability gap;
- source/version/commit and, when practical, content integrity/hash are recorded;
- maintenance/activity is reasonable for the dependency;
- target engine/framework/version is compatible;
- `SKILL.md` instructions are bounded and do not conflict with project authorities;
- scripts/dependencies are understood before execution;
- license permits intended use/distribution;
- it does not request unnecessary credentials/permissions/destructive actions;
- it does not duplicate a better already-installed skill;
- its description/trigger is narrow enough for reliable routing.

Prefer version/commit pinning when the project depends materially on behavior that may change.

Global installation is a user/environment choice unless policy explicitly permits it. Repository-local reversible skill installation may be automated when policy allows and the source passed review.

Never execute third-party setup/install scripts blindly merely because a repository calls itself a skill collection.

---

# 5. Capability-first catalogs, not domain cargo cults

Curated collections and vendor/community catalogs are discovery sources, not authorities and not installation checklists.

Derive candidates from the actual project first. Common capability families include:
- skill creation/evaluation;
- codebase reconnaissance/onboarding;
- language/framework/engine expertise;
- testing, browser/app QA and visual verification;
- debugging/build/CI;
- code/security review;
- MCP/integration authoring;
- frontend/design-system implementation;
- database/migration/data workflows;
- deployment/release;
- artifact creation;
- observability/performance;
- agent governance/supply-chain safety.

Different projects resolve these families differently: an interactive application may need framework/input/presentation skills; a website may need accessibility/browser/design-system skills; an API/business workflow may need auth/data/integration/observability skills. These are examples, never universal product-type requirements.

Resolve the smallest sufficient set and record rejected/overlapping candidates so later agents do not repeatedly rediscover them.

# 6. `SKILL_REQUIREMENTS.yaml` becomes a resolution contract

Keep capability requirements vendor-neutral, but record concrete resolutions after discovery.

Recommended shape:

```yaml
schema_version: 2

requirements:
  SKILLREQ-FRAMEWORK:
    capability: target framework implementation guidance
    needed_by: [SYS-UI-SHELL, SYS-NAVIGATION]
    load_when: [framework_task]
    priority: high
    resolution:
      status: resolved
      skill: framework-guidance
      source: "[reviewed source]"
      scope: global
      version_or_commit: "[pin when material]"
      content_hash: "[record when practical]"
      license: "[record]"
      reviewed: true

  SKILLREQ-CONTENT-AUTHORING:
    capability: add content through canonical schema/validation/registry paths without duplicating domain logic
    needed_by: [SYS-CONTENT]
    load_when: [content_authoring]
    priority: medium
    resolution:
      status: project_local
      skill: entity-authoring
      source: .agents/skills/content-authoring/SKILL.md
      reviewed: true
```

Statuses may include:
- `unresolved`
- `candidate_found`
- `resolved`
- `project_local`
- `optional`
- `rejected`
- `blocked_permission`
- `blocked_capability`

Record rejection reasons so future agents do not repeatedly rediscover unsuitable skills.

---

# 7. When to generate a project-local skill

Generate a repository-local skill only when all are true:

1. the workflow repeats across multiple tasks/content items or sessions;
2. the workflow is procedural agent guidance, not product truth;
3. canonical project authorities already define the underlying behavior;
4. no existing installed/external skill adequately captures the procedure;
5. having a skill materially reduces drift, duplicate ownership, or repeated setup mistakes.

Good examples:
- `content-authoring`: create a new definition through the canonical schema/validation/registry path, then run authoring proof;
- `provider-integration`: add a provider behind the existing contract without creating provider-specific domain ownership;
- `screen-implementation`: implement a new screen from flow + visual contract + shell/navigation systems, including required visual evidence;
- `release-evidence`: execute this repository's exact build + black-box + screenshot evidence workflow.

Bad examples:
- one skill for every master system;
- a skill containing the complete interaction specification;
- a skill containing product values that belong in canonical content/config data;
- a one-off skill for a single bug fix.

---

# 8. Project-local skill structure

Prefer the open Agent Skills shape. Use the portable project skill location selected by `AGENT_RUNTIME_PROFILE.yaml` (commonly `.agents/skills/` when supported):

```text
.agents/skills/content-authoring/
  SKILL.md
  references/        # only if procedure-specific support is useful
  scripts/           # only deterministic helpers that earn their maintenance cost
```

Keep portable `SKILL.md` frontmatter minimal (`name`, `description`) unless a provider extension is intentionally generated as a thin overlay. A project-local `SKILL.md` should:
- have a narrow name/description with strong trigger terms;
- state when **not** to use it;
- point to canonical artifact/system IDs that must be read first;
- describe the repeatable procedure;
- state reuse/duplicate-owner constraints;
- declare verification expected after the workflow;
- avoid copying long project specs into the skill.

Example concept:

```markdown
---
name: entity-authoring
description: Add or modify content in this repository through the canonical schema, validation, registry and owner paths. Use for repeated content authoring; do not use to redesign canonical owners.
---

1. Read SYSTEM_MAP entries for the required systems and the entity content authority.
2. Inspect an existing representative entity and the content registry.
3. Add data/profiles/animations/moves through declared extension points.
4. Do not add consumer-local validation, state ownership, provider bypasses or presentation architecture when canonical owners already exist.
5. Run content/schema tests and the representative runtime/content entity check.
```

---

# 9. Project-specific skill generation during compilation

During project compilation:

1. create `contracts/SYSTEM_MAP.yaml`;
2. identify repeated authoring/verification workflows implied by the project;
3. inspect available skills;
4. resolve external skills first where appropriate;
5. propose/generate only justified project-local skills;
6. register them in `SKILL_REQUIREMENTS.yaml`;
7. reference them from Start/Continue prompts only by capability/trigger where useful;
8. let runtime routing load them JIT.

Do not generate dozens of speculative project skills before a workflow actually exists.

For greenfield projects, likely project-local skills may be declared as `planned` and created only when their first real workflow becomes concrete.

---

# 10. Skill/version drift

External skills can become stale even when the project does not.

When a material skill is version-sensitive:
- record source + version/commit;
- compare its target framework/engine version with the repository;
- re-evaluate after major engine/framework upgrades;
- do not silently upgrade if changed guidance could alter architecture/behavior;
- keep project authorities independent so replacing a skill does not rewrite project truth.

---

# 11. Skill validation

Before treating a generated project-local skill as ready:

- validate required frontmatter (`name`, `description`);
- verify paths/references resolve;
- ensure it does not duplicate project canon;
- ensure triggers are neither too broad nor too vague;
- test it on representative positive and negative trigger prompts and at least one real execution task when practical;
- for material skills, keep structured eval cases (for example `evals/evals.json`) when the harness/tooling can run them;
- for materially influential external/project skills, compare output/evidence against the unskilled or baseline workflow when feasible; a skill that adds context but does not improve reliability need not remain active;
- confirm it causes the agent to read the intended authorities and follow the intended workflow;
- revise the skill when an eval shows non-triggering, over-triggering, or workflow drift.

Skills are implementation aids and should be evaluated like other executable project processes.

---

# 12. Compiler recoverability invariant

The installable plugin package must contain enough canonical kernel + routed references to reconstruct the compiler model without release-history or chat dependence. Preserve these core invariants:

```text
whole user vision preserved
-> readable decision model + Fresh-Agent Reconstruction
-> master systems defined
-> compositions reuse systems
-> skills routed as capabilities
-> provider-neutral runtime primitives selected by semantic purpose
-> project authorities remain canonical
-> every normative authority is discoverable through PROJECT_INDEX and required sources are loaded before dependent edits
-> context-rich Start/Goal/Continue handoff
-> evidence-based completion
```

Do not let plugin UI metadata, host memory, or historical release notes become the only place that knows how to compile the project. Canonical behavior remains recoverable from the packaged Skill + routed references.


---

# 13. Plugin-native JIT routing boundary

The plugin Skill is an orchestrator kernel, not a second policy corpus. Route material compiler concerns to the existing reference owner before acting:

| Material compiler trigger | JIT owner(s) |
| --- | --- |
| classify/research/compile mode | `COMPILER_GUIDE.md` |
| interview rounds, coverage, verbatim provenance, handoff | `INTERVIEW_COMPLETENESS_AND_HANDOFF_GUIDE.md` |
| references, visual/product intent preservation | `VISION_AND_REFERENCE_PRESERVATION_GUIDE.md` |
| responsibility coverage, systems, composition, Atlas | `SYSTEM_COMPOSITION_AND_ATLAS_GUIDE.md` |
| capability/change class/reuse/extension | `CAPABILITY_HIERARCHY_AND_CHANGE_GATE_GUIDE.md` + companion Core-First when available/material |
| cross-system owner/state/producer/runtime trace | `SYSTEM_INTEGRATION_AND_RUNTIME_TRACE_GUIDE.md` |
| runtime provider/skills/hooks/memory/plugin bindings | `AGENT_RUNTIME_PORTABILITY_GUIDE.md` + this guide |
| Blueprint/repository topology and source identity | `BLUEPRINT_GUIDE.md`, `BLUEPRINT_REPOSITORY_GUIDE.md` |
| product-realization/Acceptance/evidence/completion | `DELIVERY_AND_VERIFICATION_GUIDE.md` |
| execution order/admission/current work | `EXECUTION_RUNTIME_GUIDE.md` |
| actual UI/runtime/external observable evidence | `USER_SURFACE_VERIFICATION_GUIDE.md` + companion observable verification when available/material |
| context/runtime/recovery/required-source gates | `RUNTIME_GUIDE.md` |
| START/CONTINUE/GOAL | `BOOTSTRAP_PROMPT_AND_GOAL_GUIDE.md` |
| fresh-agent fidelity/completeness challenge | `FRESH_AGENT_RECONSTRUCTION_GUIDE.md` |
| concrete artifact shapes | relevant template file only |

If one turn crosses several boundaries, load only the owners needed for the next material decision; sequence them when concurrent Skill composition is unreliable. Current project/package authorities outrank remembered Skill content.

## Companion Core-First routing

Do not mirror the companion plugin's detailed orchestration inside APC. Keep only trigger knowledge here:

- architecture/ownership/authoritative state/reuse/composition/capability/provider/extension material → primary agent must load/apply `core-first-extension-architecture`;
- routing/freshness/verification semantics needed → load `core-first-orchestration` or its specific JIT procedure;
- architecture conformance material → `core-first-verifier` in fresh read-only isolation when feasible;
- real external/user outcome material → `observable-product-verification`;
- consequential/high-risk/difficult-to-verify implementation → `independent-review`.

If the plugin is unavailable, follow APC's project-native owners and gates without fabricating external Skill use.

# Interview-complete compiler behavior

`INTERVIEW_COMPLETENESS_AND_HANDOFF_GUIDE.md` solely owns question rounds/Q&A/coverage/handoff; `FRESH_AGENT_RECONSTRUCTION_GUIDE.md` solely owns the Decision Compendium, guardrails/example semantics/adversarial abstraction checks and reconstruction-fidelity acceptance. The Skill routes to those guides instead of duplicating either policy.


# Atlas lifecycle in the compiler Skill

For nontrivial projects generate `PROJECT_ATLAS.html`, register a reproducible generator, route the view for bootstrap inspection, validate freshness after source changes, and require fresh-agent/context-recovery inspection. The Atlas is a procedure/orientation artifact, never project truth.
