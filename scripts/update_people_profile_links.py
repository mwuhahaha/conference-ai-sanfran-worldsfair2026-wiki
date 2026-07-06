#!/usr/bin/env python3
"""Upsert speaker profile links onto existing people pages.

This preserves hand-written/enriched page bodies while surfacing public profile
links from the official speaker roster near the role/company section.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEAKERS = ROOT / "raw" / "sources" / "official-speakers.json"
PEOPLE = ROOT / "wiki" / "people"
PROFILE_KEYS = ("linkedin", "twitter", "website", "blog")


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-") or "untitled"


def profile_link_lines(speaker: dict) -> list[str]:
    links = []
    if speaker.get("linkedin"):
        links.append(f"- [LinkedIn]({speaker['linkedin']})")
    if speaker.get("twitter"):
        links.append(f"- [X / Twitter]({speaker['twitter']})")
    if speaker.get("website"):
        links.append(f"- [Website]({speaker['website']})")
    if speaker.get("blog"):
        links.append(f"- [Blog]({speaker['blog']})")
    return links


def upsert_frontmatter(text: str, speaker: dict) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---", 4)
    if end == -1:
        return text
    front = text[4:end]
    rest = text[end:]
    lines = [line for line in front.splitlines() if not any(line.startswith(f"{key}:") for key in PROFILE_KEYS)]
    insert_at = len(lines)
    for idx, line in enumerate(lines):
        if line.startswith("company:"):
            insert_at = idx + 1
            break
    additions = [f"{key}: {json.dumps(speaker[key], ensure_ascii=False)}" for key in PROFILE_KEYS if speaker.get(key)]
    if additions:
        lines[insert_at:insert_at] = additions
    return "---\n" + "\n".join(lines).rstrip() + rest


def upsert_profile_section(text: str, speaker: dict) -> str:
    links = profile_link_lines(speaker)
    section = "## Profile Links\n" + "\n".join(links or ["No public profile links listed in the official speaker roster."]) + "\n\n"
    text = re.sub(r"\n## Links\n.*?(?=\n## |\Z)", "\n", text, flags=re.S)
    text = re.sub(r"\n## Profile Links\n.*?(?=\n## |\Z)", "\n", text, flags=re.S)
    marker = "\n## Official Bio\n"
    if marker in text:
        return text.replace(marker, "\n" + section + "## Official Bio\n", 1)
    return text.rstrip() + "\n\n" + section.rstrip() + "\n"


def main() -> int:
    data = json.loads(SPEAKERS.read_text())
    updated = 0
    for speaker in data.get("speakers", []):
        name = speaker.get("name")
        if not name:
            continue
        path = PEOPLE / f"{slugify(name)}.md"
        if not path.exists():
            continue
        original = path.read_text()
        text = upsert_frontmatter(original, speaker)
        text = upsert_profile_section(text, speaker)
        if text != original:
            path.write_text(text.rstrip() + "\n")
            updated += 1
    print(json.dumps({"updated_people_pages": updated}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
