#!/usr/bin/env python3
"""Import a Google Photos slide album into the wiki slide evidence layer.

This tool expects a prepared cache directory with:
- manifest.json from the Google Photos share metadata
- images/<NNN-photo-id>.jpg
- ocr-rapidocr/<NNN-photo-id>.txt

It creates a separate, labeled source layer instead of rewriting YouTube OCR
outputs. That keeps human phone photos distinct from official schedule facts
and from video-derived slide frames.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from markdown_blocks import blockquote


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw" / "sources"


IMPORT_ID = "aie-slides-9gWZzS1EpXM1C5eK6"
AUTHOR = "boxofchocolates"
DEFAULT_CACHE = ROOT / ".ops" / "state" / "cache" / f"google-photos-import-{IMPORT_ID.removeprefix('aie-slides-')}"


@dataclass(frozen=True)
class SlideGroup:
    key: str
    title: str
    photo_indexes: list[int]
    confidence: str
    evidence: list[str]
    talk_paths: list[str] = field(default_factory=list)
    timestamp_note: str = ""


GROUPS = [
    SlideGroup(
        key="cooking-with-codex",
        title="Google Photos Slides: Cooking with Codex",
        photo_indexes=[1],
        confidence="medium",
        talk_paths=["wiki/talks/2026-06-29-charlie-guo-cooking-with-codex.md"],
        evidence=["OCR names the Codex app and event promo codes.", "Photo timestamp falls during the Day 1 workshop block."],
        timestamp_note="Treat as event/workshop slide evidence, not an official talk recording.",
    ),
    SlideGroup(
        key="llm-inference-at-scale",
        title="Google Photos Slides: LLM Inference at Scale Workshop",
        photo_indexes=[2, 3, 4],
        confidence="high",
        talk_paths=[
            "wiki/talks/2026-06-29-harshul-jain-2-hr-deep-dive-on-llm-inference-at-scale-part-1-of-2.md",
            "wiki/talks/2026-06-29-harshul-jain-2-hr-deep-dive-on-llm-inference-at-scale-part-2-of-2.md",
        ],
        evidence=["OCR includes tensor/data/pipeline/expert/context parallelism.", "OCR names NSight Systems, Torch profilers, CuPTI, vLLM resources, and Modal."],
        timestamp_note="Photo timestamps are around the Day 1 LLM inference workshop transition; linked to both workshop parts.",
    ),
    SlideGroup(
        key="gemini-live",
        title="Google Photos Slides: Gemini Live API Workshop",
        photo_indexes=[5, 6],
        confidence="medium",
        talk_paths=[
            "wiki/talks/2026-06-30-thor-schaeff-build-realtime-multimodal-agents-with-gemini-live.md",
            "wiki/talks/2026-06-30-thor-schaeff-build-realtime-multimodal-agents-with-gemini-live-continued-2.md",
            "wiki/talks/2026-06-30-thor-schaeff-build-realtime-multimodal-agents-with-gemini-live-continued-3.md",
            "wiki/talks/2026-06-30-thor-schaeff-build-realtime-multimodal-agents-with-gemini-live-continued-4.md",
        ],
        evidence=["OCR names Gemini API inputs and outputs.", "OCR names Gemini Omni Flash and multimodal input/output flow."],
        timestamp_note="Linked to the Gemini Live workshop series; the photo clock does not isolate a single continued segment.",
    ),
    SlideGroup(
        key="unleash-agent-watch-it-burn",
        title="Google Photos Slides: Build a Platform, Unleash an Agent on it",
        photo_indexes=[7],
        confidence="high",
        talk_paths=["wiki/talks/2026-06-29-michael-forrester-build-a-platform-unleash-an-agent-on-it-and-watch-it-burn.md"],
        evidence=["OCR captures the exact GitHub repository name peopletorrester/Unleash_an_Agent_Watch_It_Burn.", "The repository and screenshot terms match the scheduled workshop premise."],
    ),
    SlideGroup(
        key="bm25-agentic-search",
        title="Google Photos Slides: The Unreasonable Effectiveness of BM25 for Agentic Search",
        photo_indexes=[8, 9, 10],
        confidence="high",
        talk_paths=["wiki/talks/2026-06-29-jo-kristian-bergum-the-unreasonable-effectiveness-of-bm25-for-agentic-search.md"],
        evidence=["OCR names HORNET, BM25, agentic retrieval, Jo Kristian Bergum, and Hornet.dev.", "The concepts match the official BM25 for agentic search session."],
        timestamp_note="Photo timestamps should be treated as capture provenance; official schedule fields remain canonical.",
    ),
    SlideGroup(
        key="rebuilding-the-web-for-agents",
        title="Google Photos Slides: Rebuilding the Web for Agents",
        photo_indexes=[11, 12, 13],
        confidence="high",
        talk_paths=["wiki/talks/2026-06-29-liad-yosef-rebuilding-the-web-for-agents.md"],
        evidence=["OCR says Agent Ready, Human UI, Browser, Agent, MCP, Agent App.", "OCR lists Discovery, User Experience, Identity, Integration, and Auth and Access, matching agent-ready web surfaces."],
        timestamp_note="Photo timestamp aligns with the Day 2 12:05 session block, while the generated slug uses the project's existing date convention.",
    ),
    SlideGroup(
        key="knowledge-agents",
        title="Google Photos Slides: Knowledge Agents",
        photo_indexes=[14, 15, 16, 17, 18, 19, 20, 21],
        confidence="high",
        talk_paths=["wiki/talks/2026-06-29-benjamin-clavi-if-we-want-them-to-do-knowledge-work-we-need-to-design-knowledge-agents.md"],
        evidence=["OCR repeatedly discusses knowledge work, tools, organization, DeepResearch, MixedbreadSearch, BM25, and orchestrated research.", "Photo timing matches the Day 2 Search and Retrieval session block for Benjamin Clavie's talk."],
    ),
    SlideGroup(
        key="browser-agent-success-harness",
        title="Google Photos Slides: Browser Agent Success Harness",
        photo_indexes=[22, 23, 24, 25],
        confidence="medium",
        talk_paths=["wiki/talks/2026-06-29-derek-meegan-deploying-browser-agents-at-scale.md"],
        evidence=["OCR describes concrete success artifacts, browser harnesses, auth outside the model, skills, verification, and a system-of-record database.", "Photo timing points to the Day 2 1:55pm browser-agents slot, but OCR does not name the speaker or Browserbase."],
        timestamp_note="Medium-confidence schedule match. Keep this as photo-slide evidence until another source confirms the exact talk.",
    ),
    SlideGroup(
        key="software-factories-fail",
        title="Google Photos Slides: Why Software Factories Fail",
        photo_indexes=[26, 27],
        confidence="high",
        talk_paths=["wiki/talks/2026-06-29-dex-horthy-harness-engineering-is-not-enough-why-software-factories-fail.md"],
        evidence=["OCR names SWE-Marathon, abundant.ai, Dex Horthy, HumanLayer, and software factories fail.", "OCR includes the HumanLayer slide URL shown in the talk."],
    ),
    SlideGroup(
        key="dark-arts-web-automation",
        title="Google Photos Slides: The Dark Arts of Web Automation",
        photo_indexes=[28, 29, 30, 31, 32, 33, 34, 35],
        confidence="high",
        talk_paths=["wiki/talks/2026-06-30-corey-gallon-the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md"],
        evidence=["OCR names CDP browser, Sense/Act/Verify, Meatbag Ladder, Demazon, Cloudflare Turnstile, MTCaptcha, chrome-agent, @coreygallon, and Runlayer.", "The slide content uniquely matches the Dark Arts of Web Automation talk."],
        timestamp_note="Photo timestamp aligns with the Day 3 12:05 computer-use slot; the generated talk page is the canonical schedule page.",
    ),
    SlideGroup(
        key="knowledge-systems-gtm-stack",
        title="Google Photos Slides: Knowledge Systems, the New GTM Stack",
        photo_indexes=[36, 37, 38, 39, 40, 41, 42, 43],
        confidence="high",
        talk_paths=["wiki/talks/2026-07-01-jeffrey-wang-knowledge-systems-the-new-gtm-stack.md"],
        evidence=["OCR names GTM teams, Knowledge System, ICP Dashboard, RequestLens, Coding Harnesses, Jeffbot, Exa, and Exa technical stack.", "Photo timestamp aligns with the Day 4 AI in GTM session block."],
        timestamp_note="Photo timestamp is 2026-07-02 local; the generated talk slug uses the project's existing date convention.",
    ),
    SlideGroup(
        key="nyt-games-connections",
        title="Google Photos Slides: On-Device Agentic AI for the New York Times Games",
        photo_indexes=[45],
        confidence="high",
        talk_paths=["wiki/talks/2026-07-01-shafik-quoraishee-on-device-agentic-ai-for-the-new-york-times-games.md"],
        evidence=["OCR and image text identify AI and Game Theory, NYT Connections, and World's Fair.", "Existing wiki media maps Shafik Quoraishee's NYT Connections video to this scheduled session."],
    ),
    SlideGroup(
        key="velocity-sickness-ref",
        title="Google Photos Slides: Velocity Sickness and Ref",
        photo_indexes=[46, 47],
        confidence="high",
        talk_paths=["wiki/talks/2026-07-01-matt-dailey-velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md"],
        evidence=["OCR names Ref, ref.tools, too many PRs to merge, agent bankruptcy, and human-owned critical decisions.", "Photo timestamp aligns with the official Day 4 3:20pm Velocity Sickness slot."],
    ),
    SlideGroup(
        key="unmatched-graphs-seo4ai",
        title="Google Photos Slides: Unmatched Graphs or SEO4AI Schedule Photo",
        photo_indexes=[44],
        confidence="low",
        talk_paths=[],
        evidence=["OCR is too weak to identify the schedule page confidently.", "Visible image appears to reference World's Fair, Graphs, and SEO4AI, but requires manual review."],
        timestamp_note="Kept as unmatched source evidence until a stronger schedule/video match exists.",
    ),
]


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_title(path: Path) -> str:
    text = read_text(path)
    match = re.search(r'^title:\s*"(.+?)"', text, re.M)
    if match:
        return match.group(1)
    h1 = re.search(r"^#\s+(.+)$", text, re.M)
    return h1.group(1) if h1 else path.stem


def load_records(cache: Path) -> list[dict]:
    records = json.loads((cache / "manifest.json").read_text(encoding="utf-8"))
    if not isinstance(records, list):
        raise ValueError("manifest.json must contain a list of photo records")
    return records


def photo_paths(cache: Path, index: int, photo_id: str) -> tuple[Path, Path]:
    image_matches = sorted((cache / "images").glob(f"{index:03d}-{photo_id}.jpg"))
    ocr_matches = sorted((cache / "ocr-rapidocr").glob(f"{index:03d}-{photo_id}.txt"))
    if not image_matches:
        image_matches = sorted((cache / "images").glob(f"{index:03d}-*.jpg"))
    if not ocr_matches:
        ocr_matches = sorted((cache / "ocr-rapidocr").glob(f"{index:03d}-*.txt"))
    if not image_matches:
        raise FileNotFoundError(f"missing cached image for photo {index}")
    return image_matches[0], ocr_matches[0] if ocr_matches else Path()


def copy_sources(cache: Path, records: list[dict]) -> list[dict]:
    raw_base = RAW / "google-photos-slides" / IMPORT_ID
    asset_base = WIKI / "assets" / "slides" / f"google-photos-{IMPORT_ID}"
    copied = []
    for index, record in enumerate(records, start=1):
        photo_id = record["photoId"]
        image_src, ocr_src = photo_paths(cache, index, photo_id)
        image_name = f"photo-{index:03d}.jpg"
        ocr_name = f"photo-{index:03d}.txt"
        raw_image = raw_base / "images" / image_name
        raw_ocr = raw_base / "ocr" / ocr_name
        asset_image = asset_base / image_name
        raw_image.parent.mkdir(parents=True, exist_ok=True)
        raw_ocr.parent.mkdir(parents=True, exist_ok=True)
        asset_image.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(image_src, raw_image)
        shutil.copy2(image_src, asset_image)
        ocr_text = read_text(ocr_src).strip()
        write_text(raw_ocr, ocr_text)
        copied.append(
            {
                "photoIndex": index,
                "photoId": photo_id,
                "capturedAtUtc": record.get("utc"),
                "capturedAtLocalClock": record.get("local"),
                "sourceAlbum": record.get("sourceAlbum"),
                "author": AUTHOR,
                "rawImage": str(raw_image.relative_to(ROOT)),
                "rawOcr": str(raw_ocr.relative_to(ROOT)),
                "wikiAsset": str(asset_image.relative_to(WIKI)),
                "ocrText": ocr_text,
            }
        )
    write_text(raw_base / "manifest.json", json.dumps(copied, indent=2, ensure_ascii=False))
    return copied


def group_records(copied: list[dict]) -> list[dict]:
    by_index = {item["photoIndex"]: item for item in copied}
    matches = []
    for group in GROUPS:
        photos = []
        for index in group.photo_indexes:
            if index in by_index:
                photos.append(by_index[index])
        talk_links = []
        for talk_path in group.talk_paths:
            path = ROOT / talk_path
            talk_links.append(
                {
                    "path": talk_path,
                    "wikilink": Path(talk_path).stem,
                    "title": load_title(path),
                }
            )
        matches.append(
            {
                "id": f"google-photos-{IMPORT_ID}-{group.key}",
                "title": group.title,
                "key": group.key,
                "confidence": group.confidence,
                "evidence": group.evidence,
                "timestampNote": group.timestamp_note,
                "relatedTalks": talk_links,
                "photos": photos,
            }
        )
    return matches


def markdown_quote(text: str) -> str:
    if not text.strip():
        return "> No OCR text was extracted."
    return blockquote(text)


def write_slide_pages(matches: list[dict]) -> list[dict]:
    written = []
    for match in matches:
        page = WIKI / "slides" / f"{match['id']}-slides.md"
        lines = [
            "---",
            f'title: "{match["title"]}"',
            'category: "slides"',
            f'import_id: "{IMPORT_ID}"',
            f'author: "{AUTHOR}"',
            'sourceLabels: ["Google Photos share", "Phone photo slide evidence", "RapidOCR text"]',
            f'confidence: "{match["confidence"]}"',
            "---",
            "",
            f"# {match['title']}",
            "",
            "## Source",
            f"- Author: {AUTHOR}",
            "- Source type: Google Photos album import supplied to the wiki builder.",
            f"- Imported source layer: `raw/sources/google-photos-slides/{IMPORT_ID}/`",
            "- OCR engine: RapidOCR over downloaded Google Photos images.",
            "",
            "## Relationship To World's Fair 2026",
        ]
        if match["relatedTalks"]:
            lines.extend(["These photos are matched to the following scheduled session(s):"])
            for talk in match["relatedTalks"]:
                lines.append(f"- [[{talk['wikilink']}]] - {talk['title']}")
        else:
            lines.append("No scheduled session mapping has been assigned yet. Treat this as unmatched event slide evidence.")
        lines.extend(
            [
                "",
                "## Match Confidence",
                f"- Confidence: {match['confidence']}",
            ]
        )
        for evidence in match["evidence"]:
            lines.append(f"- {evidence}")
        if match["timestampNote"]:
            lines.append(f"- Timestamp note: {match['timestampNote']}")
        lines.extend(["", "## Photo Slides"])
        for photo in match["photos"]:
            lines.extend(
                [
                    f"### Photo {photo['photoIndex']:03d}",
                    f"- Captured at UTC: {photo.get('capturedAtUtc') or 'unknown'}",
                    f"- Captured local clock: {photo.get('capturedAtLocalClock') or 'unknown'}",
                    f"- Raw OCR: `{photo['rawOcr']}`",
                    "",
                    f"![[{photo['wikiAsset']}]]",
                    "",
                    "OCR text:",
                    "",
                    markdown_quote(photo.get("ocrText", "")),
                    "",
                ]
            )
        write_text(page, "\n".join(lines))
        written.append(
            {
                "id": page.stem,
                "title": match["title"],
                "path": str(page.relative_to(ROOT)),
                "slide_count": len(match["photos"]),
                "confidence": match["confidence"],
            }
        )
    return written


def upsert_talk_backlinks(matches: list[dict]) -> int:
    updated = 0
    by_talk: dict[str, list[dict]] = {}
    for match in matches:
        if match["confidence"] == "low":
            continue
        for talk in match["relatedTalks"]:
            by_talk.setdefault(talk["path"], []).append(match)

    for talk_path, talk_matches in by_talk.items():
        path = ROOT / talk_path
        if not path.exists():
            continue
        text = read_text(path).rstrip()
        lines = [
            "## Additional Photo Slide Evidence",
            "These are phone-photo slide captures from the Google Photos `AIE Slides` album. They are supporting slide evidence and do not override official schedule fields.",
        ]
        for match in talk_matches:
            lines.append(f"- [[{match['id']}-slides]] - {match['title']} (confidence: {match['confidence']}).")
        block = "\n" + "\n".join(lines) + "\n"
        pattern = re.compile(r"\n## Additional Photo Slide Evidence\n.*?(?=\n## |\Z)", re.S)
        if pattern.search(text):
            new_text = pattern.sub(block.rstrip(), text)
        else:
            new_text = text + "\n" + block
        if new_text.rstrip() != text:
            write_text(path, new_text)
            updated += 1
    return updated


def update_slide_registry(entries: list[dict]) -> None:
    path = WIKI / "slides" / "registry.json"
    registry = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    keep = [item for item in registry if not str(item.get("id", "")).startswith(f"google-photos-{IMPORT_ID}-")]
    keep.extend(entries)
    keep.sort(key=lambda item: item.get("id", ""))
    write_text(path, json.dumps(keep, indent=2, ensure_ascii=False))


def write_resource_page(matches: list[dict]) -> None:
    lines = [
        "---",
        'title: "Google Photos AIE Slides Import"',
        'category: "resources"',
        'sourceLabels: ["Google Photos share", "Photo slide evidence", "Import manifest"]',
        "---",
        "",
        "# Google Photos AIE Slides Import",
        "",
        f"This page indexes additional phone-photo slide captures supplied by {AUTHOR} for World's Fair slide enrichment.",
        "",
        "## Source",
        f"- Author: {AUTHOR}",
        "- Source type: Google Photos album import supplied to the wiki builder.",
        f"- Raw source layer: `raw/sources/google-photos-slides/{IMPORT_ID}/`",
        f"- Import manifest: `raw/sources/google-photos-slides/{IMPORT_ID}/matches.json`",
        "",
        "## Evidence Boundary",
        "- These photos are supporting slide evidence.",
        "- Official schedule pages remain canonical for title, speaker, room, track, and time.",
        "- Photo timestamps are capture provenance and can disagree with generated page slugs or schedule labels.",
        "- OCR text is best-effort RapidOCR and should be checked against the embedded image before becoming a confident claim.",
        "",
        "## Matched Slide Groups",
    ]
    for match in matches:
        lines.append(f"- [[{match['id']}-slides]] - {match['title']} (confidence: {match['confidence']}, photos: {len(match['photos'])})")
        for talk in match["relatedTalks"]:
            lines.append(f"  - Related talk: [[{talk['wikilink']}]] - {talk['title']}")
        if not match["relatedTalks"]:
            lines.append("  - Related talk: unmatched")
    write_text(WIKI / "resources" / "google-photos-aie-slides.md", "\n".join(lines))


def update_agent_source_index() -> None:
    path = WIKI / "resources" / "agent-source-index.md"
    text = read_text(path)
    marker = "- Google Photos slide import: [[google-photos-aie-slides]]"
    if marker in text:
        return
    needle = "## Slide And OCR Sources\n"
    insert = (
        "## Slide And OCR Sources\n"
        f"- Google Photos slide import: [[google-photos-aie-slides]]\n"
        f"  - Raw source layer: `raw/sources/google-photos-slides/{IMPORT_ID}/`\n"
        "  - Treat as supporting phone-photo slide evidence; official schedule metadata remains canonical.\n"
    )
    if needle in text:
        text = text.replace(needle, insert, 1)
    else:
        text = text.rstrip() + "\n\n" + insert
    write_text(path, text)


def write_receipt(matches: list[dict], updated_talks: int) -> None:
    receipt = {
        "type": "google-photos-slide-import",
        "importId": IMPORT_ID,
        "author": AUTHOR,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "sourceType": "Google Photos album import supplied to the wiki builder",
        "groups": len(matches),
        "photos": sum(len(match["photos"]) for match in matches),
        "updatedTalkPages": updated_talks,
    }
    write_text(ROOT / ".ops" / "state" / "runs" / f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-google-photos-slide-import.json", json.dumps(receipt, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    args = parser.parse_args()

    if not args.cache.exists():
        raise SystemExit(f"cache directory not found: {args.cache}")

    records = load_records(args.cache)
    copied = copy_sources(args.cache, records)
    matches = group_records(copied)
    raw_base = RAW / "google-photos-slides" / IMPORT_ID
    write_text(raw_base / "matches.json", json.dumps(matches, indent=2, ensure_ascii=False))
    entries = write_slide_pages(matches)
    update_slide_registry(entries)
    write_resource_page(matches)
    update_agent_source_index()
    updated_talks = upsert_talk_backlinks(matches)
    write_receipt(matches, updated_talks)

    print(f"imported {len(copied)} photos into {len(matches)} slide groups")
    print(f"updated {updated_talks} talk pages")
    print(f"source layer: raw/sources/google-photos-slides/{IMPORT_ID}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
