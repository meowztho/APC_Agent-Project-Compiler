from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "plugin.json"
SKILL = ROOT / "skills" / "instructions" / "SKILL.md"
REFS = ROOT / "skills" / "instructions" / "references"

EXPECTED_REFS = {
    "AGENT_RUNTIME_PORTABILITY_GUIDE.md",
    "BLUEPRINT_GUIDE.md",
    "BLUEPRINT_REPOSITORY_GUIDE.md",
    "BLUEPRINT_TEMPLATES.md",
    "BOOTSTRAP_PROMPT_AND_GOAL_GUIDE.md",
    "CAPABILITY_HIERARCHY_AND_CHANGE_GATE_GUIDE.md",
    "COMPILER_GUIDE.md",
    "DELIVERY_AND_VERIFICATION_GUIDE.md",
    "EXECUTION_RUNTIME_GUIDE.md",
    "FRESH_AGENT_RECONSTRUCTION_GUIDE.md",
    "HIERARCHICAL_INSTRUCTIONS_GUIDE.md",
    "INTERVIEW_COMPLETENESS_AND_HANDOFF_GUIDE.md",
    "REFERENCE_INDEX.md",
    "RUNTIME_GUIDE.md",
    "RUNTIME_TEMPLATES.md",
    "SKILL_NATIVE_COMPILER_GUIDE.md",
    "SYSTEM_COMPOSITION_AND_ATLAS_GUIDE.md",
    "SYSTEM_INTEGRATION_AND_RUNTIME_TRACE_GUIDE.md",
    "USER_SURFACE_VERIFICATION_GUIDE.md",
    "VISION_AND_REFERENCE_PRESERVATION_GUIDE.md",
}

REQUIRED_KERNEL_PHRASES = (
    "Interview in the user's language",
    "Preserve verbatim provenance unchanged",
    "adopt | adapt | reject | inspiration-only",
    "may not redesign Product Truth",
    "STATE` is only the current execution/admission pointer",
    "PROJECT_INDEX.yaml",
    "Workspace awareness != workspace hydration",
    "discovering current state first",
    "Design is Product Realization, not late polish",
    "Specified → Declared → Connected → Exercised → Verified",
    "Runtime/user-surface claims remain unverified until exercised",
    "TECHNICALLY EXECUTABLE != ADMITTED FOR PRODUCT CONCLUSIONS",
    "project-native executable gate",
    "If Core-First is available",
    "Rich bootstrap/handoff artifacts are orientation, not authority",
)

ACTIVE_RUNTIME_FILES = [
    ROOT / "README.md",
    ROOT / "plugin.json",
    ROOT / "skills",
    ROOT / ".github",
]

errors: list[str] = []


def require(cond: bool, msg: str) -> None:
    if not cond:
        errors.append(msg)


try:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"FAIL: cannot parse plugin.json: {exc}")
    raise SystemExit(1)

require(manifest.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", "wrong/missing Agent Plugins 1.0 schema")
require(manifest.get("name") == "prompt-compiler-gpt", "manifest name must be prompt-compiler-gpt")
version = str(manifest.get("version", ""))
require(bool(re.fullmatch(r"\d+\.\d+\.\d+", version)), "version must be strict semver x.y.z")
require(version == "2.34.1", f"expected repository version 2.34.1, got {version}")

iface = (((manifest.get("extensions") or {}).get("com.openai") or {}).get("interface") or {})
short = iface.get("shortDescription", "")
require(isinstance(short, str) and 1 <= len(short) <= 30, f"shortDescription must be 1..30 chars, got {len(short) if isinstance(short, str) else 'non-string'}")
default_prompt = iface.get("defaultPrompt")
require(isinstance(default_prompt, (str, list)), "defaultPrompt must be a string or array")
if isinstance(default_prompt, list):
    require(1 <= len(default_prompt) <= 3 and all(isinstance(x, str) and x.strip() for x in default_prompt), "defaultPrompt array must contain 1..3 non-empty strings")

require(SKILL.is_file(), "skills/instructions/SKILL.md missing")
skill_text = SKILL.read_text(encoding="utf-8") if SKILL.is_file() else ""
if skill_text:
    require(skill_text.startswith("---\n"), "SKILL.md YAML frontmatter missing")
    require(re.search(r"(?m)^name:\s*instructions\s*$", skill_text) is not None, "SKILL.md name must match skills/instructions folder")
    require(re.search(r"(?m)^description:\s*\S", skill_text) is not None, "SKILL.md description missing")
    routed = set(re.findall(r"references/([A-Z0-9_]+\.md)", skill_text))
    missing_routes = sorted(EXPECTED_REFS - routed)
    require(not missing_routes, f"SKILL.md does not route all canonical references: {missing_routes}")
    for phrase in REQUIRED_KERNEL_PHRASES:
        require(phrase in skill_text, f"always-active kernel invariant missing: {phrase}")

actual_refs = {p.name for p in REFS.glob("*.md")}
require(actual_refs == EXPECTED_REFS, f"reference set mismatch; missing={sorted(EXPECTED_REFS-actual_refs)} extra={sorted(actual_refs-EXPECTED_REFS)}")

# Active runtime must be plugin-only. Historical provenance under docs/history is allowed to mention the old Custom-GPT path.
for root in ACTIVE_RUNTIME_FILES:
    files = [root] if root.is_file() else list(root.rglob("*"))
    for p in files:
        if not p.is_file() or p.suffix == ".pyc":
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        lowered = text.lower()
        require("build_legacy_gpt" not in lowered, f"active legacy build path remains in {p.relative_to(ROOT)}")
        require("legacy/custom_gpt_instructions" not in lowered, f"active legacy runtime path remains in {p.relative_to(ROOT)}")
        if p.is_relative_to(ROOT / "skills"):
            require("legacy custom gpt" not in lowered, f"active reference still treats legacy Custom GPT as runtime in {p.relative_to(ROOT)}")

require(not (ROOT / "legacy").exists(), "legacy runtime directory must not exist in v2.34")
require(not (ROOT / "tools" / "build_legacy_gpt.py").exists(), "legacy build script must not exist in v2.34")
require((ROOT / "docs" / "history" / "CUSTOM_GPT_INSTRUCTIONS_v2.31_ORIGINAL.md").is_file(), "historical v2.31 Instructions provenance missing")
require((ROOT / "docs" / "history" / "CUSTOM_GPT_TO_PLUGIN_v2.33.md").is_file(), "historical v2.33 migration record missing")

# Context-rot lessons must live in their canonical detailed owner, not only in the kernel.
runtime_text = (REFS / "RUNTIME_GUIDE.md").read_text(encoding="utf-8")
for phrase in (
    "Workspace awareness != workspace hydration",
    "Do not fight context rot by preloading the whole workspace",
    "replan before material execution if the next best action changed",
    "PROJECT_INDEX.yaml` is the single canonical retrieval router",
):
    require(phrase in runtime_text, f"RUNTIME_GUIDE missing context-freshness rule: {phrase}")

for p in ROOT.rglob("*"):
    if ".git" in p.parts or "dist" in p.parts:
        continue
    if p.is_symlink():
        errors.append(f"symlink not allowed in distributable source: {p.relative_to(ROOT)}")

if errors:
    print("FAIL")
    for e in errors:
        print(f" - {e}")
    raise SystemExit(1)

print("PASS")
print(f"manifest: {manifest['name']} {version}")
print(f"shortDescription: {len(short)}/30 chars")
print(f"canonical references: {len(actual_refs)}/{len(EXPECTED_REFS)}")
print("skill routing: complete")
print(f"always-active invariant checks: {len(REQUIRED_KERNEL_PHRASES)}/{len(REQUIRED_KERNEL_PHRASES)}")
print("distribution: plugin-only; legacy runtime removed")
print("context freshness: kernel + RUNTIME_GUIDE checks present")
