from __future__ import annotations

import tempfile
from pathlib import Path

from build_plugin_release import ROOT, build_release


def main() -> None:
    with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
        zip_a, sha_a = build_release(ROOT, Path(a))
        zip_b, sha_b = build_release(ROOT, Path(b))
        if sha_a != sha_b or zip_a.read_bytes() != zip_b.read_bytes():
            raise SystemExit(f"FAIL: non-reproducible release: {sha_a} != {sha_b}")
        print("PASS")
        print(f"reproducible release sha256: {sha_a}")


if __name__ == "__main__":
    main()
