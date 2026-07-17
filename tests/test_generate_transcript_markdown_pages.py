import importlib.util
import json
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "generate_transcript_markdown_pages.py"
)
SPEC = importlib.util.spec_from_file_location(
    "generate_transcript_markdown_pages_test",
    SCRIPT,
)
TRANSCRIPTS = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(TRANSCRIPTS)


def stale_talk_page() -> str:
    return (
        "# Field Guide to Fable\n\n"
        "## Media Evidence\n"
        f"{TRANSCRIPTS.STALE_NO_RELATED_VIDEO}\n\n"
        "- Source video: `youtube-I2cbIws9j10`\n"
        "- Slide deck: [[youtube-I2cbIws9j10-slides]]\n"
        "![[assets/slides/I2cbIws9j10/slide-001.jpg]]\n\n"
        "- Source video: `youtube-I2cbIws9j10`\n"
        "- Slide deck: [[youtube-I2cbIws9j10-slides]]\n"
        "![[assets/slides/I2cbIws9j10/slide-001.jpg]]\n"
        "- Additional context retained once.\n\n"
        "## Transcript Status\n"
        f"{TRANSCRIPTS.STALE_NO_OFFICIAL_TRANSCRIPT}\n"
    )


def test_manifest_mapping_projects_every_eligible_matched_talk() -> None:
    videos = [
        {
            "id": "9fubhllmsBU",
            "mediaType": "talk_recording",
            "playlistAvailability": "available",
            "playlistIndex": 27,
            "matchedTalks": ["2026-06-30-thariq-shihipar-field-guide-to-fable"],
        },
        {
            "id": "PREMIERE001",
            "mediaType": "scheduled_premiere",
            "matchedTalks": ["premiere-talk"],
        },
        {
            "id": "PRIVATE0001",
            "mediaType": "talk_recording",
            "videoAvailability": "private",
            "matchedTalks": ["private-talk"],
        },
    ]

    mapping = TRANSCRIPTS.official_recordings_by_talk(videos)

    assert list(mapping) == ["2026-06-30-thariq-shihipar-field-guide-to-fable"]
    assert (
        mapping["2026-06-30-thariq-shihipar-field-guide-to-fable"][0]["id"]
        == "9fubhllmsBU"
    )


def test_projection_replaces_stale_status_and_deduplicates_media_blocks(
    tmp_path,
    monkeypatch,
) -> None:
    root = tmp_path / "project"
    transcript_dir = root / "raw" / "sources" / "youtube-transcripts"
    transcript_dir.mkdir(parents=True)
    transcript = transcript_dir / "9fubhllmsBU.txt"
    transcript.write_text("A dedicated official transcript with useful evidence.")
    monkeypatch.setattr(TRANSCRIPTS, "ROOT", root)
    monkeypatch.setattr(
        TRANSCRIPTS,
        "TRANSCRIPT_DIRS",
        [(transcript_dir, "YouTube transcript")],
    )
    recordings = [
        {
            "id": "9fubhllmsBU",
            "title": "Field Guide to Fable — Thariq Shihipar, Anthropic",
            "mediaType": "talk_recording",
            "uploadDate": "2026-07-06",
        }
    ]

    projected = TRANSCRIPTS.project_official_media_to_talk(
        stale_talk_page(),
        recordings,
        {"9fubhllmsBU"},
    )

    assert TRANSCRIPTS.STALE_NO_RELATED_VIDEO not in projected
    assert TRANSCRIPTS.STALE_NO_OFFICIAL_TRANSCRIPT not in projected
    assert "[[youtube-9fubhllmsBU|Field Guide to Fable" in projected
    assert "dedicated official recording transcript" in projected
    assert "raw/sources/youtube-transcripts/9fubhllmsBU.txt" in projected
    assert projected.count("- Source video: `youtube-I2cbIws9j10`") == 1
    assert projected.count("![[assets/slides/I2cbIws9j10/slide-001.jpg]]") == 1
    assert projected.count("- Additional context retained once.") == 1
    assert (
        TRANSCRIPTS.project_official_media_to_talk(
            projected,
            recordings,
            {"9fubhllmsBU"},
        )
        == projected
    )


def test_non_recording_manifest_states_preserve_honest_absence_prose() -> None:
    page = stale_talk_page()

    assert TRANSCRIPTS.project_official_media_to_talk(page, [], set()) == page


def test_recording_without_cached_transcript_keeps_transcript_absence_prose() -> None:
    projected = TRANSCRIPTS.project_official_media_to_talk(
        stale_talk_page(),
        [
            {
                "id": "9fubhllmsBU",
                "title": "Field Guide to Fable",
                "mediaType": "talk_recording",
            }
        ],
        set(),
    )

    assert TRANSCRIPTS.STALE_NO_RELATED_VIDEO not in projected
    assert TRANSCRIPTS.STALE_NO_OFFICIAL_TRANSCRIPT in projected
    assert "[[youtube-9fubhllmsBU-transcript]]" not in projected


def test_main_projects_manifest_match_without_preexisting_video_link(
    tmp_path,
    monkeypatch,
) -> None:
    root = tmp_path / "project"
    wiki = root / "wiki"
    raw = root / "raw" / "sources"
    transcript_dir = raw / "youtube-transcripts"
    for directory in (
        wiki / "talks",
        wiki / "resources",
        wiki / "transcripts",
        transcript_dir,
    ):
        directory.mkdir(parents=True, exist_ok=True)
    talk_id = "2026-06-30-thariq-shihipar-field-guide-to-fable"
    (wiki / "talks" / f"{talk_id}.md").write_text(stale_talk_page())
    (transcript_dir / "9fubhllmsBU.txt").write_text(
        "Dedicated Field Guide to Fable transcript."
    )
    manifest = raw / "official-wf26-video-manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "videos": [
                    {
                        "id": "9fubhllmsBU",
                        "title": "Field Guide to Fable — Thariq Shihipar, Anthropic",
                        "mediaType": "talk_recording",
                        "playlistAvailability": "available",
                        "matchedTalks": [talk_id],
                    }
                ]
            }
        )
    )
    monkeypatch.setattr(TRANSCRIPTS, "ROOT", root)
    monkeypatch.setattr(TRANSCRIPTS, "WIKI", wiki)
    monkeypatch.setattr(TRANSCRIPTS, "RAW", raw)
    monkeypatch.setattr(TRANSCRIPTS, "OFFICIAL_VIDEO_MANIFEST", manifest)
    monkeypatch.setattr(
        TRANSCRIPTS,
        "TRANSCRIPT_DIRS",
        [(transcript_dir, "YouTube transcript")],
    )
    monkeypatch.setattr(TRANSCRIPTS, "VIDEO_CATALOG", raw / "missing-catalog.json")
    monkeypatch.setattr(TRANSCRIPTS, "IMPORT_REPORT", raw / "missing-import.json")
    monkeypatch.setattr(
        TRANSCRIPTS,
        "EXTERNAL_DISCOVERY",
        raw / "missing-external.json",
    )

    assert TRANSCRIPTS.main([]) == 0

    projected = (wiki / "talks" / f"{talk_id}.md").read_text()
    assert "[[youtube-9fubhllmsBU|Field Guide to Fable" in projected
    assert "[[youtube-9fubhllmsBU-transcript]]" in projected
    assert TRANSCRIPTS.STALE_NO_RELATED_VIDEO not in projected
    assert TRANSCRIPTS.STALE_NO_OFFICIAL_TRANSCRIPT not in projected


def test_video_id_selection_does_not_project_other_manifest_recordings(
    tmp_path,
    monkeypatch,
) -> None:
    root = tmp_path / "project"
    wiki = root / "wiki"
    raw = root / "raw" / "sources"
    transcript_dir = raw / "youtube-transcripts"
    for directory in (
        wiki / "talks",
        wiki / "resources",
        wiki / "transcripts",
        transcript_dir,
    ):
        directory.mkdir(parents=True, exist_ok=True)
    selected_id = "SELECTED001"
    other_id = "UNRELATED01"
    selected_talk = "selected-talk"
    other_talk = "other-talk"
    for talk_id in (selected_talk, other_talk):
        (wiki / "talks" / f"{talk_id}.md").write_text(stale_talk_page())
    for video_id in (selected_id, other_id):
        (transcript_dir / f"{video_id}.txt").write_text(
            f"Transcript for {video_id}."
        )
    manifest = raw / "official-wf26-video-manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "videos": [
                    {
                        "id": selected_id,
                        "title": "Selected recording",
                        "mediaType": "talk_recording",
                        "matchedTalks": [selected_talk],
                    },
                    {
                        "id": other_id,
                        "title": "Other recording",
                        "mediaType": "talk_recording",
                        "matchedTalks": [other_talk],
                    },
                ]
            }
        )
    )
    monkeypatch.setattr(TRANSCRIPTS, "ROOT", root)
    monkeypatch.setattr(TRANSCRIPTS, "WIKI", wiki)
    monkeypatch.setattr(TRANSCRIPTS, "RAW", raw)
    monkeypatch.setattr(TRANSCRIPTS, "OFFICIAL_VIDEO_MANIFEST", manifest)
    monkeypatch.setattr(
        TRANSCRIPTS,
        "TRANSCRIPT_DIRS",
        [(transcript_dir, "YouTube transcript")],
    )
    monkeypatch.setattr(TRANSCRIPTS, "VIDEO_CATALOG", raw / "missing-catalog.json")
    monkeypatch.setattr(TRANSCRIPTS, "IMPORT_REPORT", raw / "missing-import.json")
    monkeypatch.setattr(
        TRANSCRIPTS,
        "EXTERNAL_DISCOVERY",
        raw / "missing-external.json",
    )

    assert TRANSCRIPTS.main(["--video-id", selected_id]) == 0

    selected = (wiki / "talks" / f"{selected_talk}.md").read_text()
    other = (wiki / "talks" / f"{other_talk}.md").read_text()
    assert f"[[youtube-{selected_id}|Selected recording]]" in selected
    assert f"[[youtube-{other_id}|Other recording]]" not in other
    assert other == stale_talk_page()
