from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from markdown_blocks import blockquote  # noqa: E402


def test_blockquote_preserves_paragraphs_without_trailing_space() -> None:
    rendered = blockquote("first line\n\nsecond line\n\n\nthird line")

    assert rendered == "> first line\n>\n> second line\n>\n> third line"
    assert not any(line.endswith(" ") for line in rendered.splitlines())
