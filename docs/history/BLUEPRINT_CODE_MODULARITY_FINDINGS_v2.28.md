# APC v2.28 — Blueprint/Code Modularity Findings

## User principle

Use the useful architectural property of Unreal-style Blueprint composition even when the implementation is ordinary code: clean, bounded systems that can be composed without duplicating or reaching through each other's internals.

## Existing APC support

v2.27 already had:
- machine-readable Project Blueprints inspired by node-based visual scripting;
- one Blueprint per bounded responsibility;
- stable calls by Blueprint ID;
- Behavior / Implementation / Data Blueprint layers;
- unique responsibility ownership;
- Blueprint Registry and implementation anchors.

## v2.28 calibration

The missing explicit invariant was Blueprint↔Code conformance.

```text
Responsibility/Capability
→ Blueprint
→ public contract
→ cohesive implementation boundary
→ internal files/classes/functions
```

Key rules:
- not one Blueprint per trivial function;
- not necessarily one Blueprint per source file/class;
- one boundary may contain multiple internal files;
- consumers call public contracts rather than internal helpers/stores;
- composition coordinates systems without absorbing their ownership;
- project validation should compare declared Blueprint boundaries with real implementation topology where practical;
- a modular-looking Blueprint graph with monolithic/bypassed runtime code is not Verified modularity.

This is provider-, language- and engine-neutral.
