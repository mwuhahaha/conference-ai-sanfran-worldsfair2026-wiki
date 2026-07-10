#!/usr/bin/env python3
"""Remove known non-public editorial labels from publishable wiki text."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCOPES = [ROOT / "wiki", ROOT / "raw" / "sources"]
TEXT_SUFFIXES = {".md", ".json", ".txt"}
BLOCKED_PHRASES = [
    " (DO NOT PUBLISH)",
]


def should_scan(path: Path) -> bool:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return False
    rel = path.relative_to(ROOT).as_posix()
    return not (
        rel.startswith(".ops/state/cache/")
        or rel.startswith(".ops/state/runs/")
        or rel.startswith("raw/video-cache/")
        or rel.startswith("raw/audio-cache/")
        or rel.startswith("raw/slide-frames-tmp/")
    )


def main() -> int:
    changed = 0
    for scope in SCOPES:
        if not scope.exists():
            continue
        for path in scope.rglob("*"):
            if not path.is_file() or not should_scan(path):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            updated = text
            for phrase in BLOCKED_PHRASES:
                updated = updated.replace(phrase, "")
            if updated != text:
                path.write_text(updated, encoding="utf-8")
                changed += 1
    print(f"Sanitized {changed} public wiki/source files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
