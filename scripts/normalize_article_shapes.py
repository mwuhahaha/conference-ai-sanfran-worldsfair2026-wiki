#!/usr/bin/env python3
"""Normalize public wiki article shapes by page category.

The goal is not to make every page identical. It is to give each page type a
predictable, agent-friendly Wikipedia-like shape while avoiding explicit
journalistic headings such as "what/why/how" on topic articles.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import OrderedDict, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"


ALIASES: dict[str, dict[str, str]] = {
    "talks": {
        "Why This Talk Matters": "Significance",
        "Why This Talk Is Important": "Significance",
        "Official Schedule Context": "Conference Context",
        "Schedule Labels": "Conference Context",
        "Official Description": "Session Description",
        "Technical Throughline": "Technical Pattern",
        "Practical Pattern": "Applied Pattern",
        "Related YouTube Video": "Media Evidence",
        "Transcript Markdown": "Media Evidence",
        "Additional Photo Slide Evidence": "Media Evidence",
        "Slides": "Media Evidence",
        "Related Public Sources": "Sources",
        "Related Pages": "Connections",
        "Source-Derived Enrichment": "Evidence Graph",
    },
    "people": {
        "Official Role": "Profile",
        "Profile Links": "Profile",
        "Official Bio": "Biography",
        "Why He Matters At World's Fair": "Conference Relevance",
        "Why She Matters At World's Fair": "Conference Relevance",
        "Why They Matter At World's Fair": "Conference Relevance",
        "Why This Person Matters At World's Fair": "Conference Relevance",
        "Scheduled Sessions": "Conference Sessions",
        "Related AI Engineer Media": "Media Evidence",
        "Related Company And Tool Context": "Connections",
        "Related Pages": "Connections",
        "Source-Derived Enrichment": "Evidence Graph",
    },
    "companies": {
        "What It Is": "Overview",
        "Origin And Context": "Background",
        "Why It Matters At World's Fair": "Conference Relevance",
        "Related People": "Connections",
        "Related Scheduled Sessions": "Conference Sessions",
        "Related Tools": "Connections",
        "Public Sources": "Sources",
        "Source-Derived Enrichment": "Evidence Graph",
    },
    "topics": {
        "Synopsis": "Overview",
        "What It Is": "Overview",
        "Origin And Context": "Conference Context",
        "Origins In This Conference": "Conference Context",
        "Why It Matters": "Significance",
        "How It Works": "Technical Model",
        "How To Use It": "Applied Use",
        "Where It Is Useful": "Applied Use",
        "When To Use It": "Applied Use",
        "Related Slide Decks": "Connections",
        "Related Scheduled Sessions": "Connections",
        "Related People": "Connections",
        "Related Companies": "Connections",
        "Related Companies And Tools": "Connections",
        "Related Resources": "Connections",
        "Related Topics": "Connections",
        "Related Pages": "Connections",
        "Highlighted Paths": "Connections",
        "Transcript And Resource Support": "Evidence Graph",
        "Source-Derived Enrichment": "Evidence Graph",
        "Evidence Table": "Source Coverage",
        "Representative Evidence Links": "Source Coverage",
    },
    "questions": {
        "Why This Question Matters": "Context",
        "Current Working Answer": "Working Answer",
        "Source Evidence": "Evidence",
        "Follow-Up": "Next Questions",
    },
    "harnesses": {
        "Purpose": "Overview",
        "Observed At AIE": "Conference Context",
        "Recommended Implementation Steps": "Implementation Pattern",
        "Source Evidence": "Evidence",
    },
    "playbooks": {
        "Purpose": "Overview",
        "Recommended Implementation Steps": "Implementation Pattern",
        "Source Evidence": "Evidence",
    },
    "evaluations": {
        "Purpose": "Overview",
        "Recommended Implementation Steps": "Implementation Pattern",
        "Source Evidence": "Evidence",
    },
}

ORDER: dict[str, list[str]] = {
    "talks": [
        "Significance",
        "Conference Context",
        "Session Description",
        "Recording Search Status",
        "Technical Pattern",
        "Applied Pattern",
        "Conference Sessions",
        "Media Evidence",
        "Connections",
        "Sources",
        "Evidence Graph",
        "Evidence Boundary",
    ],
    "people": [
        "Profile",
        "Conference Relevance",
        "Biography",
        "Conference Sessions",
        "Media Evidence",
        "Connections",
        "Sources",
        "Evidence Graph",
        "Evidence Boundary",
    ],
    "companies": [
        "Overview",
        "Background",
        "Conference Relevance",
        "Conference Sessions",
        "Connections",
        "Sources",
        "Evidence Graph",
        "Notes",
        "Evidence Boundary",
    ],
    "topics": [
        "Overview",
        "Conference Context",
        "How This Theme Evolved",
        "Significance",
        "Why This Matters Now",
        "Technical Model",
        "Applied Use",
        "Practical Lesson",
        "Design Patterns",
        "Risks And Failure Modes",
        "Open Questions",
        "Connections",
        "Evidence Graph",
        "Source Coverage",
        "Evidence Boundary",
    ],
    "questions": ["Context", "How This Theme Evolved", "Why This Matters Now", "Working Answer", "Practical Lesson", "Evidence", "Next Questions", "Evidence Boundary"],
    "harnesses": ["Overview", "Conference Context", "How This Theme Evolved", "Why This Matters Now", "Implementation Pattern", "Practical Lesson", "Evidence", "Evidence Boundary"],
    "playbooks": ["Overview", "Conference Context", "How This Theme Evolved", "Why This Matters Now", "Implementation Pattern", "Practical Lesson", "Evidence", "Evidence Boundary"],
    "evaluations": ["Overview", "Conference Context", "How This Theme Evolved", "Why This Matters Now", "Implementation Pattern", "Practical Lesson", "Evidence", "Evidence Boundary"],
}

TARGET_DIRS = ["talks", "people", "companies", "topics", "questions", "harnesses", "playbooks", "evaluations"]
WRITER_CONTRACT = {
    "writer_id": "normalize-article-shapes",
    "scope": "whole_page",
    "owned_output_keys": [],
    "incremental_safe": False,
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    return text[: end + 5], text[end + 5 :].lstrip()


def split_h1(content: str, fallback_title: str) -> tuple[str, str]:
    match = re.match(r"(# .+?\n)(.*)\Z", content, flags=re.S)
    if match:
        return match.group(1).rstrip(), match.group(2).lstrip()
    return f"# {fallback_title}", content


def parse_sections(rest: str) -> tuple[str, list[tuple[str, str]]]:
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", rest, flags=re.M))
    if not matches:
        return rest.strip(), []
    lead = rest[: matches[0].start()].strip()
    sections: list[tuple[str, str]] = []
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(rest)
        sections.append((match.group(1).strip(), rest[start:end].strip()))
    return lead, sections


def normalize_subheadings(body: str) -> str:
    replacements = {
        "Source Signals": "Media Signals",
        "Slide And Transcript Signals": "Media Signals",
        "Talk Evidence": "Linked Sessions",
        "Related Sessions": "Linked Sessions",
        "Article Use": "Agent Reading Notes",
    }
    for old, new in replacements.items():
        body = re.sub(rf"^###\s+{re.escape(old)}\s*$", f"### {new}", body, flags=re.M)
    body = body.replace(
        "This section is generated from all currently linked source material for the article:",
        "This evidence graph is generated from currently linked source material:",
    )
    body = body.replace(
        "This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.",
        "This evidence graph consolidates scheduled talks, linked videos, transcripts, and slide-derived material connected to this topic.",
    )
    body = body.replace(
        "This section summarizes how this person appears across the conference source graph:",
        "This evidence graph summarizes how this person appears across the conference source graph:",
    )
    body = body.replace(
        "This section summarizes how this organization appears across the conference source graph:",
        "This evidence graph summarizes how this organization appears across the conference source graph:",
    )
    body = body.replace(
        "Use these source signals to refine the synopsis, topic links, people/company context, and method notes.",
        "Use these signals to refine the synopsis, topic links, people/company context, and method notes.",
    )
    return body.strip()


def merge_sections(kind: str, sections: list[tuple[str, str]]) -> OrderedDict[str, list[str]]:
    aliases = ALIASES.get(kind, {})
    merged: OrderedDict[str, list[str]] = OrderedDict()
    for heading, body in sections:
        canonical = aliases.get(heading, heading)
        body = normalize_subheadings(body)
        if not body:
            continue
        merged.setdefault(canonical, [])
        if body not in merged[canonical]:
            merged[canonical].append(body)
    return merged


def dedupe_lines(body: str) -> str:
    out: list[str] = []
    seen_bullets: set[str] = set()
    for line in body.splitlines():
        key = ""
        stripped = line.strip()
        if stripped.startswith("- ") or stripped.startswith("|"):
            key = re.sub(r"\s+", " ", stripped.lower())
        if key and key in seen_bullets:
            continue
        if key:
            seen_bullets.add(key)
        out.append(line.rstrip())
    return "\n".join(out).strip()


def compact_join(parts: list[str]) -> str:
    cleaned = [dedupe_lines(part) for part in parts if part.strip()]
    return "\n\n".join(cleaned).strip()


def ordered_sections(kind: str, merged: OrderedDict[str, list[str]]) -> list[tuple[str, str]]:
    emitted: set[str] = set()
    output: list[tuple[str, str]] = []
    for heading in ORDER.get(kind, []):
        if heading in merged:
            output.append((heading, compact_join(merged[heading])))
            emitted.add(heading)
    for heading, bodies in merged.items():
        if heading not in emitted:
            output.append((heading, compact_join(bodies)))
    return output


def normalize_page(path: Path, kind: str, *, write_changes: bool = True) -> bool:
    original = read(path)
    fm, content = split_frontmatter(original)
    h1, rest = split_h1(content, path.stem.replace("-", " ").title())
    lead, sections = parse_sections(rest)
    if not sections:
        return False
    merged = merge_sections(kind, sections)
    ordered = ordered_sections(kind, merged)
    blocks = [h1]
    if lead:
        blocks.append(lead)
    for heading, body in ordered:
        if not body:
            continue
        blocks.append(f"## {heading}\n{body}")
    normalized = fm + "\n\n".join(blocks).rstrip() + "\n"
    if normalized != original:
        if write_changes:
            write(path, normalized)
        return True
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--kind", action="append", choices=TARGET_DIRS)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)

    kinds = args.kind or TARGET_DIRS
    counts = defaultdict(int)
    changed_paths: list[str] = []
    for kind in kinds:
        for path in sorted((WIKI / kind).glob("*.md")):
            if path.name in {"index.md"}:
                continue
            changed = normalize_page(path, kind, write_changes=not args.check)
            if changed:
                counts[kind] += 1
                changed_paths.append(str(path.relative_to(ROOT)))
    result = {"changed": dict(counts), "changed_paths": changed_paths[:50], "total_changed": len(changed_paths)}
    print(json.dumps(result, indent=2, sort_keys=True))
    if args.check and changed_paths:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
