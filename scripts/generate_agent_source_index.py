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


def category_index_line(category: str, label: str | None = None) -> str:
    label = label or category.replace("-", " ").title()
    return f"- {label} index: https://aie-worldsfair2026.plusrobot.ai/{category}/"


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
    external_video_discovery = load_json(RAW / "external-video-discovery-latest.json", {})
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
        "- Transcripts index: https://aie-worldsfair2026.plusrobot.ai/transcripts/",
        "- Quotes index: https://aie-worldsfair2026.plusrobot.ai/quotes/",
        "- Tools index: https://aie-worldsfair2026.plusrobot.ai/tools/",
        "- Highlights index: https://aie-worldsfair2026.plusrobot.ai/highlights/",
        category_index_line("claims", "Claims"),
        category_index_line("conversations", "Conversations"),
        category_index_line("patterns", "Patterns"),
        category_index_line("questions", "Questions"),
        category_index_line("harnesses", "Harnesses"),
        category_index_line("playbooks", "Playbooks"),
        category_index_line("evaluations", "Evaluations"),
        category_index_line("policies", "Policies"),
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
        f"- Transcripts: {count_pages('transcripts')} transcript markdown pages.",
        f"- Quotes: {count_pages('quotes')} selected quote pages tied back to source videos and topics.",
        f"- Tools: {count_pages('tools')} tool/protocol/entity pages generated from the conference evidence layer.",
        f"- Claims: {count_pages('claims')} evidence-backed claim pages.",
        f"- Conversations: {count_pages('conversations')} cross-page conversation maps.",
        f"- Patterns: {count_pages('patterns')} reusable AI engineering pattern pages.",
        f"- Questions: {count_pages('questions')} question pages raised by the conference corpus.",
        f"- Harnesses: {count_pages('harnesses')} evaluation or implementation harness pages.",
        f"- Playbooks: {count_pages('playbooks')} reusable playbook pages.",
        f"- Evaluations: {count_pages('evaluations')} evaluation design pages.",
        f"- Policies: {count_pages('policies')} credibility or evidence-policy pages.",
        f"- Events: {count_pages('events')} day/event overview pages.",
        "",
        "## Page Shapes",
        "- Talk pages answer what happened, who presented, where and when it was scheduled, what the synthesized argument is, which topics/tools/companies connect to it, and what transcript/slide/video evidence backs it.",
        "- Person pages identify the speaker, role/company, profile links when available, scheduled sessions, related videos, topics, companies, and source-backed context.",
        "- Company pages explain what the organization does, why it matters in the conference graph, which people and sessions connect to it, and which public company/profile sources support the article.",
        "- Topic pages synthesize what the topic is, why it matters, how and when to use it, origin/use-case context, related scheduled sessions, people, companies, tools, quotes, slides, transcripts, and resources.",
        "- Resource, transcript, and slide pages are evidence layers. They should be cited or inspected before turning media-derived material into a confident claim.",
        "- Claims, patterns, questions, harnesses, playbooks, evaluations, and policies are synthesis layers. Treat them as navigational and analytic pages that point back to talks, transcripts, slides, and resources.",
        "",
        "## Navigation Strategy",
        "- If you know a talk title or speaker, start with `/search/`, `/talks/`, or `/people/`.",
        "- If you know a theme, start with `/topics/`, then follow related talks, people, companies, tools, quotes, and resources from that topic page.",
        "- For page content extraction, prefer `/md/...` markdown backing files over scraping rendered HTML.",
        "- If you need primary schedule context, use the talk page first. Talk pages preserve title, speaker, company, date, track, room, and schedule labels.",
        "- If you need a speaker's context, use the person page, then follow company, scheduled talks, related videos, and social/profile links when present.",
        "- If you need organizational context, use the company page, then follow related people and scheduled talks.",
        "- If you need media evidence, use the talk/video/transcript map and the YouTube resource pages before relying on a transcript or slide page.",
        "- If you need exact wording, fetch the transcript page under `/md/transcripts/...` and then cross-check the linked YouTube resource page.",
        "- If you need slide evidence, prefer reconstructed slide pages for readable cropped slides, then use dense or full-stage slide pages as supporting views.",
        "- If you need reusable concepts, use topics, tools, claims, patterns, questions, harnesses, playbooks, evaluations, and policies; they synthesize across multiple talks and resources.",
        "- If a page is marked highlighted, use `/highlights/` as a curated index into especially important concepts, people, talks, and source pages.",
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
        "- External YouTube video discovery: https://aie-worldsfair2026.plusrobot.ai/resources/external-video-discovery/",
        "- Livestreams resource: https://aie-worldsfair2026.plusrobot.ai/resources/worldsfair-2026-livestreams/",
        "- Livestream talk segments: https://aie-worldsfair2026.plusrobot.ai/resources/livestream-talk-segments/",
        "- Slide library: https://aie-worldsfair2026.plusrobot.ai/resources/slide-library/",
        "- Reconstructed slide library: https://aie-worldsfair2026.plusrobot.ai/resources/reconstructed-slide-library/",
        "- Dense slide library: https://aie-worldsfair2026.plusrobot.ai/resources/dense-slide-library/",
        "- Transcript index: https://aie-worldsfair2026.plusrobot.ai/transcripts/",
        "- Claims index: https://aie-worldsfair2026.plusrobot.ai/claims/",
        "- Patterns index: https://aie-worldsfair2026.plusrobot.ai/patterns/",
        "- Questions index: https://aie-worldsfair2026.plusrobot.ai/questions/",
        "- Harnesses index: https://aie-worldsfair2026.plusrobot.ai/harnesses/",
        "- Playbooks index: https://aie-worldsfair2026.plusrobot.ai/playbooks/",
        "- Evaluations index: https://aie-worldsfair2026.plusrobot.ai/evaluations/",
        "- Policies index: https://aie-worldsfair2026.plusrobot.ai/policies/",
        "- Highlights index: https://aie-worldsfair2026.plusrobot.ai/highlights/",
        "",
        "## Evidence Confidence",
        "- Official schedule and speaker facts are canonical for dates, titles, speakers, organizations, tracks, rooms, and session status.",
        "- Official AI Engineer World's Fair San Francisco 2026 livestreams and cut videos are primary event video sources for media, transcript, and slide evidence.",
        "- Other YouTube pages, including external uploads, older AI Engineer talks, and videos from other AIE events, are supporting context unless manually promoted as exact official event recordings.",
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
        f"- Cached external secondary-source transcript files: {count_glob('raw/sources/external-youtube-transcripts/*.txt')}.",
        f"- External YouTube discovery rows: {entry_count(external_video_discovery.get('results', []) if isinstance(external_video_discovery, dict) else [])}.",
        f"- High-confidence livestream talk timestamp matches: {entry_count(load_json(RAW / 'livestream-talk-segments.json', []))}.",
        "",
        "## Agent Task Recipes",
        "- To answer `what was said about X`: search X, inspect the relevant topic page, open related talks, then follow video/transcript and slide links.",
        "- To answer `who is connected to X`: inspect the topic or company page, then follow Related People and Related Scheduled Sessions.",
        "- To answer `which companies are involved`: start with `/companies/`, search the company name, then cross-check people and talks linked from that company page.",
        "- To answer `what evidence supports this`: prefer talk pages and resource pages, then use transcripts, quotes, and slide pages as supporting evidence.",
        "- To answer `is this official or supporting evidence`: inspect Source Boundary, the page frontmatter/source labels, and the media/source section before relying on the claim.",
        "- To answer `which markdown should I read`: convert the rendered URL to `/md/<page-id>.md`, or fetch `/agent-index.md` again for routing.",
        "- To answer `where should I browse next`: use the related links at the bottom of the current page; the wiki is intentionally cross-linked across talks, people, companies, topics, tools, quotes, resources, and slides.",
    ]

    write(WIKI / "resources" / "agent-source-index.md", "\n".join(lines))
    print(json.dumps({"agent_source_index": "wiki/resources/agent-source-index.md"}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
