# APC v2.22 — Product Capability Envelope Findings

## Real failure addressed
A compiler can preserve every user statement and still under-model the requested product if it only decomposes concepts the user explicitly names. The later implementation agent then receives less domain context than the compiler had and may invent missing responsibilities ad hoc.

## New compiler law

```text
USER VISION / REFERENCES
→ provisional PRODUCT ARCHETYPE (COMPILER inference)
→ EXPECTED CAPABILITY / RESPONSIBILITY ENVELOPE
→ domain-expert omission / coverage sweep
→ user-owned decisions + research/delegation/dispositions
→ Responsibility Owners / SYSTEM_MAP
→ CAPABILITY_GRAPH / composition
→ Representative Proof Set
→ dependency/admission-aware implementation plan
```

The envelope is not a mandatory architecture taxonomy and is never silently promoted to USER intent. Every material expected responsibility must be considered and explicitly modeled, covered elsewhere, marked not applicable/deferred, delegated, or routed to a real user decision.

## Hard coverage question
> Could a competent domain expert look at the generated System Map and immediately identify an important ordinary responsibility implied by the requested product that the compiler never considered?

If yes, compilation is not complete.

## Boundaries retained
- Responsibility/Owner discovery precedes Capability Contract and Representative Reuse Proof.
- Owner/capability existence does not require multiple consumers.
- Representative Proof validates reusable seams, not ownership existence.
- PROJECT_ATLAS.html is a compiler-generated non-authoritative package view; optional agent Working Views are disposable runtime cache.
- No new mandatory Knowledge file or generated-project file type is introduced.
