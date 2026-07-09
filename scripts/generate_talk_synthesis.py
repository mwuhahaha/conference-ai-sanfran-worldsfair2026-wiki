#!/usr/bin/env python3
"""Add transcript/source-backed synthesis sections to talk pages."""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw" / "sources"
TRANSCRIPT_DIRS = [
    RAW / "youtube-transcripts",
    RAW / "external-youtube-transcripts",
    RAW / "youtube-livestream-transcripts",
]

TOPIC_KEYWORDS = {
    "agentic-web": ["agentic web", "web for agents", "agent-ready", "agent readiness", "nearly headless", "webmcp", "browser", "homepage", "docs"],
    "mcp": ["mcp", "model context protocol", "mcp server", "mcp host"],
    "mcp-apps": ["mcp apps", "mcp ui", "interactive ui", "agentic app runtime", "sep-1865"],
    "agentic-search": ["search", "retrieval", "discover", "finding", "docs", "homepage"],
    "agent-security": ["auth", "authenticate", "permission", "safe", "trust", "control"],
    "coding-agents": ["claude code", "coding agent", "developer", "code"],
    "ai-sandboxes": ["sandbox", "browser", "execution"],
}

NOVEL_CONCEPTS = [
    {
        "slug": "reachability-over-format",
        "title": "Reachability Over Format",
        "patterns": ["format isn't the key", "reachability is", "linked properly", "usage jumps"],
        "summary": "Agent-facing files and specs matter less than whether agents can actually find and reach them from the surfaces they use.",
    },
    {
        "slug": "nearly-headless-web",
        "title": "Nearly Headless Web",
        "patterns": ["nearly headless", "never be completely headless", "human eye at the end"],
        "summary": "The web moves toward machine-operable surfaces while preserving human-visible moments for choice, review, and judgment.",
    },
    {
        "slug": "agent-ready-accessibility",
        "title": "Agent-Ready Accessibility",
        "patterns": ["agent-ready", "accessible", "same engineering problem"],
        "summary": "Designing for agents and designing for accessibility converge around explicit structure, reachable controls, and understandable state.",
    },
    {
        "slug": "mcp-app-runtime",
        "title": "MCP Apps As Agentic App Runtime",
        "patterns": ["agentic app runtime", "mcp apps", "interactive experiences", "official extension"],
        "summary": "MCP Apps treats interactive UI returned from MCP servers as a runtime layer for agent-facing software.",
    },
]


def load_json(path: Path, fallback):
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def split_frontmatter(text: str) -> tuple[str, str, dict[str, str]]:
    if not text.startswith("---\n"):
        return "", text, {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text, {}
    raw_fm = text[: end + 5]
    body = text[end + 5 :].lstrip()
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return raw_fm, body, fields


def upsert_section(markdown: str, heading: str, section: str) -> str:
    fm, body, _fields = split_frontmatter(markdown)
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    replacement = f"## {heading}\n{section.strip()}\n"
    if pattern.search(body):
        body = pattern.sub(replacement, body).rstrip() + "\n"
    else:
        body = body.rstrip() + "\n\n" + replacement
    return fm + body


def video_ids(text: str) -> list[str]:
    ids = set(re.findall(r"(?:watch\?v=|youtu\.be/)([A-Za-z0-9_-]{11})", text))
    ids.update(re.findall(r"youtube-([A-Za-z0-9_-]{11})(?=[\]\)\s/#-]|$)", text))
    return sorted(ids)


def transcript_for(video_id: str) -> tuple[Path | None, str]:
    for folder in TRANSCRIPT_DIRS:
        path = folder / f"{video_id}.txt"
        if path.exists():
            return path, path.read_text(encoding="utf-8", errors="ignore")
    return None, ""


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-") or "untitled"


def parse_people_companies() -> tuple[dict[str, dict], dict[str, str]]:
    speakers = load_json(RAW / "official-speakers.json", {}).get("speakers", [])
    by_name = {item.get("name"): item for item in speakers if item.get("name")}
    company_slug = {item.get("company"): slugify(item.get("company", "")) for item in speakers if item.get("company")}
    return by_name, company_slug


def list_from_frontmatter(value: str) -> list[str]:
    if not value:
        return []
    return re.findall(r'"([^"]+)"', value) or [part.strip() for part in value.strip("[]").split(",") if part.strip()]


def first_sentences(text: str, count: int = 3) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    clean = re.sub(r"(?i)\[(?:music|applause|laughter)\]", " ", clean)
    clean = re.sub(r"(?:&gt;&gt;|>>)\s*", " ", clean)
    sentences = re.split(r"(?<=[.!?])\s+", clean)
    return " ".join(sentences[:count]).strip()


def curated_synopsis(title: str, blob: str) -> str:
    low_title = title.lower()
    low_blob = blob.lower()
    if "rebuilding the web for agents" in low_title:
        return (
            "This talk argues that AI apps are becoming the new browsers, so the web has to be designed for agents as operators, not only for human readers. "
            "It breaks agentic-web readiness into the whole journey of discovery, understanding, authentication, action, and human handoff. "
            "The key finding is reachability over format: agent-facing files and specs only help when agents can actually find them from trusted surfaces such as docs and homepages. "
            "The resulting design frame is a nearly headless web, where agents handle most execution while human-visible checkpoints remain available for judgment, comparison, and consent."
        )
    if "mcp apps" in low_title and "extending" in low_title:
        return (
            "This talk frames MCP Apps as the interactive application runtime for agentic software. "
            "Instead of MCP servers returning only structured tool data or text, MCP Apps lets servers return UI views inside MCP hosts so models get actionable context and humans get usable controls. "
            "The session connects MCP UI, the MCP Apps extension, SEP-1865, host integration, real-world use cases, and the move from chat responses toward agentic applications. "
            "Its practical method is to separate model-operable data from human-operable interface while keeping both inside the same MCP interaction."
        )
    if "reachability is" in low_blob and "agent-ready" in low_blob:
        return (
            "The session centers on agent-readiness as an operability problem: agents must be able to discover the right surface, understand it, authenticate, act, and hand work back to a human. "
            "The most important pattern is making authoritative guidance reachable from places agents already trust, then using protocols and UI only where they reduce friction."
        )
    if "mcp apps" in low_blob and ("interactive" in low_blob or "sep-1865" in low_blob):
        return (
            "The session explains MCP Apps as a way to add interactive UI to MCP-based workflows. "
            "It treats the MCP host as the place where tool data, model reasoning, and human controls meet."
        )
    return ""


def detect_topics(blob: str) -> list[str]:
    low = blob.lower()
    found = []
    for slug, patterns in TOPIC_KEYWORDS.items():
        page_exists = (WIKI / "topics" / f"{slug}.md").exists() or (WIKI / "tools" / f"{slug}.md").exists()
        if any(pattern in low for pattern in patterns) and page_exists:
            found.append(slug)
    return sorted(set(found))


def detect_concepts(blob: str) -> list[dict]:
    low = blob.lower()
    hits = []
    for concept in NOVEL_CONCEPTS:
        if any(pattern in low for pattern in concept["patterns"]):
            hits.append(concept)
    return hits


def section_for(path: Path, text: str, people: dict[str, dict], company_slugs: dict[str, str]) -> tuple[str, list[dict]]:
    _fm, body, fields = split_frontmatter(text)
    title = fields.get("title") or path.stem.replace("-", " ").title()
    speakers = list_from_frontmatter(fields.get("speakers", ""))
    ids = video_ids(text)
    transcripts = []
    transcript_text = ""
    for video_id in ids:
        tpath, ttext = transcript_for(video_id)
        if tpath and ttext:
            transcripts.append((video_id, tpath, len(ttext.split())))
            transcript_text += "\n" + ttext
    source_blob = title + "\n" + body + "\n" + transcript_text
    topics = detect_topics(source_blob)
    concepts = detect_concepts(source_blob)
    speaker_lines = []
    for speaker in speakers:
        info = people.get(speaker, {})
        role = info.get("role") or "role not listed"
        company = info.get("company") or "company not listed"
        company_slug = company_slugs.get(company)
        company_link = f"[[{company_slug}|{company}]]" if company_slug and (WIKI / "companies" / f"{company_slug}.md").exists() else company
        speaker_lines.append(f"- [[{slugify(speaker)}|{speaker}]] — {role} at {company_link}.")
    if not speaker_lines:
        speaker_lines.append("- No speaker profile is attached in the official schedule data.")

    summary_basis = transcript_text or body
    synopsis = curated_synopsis(title, source_blob) or first_sentences(summary_basis, 4)
    if not synopsis:
        synopsis = "No transcript-backed synthesis is available yet; this page currently relies on official schedule context."

    lines = [
        "### Synthesized Breakdown",
        synopsis,
        "",
        "### Speaker And Company Context",
        *speaker_lines,
        "",
        "### Topics Covered",
    ]
    if topics:
        for topic in topics:
            lines.append(f"- [[{topic}]]")
    else:
        lines.append("- Topic links are pending transcript-backed classification.")
    lines.extend(["", "### Derived Links And Source Material"])
    if transcripts:
        for video_id, tpath, words in transcripts:
            lines.append(f"- [[youtube-{video_id}-transcript]] — transcript markdown; source cache `{tpath.relative_to(ROOT)}` ({words:,} words).")
    for video_id in ids:
        if (WIKI / "resources" / f"youtube-{video_id}.md").exists():
            lines.append(f"- [[youtube-{video_id}]] — related YouTube source page.")
        for suffix in ["slides", "reconstructed-slides", "dense-slides"]:
            if (WIKI / "slides" / f"youtube-{video_id}-{suffix}.md").exists():
                lines.append(f"- [[youtube-{video_id}-{suffix}]] — slide evidence.")
    lines.extend(["", "### Novel Concepts / Clever Methods"])
    if concepts:
        for concept in concepts:
            lines.append(f"- [[{concept['slug']}|{concept['title']}]] — {concept['summary']}")
    else:
        lines.append("- No highlighted novel concept has been detected yet.")
    lines.extend(["", "### Evidence Boundary"])
    if transcripts:
        lines.append("This synthesis uses the official schedule plus cached video transcripts. Official AI Engineer World's Fair San Francisco 2026 livestreams and cut videos are primary event video sources for transcript/slide evidence; external, historical, or speaker-matched videos remain supporting context unless manually verified as exact official event recordings.")
    else:
        lines.append("This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.")
    return "\n".join(lines), concepts


def write_registry(category: str) -> None:
    rows = []
    for p in sorted((WIKI / category).glob("*.md")):
        if p.name == "index.md":
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        _fm, _body, fields = split_frontmatter(text)
        title = fields.get("title") or p.stem.replace("-", " ").title()
        rows.append({"id": p.stem, "title": title, "path": str(p.relative_to(ROOT))})
    (WIKI / category / "registry.json").write_text(json.dumps(sorted(rows, key=lambda r: r["title"].lower()), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--speaker", action="append", help="Only update talks containing this speaker. Repeatable.")
    parser.add_argument("--all", action="store_true", help="Update every talk with source context.")
    args = parser.parse_args()

    people, companies = parse_people_companies()
    wanted = {s.lower() for s in (args.speaker or [])}
    updated = 0
    concept_hits = defaultdict(int)
    for path in sorted((WIKI / "talks").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        _fm, _body, fields = split_frontmatter(text)
        speakers = [s.lower() for s in list_from_frontmatter(fields.get("speakers", ""))]
        if wanted and not any(s in wanted for s in speakers):
            continue
        if not args.all and not wanted:
            continue
        section, concepts = section_for(path, text, people, companies)
        new_text = upsert_section(text, "Synthesis", section)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
        for concept in concepts:
            concept_hits[concept["slug"]] += 1
    print(json.dumps({"talks_updated": updated, "concept_hits": dict(concept_hits)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
