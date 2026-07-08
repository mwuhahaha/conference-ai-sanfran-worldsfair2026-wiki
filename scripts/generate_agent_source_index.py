#!/usr/bin/env python3
"""Generate an agent-facing source index for the World's Fair wiki."""

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
    company_profiles = load_json(RAW / "company-profiles.json", {})
    livestreams = load_json(RAW / "aidotengineer-channel-streams-latest.json", [])
    videos = load_json(RAW / "aidotengineer-channel-videos-latest.json", [])

    lines = [
        "---",
        'title: "Agent Source Index"',
        'category: "resources"',
        'sourceLabels: ["Agent guidance", "Source index", "Public source map"]',
        "---",
        "",
        "# Agent Source Index",
        "",
        "This page is the markdown source map for agents working on the AI Engineer World's Fair 2026 wiki. Start here when deciding which files are allowed to support a claim, which sources are canonical, and which scripts refresh derived pages.",
        "",
        "## Agent Start Order",
        "- Read `AGENT.md` at the repository root for the short operating contract.",
        "- Read `AGENTS.md` for local project instructions, category boundaries, and regeneration rules.",
        "- Read this page before adding source links, public-source enrichment, or new generated pages.",
        "- Read [[source-boundary]] before promoting transcript, OCR, slide, or public-profile context into article prose.",
        "",
        "## Canonical Public Sources",
        "- Official conference website: https://www.ai.engineer/worldsfair/2026",
        "- Official sessions JSON mirror: `raw/sources/official-sessions.json`",
        f"  - Status: {source_exists('raw/sources/official-sessions.json')}; sessions indexed: {len(sessions)}",
        "- Official speakers JSON mirror: `raw/sources/official-speakers.json`",
        f"  - Status: {source_exists('raw/sources/official-speakers.json')}; speakers indexed: {len(speakers)}",
        "- AI Engineer YouTube channel: https://www.youtube.com/@aiDotEngineer",
        "- AI Engineer channel video metadata: `raw/sources/aidotengineer-channel-videos-latest.json`",
        f"  - Status: {source_exists('raw/sources/aidotengineer-channel-videos-latest.json')}; video entries: {entry_count(videos)}",
        "- AI Engineer channel livestream metadata: `raw/sources/aidotengineer-channel-streams-latest.json`",
        f"  - Status: {source_exists('raw/sources/aidotengineer-channel-streams-latest.json')}; livestream entries: {entry_count(livestreams)}",
        "",
        "## Derived Source Maps",
        "- Talk/video/caption map: [[talk-video-transcript-map]]",
        f"  - Raw relation file: `raw/sources/speaker-video-map.json`; relation rows: {len(related_videos) if isinstance(related_videos, list) else 'unknown'}",
        "- Caption availability: `raw/sources/related-video-caption-status.json`",
        "- Official livestream resource: [[worldsfair-2026-livestreams]]",
        "- Public company/profile enrichment data: `raw/sources/company-profiles.json`",
        f"  - Curated company profiles: {len(company_profiles)}",
        "- Agentic Web topic page: [[agentic-web]]",
        "",
        "## Transcript Sources",
        "- Speaker-matched YouTube transcripts: `raw/sources/youtube-transcripts/<video-id>.txt`",
        f"  - Cached transcript files: {count_glob('raw/sources/youtube-transcripts/*.txt')}",
        "- Livestream transcript bundles: `raw/sources/youtube-livestream-transcripts/*.bundle.json`",
        f"  - Cached livestream plain-text transcripts: {count_glob('raw/sources/youtube-livestream-transcripts/*.txt')}",
        "- Whisper fallback transcripts: generated by `scripts/transcribe_youtube_audio.py` when public captions are unavailable.",
        "",
        "## Slide And OCR Sources",
        "- Full-stage extracted slide pages: [[slide-library]]",
        f"  - Markdown slide pages: {count_slide_pages('standard')}",
        "- Reconstructed crop slide pages: [[reconstructed-slide-library]]",
        f"  - Reconstructed slide pages: {count_slide_pages('reconstructed')}",
        "- Dense scene-detection slide pages: [[dense-slide-library]]",
        f"  - Dense slide pages: {count_slide_pages('dense')}",
        "- Full-stage OCR text: `raw/sources/slide-ocr/<video-id>/slide-*.txt`",
        "- RapidOCR rereads: `raw/sources/slide-ocr-rapidocr/<video-id>/slide-*.txt`",
        "- Improved OCR replacements: `raw/sources/slide-ocr-improved/<video-id>/slide-*.txt`",
        "- Reconstructed slide OCR: `raw/sources/reconstructed-slide-ocr/<video-id>/slide-*.txt`",
        "- OCR quality audit: `raw/sources/slide-ocr-quality-audit.json`",
        "- RapidOCR audit: `raw/sources/slide-ocr-rapidocr-audit.json`",
        "- Reconstructed slide audit: `raw/sources/reconstructed-slide-audit.json`",
        "- Dense slide audit: `raw/sources/dense-scenedetect-audit.json`",
        "",
        "## Public Source-Of-Source Enrichment",
        "- Speaker social/profile links belong on people pages near the role/company context when present in the official speaker roster.",
        "- Company pages may use official company sites, product docs, public professional profiles, and related public pages when directly relevant.",
        "- Public profile/company context must remain labeled as supporting context; it does not override official schedule facts.",
        "- Add curated company context to `raw/sources/company-profiles.json`, then run `python3 scripts/enrich_company_pages.py`.",
        "",
        "## Main Wiki-Making Scripts",
        "- `python3 scripts/build_worldsfair_wiki.py` - bootstrap official schedule, people, companies, talks, resources, and registries.",
        "- `python3 scripts/enrich_company_pages.py` - refresh company articles from roster, schedule, and curated public company profiles.",
        "- `python3 scripts/update_people_profile_links.py` - upsert speaker profile/social links from official roster data.",
        "- `python3 scripts/enrich_from_youtube_transcripts.py` - enrich pages from cached YouTube transcripts.",
        "- `python3 scripts/extract_video_slides.py` - extract stage-frame slide evidence from related videos.",
        "- `python3 scripts/reconstruct_video_slides.py` - create cleaner crop-based slide decks.",
        "- `python3 scripts/dense_scenedetect_slide_pass.py` - capture high-recall slide changes from scene detection.",
        "- `python3 scripts/rapidocr_slide_pass.py` and `python3 scripts/reread_slide_ocr.py` - improve OCR quality.",
        "- `python3 scripts/generate_tool_inventory.py` - generate tool pages and registry.",
        "- `python3 scripts/generate_question_layer.py` - generate question pages and registry.",
        "- `python3 scripts/generate_agentic_web_topic.py` - refresh the Agentic Web topic from official schedule titles and related local resources.",
        "- `python3 scripts/update_talk_schedule_labels.py` - upsert official track, room, type, and status labels on talk pages.",
        "- `python3 scripts/generate_agent_source_index.py` - refresh this page.",
        "- `npm run build` - export static HTML to `dist/` using `scripts/export_static_site.py`.",
        "",
        "## Agent Rules For Using Sources",
        "- Prefer official schedule and speaker data for titles, dates, times, rooms, tracks, speakers, and affiliations.",
        "- Treat related YouTube videos as supporting evidence unless an exact session recording is confirmed.",
        "- Treat YouTube captions and Whisper transcripts as transcript evidence, with speaker/session matching reviewed before confident attribution.",
        "- Treat OCR as best-effort. Use embedded slide images or reconstructed crops to verify important slide claims.",
        "- Do not import private notes, diary material, local-only caches, or unrelated Obsidian content into the publishable wiki.",
        "- When adding a claim, leave a path back to the source layer: talk, resource, slide, transcript map, public company/profile source, or raw source file.",
    ]

    write(WIKI / "resources" / "agent-source-index.md", "\n".join(lines))
    print(json.dumps({"agent_source_index": "wiki/resources/agent-source-index.md"}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
