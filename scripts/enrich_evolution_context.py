#!/usr/bin/env python3
"""Add evidence-gated evolution context to topic and synthesis articles.

The prose comes from a reviewed profile rather than being inferred from page
text. A page is changed only when it matches a configured theme and already
links to enough local evidence for that theme.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
DEFAULT_PROFILE = ROOT / "raw" / "sources" / "evolution-context-profile.json"
DEFAULT_CATEGORIES = ("topics", "questions", "harnesses", "playbooks", "evaluations")
SECTION_NAMES = ("How This Theme Evolved", "Why This Matters Now", "Practical Lesson")
WRITER_CONTRACT = {
    "writer_id": "enrich-evolution-context",
    "scope": "owned_block",
    "owned_output_keys": [f"section:{name}" for name in SECTION_NAMES],
    "incremental_safe": True,
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def wikilinks(markdown: str) -> set[str]:
    return {
        raw.split("|", 1)[0].split("#", 1)[0].strip()
        for raw in re.findall(r"\[\[([^\]]+)\]\]", markdown)
        if raw.split("|", 1)[0].split("#", 1)[0].strip()
    }


def upsert_section(markdown: str, heading: str, body: str) -> str:
    replacement = f"## {heading}\n{body.strip()}\n\n"
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    if pattern.search(markdown):
        return pattern.sub(lambda _match: replacement, markdown).rstrip() + "\n"
    return markdown.rstrip() + "\n\n" + replacement


def validate_profile(profile: dict) -> None:
    if profile.get("schemaVersion") != 1:
        raise ValueError("profile schemaVersion must be 1")
    if not profile.get("comparisonBoundary"):
        raise ValueError("profile comparisonBoundary is required")
    stage_ids = {stage.get("id") for stage in profile.get("stages", [])}
    if not stage_ids or None in stage_ids:
        raise ValueError("profile stages require unique ids")
    if len(stage_ids) != len(profile["stages"]):
        raise ValueError("profile stage ids must be unique")
    for theme in profile.get("themes", []):
        missing = [name for name in ("id", "match", "evolution", "whyNow", "practicalLesson", "confidence") if not theme.get(name)]
        if missing:
            raise ValueError(f"theme is missing required fields: {', '.join(missing)}")
        unknown = set(theme["evolution"]) - stage_ids
        if unknown:
            raise ValueError(f"theme {theme['id']} references unknown stages: {sorted(unknown)}")
        gate = theme.get("evidenceGate", {})
        if not gate.get("requiredAny") or int(gate.get("minimumMatches", 0)) < 1:
            raise ValueError(f"theme {theme['id']} requires a non-empty evidence gate")


def matching_theme(path: Path, markdown: str, profile: dict) -> dict | None:
    category = path.parent.name
    slug = path.stem
    links = wikilinks(markdown)
    for theme in profile["themes"]:
        match = theme["match"]
        if category not in match.get("categories", DEFAULT_CATEGORIES):
            continue
        if slug not in match.get("slugs", []):
            continue
        gate = theme["evidenceGate"]
        hits = links.intersection(gate["requiredAny"])
        if len(hits) >= int(gate.get("minimumMatches", 1)):
            return {**theme, "matchedEvidence": sorted(hits)}
    return None


def render_sections(theme: dict, profile: dict) -> dict[str, str]:
    stages = {stage["id"]: stage for stage in profile["stages"]}
    evolution = [
        f"- **{stages[stage_id]['label']} ({stages[stage_id]['evidenceRole']}):** {summary}"
        for stage_id, summary in theme["evolution"].items()
    ]
    evolution.extend(
        [
            "",
            f"**Confidence:** {theme['confidence']}.",
            f"**Boundary:** {profile['comparisonBoundary']}",
            f"**Comparison source:** [[{profile['comparisonSource']}]].",
        ]
    )
    evidence = ", ".join(f"[[{slug}]]" for slug in theme["matchedEvidence"])
    why_now = "\n\n".join(
        [
            theme["whyNow"],
            f"**WF26 evidence gate:** this section was emitted only because the page links to configured local evidence. Relevant configured evidence: {evidence}.",
            f"**Confidence:** {theme['confidence']}. Comparison history is context; linked WF26 pages remain the evidence for current-event claims.",
        ]
    )
    practical = "\n\n".join(
        [
            theme["practicalLesson"],
            f"**Confidence:** {theme['confidence']}. Treat this as synthesis derived from the linked evidence graph, not as an official schedule claim.",
        ]
    )
    return dict(zip(SECTION_NAMES, ("\n".join(evolution), why_now, practical)))


def enrich(markdown: str, theme: dict, profile: dict) -> str:
    updated = markdown
    for heading, body in render_sections(theme, profile).items():
        updated = upsert_section(updated, heading, body)
    return updated.rstrip() + "\n"


def candidate_paths(paths: list[str], categories: list[str]) -> list[Path]:
    if paths:
        resolved = [(ROOT / value).resolve() if not Path(value).is_absolute() else Path(value).resolve() for value in paths]
        for path in resolved:
            if ROOT not in path.parents or path.suffix != ".md":
                raise ValueError(f"input must be a markdown file under the project root: {path}")
        return sorted(set(resolved))
    return [
        path
        for category in categories
        for path in sorted((WIKI / category).glob("*.md"))
        if path.name != "index.md"
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--path", action="append", default=[], help="Project-relative markdown input; repeatable.")
    parser.add_argument("--category", action="append", choices=DEFAULT_CATEGORIES, default=[])
    parser.add_argument("--all", action="store_true", help="Scan every supported synthesis category.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--check", action="store_true", help="Exit 1 if an eligible page is not current.")
    args = parser.parse_args(argv)

    profile = json.loads(read(args.profile))
    validate_profile(profile)
    categories = list(DEFAULT_CATEGORIES) if args.all or not args.category else args.category
    paths = candidate_paths(args.path, categories)
    changed: list[str] = []
    skipped_no_theme = 0
    skipped_evidence_gate = 0
    configured_slugs = {slug for theme in profile["themes"] for slug in theme["match"].get("slugs", [])}

    for path in paths:
        original = read(path)
        theme = matching_theme(path, original, profile)
        if theme is None:
            if path.stem in configured_slugs:
                skipped_evidence_gate += 1
            else:
                skipped_no_theme += 1
            continue
        updated = enrich(original, theme, profile)
        if updated != original:
            changed.append(str(path.relative_to(ROOT)))
            if not args.dry_run and not args.check:
                write(path, updated)

    print(json.dumps({
        "profile": str(args.profile),
        "scanned": len(paths),
        "changed": changed,
        "changedCount": len(changed),
        "skippedNoTheme": skipped_no_theme,
        "skippedEvidenceGate": skipped_evidence_gate,
        "dryRun": args.dry_run,
    }, indent=2))
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
