#!/usr/bin/env python3
"""Generate linkable wiki markdown pages for cached YouTube transcripts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw" / "sources"
TRANSCRIPT_DIRS = [
    (RAW / "youtube-transcripts", "YouTube transcript"),
    (RAW / "youtube-livestream-transcripts", "YouTube livestream transcript"),
    (RAW / "external-youtube-transcripts", "External YouTube secondary-source transcript"),
]
VIDEO_CATALOG = RAW / "aidotengineer-channel-videos-latest.json"
IMPORT_REPORT = RAW / "new-video-import-2026-07-09.json"
EXTERNAL_DISCOVERY = RAW / "external-video-discovery-latest.json"
OFFICIAL_VIDEO_MANIFEST = RAW / "official-wf26-video-manifest.json"


def yaml_value(value: object) -> str:
    if isinstance(value, list):
        return "[" + ", ".join(json.dumps(str(item), ensure_ascii=False) for item in value) + "]"
    return json.dumps(str(value), ensure_ascii=False)


def frontmatter(fields: dict[str, object]) -> str:
    lines = ["---"]
    for key, value in fields.items():
        lines.append(f"{key}: {yaml_value(value)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def titleize(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("-", " ").replace("_", " ")).strip().title()


def load_titles() -> dict[str, str]:
    titles: dict[str, str] = {}
    if VIDEO_CATALOG.exists():
        data = json.loads(VIDEO_CATALOG.read_text(encoding="utf-8"))
        for item in data.get("entries", []):
            if item.get("id") and item.get("title"):
                titles[item["id"]] = item["title"]
    if IMPORT_REPORT.exists():
        data = json.loads(IMPORT_REPORT.read_text(encoding="utf-8"))
        for item in data.get("imported_transcripts", []):
            if item.get("id") and item.get("title"):
                titles[item["id"]] = item["title"]
        for item in data.get("pending_premieres", []):
            if item.get("id") and item.get("title"):
                titles[item["id"]] = item["title"]
    if EXTERNAL_DISCOVERY.exists():
        data = json.loads(EXTERNAL_DISCOVERY.read_text(encoding="utf-8"))
        for item in data.get("results", []):
            video = item.get("video") or {}
            if video.get("id") and video.get("title"):
                titles[video["id"]] = video["title"]
    if OFFICIAL_VIDEO_MANIFEST.exists():
        data = json.loads(OFFICIAL_VIDEO_MANIFEST.read_text(encoding="utf-8"))
        for item in data.get("videos", []):
            if item.get("id") and item.get("title"):
                titles[item["id"]] = item["title"]
    return titles


def transcript_paths(video_ids: set[str] | None = None) -> list[tuple[Path, str]]:
    paths: list[tuple[Path, str]] = []
    for folder, label in TRANSCRIPT_DIRS:
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.txt")):
            if video_ids is not None and path.stem not in video_ids:
                continue
            paths.append((path, label))
    return paths


def official_manifest_video_ids() -> set[str]:
    if not OFFICIAL_VIDEO_MANIFEST.is_file():
        return set()
    value = json.loads(OFFICIAL_VIDEO_MANIFEST.read_text(encoding="utf-8"))
    videos = value.get("videos", [])
    if not isinstance(videos, list):
        raise ValueError("official WF26 video manifest must contain a videos array")
    return {
        str(item["id"])
        for item in videos
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate linkable markdown for cached video transcripts."
    )
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument(
        "--manifest-only",
        action="store_true",
        help="Generate only transcripts admitted to the verified WF26 media manifest.",
    )
    selection.add_argument(
        "--video-id",
        action="append",
        default=[],
        help="Generate only the named video ID; repeat as needed.",
    )
    return parser.parse_args(argv)


def render_transcript_page(video_id: str, title: str, text: str, source_path: Path, label: str) -> str:
    words = len(text.split())
    body = [
        frontmatter(
            {
                "title": f"Transcript: {title}",
                "category": "transcripts",
                "videoId": video_id,
                "sourceLabels": [label, "Cached transcript markdown"],
                "wordCount": words,
            }
        ),
        f"# Transcript: {title}",
        "",
        "## Source Video",
        f"- [YouTube](https://www.youtube.com/watch?v={video_id})",
        "",
        "## Local Cache",
        f"- `{source_path.relative_to(ROOT)}`",
        f"- {words:,} words",
        "",
        "## Transcript",
        "",
        text.strip(),
        "",
    ]
    return "\n".join(body)


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    return text[: end + 5], text[end + 5 :].lstrip()


def upsert_section(markdown: str, heading: str, section: str) -> str:
    fm, body = split_frontmatter(markdown)
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    replacement = f"## {heading}\n{section.strip()}\n"
    if pattern.search(body):
        body = pattern.sub(replacement, body).rstrip() + "\n"
    else:
        body = body.rstrip() + "\n\n" + replacement
    return fm + body


def video_ids_in_text(text: str) -> set[str]:
    ids = set(re.findall(r"youtube-([A-Za-z0-9_-]{11})(?=[\]\)\s/#-]|$)", text))
    ids.update(re.findall(r"(?:watch\?v=|youtu\.be/)([A-Za-z0-9_-]{11})", text))
    return ids


def existing_transcript_records(out_dir: Path) -> list[dict[str, object]]:
    records_by_id: dict[str, dict[str, object]] = {}
    registry = out_dir / "registry.json"
    if registry.is_file():
        loaded = json.loads(registry.read_text(encoding="utf-8"))
        if not isinstance(loaded, list):
            raise ValueError("transcript registry must contain an array")
        for item in loaded:
            if not isinstance(item, dict):
                continue
            record_id = item.get("id")
            relative_path = item.get("path")
            if not isinstance(record_id, str) or not isinstance(relative_path, str):
                continue
            page = (ROOT / relative_path).resolve()
            if page.parent != out_dir.resolve() or not page.is_file():
                continue
            records_by_id[record_id] = dict(item)

    for page in sorted(out_dir.glob("youtube-*-transcript.md")):
        match = re.fullmatch(r"youtube-([A-Za-z0-9_-]{11})-transcript", page.stem)
        if match is None or page.stem in records_by_id:
            continue
        text = page.read_text(encoding="utf-8", errors="ignore")
        title_match = re.search(r"^#\s+(.+?)\s*$", text, re.M)
        word_count_match = re.search(r"^wordCount:\s*[\"']?(\d+)", text, re.M)
        records_by_id[page.stem] = {
            "id": page.stem,
            "title": title_match.group(1) if title_match else f"Transcript: {match.group(1)}",
            "path": str(page.relative_to(ROOT)),
            "videoId": match.group(1),
            "wordCount": int(word_count_match.group(1)) if word_count_match else 0,
            "sourceLabel": "Cached transcript markdown",
        }
    return list(records_by_id.values())


def write_registry(
    records: list[dict[str, object]],
    *,
    official_video_ids: set[str],
) -> None:
    out_dir = WIKI / "transcripts"
    records_by_id = {
        str(record["id"]): record for record in existing_transcript_records(out_dir)
    }
    records_by_id.update({str(record["id"]): record for record in records})
    catalog = []
    for record in records_by_id.values():
        official = record.get("videoId") in official_video_ids
        catalog.append(
            {
                **record,
                "manifestStatus": (
                    "admitted_official_wf26"
                    if official
                    else "not_admitted_official_wf26"
                ),
                "sourceRole": "primary_event_evidence" if official else "context_only",
            }
        )

    lines = [
        frontmatter({"title": "Transcripts", "category": "transcripts", "sourceLabels": ["Cached transcript markdown"]}),
        "# Transcripts",
        "",
        "These pages expose cached YouTube and livestream transcripts as linkable wiki markdown. Official WF26 manifest entries are primary event evidence; every other retained transcript is supporting context only.",
        "",
        "## Official WF26 Event Transcripts",
    ]
    ordered = sorted(catalog, key=lambda item: str(item["title"]).lower())
    for record in ordered:
        if record["sourceRole"] != "primary_event_evidence":
            continue
        lines.append(f"- [[{record['id']}|{record['title']}]]")
    lines.extend(["", "## Supporting Context Transcripts"])
    for record in ordered:
        if record["sourceRole"] != "context_only":
            continue
        lines.append(f"- [[{record['id']}|{record['title']}]]")
    (out_dir / "index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    (out_dir / "registry.json").write_text(json.dumps(ordered, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    titles = load_titles()
    out_dir = WIKI / "transcripts"
    out_dir.mkdir(parents=True, exist_ok=True)
    transcript_ids: set[str] = set()
    records: list[dict[str, object]] = []

    official_video_ids = official_manifest_video_ids()
    selected_ids = (
        official_video_ids
        if args.manifest_only
        else set(args.video_id) if args.video_id else None
    )
    for source_path, label in transcript_paths(selected_ids):
        video_id = source_path.stem
        title = titles.get(video_id) or titleize(video_id)
        text = source_path.read_text(encoding="utf-8", errors="ignore")
        page_id = f"youtube-{video_id}-transcript"
        out = out_dir / f"{page_id}.md"
        out.write_text(render_transcript_page(video_id, title, text, source_path, label), encoding="utf-8")
        transcript_ids.add(video_id)
        records.append(
            {
                "id": page_id,
                "title": f"Transcript: {title}",
                "path": str(out.relative_to(ROOT)),
                "videoId": video_id,
                "wordCount": len(text.split()),
                "sourceLabel": label,
            }
        )

    resource_updates = 0
    for path in sorted((WIKI / "resources").glob("youtube-*.md")):
        text = path.read_text(encoding="utf-8")
        ids = video_ids_in_text(text)
        stem_match = re.match(r"youtube-([A-Za-z0-9_-]{11})$", path.stem)
        if stem_match:
            ids.add(stem_match.group(1))
        linked = sorted(video_id for video_id in ids if video_id in transcript_ids)
        if not linked:
            continue
        section = "\n".join(f"- [[youtube-{video_id}-transcript]] — full cached transcript markdown." for video_id in linked)
        updated = upsert_section(text, "Transcript Markdown", section)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            resource_updates += 1

    talk_updates = 0
    for path in sorted((WIKI / "talks").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        linked = sorted(video_id for video_id in video_ids_in_text(text) if video_id in transcript_ids)
        if not linked:
            continue
        section = "\n".join(f"- [[youtube-{video_id}-transcript]] — full cached transcript markdown for the related YouTube source." for video_id in linked)
        updated = upsert_section(text, "Transcript Markdown", section)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            talk_updates += 1

    write_registry(records, official_video_ids=official_video_ids)
    print(json.dumps({"transcript_pages": len(records), "resource_pages_updated": resource_updates, "talk_pages_updated": talk_updates}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
