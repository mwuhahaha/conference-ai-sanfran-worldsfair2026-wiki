#!/usr/bin/env python3
"""Install the immutable wiki-maker runtime used by the WF26 monitor."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_REPOSITORY = ROOT.parent / "wiki-from-topic-maker"
EXPECTED_COMMIT = "c5bc782956d85fdf5d3347858eb2ce49b6054f6a"
RUNTIME_ROOT = (
    ROOT
    / ".ops"
    / "runtime"
    / f"wiki-from-topic-maker-{EXPECTED_COMMIT[:12]}"
)


def git(*args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        check=True,
        capture_output=True,
        text=True,
        timeout=300,
    )
    return completed.stdout.strip()


def validate_runtime(path: Path = RUNTIME_ROOT) -> dict[str, str]:
    if not path.is_dir():
        raise RuntimeError(f"pinned wiki-maker runtime is missing: {path}")
    head = git("-C", str(path), "rev-parse", "HEAD")
    if head != EXPECTED_COMMIT:
        raise RuntimeError(
            "pinned wiki-maker runtime has the wrong commit: "
            f"expected {EXPECTED_COMMIT}, found {head}"
        )
    status = git(
        "-C",
        str(path),
        "status",
        "--porcelain",
        "--untracked-files=all",
    )
    if status:
        raise RuntimeError(f"pinned wiki-maker runtime is dirty: {path}")
    package = path / "src" / "wiki_from_topic_maker" / "__init__.py"
    if not package.is_file():
        raise RuntimeError(f"pinned wiki-maker package is missing: {package}")
    return {
        "commit": head,
        "runtime": str(path),
        "source": str(SOURCE_REPOSITORY),
    }


def install_runtime() -> dict[str, str]:
    if RUNTIME_ROOT.exists():
        return {"status": "reused", **validate_runtime()}
    if not (SOURCE_REPOSITORY / ".git").exists():
        raise RuntimeError(
            f"wiki-maker source repository is unavailable: {SOURCE_REPOSITORY}"
        )
    git(
        "-C",
        str(SOURCE_REPOSITORY),
        "cat-file",
        "-e",
        f"{EXPECTED_COMMIT}^{{commit}}",
    )
    RUNTIME_ROOT.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(
        tempfile.mkdtemp(
            prefix=f".wiki-from-topic-maker-{EXPECTED_COMMIT[:12]}-",
            dir=RUNTIME_ROOT.parent,
        )
    )
    try:
        git(
            "clone",
            "--quiet",
            "--no-hardlinks",
            "--no-checkout",
            str(SOURCE_REPOSITORY),
            str(temporary),
        )
        git(
            "-C",
            str(temporary),
            "checkout",
            "--quiet",
            "--detach",
            EXPECTED_COMMIT,
        )
        validate_runtime(temporary)
        os.replace(temporary, RUNTIME_ROOT)
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
    return {"status": "installed", **validate_runtime()}


def main() -> int:
    print(json.dumps(install_runtime(), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
