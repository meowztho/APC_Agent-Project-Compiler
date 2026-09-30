# System Composition and Project Atlas Guide

# Current Precedence — v2.22 Product Capability Envelope, Responsibility Discovery and Atlas

Before freezing `SYSTEM_MAP` in greenfield/unclear projects, discover durable Responsibilities from outcomes, authoritative state/decisions, workflows/events, external/I-O boundaries, data/lifecycle/persistence boundaries and, for existing repositories, APIs/call graphs/tests. Do not convert every feature noun into a system.

Terminology: Project Authority Artifact documents truth; it is not the runtime/domain Responsibility Owner. A Responsibility Owner/Master System owns a durable policy/state responsibility. Capability Contracts expose reusable semantics beneath owners. Modules/Providers realize contracts; Consumers compose them.

For nontrivial projects Atlas remains mandatory generated orientation, never normative truth. Its generator/fingerprint/freshness lifecycle must reflect roadmap/build-order and phase-admission status from canonical `PROJECT_PLAN`/Acceptance authorities. On fresh session/context recovery inspect a fresh Atlas for whole-project orientation, then load exact normative sources; Atlas inspection never replaces source reads.

---


## Purpose

A project can be accurately described and still drift if the coding agent is repeatedly allowed to invent the same responsibility in several places.

The compiler must therefore turn the product into a **coherent set of canonical master systems** and make higher-level product objects compose those systems instead of rebuilding them.

Examples:

```text
Interactive consumer
= Input/Command System
+ Runtime State/Policy System
+ Action/Workflow System
+ Presentation System
+ Consumer Data/Profiles/Modifiers
```

```text
Website page
= Site Shell
+ Navigation System
+ Typography/Theme System
+ Layout System
+ Motion/Effects System
+ Data/API System
+ Page Content
```


```text
Discord-as-UI automation
= Discord Interaction Core (post/edit/stop/enable/disable lifecycle)
+ Scheduler/State System
+ Desktop GUI consumer
+ Feature modules
+ per-consumer configuration/modifiers
```

The desktop GUI or a new feature should call/compose the same posting/lifecycle core rather than recreating when/how Discord messages are posted. One central rule change then propagates to every consumer unless a declared local modifier/replacement intentionally differs.

The exact system set is project-specific. The compiler discovers it from the user's vision, references, product surface, and future extension requirements.

---

# 1. System-first decomposition

Apply the single-owner/reuse principle to every coding project. Scale the number/formality of systems to complexity: a tiny program may need only a few clear responsibility boundaries, while a large application needs explicit contracts and many system authorities. Modularity means shared reusable behavior is not copied per consumer; it does **not** mean manufacturing unnecessary services/classes.

Before creating task-sized Blueprints, identify the durable responsibilities that should exist once and be reused. `CAPABILITY_HIERARCHY_AND_CHANGE_GATE_GUIDE.md` is the canonical authority for how far to decompose below master systems and for classifying later user-request deltas.

Generate for nontrivial projects:

```text
contracts/SYSTEM_MAP.yaml
```

A master system should have:
- stable `system_id`;
- one clear responsibility scope;
- what responsibility domain belongs to it;
- what it explicitly must not own;
- public semantic interface/capabilities;
- dependencies;
- configuration/data inputs;
- extension/modifier/explicit-replacement points;
- systems/objects that consume it;
- authoritative docs/Blueprint IDs;
- acceptance/verification links.

Do not use arbitrary folder names as systems. A system exists because it owns a durable responsibility.

---

# 2. Example system maps

## Interactive realtime application (illustrative)

Possible responsibility candidates, adapted to the actual product:

```text
SYS-INPUT-COMMAND       semantic inputs/commands and source routing
SYS-RUNTIME-STATE       canonical actor/session state where applicable
SYS-MOVEMENT-STATE      spatial/state-transition rules when movement exists
SYS-ACTION              action availability, validation and execution semantics
SYS-ENVIRONMENT         shared environment/boundary/world rules when applicable
SYS-PRESENTATION        presentation requests/bindings
SYS-CONTENT             definitions/profiles/configuration and selection
SYS-SESSION-FLOW        lifecycle, setup, active flow, result/exit state
SYS-UI-SHELL            persistent shell/navigation surfaces
SYS-SETTINGS            configuration/accessibility/persistence where applicable
SYS-AUTHORING           builder/content-authoring path when it proves modularity
```

This is not a checklist. The Product Capability Envelope decides what is applicable; responsibility discovery decides what deserves a canonical owner.

## Website / web application

Possible candidates:

```text
SYS-WEB-SHELL          app/site shell and global regions
SYS-NAVIGATION         routes, navigation state, breadcrumbs/history
SYS-THEME              colors, design tokens, light/dark variants
SYS-TYPOGRAPHY         font roles, scale, text rhythm
SYS-LAYOUT             responsive layout primitives/grid/spacing
SYS-MOTION             transitions, effects, reduced-motion behavior
SYS-COMPONENTS         reusable UI primitives
SYS-PAGE-COMPOSITION   page-specific composition using shared systems
SYS-FORMS              form behavior, validation, submission feedback
SYS-DATA               fetching/cache/state/API integration
SYS-AUTH               identity/session/authorization when applicable
SYS-ACCESSIBILITY      focus, keyboard, semantics, contrast policy
SYS-SEO-METADATA       when applicable
SYS-AUTHORING          CMS/template/admin authoring when it is a core extension path
```

Again, derive the actual map from the project rather than forcing a template.

---

# 3. Master once, reference many

The most important invariant:

> A reusable responsibility is defined once at its canonical owner. Consumers reference/configure it; they do not rebuild local copies.

Example for a configurable consumer:

```yaml
composition:
  consumer_priority:
    type: configurable_consumer
    uses:
      - SYS-INPUT-COMMAND
      - SYS-RUNTIME-STATE
      - SYS-ACTION
      - SYS-PRESENTATION
    data:
      definition: DATA-CONSUMER-PRIORITY
    profiles:
      behavior: priority_default
    modifiers:
      timeout:
        op: add
        value: 8
```

The consumer does **not** own another command parser, state engine, action-policy engine, or presentation architecture.

Local variation belongs in data/config/profiles/declared modifiers or intentional explicit replacements.

## Defaults, profiles, modifiers, and replacement policy

Each reusable system should define, where applicable:
- canonical defaults and their provenance;
- reusable profiles/presets;
- allowed local modifiers and explicit replacements;
- forbidden per-object duplication/bypass;
- what kind of change requires editing the master system contract instead of adding a modifier/replacement.

Prefer:

```text
master default
+ reusable profile
+ small explicit modifier (preferred when base changes should propagate)
```

over copying the system and customizing the copy. Defaults may be user-confirmed, reference-derived, researched, or compiler-selected; record the provenance when it materially affects later decisions.

## Consumer shell + layered value resolution

For reusable architectures, prefer a thin **consumer shell** (entity/page/bot/workflow/component host) that composes canonical systems/modules plus data instead of embedding copies of those systems. The consumer may own identity/content-specific state and declared local modifiers, but shared reusable behavior remains at its master owner.

Do not use the word `override` without defining its merge semantics. A local value can mean very different things:

- `add` / delta;
- `multiply`;
- `replace` (absolute value);
- `min` / `max`;
- collection `append` / `remove`;
- another project-specific deterministic merge operator.

Prefer **relative modifiers** when the user expects global/base changes to propagate. Example:

```text
ReusableAction base timeout = 5
Consumer modifier = add +8
Effective timeout = 13

Later ReusableAction base = 7
Same consumer modifier = +8
Effective timeout = 15
```

Do not store `13` as a copied consumer value in this case; that would sever propagation from the canonical ReusableAction definition. Use explicit `replace: 13` only when the consumer is intentionally fixed independently of future base changes.

For important configurable values, define the resolution pipeline, for example:

```text
master/system default
→ content/module definition
→ reusable profile/preset
→ consumer-specific modifier
→ contextual/runtime modifier
→ effective value
```

Each field/system may use a different valid subset/order, but it must be deterministic and traceable when material. Core changes should propagate automatically through non-replacing layers.

This principle applies beyond games: shared bot scheduling + channel-specific timing deltas, site theme tokens + page-specific modifiers, API retry defaults + endpoint modifiers, workflow defaults + customer-specific policy deltas, etc.

---

# 4. Input/Command vs Action/Workflow

Avoid coupling input-source mechanics to consumer-specific behavior.

## Input/Command System
Owns, as applicable:
- semantic commands/actions;
- device/API/UI source mappings;
- source ownership/context;
- buffering/debouncing where globally applicable;
- remapping/configuration/persistence;
- normalized command events.

It should not own one consumer's action catalog or domain policy.

## Action/Workflow System
Owns, as applicable:
- actions available to a consumer/profile;
- sequencing/timing/preconditions;
- transitions/chains;
- action state/validity;
- resource/rate/policy requirements;
- consumer-specific variation through definitions/profiles.

The Action/Workflow system consumes semantic commands from the Input/Command system. A new consumer normally adds data/profile/action definitions, not another input stack. If a project intentionally combines these responsibilities, define one canonical combined owner rather than recreating it per consumer.

---

# 5. Composition objects

Many user-facing things are not standalone systems. They are **compositions**.

Examples:
- configurable actor/consumer;
- page/page template;
- dashboard;
- product workflow;
- provider-backed integration;
- report/export definition;
- editor/authoring tool.

Generate composition definitions when reuse matters, either in `contracts/SYSTEM_MAP.yaml`, `contracts/CONTENT_REGISTRY.yaml`, or dedicated data Blueprints.

Each composition should state:
- systems it uses;
- data/profile IDs;
- allowed profiles/modifiers/explicit replacements;
- forbidden local duplicate ownership;
- verification that the shared systems are actually reused.

## Authoring as architecture proof

When the user's modular/data-driven goal depends on creating new content without core-code changes, model the authoring/builder path as a first-class system/domain instead of a late convenience UI. It must produce data/content consumed by the same canonical runtime systems. Use `FRESH_AGENT_RECONSTRUCTION_GUIDE.md` for the operational authoring proof and adversarial examples.

---

# 6. System Map contract

Recommended shape:

```yaml
schema_version: 1

systems:
  SYS-INPUT-COMMAND:
    responsibility: semantic command normalization and source routing
    authority_ids: [DOC-INPUT, BP-SYS-INPUT, DATA-ACTIONS]
    responsibility_scope:
      - semantic_command_registry
      - source_assignment
      - input_context
    must_not_own:
      - consumer_action_catalog
      - domain_outcome_policy
    provides:
      - semantic_command_stream
      - mapping_api
    depends_on: []
    consumed_by:
      - SYS-ACTION
      - SYS-NAVIGATION
    verification:
      - AC-INPUT-CANONICAL

compositions:
  configurable_consumer:
    required_systems:
      - SYS-INPUT-COMMAND
      - SYS-RUNTIME-STATE
      - SYS-ACTION
      - SYS-PRESENTATION
    local_duplicate_ownership_forbidden: true
```

`SYSTEM_MAP.yaml` is authoritative for **top-level system topology and responsibility scope**. When reusable capability depth is material, `CAPABILITY_GRAPH.yaml` owns the semantic hierarchy below/among master systems. `SYSTEM_INTEGRATION.yaml` owns material per-rule decision ownership, mutable-state ownership, allowed writers and cross-system runtime edges. Do not maintain competing detailed ownership matrices across them.

`SYSTEM_MAP.yaml` should be compact **as a routing/topology contract**, but the project package itself is not compactness-limited. Every nontrivial core system should have a detailed canonical authority plus bounded Blueprints/contracts where applicable. Detailed rules must never be dropped merely to keep the file count small.

---

# 7. Product Capability Envelope + system discovery protocol

Before the final `SYSTEM_MAP`, infer a provisional **Product Archetype** and **Expected Capability/Responsibility Envelope** from the confirmed vision, reference traits, product modality and general domain knowledge. This lets the compiler contribute knowledge the later implementation agent may not have in active context.

The envelope is a coverage surface, not a class/file/service list. It answers: *what ordinary responsibilities/capabilities should a competent designer/engineer at least consider for this requested product?* A responsibility may ultimately live inside an existing owner, be configuration/content, be deferred, be not applicable, or require a user decision. Do not create systems merely to make the envelope look complete.

A useful decomposition test is to expand user-visible outcomes until the required semantic supports become visible. For example, a multi-participant interactive flow implies participant/slot instances and some source of control/actions; an actor that can perform actions normally implies state, action mapping and presentation/runtime consequences. These are inference prompts, not mandated names/mechanics. Continue only as deep as needed to expose durable responsibilities, reuse seams and integration paths.

During project compilation:

1. preserve the whole user vision/reference semantics;
2. infer a provisional product archetype + expected capability/responsibility envelope;
3. run the domain-expert omission challenge and disposition every material envelope item;
4. identify user-visible product areas/workflows and required actors/instances/providers;
5. identify authoritative state/decisions, repeated/stateful and cross-cutting responsibilities;
6. identify future variation that should be data/config/module/provider rather than new owners;
7. propose canonical Responsibility Owners/master systems and capability contracts;
8. inspect relationships, producer convergence and ownership conflicts;
9. ask the user only if boundaries/behavior materially change user-owned product semantics;
10. challenge the map with representative/adversarial cases when reuse/extensibility matters;
11. compile `contracts/SYSTEM_MAP.yaml` and `CAPABILITY_GRAPH.yaml` where needed;
12. require Fresh-Agent Reconstruction before final fine-grained task decomposition;
13. create bounded Blueprints/specs beneath those systems.

Do not let the coding agent decide the fundamental system topology from scratch when the compiler can derive it from confirmed intent.

Reversible implementation details inside a system remain delegated.

---

# 8. Ownership and runtime integration layer

`SYSTEM_MAP.yaml` says which master system owns a durable responsibility. For material cross-system rules/state/configuration, also generate `contracts/SYSTEM_INTEGRATION.yaml` using `SYSTEM_INTEGRATION_AND_RUNTIME_TRACE_GUIDE.md`.

This second contract distinguishes decision owner, state owner, producers, allowed writers and consumers; it records producer -> contract/data -> consumer paths and prevents two locally plausible systems from implementing the same rule independently.

A composition is not proven reusable merely because it references shared systems in YAML; runtime must actually consume those systems/data through the canonical path.

---

# 9. System-level acceptance

A master system is not proven merely because one consumer works.

Where important, acceptance should prove:
- the canonical owner exists;
- consumers use it through the intended interface;
- no duplicate owner exists;
- configuration/profiles/modifiers work without forking the system and relative modifiers inherit canonical base changes;
- at least one additional representative consumer can reuse it where relevant.

Example:

```text
AC-SYS-INPUT-01
- UI and external/API producers both route through the same semantic command registry
- consumer A and B do not own separate command parsers
- mapping/config changes update behavior without consumer-local code changes
```

---

# 10. Skill boundary

System composition determines **which capabilities are needed**, but skill lifecycle/routing is a separate authority. Use `SKILL_NATIVE_COMPILER_GUIDE.md` for `contracts/SKILL_REQUIREMENTS.yaml`, installed/global/project/harness discovery, external GitHub review, minimal JIT activation, and project-local skill generation.

Invariant:

```text
SYSTEM_MAP / system authorities = what exists and how it must behave
SKILL_REQUIREMENTS / skills       = how an agent performs recurring work
```

Never put project truth into a skill, and never duplicate skill-resolution policy in this guide.

---

# 11. Bootstrap prompt boundary

System composition must be visible in the initial implementation context, but this guide does not own prompt construction. `BOOTSTRAP_PROMPT_AND_GOAL_GUIDE.md` defines the context-rich START/GOAL/CONTINUE policy.

Invariant: a fresh implementation agent should see the master-system/composition model directly in its initial orientation instead of having to infer it from a pointer chain.

---

# 12. Project Atlas HTML

Agents often reason well when the project is presented as one visually scannable page. For every **nontrivial compiled project**, generate and maintain:

```text
PROJECT_ATLAS.html
```

It is a **generated view**, not a new authority.

Recommended sections:
- product/vision capsule;
- decision-model highlights and important guardrails/example semantics;
- Authority Reachability/discoverability status;
- Fresh-Agent Reconstruction status;
- master system cards;
- system dependency/composition map;
- product object compositions (e.g. entity = systems + data);
- primary screens/pages and user flow;
- visual shell/reference thumbnails/links where practical;
- current acceptance status;
- representative architecture-proof status when reuse/composition is material (integration case, heterogeneous proof cases, covered variation axes);
- unresolved decisions/blockers;
- skill/capability status;
- latest verification summary;
- links/paths/IDs to canonical project artifacts.

The Atlas should be standalone HTML/CSS when practical so it opens locally without a build step.

---

## Project Atlas vs runtime Working View

Keep two concepts distinct:

```text
PROJECT_ATLAS.html
= compiler-generated, reproducible, non-authoritative package orientation view with freshness lifecycle

Agent Working View / Working Atlas
= optional disposable runtime reasoning cache created by an implementation/orchestration agent
```

A temporary Working View never becomes project truth and does not satisfy the compiler's `PROJECT_ATLAS.html` lifecycle; conversely the Project Atlas is not a scratchpad for the running agent.

# 13. Atlas generation rule

Preferred flow:

```text
canonical project files
SYSTEM_MAP / APP_FLOW / USER_VISION / DECISION_COMPENDIUM / PROJECT_INDEX / guardrails / registries / acceptance / reachability / reconstruction / skills
        ↓
small deterministic generator or compiler generation step
        ↓
PROJECT_ATLAS.html
```

The Atlas must declare:

```text
GENERATED VIEW — NOT AUTHORITATIVE
```

Do not manually patch the Atlas when the source contracts are wrong. Fix the canonical source and regenerate.

For a nontrivial project, also generate/register a reproducible Atlas regeneration command/tool (for example `tools/generate_project_atlas.py` or an equivalent project-native command). The initial compiler may emit the first HTML directly, but delivery is incomplete if later agents have no defined way to regenerate it. Tiny/simple projects may omit the Atlas entirely when the project profile explicitly classifies it as unnecessary.

---

# 14. Atlas as context router, not context dump

The Atlas is a required **whole-project orientation view** for nontrivial projects. It does not replace JIT loading of exact contracts.

Required use on fresh implementation sessions, major context recovery, and fresh-agent reconstruction:

```text
START orientation
→ validate/regenerate PROJECT_ATLAS.html if stale
→ inspect PROJECT_ATLAS.html once for whole-project orientation
→ select current system/requirement
→ load exact authority/Blueprint via PROJECT_INDEX/REGISTRY
→ implement/verify
```

Do not embed complete source code, full specs, or every test log into the Atlas. Record inspection in runtime context (`inspected_view_ids`) when the harness can track it. A stale Atlas must be regenerated before it is used for orientation.

---

# 15. Atlas lifecycle / freshness gate

For nontrivial projects the Atlas has a lifecycle even though it is non-authoritative.

Registry metadata should declare:
- `normative: false`;
- `discoverability_required: true`;
- the generator artifact/command;
- the canonical source selector/IDs used to build the view;
- a generated source fingerprint/revision;
- `edit_policy: generated_only`.

A project validator should recompute Atlas freshness from the current registered sources. When any selected source changes, is added/removed, or the project revision/current acceptance state materially changes, the Atlas becomes **stale**.

At a minimum regenerate it:
1. after compilation before package delivery;
2. after material architecture/flow/decision/acceptance changes at the next milestone;
3. before a fresh/context-recovery agent uses it;
4. before handoff/final completion.

Do not hide stale state. If regeneration cannot run, mark the view stale and do not treat it as orientation evidence.

`PROJECT_INDEX.yaml` remains the routing authority. Atlas metadata/freshness evidence is derived and must never become a second project truth.

# 16. Coverage gate

Before package delivery verify:

- Has the project been decomposed into canonical reusable systems rather than only feature/task fragments?
- Does each durable responsibility have one owner?
- Are product objects composed from systems instead of rebuilding them?
- Are data/profiles/modifiers/explicit replacements separated from shared system behavior where appropriate?
- Are material merge operators and propagation semantics explicit rather than hidden behind a generic `override`?
- Can a new consumer/page/content item be added mostly by composition/data when that was part of the intent?
- Are skill/capability requirements derived from actual systems and verification needs?
- Does the start prompt contain both product vision and execution contract?
- Does the preflight question gate prevent silent material guessing without creating a "keep asking" loop?
- Has the system model been challenged by adversarial examples when extensibility matters?
- Does `PROJECT_INDEX.yaml` route every active normative authority/required Blueprint, with zero unreachable nodes in generated reachability evidence?
- Has Fresh-Agent Reconstruction passed before final task decomposition, including a deep-authority discovery challenge?
- For a nontrivial project, is `PROJECT_ATLAS.html` present, fresh, registered, routed as a required generated view, and reproducibly regenerable from canonical sources?
- On fresh/context-recovery execution, was the fresh Atlas actually inspected before JIT implementation work?

Core invariant:

```text
Preserve the whole vision.
Define the master systems.
Compose instead of duplicate.
Use skills as tools.
Show the project as a generated Atlas.
Verify the assembled product.
```

---

# 17. Skill routing boundary

For skill discovery/review/install/routing and compiler-as-skill parity, use `SKILL_NATIVE_COMPILER_GUIDE.md`. This guide only owns the system-side capability demand and composition context.

---

---

# System Map as Interview Coverage Surface

The first `SYSTEM_MAP` draft is also an interview-discovery tool. Once candidate master systems/domains are identified, cross-check them against `INTERVIEW_COVERAGE.yaml` before freezing the architecture.

A system may be structurally obvious to the compiler but still contain unresolved user-owned behavior. Do not let an inferred system boundary silently become a final product decision. Ask when the boundary changes user-visible behavior, authoring workflow, scope, or future extension; otherwise mark it delegated technical.

# Presentation primitives and parent-slot composition

For multi-surface UI, menus or editor shells, apply Core-First to presentation as well as domain logic.

Semantic ownership:

```text
Design tokens/theme
→ Primitive/component contract
→ Layout/container slot contract
→ Page/screen composition
→ local content/data
```

A parent/container owns **placement and available-space constraints** for its slots (grid/flex/region, ordering, alignment, responsive allocation). A reusable primitive owns its **internal visual/interaction contract** (typography role, padding rules, focus/disabled/hover behavior, border/frame semantics, minimum hit area, internal icon/text arrangement).

A consumer may vary a primitive only through declared tokens/variants/properties or an explicit one-off exception. Do not let a page/container reach inside and restyle the primitive ad hoc, and do not let the primitive own page placement. If a container needs a compact button, expose/use a `compact`/size variant or slot contract rather than creating a second local button style.

A Design System is not `Exercised` because `tokens.*` or `primitives.*` files exist. For material reusable presentation, prove at least two representative consumers use the same primitive/layout contract and that a shared change propagates without page-local rewrites.

For container conformance, test representative narrow/wide/overflow/content states so children actually obey the slot constraints. A box existing on screen does not prove its contents obey the box's layout contract.


# Blueprint-backed composition

When a reusable System/Capability is material enough to need an explicit Blueprint/contract, treat it as a composable building block:

```text
Consumer / Product node
→ composes declared capabilities/modules
→ calls their public contracts
→ supplies profile/data/modifiers
```

The consumer should not absorb the internal rules/state of the composed system.

This does not prescribe an engine or visual scripting language. Code modules, services, components, resources and engine-native subsystems may all realize the same Blueprint-backed boundary.


# v2.30 Project-native engine model

For products with repeatable objects/records/workflows/surfaces/providers, compile a **project-native engine model** from existing owners rather than creating a new universal Engine system.

The model should identify:

```text
reusable Definition Type contract
definition/profile source
capabilities/modules it may compose
allowed modifiers/replacements
generic runtime/surface consumer
mutable instance-state owner
authoring/registration path
```

A project can therefore expand by registering/authoring definitions and composing existing modules.

Generic pattern:

```yaml
definition_type:
  id: TYPE-...
  owner: SYS-...
  public_contract: CAP-...
  definition_schema: DATA-...
  allowed_capabilities: [CAP-...]
  allowed_modifiers: [MOD-...]
  runtime_consumer: MOD-...
  surface_consumer: MOD-...
  instance_state_owner: SYS-...
```

Use only the fields that are material. This is a semantic relationship, not a requirement to create one physical file/class per field.

## Generic consumer invariant

When a consumer can render/execute any valid definition of a reusable Definition Type, adding a new definition must not require duplicating that consumer.

Examples of generic consumers include detail surfaces, workflow runners, exporters, schedulers, renderers, evaluators and runtime hosts. The exact form is domain-specific.

Consumer Composition != Definition Ownership != Runtime State Ownership.

## Category / grouping invariant

If grouping/taxonomy is data-driven, adding an item to an existing category should normally change the item's definition/reference or category registry, not create another category implementation. Creating a new category normally creates another definition/registry entry unless the category itself introduces new reusable behavior requiring a Capability change.


# v2.31 Definition-Type authority boundary

`Product Archetype` is only a compiler discovery hypothesis about the kind of product being built.

`Reusable Definition Type` is a project architecture concept for repeatable domain instances.

Never conflate them.

Do **not** create a universal `ARCHETYPES.yaml` / `DEFINITION_TYPES.yaml` merely because v2.30/v2.31 uses this semantic model. Store Definition-Type metadata in the existing canonical domain/content/definition/Blueprint authority that already owns those definitions. Create a dedicated contract only when no existing authority can own the semantics without ambiguity and the project materially needs it.

# v2.31 Composition coherence

A composition may be structurally valid yet product-incoherent if its dependent projections disagree.

For material relationships, route to `SYSTEM_INTEGRATION`:

```text
canonical source owner
→ declared relation/derivation
→ dependent consumer/projection A
→ dependent consumer/projection B
→ Acceptance evidence
```

The composition definition may reference the invariant ID; it must not duplicate the invariant's owner/derivation semantics.
