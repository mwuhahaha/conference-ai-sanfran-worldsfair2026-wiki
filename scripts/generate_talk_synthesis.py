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
OFFICIAL_VIDEO_MANIFEST = RAW / "official-wf26-video-manifest.json"
PLAYABLE_VIDEO_AVAILABILITIES = {"", "public", "unlisted"}
PLAYABLE_PLAYLIST_AVAILABILITIES = {"", "available"}
TRANSCRIPT_DIRS = [
    RAW / "youtube-transcripts",
    RAW / "external-youtube-transcripts",
    RAW / "youtube-livestream-transcripts",
]

TOPIC_KEYWORDS = {
    "agent-memory": [
        "company brain",
        "context engineering",
        "memory hygiene",
        "working memory",
    ],
    "agentic-web": ["agentic web", "web for agents", "agent-ready", "agent readiness", "nearly headless", "webmcp", "browser", "homepage", "docs"],
    "mcp": ["mcp", "model context protocol", "mcp server", "mcp host"],
    "mcp-apps": ["mcp apps", "mcp ui", "interactive ui", "agentic app runtime", "sep-1865"],
    "agentic-search": ["search", "retrieval", "discover", "finding", "docs", "homepage"],
    "agent-security": ["auth", "authenticate", "permission", "safe", "trust", "control"],
    "coding-agents": ["claude code", "coding agent", "developer", "code"],
    "ai-sandboxes": [
        "sandbox",
        "sandboxed",
        "isolated execution",
        "execution isolation",
        "isolated browser",
    ],
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


def remove_generated_section(markdown: str, heading: str, marker: str) -> str:
    fm, body, _fields = split_frontmatter(markdown)
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    match = pattern.search(body)
    if not match or marker not in match.group(0):
        return markdown
    body = pattern.sub("", body).rstrip() + "\n"
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


def official_manifest_videos() -> list[dict]:
    data = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    videos = data.get("videos", []) if isinstance(data, dict) else []
    if not isinstance(videos, list):
        raise ValueError("official WF26 video manifest must contain a videos array")
    return [item for item in videos if isinstance(item, dict)]


def manifest_row_is_playable(item: dict) -> bool:
    return (
        str(item.get("videoAvailability") or "").casefold()
        in PLAYABLE_VIDEO_AVAILABILITIES
        and str(item.get("playlistAvailability") or "").casefold()
        in PLAYABLE_PLAYLIST_AVAILABILITIES
    )


def official_manifest_video_ids() -> set[str]:
    return {
        str(item["id"])
        for item in official_manifest_videos()
        if isinstance(item.get("id"), str)
    }


def official_recording_ids_by_talk() -> dict[str, list[str]]:
    videos = official_manifest_videos()

    recordings: dict[str, list[str]] = {}
    ordered = sorted(
        videos,
        key=lambda item: (
            int(item.get("playlistIndex") or 1_000_000),
            str(item.get("id") or ""),
        ),
    )
    for item in ordered:
        video_id = item.get("id")
        if not isinstance(video_id, str) or item.get("mediaType") != "talk_recording":
            continue
        if not manifest_row_is_playable(item):
            continue
        matched_talks = item.get("matchedTalks")
        if not isinstance(matched_talks, list):
            continue
        for talk_id in matched_talks:
            if isinstance(talk_id, str) and talk_id:
                recordings.setdefault(talk_id, []).append(video_id)
    return recordings


def broad_event_video_ids() -> set[str]:
    return {
        str(item.get("id"))
        for item in official_manifest_videos()
        if item.get("id")
        and item.get("mediaType")
        in {"event_livestream", "scheduled_premiere", "unavailable_playlist_item"}
    }


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
    # Generated summaries must never ingest Markdown structure as prose. The
    # previous fallback collapsed an entire page, including its H1/H2 headings,
    # into one line inside the Synthesis section.
    clean = re.sub(r"```.*?```|~~~.*?~~~", " ", text, flags=re.S)
    clean = re.sub(r"^#{1,6}\s+.*$", " ", clean, flags=re.M)
    clean = re.sub(r"!\[\[[^\]]+\]\]", " ", clean)
    clean = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", clean)
    clean = re.sub(r"\[\[([^\]]+)\]\]", r"\1", clean)
    clean = re.sub(r"^\s*[-*+]\s+", "", clean, flags=re.M)
    clean = re.sub(r"\s+", " ", clean).strip()
    clean = re.sub(r"(?i)\[(?:music|applause|laughter)\]", " ", clean)
    clean = re.sub(r"(?:&gt;&gt;|>>)\s*", " ", clean)
    sentences = re.split(r"(?<=[.!?])\s+", clean)
    return " ".join(sentences[:count]).strip()


def section_body(markdown: str, heading: str) -> str:
    match = re.search(
        rf"^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)",
        markdown,
        flags=re.M | re.S,
    )
    return match.group(1).strip() if match else ""


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
    if (
        "a skill file is an employee" in low_blob
        and "the library plus the librarian" in low_blob
        and "memory plus hygiene" in low_blob
    ):
        return (
            "The session argues that the leverage in AI-native organizations comes from how work is wired, not from model access alone. "
            "It maps skill files, resolver tables, filing rules, and trigger evaluations to organizational roles and controls, treating agents as a managed workforce rather than autocomplete. "
            "It separates judgment and interpretation in latent space from reliable state and calculation in deterministic systems, then defines a company brain as a curated library plus the librarian that selects the right context. "
            "The practical discipline is to preserve provenance, contradiction checks, and active pruning, and to turn successful one-off work into reusable skills so organizational knowledge compounds."
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


def section_for(
    path: Path,
    text: str,
    people: dict[str, dict],
    company_slugs: dict[str, str],
    matched_recordings: dict[str, list[str]] | None = None,
) -> tuple[str, str, list[dict]]:
    _fm, body, fields = split_frontmatter(text)
    title = fields.get("title") or path.stem.replace("-", " ").title()
    speakers = list_from_frontmatter(fields.get("speakers", ""))
    recording_map = (
        matched_recordings
        if matched_recordings is not None
        else official_recording_ids_by_talk()
    )
    dedicated_ids = recording_map.get(path.stem, [])
    manifest_ids = official_manifest_video_ids() | broad_event_video_ids()
    ids = list(
        dict.fromkeys(
            [
                *dedicated_ids,
                *(
                    video_id
                    for video_id in video_ids(text)
                    if video_id not in manifest_ids
                ),
            ]
        )
    )
    transcripts = []
    for video_id in ids:
        tpath, ttext = transcript_for(video_id)
        if tpath and ttext:
            if video_id in dedicated_ids:
                source_kind = "dedicated"
            elif tpath.parent.name == "youtube-livestream-transcripts":
                source_kind = "livestream"
            elif tpath.parent.name == "external-youtube-transcripts":
                source_kind = "external"
            else:
                source_kind = "official"
            transcripts.append(
                (video_id, tpath, len(ttext.split()), source_kind, ttext)
            )
    priority = {"dedicated": 0, "official": 1, "livestream": 2, "external": 3}
    transcripts.sort(key=lambda item: (priority[item[3]], item[0]))
    preferred = [item for item in transcripts if item[3] == "dedicated"]
    external_only = (
        not preferred
        and bool(transcripts)
        and all(item[3] == "external" for item in transcripts)
    )
    if external_only:
        preferred = [item for item in transcripts if item[3] == "external"]
    transcript_text = "\n".join(item[4] for item in preferred)
    description = section_body(body, "Session Description")
    source_blob = title + "\n" + description + "\n" + transcript_text
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

    summary_basis = transcript_text or description
    synopsis = curated_synopsis(title, source_blob) or first_sentences(summary_basis, 4)
    if not synopsis:
        synopsis = "No transcript-backed synthesis is available yet; this page currently relies on official schedule context."

    heading = "Secondary Interview Context" if external_only else "Synthesis"
    lines = [
        "### Interview Opening (Secondary Source)" if external_only else "### Synthesized Breakdown",
        synopsis,
        "",
        "### Official Schedule Identity" if external_only else "### Speaker And Company Context",
        *speaker_lines,
        "",
        "### Topics Mentioned In The Interview" if external_only else "### Topics Covered",
    ]
    if topics:
        for topic in topics:
            lines.append(f"- [[{topic}]]")
    else:
        lines.append("- Topic links are pending transcript-backed classification.")
    lines.extend(["", "### Secondary Source Material" if external_only else "### Derived Links And Source Material"])
    if transcripts:
        source_labels = {
            "dedicated": "dedicated official recording transcript",
            "official": "supporting official-channel transcript",
            "livestream": "official livestream context transcript",
            "external": "secondary-source transcript",
        }
        for video_id, tpath, words, source_kind, _ttext in transcripts:
            lines.append(
                f"- [[youtube-{video_id}-transcript]] — {source_labels[source_kind]}; "
                f"source cache `{tpath.relative_to(ROOT)}` ({words:,} words)."
            )
    for video_id in ids:
        if (WIKI / "resources" / f"youtube-{video_id}.md").exists():
            lines.append(f"- [[youtube-{video_id}]] — related YouTube source page.")
        for suffix in ["slides", "reconstructed-slides", "dense-slides"]:
            if (WIKI / "slides" / f"youtube-{video_id}-{suffix}.md").exists():
                lines.append(f"- [[youtube-{video_id}-{suffix}]] — slide evidence.")
    lines.extend(["", "### Interview Concepts / Methods" if external_only else "### Novel Concepts / Clever Methods"])
    if concepts:
        for concept in concepts:
            lines.append(f"- [[{concept['slug']}|{concept['title']}]] — {concept['summary']}")
    else:
        lines.append("- No highlighted novel concept has been detected yet.")
    lines.extend(["", "### Evidence Boundary"])
    if external_only:
        lines.append("This section presents a third-party interview, not an official recording or transcript of this scheduled session. It is retained as secondary context only; the official schedule remains the canonical source for the session title, time, room, status, and speaker attribution.")
    elif transcripts:
        lines.append(
            "This synthesis uses the official schedule and only a dedicated manifest-matched "
            "recording transcript for session-level claims and topic extraction. Related "
            "official-channel, external, and broad livestream sources remain supporting "
            "context and do not stand in for the scheduled session."
        )
    else:
        lines.append("This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.")
    return heading, "\n".join(lines), concepts


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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--speaker", action="append", help="Only update talks containing this speaker. Repeatable.")
    parser.add_argument("--all", action="store_true", help="Update every talk with source context.")
    args = parser.parse_args(argv)

    people, companies = parse_people_companies()
    matched_recordings = official_recording_ids_by_talk()
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
        heading, section, concepts = section_for(
            path,
            text,
            people,
            companies,
            matched_recordings,
        )
        if heading == "Secondary Interview Context":
            text = remove_generated_section(text, "Synthesis", "### Synthesized Breakdown")
        new_text = upsert_section(text, heading, section)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
        for concept in concepts:
            concept_hits[concept["slug"]] += 1
    print(json.dumps({"talks_updated": updated, "concept_hits": dict(concept_hits)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
