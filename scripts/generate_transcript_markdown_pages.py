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
STALE_NO_RELATED_VIDEO = "No related AI Engineer channel video found yet."
STALE_NO_OFFICIAL_TRANSCRIPT = (
    "No official session recording transcript was found by exact title match on the "
    "AI Engineer YouTube channel during this run."
)
PLAYABLE_VIDEO_AVAILABILITIES = {"", "public", "unlisted"}
PLAYABLE_PLAYLIST_AVAILABILITIES = {"", "available"}


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


def official_manifest_videos() -> list[dict[str, object]]:
    if not OFFICIAL_VIDEO_MANIFEST.is_file():
        return []
    value = json.loads(OFFICIAL_VIDEO_MANIFEST.read_text(encoding="utf-8"))
    videos = value.get("videos", [])
    if not isinstance(videos, list):
        raise ValueError("official WF26 video manifest must contain a videos array")
    return [
        dict(item)
        for item in videos
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    ]


def manifest_row_is_playable(item: dict[str, object]) -> bool:
    return (
        str(item.get("videoAvailability") or "").casefold()
        in PLAYABLE_VIDEO_AVAILABILITIES
        and str(item.get("playlistAvailability") or "").casefold()
        in PLAYABLE_PLAYLIST_AVAILABILITIES
    )


def official_manifest_video_ids(
    videos: list[dict[str, object]] | None = None,
) -> set[str]:
    source = videos if videos is not None else official_manifest_videos()
    return {
        str(item["id"])
        for item in source
        if item.get("mediaType") in {"talk_recording", "event_livestream"}
        and manifest_row_is_playable(item)
    }


def official_recordings_by_talk(
    videos: list[dict[str, object]],
) -> dict[str, list[dict[str, object]]]:
    recordings: dict[str, list[dict[str, object]]] = {}
    ordered = sorted(
        videos,
        key=lambda item: (
            int(item.get("playlistIndex") or 1_000_000),
            str(item.get("id") or ""),
        ),
    )
    for item in ordered:
        if item.get("mediaType") != "talk_recording":
            continue
        if not manifest_row_is_playable(item):
            continue
        matched_talks = item.get("matchedTalks")
        if not isinstance(matched_talks, list):
            continue
        for talk_id in matched_talks:
            if isinstance(talk_id, str) and talk_id:
                recordings.setdefault(talk_id, []).append(item)
    return recordings


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
    replacement = f"## {heading}\n{section.strip()}\n\n"
    if pattern.search(body):
        body = pattern.sub(replacement, body).rstrip() + "\n"
    else:
        body = body.rstrip() + "\n\n" + replacement
    return fm + body


def video_ids_in_text(text: str) -> set[str]:
    ids = set(re.findall(r"youtube-([A-Za-z0-9_-]{11})(?=[\]\)\s/#-]|$)", text))
    ids.update(re.findall(r"(?:watch\?v=|youtu\.be/)([A-Za-z0-9_-]{11})", text))
    return ids


def cached_transcript(video_id: str) -> tuple[Path | None, str]:
    for folder, label in TRANSCRIPT_DIRS:
        path = folder / f"{video_id}.txt"
        if path.is_file():
            return path, label
    return None, ""


def relative_source_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def rewrite_existing_section(markdown: str, heading: str, transform) -> str:
    fm, body = split_frontmatter(markdown)
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    match = pattern.search(body)
    if match is None:
        return markdown
    current = match.group(0).split("\n", 1)[1]
    replacement = f"## {heading}\n{transform(current).strip()}\n\n"
    body = body[: match.start()] + replacement + body[match.end() :]
    return fm + body.rstrip() + "\n"


def reconcile_generated_media_sections(
    markdown: str,
    excluded_video_ids: set[str],
) -> str:
    """Remove stale generator-owned projections while preserving manual prose."""

    if not excluded_video_ids:
        return markdown

    def update_section(heading: str, transform) -> None:
        nonlocal markdown
        fm, body = split_frontmatter(markdown)
        pattern = re.compile(
            rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", re.M | re.S
        )
        match = pattern.search(body)
        if match is None:
            return
        updated = transform(match.group(1)).strip()
        replacement = f"## {heading}\n{updated}\n\n" if updated else ""
        body = body[: match.start()] + replacement + body[match.end() :]
        markdown = fm + body.rstrip() + "\n"

    def recording_lines(section: str) -> str:
        lines: list[str] = []
        skip_evidence = False
        retained_generated_recording = False
        recording_pattern = re.compile(
            r"^- \[\[youtube-([A-Za-z0-9_-]{11})(?:\|[^\]]+)?\]\] "
            r"— official AI Engineer YouTube recording"
        )
        for line in section.splitlines():
            match = recording_pattern.match(line)
            if match:
                skip_evidence = match.group(1) in excluded_video_ids
                if skip_evidence:
                    continue
                retained_generated_recording = True
            elif skip_evidence and line.startswith("- Evidence status:"):
                skip_evidence = False
                continue
            lines.append(line)
        if not retained_generated_recording:
            lines = [
                line
                for line in lines
                if not line.startswith(
                    (
                        "- Boundary: use these recordings as media evidence;",
                        "- Boundary: use this recording as media evidence;",
                    )
                )
            ]
        return "\n".join(lines)

    def dedicated_status_lines(section: str) -> str:
        return "\n".join(
            line
            for line in section.splitlines()
            if not (
                line.startswith(
                    "Cached dedicated-session transcript text is available at"
                )
                and any(video_id in line for video_id in excluded_video_ids)
            )
        )

    def transcript_link_lines(section: str) -> str:
        generated_link = re.compile(
            r"^- \[\[youtube-([A-Za-z0-9_-]{11})-transcript\]\] —"
        )
        return "\n".join(
            line
            for line in section.splitlines()
            if not (
                (match := generated_link.match(line))
                and match.group(1) in excluded_video_ids
            )
        )

    update_section("Official YouTube Recording", recording_lines)
    update_section("Transcript Status", dedicated_status_lines)
    update_section("Transcript Markdown", transcript_link_lines)
    return markdown


def dedupe_media_source_blocks(section: str) -> str:
    prefix: list[str] = []
    order: list[str] = []
    blocks: dict[str, list[str]] = {}
    current_id: str | None = None
    marker = re.compile(r"^- Source video: `youtube-([A-Za-z0-9_-]{11})`\s*$")

    for line in section.strip().splitlines():
        match = marker.match(line)
        if match:
            current_id = match.group(1)
            if current_id not in blocks:
                order.append(current_id)
                blocks[current_id] = [line]
            continue
        if current_id is None:
            prefix.append(line)
            continue
        if line.strip() and line not in blocks[current_id]:
            blocks[current_id].append(line)

    parts = []
    if "\n".join(prefix).strip():
        parts.append("\n".join(prefix).strip())
    parts.extend("\n".join(blocks[video_id]).strip() for video_id in order)
    return "\n\n".join(parts)


def recording_section(
    recordings: list[dict[str, object]],
    cached_transcript_ids: set[str],
) -> str:
    lines: list[str] = []
    seen: set[str] = set()
    for item in recordings:
        video_id = str(item["id"])
        if video_id in seen:
            continue
        seen.add(video_id)
        title = str(item.get("title") or item.get("playlistTitle") or video_id)
        published = str(item.get("uploadDate") or item.get("releaseDate") or "")
        published_note = f" published {published}" if published else ""
        lines.append(
            f"- [[youtube-{video_id}|{title}]] — official AI Engineer YouTube "
            f"recording{published_note}."
        )
        if video_id in cached_transcript_ids:
            lines.append(
                f"- Evidence status: [[youtube-{video_id}-transcript]] — dedicated "
                "official recording transcript."
            )
    lines.append(
        "- Boundary: use these recordings as media evidence; keep date/time/room facts "
        "tied to the official schedule."
    )
    return "\n".join(lines)


def transcript_markdown_line(video_id: str, *, dedicated: bool) -> str:
    path, label = cached_transcript(video_id)
    if dedicated:
        description = "dedicated official recording transcript"
    elif path is not None and path.parent.name == "youtube-livestream-transcripts":
        description = "official livestream context transcript"
    elif path is not None and path.parent.name == "external-youtube-transcripts":
        description = "secondary-source transcript"
    else:
        description = label.lower() if label else "cached transcript"
    source = f"; source cache `{relative_source_path(path)}`" if path is not None else ""
    return f"- [[youtube-{video_id}-transcript]] — {description}{source}."


def project_official_media_to_talk(
    markdown: str,
    recordings: list[dict[str, object]],
    available_transcript_ids: set[str],
    *,
    excluded_video_ids: set[str] | None = None,
) -> str:
    if not recordings:
        return markdown

    official_ids = list(dict.fromkeys(str(item["id"]) for item in recordings))
    cached_official_ids = [
        video_id for video_id in official_ids if video_id in available_transcript_ids
    ]
    updated = upsert_section(
        markdown,
        "Official YouTube Recording",
        recording_section(recordings, set(cached_official_ids)),
    )

    def clean_media_evidence(section: str) -> str:
        lines = [
            line
            for line in section.splitlines()
            if line.strip() != STALE_NO_RELATED_VIDEO
        ]
        return dedupe_media_source_blocks("\n".join(lines))

    updated = rewrite_existing_section(updated, "Media Evidence", clean_media_evidence)
    linked_ids = list(cached_official_ids)
    linked_ids.extend(
        sorted(
            video_id
            for video_id in video_ids_in_text(updated)
            if video_id in available_transcript_ids
            and video_id not in cached_official_ids
            and video_id not in (excluded_video_ids or set())
        )
    )
    if linked_ids:
        lines = [
            transcript_markdown_line(
                video_id,
                dedicated=video_id in cached_official_ids,
            )
            for video_id in linked_ids
        ]
        updated = upsert_section(updated, "Transcript Markdown", "\n".join(lines))
    if cached_official_ids:
        status_lines = []
        for video_id in cached_official_ids:
            path, _label = cached_transcript(video_id)
            if path is None:
                continue
            words = len(path.read_text(encoding="utf-8", errors="ignore").split())
            status_lines.append(
                f"Cached dedicated-session transcript text is available at "
                f"`{relative_source_path(path)}` ({words:,} words)."
            )
        if status_lines:
            updated = upsert_section(updated, "Transcript Status", "\n".join(status_lines))
    return updated


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
        "These pages expose cached YouTube and livestream transcripts as linkable wiki markdown. Playable official WF26 talk recordings and admitted event livestreams are primary event evidence; pending, unavailable, and every other retained transcript are supporting context only.",
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

    manifest_videos = official_manifest_videos()
    official_video_ids = official_manifest_video_ids(manifest_videos)
    recordings_by_talk = official_recordings_by_talk(manifest_videos)
    all_manifest_ids = {str(item["id"]) for item in manifest_videos}
    requested_ids = set(args.video_id)
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

    cached_official_transcript_ids = {
        str(item["id"])
        for recordings in recordings_by_talk.values()
        for item in recordings
        if cached_transcript(str(item["id"]))[0] is not None
    }
    available_transcript_ids = transcript_ids | cached_official_transcript_ids
    talk_updates = 0
    for path in sorted((WIKI / "talks").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        recordings = recordings_by_talk.get(path.stem, [])
        exact_ids = {str(item["id"]) for item in recordings}
        reconciliation_scope = requested_ids if args.video_id else all_manifest_ids
        if args.video_id and not (
            exact_ids & requested_ids
            or any(video_id in text for video_id in reconciliation_scope)
        ):
            continue
        excluded_manifest_ids = reconciliation_scope - exact_ids
        updated = reconcile_generated_media_sections(text, excluded_manifest_ids)
        if recordings:
            updated = project_official_media_to_talk(
                updated,
                recordings,
                available_transcript_ids,
                excluded_video_ids=all_manifest_ids - exact_ids,
            )
        else:
            linked = sorted(
                video_id
                for video_id in video_ids_in_text(updated)
                if video_id in transcript_ids
                and video_id not in all_manifest_ids
            )
            if not linked:
                if updated == text:
                    continue
            else:
                section = "\n".join(
                    transcript_markdown_line(video_id, dedicated=False)
                    for video_id in linked
                )
                updated = upsert_section(updated, "Transcript Markdown", section)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            talk_updates += 1

    write_registry(records, official_video_ids=official_video_ids)
    print(json.dumps({"transcript_pages": len(records), "resource_pages_updated": resource_updates, "talk_pages_updated": talk_updates}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
