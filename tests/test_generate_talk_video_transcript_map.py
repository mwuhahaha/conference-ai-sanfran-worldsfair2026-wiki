import copy
import importlib.util
import json
from pathlib import Path

import pytest


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "generate_talk_video_transcript_map.py"
)
SPEC = importlib.util.spec_from_file_location(
    "generate_talk_video_transcript_map_test",
    SCRIPT,
)
MEDIA_MAP = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MEDIA_MAP)


def write_talks(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    pages = {
        "talk-a.md": """---
title: "Published Talk"
category: talks
date: "2026-06-29"
time: "9:00am-9:20am"
track: Main Stage
room: Main Stage
speakers: ["Alice"]
---
# Published Talk
""",
        "talk-b.md": """---
title: >-
  Recording Without
  Slides
category: talks
date: '2026-06-29'
time: '10:00am-10:20am'
track: Main Stage
room: Main Stage
speakers:
  - Bob
  - Bea
---
# Recording Without Slides
""",
        "talk-c.md": """---
title: 'Stream Only Talk'
category: talks
date: '2026-06-29'
time: '11:00am-11:20am'
track: Main Stage
room: Main Stage
speakers: []
---
# Stream Only Talk
""",
        "talk-d.md": """---
title: Pending Talk
category: talks
date: '2026-06-29'
time: '12:00pm-12:20pm'
track: Main Stage
room: Main Stage
speakers:
  - Devon
---
# Pending Talk
""",
        "talk-e.md": """---
title: No Media Talk
category: talks
date: '2026-06-29'
time: '1:00pm-1:20pm'
track: Main Stage
room: Main Stage
speakers:
  - Erin
---
# No Media Talk
""",
    }
    for name, content in pages.items():
        (directory / name).write_text(content, encoding="utf-8")


def fixture_payloads() -> tuple[list[dict], list[dict]]:
    videos = [
        {
            "id": "AAAAAAAAAAA",
            "title": "Published recording",
            "mediaType": "talk_recording",
            "playlistId": MEDIA_MAP.OFFICIAL_PLAYLIST_ID,
            "playlistIndex": 1,
            "playlistAvailability": "available",
            "videoAvailability": "public",
            "transcriptStatus": "cached",
            "slideStatus": "cached",
            "matchedTalks": ["talk-a"],
        },
        {
            "id": "BBBBBBBBBBB",
            "title": "Recording without slides",
            "mediaType": "talk_recording",
            "playlistId": MEDIA_MAP.OFFICIAL_PLAYLIST_ID,
            "playlistIndex": 2,
            "playlistAvailability": "available",
            "videoAvailability": "unlisted",
            "transcriptStatus": "cached",
            "slideStatus": "no_slides",
            "matchedTalks": ["talk-b"],
        },
        {
            "id": "DDDDDDDDDDD",
            "title": "Scheduled premiere",
            "mediaType": "scheduled_premiere",
            "playlistId": MEDIA_MAP.OFFICIAL_PLAYLIST_ID,
            "playlistIndex": 3,
            "playlistAvailability": "available",
            "videoAvailability": "public",
            "transcriptStatus": "pending",
            "slideStatus": "pending",
            "releaseDate": "2026-07-20",
            "matchedTalks": ["talk-d"],
        },
        {
            "id": "UUUUUUUUUUU",
            "title": "Unmatched recording",
            "mediaType": "talk_recording",
            "playlistId": MEDIA_MAP.OFFICIAL_PLAYLIST_ID,
            "playlistIndex": 4,
            "playlistAvailability": "available",
            "videoAvailability": "public",
            "transcriptStatus": "cached",
            "slideStatus": "cached",
            "matchedTalks": [],
        },
        {
            "id": "XXXXXXXXXXX",
            "title": "",
            "mediaType": "unavailable_playlist_item",
            "playlistId": MEDIA_MAP.OFFICIAL_PLAYLIST_ID,
            "playlistIndex": 5,
            "playlistAvailability": "unavailable",
            "videoAvailability": "unknown",
            "transcriptStatus": "unavailable",
            "slideStatus": "unavailable",
            "unavailableReason": "private",
            "matchedTalks": [],
        },
        {
            "id": "SSSSSSSSSSS",
            "title": "Event livestream",
            "mediaType": "event_livestream",
            "matchedTalks": [],
        },
        {
            "id": "LLLLLLLLLLL",
            "title": "Legacy non-playlist admission",
            "mediaType": "talk_recording",
            "matchedTalks": [],
        },
    ]
    segments = [
        {
            "talk_slug": "talk-b",
            "video_id": "SSSSSSSSSSS",
            "date": "2026-06-29",
            "start_seconds": 100,
            "confidence": "high",
            "evidence_excerpt": "unrelated excerpt",
        },
        {
            "talk_slug": "talk-c",
            "video_id": "SSSSSSSSSSS",
            "date": "2026-06-29",
            "start_seconds": 200,
            "confidence": "high",
            "confidence_score": 999,
        },
        {
            "talk_slug": "talk-d",
            "video_id": "SSSSSSSSSSS",
            "date": "2026-06-29",
            "start_seconds": 300,
            "confidence": "high",
        },
    ]
    return videos, segments


def write_inputs(tmp_path: Path) -> tuple[Path, Path, Path]:
    talks = tmp_path / "wiki" / "talks"
    write_talks(talks)
    videos, segments = fixture_payloads()
    raw = tmp_path / "raw"
    raw.mkdir()
    manifest = raw / "manifest.json"
    manifest.write_text(json.dumps({"videos": list(reversed(videos))}), encoding="utf-8")
    segment_path = raw / "segments.json"
    segment_path.write_text(json.dumps(list(reversed(segments))), encoding="utf-8")
    return talks, manifest, segment_path


def render_fixture(tmp_path: Path) -> str:
    talks, manifest, segments = write_inputs(tmp_path)
    return MEDIA_MAP.render_map(
        MEDIA_MAP.load_talks(talks),
        MEDIA_MAP.load_manifest(manifest),
        MEDIA_MAP.load_segments(segments),
    )


def test_media_sections_preserve_exact_states_and_boundary(tmp_path: Path) -> None:
    rendered = render_fixture(tmp_path)

    assert "## Dedicated Session Recordings" in rendered
    assert "[[talk-a|Published Talk]]" in rendered
    assert "[[youtube-AAAAAAAAAAA-transcript|Cached transcript]]" in rendered
    assert "[[youtube-AAAAAAAAAAA-slides|Cached extracted slides]]" in rendered
    assert "[[talk-b|Recording Without Slides]]" in rendered
    assert "Confirmed no slide deck" in rendered
    assert "[[youtube-BBBBBBBBBBB-slides" not in rendered
    assert "## Pending Scheduled Premieres" in rendered
    assert "[[talk-d|Pending Talk]]" in rendered
    assert "2026-07-20" in rendered
    assert "[[youtube-DDDDDDDDDDD-transcript" not in rendered
    assert "[[youtube-DDDDDDDDDDD-slides" not in rendered
    assert "Pending publication" in rendered


def test_schedule_coverage_contains_every_talk_including_no_media(
    tmp_path: Path,
) -> None:
    rendered = render_fixture(tmp_path)
    schedule = rendered.split("## Schedule Coverage", 1)[1].split(
        "## Dedicated Session Recordings", 1
    )[0]

    for slug in ("talk-a", "talk-b", "talk-c", "talk-d", "talk-e"):
        assert schedule.count(f"[[{slug}|") == 1
    no_media_row = next(line for line in schedule.splitlines() if "[[talk-e|" in line)
    assert "No dedicated playlist mapping" in no_media_row
    assert no_media_row.count("Not applicable") == 2
    assert "No public segment mapping" in no_media_row


def test_playable_cut_suppresses_stream_but_pending_premiere_does_not(
    tmp_path: Path,
) -> None:
    rendered = render_fixture(tmp_path)

    assert "&t=100s" not in rendered
    assert "&t=200s" in rendered
    assert "&t=300s" in rendered
    assert "unrelated excerpt" not in rendered
    assert "confidence_score" not in rendered
    assert "confidence: high" not in rendered
    assert "score" not in rendered.lower()
    assert "ranking" not in rendered.lower()
    assert "Related video" not in rendered
    assert "None found" not in rendered


def test_inventory_is_partitioned_and_excludes_non_playlist_admissions(
    tmp_path: Path,
) -> None:
    rendered = render_fixture(tmp_path)

    assert "## Unmatched Playable Playlist Recordings" in rendered
    assert "[[youtube-UUUUUUUUUUU|Unmatched recording]]" in rendered
    assert "No exact schedule mapping" in rendered
    assert "## Unavailable Playlist Items" in rendered
    assert "[[youtube-XXXXXXXXXXX|XXXXXXXXXXX]]" in rendered
    assert "| private | Unavailable | Unavailable |" in rendered
    assert "Legacy non-playlist admission" not in rendered
    assert "Official playlist items: 5" in rendered
    assert "Playable dedicated recordings: 3" in rendered


def test_multi_talk_edges_and_input_order_are_deterministic(tmp_path: Path) -> None:
    talks_dir = tmp_path / "talks"
    write_talks(talks_dir)
    talks = MEDIA_MAP.load_talks(talks_dir)
    videos, segments = fixture_payloads()
    videos[0]["matchedTalks"] = ["talk-c", "talk-a"]
    segments = [segment for segment in segments if segment["talk_slug"] != "talk-c"]

    first = MEDIA_MAP.render_map(talks, videos, segments)
    videos[0]["matchedTalks"] = ["talk-a", "talk-c"]
    second = MEDIA_MAP.render_map(talks, list(reversed(videos)), list(reversed(segments)))

    assert first == second
    assert "2 videos across 3 talk mappings" in first
    dedicated = first.split("## Dedicated Session Recordings", 1)[1].split(
        "## Pending Scheduled Premieres", 1
    )[0]
    assert dedicated.count("[[youtube-AAAAAAAAAAA|Published recording]]") == 2


def test_missing_talk_reference_fails_instead_of_emitting_broken_link(
    tmp_path: Path,
) -> None:
    talks_dir = tmp_path / "talks"
    write_talks(talks_dir)
    videos, segments = fixture_payloads()
    videos[0]["matchedTalks"] = ["missing-talk"]

    with pytest.raises(ValueError, match="references missing talk"):
        MEDIA_MAP.render_map(MEDIA_MAP.load_talks(talks_dir), videos, segments)


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda video: video.update(matchedTalks="talk-a"), "must be a list"),
        (lambda video: video.update(matchedTalks=None), "must be a list"),
        (lambda video: video.update(matchedTalks=[123]), "non-empty strings"),
        (
            lambda video: video.update(playlistId="unrelated-playlist"),
            "not in the official WF26 playlist",
        ),
    ],
)
def test_invalid_playlist_mapping_schema_fails(
    tmp_path: Path,
    mutation,
    message: str,
) -> None:
    talks_dir = tmp_path / "talks"
    write_talks(talks_dir)
    videos, segments = fixture_payloads()
    mutation(videos[0])

    with pytest.raises(ValueError, match=message):
        MEDIA_MAP.render_map(MEDIA_MAP.load_talks(talks_dir), videos, segments)


def test_invalid_or_duplicate_livestream_segments_fail(tmp_path: Path) -> None:
    talks_dir = tmp_path / "talks"
    write_talks(talks_dir)
    videos, segments = fixture_payloads()
    segments[0]["confidence"] = "low"
    with pytest.raises(ValueError, match="not high confidence"):
        MEDIA_MAP.render_map(MEDIA_MAP.load_talks(talks_dir), videos, segments)

    videos, segments = fixture_payloads()
    segments.append(copy.deepcopy(segments[0]))
    with pytest.raises(ValueError, match="duplicate livestream segment"):
        MEDIA_MAP.render_map(MEDIA_MAP.load_talks(talks_dir), videos, segments)

    videos, segments = fixture_payloads()
    segments[0]["date"] = "2026-07-01"
    with pytest.raises(ValueError, match="date does not match talk frontmatter"):
        MEDIA_MAP.render_map(MEDIA_MAP.load_talks(talks_dir), videos, segments)


def test_cli_write_and_check_are_idempotent(tmp_path: Path) -> None:
    talks, manifest, segments = write_inputs(tmp_path)
    output = tmp_path / "wiki" / "resources" / "talk-video-transcript-map.md"
    args = [
        "--talks-dir",
        str(talks),
        "--manifest",
        str(manifest),
        "--segments",
        str(segments),
        "--output",
        str(output),
    ]

    assert MEDIA_MAP.main(args) == 0
    first = output.read_bytes()
    assert MEDIA_MAP.main([*args, "--check"]) == 0
    assert MEDIA_MAP.main(args) == 0
    assert output.read_bytes() == first

    output.write_text("stale\n", encoding="utf-8")
    assert MEDIA_MAP.main([*args, "--check"]) == 1
    assert output.read_text(encoding="utf-8") == "stale\n"


def test_checked_in_map_matches_default_inputs() -> None:
    assert MEDIA_MAP.main(["--check"]) == 0
