from __future__ import annotations

import json
from pathlib import Path

from scripts import generate_attendance_calibration as attendance


def _configure_fixture(monkeypatch, tmp_path: Path) -> tuple[Path, Path]:
    wiki = tmp_path / "wiki"
    raw = tmp_path / "raw" / "sources"
    (wiki / "talks").mkdir(parents=True)
    raw.mkdir(parents=True)
    monkeypatch.setattr(attendance, "ROOT", tmp_path)
    monkeypatch.setattr(attendance, "WIKI", wiki)
    monkeypatch.setattr(attendance, "RAW", raw)
    monkeypatch.setattr(attendance, "VIDEO_CACHE", tmp_path / "raw" / "video-cache")
    monkeypatch.setattr(
        attendance,
        "FRAME_CACHE",
        tmp_path / "raw" / "slide-frames-tmp",
    )
    monkeypatch.setattr(
        attendance,
        "MEDIA_MANIFEST",
        raw / "official-wf26-video-manifest.json",
    )
    monkeypatch.setattr(
        attendance,
        "LIVESTREAM_SEGMENTS",
        raw / "livestream-talk-segments.json",
    )
    return wiki, raw


def test_collect_room_videos_admits_only_current_primary_media(
    monkeypatch,
    tmp_path: Path,
) -> None:
    wiki, raw = _configure_fixture(monkeypatch, tmp_path)
    talk_slug = "2026-07-01-garry-tan-closing-keynote-garry-tan"
    (raw / "official-wf26-video-manifest.json").write_text(
        json.dumps(
            {
                "videos": [
                    {
                        "id": "eBUyTS7SzV4",
                        "mediaType": "talk_recording",
                        "videoAvailability": "public",
                        "playlistAvailability": "available",
                        "matchedTalks": [talk_slug],
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    (raw / "livestream-talk-segments.json").write_text(
        json.dumps(
            [
                {
                    "talk_slug": talk_slug,
                    "video_id": "htM02KMNZnk",
                    "start_seconds": 628,
                }
            ]
        ),
        encoding="utf-8",
    )
    (wiki / "talks" / f"{talk_slug}.md").write_text(
        "---\n"
        'title: "Closing Keynote: Garry Tan"\n'
        'scheduleRoom: "Main Stage"\n'
        'scheduleTrack: "Keynote"\n'
        "---\n"
        "# Closing Keynote: Garry Tan\n\n"
        "- [[youtube-eBUyTS7SzV4|Dedicated recording]]\n"
        "- https://www.youtube.com/watch?v=htM02KMNZnk&t=628s\n"
        "- https://www.youtube.com/watch?v=I2cbIws9j10&t=28640s\n"
        "- https://www.youtube.com/watch?v=abc12345678\n"
        "- speaker-match related prior/adjacent: "
        "https://www.youtube.com/watch?v=SUPPORT1234\n",
        encoding="utf-8",
    )

    rows = attendance.collect_room_videos()["Main Stage"]
    found = {
        (
            row["video_id"],
            row["source_kind"],
            row["segment_start_seconds"],
        )
        for row in rows
    }

    assert found == {
        ("eBUyTS7SzV4", "candidate-session-video", None),
        ("htM02KMNZnk", "worldsfair-livestream-segment", 628),
        ("SUPPORT1234", "supporting-related-video", None),
    }


def test_stale_evidence_keys_flags_removed_segment(monkeypatch, tmp_path: Path) -> None:
    wiki, raw = _configure_fixture(monkeypatch, tmp_path)
    monkeypatch.setattr(attendance, "REPORT", raw / "room-report.json")
    monkeypatch.setattr(attendance, "VIDEO_REPORT", raw / "video-report.json")
    (raw / "official-wf26-video-manifest.json").write_text(
        json.dumps({"videos": []}),
        encoding="utf-8",
    )
    (raw / "livestream-talk-segments.json").write_text("[]\n", encoding="utf-8")
    (attendance.REPORT).write_text(
        json.dumps(
            {
                "rooms": {
                    "Main Stage": {
                        "selected_videos": [
                            {
                                "video_id": "I2cbIws9j10",
                                "segment_start_seconds": 28640,
                            }
                        ],
                        "used_videos": [],
                    }
                }
            }
        ),
        encoding="utf-8",
    )
    attendance.VIDEO_REPORT.write_text(
        json.dumps({"videos": {"I2cbIws9j10-t28640": {}}}),
        encoding="utf-8",
    )

    assert attendance.stale_evidence_keys() == {"I2cbIws9j10-t28640"}
