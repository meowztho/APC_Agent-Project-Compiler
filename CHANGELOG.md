# Changelog

## 2.34.1 — Plugin-native terminology and release hygiene

- Kept the stable portable package identity `prompt-compiler-gpt` for update compatibility while changing the user-facing display name to `Agent Project Compiler`.
- Renamed the active JIT router from `KNOWLEDGE_INDEX.md` to `REFERENCE_INDEX.md` and removed remaining Custom-GPT-era `Knowledge` terminology from active Skill/reference text.
- Reduced the installable ZIP to actual plugin runtime files (`plugin.json` + `skills/`); source-repository README, history, CI, and build tooling remain in the GitHub source package only.
- Preserved the v2.34 compiler architecture, Core-First companion boundary, context-freshness rules, and deterministic release build.

## 2.34.0 — Plugin-first context-freshness model

- Removed the active Custom-GPT compatibility runtime, its 8000-byte constraint, legacy build script, and CI path. Historical files remain provenance only.
- Strengthened the always-active kernel with the learned context-rot invariants: active context is disposable, workspace awareness is not hydration, current truth beats cache, and recovery uses discover → route → JIT read → reconcile → replan.
- Kept `PROJECT_INDEX.yaml` as the single retrieval router and `STATE` as a compact pointer/session record rather than project canon.
- Explicitly separated rich START/Handoff/Atlas orientation from canonical authority reads.
- Aligned plugin routing/freshness behavior with Core-First orchestration while keeping Core-First as a separate optional procedural owner.
- Updated verification and GitHub CI for a plugin-only distribution.

## 2.33.0 — Single-source kernel migration

- Migrated the former Custom GPT Instructions semantics into the canonical plugin `SKILL.md` kernel.
- Restored always-active invariants that must be known before JIT routing: language/provenance, reference-trait semantics, compiler/build-agent boundary, `PROJECT_INDEX.yaml` source-load routing, design-as-realization, maturity/completion semantics, observable-evidence boundary, admission rule, and executable project gate.
- Made `legacy/CUSTOM_GPT_INSTRUCTIONS.md` a deterministic projection from selected `SKILL.md` sections instead of a second independently maintained instruction source.
- Archived the exact pre-migration v2.31 Instructions text for provenance.
- Added an explicit Custom GPT → Plugin rule migration map.
- Added verification that the legacy projection stays under 8000 UTF-8 bytes and cannot drift from the plugin kernel.

## 2.32.0 — Plugin-native JIT routing

- Converted the former Custom GPT knowledge distribution into an Agent Plugins 1.0 skills-only package.
- Made `skills/instructions/SKILL.md` the compact always-loaded APC kernel.
- Moved detailed compiler procedures behind material-trigger JIT routing in `skills/instructions/references/`.
- Kept Core-First Governance as a separate optional procedural owner rather than vendoring or duplicating it.
- Added deterministic legacy Custom GPT packaging from the canonical plugin references.
- Added repository verification and GitHub CI.
