#!/usr/bin/env python3
"""Find source-backed relationships between people without publishing scores."""

from __future__ import annotations

import argparse
import itertools
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from third_party_connection_policy import assess_connection, write_internal_policy

ROOT = Path(__file__).resolve().parents[1]
PEOPLE = ROOT / "wiki" / "people"
CACHE = ROOT / ".ops" / "state" / "cache" / "person-linking"
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
URL_RE = re.compile(r'https?://[^\s)\]>"\']+')
PROFILE_HOSTS = ("github.com", "linkedin.com", "x.com", "twitter.com")

# Internal calibration only. Never include these values in wiki output.
WEIGHTS = {"shared_session": 5, "explicit_person_link": 5, "shared_organization": 4}


@dataclass(frozen=True)
class Person:
    slug: str
    title: str
    path: Path
    organizations: frozenset[str]
    sessions: frozenset[str]
    people: frozenset[str]
    resources: frozenset[str]


def load_people() -> list[Person]:
    slugs = {path.stem for path in PEOPLE.glob("*.md") if path.name not in {"index.md", "people.md"}}
    result = []
    for path in sorted(PEOPLE.glob("*.md")):
        if path.stem not in slugs:
            continue
        text = path.read_text(encoding="utf-8")
        links = set(WIKILINK_RE.findall(text))
        title = next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), path.stem)
        sessions = {link for link in links if re.match(r"^20\d\d-\d\d-\d\d-", link)}
        people = links & slugs
        organizations = links - sessions - people
        resources = {url.rstrip("/.,") for url in URL_RE.findall(text) if any(host in url.lower() for host in PROFILE_HOSTS)}
        result.append(Person(path.stem, title, path, frozenset(organizations), frozenset(sessions), frozenset(people), frozenset(resources)))
    return result


def compare(left: Person, right: Person) -> dict | None:
    evidence = []
    for value in sorted(left.sessions & right.sessions):
        evidence.append({"type": "shared_session", "target": value})
    for value in sorted(left.organizations & right.organizations):
        evidence.append({"type": "shared_organization", "target": value})
    if right.slug in left.people or left.slug in right.people:
        evidence.append({"type": "explicit_person_link", "target": right.slug if right.slug in left.people else left.slug})
    if not evidence:
        return None
    score = sum(WEIGHTS[item["type"]] for item in evidence)
    confidence = "high" if score >= 5 else "medium"
    validation = assess_connection(
        {"official_exact_source": any(item["type"] == "shared_session" for item in evidence)},
        identity_required=False,
    )
    return {
        "left": left.slug,
        "right": right.slug,
        "confidence": confidence,
        "evidence": evidence,
        "validation": validation,
        "internal_score": score,
    }


def profile_identity_collisions(people: list[Person]) -> list[dict]:
    owners: dict[str, list[str]] = defaultdict(list)
    for person in people:
        for resource in person.resources:
            owners[resource].append(person.slug)
    return [
        {
            "resource": resource,
            "people": sorted(set(slugs)),
            "validation": assess_connection({"identity_conflict": True}, identity_required=True),
        }
        for resource, slugs in sorted(owners.items())
        if len(set(slugs)) > 1
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Evaluate without writing internal artifacts.")
    args = parser.parse_args()
    people = load_people()
    pairs = len(people) * (len(people) - 1) // 2
    connections = [item for left, right in itertools.combinations(people, 2) if (item := compare(left, right))]
    collisions = profile_identity_collisions(people)
    payload = {
        "version": 2,
        "people": len(people),
        "pairs_evaluated": pairs,
        "connections": connections,
        "identity_collisions": collisions,
        "research_boundary": "Shared external profiles are identity-collision warnings, never positive evidence that two people are connected.",
    }
    if not args.check:
        write_internal_policy()
        CACHE.mkdir(parents=True, exist_ok=True)
        (CACHE / "connections.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        (CACHE / "scoring-profile.json").write_text(json.dumps({"version": 2, "weights": WEIGHTS}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"people": len(people), "pairs_evaluated": pairs, "connections": len(connections), "identity_collisions": len(collisions), "written": not args.check}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
