# PACKAGE_AUDIT_v2.34

Date: 2026-09-30
Scope: plugin-first Prompt Compiler distribution
Status: PASS with independence limitation noted below

## Intent

v2.34 removes the active Custom-GPT compatibility runtime and keeps only the Agent Plugins 1.0 Skill distribution. The architecture change is deliberately narrow: preserve the existing APC Product/Realization/Verification model, strengthen context-freshness/recovery routing using the lessons learned in Core-First orchestration, and avoid introducing a second context manager, planner, index, or policy owner.

## Canonical runtime ownership

- `plugin.json` — package identity and UI metadata only.
- `skills/instructions/SKILL.md` — always-active APC kernel and material-trigger router.
- `skills/instructions/references/KNOWLEDGE_INDEX.md` — detailed compiler-reference retrieval router when the kernel capsule is insufficient.
- `skills/instructions/references/RUNTIME_GUIDE.md` — detailed context/source-load/recovery contract.
- `skills/instructions/references/FRESH_AGENT_RECONSTRUCTION_GUIDE.md` — package reconstruction fidelity and fresh-agent acceptance.
- `PROJECT_INDEX.yaml` in generated projects remains the single project-authority retrieval router; `STATE` remains pointer/session state, not project canon.

Historical Custom-GPT artifacts remain under `docs/history/` only and are excluded from the installable plugin ZIP.

## Context-rot lessons incorporated

1. Active model context is disposable working memory; current project authorities and current runtime/external evidence outrank chat memory, summaries, old plans, and stale source-load markers.
2. `WORKSPACE AWARENESS != WORKSPACE HYDRATION`: discovering that a source exists does not establish that its current content was consumed.
3. Recovery after fresh session/compaction/project switch/authority revision/workstream switch/material state change is:

   `discover current state → PROJECT_INDEX route → JIT read required authorities → reconcile state/evidence → replan if needed`.

4. Recovery must not bulk-load the whole workspace merely to regain confidence.
5. Rich START/CONTINUE/Handoff/Atlas artifacts provide initial mental-model hydration, but remain generated/non-authoritative orientation. Exact dependent work rereads canonical authorities.
6. `STATE` may hold compact current pointers and session source-load evidence, but it cannot become a parallel knowledge store or completion authority.
7. Fresh-Agent Reconstruction continues to prove both whole-product understanding and precise deep-authority discovery.

## Distribution changes

Removed from active source/runtime:

- `legacy/CUSTOM_GPT_INSTRUCTIONS.md`
- `tools/build_legacy_gpt.py`
- Custom-GPT release build in CI
- 8000-byte Instructions verification
- runtime parity requirements between two deployment surfaces

Retained only as historical provenance:

- original v2.31 `CUSTOM_GPT_INSTRUCTIONS.md`
- v2.33 migration record and earlier audits/findings

## Verification

Repository verifier checks:

- Agent Plugins 1.0 manifest identity/version/presentation constraints;
- all 20 canonical JIT references exist and are routed by `SKILL.md`;
- 15 always-active kernel invariants are present;
- plugin-only active distribution contains no legacy runtime path;
- detailed context-freshness rules exist in `RUNTIME_GUIDE.md` rather than only in the kernel;
- historical migration/provenance artifacts remain available;
- distributable source contains no symlinks.

Build verification additionally checks the installable ZIP structure and archive integrity.

## Architecture review status

The primary change followed the current Core-First routing/extension-architecture rules: reuse existing owners, strengthen `SKILL.md` + `RUNTIME_GUIDE.md`, and remove the obsolete compatibility path rather than adding a new context subsystem.

A genuinely separate fresh read-only `core-first-verifier` context was not available in this execution environment. Therefore this audit does **not** claim independent verifier isolation. Verification consists of baseline Git diff inspection, executable repository gates, release-archive checks, and direct owner/routing review.

## Final release evidence

Executed on 2026-09-30:

- `python -m py_compile tools/verify_repo.py tools/build_plugin_release.py` — PASS
- `python tools/verify_repo.py` — PASS
- `python tools/verify_release_reproducibility.py` — PASS (two byte-identical builds)
- `python tools/build_plugin_release.py` — PASS
- ZIP integrity (`ZipFile.testzip`) — PASS
- installable ZIP file count — 23
- JIT reference count in installable ZIP — 20/20
- legacy runtime entries in installable ZIP — 0
- packaged manifest version — `2.34.0`
- plugin ZIP SHA-256 — `cc5da22923b8d17e2ec430c4ad57fe4aa202f71740047efdea6ff7c978588876`
