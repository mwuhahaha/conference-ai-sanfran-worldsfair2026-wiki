import importlib.util
import json
from pathlib import Path

import pytest


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "livestream_segment_projection.py"
)
SPEC = importlib.util.spec_from_file_location(
    "livestream_segment_projection_test",
    SCRIPT,
)
PROJECTION = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(PROJECTION)


def page(title: str, date: str, speakers: list[str], body: str = "") -> str:
    return (
        "---\n"
        + f"title: {json.dumps(title)}\n"
        + f"date: {json.dumps(date)}\n"
        + f"speakers: {json.dumps(speakers)}\n"
        + "---\n"
        + f"# {title}\n"
        + body
    )


def write_fixture(tmp_path: Path) -> tuple[list[str], Path]:
    talks = tmp_path / "wiki" / "talks"
    people = tmp_path / "wiki" / "people"
    raw = tmp_path / "raw"
    resource = tmp_path / "wiki" / "resources" / "livestream-talk-segments.md"
    for directory in (talks, people, raw, resource.parent):
        directory.mkdir(parents=True, exist_ok=True)

    (talks / "stream-only.md").write_text(
        page("Stream Only", "2026-07-01", ["Alice"], "\n## Notes\nkeep me\n"),
        encoding="utf-8",
    )
    (talks / "now-dedicated.md").write_text(
        page(
            "Now Dedicated",
            "2026-07-01",
            ["Bob"],
            "\n## Livestream Segment\n- stale broad link\n\n## Notes\nkeep me too\n",
        ),
        encoding="utf-8",
    )
    (talks / "removed-segment.md").write_text(
        page(
            "Removed Segment",
            "2026-07-01",
            ["Carol"],
            "\n## Livestream Segment\n- stale deleted match\n",
        ),
        encoding="utf-8",
    )
    for name in ("Alice", "Bob", "Carol"):
        (people / f"{name.lower()}.md").write_text(
            page(name, "2026-07-01", []), encoding="utf-8"
        )

    manifest = raw / "manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "videos": [
                    {
                        "id": "stream00001",
                        "mediaType": "event_livestream",
                        "title": "Day 3 Stream",
                    },
                    {
                        "id": "dedicated01",
                        "mediaType": "talk_recording",
                        "playlistAvailability": "available",
                        "videoAvailability": "public",
                        "matchedTalks": ["now-dedicated"],
                    },
                ]
            }
        ),
        encoding="utf-8",
    )
    segments = raw / "segments.json"
    segments.write_text(
        json.dumps(
            [
                {
                    "talk_slug": "stream-only",
                    "title": "Stream Only",
                    "date": "2026-07-01",
                    "speakers": ["Alice"],
                    "video_id": "stream00001",
                    "video_title": "Day 3 Stream",
                    "start_seconds": 11668,
                    "confidence": "high",
                },
                {
                    "talk_slug": "now-dedicated",
                    "title": "Now Dedicated",
                    "date": "2026-07-01",
                    "speakers": ["Bob"],
                    "video_id": "stream00001",
                    "video_title": "Day 3 Stream",
                    "start_seconds": 200,
                    "confidence": "high",
                },
            ]
        ),
        encoding="utf-8",
    )
    args = [
        "--talks-dir",
        str(talks),
        "--people-dir",
        str(people),
        "--manifest",
        str(manifest),
        "--segments",
        str(segments),
        "--resource",
        str(resource),
    ]
    return args, resource


def test_reconciles_current_segments_after_whole_page_rewrite(tmp_path: Path) -> None:
    args, resource = write_fixture(tmp_path)
    talks = tmp_path / "wiki" / "talks"
    people = tmp_path / "wiki" / "people"

    assert PROJECTION.main([*args, "--check"]) == 1
    assert PROJECTION.main(args) == 0

    current = (talks / "stream-only.md").read_text(encoding="utf-8")
    assert current.count("## Livestream Segment") == 1
    assert "I2cbIws9j10" not in current
    assert "stream00001&t=11668s" in current
    assert "## Notes\nkeep me" in current

    dedicated = (talks / "now-dedicated.md").read_text(encoding="utf-8")
    removed = (talks / "removed-segment.md").read_text(encoding="utf-8")
    assert "## Livestream Segment" not in dedicated
    assert "## Notes\nkeep me too" in dedicated
    assert "## Livestream Segment" not in removed

    alice = (people / "alice.md").read_text(encoding="utf-8")
    bob = (people / "bob.md").read_text(encoding="utf-8")
    assert "## Livestream Appearances" in alice
    assert "stream00001&t=11668s" in alice
    assert "## Livestream Appearances" not in bob

    resource_text = resource.read_text(encoding="utf-8")
    assert "[[stream-only|Stream Only]]" in resource_text
    assert "[[now-dedicated|" not in resource_text
    assert "removed-segment" not in resource_text

    stable = {
        path: path.read_bytes()
        for path in [
            talks / "stream-only.md",
            talks / "now-dedicated.md",
            talks / "removed-segment.md",
            people / "alice.md",
            people / "bob.md",
            resource,
        ]
    }
    assert PROJECTION.main([*args, "--check"]) == 0
    assert PROJECTION.main(args) == 0
    assert all(path.read_bytes() == body for path, body in stable.items())


def test_invalid_or_non_admitted_segment_fails_closed(tmp_path: Path) -> None:
    args, _resource = write_fixture(tmp_path)
    segments = Path(args[args.index("--segments") + 1])
    payload = json.loads(segments.read_text(encoding="utf-8"))
    payload[0]["confidence"] = "low"
    segments.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="not high confidence"):
        PROJECTION.main(args)

    payload[0]["confidence"] = "high"
    payload[0]["video_id"] = "missing0001"
    segments.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="non-admitted stream"):
        PROJECTION.main(args)

    manifest = Path(args[args.index("--manifest") + 1])
    manifest_payload = json.loads(manifest.read_text(encoding="utf-8"))
    manifest_payload["videos"][0]["videoAvailability"] = "private"
    manifest.write_text(json.dumps(manifest_payload), encoding="utf-8")
    payload[0]["video_id"] = "stream00001"
    segments.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="non-admitted stream"):
        PROJECTION.main(args)


def test_cross_talk_timestamp_collision_fails_closed(tmp_path: Path) -> None:
    args, _resource = write_fixture(tmp_path)
    segments = Path(args[args.index("--segments") + 1])
    payload = json.loads(segments.read_text(encoding="utf-8"))
    payload[1]["start_seconds"] = payload[0]["start_seconds"]
    segments.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(
        ValueError,
        match="livestream timestamp is attributed to multiple talks",
    ):
        PROJECTION.main(args)
