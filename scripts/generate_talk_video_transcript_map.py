#!/usr/bin/env python3
"""Generate the public WF26 talk-to-media coverage map."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw" / "sources"
TALKS_DIR = WIKI / "talks"
OFFICIAL_VIDEO_MANIFEST = RAW / "official-wf26-video-manifest.json"
LIVESTREAM_SEGMENTS = RAW / "livestream-talk-segments.json"
OUTPUT = WIKI / "resources" / "talk-video-transcript-map.md"
OFFICIAL_PLAYLIST_ID = "PLDyBmFH9HlVc"

PLAYLIST_MEDIA_TYPES = {
    "scheduled_premiere",
    "talk_recording",
    "unavailable_playlist_item",
}


def read_json(path: Path, expected_type: type) -> object:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"required input is missing: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, expected_type):
        raise ValueError(
            f"expected {expected_type.__name__} in {path}, got {type(value).__name__}"
        )
    return value


def parse_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"talk page has no YAML frontmatter: {path}")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"talk page has unterminated YAML frontmatter: {path}")
    try:
        fields = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML frontmatter in {path}: {exc}") from exc
    if not isinstance(fields, dict):
        raise ValueError(f"talk frontmatter must be a mapping: {path}")
    return fields


def as_string_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if value is None or value == "":
        return []
    return [str(value)]


def start_minutes(value: str) -> int:
    match = re.search(r"(?i)\b(\d{1,2})(?::(\d{2}))?\s*(am|pm)\b", value)
    if not match:
        return 24 * 60
    hour = int(match.group(1)) % 12
    minute = int(match.group(2) or 0)
    if match.group(3).lower() == "pm":
        hour += 12
    return hour * 60 + minute


def load_talks(path: Path = TALKS_DIR) -> list[dict[str, object]]:
    talks: list[dict[str, object]] = []
    for talk_path in sorted(path.glob("*.md")):
        fields = parse_frontmatter(talk_path)
        talks.append(
            {
                "slug": talk_path.stem,
                "title": str(fields.get("title") or talk_path.stem),
                "date": str(fields.get("date") or ""),
                "time": str(fields.get("time") or ""),
                "track": str(fields.get("track") or ""),
                "room": str(fields.get("room") or ""),
                "speakers": as_string_list(fields.get("speakers")),
            }
        )
    return sorted(
        talks,
        key=lambda talk: (
            str(talk["date"]),
            start_minutes(str(talk["time"])),
            str(talk["track"]).casefold(),
            str(talk["room"]).casefold(),
            str(talk["title"]).casefold(),
            str(talk["slug"]),
        ),
    )


def load_manifest(path: Path = OFFICIAL_VIDEO_MANIFEST) -> list[dict[str, object]]:
    payload = read_json(path, dict)
    videos = payload.get("videos")
    if not isinstance(videos, list) or not all(isinstance(video, dict) for video in videos):
        raise ValueError(f"manifest videos must be a list of objects: {path}")
    return videos


def load_segments(path: Path = LIVESTREAM_SEGMENTS) -> list[dict[str, object]]:
    segments = read_json(path, list)
    if not all(isinstance(segment, dict) for segment in segments):
        raise ValueError(f"livestream segments must be a list of objects: {path}")
    return segments


def matched_talks(video: dict[str, object]) -> list[str]:
    value = video.get("matchedTalks")
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError("matchedTalks must be a list")
    if any(not isinstance(slug, str) or not slug.strip() for slug in value):
        raise ValueError("matchedTalks entries must be non-empty strings")
    normalized = [slug.strip() for slug in value]
    if len(normalized) != len(set(normalized)):
        raise ValueError("matchedTalks entries must be unique")
    return sorted(normalized)


def is_playlist_item(video: dict[str, object]) -> bool:
    return (
        video.get("mediaType") in PLAYLIST_MEDIA_TYPES
        and isinstance(video.get("playlistIndex"), int)
        and video.get("playlistId") == OFFICIAL_PLAYLIST_ID
    )


def is_playable_recording(video: dict[str, object]) -> bool:
    return (
        is_playlist_item(video)
        and video.get("mediaType") == "talk_recording"
        and video.get("playlistAvailability") == "available"
        and video.get("videoAvailability") in {"public", "unlisted"}
    )


def playlist_sort_key(video: dict[str, object]) -> tuple[int, str]:
    index = video.get("playlistIndex")
    return (
        index if isinstance(index, int) else 1_000_000,
        str(video.get("id") or ""),
    )


def validate_inputs(
    talks: list[dict[str, object]],
    videos: list[dict[str, object]],
    segments: list[dict[str, object]],
) -> None:
    talks_by_slug = {str(talk["slug"]): talk for talk in talks}
    if len(talks_by_slug) != len(talks):
        raise ValueError("talk slugs must be unique")

    seen_ids: set[str] = set()
    playlist_positions: set[int] = set()
    stream_ids: set[str] = set()
    for video in videos:
        video_id = str(video.get("id") or "")
        if not video_id:
            raise ValueError("every manifest video must have an id")
        if video_id in seen_ids:
            raise ValueError(f"duplicate manifest video id: {video_id}")
        seen_ids.add(video_id)
        if video.get("mediaType") == "event_livestream":
            stream_ids.add(video_id)

        has_playlist_metadata = (
            video.get("playlistId") is not None
            or video.get("playlistIndex") is not None
        )
        if has_playlist_metadata:
            position = video.get("playlistIndex")
            if not isinstance(position, int) or position < 1:
                raise ValueError(f"playlist item {video_id} has invalid playlistIndex")
            if video.get("playlistId") != OFFICIAL_PLAYLIST_ID:
                raise ValueError(
                    f"playlist item {video_id} is not in the official WF26 playlist"
                )
            if video.get("mediaType") not in PLAYLIST_MEDIA_TYPES:
                raise ValueError(f"playlist item {video_id} has invalid mediaType")
            if position in playlist_positions:
                raise ValueError(f"duplicate playlistIndex: {position}")
            playlist_positions.add(position)

        if is_playlist_item(video):
            if not isinstance(video.get("matchedTalks"), list):
                raise ValueError(
                    f"playlist item {video_id} matchedTalks must be a list"
                )
            for slug in matched_talks(video):
                if slug not in talks_by_slug:
                    raise ValueError(
                        f"playlist item {video_id} references missing talk: {slug}"
                    )

    segment_keys: set[tuple[str, str, int]] = set()
    for segment in segments:
        slug = str(segment.get("talk_slug") or "")
        video_id = str(segment.get("video_id") or "")
        start_seconds = segment.get("start_seconds")
        if slug not in talks_by_slug:
            raise ValueError(f"livestream segment references missing talk: {slug}")
        segment_date = str(segment.get("date") or "")
        talk_date = str(talks_by_slug[slug].get("date") or "")
        if not segment_date or segment_date != talk_date:
            raise ValueError(
                f"livestream segment {slug} date does not match talk frontmatter"
            )
        if video_id not in stream_ids:
            raise ValueError(
                f"livestream segment {slug} references non-livestream video: {video_id}"
            )
        if not isinstance(start_seconds, int) or start_seconds < 0:
            raise ValueError(f"livestream segment {slug} has invalid start_seconds")
        if segment.get("confidence") != "high":
            raise ValueError(f"livestream segment {slug} is not high confidence")
        segment_key = (slug, video_id, start_seconds)
        if segment_key in segment_keys:
            raise ValueError(f"duplicate livestream segment: {segment_key}")
        segment_keys.add(segment_key)


def compact(value: object, fallback: str = "") -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    return text.replace("|", "&#124;") or fallback


def wiki_link(target: str, label: object | None = None) -> str:
    if label is None:
        return f"[[{target}]]"
    return f"[[{target}|{compact(label, target)}]]"


def talk_link(talk: dict[str, object]) -> str:
    return wiki_link(str(talk["slug"]), talk["title"])


def video_label(video: dict[str, object]) -> str:
    return compact(
        video.get("title") or video.get("playlistTitle"),
        str(video.get("id") or "Unknown playlist item"),
    )


def video_link(video: dict[str, object]) -> str:
    video_id = compact(video.get("id"), "unknown-video")
    return wiki_link(f"youtube-{video_id}", video_label(video))


def transcript_state(video: dict[str, object]) -> str:
    video_id = compact(video.get("id"), "unknown-video")
    status = compact(video.get("transcriptStatus"), "not reported")
    if status == "cached":
        return wiki_link(f"youtube-{video_id}-transcript", "Cached transcript")
    if status == "pending":
        return "Pending publication"
    if status == "unavailable":
        return "Unavailable"
    return f"Status {status}"


def slide_state(video: dict[str, object]) -> str:
    video_id = compact(video.get("id"), "unknown-video")
    status = compact(video.get("slideStatus"), "not reported")
    if status == "cached":
        return wiki_link(f"youtube-{video_id}-slides", "Cached extracted slides")
    if status == "no_slides":
        return "Confirmed no slide deck"
    if status == "pending":
        return "Pending publication"
    if status == "unavailable":
        return "Unavailable"
    return f"Status {status}"


def format_hms(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def exact_media_by_talk(
    videos: list[dict[str, object]],
) -> dict[str, list[dict[str, object]]]:
    mapping: dict[str, list[dict[str, object]]] = {}
    for video in sorted(videos, key=playlist_sort_key):
        if not is_playlist_item(video) or video.get("mediaType") not in {
            "scheduled_premiere",
            "talk_recording",
        }:
            continue
        for slug in matched_talks(video):
            mapping.setdefault(slug, []).append(video)
    return mapping


def exact_recording_state(video: dict[str, object]) -> str:
    if is_playable_recording(video):
        availability = compact(video.get("videoAvailability"), "available")
        return f"Playable dedicated recording ({availability}): {video_link(video)}"
    if video.get("mediaType") == "scheduled_premiere":
        return f"Scheduled premiere pending: {video_link(video)}"
    if video.get("playlistAvailability") == "unavailable":
        return f"Unavailable playlist item: {video_link(video)}"
    return f"Dedicated recording not playable: {video_link(video)}"


def join_media_states(
    media: list[dict[str, object]],
    renderer,
    missing: str,
) -> str:
    if not media:
        return missing
    return "<br>".join(renderer(video) for video in media)


def segment_navigation_state(
    segment: dict[str, object],
    videos_by_id: dict[str, dict[str, object]],
) -> str:
    video_id = str(segment["video_id"])
    seconds = int(segment["start_seconds"])
    url = f"https://www.youtube.com/watch?v={video_id}&t={seconds}s"
    return (
        f"Navigation only: [{format_hms(seconds)}]({url}) in "
        f"{video_link(videos_by_id[video_id])}"
    )


def render_schedule_coverage(
    talks: list[dict[str, object]],
    videos: list[dict[str, object]],
    broad_segments: list[dict[str, object]],
    videos_by_id: dict[str, dict[str, object]],
) -> list[str]:
    exact_by_talk = exact_media_by_talk(videos)
    broad_by_talk: dict[str, list[dict[str, object]]] = {}
    for segment in broad_segments:
        broad_by_talk.setdefault(str(segment["talk_slug"]), []).append(segment)
    lines = [
        "| Date | Time | Track / room | Scheduled talk | Speakers | Exact recording state | Transcript | Slides | Broad navigation state |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for talk in talks:
        slug = str(talk["slug"])
        media = exact_by_talk.get(slug, [])
        navigation = "<br>".join(
            segment_navigation_state(segment, videos_by_id)
            for segment in broad_by_talk.get(slug, [])
        ) or "No public segment mapping"
        location = " / ".join(
            value
            for value in (compact(talk["track"]), compact(talk["room"]))
            if value
        ) or "Not listed"
        speakers = ", ".join(compact(speaker) for speaker in talk["speakers"])
        lines.append(
            "| "
            + " | ".join(
                [
                    compact(talk["date"], "Not listed"),
                    compact(talk["time"], "Not listed"),
                    location,
                    talk_link(talk),
                    speakers or "Not listed",
                    join_media_states(
                        media,
                        exact_recording_state,
                        "No dedicated playlist mapping",
                    ),
                    join_media_states(media, transcript_state, "Not applicable"),
                    join_media_states(media, slide_state, "Not applicable"),
                    navigation,
                ]
            )
            + " |"
        )
    return lines


def render_dedicated_recordings(
    videos: list[dict[str, object]],
    talks_by_slug: dict[str, dict[str, object]],
) -> list[str]:
    lines = [
        "| Playlist | Scheduled talk | Official recording | Transcript | Slides |",
        "|---:|---|---|---|---|",
    ]
    for video in sorted(videos, key=playlist_sort_key):
        if not is_playable_recording(video):
            continue
        for slug in matched_talks(video):
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(video["playlistIndex"]),
                        talk_link(talks_by_slug[slug]),
                        video_link(video),
                        transcript_state(video),
                        slide_state(video),
                    ]
                )
                + " |"
            )
    return lines


def render_pending_premieres(
    videos: list[dict[str, object]],
    talks_by_slug: dict[str, dict[str, object]],
) -> list[str]:
    lines = [
        "| Playlist | Scheduled talk | Premiere | Release | Transcript | Slides |",
        "|---:|---|---|---|---|---|",
    ]
    for video in sorted(videos, key=playlist_sort_key):
        if not is_playlist_item(video) or video.get("mediaType") != "scheduled_premiere":
            continue
        slugs = matched_talks(video)
        schedule = "<br>".join(talk_link(talks_by_slug[slug]) for slug in slugs)
        lines.append(
            "| "
            + " | ".join(
                [
                    str(video["playlistIndex"]),
                    schedule or "No schedule mapping",
                    video_link(video),
                    compact(video.get("releaseDate"), "Not announced"),
                    transcript_state(video),
                    slide_state(video),
                ]
            )
            + " |"
        )
    return lines


def visible_segments(
    videos: list[dict[str, object]],
    segments: list[dict[str, object]],
) -> list[dict[str, object]]:
    recorded_slugs = {
        slug
        for video in videos
        if is_playable_recording(video)
        for slug in matched_talks(video)
    }
    return sorted(
        (
            segment
            for segment in segments
            if str(segment.get("talk_slug") or "") not in recorded_slugs
        ),
        key=lambda segment: (
            str(segment.get("date") or ""),
            str(segment.get("video_id") or ""),
            int(segment["start_seconds"]),
            str(segment.get("talk_slug") or ""),
        ),
    )


def render_livestream_navigation(
    segments: list[dict[str, object]],
    talks_by_slug: dict[str, dict[str, object]],
    videos_by_id: dict[str, dict[str, object]],
) -> list[str]:
    lines = [
        "| Date | Scheduled talk | Broad livestream | Timestamp |",
        "|---|---|---|---:|",
    ]
    for segment in segments:
        slug = str(segment["talk_slug"])
        video_id = str(segment["video_id"])
        seconds = int(segment["start_seconds"])
        stream = videos_by_id[video_id]
        url = f"https://www.youtube.com/watch?v={video_id}&t={seconds}s"
        lines.append(
            "| "
            + " | ".join(
                [
                    compact(talks_by_slug[slug]["date"], "Not listed"),
                    talk_link(talks_by_slug[slug]),
                    video_link(stream),
                    f"[{format_hms(seconds)}]({url})",
                ]
            )
            + " |"
        )
    return lines


def render_unmatched_recordings(videos: list[dict[str, object]]) -> list[str]:
    lines = [
        "| Playlist | Recording | Transcript | Slides | Schedule relationship |",
        "|---:|---|---|---|---|",
    ]
    for video in sorted(videos, key=playlist_sort_key):
        if not is_playable_recording(video) or matched_talks(video):
            continue
        lines.append(
            "| "
            + " | ".join(
                [
                    str(video["playlistIndex"]),
                    video_link(video),
                    transcript_state(video),
                    slide_state(video),
                    "No exact schedule mapping",
                ]
            )
            + " |"
        )
    return lines


def unavailable_items(videos: list[dict[str, object]]) -> list[dict[str, object]]:
    return sorted(
        [
            video
            for video in videos
            if is_playlist_item(video)
            and (
                video.get("mediaType") == "unavailable_playlist_item"
                or video.get("playlistAvailability") == "unavailable"
            )
        ],
        key=playlist_sort_key,
    )


def render_unavailable_items(videos: list[dict[str, object]]) -> list[str]:
    lines = [
        "| Playlist | Item | Availability | Reason | Transcript | Slides |",
        "|---:|---|---|---|---|---|",
    ]
    for video in videos:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(video["playlistIndex"]),
                    video_link(video),
                    "Unavailable playlist item",
                    compact(video.get("unavailableReason"), "Not reported"),
                    transcript_state(video),
                    slide_state(video),
                ]
            )
            + " |"
        )
    return lines


def render_map(
    talks: list[dict[str, object]],
    videos: list[dict[str, object]],
    segments: list[dict[str, object]],
) -> str:
    validate_inputs(talks, videos, segments)
    talks_by_slug = {str(talk["slug"]): talk for talk in talks}
    videos_by_id = {str(video["id"]): video for video in videos}
    playlist_items = sorted(
        [video for video in videos if is_playlist_item(video)],
        key=playlist_sort_key,
    )
    playable = [video for video in playlist_items if is_playable_recording(video)]
    matched_playable = [video for video in playable if matched_talks(video)]
    unmatched_playable = [video for video in playable if not matched_talks(video)]
    pending = [
        video
        for video in playlist_items
        if video.get("mediaType") == "scheduled_premiere"
    ]
    unavailable = unavailable_items(playlist_items)
    broad_segments = visible_segments(videos, segments)
    talk_edges = sum(len(matched_talks(video)) for video in matched_playable)

    lines = [
        "---",
        'title: "Talk Video Transcript Map"',
        'category: "resources"',
        'sourceLabels: ["Official conference schedule", "Official WF26 playlist membership", "YouTube livestream captions"]',
        "---",
        "",
        "# Talk Video Transcript Map",
        "",
        "## Source Boundary",
        "The official schedule owns session titles, speakers, dates, times, tracks, and rooms. Official WF26 playlist membership establishes event association for the media items below.",
        "",
        "Recording, transcript, and slide states are projected onto scheduled talks only when the manifest contains an exact mapping. Playlist-only artifacts for unmatched recordings remain inventoried without attributing them to a scheduled talk. Broad livestream timestamps are navigation into full-event recordings; they are not dedicated session recordings and do not establish session-specific transcript or slide evidence.",
        "",
        "Only the public evidence states and relationships described above are included; loose speaker/title matches from unrelated videos are excluded.",
        "",
        "## Coverage Summary",
        f"- Scheduled talks: {len(talks)}",
        f"- Official playlist items: {len(playlist_items)}",
        f"- Playable dedicated recordings: {len(playable)}",
        f"- Playable recordings with exact schedule mappings: {len(matched_playable)} videos across {talk_edges} talk mappings",
        f"- Unmatched playable recordings: {len(unmatched_playable)}",
        f"- Cached recording transcripts: {sum(video.get('transcriptStatus') == 'cached' for video in playable)}",
        f"- Cached recording slide sets: {sum(video.get('slideStatus') == 'cached' for video in playable)}",
        f"- Confirmed no-slide recordings: {sum(video.get('slideStatus') == 'no_slides' for video in playable)}",
        f"- Pending scheduled premieres: {len(pending)}",
        f"- Broad livestream navigation entries: {len(broad_segments)}",
        f"- Unavailable playlist items: {len(unavailable)}",
        "",
        "## Schedule Coverage",
        "",
        "Every scheduled talk appears once below. Exact media columns use only official playlist mappings; broad navigation remains a separate state and never supplies transcript or slide status.",
        "",
    ]
    lines.extend(
        render_schedule_coverage(
            talks,
            videos,
            broad_segments,
            videos_by_id,
        )
    )
    lines.extend(
        [
        "",
        "## Dedicated Session Recordings",
        "",
        ]
    )
    lines.extend(render_dedicated_recordings(videos, talks_by_slug))
    lines.extend(["", "## Pending Scheduled Premieres", ""])
    lines.extend(render_pending_premieres(videos, talks_by_slug))
    lines.extend(
        [
            "",
            "## Broad Livestream Navigation",
            "",
            "These timestamp links are navigation-only. A playable dedicated recording suppresses the same talk's broad-stream link; a pending premiere does not suppress still-useful navigation.",
            "",
        ]
    )
    if broad_segments:
        lines.extend(
            render_livestream_navigation(
                broad_segments, talks_by_slug, videos_by_id
            )
        )
    else:
        lines.append("No public broad-livestream navigation entries are currently mapped.")
    lines.extend(["", "## Unmatched Playable Playlist Recordings", ""])
    lines.extend(render_unmatched_recordings(videos))
    lines.extend(["", "## Unavailable Playlist Items", ""])
    lines.extend(render_unavailable_items(unavailable))
    return "\n".join(lines).rstrip() + "\n"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate the public WF26 talk-to-media coverage map."
    )
    parser.add_argument("--talks-dir", type=Path, default=TALKS_DIR)
    parser.add_argument("--manifest", type=Path, default=OFFICIAL_VIDEO_MANIFEST)
    parser.add_argument("--segments", type=Path, default=LIVESTREAM_SEGMENTS)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Return non-zero if the generated output differs without writing it.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    rendered = render_map(
        load_talks(args.talks_dir),
        load_manifest(args.manifest),
        load_segments(args.segments),
    )
    current = args.output.read_text(encoding="utf-8") if args.output.exists() else ""
    changed = current != rendered
    if not args.check and changed:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(
        json.dumps(
            {
                "changed": changed,
                "check": args.check,
                "output": str(args.output),
            },
            sort_keys=True,
        )
    )
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
