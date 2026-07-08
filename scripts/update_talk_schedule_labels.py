#!/usr/bin/env python3
"""Add explicit schedule track/room labels to existing talk pages."""

from __future__ import annotations

import json
import re
from pathlib import Path

from build_worldsfair_wiki import ROOT, assign_talk_slugs, day_to_date, schedule_labels, talk_slug, yaml_list


def load_sessions() -> list[dict]:
    blob = json.loads((ROOT / "raw" / "sources" / "official-sessions.json").read_text())
    sessions = blob.get("sessions", blob) if isinstance(blob, dict) else blob
    assign_talk_slugs(sessions)
    return sessions


def quote_yaml(value: str | None) -> str:
    return json.dumps(str(value), ensure_ascii=False) if value else '""'


def upsert_frontmatter_field(frontmatter: str, key: str, value: str) -> str:
    line = f"{key}: {value}"
    pattern = re.compile(rf"^{re.escape(key)}: .*$", re.M)
    if pattern.search(frontmatter):
        return pattern.sub(line, frontmatter)
    return frontmatter.rstrip() + "\n" + line + "\n"


def remove_existing_schedule_labels(body: str) -> str:
    return re.sub(r"\n## Schedule Labels\n(?:- .+\n?)+", "\n", body)


def insert_schedule_block(body: str, session: dict) -> str:
    body = remove_existing_schedule_labels(body)
    block = "\n".join(
        [
            "## Schedule Labels",
            f"- Track: {session.get('track') or 'track TBD'}",
            f"- Room: {session.get('room') or 'room TBD'}",
            f"- Session type: {session.get('type', 'unknown')}",
            f"- Status: {session.get('status', 'unknown')}",
            "",
        ]
    )
    marker = "\n## Official Description\n"
    if marker in body:
        return body.replace(marker, "\n" + block + marker, 1)
    return body.rstrip() + "\n\n" + block


def update_page(path: Path, session: dict) -> bool:
    original = path.read_text(encoding="utf-8")
    if not original.startswith("---\n"):
        return False
    end = original.find("\n---\n", 4)
    if end == -1:
        return False
    fm = original[4:end]
    body = original[end + 5 :]
    fm = upsert_frontmatter_field(fm, "scheduleTrack", quote_yaml(session.get("track")))
    fm = upsert_frontmatter_field(fm, "scheduleRoom", quote_yaml(session.get("room")))
    fm = upsert_frontmatter_field(fm, "scheduleLabels", yaml_list(schedule_labels(session)))
    updated = "---\n" + fm.rstrip() + "\n---\n" + insert_schedule_block(body, session).lstrip()
    if updated == original:
        return False
    path.write_text(updated.rstrip() + "\n", encoding="utf-8")
    return True


def main() -> int:
    updated = 0
    missing = 0
    for session in load_sessions():
        path = ROOT / "wiki" / "talks" / f"{talk_slug(session)}.md"
        if not path.exists():
            missing += 1
            continue
        if update_page(path, session):
            updated += 1
    print(json.dumps({"updated_talk_pages": updated, "missing_talk_pages": missing}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
