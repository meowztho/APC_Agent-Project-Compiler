# Real-project compiler eval — Quint Chronicles R11

## Evidence reviewed
- generated compiler package `Quint_Chronicles_APC_Package_R11_2026-08-27.zip`;
- later real repository snapshot `quint-chronicles.zip`;
- Core-First Governance v0.11.2 handoff.

## Confirmed compiler failure classes

### 1. Placebo validator
R11 `tools/validate_project_contracts.py` used regular expressions to extract `path:` values and only checked filesystem existence. It did not parse YAML or validate structure/reference semantics. Therefore broken YAML/ownership structures could coexist with `PASS`.

Compiler correction: project-native executable gate + known-bad self-test is mandatory for nontrivial structured packages.

### 2. Declared Design Core without consumer enforcement
R11 correctly declared Design System, UI primitives, shared Card Renderer and Acceptance, yet the implementation still proliferated page-local styling. The current repository later gained `src/shell/primitives.ts`, but page sources still contain extensive local inline styling. File existence therefore proved only Declared, not Exercised reuse.

Compiler correction: Design Core admission requires two-consumer reuse proof + slot/primitive contract + whole-surface reference evidence before broad surface expansion.

### 3. User visual assets not routed strongly enough
The current repository contains `references/Home.png`, `references/Arena .png`, `references/Albung Jurnal.png`, etc. They appear in the ingest manifest but are not each registered/routed as stable visual Reference IDs in the Project Registry/Index. A later agent can legitimately miss them.

Compiler correction: every material supplied visual artifact gets stable ID, registry path, domain route and task-local inspected-reference evidence.

### 4. Canonical definition/data path had to be repaired manually
The later repository now has a versioned `CardRepository`, deep match snapshots and a shared validator. This is the architecture the compiler should have operationally admitted before dependent consumers rather than letting Builder/localStorage/fixtures drift.

Compiler correction: multi-consumer definitions require a single producer→validation→versioned store→read model→consumer path plus runtime snapshot/state separation and representative propagation tests.

### 5. Governance remembrance is not project correctness
Core-First Governance v0.11.2 correctly treats remembered Skill content as cache and requires reload after compaction/context loss. But a compiled project must remain usable when the plugin is absent or ignored.

Compiler correction: generated START/CONTINUE/AGENTS explicitly reload the bound Governance capability when available and always run the project-native gate; fallback is project authorities + gate, never fabricated plugin success.
