# PACKAGE_AUDIT_v2.33

Date: 2026-09-30

## Scope

Migration of the Prompt Compiler from a dual-source Custom GPT / Plugin model to a single canonical plugin kernel with deterministic Custom GPT compatibility projection.

## Canonical ownership after migration

- Always-active compiler behavior: `skills/instructions/SKILL.md`
- Conditional compiler procedures: `skills/instructions/references/*.md`
- Custom GPT Instructions: generated projection at `legacy/CUSTOM_GPT_INSTRUCTIONS.md`
- Historical pre-migration Instructions: `docs/history/CUSTOM_GPT_INSTRUCTIONS_v2.31_ORIGINAL.md`

## Material findings resolved

1. The former Custom GPT Instructions contained several invariants not guaranteed to be loaded before JIT routing in v2.32.
2. Those invariants were moved into the plugin always-active kernel where required to decide routing, authority, evidence, admission, or delegation boundaries.
3. The legacy Instructions file is no longer independently editable and is generated from selected `SKILL.md` sections.
4. The Custom GPT 8000-byte Instructions constraint is executable verification, not documentation-only guidance.
5. The plugin-specific JIT table remains plugin-only; the legacy projection relies on uploaded Knowledge plus its compact routing kernel.
6. Core-First Governance remains a separate optional procedural owner and is not vendored into APC.

## Restored always-active invariants

- interview language / authority language / verbatim provenance;
- explicit `adopt | adapt | reject | inspiration-only` reference semantics;
- compiler vs build-agent authority boundary;
- `APP_FLOW` scope boundary;
- exact admission gate semantics and `TECHNICALLY EXECUTABLE != ADMITTED FOR PRODUCT CONCLUSIONS`;
- `PROJECT_INDEX.yaml` as canonical discoverability and source-load gate;
- design as Product Realization;
- maturity ladder `Specified → Declared → Connected → Exercised → Verified`;
- Product Complete vs Release Ready distinction;
- runtime/user-surface claims require exercised evidence;
- project-native executable gate and context-loss rerun semantics;
- compact Core-First availability/fallback routing.

## Verification

Repository verification checks:

- Agent Plugins 1.0 manifest parses and version is `2.33.0`;
- OpenAI `shortDescription` remains within 30 characters;
- all 20 canonical JIT references exist and are routed from `SKILL.md`;
- 11 required always-active semantic markers are present;
- legacy Instructions are exactly regenerated from `SKILL.md` selected sections;
- legacy Instructions remain within the former 8000-byte Custom GPT limit;
- legacy Instructions contain no plugin-only `references/` paths;
- migration and historical provenance files exist;
- distributable source contains no symlinks.

Observed result during package preparation:

```text
PASS
manifest: prompt-compiler-gpt 2.33.0
shortDescription: 29/30 chars
canonical references: 20/20
skill routing: complete
legacy projection: 7995/8000 bytes, generated from SKILL.md
always-active invariant checks: 11/11
```

## Remaining limitation

No genuinely fresh external verifier context was available during this packaging session. The package therefore records deterministic repository/build verification, but does not claim an independent anti-anchored architecture-verifier pass.
