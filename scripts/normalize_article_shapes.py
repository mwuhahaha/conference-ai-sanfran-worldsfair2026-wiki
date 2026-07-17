#!/usr/bin/env python3
"""Normalize WF26 articles through reusable, fence-aware maker contracts.

This adapter defines the event-specific category and resource-subtype schemas.
The parser and whole-section normalizer live in ``wiki-from-topic-maker`` so
future event wikis can supply their own registry without copying Markdown
rewriting logic.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from wiki_from_topic_maker.article_shapes import (
    ArticleContract,
    ArticleContractCheck,
    ArticleContractRegistry,
    ArticleSection,
    normalize_article_contract,
)


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
TARGET_DIRS = [
    "talks",
    "people",
    "companies",
    "topics",
    "tools",
    "questions",
    "patterns",
    "harnesses",
    "playbooks",
    "evaluations",
    "resources",
]
WRITER_CONTRACT = {
    "writer_id": "normalize-article-shapes",
    "scope": "whole_page",
    "owned_output_keys": [],
    "incremental_safe": False,
}


def section(
    key: str,
    heading: str,
    *aliases: str,
    required: bool = False,
    terminal: bool = False,
    duplicate_merge: str = "preserve",
) -> ArticleSection:
    return ArticleSection(
        key=key,
        heading=heading,
        aliases=tuple(aliases),
        min_count=1 if required else 0,
        terminal=terminal,
        duplicate_merge=duplicate_merge,
    )


def contract(
    category: str,
    schema_id: str,
    sections: list[ArticleSection],
    *,
    subtype: str | None = None,
) -> ArticleContract:
    return ArticleContract(
        schema_id=schema_id,
        category=category,
        subtype=subtype,
        sections=tuple(sections),
    )


WF26_ARTICLE_CONTRACTS = ArticleContractRegistry(
    (
        contract(
            "talks",
            "wf26/talk-v2",
            [
                section("conference_context", "Conference Context", required=True),
                section("session_description", "Session Description", required=True),
                section("summary", "Summary"),
                section("synthesis", "Synthesis"),
                section(
                    "secondary_interview",
                    "Secondary Interview Context",
                ),
                section("significance", "Significance"),
                section("recording_search", "Recording Search Status"),
                section("technical_pattern", "Technical Pattern"),
                section("applied_pattern", "Applied Pattern"),
                section("people", "People"),
                section("slide_evidence", "Slide Evidence"),
                section("official_recording", "Official YouTube Recording"),
                section("livestream_segment", "Livestream Segment"),
                section(
                    "external_media",
                    "External Secondary Source Candidates",
                ),
                section(
                    "media_evidence",
                    "Media Evidence",
                    "Supporting Slides",
                    "Slides",
                    required=True,
                    duplicate_merge="append",
                ),
                section("transcript_status", "Transcript Status"),
                section("transcript_markdown", "Transcript Markdown"),
                section("attendance", "Attendance Visibility"),
                section("connections", "Connections"),
                section("sources", "Sources"),
                section("evidence_graph", "Evidence Graph", required=True),
                section("notes", "Notes"),
                section(
                    "evidence_boundary",
                    "Evidence Boundary",
                    terminal=True,
                ),
            ],
        ),
        contract(
            "people",
            "wf26/person-v2",
            [
                section("profile", "Profile", required=True),
                section("who", "Who They Are"),
                section("biography", "Biography"),
                section("background", "Background"),
                section("relevance", "Conference Relevance", "Why Highlighted"),
                section("thesis", "Agentic Web Thesis"),
                section("ora_context", "ORA Context"),
                section("sessions", "Conference Sessions"),
                section("livestream", "Livestream Appearances"),
                section("media", "Media Evidence"),
                section("source_pages", "Related Source Pages"),
                section("organizations", "Related Organizations"),
                section("people", "Related People"),
                section("source_material", "Related Source Material"),
                section("connections", "Connections"),
                section("evidence_graph", "Evidence Graph", required=True),
                section(
                    "evidence_boundary",
                    "Evidence Boundary",
                    terminal=True,
                ),
            ],
        ),
        contract(
            "companies",
            "wf26/company-v2",
            [
                section("overview", "Overview", "What It Is", required=True),
                section("background", "Background", "Origin And Context"),
                section("public_company", "Public Company Context"),
                section("operating_model", "Operating Model Signals"),
                section("public_research", "Public Research Context"),
                section(
                    "relevance",
                    "Conference Relevance",
                    "Why It Matters At World's Fair",
                    required=True,
                ),
                section(
                    "sessions",
                    "Conference Sessions",
                    "Related Scheduled Sessions",
                ),
                section(
                    "connections",
                    "Connections",
                    "Related People",
                    required=True,
                ),
                section("source_pages", "Related Source Pages"),
                section("topics_tools", "Related Topics And Tools"),
                section("organizations", "Related Organizations"),
                section("sources", "Sources", "Public Sources", required=True),
                section("notes", "Notes"),
                section("evidence_graph", "Evidence Graph", required=True),
                section(
                    "evidence_boundary",
                    "Evidence Boundary",
                    required=True,
                    terminal=True,
                ),
            ],
        ),
        contract(
            "topics",
            "wf26/topic-v2",
            [
                section("overview", "Overview"),
                section("conference_context", "Conference Context"),
                section("evolution", "How This Theme Evolved"),
                section("significance", "Significance", required=True),
                section("why_now", "Why This Matters Now"),
                section("technical_model", "Technical Model"),
                section("applied_use", "Applied Use", required=True),
                section("active_use_cases", "Active Use Cases"),
                section("design_patterns", "Design Patterns"),
                section("practical_lesson", "Practical Lesson"),
                section("risks", "Risks And Failure Modes"),
                section("open_questions", "Open Questions"),
                section("livestream", "Livestream Source"),
                section("scheduled_signals", "Slide-Derived Scheduled Session Signals"),
                section("supporting_decks", "Slide-Derived Supporting Decks"),
                section("neighboring", "Neighboring Subjects"),
                section("connections", "Connections", required=True),
                section("source_coverage", "Source Coverage"),
                section("evidence_graph", "Evidence Graph", required=True),
                section(
                    "evidence_boundary",
                    "Evidence Boundary",
                    terminal=True,
                ),
            ],
        ),
        contract(
            "tools",
            "wf26/tool-v2",
            [
                section("overview", "Overview", "What It Is"),
                section(
                    "conference_context",
                    "Conference Context",
                    "Why It Belongs",
                    "Why It Matters At World's Fair",
                    "Why It Appears In This Wiki",
                ),
                section("capabilities", "Capabilities", "Important Capabilities"),
                section("applied_use", "Applied Use", "How To Use It"),
                section("use_cases", "Effective Use Cases"),
                section("guardrails", "Operating Tricks And Guardrails"),
                section("alternative", "Alternative Implementation"),
                section("schedule", "Related Scheduled Sessions", "Official Schedule"),
                section("maintainer", "Maintainer"),
                section("comparison", "Comparison Context"),
                section("connections", "Connections", "Related Pages"),
                section("evidence", "Confirmed Evidence"),
                section("sources", "Sources", "Public Sources"),
                section("confidence", "Confidence"),
                section(
                    "evidence_boundary",
                    "Evidence Boundary",
                    "Source Boundary",
                    terminal=True,
                ),
            ],
        ),
        contract(
            "questions",
            "wf26/question-v2",
            [
                section("context", "Context", required=True),
                section("working_answer", "Working Answer", required=True),
                section("evidence", "Evidence", required=True),
                section("confidence", "Confidence"),
                section("next_questions", "Next Questions", required=True),
                section("evidence_boundary", "Evidence Boundary", terminal=True),
            ],
        ),
        contract(
            "patterns",
            "wf26/pattern-v2",
            [
                section("pattern", "Pattern", required=True),
                section("when", "When To Use", required=True),
                section("moves", "Implementation Moves", required=True),
                section("evidence", "Source Evidence", required=True),
                section(
                    "evidence_boundary",
                    "Evidence Boundary",
                    required=True,
                    terminal=True,
                ),
            ],
        ),
        contract(
            "harnesses",
            "wf26/harness-v2",
            [
                section("overview", "Overview", "Purpose", required=True),
                section(
                    "context",
                    "Conference Context",
                    "Observed At AIE",
                    required=True,
                ),
                section(
                    "implementation",
                    "Implementation Pattern",
                    "Recommended Implementation Steps",
                    required=True,
                ),
                section("evidence", "Evidence", "Source Evidence", required=True),
                section(
                    "evidence_boundary",
                    "Evidence Boundary",
                    required=True,
                    terminal=True,
                ),
            ],
        ),
        contract(
            "playbooks",
            "wf26/playbook-v2",
            [
                section("overview", "Overview", "Purpose", required=True),
                section("when", "When To Use", required=True),
                section("steps", "Steps", required=True),
                section("evidence", "Evidence", "Source Evidence", required=True),
                section(
                    "evidence_boundary",
                    "Evidence Boundary",
                    required=True,
                    terminal=True,
                ),
            ],
        ),
        contract(
            "evaluations",
            "wf26/evaluation-v2",
            [
                section("question", "Decision Question", required=True),
                section("criteria", "Criteria", required=True),
                section("evidence", "Evidence", "Source Evidence", required=True),
                section("recommendation", "Tentative Recommendation", required=True),
                section("confidence", "Confidence", required=True),
                section("open_questions", "Open Questions", required=True),
                section("evidence_boundary", "Evidence Boundary", terminal=True),
            ],
        ),
        contract(
            "resources",
            "wf26/video-source-v2",
            [
                section("what", "What It Is", "Source"),
                section("classification", "Source Classification"),
                section(
                    "event_relationship",
                    "Relationship To World's Fair 2026",
                    "Matched Schedule Pages",
                    "Related Scheduled Sessions",
                ),
                section("related_pages", "Related Pages"),
                section("topic_signals", "Topic Signals"),
                section("transcript_status", "Transcript Status", "Transcript Availability"),
                section("cached_transcript", "Cached Transcript"),
                section("local_cache", "Local Cache"),
                section("slides", "Extracted Slides"),
                section("transcript_markdown", "Transcript Markdown"),
                section("link", "Link"),
                section(
                    "evidence_boundary",
                    "Evidence Boundary",
                    terminal=True,
                ),
            ],
            subtype="video-source",
        ),
    )
)


def contract_for(path: Path, kind: str) -> ArticleContract | None:
    if kind == "resources":
        if not path.name.startswith("youtube-"):
            return None
        return WF26_ARTICLE_CONTRACTS.resolve(kind, "video-source")
    return WF26_ARTICLE_CONTRACTS.resolve(kind)


def is_index_page(path: Path, kind: str) -> bool:
    return path.stem.casefold() in {"index", kind.casefold()}


def normalize_page(
    path: Path,
    kind: str,
    *,
    write_changes: bool = True,
) -> bool:
    selected = contract_for(path, kind)
    if selected is None or is_index_page(path, kind):
        return False
    original = path.read_text(encoding="utf-8", errors="ignore")
    normalized = normalize_article_contract(original, selected)
    if normalized.changed and write_changes:
        path.write_text(normalized.text, encoding="utf-8")
    return normalized.changed


def inspect_page(path: Path, kind: str) -> tuple[bool, ArticleContractCheck | None]:
    selected = contract_for(path, kind)
    if selected is None or is_index_page(path, kind):
        return False, None
    original = path.read_text(encoding="utf-8", errors="ignore")
    normalized = normalize_article_contract(original, selected)
    return normalized.changed, normalized.check_after


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--kind", action="append", choices=TARGET_DIRS)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)

    kinds = args.kind or TARGET_DIRS
    changed_counts: Counter[str] = Counter()
    changed_paths: list[str] = []
    issue_counts: Counter[str] = Counter()
    issues: list[dict[str, object]] = []

    for kind in kinds:
        for path in sorted((WIKI / kind).glob("*.md")):
            selected = contract_for(path, kind)
            if selected is None or is_index_page(path, kind):
                continue
            original = path.read_text(encoding="utf-8", errors="ignore")
            normalized = normalize_article_contract(original, selected)
            if normalized.changed:
                changed_counts[kind] += 1
                changed_paths.append(str(path.relative_to(ROOT)))
                if not args.check:
                    path.write_text(normalized.text, encoding="utf-8")
            for issue in normalized.check_after.issues:
                issue_counts[issue.code] += 1
                issues.append(
                    {
                        "path": str(path.relative_to(ROOT)),
                        "schema": selected.schema_id,
                        "code": issue.code,
                        "severity": issue.severity,
                        "heading": issue.heading,
                        "line": issue.line,
                    }
                )

    result = {
        "changed": dict(sorted(changed_counts.items())),
        "changed_paths": changed_paths[:100],
        "total_changed": len(changed_paths),
        "issue_counts": dict(sorted(issue_counts.items())),
        "issues": issues[:100],
        "total_issues": len(issues),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    has_errors = any(item["severity"] == "error" for item in issues)
    if has_errors or (args.check and (changed_paths or issues)):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
