#!/usr/bin/env python3
"""Enrich generated company pages without overwriting curated company prose.

This is the targeted updater for the company-page portion of
build_worldsfair_wiki.py. It replaces old stub-shaped company pages and pages
with curated public profiles, while leaving existing hand/synthesis enriched
company pages in place.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

from build_worldsfair_wiki import (
    ROOT,
    build_company_pages,
    company_importance_text,
    day_to_date,
    frontmatter,
    load_company_profiles,
    md_label,
    slugify,
    talk_slug,
    unique_list,
    write,
)


STUB_MARKER = "## Why It Appears\nThis organization appears in the official AI Engineer World's Fair 2026 speaker roster."


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def should_update(path: Path, profile: dict) -> bool:
    if profile:
        return True
    if not path.exists():
        return True
    text = path.read_text(errors="ignore")
    return STUB_MARKER in text


def render_company_page(company_slug: str, company_page: dict) -> str:
    company = company_page["title"]
    aliases = company_page["aliases"]
    people = company_page["people"]
    related_sessions = company_page["sessions"]
    profile = company_page.get("profile") or {}
    source_labels = unique_list(["Official speaker roster", "Official conference schedule", *profile.get("sourceLabels", [])])
    body = [
        frontmatter(
            {
                "title": company,
                "category": "companies",
                "aliases": aliases,
                "website": profile.get("website"),
                "sourceLabels": source_labels,
            }
        ),
        f"# {company}",
        "",
        "## What It Is",
        profile.get("summary")
        or "No public company profile has been added yet. This page is grounded in the official speaker roster and schedule context until a relevant company site, product page, or public profile is reviewed.",
        "",
        "## Why It Matters At World's Fair",
        company_importance_text(company, people, related_sessions, profile),
        "",
        "## Related People",
    ]
    for person in sorted(people, key=lambda p: p.get("name", "")):
        body.append(f"- [[{slugify(person.get('name', ''))}]] - {person.get('role') or 'role not listed'}")
    body.extend(["", "## Related Scheduled Sessions"])
    if related_sessions:
        for session in sorted(related_sessions, key=lambda s: (day_to_date(s.get("day", "")), s.get("time", ""), s.get("title", ""))):
            body.append(f"- [[{talk_slug(session)}]] - {session.get('title')} ({day_to_date(session.get('day', ''))}, {session.get('time') or 'time TBD'})")
    else:
        body.append("- No related scheduled sessions were found from the official schedule data.")
    if profile.get("origin"):
        body.extend(["", "## Origin And Context", profile["origin"]])
    if profile.get("notes"):
        body.extend(["", "## Notes"])
        for note in profile["notes"]:
            body.append(f"- {note}")
    body.extend(["", "## Public Sources"])
    links = profile.get("sourceLinks") or []
    if links:
        for link in links:
            body.append(f"- [{md_label(link.get('label') or link.get('url'))}]({link.get('url')})")
    else:
        body.append("- No public company/profile source links have been added yet.")
    body.extend(
        [
            "",
            "## Evidence Boundary",
            "Official roster and schedule facts are treated as canonical for conference participation. Public company sites, documentation, and professional profiles are supporting context used to explain what the organization does and why it is relevant.",
        ]
    )
    return "\n".join(body)


def main() -> int:
    speakers_blob = load_json(ROOT / "raw" / "sources" / "official-speakers.json")
    sessions_blob = load_json(ROOT / "raw" / "sources" / "official-sessions.json")
    speakers = speakers_blob.get("speakers", [])
    sessions = sessions_blob.get("sessions", [])

    sessions_by_speaker = defaultdict(list)
    for session in sessions:
        for speaker in session.get("speakers", []):
            sessions_by_speaker[speaker].append(session)

    company_people = defaultdict(list)
    for speaker in speakers:
        if speaker.get("company"):
            company_people[speaker["company"]].append(speaker)

    pages = build_company_pages(company_people, sessions_by_speaker, load_company_profiles())
    changed = []
    skipped = []
    for company_slug, page in sorted(pages.items()):
        path = ROOT / "wiki" / "companies" / f"{company_slug}.md"
        if not should_update(path, page.get("profile") or {}):
            skipped.append(company_slug)
            continue
        write(path, render_company_page(company_slug, page))
        changed.append(company_slug)

    print(f"updated {len(changed)} company pages")
    if changed:
        print("\n".join(changed[:80]))
    print(f"skipped {len(skipped)} already enriched company pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
