#!/usr/bin/env python3
"""Repair talk-page official descriptions from the official schedule data."""

from __future__ import annotations

import json
import re
from pathlib import Path

from build_worldsfair_wiki import ROOT, assign_talk_slugs, format_official_description, talk_slug


def load_sessions() -> list[dict]:
    path = ROOT / "raw" / "sources" / "official-sessions.json"
    blob = json.loads(path.read_text(encoding="utf-8"))
    sessions = blob.get("sessions", blob) if isinstance(blob, dict) else blob
    assign_talk_slugs(sessions)
    return sessions


def replace_section(text: str, heading: str, body: str) -> str:
    section = f"## {heading}\n{body.strip()}\n\n"
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    if not pattern.search(text):
        return text.rstrip() + "\n\n" + section
    return pattern.sub(section, text).rstrip() + "\n"


def main() -> int:
    updated = 0
    missing = 0
    for session in load_sessions():
        page = ROOT / "wiki" / "talks" / f"{talk_slug(session)}.md"
        if not page.exists():
            missing += 1
            continue
        original = page.read_text(encoding="utf-8")
        formatted = format_official_description(session.get("description"))
        repaired = replace_section(original, "Official Description", formatted)
        if repaired != original:
            page.write_text(repaired, encoding="utf-8")
            updated += 1
    print(json.dumps({"updated_talk_pages": updated, "missing_talk_pages": missing}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
