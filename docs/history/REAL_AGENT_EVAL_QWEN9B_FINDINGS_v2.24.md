# APC v2.24 — Real-Agent Eval Findings

## Trigger

A local Qwen 9B implementation run was stopped before completion. The run nevertheless exposed useful long-session behavior:
- the model broadly understood Core-First;
- existing rules were still violated over time;
- parallel/shadow implementations and divergent progress claims appeared;
- canonical data authorities existed but were not always consumed by runtime;
- agents often interpret the initial foundation/walking skeleton as the practical end of the assignment;
- visual/user-surface intent can remain documented yet lose influence over execution, producing generic/default-looking results.

Because the run was incomplete, unfinished polish and temporary scratch artifacts are not treated as final-project failures by themselves.

## Diagnosis classes

Before changing the compiler for a real-agent failure:

`SEMANTIC_GAP`
`ADHERENCE_OR_EXECUTION_DRIFT`
`INCOMPLETE_RUN_ARTIFACT`
`VALIDATION_GAP`

Do not duplicate an invariant merely because a weaker model violated it.

## v2.24 corrections

1. Foundation/walking skeleton is explicitly an early proof, never product completion.
2. START/GOAL/CONTINUE expose the full remaining product-realization roadmap, not only the first target.
3. Design-heavy products carry a compact visual/user-surface target in active orientation context.
4. Design/surface fidelity is exercised early on a representative normal-user surface before broad scale-out.
5. STATE is the sole current execution/admission pointer; Plan owns transition rules; Acceptance/Evidence owns verification truth; prompts/Handoff/Atlas are derived.
6. Project-native gates may validate runtime progress: admission, build/typecheck, required evidence, state consistency and project-specific canonical data-path probes.
7. Interrupted-run scratch artifacts are not automatically architecture defects; they become defects when promoted into active architecture or left conflicting at clean milestone/handoff boundaries.
8. Prefer executable project-specific convergence checks over additional portable Governance prose.
