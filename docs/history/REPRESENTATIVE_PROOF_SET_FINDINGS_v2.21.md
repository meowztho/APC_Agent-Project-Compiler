# APC v2.21 — Representative Proof Set Findings

## New compiler insight

Reusable architecture maturity must be proven by the **smallest semantically diverse set of cases**, not by production-consumer count.

Canonical distinction:

```text
Canonical Walking Skeleton / Reference Consumer
→ proves end-to-end integration

Heterogeneous Representative Consumers / Fixtures
→ prove reuse, composition and variation seams

Additional Similar Consumers
→ product/content breadth or scale testing
```

A walking skeleton alone can prove that the canonical path connects, but not necessarily that materially different consumers can compose the same owners/capabilities without local rule duplication. Conversely, once heterogeneous representative cases cover the promised variation axes, building more similar consumers does not strengthen architecture acceptance.

## Compiler effect

- Core-First planning may include a bounded representative architecture-proof milestone before broad content scale.
- `CAPABILITY_HIERARCHY_AND_CHANGE_GATE_GUIDE.md` owns the Representative Proof Set concept.
- Existing `verification/ABSTRACTION_TESTS.yaml` carries the proof-set cases; no new mandatory file type is introduced.
- Acceptance distinguishes integration proof, reuse/composition proof and product breadth.
- Fresh-Agent Reconstruction tests whether an agent can choose the smallest semantically sufficient proof set.
- Execution stops adding similar consumers for architecture proof once the representative set passes.
- A second case does not need to become speculative shipping content; adversarial fixtures/challenges remain valid when production content is not already required.

## Core invariant

> REUSE PROOF SCALES WITH SEMANTIC DIVERSITY, NOT CONSUMER COUNT.
