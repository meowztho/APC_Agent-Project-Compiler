from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)
FILE_MODE = 0o100644


def release_files(root: Path) -> list[Path]:
    files = [root / "plugin.json"]
    files.extend(p for p in (root / "skills").rglob("*") if p.is_file())
    return sorted(files, key=lambda p: p.relative_to(root).as_posix())


def build_release(root: Path = ROOT, dist: Path | None = None) -> tuple[Path, str]:
    manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
    name = manifest["name"]
    version = manifest["version"]
    dist = dist or (root / "dist")
    dist.mkdir(parents=True, exist_ok=True)
    zip_path = dist / f"{name}-{version}.zip"

    if zip_path.exists():
        zip_path.unlink()

    # ZIP_STORED + normalized metadata makes the package reproducible across
    # checkouts/extractions instead of inheriting filesystem mtimes or modes.
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_STORED) as zf:
        for src in release_files(root):
            rel = src.relative_to(root).as_posix()
            arcname = f"{name}/{rel}"
            info = zipfile.ZipInfo(arcname, date_time=FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_STORED
            info.create_system = 3
            info.external_attr = FILE_MODE << 16
            info.flag_bits |= 0x800  # UTF-8 names
            zf.writestr(info, src.read_bytes())

    sha = hashlib.sha256(zip_path.read_bytes()).hexdigest()
    (dist / f"{zip_path.name}.sha256").write_text(f"{sha}  {zip_path.name}\n", encoding="utf-8")
    return zip_path, sha


if __name__ == "__main__":
    path, sha = build_release()
    print(path)
    print(sha)
