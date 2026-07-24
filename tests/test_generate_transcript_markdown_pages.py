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

SYNTHESIS_SCRIPT = (
    Path(__file__).resolve().parents[1] / "scripts" / "generate_talk_synthesis.py"
)
SYNTHESIS_SPEC = importlib.util.spec_from_file_location(
    "generate_talk_synthesis_projection_test",
    SYNTHESIS_SCRIPT,
)
SYNTHESIS = importlib.util.module_from_spec(SYNTHESIS_SPEC)
assert SYNTHESIS_SPEC.loader
SYNTHESIS_SPEC.loader.exec_module(SYNTHESIS)


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
        {
            "id": "PLAYLISTBAD",
            "mediaType": "talk_recording",
            "videoAvailability": "public",
            "playlistAvailability": "unavailable",
            "matchedTalks": ["unavailable-playlist-talk"],
        },
        {
            "id": "PLAYLISTUNK",
            "mediaType": "talk_recording",
            "videoAvailability": "public",
            "playlistAvailability": "unknown",
            "matchedTalks": ["unknown-playlist-talk"],
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


def test_part_one_projection_retires_other_parts_and_is_idempotent(
    tmp_path,
    monkeypatch,
) -> None:
    root = tmp_path / "project"
    wiki = root / "wiki"
    raw = root / "raw" / "sources"
    transcript_dir = raw / "youtube-transcripts"
    external_dir = raw / "external-youtube-transcripts"
    for directory in (
        wiki / "talks",
        wiki / "resources",
        wiki / "transcripts",
        transcript_dir,
        external_dir,
    ):
        directory.mkdir(parents=True, exist_ok=True)

    recording_id = "PARTONE0001"
    external_id = "EXTERNAL001"
    part_ids = ["part-1", "part-2", "part-3"]
    (transcript_dir / f"{recording_id}.txt").write_text(
        (
            "The Part 1 recording discusses its own bounded workshop material "
            "and keeps each workshop segment tied to exact source evidence. "
        )
        * 8
    )
    (external_dir / f"{external_id}.txt").write_text(
        "A separate interview remains useful supporting context."
    )
    for video_id in (recording_id, external_id):
        (wiki / "resources" / f"youtube-{video_id}.md").write_text(
            f"# {video_id}\n", encoding="utf-8"
        )

    for index, talk_id in enumerate(part_ids, start=1):
        stale = (
            "---\n"
            f'title: "Workshop Part {index}"\n'
            "---\n"
            f"# Workshop Part {index}\n\n"
            "## Session Description\n"
            f"This is the distinct Part {index} schedule description.\n\n"
            "## Synthesis\n"
            "### Synthesized Breakdown\n"
            "Stale synthesis copied from the Part 1 recording.\n\n"
            "### Derived Links And Source Material\n"
            f"- [[youtube-{recording_id}-transcript]] — stale.\n\n"
            "## Official YouTube Recording\n"
            f"- [[youtube-{recording_id}|Part 1 recording]] — official AI Engineer "
            "YouTube recording.\n"
            f"- Evidence status: [[youtube-{recording_id}-transcript]] — dedicated "
            "official recording transcript.\n"
            "- Boundary: use these recordings as media evidence; keep schedule facts "
            "tied to the official schedule.\n\n"
            "## Transcript Status\n"
            "Cached dedicated-session transcript text is available at "
            f"`raw/sources/youtube-transcripts/{recording_id}.txt` (10 words).\n\n"
            "## Transcript Markdown\n"
            f"- [[youtube-{recording_id}-transcript]] — dedicated official recording "
            "transcript.\n\n"
            "## Manual Notes\n"
            f"- [[youtube-{external_id}]] — preserve this unrelated manual source.\n"
        )
        (wiki / "talks" / f"{talk_id}.md").write_text(stale, encoding="utf-8")

    manifest = raw / "official-wf26-video-manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "videos": [
                    {
                        "id": recording_id,
                        "title": "Workshop Part 1",
                        "mediaType": "talk_recording",
                        "videoAvailability": "public",
                        "playlistAvailability": "available",
                        "matchedTalks": ["part-1"],
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    for module in (TRANSCRIPTS, SYNTHESIS):
        monkeypatch.setattr(module, "ROOT", root)
        monkeypatch.setattr(module, "WIKI", wiki)
        monkeypatch.setattr(module, "RAW", raw)
        monkeypatch.setattr(module, "OFFICIAL_VIDEO_MANIFEST", manifest)
    monkeypatch.setattr(
        TRANSCRIPTS,
        "TRANSCRIPT_DIRS",
        [
            (transcript_dir, "YouTube transcript"),
            (external_dir, "External YouTube secondary-source transcript"),
        ],
    )
    monkeypatch.setattr(TRANSCRIPTS, "VIDEO_CATALOG", raw / "missing-catalog.json")
    monkeypatch.setattr(TRANSCRIPTS, "IMPORT_REPORT", raw / "missing-import.json")
    monkeypatch.setattr(
        TRANSCRIPTS,
        "EXTERNAL_DISCOVERY",
        raw / "missing-external.json",
    )

    def fake_digests(jobs, **_kwargs):
        assert len(jobs) == 1
        job = jobs[0]
        excerpt = (
            "The Part 1 recording discusses its own bounded workshop material "
            "and keeps each workshop segment tied to exact source evidence."
        )
        payload = {
            "summary": (
                "The first workshop segment establishes a bounded source scope "
                "for its own material. It keeps session projection tied to exact "
                "recording evidence instead of sharing one recording across all "
                "parts. The resulting boundary lets later workshop pages retain "
                "their separate schedule identity until their own recordings are "
                "available."
            ),
            "takeaways": [
                {"text": "Keep workshop evidence bound to its exact segment.", "evidenceExcerpt": excerpt},
                {"text": "Do not project one recording across sibling sessions.", "evidenceExcerpt": excerpt},
                {"text": "Preserve separate schedule identities for later parts.", "evidenceExcerpt": excerpt},
            ],
            "claims": [
                {"text": "The recording covers only its own bounded workshop segment.", "evidenceExcerpt": excerpt, "support": "explicit"},
                {"text": "Exact source binding prevents cross-session projection.", "evidenceExcerpt": excerpt, "support": "strong"},
            ],
            "topics": [
                {"name": "Source binding", "description": "Binding recording evidence to the exact session it documents.", "evidenceExcerpt": excerpt},
                {"name": "Session projection", "description": "Projecting media only onto the schedule page supported by exact evidence.", "evidenceExcerpt": excerpt},
            ],
            "tools": [],
            "methods": [
                {"name": "Bounded session evidence", "description": "A method for preventing one recording from standing in for sibling sessions.", "evidenceExcerpt": excerpt}
            ],
            "questions": [
                {"question": "How should multipart sessions share evidence safely?", "whyItMatters": "Shared descriptions can otherwise cause one recording to contaminate sibling pages.", "evidenceExcerpt": excerpt}
            ],
            "methodNotes": "The fixture models exact session binding without external semantic execution.",
        }
        envelope = {
            "talkId": job["talk_id"],
            "talkTitle": job["title"],
            "videoId": job["video_id"],
            "payload": payload,
        }
        return [envelope], 0, 1, []

    monkeypatch.setattr(SYNTHESIS, "TRANSCRIPT_DIRS", [transcript_dir, external_dir])
    monkeypatch.setattr(SYNTHESIS, "obtain_digests", fake_digests)
    monkeypatch.setattr(
        SYNTHESIS,
        "obtain_cross_topic_synthesis",
        lambda *_args, **_kwargs: (
            {
                "payload": {
                    "clusters": [
                        {
                            "canonicalTopic": "Bounded session projection",
                            "synthesis": (
                                "The candidate records bind media evidence to one "
                                "scheduled segment. They preserve distinct session "
                                "identity when multipart descriptions overlap."
                            ),
                            "preferredExistingTopicSlug": "",
                            "memberIds": ["T0001", "T0002"],
                        }
                    ]
                }
            },
            False,
        ),
    )

    def run_generators() -> dict[str, str]:
        assert TRANSCRIPTS.main(["--manifest-only"]) == 0
        assert SYNTHESIS.main(["--all"]) == 0
        return {
            talk_id: (wiki / "talks" / f"{talk_id}.md").read_text()
            for talk_id in part_ids
        }

    first = run_generators()
    second = run_generators()

    assert second == first
    assert recording_id in first["part-1"]
    for talk_id in ("part-2", "part-3"):
        assert recording_id not in first[talk_id]
        assert external_id in first[talk_id]
