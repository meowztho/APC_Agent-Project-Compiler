# APC v2.32 Package Audit

## Release

- Version: `v2.32`
- Release: **Plugin-Native JIT Routing**
- Baseline: `v2.31 Composition Coherence & Survivability`
- Primary runtime surface: `Plugin/skills/instructions/skill.md`
- Legacy compatibility surface: `CUSTOM_GPT_INSTRUCTIONS.md` + 20 `Knowledge/` files

## Core-First change boundary

Requested outcome: adapt APC from a Custom-GPT-centered distribution to a plugin-native distribution that benefits from Core-First Governance-style JIT routing without creating a second governance owner.

Resolved responsibility/owner path:

```text
compiler detailed policy
→ existing 20 Knowledge authorities

compiler retrieval / Skill lifecycle
→ KNOWLEDGE_INDEX.md + SKILL_NATIVE_COMPILER_GUIDE.md

provider/plugin binding semantics
→ AGENT_RUNTIME_PORTABILITY_GUIDE.md

Prompt Compiler plugin runtime interface
→ compact procedural Skill adapter
→ generated JIT reference projection of canonical Knowledge

Core-First Governance
→ external optional procedural owner
→ loaded only on material triggers
```

Smallest semantic change: runtime/provider binding + composition of existing capabilities. No new Product/Realization owner, planner, acceptance engine, architecture authority, or 21st Knowledge policy file was introduced.

## v2.32 checks

- plugin_primary_runtime_interface: PASS
- legacy_custom_gpt_preserved: PASS
- canonical_knowledge_count_20: PASS
- no_21st_knowledge_policy_file: PASS
- plugin_reference_projection_count_20: PASS
- plugin_references_byte_identical_to_canonical_knowledge: PASS
- plugin_skill_routes_all_20_knowledge_files: PASS
- compact_jit_trigger_routing_present: PASS
- core_first_extension_architecture_material_trigger_present: PASS
- core_first_orchestration_jit_route_present: PASS
- observable_product_verification_trigger_present: PASS
- core_first_verifier_trigger_present: PASS
- independent_review_trigger_present: PASS
- no_vendored_core_first_governance_files: PASS
- companion_plugin_absence_fallback_present: PASS
- projection_builder_present_and_idempotent: PASS
- legacy_custom_gpt_size: PASS (`7998` UTF-8 bytes, limit `8000`)
- markdown_fence_balance: PASS
- manifest_paths_and_counts: PASS
- package_sha256_coverage: PASS
- git_diff_check: PASS

## Deterministic distribution gate

Run:

```text
python tools/build_plugin_projection.py
python tools/verify_distribution.py
```

The verifier checks manifest/version/counts, canonical-vs-plugin reference identity, plugin Skill reference reachability and routing coverage, companion Governance non-vendoring, Markdown fence balance, legacy 8 KB compatibility, and package checksums.

## Architecture conformance review

Primary Core-First review found no material parallel-owner or duplicated-governance defect:

- existing Knowledge owners were extended rather than replaced;
- plugin `references/` are explicitly generated projections, not canonical copies;
- Core-First Governance remains external and optional;
- architecture/ownership/reuse materiality routes the primary agent to the canonical Core-First extension procedure when actually available;
- verification/review siblings are trigger-gated rather than eagerly loaded;
- absence of the companion plugin falls back to APC's project-native authorities/gates without pretending plugin use.

A fully fresh two-phase `core-first-verifier` isolation was **not available in this host context after implementation evidence had already been observed**, so no claim of independent anti-anchored verifier PASS is made. Structural and primary conformance evidence above remains valid.

## Compatibility note

`CUSTOM_GPT_INSTRUCTIONS.md` remains unchanged from v2.31. The legacy GPT path therefore retains its previous 8 KB-compatible instruction surface, while the plugin path adds true JIT reference routing and companion-Skill routing.

## Result

**PASS — v2.32 distribution is internally coherent and ready as a portable plugin-first package.**
