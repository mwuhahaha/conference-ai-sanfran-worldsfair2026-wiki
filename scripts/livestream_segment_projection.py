#!/usr/bin/env python3
"""Reconcile current public livestream segments onto their owned wiki surfaces.

Caption matching is intentionally out of scope here.  This cheap projector reads
the already-reviewed public segment JSON, removes segments superseded by a
playable dedicated recording, and restores the exact generated sections after
whole-page enrichers have run.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw" / "sources"
TALKS_DIR = WIKI / "talks"
PEOPLE_DIR = WIKI / "people"
MANIFEST = RAW / "official-wf26-video-manifest.json"
SEGMENTS = RAW / "livestream-talk-segments.json"
RESOURCE = WIKI / "resources" / "livestream-talk-segments.md"
VIDEO_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{11}$")


def read_json(path: Path, expected_type: type):
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"required input is missing: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(payload, expected_type):
        raise ValueError(
            f"expected {expected_type.__name__} in {path}, "
            f"got {type(payload).__name__}"
        )
    return payload


def load_manifest(path: Path = MANIFEST) -> list[dict[str, object]]:
    payload = read_json(path, dict)
    videos = payload.get("videos")
    if not isinstance(videos, list) or not all(isinstance(row, dict) for row in videos):
        raise ValueError(f"manifest videos must be a list of objects: {path}")
    return videos


def load_segments(path: Path = SEGMENTS) -> list[dict[str, object]]:
    rows = read_json(path, list)
    if not all(isinstance(row, dict) for row in rows):
        raise ValueError(f"livestream segments must be a list of objects: {path}")
    return rows


def parse_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"wiki page has no YAML frontmatter: {path}")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"wiki page has unterminated YAML frontmatter: {path}")
    try:
        fields = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML frontmatter in {path}: {exc}") from exc
    if not isinstance(fields, dict):
        raise ValueError(f"wiki page frontmatter must be a mapping: {path}")
    return fields


def as_string_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if value is None or value == "":
        return []
    return [str(value)]


def load_talks(path: Path = TALKS_DIR) -> dict[str, dict[str, object]]:
    talks: dict[str, dict[str, object]] = {}
    for page in sorted(path.glob("*.md")):
        fields = parse_frontmatter(page)
        talks[page.stem] = {
            "path": page,
            "slug": page.stem,
            "title": str(fields.get("title") or page.stem),
            "date": str(fields.get("date") or ""),
            "speakers": as_string_list(fields.get("speakers")),
        }
    return talks


def matched_talks(video: dict[str, object]) -> list[str]:
    value = video.get("matchedTalks", [])
    if not isinstance(value, list):
        raise ValueError("manifest matchedTalks must be a list")
    if any(not isinstance(slug, str) or not slug.strip() for slug in value):
        raise ValueError("manifest matchedTalks entries must be non-empty strings")
    return [slug.strip() for slug in value]


def playable_dedicated_talks(videos: list[dict[str, object]]) -> set[str]:
    return {
        slug
        for video in videos
        if video.get("mediaType") == "talk_recording"
        and video.get("playlistAvailability") == "available"
        and video.get("videoAvailability") in {"public", "unlisted"}
        for slug in matched_talks(video)
    }


def validate_and_filter_segments(
    talks: dict[str, dict[str, object]],
    videos: list[dict[str, object]],
    segments: list[dict[str, object]],
) -> list[dict[str, object]]:
    videos_by_id: dict[str, dict[str, object]] = {}
    for video in videos:
        video_id = str(video.get("id") or "")
        if not VIDEO_ID_PATTERN.fullmatch(video_id):
            raise ValueError(f"manifest video has invalid id: {video_id!r}")
        if video_id in videos_by_id:
            raise ValueError(f"duplicate manifest video id: {video_id}")
        videos_by_id[video_id] = video

    dedicated = playable_dedicated_talks(videos)
    seen: set[tuple[str, str, int]] = set()
    timestamp_owners: dict[tuple[str, int], str] = {}
    visible: list[dict[str, object]] = []
    for row in segments:
        slug = str(row.get("talk_slug") or "")
        video_id = str(row.get("video_id") or "")
        seconds = row.get("start_seconds")
        if slug not in talks:
            raise ValueError(f"livestream segment references missing talk: {slug}")
        video = videos_by_id.get(video_id)
        if (
            not video
            or video.get("mediaType") != "event_livestream"
            or video.get("videoAvailability", "") not in {"", "public", "unlisted"}
            or video.get("playlistAvailability", "") not in {"", "available"}
        ):
            raise ValueError(
                f"livestream segment {slug} references non-admitted stream: {video_id}"
            )
        if row.get("confidence") != "high":
            raise ValueError(f"livestream segment {slug} is not high confidence")
        if not isinstance(seconds, int) or seconds < 0:
            raise ValueError(f"livestream segment {slug} has invalid start_seconds")
        if str(row.get("date") or "") != str(talks[slug]["date"]):
            raise ValueError(
                f"livestream segment {slug} date does not match talk frontmatter"
            )
        key = (slug, video_id, seconds)
        if key in seen:
            raise ValueError(f"duplicate livestream segment: {key}")
        seen.add(key)
        timestamp_key = (video_id, seconds)
        previous_owner = timestamp_owners.get(timestamp_key)
        if previous_owner is not None and previous_owner != slug:
            raise ValueError(
                "livestream timestamp is attributed to multiple talks: "
                f"{timestamp_key} -> {previous_owner}, {slug}"
            )
        timestamp_owners[timestamp_key] = slug
        if slug in dedicated:
            continue
        normalized = dict(row)
        normalized["url"] = (
            f"https://www.youtube.com/watch?v={video_id}&t={seconds}s"
        )
        normalized["start_hms"] = display_hms(seconds)
        normalized["title"] = str(talks[slug]["title"])
        normalized["speakers"] = as_string_list(talks[slug]["speakers"])
        video_title = str(video.get("title") or "").strip()
        if not video_title:
            raise ValueError(f"admitted livestream {video_id} has no canonical title")
        normalized["video_title"] = video_title
        visible.append(normalized)
    return sorted(
        visible,
        key=lambda row: (
            str(row.get("date") or ""),
            str(row.get("video_id") or ""),
            int(row["start_seconds"]),
            str(row.get("talk_slug") or ""),
        ),
    )


def display_hms(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-") or "untitled"


def reconcile_section(text: str, heading: str, body: str | None) -> str:
    pattern = re.compile(rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    matches = list(pattern.finditer(text))
    if body is None:
        rendered = pattern.sub("", text)
    else:
        section = f"\n## {heading}\n{body.strip()}\n"
        if len(matches) == 1:
            rendered = pattern.sub(section.rstrip(), text, count=1)
        else:
            rendered = pattern.sub("", text).rstrip() + section
    return rendered.rstrip() + "\n"


def render_talk_body(rows: list[dict[str, object]]) -> str:
    blocks = []
    for row in rows:
        blocks.append(
            "\n".join(
                [
                    f"- [Watch in livestream at {row['start_hms']}]({row['url']}) — {row['video_title']}.",
                    "- Evidence: transcript-aligned segment validated against the official schedule and timed captions.",
                    "- Confidence: high automated match; prefer a dedicated cut-video recording when one exists.",
                ]
            )
        )
    return "\n\n".join(blocks)


def render_person_body(rows: list[dict[str, object]]) -> str:
    return "\n".join(
        f"- [[{row['talk_slug']}|{row['title']}]] — "
        f"[watch at {row['start_hms']}]({row['url']}) in {row['video_title']}."
        for row in rows
    )


def render_resource(rows: list[dict[str, object]]) -> str:
    lines = [
        "---",
        'title: "Livestream Talk Segments"',
        'category: "resources"',
        'sourceLabels: ["YouTube livestream captions", "Official conference schedule"]',
        "---",
        "",
        "# Livestream Talk Segments",
        "",
        "This page lists scheduled talks aligned to a specific timestamp inside one of the broad AI Engineer World's Fair 2026 livestreams. Each entry was validated against official schedule metadata and local timed YouTube captions; detailed matching diagnostics remain internal.",
        "",
        "Use these as navigational evidence into the livestream, not as a substitute for a cut talk video when a dedicated recording exists.",
        "",
    ]
    by_stream: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_stream[str(row["video_id"])].append(row)
    for video_id in sorted(by_stream):
        stream_rows = sorted(
            by_stream[video_id], key=lambda row: int(row["start_seconds"])
        )
        titles = {str(row["video_title"]) for row in stream_rows}
        if len(titles) != 1:
            raise ValueError(f"livestream {video_id} has conflicting titles")
        lines.extend(["", f"## {next(iter(titles))}", ""])
        for row in stream_rows:
            lines.append(
                f"- [[{row['talk_slug']}|{row['title']}]] — "
                f"[{row['start_hms']}]({row['url']}) "
                "(confidence: high; transcript-aligned segment)"
            )
    return "\n".join(lines).rstrip() + "\n"


def reconcile_livestream_segment_projections(
    talks: dict[str, dict[str, object]],
    videos: list[dict[str, object]],
    segments: list[dict[str, object]],
    *,
    people_dir: Path,
    resource_path: Path,
    write: bool,
) -> dict[str, object]:
    visible = validate_and_filter_segments(talks, videos, segments)
    by_talk: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_person: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in visible:
        by_talk[str(row["talk_slug"])].append(row)
        for speaker in row["speakers"]:
            by_person[str(speaker)].append(row)

    expected_resource = render_resource(visible)
    current_resource = (
        resource_path.read_text(encoding="utf-8") if resource_path.exists() else ""
    )
    resource_changed = current_resource != expected_resource

    talk_changes: list[Path] = []
    talk_writes: list[tuple[Path, str]] = []
    for slug, talk in sorted(talks.items()):
        path = Path(talk["path"])
        current = path.read_text(encoding="utf-8")
        rows = by_talk.get(slug, [])
        rendered = reconcile_section(
            current,
            "Livestream Segment",
            render_talk_body(rows) if rows else None,
        )
        if rendered != current:
            talk_changes.append(path)
            talk_writes.append((path, rendered))

    people_changes: list[Path] = []
    people_writes: list[tuple[Path, str]] = []
    for path in sorted(people_dir.glob("*.md")):
        current = path.read_text(encoding="utf-8")
        fields = parse_frontmatter(path)
        name = str(fields.get("title") or "")
        rows = sorted(
            by_person.get(name, []),
            key=lambda row: (
                str(row.get("date") or ""),
                int(row["start_seconds"]),
                str(row.get("talk_slug") or ""),
            ),
        )
        rendered = reconcile_section(
            current,
            "Livestream Appearances",
            render_person_body(rows) if rows else None,
        )
        if rendered != current:
            people_changes.append(path)
            people_writes.append((path, rendered))

    if write:
        for path, rendered in [*talk_writes, *people_writes]:
            path.write_text(rendered, encoding="utf-8")
        if resource_changed:
            resource_path.parent.mkdir(parents=True, exist_ok=True)
            resource_path.write_text(expected_resource, encoding="utf-8")

    return {
        "changed": bool(talk_changes or people_changes or resource_changed),
        "visible_segments": len(visible),
        "talk_pages_changed": len(talk_changes),
        "people_pages_changed": len(people_changes),
        "resource_changed": resource_changed,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--talks-dir", type=Path, default=TALKS_DIR)
    parser.add_argument("--people-dir", type=Path, default=PEOPLE_DIR)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--segments", type=Path, default=SEGMENTS)
    parser.add_argument("--resource", type=Path, default=RESOURCE)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Return non-zero when any owned projection differs without writing.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    report = reconcile_livestream_segment_projections(
        load_talks(args.talks_dir),
        load_manifest(args.manifest),
        load_segments(args.segments),
        people_dir=args.people_dir,
        resource_path=args.resource,
        write=not args.check,
    )
    report["check"] = args.check
    print(json.dumps(report, sort_keys=True))
    return 1 if args.check and report["changed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
