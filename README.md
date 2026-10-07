# Agent Project Compiler (APC)

A skills-only Agent Plugin that compiles ideas, interviews, references, files, and grounded research into durable provider-neutral project authorities.

The portable package identity remains `prompt-compiler-gpt` for update compatibility with existing installs. The user-facing plugin name is **Agent Project Compiler**; the legacy `gpt` token is not a runtime model or Custom-GPT dependency.

## Architecture

The runtime has one canonical compiler kernel plus JIT procedural references:

- `plugin.json` — Agent Plugins 1.0 manifest.
- `skills/instructions/SKILL.md` — **canonical always-active APC kernel**, JIT router, context-freshness capsule, and companion-procedure routing.
- `skills/instructions/references/` — canonical detailed compiler procedures, loaded only when their material triggers apply.
- `docs/history/` — historical audits and pre-plugin provenance; never runtime authority.

There is no Custom-GPT compatibility runtime in v2.34.1. Historical Custom-GPT files are retained only under `docs/history/` so the compiler's evolution remains auditable.

The repository does **not** vendor Core-First Governance. If the companion `core-first-governance` plugin is installed, APC routes architecture/ownership/reuse and verification procedures to it JIT. Otherwise APC degrades to its packaged compiler/project authorities without pretending the external skill was loaded.

## Context model

The plugin deliberately does **not** solve context rot by loading more context.

- active context is disposable working memory;
- project/repository authorities and current evidence are durable truth;
- `PROJECT_INDEX.yaml` is routing, not a knowledge summary;
- `STATE` is a compact pointer/session record, not project canon;
- fresh session, compaction, project switch, authority revision, workstream switch, or material current-state change invalidates relevant cached context;
- recovery is `discover current state → route → JIT read → reconcile → replan`, not bulk history hydration;
- rich START/Handoff/Atlas artifacts orient a fresh agent but never replace exact authority reads.

Detailed rules live in `RUNTIME_GUIDE.md`, `BOOTSTRAP_PROMPT_AND_GOAL_GUIDE.md`, and `FRESH_AGENT_RECONSTRUCTION_GUIDE.md` and are loaded JIT.

## Canonical source rules

`skills/instructions/SKILL.md` owns all always-active compiler behavior and material-trigger routing.

`skills/instructions/references/` owns detailed conditional procedures. Each concern has one detailed owner; other files may only carry a short invariant or route to that owner.

## Verify

```bash
python tools/verify_repo.py
```

The verifier checks manifest shape/version, all 20 JIT routes, required always-active invariants, plugin-only distribution hygiene, absence of active legacy runtime paths, and repository symlink hygiene. `tools/verify_release_reproducibility.py` separately proves that the installable ZIP is byte-reproducible across repeated builds.

## Build installable plugin ZIP

```bash
python tools/build_plugin_release.py
```

Output:

```text
dist/prompt-compiler-gpt-2.34.0.zip
```

The ZIP contains exactly one top-level `prompt-compiler-gpt/` directory as required by the standalone plugin package format.

## GitHub CI

`.github/workflows/verify.yml` runs the repository verifier, proves release reproducibility, builds the plugin release, then verifies again on pushes and pull requests.

## History

Prior audits and design findings from the v2.21–v2.33 evolution are retained under `docs/history/`. They explain how the compiler evolved from a Custom GPT into a plugin-native compiler, but they are not loaded at runtime.

## License

No open-source license has been selected in this package. Add one before publishing if you want to grant reuse rights beyond GitHub's default repository access terms.
