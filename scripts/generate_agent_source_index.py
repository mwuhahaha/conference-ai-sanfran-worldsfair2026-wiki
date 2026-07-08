#!/usr/bin/env python3
"""Generate an agent-facing navigation index for the World's Fair wiki."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw" / "sources"


def load_json(path: Path, fallback):
    if not path.exists():
        return fallback
    return json.loads(path.read_text())


def count_glob(pattern: str) -> int:
    return len(list(ROOT.glob(pattern)))


def count_pages(category: str) -> int:
    return len(list((WIKI / category).glob("*.md")))


def count_slide_pages(kind: str) -> int:
    pages = list((WIKI / "slides").glob("youtube-*.md"))
    if kind == "standard":
        return len([page for page in pages if not page.name.endswith("-reconstructed-slides.md") and not page.name.endswith("-dense-slides.md")])
    if kind == "reconstructed":
        return len([page for page in pages if page.name.endswith("-reconstructed-slides.md")])
    if kind == "dense":
        return len([page for page in pages if page.name.endswith("-dense-slides.md")])
    return len(pages)


def entry_count(blob) -> int | str:
    if isinstance(blob, list):
        return len(blob)
    if isinstance(blob, dict) and isinstance(blob.get("entries"), list):
        return len(blob["entries"])
    return "unknown"


def source_exists(path: str) -> str:
    return "present" if (ROOT / path).exists() else "missing"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    sessions = load_json(RAW / "official-sessions.json", {}).get("sessions", [])
    speakers = load_json(RAW / "official-speakers.json", {}).get("speakers", [])
    related_videos = load_json(RAW / "speaker-video-map.json", [])
    livestreams = load_json(RAW / "aidotengineer-channel-streams-latest.json", [])
    videos = load_json(RAW / "aidotengineer-channel-videos-latest.json", [])

    lines = [
        "---",
        'title: "Agent Navigation Index"',
        'category: "resources"',
        'sourceLabels: ["Agent guidance", "Navigation index", "Public wiki map"]',
        "---",
        "",
        "# Agent Navigation Index",
        "",
        "This is the agent-readable navigation map for the AI Engineer World's Fair 2026 wiki. Point an agent here when it needs to consume the public wiki, find the right page type, follow evidence links, or understand how topics, talks, people, companies, slides, quotes, and resources connect.",
        "",
        "Raw standalone markdown for agents: https://aie-worldsfair2026.plusrobot.ai/agent-index.md",
        "",
        "Human-rendered page: https://aie-worldsfair2026.plusrobot.ai/resources/agent-source-index/",
        "",
        "## Start Here",
        "- Home overview: https://aie-worldsfair2026.plusrobot.ai/",
        "- Full index: https://aie-worldsfair2026.plusrobot.ai/index/",
        "- Search page: https://aie-worldsfair2026.plusrobot.ai/search/",
        "- Topics index: https://aie-worldsfair2026.plusrobot.ai/topics/",
        "- Talks index: https://aie-worldsfair2026.plusrobot.ai/talks/",
        "- People index: https://aie-worldsfair2026.plusrobot.ai/people/",
        "- Companies index: https://aie-worldsfair2026.plusrobot.ai/companies/",
        "- Slides index: https://aie-worldsfair2026.plusrobot.ai/slides/",
        "- Quotes index: https://aie-worldsfair2026.plusrobot.ai/quotes/",
        "- Tools index: https://aie-worldsfair2026.plusrobot.ai/tools/",
        "- Highlights index: https://aie-worldsfair2026.plusrobot.ai/highlights/",
        "- Source boundary and evidence confidence: https://aie-worldsfair2026.plusrobot.ai/resources/source-boundary/",
        "",
        "## URL Rules",
        "- Every rendered page uses a stable lowercase slug URL ending in `/`.",
        "- Every rendered page has a backing markdown file at `/md/<same-page-id>.md`.",
        "- To convert a rendered URL to markdown, remove the leading slash and trailing slash, then prefix `/md/` and append `.md`: `/topics/agentic-web/` becomes `/md/topics/agentic-web.md`.",
        "- The home page is backed by `/md/overview.md`.",
        "- A talk page is `/talks/<date-speaker-title-slug>/`.",
        "- A person page is `/people/<person-slug>/`.",
        "- A company page is `/companies/<company-slug>/`.",
        "- A topic page is `/topics/<topic-slug>/`.",
        "- A slide page is `/slides/<youtube-video-id-kind>/`.",
        "- A quote page is `/quotes/<quote-slug>/`.",
        "- A resource page is `/resources/<resource-slug>/`.",
        "- Wiki links in markdown use `[[slug]]` or `[[slug|label]]`; on the public site these resolve to the matching rendered URL.",
        "- If a rendered page is hard to parse, fetch its markdown backing file first and use the rendered page only for images or visual inspection.",
        "",
        "## Corpus Map",
        f"- Talks: {count_pages('talks')} rendered talk pages; official schedule sessions indexed: {len(sessions)}.",
        f"- People: {count_pages('people')} rendered people pages; official speakers indexed: {len(speakers)}.",
        f"- Companies: {count_pages('companies')} rendered company pages.",
        f"- Topics: {count_pages('topics')} synthesis pages across repeated conference themes.",
        f"- Resources: {count_pages('resources')} pages for source maps, YouTube evidence, livestreams, and processing audits.",
        f"- Slides: {count_pages('slides')} slide pages; standard decks: {count_slide_pages('standard')}; reconstructed decks: {count_slide_pages('reconstructed')}; dense decks: {count_slide_pages('dense')}.",
        f"- Quotes: {count_pages('quotes')} selected quote pages tied back to source videos and topics.",
        f"- Tools: {count_pages('tools')} tool/protocol/entity pages generated from the conference evidence layer.",
        f"- Events: {count_pages('events')} day/event overview pages.",
        "",
        "## Navigation Strategy",
        "- If you know a talk title or speaker, start with `/search/`, `/talks/`, or `/people/`.",
        "- If you know a theme, start with `/topics/`, then follow related talks, people, companies, tools, quotes, and resources from that topic page.",
        "- For page content extraction, prefer `/md/...` markdown backing files over scraping rendered HTML.",
        "- If you need primary schedule context, use the talk page first. Talk pages preserve title, speaker, company, date, track, room, and schedule labels.",
        "- If you need a speaker's context, use the person page, then follow company, scheduled talks, related videos, and social/profile links when present.",
        "- If you need organizational context, use the company page, then follow related people and scheduled talks.",
        "- If you need media evidence, use the talk/video/transcript map and the YouTube resource pages before relying on a transcript or slide page.",
        "- If you need slide evidence, prefer reconstructed slide pages for readable cropped slides, then use dense or full-stage slide pages as supporting views.",
        "- If you need reusable concepts, use topics and tools pages; they synthesize across multiple talks and resources.",
        "- If a page is marked highlighted, expect richer synthesis and check `/highlights/` for the operator's reason and maintenance brief.",
        "- If you need a concise evidence-backed excerpt, use quote pages and then follow their source video, related topic, and scheduled talk links.",
        "",
        "## High-Value Entry Points",
        "- Agentic Web topic: https://aie-worldsfair2026.plusrobot.ai/topics/agentic-web/",
        "- Agentic Search topic: https://aie-worldsfair2026.plusrobot.ai/topics/agentic-search/",
        "- Coding Agents topic: https://aie-worldsfair2026.plusrobot.ai/topics/coding-agents/",
        "- Agent Evaluations topic: https://aie-worldsfair2026.plusrobot.ai/topics/agent-evaluations/",
        "- Agent Memory topic: https://aie-worldsfair2026.plusrobot.ai/topics/agent-memory/",
        "- AI Sandboxes topic: https://aie-worldsfair2026.plusrobot.ai/topics/ai-sandboxes/",
        "- MCP topic: https://aie-worldsfair2026.plusrobot.ai/topics/mcp/",
        "- Inference Engineering topic: https://aie-worldsfair2026.plusrobot.ai/topics/inference-engineering/",
        "- Talk/video/transcript map: https://aie-worldsfair2026.plusrobot.ai/resources/talk-video-transcript-map/",
        "- Livestreams resource: https://aie-worldsfair2026.plusrobot.ai/resources/worldsfair-2026-livestreams/",
        "- Slide library: https://aie-worldsfair2026.plusrobot.ai/resources/slide-library/",
        "- Reconstructed slide library: https://aie-worldsfair2026.plusrobot.ai/resources/reconstructed-slide-library/",
        "- Dense slide library: https://aie-worldsfair2026.plusrobot.ai/resources/dense-slide-library/",
        "- Highlights index: https://aie-worldsfair2026.plusrobot.ai/highlights/",
        "",
        "## Evidence Confidence",
        "- Official schedule and speaker facts are canonical for dates, titles, speakers, organizations, tracks, rooms, and session status.",
        "- Related YouTube pages are supporting context unless the page explicitly confirms an exact recording match.",
        "- Transcripts are useful evidence, but speaker/session matching and caption quality may vary.",
        "- Slide OCR is best-effort. For important claims, inspect the embedded slide image or reconstructed crop.",
        "- Topic, tool, quote, and company pages are synthesis layers. Follow their linked talks, resources, videos, slides, and source-boundary notes before treating a claim as primary.",
        "",
        "## Media And Source Pointers",
        "- Official conference website: https://www.ai.engineer/worldsfair/2026",
        f"- Official schedule mirror status: {source_exists('raw/sources/official-sessions.json')}; sessions indexed: {len(sessions)}.",
        f"- Official speaker mirror status: {source_exists('raw/sources/official-speakers.json')}; speakers indexed: {len(speakers)}.",
        "- AI Engineer YouTube channel: https://www.youtube.com/@aiDotEngineer",
        f"- Channel video metadata status: {source_exists('raw/sources/aidotengineer-channel-videos-latest.json')}; video entries: {entry_count(videos)}.",
        f"- Channel livestream metadata status: {source_exists('raw/sources/aidotengineer-channel-streams-latest.json')}; livestream entries: {entry_count(livestreams)}.",
        f"- Related talk/video rows indexed: {len(related_videos) if isinstance(related_videos, list) else 'unknown'}.",
        f"- Cached speaker-matched transcript files: {count_glob('raw/sources/youtube-transcripts/*.txt')}.",
        f"- Cached livestream transcript files: {count_glob('raw/sources/youtube-livestream-transcripts/*.txt')}.",
        "",
        "## Agent Task Recipes",
        "- To answer `what was said about X`: search X, inspect the relevant topic page, open related talks, then follow video/transcript and slide links.",
        "- To answer `who is connected to X`: inspect the topic or company page, then follow Related People and Related Scheduled Sessions.",
        "- To answer `which companies are involved`: start with `/companies/`, search the company name, then cross-check people and talks linked from that company page.",
        "- To answer `what evidence supports this`: prefer talk pages and resource pages, then use transcripts, quotes, and slide pages as supporting evidence.",
        "- To answer `where should I browse next`: use the related links at the bottom of the current page; the wiki is intentionally cross-linked across talks, people, companies, topics, tools, quotes, resources, and slides.",
    ]

    write(WIKI / "resources" / "agent-source-index.md", "\n".join(lines))
    print(json.dumps({"agent_source_index": "wiki/resources/agent-source-index.md"}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
