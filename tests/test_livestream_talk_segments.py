import json
import sys
from pathlib import Path

import pytest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from generate_livestream_talk_segments import STREAMS, dedicated_talk_slugs


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
