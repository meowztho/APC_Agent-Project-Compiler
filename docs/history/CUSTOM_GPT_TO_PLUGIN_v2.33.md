# Custom GPT → Plugin Kernel Migration v2.33

## Purpose

This migration removes the remaining split-brain between the former Custom GPT `Instructions` field and the plugin-native skill runtime.

Canonical runtime ownership after v2.33:

```text
skills/instructions/SKILL.md
  ├─ always-active APC kernel
  ├─ compact JIT routing capsule
  ├─ companion Core-First routing
  └─ detailed procedures → skills/instructions/references/*.md

legacy/CUSTOM_GPT_INSTRUCTIONS.md
  └─ generated compatibility projection from selected SKILL.md sections
```

`legacy/CUSTOM_GPT_INSTRUCTIONS.md` is no longer an independently edited authority.
The exact pre-migration v2.31 text is retained at
`docs/history/CUSTOM_GPT_INSTRUCTIONS_v2.31_ORIGINAL.md` for provenance.

## Rule-by-rule migration

| Former Custom GPT responsibility | v2.33 owner | Classification |
| --- | --- | --- |
| APC role; durable provider-neutral compilation | `SKILL.md` Always-active kernel | ALWAYS ACTIVE |
| Interview in user language; authorities normally English; verbatim provenance | `SKILL.md` Always-active kernel | ALWAYS ACTIVE |
| Product / Realization / Verification Truth separation | `SKILL.md` Always-active kernel | ALWAYS ACTIVE |
| Stable Round/Q identity and exact Q/A materialization | `SKILL.md` Always-active kernel + `INTERVIEW_COMPLETENESS_AND_HANDOFF_GUIDE.md` | KERNEL + JIT DETAIL |
| `adopt | adapt | reject | inspiration-only` reference semantics | `SKILL.md` Always-active kernel + vision/runtime templates | KERNEL + JIT DETAIL |
| Research material unknowns before asking; thematic interview closure | `SKILL.md` Compilation sequence + compiler/interview guides | KERNEL + JIT DETAIL |
| Canonical owner / capability / provider / composition semantics | `SKILL.md` Always-active kernel + Core-First routing + capability/system guides | KERNEL + JIT DETAIL |
| Product archetype / capability envelope and responsibility coverage | `SKILL.md` Compilation sequence + system/compiler guides | KERNEL + JIT DETAIL |
| Build order, production-shaped skeleton, admission semantics | `SKILL.md` kernel + compilation sequence + compiler/execution guides | KERNEL + JIT DETAIL |
| `APP_FLOW` owns transitions, not whole product scope | `SKILL.md` Always-active kernel + runtime/compiler guides | ALWAYS ACTIVE + JIT DETAIL |
| Exact gate boundary; reversible preparation allowed | `SKILL.md` Always-active kernel + compiler/execution guides | ALWAYS ACTIVE + JIT DETAIL |
| `TECHNICALLY EXECUTABLE != ADMITTED FOR PRODUCT CONCLUSIONS` | `SKILL.md` Always-active kernel | ALWAYS ACTIVE |
| Compiler vs build-agent authority boundary | `SKILL.md` Always-active kernel | ALWAYS ACTIVE |
| `DELEGATED_TECHNICAL_DECISION` | `SKILL.md` kernel/sequence + compiler guides | ALWAYS ACTIVE + JIT DETAIL |
| No second planner / acceptance engine | `SKILL.md` Always-active kernel | ALWAYS ACTIVE |
| `PROJECT_INDEX.yaml` canonical routing and source-load gate | `SKILL.md` Always-active kernel + runtime/bootstrap guides | ALWAYS ACTIVE + JIT DETAIL |
| Design is Product Realization, not late polish | `SKILL.md` Always-active kernel + vision/user-surface guides | ALWAYS ACTIVE + JIT DETAIL |
| START / CONTINUE / GOAL semantics | `SKILL.md` Output/bootstrap invariants + bootstrap/runtime guides | KERNEL + JIT DETAIL |
| `PROJECT_ATLAS.html` generated, non-authoritative | `SKILL.md` Output/bootstrap invariants + system/runtime guides | KERNEL + JIT DETAIL |
| Skills are procedures, never truth; provider memory noncanonical | `SKILL.md` Always-active kernel | ALWAYS ACTIVE |
| `Specified → Declared → Connected → Exercised → Verified` | `SKILL.md` Always-active kernel + integration/delivery guides | ALWAYS ACTIVE + JIT DETAIL |
| Product Complete / Release Ready distinction | `SKILL.md` Always-active kernel + delivery guide | ALWAYS ACTIVE + JIT DETAIL |
| Runtime/user-surface claims require exercised evidence | `SKILL.md` Always-active kernel + user-surface guide | ALWAYS ACTIVE + JIT DETAIL |
| Fresh-Agent Reconstruction | `SKILL.md` Compilation sequence + reconstruction guide | KERNEL + JIT DETAIL |
| Project-native executable gate and known-bad mutants | `SKILL.md` Always-active kernel + delivery/runtime templates | ALWAYS ACTIVE + JIT DETAIL |
| Core-First companion use | compact fallback rule in kernel + `Companion Core-First governance` section | PLUGIN-NATIVE ROUTING |
| Plugin reference paths / explicit JIT table | `SKILL.md` Plugin-native JIT routing | PLUGIN ONLY |
| Custom GPT Knowledge delivery mechanics | `tools/build_legacy_gpt.py` projection/build | LEGACY ONLY |

## Why some rules remain in the kernel

A rule stays always active when it determines one of these before any JIT read can safely occur:

- truth/authority precedence;
- what must never be delegated or weakened;
- how to recognize a material routing trigger;
- when evidence is insufficient for a claim;
- which artifact owns routing/admission/completion;
- whether the next transition is authorized.

Detailed procedures, templates, checklists, and domain-specific mechanics remain in `references/` and are loaded only when triggered.

## Legacy Custom GPT projection

`tools/build_legacy_gpt.py` derives the Custom GPT Instructions text from these `SKILL.md` sections:

1. `Always-active kernel`
2. `Compilation sequence`
3. `Output and bootstrap invariants`

The generated text is capped at 8000 UTF-8 bytes to remain compatible with the former Custom GPT Instructions field. v2.33 currently renders to 7995 bytes.

The old independently maintained Instructions file must not be edited. `tools/verify_repo.py` fails when the generated projection drifts from `SKILL.md`.

## Core-First boundary

APC does not vendor or duplicate Core-First Governance. The APC kernel knows only the material routing boundary required to decide when the companion procedure must be loaded. The companion plugin remains the canonical procedural owner when installed.

If it is unavailable, APC degrades to its packaged capability/ownership/runtime guides and project-native gates without claiming that Core-First was loaded.
