# PACKAGE_AUDIT_v2.34.1

Date: 2026-09-30
Scope: plugin-native cleanup review after Custom GPT retirement
Status: PASS after narrow remediation

## Findings

The v2.34.0 runtime architecture was already plugin-native and no longer depended on the former Custom-GPT Instructions/Knowledge delivery model or its 8,000-byte limit. Historical Custom-GPT artifacts were isolated under `docs/history/` and excluded from the installable release.

Three non-architectural cleanup items remained:

1. user-facing presentation still said `Prompt Compiler GPT`;
2. active references still used `Knowledge` terminology and `KNOWLEDGE_INDEX.md`, which could be confused with the retired Custom-GPT Knowledge surface;
3. the installable ZIP included the source-repository `README.md`, whose verification/build commands reference tools intentionally excluded from the installable plugin.

## Remediation

- portable package identity remains `prompt-compiler-gpt` to preserve update compatibility;
- OpenAI display name is now `Agent Project Compiler`;
- JIT router renamed to `REFERENCE_INDEX.md`; active Skill/reference prose uses plugin-native reference terminology;
- installable ZIP contains only `plugin.json` and `skills/`; GitHub/source-only support files stay outside the installable package.

## Architecture decision

No new planner, context manager, router, policy corpus, MCP server, or runtime dependency was added. The existing canonical owners remain unchanged: `SKILL.md` owns the always-active compiler kernel and material-trigger routing, reference files own JIT procedures, generated project authorities own project truth, and optional Core-First governance remains a separate procedural dependency when available.

## Verification

Run the repository verifier, reproducibility check, deterministic build, ZIP integrity check, package-shape inspection, and active legacy-terminology scan before release.
