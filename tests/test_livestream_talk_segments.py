import json
import sys
from pathlib import Path

import pytest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import generate_livestream_talk_segments as generator
from generate_livestream_talk_segments import (
    STREAMS,
    dedicated_talk_slugs,
    manifest_admitted_streams,
)


def test_streams_are_bounded_to_distinct_event_dates() -> None:
    assert {stream["date"] for stream in STREAMS.values()} == {
        "2026-06-29",
        "2026-06-30",
        "2026-07-01",
    }


def test_dedicated_recordings_supersede_livestream_segments(tmp_path: Path) -> None:
    manifest = tmp_path / "manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "videos": [
                    {
                        "id": "dedicated01",
                        "mediaType": "talk_recording",
                        "playlistAvailability": "available",
                        "videoAvailability": "public",
                        "matchedTalks": ["talk-with-exact-recording"],
                    },
                    {
                        "id": "stream00001",
                        "mediaType": "event_livestream",
                        "matchedTalks": ["broad-stream-only"],
                    },
                    {
                        "id": "premiere001",
                        "mediaType": "scheduled_premiere",
                        "videoAvailability": "public",
                        "matchedTalks": ["scheduled-exact-recording"],
                    },
                    {
                        "id": "private0001",
                        "mediaType": "talk_recording",
                        "videoAvailability": "private",
                        "matchedTalks": ["unavailable-recording"],
                    },
                    {
                        "id": "unlisted001",
                        "mediaType": "talk_recording",
                        "playlistAvailability": "available",
                        "videoAvailability": "unlisted",
                        "matchedTalks": ["unlisted-exact-recording"],
                    },
                ]
            }
        )
    )

    assert dedicated_talk_slugs(manifest) == {
        "talk-with-exact-recording",
        "unlisted-exact-recording",
    }


def test_missing_or_invalid_manifest_aborts_matching(tmp_path: Path) -> None:
    missing = tmp_path / "missing.json"
    invalid = tmp_path / "invalid.json"
    invalid.write_text("not-json")

    with pytest.raises(FileNotFoundError, match="official media manifest"):
        dedicated_talk_slugs(missing)
    with pytest.raises(ValueError, match="invalid official media manifest"):
        dedicated_talk_slugs(invalid)


def test_manifest_admission_filters_absent_and_demoted_configured_streams(
    tmp_path: Path,
) -> None:
    configured_ids = list(STREAMS)
    manifest = tmp_path / "manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "videos": [
                    {
                        "id": configured_ids[0],
                        "mediaType": "event_livestream",
                    },
                    {
                        "id": configured_ids[1],
                        "mediaType": "talk_recording",
                    },
                    {
                        "id": configured_ids[2],
                        "mediaType": "event_livestream",
                        "videoAvailability": "private",
                    },
                ]
            }
        )
    )

    admitted = manifest_admitted_streams(manifest)

    assert set(admitted) == {configured_ids[0]}
    assert configured_ids[1] not in admitted
    assert configured_ids[2] not in admitted


def test_manifest_admission_fails_closed_when_manifest_is_missing(
    tmp_path: Path,
) -> None:
    with pytest.raises(FileNotFoundError, match="official media manifest"):
        manifest_admitted_streams(tmp_path / "missing.json")


def test_manifest_rows_must_all_be_objects(tmp_path: Path) -> None:
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps({"videos": [{"id": "stream00001"}, None]}))

    with pytest.raises(ValueError, match="must all be objects"):
        manifest_admitted_streams(manifest)


def test_yaml_frontmatter_loader_keeps_auto_summarized_talks(
    tmp_path: Path, monkeypatch
) -> None:
    wiki = tmp_path / "wiki"
    talks = wiki / "talks"
    talks.mkdir(parents=True)
    (talks / "mike.md").write_text(
        """---
title: 'Harness Engineering'
date: '2026-07-01'
time: '12:05pm-12:25pm'
track: Harness Engineering
room: Main Stage
speakers:
  - Mike Chambers
last_auto_summarized: '2026-07-18T13:17:34.278Z'
---
# Harness Engineering
""",
        encoding="utf-8",
    )
    monkeypatch.setattr(generator, "WIKI", wiki)

    loaded = generator.load_talks()

    assert [talk["slug"] for talk in loaded] == ["mike"]
    assert loaded[0]["date"] == "2026-07-01"
    assert loaded[0]["speakers"] == ["Mike Chambers"]


def test_generator_semantic_validation_precedes_every_write(
    tmp_path: Path, monkeypatch
) -> None:
    wiki = tmp_path / "wiki"
    raw = tmp_path / "raw" / "sources"
    talk = wiki / "talks" / "talk.md"
    person = wiki / "people" / "alice.md"
    resource = wiki / "resources" / "livestream-talk-segments.md"
    output = raw / "livestream-talk-segments.json"
    audit = tmp_path / ".ops" / "matches.json"
    for path in (talk, person, resource, output, audit):
        path.parent.mkdir(parents=True, exist_ok=True)
    talk.write_text(
        "---\ntitle: Talk\ndate: '2026-07-01'\nspeakers: [Alice]\n---\n"
        "# Talk\n\n## Livestream Segment\n- preserve me\n",
        encoding="utf-8",
    )
    person.write_text(
        "---\ntitle: Alice\n---\n# Alice\n\n"
        "## Livestream Appearances\n- preserve me\n",
        encoding="utf-8",
    )
    resource.write_text("preserve resource\n", encoding="utf-8")
    output.write_text('[{"preserve": true}]\n', encoding="utf-8")
    audit.write_text('[{"preserve": true}]\n', encoding="utf-8")
    before = {
        path: path.read_bytes() for path in (talk, person, resource, output, audit)
    }

    monkeypatch.setattr(generator, "WIKI", wiki)
    monkeypatch.setattr(generator, "RAW", raw)
    monkeypatch.setattr(generator, "INTERNAL_AUDIT", audit)
    monkeypatch.setattr(generator, "manifest_admitted_streams", lambda: {})
    monkeypatch.setattr(generator, "load_talks", lambda: [])
    monkeypatch.setattr(generator, "dedicated_talk_slugs", lambda: set())
    monkeypatch.setattr(
        generator,
        "load_projection_manifest",
        lambda _path: [
            {
                "id": "dedicated01",
                "mediaType": "talk_recording",
                "playlistAvailability": "available",
                "videoAvailability": "public",
                "matchedTalks": "not-a-list",
            }
        ],
    )

    with pytest.raises(ValueError, match="matchedTalks must be a list"):
        generator.main()

    assert all(path.read_bytes() == body for path, body in before.items())
