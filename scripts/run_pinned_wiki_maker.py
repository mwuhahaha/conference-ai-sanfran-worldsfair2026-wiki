#!/usr/bin/env python3
"""Run WF26 updates with the immutable, locally installed wiki-maker source."""

from __future__ import annotations

import os
import sys

from install_pinned_wiki_maker_runtime import RUNTIME_ROOT, validate_runtime


PYTHON = "/usr/bin/python3"


def main() -> int:
    try:
        validate_runtime()
    except (OSError, RuntimeError) as exc:
        print(
            f"{exc}. Run scripts/install_pinned_wiki_maker_runtime.py first.",
            file=sys.stderr,
        )
        return 2
    environment = os.environ.copy()
    pinned_source = str(RUNTIME_ROOT / "src")
    inherited = environment.get("PYTHONPATH", "")
    environment["PYTHONPATH"] = (
        pinned_source + (os.pathsep + inherited if inherited else "")
    )
    os.execve(
        PYTHON,
        [PYTHON, "-m", "wiki_from_topic_maker", *sys.argv[1:]],
        environment,
    )
    return 127


if __name__ == "__main__":
    raise SystemExit(main())
