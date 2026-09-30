# APC v2.31 — Composition Coherence & Survivability Findings

## Why v2.31 exists

Cross-version review of v2.20–v2.30 found no major lost predecessor capability, but one material gap remained:

The compiler modeled systems, owners, flows and reusable definitions well, yet did not explicitly model enough **relationships that must stay coherent across multiple systems/projections**.

That gap explains a common repair spiral:

```text
visible symptom
→ patch nearest consumer
→ another dependent projection drifts
→ patch again
→ product coherence degrades
```

## v2.31 corrections

### 1. Composition Coherence Invariants

Material cross-system relationships now belong in existing `SYSTEM_INTEGRATION`.

An invariant records:
- canonical source/owner;
- source IDs/contracts/state;
- dependent consumers/projections;
- update/derivation semantics;
- forbidden local overrides;
- Acceptance/evidence.

The invariant owns no state.

### 2. Repair-by-Invariant

Implementation runtime follows:

```text
reproduce symptom
→ failed Acceptance/invariant
→ canonical source/owner
→ affected projections
→ canonical repair
→ rerun invariant evidence
→ rerun affected representative product path/review
```

Local fixes remain valid for genuinely local defects.

### 3. Reusable Definition Type terminology

`Product Archetype` remains a compiler discovery hypothesis.
`Reusable Definition Type` is the project architecture concept for repeatable domain instances.

No universal `ARCHETYPES.yaml` / `DEFINITION_TYPES.yaml` is introduced. Definition-Type metadata belongs to the existing canonical domain/content/definition/Blueprint authority.

### 4. Skeleton Survivability Admission

A runnable skeleton can be exploratory.
Production admission now requires declared survivability Acceptance evidence proving representative substitution/extension preserves the canonical owner/runtime path.

`STATE` cannot self-promote the skeleton.

## New negative controls

- `MUTANT-COMPOSITION-DRIFT`
- `MUTANT-LOCAL-SYMPTOM-PATCH`
- `MUTANT-PREMATURE-SKELETON-ADMISSION`

These complement the existing v2.20–v2.30 controls without creating another status or invariant authority family.
