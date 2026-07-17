"""Small Markdown rendering helpers shared by generated evidence pages."""

from __future__ import annotations

import re


def blockquote(text: str) -> str:
    """Render a multiline blockquote without whitespace-only quote lines."""

    compact = re.sub(r"\n{3,}", "\n\n", text.strip())
    return "\n".join(
        ">" if not line else f"> {line}" for line in compact.splitlines()
    )
