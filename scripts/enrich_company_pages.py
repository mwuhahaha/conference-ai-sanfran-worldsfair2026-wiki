#!/usr/bin/env python3
"""Enrich generated company pages without overwriting curated company prose.

This is the targeted updater for the company-page portion of
build_worldsfair_wiki.py. It replaces old stub-shaped company pages and pages
with curated public profiles, while leaving existing hand/synthesis enriched
company pages in place.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from build_worldsfair_wiki import (
    ROOT,
    build_company_pages,
    company_importance_text,
    day_to_date,
    frontmatter,
    md_label,
    slugify,
    talk_slug,
    unique_list,
    write,
)


STUB_MARKER = "## Why It Appears\nThis organization appears in the official AI Engineer World's Fair 2026 speaker roster."
PRIVATE_CREDIBILITY_POLICY = (
    ROOT
    / ".ops"
    / "state"
    / "cache"
    / "wiki-maker"
    / "credibility-v2"
    / "writing-policy.json"
)
PRIVATE_COMPANY_PROFILES = (
    ROOT
    / ".ops"
    / "state"
    / "cache"
    / "wiki-maker"
    / "credibility-v2"
    / "company-profile-candidates.json"
)
LEGACY_COMPANY_PROFILES = ROOT / "raw" / "sources" / "company-profiles.json"
PRESERVE_SECTIONS = [
    "Source-Derived Enrichment",
]
COLLECTION_PROCESS_PATTERN = re.compile(
    r"\b(?:"
    r"automated company profile fetch|"
    r"candidate[- ]state|"
    r"credibility[- ]v2|"
    r"domain[- ]guess(?:ing)?|"
    r"fetch status|"
    r"fetched for (?:homepage )?metadata|"
    r"manual (?:company )?url override|"
    r"manual override|"
    r"private credibility|"
    r"(?:company profile|homepage|public (?:company )?site) (?:was )?fetched|"
    r"validation (?:check|decision|pipeline|status)"
    r")\b",
    re.IGNORECASE,
)
COLLECTION_PROCESS_LABEL_PATTERN = re.compile(
    r"(?:"
    r"automated .*(?:discovery|fetch|profile)|"
    r"candidate|"
    r"collection process|"
    r"credibility[- ]v2|"
    r"domain[- ]guess|"
    r"fetch status|"
    r"manual .*(?:override|selection)|"
    r"private source selection|"
    r"validation (?:decision|pipeline|status)"
    r")",
    re.IGNORECASE,
)


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


def company_profile_decisions() -> dict[str, dict]:
    policy = load_json(PRIVATE_CREDIBILITY_POLICY)
    rows = policy.get("companyProfileWritingDecisions", {})
    if not isinstance(rows, dict):
        return {}
    return {slug: value for slug, value in rows.items() if isinstance(value, dict)}


def company_profile_source_path(explicit: Path | None = None) -> Path:
    if explicit is not None:
        return explicit if explicit.is_absolute() else ROOT / explicit
    if PRIVATE_COMPANY_PROFILES.is_file():
        return PRIVATE_COMPANY_PROFILES
    return LEGACY_COMPANY_PROFILES


def load_company_profile_candidates(explicit: Path | None = None) -> dict:
    path = company_profile_source_path(explicit)
    payload = load_json(path)
    return payload if isinstance(payload, dict) else {}


def collection_process_text(value: str) -> bool:
    return COLLECTION_PROCESS_PATTERN.search(value) is not None


def collection_process_label(value: str) -> bool:
    return COLLECTION_PROCESS_LABEL_PATTERN.search(value) is not None


def sanitized_public_prose(value: object) -> str:
    if not isinstance(value, str):
        return ""
    compact = re.sub(r"\s+", " ", value).strip()
    sentences = re.split(r"(?<=[.!?])\s+", compact)
    return " ".join(
        sentence
        for sentence in sentences
        if sentence and not collection_process_text(sentence)
    )


def sanitized_source_labels(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    return unique_list(
        label.strip()
        for label in value
        if isinstance(label, str)
        and label.strip()
        and not collection_process_label(label)
    )


def sanitized_source_links(value: object) -> list[dict[str, str]]:
    if not isinstance(value, list):
        return []
    links: list[dict[str, str]] = []
    for raw_link in value:
        if not isinstance(raw_link, dict):
            continue
        url = str(raw_link.get("url") or "").strip()
        if not url.startswith("https://") or any(char.isspace() for char in url):
            continue
        link = {"url": url}
        label = sanitized_public_prose(raw_link.get("label"))
        if label and not collection_process_label(label):
            link["label"] = label
        links.append(link)
    return links


def publishable_profile(profile: dict, decision: dict | None) -> dict:
    if not profile or not decision:
        return {}
    if decision.get("writingDisposition") not in {
        "assert_with_citations",
        "attribute_to_source",
    }:
        return {}
    public: dict[str, object] = {}
    website = str(profile.get("website") or "").strip()
    if website.startswith("https://") and not any(
        char.isspace() for char in website
    ):
        public["website"] = website
    for key in ("summary", "origin", "why_it_matters"):
        value = sanitized_public_prose(profile.get(key))
        if value:
            public[key] = value
    source_links = sanitized_source_links(profile.get("sourceLinks"))
    if source_links:
        public["sourceLinks"] = source_links
    source_labels = sanitized_source_labels(profile.get("sourceLabels"))
    if source_labels:
        public["sourceLabels"] = source_labels
    return public


def profile_public_fragments(profile: dict) -> tuple[str, ...]:
    fragments: set[str] = set()
    website = profile.get("website")
    if isinstance(website, str) and website.startswith("https://"):
        fragments.add(website)
    for link in profile.get("sourceLinks", []):
        if not isinstance(link, dict):
            continue
        url = link.get("url")
        if isinstance(url, str) and url.startswith("https://"):
            fragments.add(url)
    summary = profile.get("summary")
    if isinstance(summary, str) and len(summary.strip()) >= 24:
        fragments.add(summary.strip())
    return tuple(sorted(fragments))


def held_profile_public_leaks(
    profiles: dict[str, dict],
    decisions: dict[str, dict],
    *,
    wiki_root: Path,
) -> dict[str, tuple[str, ...]]:
    """Fail closed when an omitted profile survives in a curated company page."""

    leaks: dict[str, tuple[str, ...]] = {}
    for slug, profile in sorted(profiles.items()):
        if not isinstance(profile, dict):
            continue
        decision = decisions.get(slug, {})
        if decision.get("writingDisposition") != "omit":
            continue
        path = wiki_root / "companies" / f"{slug}.md"
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        found = tuple(
            fragment for fragment in profile_public_fragments(profile) if fragment in text
        )
        if found:
            leaks[slug] = found
    return leaks


def extract_section(markdown: str, heading: str) -> str:
    import re

    match = re.search(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", markdown, re.M | re.S)
    return match.group(0).strip() if match else ""


def render_company_page(company_slug: str, company_page: dict, existing: str = "") -> str:
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
        or (
            f"{company} is represented in the official AI Engineer World's Fair 2026 roster. "
            "The article is grounded in the official roster, related speakers, and scheduled sessions while public company-source enrichment is unavailable or still being reviewed."
        ),
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
        body.append("- Official roster and schedule sources currently provide the source basis for this organization; no separate organization profile URL has been verified.")
    body.extend(
        [
            "",
            "## Evidence Boundary",
            (
                "Official roster and schedule facts are treated as canonical for conference participation. "
                "Included organization-site descriptions remain attributed owner context, not independent validation or endorsement."
                if profile
                else "Official roster and schedule facts are treated as canonical for conference participation. No separate organization-profile claim is included without a validated identity path."
            ),
        ]
    )
    for heading in PRESERVE_SECTIONS:
        preserved = extract_section(existing, heading)
        if preserved and f"## {heading}\n" not in "\n".join(body):
            body.extend(["", preserved])
    return "\n".join(body)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument(
        "--company-profiles",
        type=Path,
        help=(
            "Explicit candidate-state input. Defaults to private credibility-v2 "
            "state, with the legacy raw source retained as a read-only fallback."
        ),
    )
    args = parser.parse_args(argv)
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

    profiles = load_company_profile_candidates(args.company_profiles)
    pages = build_company_pages(company_people, sessions_by_speaker, profiles)
    decisions = company_profile_decisions()
    changed = []
    skipped = []
    for company_slug, page in sorted(pages.items()):
        path = ROOT / "wiki" / "companies" / f"{company_slug}.md"
        existing = path.read_text(errors="ignore") if path.exists() else ""
        original_profile = page.get("profile") or {}
        if not should_update(path, original_profile):
            skipped.append(company_slug)
            continue
        safe_page = dict(page)
        safe_page["profile"] = publishable_profile(
            original_profile,
            decisions.get(company_slug),
        )
        write(path, render_company_page(company_slug, safe_page, existing))
        changed.append(company_slug)

    public_leaks = held_profile_public_leaks(
        profiles,
        decisions,
        wiki_root=ROOT / "wiki",
    )
    if public_leaks:
        raise RuntimeError(
            "held company profile reached public article(s): "
            + ", ".join(sorted(public_leaks))
        )

    print(f"updated {len(changed)} company pages")
    if changed:
        print("\n".join(changed[:80]))
    print(f"skipped {len(skipped)} already enriched company pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
