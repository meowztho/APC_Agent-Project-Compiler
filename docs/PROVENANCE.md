# Provenance

This repository evolved from the APC Prompt Compiler Custom-GPT package into a plugin-native Agent Plugins 1.0 package.

Milestones retained in `docs/history/`:

- v2.31 and earlier: Custom-GPT Instructions + uploaded Knowledge distribution;
- v2.32: plugin-native JIT reference routing introduced;
- v2.33: always-active semantics consolidated into one canonical plugin `SKILL.md` kernel while legacy compatibility was still generated;
- v2.34: legacy runtime compatibility removed; the distribution is plugin-first only, with context freshness/recovery and JIT routing aligned to the later Core-First orchestration lessons.

Current runtime ownership is intentionally small:

- root `plugin.json` — package identity/presentation;
- `skills/instructions/SKILL.md` — always-active compiler kernel and routing capsule;
- `skills/instructions/references/` — conditional detailed procedures.

The exact original v2.31 `CUSTOM_GPT_INSTRUCTIONS.md` and prior migration/audit documents remain under `docs/history/` solely as provenance. They are not current runtime authority and are not packaged into the installable plugin ZIP.
