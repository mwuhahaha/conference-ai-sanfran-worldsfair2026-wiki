from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

import pytest

from scripts import generate_attendance_calibration as attendance


def _configure_fixture(monkeypatch, tmp_path: Path) -> tuple[Path, Path]:
    wiki = tmp_path / "wiki"
    raw = tmp_path / "raw" / "sources"
    out = raw / "attendance-calibration"
    (wiki / "talks").mkdir(parents=True)
    (wiki / "resources").mkdir(parents=True)
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
    monkeypatch.setattr(attendance, "OUT", out)
    monkeypatch.setattr(attendance, "FRAME_OUT", out / "frames")
    monkeypatch.setattr(attendance, "SHEET_OUT", out / "contact-sheets")
    monkeypatch.setattr(
        attendance,
        "ASSET_SHEET_OUT",
        wiki / "assets" / attendance.PUBLIC_ASSET_DIR,
    )
    monkeypatch.setattr(attendance, "REPORT", out / "room-report.json")
    monkeypatch.setattr(attendance, "VIDEO_REPORT", out / "video-report.json")
    monkeypatch.setattr(attendance, "VIDEO_OVERRIDES", out / "overrides.json")
    monkeypatch.setattr(
        attendance,
        "WIKI_PAGE",
        wiki / "resources" / "room-attendance-calibration.md",
    )
    monkeypatch.setattr(
        attendance,
        "VIDEO_WIKI_PAGE",
        wiki / "resources" / "video-attendance-visibility.md",
    )
    return wiki, raw


def test_module_import_does_not_require_image_dependencies() -> None:
    script = """
import builtins

original_import = builtins.__import__

def import_without_image_dependencies(name, *args, **kwargs):
    if name == "cv2" or name.startswith("cv2.") or name == "PIL" or name.startswith("PIL."):
        raise ModuleNotFoundError(f"{name} intentionally unavailable")
    return original_import(name, *args, **kwargs)

builtins.__import__ = import_without_image_dependencies
from scripts import generate_attendance_calibration
print(generate_attendance_calibration.__name__)
"""
    result = subprocess.run(
        [sys.executable, "-c", script],
        cwd=Path(__file__).resolve().parents[1],
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "scripts.generate_attendance_calibration"


def test_image_detector_reports_actionable_missing_opencv(
    monkeypatch,
    tmp_path: Path,
) -> None:
    def unavailable(_name: str):
        raise ModuleNotFoundError("cv2 intentionally unavailable")

    monkeypatch.setattr(attendance, "import_module", unavailable)

    with pytest.raises(
        attendance.AttendanceImageDependencyError,
        match=r"opencv-python-headless.*--sync-current/--check-current",
    ):
        attendance.local_people_detector_count(tmp_path / "frame.jpg")


def test_contact_sheet_reports_actionable_missing_pillow(
    monkeypatch,
    tmp_path: Path,
) -> None:
    frame_path = tmp_path / "frame.jpg"
    frame_path.write_bytes(b"not read before the dependency check")
    monkeypatch.setattr(attendance, "ROOT", tmp_path)

    def unavailable(name: str):
        if name.startswith("PIL."):
            raise ModuleNotFoundError("Pillow intentionally unavailable")
        raise AssertionError(f"unexpected import: {name}")

    monkeypatch.setattr(attendance, "import_module", unavailable)

    with pytest.raises(
        attendance.AttendanceImageDependencyError,
        match=r"Pillow.*Install `Pillow`.*--sync-current/--check-current",
    ):
        attendance.make_sheet("Main Stage", [{"path": "frame.jpg"}])


def test_collect_room_videos_admits_only_current_primary_media(
    monkeypatch,
    tmp_path: Path,
) -> None:
    wiki, raw = _configure_fixture(monkeypatch, tmp_path)
    talk_slug = "2026-07-01-garry-tan-closing-keynote-garry-tan"
    segment_talk_slug = "2026-07-01-mike-chambers-harness-engineering"
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
                    },
                    {
                        "id": "htM02KMNZnk",
                        "title": "Day 1 Stream",
                        "mediaType": "event_livestream",
                        "videoAvailability": "public",
                        "playlistAvailability": "available",
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
                    "talk_slug": segment_talk_slug,
                    "video_id": "htM02KMNZnk",
                    "start_seconds": 628,
                    "confidence": "high",
                }
            ]
        ),
        encoding="utf-8",
    )
    (wiki / "talks" / f"{segment_talk_slug}.md").write_text(
        "---\n"
        'title: "Harness Engineering"\n'
        'scheduleRoom: "Main Stage"\n'
        'scheduleTrack: "Harness Engineering"\n'
        "---\n"
        "# Harness Engineering\n",
        encoding="utf-8",
    )
    (wiki / "talks" / f"{talk_slug}.md").write_text(
        "---\n"
        'title: "Closing Keynote: Garry Tan"\n'
        'scheduleRoom: "Main Stage"\n'
        'scheduleTrack: "Keynote"\n'
        "---\n"
        "# Closing Keynote: Garry Tan\n\n"
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


def test_collect_room_videos_rejects_segment_from_demoted_stream(
    monkeypatch,
    tmp_path: Path,
) -> None:
    wiki, raw = _configure_fixture(monkeypatch, tmp_path)
    talk_slug = "2026-07-01-example-talk"
    (raw / "official-wf26-video-manifest.json").write_text(
        json.dumps(
            {
                "videos": [
                    {
                        "id": "htM02KMNZnk",
                        "mediaType": "event_livestream",
                        "videoAvailability": "private",
                        "playlistAvailability": "available",
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
                    "confidence": "high",
                }
            ]
        ),
        encoding="utf-8",
    )
    (wiki / "talks" / f"{talk_slug}.md").write_text(
        "---\n"
        'title: "Example Talk"\n'
        'scheduleRoom: "Main Stage"\n'
        "---\n"
        "# Example Talk\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="non-admitted stream"):
        attendance.collect_room_videos()


def test_attendance_authority_rejects_cross_talk_timestamp_collision(
    monkeypatch,
    tmp_path: Path,
) -> None:
    wiki, raw = _configure_fixture(monkeypatch, tmp_path)
    slugs = ["2026-07-01-first", "2026-07-01-second"]
    for slug in slugs:
        (wiki / "talks" / f"{slug}.md").write_text(
            "---\n"
            f'title: "{slug}"\n'
            'date: "2026-07-01"\n'
            'scheduleRoom: "Main Stage"\n'
            "---\n"
            f"# {slug}\n",
            encoding="utf-8",
        )
    (raw / "official-wf26-video-manifest.json").write_text(
        json.dumps(
            {
                "videos": [
                    {
                        "id": "htM02KMNZnk",
                        "title": "Day 1 Stream",
                        "mediaType": "event_livestream",
                        "videoAvailability": "public",
                        "playlistAvailability": "available",
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
                    "talk_slug": slug,
                    "video_id": "htM02KMNZnk",
                    "start_seconds": 628,
                    "date": "2026-07-01",
                    "confidence": "high",
                }
                for slug in slugs
            ]
        ),
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="livestream timestamp is attributed to multiple talks",
    ):
        attendance.collect_room_videos()


def test_attendance_authority_fails_closed_on_missing_or_malformed_inputs(
    monkeypatch,
    tmp_path: Path,
) -> None:
    wiki, raw = _configure_fixture(monkeypatch, tmp_path)
    (wiki / "talks" / "example.md").write_text(
        "---\ntitle: Example\ndate: '2026-07-01'\n---\n# Example\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="required input is missing"):
        attendance.collect_room_videos()

    (raw / "official-wf26-video-manifest.json").write_text(
        '{"videos": []}\n', encoding="utf-8"
    )
    (raw / "livestream-talk-segments.json").write_text(
        '{"not": "a list"}\n', encoding="utf-8"
    )
    with pytest.raises(ValueError, match="expected list"):
        attendance.collect_room_videos()


def test_sync_current_reuses_image_receipts_without_dependencies(
    monkeypatch,
    tmp_path: Path,
    capsys,
) -> None:
    wiki, raw = _configure_fixture(monkeypatch, tmp_path)
    talk_slug = "2026-07-01-example-talk"
    video_id = "eBUyTS7SzV4"
    evidence_key = f"{video_id}-full"
    talk_path = wiki / "talks" / f"{talk_slug}.md"
    talk_path.write_text(
        "---\n"
        'title: "Example Talk"\n'
        'scheduleRoom: "Main Stage"\n'
        'scheduleTrack: "Keynote"\n'
        "---\n"
        "# Example Talk\n\n"
        f"- [[youtube-{video_id}|Dedicated recording]]\n",
        encoding="utf-8",
    )
    (raw / "official-wf26-video-manifest.json").write_text(
        json.dumps(
            {
                "videos": [
                    {
                        "id": video_id,
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
    (raw / "livestream-talk-segments.json").write_text("[]\n", encoding="utf-8")

    frame_path = attendance.FRAME_OUT / "main-stage" / evidence_key / "frame.jpg"
    frame_path.parent.mkdir(parents=True)
    frame_path.write_bytes(b"existing frame must not be read during sync")
    contact_sheet = (
        attendance.ASSET_SHEET_OUT / "main-stage.jpg"
    )
    contact_sheet.parent.mkdir(parents=True)
    contact_sheet.write_bytes(b"existing contact sheet must be preserved")
    stale_contact_sheet = attendance.ASSET_SHEET_OUT / "stale-room.jpg"
    stale_contact_sheet.write_bytes(b"stale contact sheet must be removed")
    video = {
        "video_id": video_id,
        "title": "Example Talk",
        "track": "Keynote",
        "talk_page": str(talk_path.relative_to(tmp_path)),
        "source_kind": "candidate-session-video",
        "segment_start_seconds": None,
    }
    evidence = {
        "path": str(frame_path.relative_to(tmp_path)),
        "source": "video-cache",
        "frame_index": None,
        "time_seconds": 10.0,
        "segment_start_seconds": None,
        "video_id": video_id,
        "evidence_key": evidence_key,
        "title": "Example Talk",
        "track": "Keynote",
        "source_kind": "candidate-session-video",
    }
    attendance.REPORT.parent.mkdir(parents=True, exist_ok=True)
    attendance.REPORT.write_text(
        json.dumps(
            {
                "rooms": {
                    "Main Stage": {
                        "selected_videos": [video],
                        "used_videos": [video],
                        "videos_used": 1,
                        "primary_videos": 1,
                        "supporting_videos": 0,
                        "evidence_frames": 1,
                        "evidence": [evidence],
                        "contact_sheet": str(contact_sheet.relative_to(wiki)),
                        "calibration": attendance.inferred_calibration(
                            "Main Stage", 1, 1, 0
                        ),
                    },
                    "Stale Room": {
                        "selected_videos": [
                            {
                                **video,
                                "video_id": "I2cbIws9j10",
                            }
                        ],
                        "used_videos": [
                            {
                                **video,
                                "video_id": "I2cbIws9j10",
                            }
                        ],
                        "videos_used": 1,
                        "primary_videos": 1,
                        "supporting_videos": 0,
                        "evidence_frames": 1,
                        "evidence": [
                            {
                                **evidence,
                                "video_id": "I2cbIws9j10",
                                "evidence_key": "I2cbIws9j10-full",
                            }
                        ],
                        "contact_sheet": str(
                            stale_contact_sheet.relative_to(wiki)
                        ),
                        "calibration": attendance.inferred_calibration(
                            "Stale Room", 1, 1, 0
                        ),
                    },
                }
            }
        ),
        encoding="utf-8",
    )
    attendance.VIDEO_REPORT.write_text(
        json.dumps(
            {
                "videos": {
                    evidence_key: {
                        "detector_counts": [8, 6],
                    }
                }
            }
        ),
        encoding="utf-8",
    )

    def unavailable(_name: str):
        raise ModuleNotFoundError("cv2 intentionally unavailable")

    monkeypatch.setattr(attendance, "import_module", unavailable)
    monkeypatch.setattr(
        sys,
        "argv",
        ["generate_attendance_calibration.py", "--sync-current"],
    )

    assert attendance.main() == 0

    result = json.loads(capsys.readouterr().out)
    updated_video_report = json.loads(attendance.VIDEO_REPORT.read_text())
    assert result["allowed_evidence_keys"] == 1
    assert result["pruned_frames"] == 1
    assert updated_video_report["videos"][evidence_key]["detector_counts"] == [8, 6]
    assert updated_video_report["videos"][evidence_key]["max_visible_signal"] == 8
    assert contact_sheet.read_bytes() == b"existing contact sheet must be preserved"
    assert not stale_contact_sheet.exists()


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
