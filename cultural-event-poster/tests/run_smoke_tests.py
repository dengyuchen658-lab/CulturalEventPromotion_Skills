#!/usr/bin/env python3
"""Run dependency-light smoke tests for the skill's deterministic scripts."""

from __future__ import annotations

import json
import struct
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run(*arguments: str, expected: int = 0) -> None:
    result = subprocess.run([PYTHON, *arguments], cwd=ROOT, text=True, capture_output=True)
    if result.returncode != expected:
        raise AssertionError(
            f"command returned {result.returncode}, expected {expected}: {' '.join(arguments)}\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )


def write_png_header(path: Path, width: int, height: int) -> None:
    """Write the PNG signature and IHDR fields needed by the header validator."""
    path.write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00\x00\x00\rIHDR" + struct.pack(">II", width, height))


def main() -> int:
    validate_brief = str(ROOT / "scripts" / "validate_brief.py")
    fixtures = ROOT / "tests" / "fixtures"
    run(validate_brief, str(fixtures / "valid-bilingual-lecture.json"))
    run(validate_brief, str(fixtures / "valid-mixed-event.json"))
    run(validate_brief, str(fixtures / "invalid-missing-critical-fields.json"), expected=1)

    with tempfile.TemporaryDirectory() as temp_dir:
        output_root = Path(temp_dir)
        for language in ("zh-CN", "en"):
            write_png_header(output_root / f"lecture-test_{language}_4x5_final_v01.png", 2400, 3000)
        manifest = {
            "schema_version": "1.0",
            "project_id": "lecture-test",
            "files": [
                {"path": "lecture-test_zh-CN_4x5_final_v01.png", "language": "zh-CN", "format": "png", "width_px": 2400, "height_px": 3000, "status": "final"},
                {"path": "lecture-test_en_4x5_final_v01.png", "language": "en", "format": "png", "width_px": 2400, "height_px": 3000, "status": "final"},
            ],
        }
        manifest_path = output_root / "delivery.json"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        run(
            str(ROOT / "scripts" / "validate_delivery.py"),
            str(fixtures / "valid-bilingual-lecture.json"),
            str(manifest_path),
            "--output-root",
            str(output_root),
        )
        manifest["files"] = manifest["files"][:1]
        invalid_manifest_path = output_root / "delivery-invalid.json"
        invalid_manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        run(
            str(ROOT / "scripts" / "validate_delivery.py"),
            str(fixtures / "valid-bilingual-lecture.json"),
            str(invalid_manifest_path),
            "--output-root",
            str(output_root),
            expected=1,
        )

    run(str(ROOT / "scripts" / "check_internal_links.py"), str(ROOT))
    print("PASS: all smoke tests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

