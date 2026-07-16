#!/usr/bin/env python3
"""Classify YouTube resource pages by source role for the World's Fair wiki."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "sources"
WIKI = ROOT / "wiki"
RESOURCES = WIKI / "resources"
OFFICIAL_VIDEO_MANIFEST = RAW / "official-wf26-video-manifest.json"


def read_json(path: Path, fallback):
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8", errors="ignore"))


def wf26_title(title: str) -> bool:
    low = title.lower()
    return "wf2026" in low or "wf26" in low or ("world" in low and "fair" in low and "2026" in low)


def official_wf_livestream_ids() -> set[str]:
    blob = read_json(RAW / "aidotengineer-channel-streams-latest.json", {})
    entries = blob.get("entries") if isinstance(blob, dict) else blob
    ids: set[str] = set()
    for entry in entries or []:
        video_id = entry.get("id") or entry.get("video_id")
        title = entry.get("title") or ""
        if video_id and wf26_title(title):
            ids.add(video_id)
    manifest = read_json(OFFICIAL_VIDEO_MANIFEST, {})
    ids.update(
        str(item.get("id"))
        for item in manifest.get("videos", [])
        if isinstance(item, dict) and item.get("id") and item.get("mediaType") == "event_livestream"
    )
    return ids


def official_wf_cut_ids() -> set[str]:
    ids = confirmed_event_cut_ids()
    manifest = read_json(OFFICIAL_VIDEO_MANIFEST, {})
    ids.update(
        str(item.get("id"))
        for item in manifest.get("videos", [])
        if isinstance(item, dict) and item.get("id") and item.get("mediaType") != "event_livestream"
    )
    return ids


def official_wf_premiere_ids() -> set[str]:
    manifest = read_json(OFFICIAL_VIDEO_MANIFEST, {})
    return {
        str(item.get("id"))
        for item in manifest.get("videos", [])
        if isinstance(item, dict)
        and item.get("id")
        and item.get("mediaType") == "scheduled_premiere"
    }


STOPWORDS = {
    "the", "and", "for", "with", "from", "your", "you", "into", "that", "this", "are", "how", "why", "what",
    "when", "where", "can", "our", "their", "agent", "agents", "ai", "engineering", "engineer",
}


def normalize(value: str) -> set[str]:
    return {word for word in re.findall(r"[a-z0-9]+", value.lower()) if len(word) > 2 and word not in STOPWORDS}


def title_speaker(title: str) -> str:
    return re.split(r"\s+[—-]\s+", title, maxsplit=1)[0].strip()


def title_alignment(video_title: str, session_title: str) -> tuple[int, float]:
    video_terms = normalize(title_speaker(video_title))
    session_terms = normalize(session_title)
    if not video_terms or not session_terms:
        return 0, 0.0
    overlap = len(video_terms & session_terms)
    return overlap, overlap / max(1, min(len(video_terms), len(session_terms)))


def confirmed_event_cut_ids() -> set[str]:
    sessions = read_json(RAW / "official-sessions.json", {}).get("sessions", [])
    ids: set[str] = set()
    for path in sorted(RESOURCES.glob("youtube-*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        video_id = video_id_from_page(path, text)
        if not (RAW / "youtube-transcripts" / f"{video_id}.txt").exists():
            continue
        title_match = re.search(r"^#\s+(.+)$", text, re.M)
        title = title_match.group(1).strip() if title_match else video_id
        for session in sessions:
            overlap, ratio = title_alignment(title, session.get("title", ""))
            if overlap >= 2 and ratio >= 0.75:
                speaker_blob = title.lower()
                if any(str(speaker).lower() in speaker_blob for speaker in session.get("speakers") or []):
                    ids.add(video_id)
                    break
    return ids


def external_video_ids() -> set[str]:
    ids = {path.stem for path in (RAW / "external-youtube-transcripts").glob("*.txt")}
    discovery = read_json(RAW / "external-video-discovery-latest.json", {})
    for result in discovery.get("results", []) if isinstance(discovery, dict) else []:
        video = result.get("video") or {}
        if video.get("id") and not result.get("official_channel"):
            ids.add(video["id"])
    return ids


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    return text[: end + 5], text[end + 5 :].lstrip()


def video_id_from_page(path: Path, text: str) -> str:
    match = re.search(r'^videoId:\s*"([^"]+)"', text, re.M)
    if match:
        return match.group(1)
    name = path.stem
    return name.removeprefix("youtube-")


def page_link_suffix(video_id: str) -> str:
    if (RAW / "youtube-livestream-transcripts" / f"{video_id}.txt").exists():
        return "livestream"
    if (RAW / "youtube-transcripts" / f"{video_id}.txt").exists():
        return "cut video"
    if (RAW / "external-youtube-transcripts" / f"{video_id}.txt").exists():
        return "external video"
    return "video"


def classification(video_id: str, official_streams: set[str], official_cuts: set[str], official_premieres: set[str], external: set[str]) -> tuple[str, list[str]]:
    if video_id in official_streams:
        return (
            "primary event livestream",
            [
                "- Source role: primary event video source for AI Engineer World's Fair San Francisco 2026.",
                "- Channel/source: official AI Engineer YouTube channel livestream.",
                "- Use: primary evidence for what the recording, transcript, and captured slides show; official schedule pages remain canonical for titles, times, tracks, rooms, speakers, and affiliations.",
            ],
        )
    if video_id in official_premieres:
        return (
            "primary event scheduled premiere",
            [
                "- Source role: verified official event video scheduled for premiere for AI Engineer World's Fair San Francisco 2026.",
                "- Channel/source: official AI Engineer YouTube channel scheduled premiere.",
                "- Use: event-video metadata until the recording becomes playable; transcript and slide evidence remain pending, and official schedule pages remain canonical for schedule metadata.",
            ],
        )
    if video_id in official_cuts:
        return (
            "primary event cut video",
            [
                "- Source role: primary event video source for AI Engineer World's Fair San Francisco 2026.",
                "- Channel/source: official AI Engineer YouTube channel cut video.",
                "- Use: primary evidence for what the published talk recording, transcript, and captured slides show; official schedule pages remain canonical for schedule metadata.",
            ],
        )
    if video_id in external:
        return (
            "supporting external video",
            [
                "- Source role: supporting external video source.",
                "- Channel/source: non-official YouTube upload or external event-related recording.",
                "- Use: supporting context only unless manually verified as an exact official event recording.",
            ],
        )
    return (
        "supporting contextual video",
        [
            "- Source role: supporting contextual video source.",
            "- Channel/source: public YouTube or AI Engineer channel video outside the confirmed World's Fair San Francisco 2026 event-video set.",
            "- Use: background, speaker, company, or historical AIE context; not primary evidence for World's Fair San Francisco 2026 session facts.",
        ],
    )


def upsert_section(text: str, heading: str, body_lines: list[str]) -> str:
    frontmatter, body = split_frontmatter(text)
    section = f"## {heading}\n" + "\n".join(body_lines).strip() + "\n\n"
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    if pattern.search(body):
            body = pattern.sub(section, body).rstrip() + "\n"
    else:
        anchor = re.compile(r"^(## What It Is\n.*?)(?=^## |\Z)", re.M | re.S)
        if anchor.search(body):
            body = anchor.sub(lambda m: m.group(1).rstrip() + "\n\n" + section, body, count=1).rstrip() + "\n"
        else:
            body = body.rstrip() + "\n\n" + section
    body = re.sub(r"([^\n])\n(## Source Classification)", r"\1\n\n\2", body)
    return frontmatter + body


def rewrite_what_it_is(text: str, role: str, video_kind: str) -> str:
    frontmatter, body = split_frontmatter(text)
    if role == "primary event scheduled premiere":
        replacement = (
            "## What It Is\n"
            "A verified official AI Engineer YouTube premiere for AI Engineer World's Fair San Francisco 2026. "
            "The recording, transcript, and slide evidence remain pending until the premiere is playable; the official schedule remains canonical for schedule facts.\n"
        )
    elif role.startswith("primary event"):
        replacement = (
            f"## What It Is\n"
            f"An official AI Engineer YouTube {video_kind} for AI Engineer World's Fair San Francisco 2026. "
            "This is an event video source for the wiki, while the official schedule remains the canonical schedule source.\n"
        )
    elif role == "supporting external video":
        replacement = (
            "## What It Is\n"
            "A non-official YouTube video connected to AI Engineer World's Fair 2026. It is useful supporting context, not a primary event-source page.\n"
        )
    else:
        replacement = (
            "## What It Is\n"
            "A public YouTube video used as supporting context for the AI Engineer World's Fair 2026 wiki. It is not part of the confirmed World's Fair San Francisco 2026 official event-video set.\n"
        )
    pattern = re.compile(r"^## What It Is\n.*?(?=^## |\Z)", re.M | re.S)
    if pattern.search(body):
        body = pattern.sub(replacement, body).rstrip() + "\n"
    return frontmatter + body


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest-only", action="store_true", help="Update only videos in the verified WF26 manifest.")
    parser.add_argument("--video-id", action="append", default=[], help="Update only the named video ID; repeat as needed.")
    args = parser.parse_args()
    official_streams = official_wf_livestream_ids()
    official_cuts = official_wf_cut_ids()
    official_premieres = official_wf_premiere_ids()
    external = external_video_ids()
    manifest_ids = official_streams | {
        str(item.get("id"))
        for item in read_json(OFFICIAL_VIDEO_MANIFEST, {}).get("videos", [])
        if isinstance(item, dict) and item.get("id")
    }
    counts: dict[str, int] = {}
    for path in sorted(RESOURCES.glob("youtube-*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        video_id = video_id_from_page(path, text)
        if args.manifest_only and video_id not in manifest_ids:
            continue
        if args.video_id and video_id not in set(args.video_id):
            continue
        role, body = classification(video_id, official_streams, official_cuts, official_premieres, external)
        counts[role] = counts.get(role, 0) + 1
        text = rewrite_what_it_is(text, role, page_link_suffix(video_id))
        text = upsert_section(text, "Source Classification", body)
        path.write_text(text.rstrip() + "\n", encoding="utf-8")
    print(json.dumps({"updated": sum(counts.values()), "counts": counts}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
