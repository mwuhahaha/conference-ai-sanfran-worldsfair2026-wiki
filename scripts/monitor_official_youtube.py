#!/usr/bin/env python3
"""Monitor the official AI Engineer YouTube channel for WF2026 videos.

This is intentionally project-local. It uses the public YouTube RSS feed for
date-gated discovery because that path exposes stable published dates without
requiring fragile full video extraction. For new official videos, it creates
wiki resource pages immediately, tries captions/transcript import, hands the
result to the checked-in wiki-maker update profile, and records pending failures
instead of treating YouTube 429/IP-blocking as fatal.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
import time
import traceback
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date, datetime, timezone, timedelta
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "sources"
WIKI = ROOT / "wiki"
STATE_DIR = ROOT / ".ops" / "state" / "youtube-monitor"
STATUS_JSON = STATE_DIR / "status.json"
STATUS_HTML = STATE_DIR / "status.html"
RSS_SNAPSHOT = RAW / "official-youtube-rss-latest.json"
OFFICIAL_VIDEO_MANIFEST = RAW / "official-wf26-video-manifest.json"
CHANNEL_ID = "UCLKPca3kwwd-B59HNr-_lvA"
CHANNEL_RSS = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
OFFICIAL_CHANNEL = "AI Engineer"
OFFICIAL_PLAYLIST_ID = "PLDyBmFH9HlVc"
OFFICIAL_PLAYLIST_URL = f"https://www.youtube.com/playlist?list={OFFICIAL_PLAYLIST_ID}"
OFFICIAL_PLAYLIST_BASELINE_IDS = (
    "iCj_ATyThvc",
    "ZSQb5fzRFPw",
    "q4Tr-DknG2M",
    "uU5Gv2h8-9g",
    "8G_1-3IO4ZQ",
    "0vphxNt4wyk",
    "APqXGyCoGW4",
    "n97BCfyFIvw",
    "c35YoMdnI78",
    "-CnA2lGfymY",
    "OqM67QG_Ikk",
    "V-EDrhIhHzQ",
    "KB41dTlX1Uc",
    "uIiA6DquRiE",
    "1P1hJ36rxM0",
    "YZQsWVeN3rE",
    "Cz4v1WHVyZc",
    "RGSFUqzqErE",
    "ZyIoTOAbRfs",
    "VrpEyglYgeU",
    "WkBPX-oDMnA",
    "ZpK5PWX2YRM",
    "pMggiOb18tc",
    "xUnRQ9vLXxo",
    "Z2Erdirpudo",
    "eBUyTS7SzV4",
    "9fubhllmsBU",
    "Z3fP-eMEx-8",
    "PXXNCtfKZs0",
)
OFFICIAL_PLAYLIST_SCHEDULE_OVERRIDES = {
    "xUnRQ9vLXxo": ("2026-07-01-theo-browne-closing-keynote-theo-browne",),
}
CAPTION_FAILURE_STATUSES = {
    "chrome_agent_unavailable",
    "chrome_caption_import_failed",
    "empty_caption_file",
}
SLIDE_FAILURE_STATUSES = {"slide_extraction_failed"}
WIKI_MAKER_ENV = "WIKI_FROM_TOPIC_MAKER"
PLAYABLE_MEDIA_TYPES = {"event_livestream", "talk_recording"}
NO_SLIDES_STATUS = "no_slides"
NO_SLIDES_PATTERNS = (
    re.compile(r"\b(?:i|we)\s+(?:have|had)\s+no\s+(?:slides?|slide\s+deck)\b", re.I),
    re.compile(r"\b(?:i|we)\s+(?:do\s+not|don't)\s+have\s+(?:any\s+)?slides?\b", re.I),
    re.compile(r"\bthere(?:'s|\s+is)\s+no\s+(?:slides?|slide\s+deck)\b", re.I),
)


@dataclass
class VideoEntry:
    video_id: str
    title: str
    published: str
    updated: str
    url: str
    description: str = ""
    live_status: str = ""
    release_date: str = ""
    has_english_captions: bool = False
    channel_id: str = ""
    availability: str = ""

    @property
    def published_date(self) -> date:
        return datetime.fromisoformat(self.published.replace("Z", "+00:00")).date()


@dataclass(frozen=True)
class PlaylistEntry:
    video_id: str
    playlist_index: int
    playlist_title: str
    availability: str
    video: VideoEntry | None
    matched_talks: tuple[dict[str, str], ...] = ()
    metadata_error: str = ""


def run(cmd: list[str], *, timeout: int = 600, check: bool = False) -> subprocess.CompletedProcess[str]:
    print("+", " ".join(cmd), flush=True)
    cp = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=timeout)
    if cp.stdout:
        print(cp.stdout[-4000:], flush=True)
    if cp.stderr:
        print(cp.stderr[-4000:], file=sys.stderr, flush=True)
    if check and cp.returncode != 0:
        raise RuntimeError(f"command failed ({cp.returncode}): {' '.join(cmd)}\n{cp.stderr[-2000:]}")
    return cp


def slugify(value: str) -> str:
    value = value.lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def yaml_value(value: object) -> str:
    if isinstance(value, list):
        return "[" + ", ".join(json.dumps(str(item), ensure_ascii=False) for item in value) + "]"
    return json.dumps(str(value), ensure_ascii=False)


def frontmatter(fields: dict[str, object]) -> str:
    lines = ["---"]
    for key, value in fields.items():
        lines.append(f"{key}: {yaml_value(value)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def upsert_section(text: str, heading: str, body: str) -> str:
    block = f"\n## {heading}\n{body.rstrip()}\n"
    pattern = re.compile(rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    if pattern.search(text):
        return pattern.sub(block, text).rstrip() + "\n"
    return text.rstrip() + block


def normalize_title(value: str) -> str:
    value = value.lower()
    value = re.sub(r"@[a-z0-9_.-]+", " ", value)
    value = re.sub(r"\b(ai|the|a|an|and|with|for|to|of|in|on|your|you)\b", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def fetch_rss(attempts: int = 3) -> list[VideoEntry]:
    if attempts < 1:
        raise ValueError("attempts must be at least 1")

    errors: list[str] = []
    for attempt in range(1, attempts + 1):
        try:
            request = Request(CHANNEL_RSS, headers={"User-Agent": "AIE-WF2026-Wiki-Monitor/1.0"})
            xml = urlopen(request, timeout=30).read()
            root = ET.fromstring(xml)
            break
        except Exception as exc:  # Network and feed errors are retried together.
            errors.append(f"attempt {attempt}: {type(exc).__name__}: {exc}")
            if attempt < attempts:
                time.sleep(2 ** attempt)
    else:
        raise RuntimeError("official YouTube RSS fetch failed after retries: " + "; ".join(errors))

    ns = {"atom": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}
    entries: list[VideoEntry] = []
    for entry in root.findall("atom:entry", ns):
        video_id = entry.findtext("yt:videoId", namespaces=ns)
        title = entry.findtext("atom:title", namespaces=ns)
        published = entry.findtext("atom:published", namespaces=ns)
        updated = entry.findtext("atom:updated", namespaces=ns) or published
        if not video_id or not title or not published:
            continue
        entries.append(
            VideoEntry(
                video_id=video_id,
                title=title,
                published=published,
                updated=updated or published,
                url=f"https://www.youtube.com/watch?v={video_id}",
            )
        )
    return entries


def load_json(path: Path, default: object) -> object:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def resource_path(video_id: str) -> Path:
    return WIKI / "resources" / f"youtube-{video_id}.md"


def transcript_path(video_id: str) -> Path:
    return RAW / "youtube-transcripts" / f"{video_id}.txt"


def slides_path(video_id: str) -> Path:
    return WIKI / "slides" / f"youtube-{video_id}-slides.md"


def resource_schedule_projection_needed(
    video_id: str, matched_talks: list[dict[str, str]]
) -> bool:
    path = resource_path(video_id)
    if not path.exists() or not matched_talks:
        return False
    text = path.read_text(encoding="utf-8", errors="ignore")
    return any(f"[[{talk['id']}" not in text for talk in matched_talks)


def frontmatter_speaker_names(text: str) -> list[str]:
    match = re.search(r"^speakers:[ \t]*(.*)$", text, re.M)
    if not match:
        return []
    inline = match.group(1).strip()
    if inline:
        return parse_speaker_names(inline)
    tail = text[match.end() :]
    names: list[str] = []
    for line in tail.splitlines():
        item = re.match(r"^[ \t]+-[ \t]+(.+?)\s*$", line)
        if item:
            names.append(item.group(1).strip().strip('"\''))
            continue
        if line.strip():
            break
    return names


def read_talk_pages() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted((WIKI / "talks").glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        title_match = re.search(r'^title:\s*"?(.+?)"?\s*$', text, re.M)
        description_match = re.search(r"^## Session Description\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        title = title_match.group(1).strip().strip('"') if title_match else path.stem.replace("-", " ").title()
        speakers = json.dumps(frontmatter_speaker_names(text), ensure_ascii=False)
        rows.append(
            {
                "id": path.stem,
                "path": str(path),
                "title": title,
                "speakers": speakers,
                "description": description_match.group(1).strip() if description_match else "",
                "text": text,
            }
        )
    return rows


def speaker_tokens(value: str) -> set[str]:
    value = re.sub(r"[\[\]\",]", " ", value)
    tokens = {token.lower() for token in re.findall(r"[A-Za-z][A-Za-z'-]{2,}", value)}
    return {token for token in tokens if token not in {"and", "the", "with", "for", "from"}}


def match_talks(video: VideoEntry, talks: list[dict[str, str]]) -> list[dict[str, str]]:
    video_norm = normalize_title(video.title)
    video_tokens = speaker_tokens(video.title)
    scored: list[tuple[int, dict[str, str]]] = []
    for talk in talks:
        talk_norm = normalize_title(talk["title"])
        title_overlap = set(talk_norm.split()) & set(video_norm.split())
        title_ratio = len(title_overlap) / max(1, min(len(set(talk_norm.split())), len(set(video_norm.split()))))
        score = 0
        if talk_norm and talk_norm in video_norm:
            score += 10
        elif video_norm and video_norm in talk_norm:
            score += 8
        else:
            if len(title_overlap) >= 4:
                score += len(title_overlap)
        speaker_overlap = speaker_tokens(talk["speakers"]) & video_tokens
        if speaker_overlap:
            score += min(6, len(speaker_overlap) * 2)
        if score >= 7 and len(title_overlap) >= 2 and title_ratio >= 0.75:
            scored.append((score, talk))
    scored.sort(key=lambda item: (-item[0], item[1]["title"]))
    return [talk for _score, talk in scored[:3]]


def explicit_wf26_event_title(video: VideoEntry) -> bool:
    title = video.title.lower()
    if re.search(r"\b(?:wf26|wf2026)\s*:", title):
        return True
    if ("world" in title and "fair" in title and "2026" in title) or ("worldsfair" in title and "2026" in title):
        return any(marker in title for marker in ("livestream", "keynote", "talk", "session", "workshop", "recording"))
    return False


def parse_speaker_names(value: str) -> list[str]:
    try:
        parsed = json.loads(value)
    except (json.JSONDecodeError, TypeError):
        parsed = []
    if isinstance(parsed, list):
        return [str(item).strip() for item in parsed if str(item).strip()]
    return []


def normalize_evidence_text(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", value.lower())).strip()


def phrase_present(phrase: str, blob: str) -> bool:
    return bool(phrase) and f" {phrase} " in f" {blob} "


def verified_schedule_matches(video: VideoEntry, talks: list[dict[str, str]]) -> list[dict[str, str]]:
    """Match rewritten official-channel titles using schedule text, not popularity signals."""
    strict = strict_schedule_matches(video, talks)
    matched = {talk["id"]: talk for talk in strict}
    override_ids = set(OFFICIAL_PLAYLIST_SCHEDULE_OVERRIDES.get(video.video_id, ()))
    for talk in talks:
        if talk["id"] in override_ids:
            matched[talk["id"]] = talk
    evidence_blob = normalize_evidence_text(f"{video.title}\n{video.description}")
    description_blob = normalize_evidence_text(video.description)
    for talk in talks:
        if talk["id"] in matched:
            continue
        speaker_names = parse_speaker_names(talk.get("speakers", ""))
        if not any(phrase_present(normalize_evidence_text(name), evidence_blob) for name in speaker_names):
            continue
        title_phrase = normalize_evidence_text(talk["title"])
        schedule_description = normalize_evidence_text(talk.get("description", ""))
        title_signal = len(title_phrase) >= 12 and phrase_present(title_phrase, evidence_blob)
        description_signal = len(schedule_description) >= 120 and schedule_description[:120] in description_blob
        if title_signal or description_signal:
            matched[talk["id"]] = talk
    return sorted(matched.values(), key=lambda item: item["title"])


def yt_dlp_binary() -> str:
    command = shutil.which("yt-dlp")
    if command:
        return command
    local = Path.home() / ".local" / "bin" / "yt-dlp"
    return str(local) if local.exists() else "yt-dlp"


def video_entry_from_metadata(payload: dict[str, object]) -> VideoEntry:
    upload_date = str(payload.get("upload_date") or payload.get("release_date") or "")
    if not re.fullmatch(r"\d{8}", upload_date):
        raise ValueError(f"video metadata has no usable upload/release date: {payload.get('id')}")
    published_date = datetime.strptime(upload_date, "%Y%m%d").date().isoformat()
    release_raw = str(payload.get("release_date") or "")
    release_date = datetime.strptime(release_raw, "%Y%m%d").date().isoformat() if re.fullmatch(r"\d{8}", release_raw) else ""
    languages = set((payload.get("subtitles") or {}).keys()) | set((payload.get("automatic_captions") or {}).keys())
    video_id = str(payload.get("id") or "")
    return VideoEntry(
        video_id=video_id,
        title=str(payload.get("title") or video_id),
        published=f"{published_date}T00:00:00+00:00",
        updated=f"{published_date}T00:00:00+00:00",
        url=str(payload.get("webpage_url") or f"https://www.youtube.com/watch?v={video_id}"),
        description=str(payload.get("description") or ""),
        live_status=str(payload.get("live_status") or ""),
        release_date=release_date,
        has_english_captions=any(lang == "en" or lang.startswith("en-") for lang in languages),
        channel_id=str(payload.get("channel_id") or ""),
        availability=str(payload.get("availability") or ""),
    )


def fetch_video_metadata(video_id: str) -> VideoEntry:
    cp = subprocess.run(
        [
            yt_dlp_binary(),
            "--no-playlist",
            "--no-cache-dir",
            "--skip-download",
            "--ignore-no-formats-error",
            "--no-warnings",
            "--dump-single-json",
            f"https://www.youtube.com/watch?v={video_id}",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=180,
    )
    if cp.returncode != 0:
        raise RuntimeError(f"yt-dlp metadata failed for {video_id}: {(cp.stderr or cp.stdout)[-1200:]}")
    payload = json.loads(cp.stdout)
    if not isinstance(payload, dict):
        raise RuntimeError(f"yt-dlp returned no metadata for {video_id}")
    try:
        return video_entry_from_metadata(payload)
    except ValueError as exc:
        probe = subprocess.run(
            [
                yt_dlp_binary(),
                "--no-playlist",
                "--no-cache-dir",
                "--skip-download",
                f"https://www.youtube.com/watch?v={video_id}",
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=180,
        )
        unavailable_error = (probe.stderr or probe.stdout)[-1600:]
        if "private video" in unavailable_error.lower():
            raise RuntimeError(f"yt-dlp metadata reports Private video: {video_id}") from exc
        if "unavailable" in unavailable_error.lower() or "deleted" in unavailable_error.lower():
            raise RuntimeError(
                f"yt-dlp metadata reports unavailable video: {video_id}"
            ) from exc
        raise


def metadata_unavailable_reason(error: Exception) -> str:
    message = str(error).lower()
    if "private video" in message:
        return "private"
    if (
        "video unavailable" in message
        or "unavailable video" in message
        or "deleted video" in message
    ):
        return "unavailable"
    return ""


def fetch_official_playlist(
    talks: list[dict[str, str]],
) -> tuple[list[PlaylistEntry], dict[str, object]]:
    """Enumerate the official WF26 playlist without losing private entries."""
    cp = subprocess.run(
        [
            yt_dlp_binary(),
            "--flat-playlist",
            "--ignore-errors",
            "--no-cache-dir",
            "--no-warnings",
            "--dump-single-json",
            OFFICIAL_PLAYLIST_URL,
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=300,
    )
    if cp.returncode != 0:
        raise RuntimeError(
            "official WF26 playlist enumeration failed: "
            + (cp.stderr or cp.stdout)[-1600:]
        )
    try:
        payload = json.loads(cp.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("official WF26 playlist returned invalid JSON") from exc
    if not isinstance(payload, dict) or payload.get("id") != OFFICIAL_PLAYLIST_ID:
        raise RuntimeError("official WF26 playlist identity mismatch")
    if payload.get("channel_id") != CHANNEL_ID:
        raise RuntimeError("official WF26 playlist owner channel mismatch")
    raw_entries = payload.get("entries")
    if not isinstance(raw_entries, list):
        raise RuntimeError("official WF26 playlist has no entries array")

    ids: list[str] = []
    for item in raw_entries:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            raise RuntimeError("official WF26 playlist contains an invalid entry")
        video_id = str(item["id"])
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
            raise RuntimeError(f"official WF26 playlist contains invalid video ID: {video_id}")
        ids.append(video_id)
    if len(ids) != len(set(ids)):
        raise RuntimeError("official WF26 playlist contains duplicate video IDs")
    baseline_ids = set(OFFICIAL_PLAYLIST_BASELINE_IDS)
    missing_baseline = sorted(baseline_ids - set(ids))
    if missing_baseline:
        raise RuntimeError(
            "official WF26 playlist is missing baseline items: "
            + ", ".join(missing_baseline)
        )
    new_since_baseline = sorted(set(ids) - baseline_ids)

    entries: list[PlaylistEntry] = []
    unavailable = 0
    for index, item in enumerate(raw_entries, start=1):
        video_id = str(item["id"])
        playlist_title = str(item.get("title") or "").strip()
        try:
            video = fetch_video_metadata(video_id)
        except Exception as exc:
            reason = metadata_unavailable_reason(exc)
            if not reason:
                raise RuntimeError(
                    f"official WF26 playlist metadata failed for {video_id}: {exc}"
                ) from exc
            unavailable += 1
            entries.append(
                PlaylistEntry(
                    video_id=video_id,
                    playlist_index=index,
                    playlist_title=playlist_title,
                    availability=reason,
                    video=None,
                    metadata_error=str(exc)[-1600:],
                )
            )
            continue
        if video.channel_id and video.channel_id != CHANNEL_ID:
            raise RuntimeError(
                f"official WF26 playlist video owner mismatch for {video_id}"
            )
        entries.append(
            PlaylistEntry(
                video_id=video_id,
                playlist_index=index,
                playlist_title=playlist_title,
                availability=video.availability or "available",
                video=video,
                matched_talks=tuple(verified_schedule_matches(video, talks)),
            )
        )

    return entries, {
        "status": "ok",
        "playlist_id": OFFICIAL_PLAYLIST_ID,
        "playlist_title": str(payload.get("title") or ""),
        "playlist_count": len(entries),
        "baseline_count": len(OFFICIAL_PLAYLIST_BASELINE_IDS),
        "new_since_baseline_count": len(new_since_baseline),
        "new_since_baseline_ids": new_since_baseline,
        "visible_count": len(entries) - unavailable,
        "unavailable_count": unavailable,
    }


def manifest_video_ids() -> set[str]:
    payload = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    if not isinstance(payload, dict):
        return set()
    return {str(item.get("id")) for item in payload.get("videos", []) if isinstance(item, dict) and item.get("id")}


def scheduled_manifest_video_ids() -> set[str]:
    payload = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    if not isinstance(payload, dict):
        return set()
    return {
        str(item.get("id"))
        for item in payload.get("videos", [])
        if isinstance(item, dict)
        and item.get("id")
        and item.get("mediaType") == "scheduled_premiere"
    }


def pending_manifest_video_ids() -> set[str]:
    payload = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    if not isinstance(payload, dict):
        return set()
    return {
        str(item.get("id"))
        for item in payload.get("videos", [])
        if isinstance(item, dict)
        and item.get("id")
        and (item.get("mediaType") == "scheduled_premiere" or item.get("transcriptStatus") == "pending")
    }


def no_slides_manifest_video_ids() -> set[str]:
    payload = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    if not isinstance(payload, dict):
        return set()
    return {
        str(item.get("id"))
        for item in payload.get("videos", [])
        if isinstance(item, dict)
        and item.get("id")
        and item.get("slideStatus") == NO_SLIDES_STATUS
    }


def discover_recent_channel_event_rows(
    talks: list[dict[str, str]], *, limit: int = 100
) -> tuple[list[tuple[VideoEntry, list[dict[str, str]]]], dict[str, object]]:
    """Inspect recent official-channel titles, fetching details only for roster candidates."""
    cp = subprocess.run(
        [
            yt_dlp_binary(),
            "--flat-playlist",
            "--playlist-end",
            str(limit),
            "--dump-single-json",
            "https://www.youtube.com/@aiDotEngineer/videos",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=300,
    )
    if cp.returncode != 0:
        return [], {"status": "channel_scan_failed", "error": (cp.stderr or cp.stdout)[-1200:]}
    payload = json.loads(cp.stdout)
    if not isinstance(payload, dict) or payload.get("channel_id") != CHANNEL_ID:
        return [], {"status": "channel_identity_mismatch"}

    known_ids = manifest_video_ids()
    pending_ids = pending_manifest_video_ids()
    speaker_phrases = {
        normalize_evidence_text(name)
        for talk in talks
        for name in parse_speaker_names(talk.get("speakers", ""))
        if name
    }
    rows: list[tuple[VideoEntry, list[dict[str, str]]]] = []
    metadata_errors: list[dict[str, str]] = []
    candidates = 0
    for item in payload.get("entries", []):
        if not isinstance(item, dict) or not item.get("id"):
            continue
        if item.get("id") in known_ids and item.get("id") not in pending_ids:
            continue
        lightweight = VideoEntry(
            video_id=str(item["id"]),
            title=str(item.get("title") or item["id"]),
            published="1970-01-01T00:00:00+00:00",
            updated="1970-01-01T00:00:00+00:00",
            url=str(item.get("url") or f"https://www.youtube.com/watch?v={item['id']}"),
        )
        title_blob = normalize_evidence_text(lightweight.title)
        roster_candidate = any(phrase_present(phrase, title_blob) for phrase in speaker_phrases)
        if not roster_candidate and not strict_schedule_matches(lightweight, talks):
            continue
        candidates += 1
        try:
            video = fetch_video_metadata(lightweight.video_id)
        except Exception as exc:
            metadata_errors.append({"id": lightweight.video_id, "error": str(exc)})
            continue
        matched = verified_schedule_matches(video, talks)
        if matched:
            rows.append((video, matched))
    return rows, {
        "status": "ok",
        "scanned": min(limit, len(payload.get("entries", []))),
        "metadata_candidates": candidates,
        "verified_event_videos": len(rows),
        "metadata_errors": metadata_errors,
    }


def update_official_video_manifest(
    rows: list[tuple[VideoEntry, list[dict[str, str]]]],
    *,
    playlist_entries: list[PlaylistEntry] | None = None,
    write: bool = True,
) -> bool:
    payload = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    if not isinstance(payload, dict):
        payload = {}
    videos = {
        str(item.get("id")): item
        for item in payload.get("videos", [])
        if isinstance(item, dict) and item.get("id")
    }
    changed = False
    for video, matched in rows:
        existing = dict(videos.get(video.video_id) or {})
        entry = {
            **existing,
            "id": video.video_id,
            "title": video.title,
            "mediaType": "scheduled_premiere" if video.live_status == "is_upcoming" else "talk_recording",
            "associationEvidence": (
                "official_wf26_playlist_membership"
                if existing.get("playlistId") == OFFICIAL_PLAYLIST_ID
                else "official_channel_plus_schedule_text"
            ),
            "matchedTalks": (
                [talk["id"] for talk in matched]
                if matched
                else list(existing.get("matchedTalks") or [])
            ),
            "uploadDate": video.published_date.isoformat(),
            "releaseDate": video.release_date,
            "transcriptStatus": (
                "cached"
                if transcript_path(video.video_id).exists()
                else "available_on_youtube"
                if video.has_english_captions
                else "pending"
            ),
        }
        if videos.get(video.video_id) != entry:
            videos[video.video_id] = entry
            changed = True

    for item in playlist_entries or []:
        existing = dict(videos.get(item.video_id) or {})
        matched_talks = (
            [talk["id"] for talk in item.matched_talks]
            if item.matched_talks
            else list(existing.get("matchedTalks") or [])
        )
        if item.video is None:
            entry = {
                **existing,
                "id": item.video_id,
                "mediaType": "unavailable_playlist_item",
                "associationEvidence": "official_wf26_playlist_membership",
                "matchedTalks": matched_talks,
                "playlistId": OFFICIAL_PLAYLIST_ID,
                "playlistIndex": item.playlist_index,
                "playlistAvailability": "unavailable",
                "videoAvailability": "unknown",
                "unavailableReason": item.availability,
                "transcriptStatus": (
                    "cached" if transcript_path(item.video_id).exists() else "unavailable"
                ),
                "slideStatus": (
                    "cached" if slides_path(item.video_id).exists() else "unavailable"
                ),
            }
            if item.playlist_title:
                entry["playlistTitle"] = item.playlist_title
                entry.setdefault("title", item.playlist_title)
        else:
            video = item.video
            media_type = (
                "scheduled_premiere"
                if video.live_status == "is_upcoming"
                else "talk_recording"
            )
            entry = {
                **existing,
                "id": item.video_id,
                "title": video.title,
                "playlistTitle": item.playlist_title or video.title,
                "mediaType": media_type,
                "associationEvidence": "official_wf26_playlist_membership",
                "matchedTalks": matched_talks,
                "playlistId": OFFICIAL_PLAYLIST_ID,
                "playlistIndex": item.playlist_index,
                "playlistAvailability": "available",
                "videoAvailability": item.availability,
                "uploadDate": video.published_date.isoformat(),
                "releaseDate": video.release_date,
                "transcriptStatus": (
                    "cached"
                    if transcript_path(item.video_id).exists()
                    else "available_on_youtube"
                    if video.has_english_captions
                    else "pending"
                ),
                "slideStatus": (
                    "cached"
                    if slides_path(item.video_id).exists()
                    else NO_SLIDES_STATUS
                    if existing.get("slideStatus") == NO_SLIDES_STATUS
                    else "pending"
                ),
            }
            entry.pop("unavailableReason", None)
        if videos.get(item.video_id) != entry:
            videos[item.video_id] = entry
            changed = True
    if not changed:
        return False
    payload.update(
        {
            "schemaVersion": 1,
            "sourceBoundary": (
                "Official WF26 playlist membership establishes event association; "
                "the official schedule remains canonical for session titles, speakers, "
                "dates, rooms, tracks, and affiliations."
            ),
            "videos": sorted(
                videos.values(),
                key=lambda entry: (
                    0 if entry.get("playlistId") == OFFICIAL_PLAYLIST_ID else 1,
                    int(entry.get("playlistIndex") or 100000),
                    str(entry.get("uploadDate", "")),
                    str(entry.get("id", "")),
                ),
            ),
        }
    )
    if write:
        write_json(OFFICIAL_VIDEO_MANIFEST, payload)
    return True


def refresh_manifest_artifact_statuses(
    processed: list[dict[str, object]], *, write: bool = True
) -> bool:
    """Reconcile processed manifest rows with artifacts produced in this run."""
    payload = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    if not isinstance(payload, dict):
        return False
    videos = payload.get("videos")
    if not isinstance(videos, list):
        return False
    by_id = {
        str(item.get("id")): item
        for item in videos
        if isinstance(item, dict) and item.get("id")
    }
    changed = False
    for processed_item in processed:
        video_id = str(processed_item.get("id") or "")
        manifest_item = by_id.get(video_id)
        if not manifest_item:
            continue
        transcript_result = processed_item.get("transcript")
        transcript_status = (
            str(transcript_result.get("status") or "")
            if isinstance(transcript_result, dict)
            else ""
        )
        if transcript_path(video_id).exists():
            desired_transcript_status = "cached"
        elif transcript_status == "unavailable":
            desired_transcript_status = "unavailable"
        elif transcript_status == "pending_premiere":
            desired_transcript_status = "pending"
        else:
            desired_transcript_status = ""
        if (
            desired_transcript_status
            and manifest_item.get("transcriptStatus") != desired_transcript_status
        ):
            manifest_item["transcriptStatus"] = desired_transcript_status
            changed = True

        slide_result = processed_item.get("slides")
        slide_status = (
            str(slide_result.get("status") or "")
            if isinstance(slide_result, dict)
            else ""
        )
        if slide_status == NO_SLIDES_STATUS:
            desired_slide_status = NO_SLIDES_STATUS
        elif slides_path(video_id).exists():
            desired_slide_status = "cached"
        elif slide_status == "unavailable":
            desired_slide_status = "unavailable"
        elif slide_status == "pending_premiere":
            desired_slide_status = "pending"
        else:
            desired_slide_status = ""
        if desired_slide_status and manifest_item.get("slideStatus") != desired_slide_status:
            manifest_item["slideStatus"] = desired_slide_status
            changed = True

    if changed and write:
        write_json(OFFICIAL_VIDEO_MANIFEST, payload)
    return changed


def excluded_non_wf26_event_title(video: VideoEntry) -> bool:
    """Reject official-channel uploads that clearly point at another event/scope."""
    title = video.title.lower()
    other_event_markers = [
        "miami",
        "world's fair 2025",
        "worlds fair 2025",
        "worldsfair 2025",
        "wf25",
        "wf2025",
        "world's fair 2024",
        "worlds fair 2024",
        "worldsfair 2024",
        "wf24",
        "wf2024",
        "summit",
    ]
    return any(marker in title for marker in other_event_markers)


def title_tokens(value: str) -> set[str]:
    value = normalize_title(value)
    return {token for token in value.split() if len(token) >= 3}


def strict_schedule_matches(video: VideoEntry, talks: list[dict[str, str]]) -> list[dict[str, str]]:
    """Return only high-confidence matches to actual WF2026 scheduled talks.

    This is intentionally stricter than match_talks(). The monitor is allowed to
    import only official-channel WF26 event videos. A loose speaker/title overlap
    is useful for review, but not enough to create first-class event evidence.
    """
    if excluded_non_wf26_event_title(video):
        return []
    video_norm = normalize_title(video.title)
    video_title_tokens = title_tokens(video.title)
    video_speaker_tokens = speaker_tokens(video.title)
    matched: list[tuple[float, dict[str, str]]] = []
    for talk in talks:
        talk_norm = normalize_title(talk["title"])
        talk_title_tokens = title_tokens(talk["title"])
        if not talk_norm or not talk_title_tokens:
            continue
        speaker_overlap = speaker_tokens(talk["speakers"]) & video_speaker_tokens
        exact_title = talk_norm in video_norm
        overlap = talk_title_tokens & video_title_tokens
        coverage = len(overlap) / max(1, len(talk_title_tokens))
        if exact_title and speaker_overlap:
            matched.append((1.0, talk))
        elif coverage >= 0.9 and len(overlap) >= 4 and speaker_overlap:
            matched.append((coverage, talk))
    matched.sort(key=lambda item: (-item[0], item[1]["title"]))
    return [talk for _score, talk in matched[:3]]


def event_entries(entries: list[VideoEntry], talks: list[dict[str, str]]) -> list[tuple[VideoEntry, list[dict[str, str]]]]:
    rows = []
    for entry in entries:
        if excluded_non_wf26_event_title(entry):
            continue
        matched = strict_schedule_matches(entry, talks)
        if explicit_wf26_event_title(entry) or matched:
            rows.append((entry, matched))
    return rows


def write_resource_page(
    video: VideoEntry,
    matched_talks: list[dict[str, str]],
    transcript_status: str,
    slide_status: str,
    *,
    association_evidence: str = "official_channel_plus_schedule_text",
) -> bool:
    path = resource_path(video.video_id)
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    old_enriched = re.search(r'^last_enriched:\s*"?([^"\n]+)', old, re.M)
    enriched_at = old_enriched.group(1) if old_enriched else datetime.now(timezone.utc).isoformat()
    playlist_admitted = association_evidence == "official_wf26_playlist_membership"
    talk_lines = []
    if matched_talks:
        for talk in matched_talks:
            talk_lines.append(f"- [[{talk['id']}|{talk['title']}]]")
    else:
        reason = (
            "official WF26 playlist membership"
            if playlist_admitted
            else "the official-channel title explicitly identifies it as WF26 / World's Fair 2026 event media"
        )
        talk_lines.append(
            "- No exact schedule-page match has been assigned; event association comes from "
            f"{reason}. Do not infer schedule fields from the video title."
        )
    transcript_line = (
        f"Cached transcript text is available at `raw/sources/youtube-transcripts/{video.video_id}.txt`."
        if transcript_path(video.video_id).exists()
        else f"Transcript import status: {transcript_status}."
    )
    if slide_status == NO_SLIDES_STATUS:
        slide_line = "- No slide deck was used; the cached transcript explicitly reports no slides."
    elif slides_path(video.video_id).exists():
        slide_line = f"- [[youtube-{video.video_id}-slides]]"
    else:
        slide_line = f"- Slide extraction status: {slide_status}."
    upcoming = video.live_status == "is_upcoming"
    if upcoming:
        media_description = (
            "A scheduled official AI Engineer YouTube premiere admitted through the official "
            "WF26 playlist. The page records association metadata only until the premiere is "
            "playable; transcript and slide evidence remain pending."
            if playlist_admitted
            else "A scheduled official AI Engineer YouTube premiere independently matched to an AI Engineer World's Fair San Francisco 2026 session. The page records the pending media source now; transcript and slide evidence remain unavailable until the premiere is playable."
        )
    else:
        media_description = (
            "An official AI Engineer YouTube recording admitted through the official WF26 "
            "playlist. Playlist membership establishes event association; official schedule "
            "pages remain canonical for schedule metadata."
            if playlist_admitted
            else "An official AI Engineer YouTube recording independently matched to an AI Engineer World's Fair San Francisco 2026 session. Official schedule pages remain canonical for schedule metadata."
        )
    release_line = f"- Scheduled premiere date: {video.release_date}." if upcoming and video.release_date else ""
    if upcoming:
        source_role_line = "- Source role: official event-video association metadata for a scheduled premiere."
        use_line = (
            "- Use: association and premiere-state metadata only until the recording is playable; "
            "do not use this page as recording, transcript, or slide-content evidence."
        )
    else:
        source_role_line = "- Source role: primary event video source for AI Engineer World's Fair San Francisco 2026."
        use_line = (
            "- Use: use as media and transcript evidence for the event recording; no slide deck "
            "is claimed, and schedule facts remain tied to the official schedule pages."
            if slide_status == NO_SLIDES_STATUS
            else "- Use: use as media/transcript/slide evidence for the event recording; keep schedule "
            "facts tied to the official schedule pages."
        )
    text = "\n".join(
        [
            frontmatter(
                {
                    "title": video.title,
                    "category": "resources",
                    "sourceLabels": (
                        ["Official AI Engineer YouTube channel", "Official WF26 playlist membership"]
                        if playlist_admitted
                        else ["Official AI Engineer YouTube channel", "Official-channel video metadata"]
                    ),
                    "videoId": video.video_id,
                    "publishedDate": video.published_date.isoformat(),
                    "last_enriched": enriched_at,
                }
            ).rstrip(),
            f"# {video.title}",
            "",
            "## What It Is",
            media_description,
            "",
            "## Source Classification",
            source_role_line,
            (
                f"- Admission: official playlist `{OFFICIAL_PLAYLIST_ID}` membership."
                if playlist_admitted
                else "- Admission: official-channel metadata independently matched to schedule evidence."
            ),
            f"- Published date: {video.published_date.isoformat()}",
            release_line,
            f"- Channel/source: {OFFICIAL_CHANNEL}.",
            use_line,
            "",
            "## Matched Schedule Pages",
            *talk_lines,
            "",
            "## Transcript Status",
            transcript_line,
            "",
            "## Extracted Slides",
            slide_line,
            "",
            "## Link",
            f"[YouTube]({video.url})",
        ]
    )
    if old == text + "\n":
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text + "\n", encoding="utf-8")
    return True


def write_unavailable_resource_page(item: PlaylistEntry) -> bool:
    path = resource_path(item.video_id)
    title = f"Official WF26 Playlist Item {item.video_id} (Unavailable)"
    text = "\n".join(
        [
            frontmatter(
                {
                    "title": title,
                    "category": "resources",
                    "sourceLabels": ["Official WF26 playlist membership"],
                    "videoId": item.video_id,
                    "playlistId": OFFICIAL_PLAYLIST_ID,
                    "availability": item.availability,
                }
            ).rstrip(),
            f"# {title}",
            "",
            "## What It Is",
            "An unavailable item retained from the official AI Engineer WF26 playlist. Playlist membership establishes event association only; no title, speaker, transcript, slide, or schedule claim is made.",
            "",
            "## Source Classification",
            "- Source role: official WF26 playlist association metadata only.",
            f"- Playlist position: {item.playlist_index}.",
            f"- Availability: {item.availability}.",
            "- Use: do not use this placeholder as content, transcript, slide, or schedule evidence.",
            "",
            "## Transcript Status",
            "Unavailable; no transcript content was acquired.",
            "",
            "## Extracted Slides",
            "Unavailable; no slide content was acquired.",
            "",
            "## Link",
            f"[YouTube](https://www.youtube.com/watch?v={item.video_id})",
        ]
    ) + "\n"
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if old == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def update_talk_pages(video: VideoEntry, matched_talks: list[dict[str, str]]) -> int:
    updated = 0
    transcript_bits = []
    if transcript_path(video.video_id).exists():
        transcript_bits.append(f"[[youtube-{video.video_id}-transcript]]")
    if slides_path(video.video_id).exists():
        transcript_bits.append(f"[[youtube-{video.video_id}-slides]]")
    evidence = "; ".join(transcript_bits) if transcript_bits else "transcript/slide enrichment pending"
    media_line = (
        f"- [[youtube-{video.video_id}]] — scheduled official AI Engineer YouTube premiere for {video.release_date or 'a pending date'}."
        if video.live_status == "is_upcoming"
        else f"- [[youtube-{video.video_id}]] — official AI Engineer YouTube channel recording published {video.published_date.isoformat()}."
    )
    boundary_line = (
        "- Boundary: use this link as event-association and premiere-state metadata only until "
        "the recording is playable; do not use it as recording, transcript, or slide-content evidence."
        if video.live_status == "is_upcoming"
        else "- Boundary: use this recording as media evidence; keep date/time/room facts tied to the official schedule."
    )
    body = "\n".join(
        [
            media_line,
            f"- Evidence status: {evidence}.",
            boundary_line,
        ]
    )
    for talk in matched_talks:
        path = Path(talk["path"])
        text = path.read_text(encoding="utf-8")
        new_text = upsert_section(text, "Official YouTube Recording", body)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
    return updated


def yt_dlp_js_runtime_arg() -> str:
    node = shutil.which("node")
    if not node:
        for candidate in sorted(Path("/home/dylan/.nvm/versions/node").glob("*/bin/node"), reverse=True):
            if candidate.exists():
                node = str(candidate)
                break
    return f"node:{node}" if node else "node"


def vtt_to_text(path: Path) -> str:
    lines: list[str] = []
    seen: set[str] = set()
    for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.strip()
        if not line or line == "WEBVTT" or "-->" in line or line.isdigit() or line.startswith(("Kind:", "Language:")):
            continue
        line = re.sub(r"<[^>]+>", "", line)
        line = re.sub(r"\s+", " ", line).strip()
        if line and line not in seen:
            seen.add(line)
            lines.append(line)
    return " ".join(lines)


def try_import_captions(
    video: VideoEntry, *, allow_browser_fallback: bool = True
) -> dict[str, object]:
    if transcript_path(video.video_id).exists():
        return {"status": "already_cached", "path": str(transcript_path(video.video_id).relative_to(ROOT))}
    if video.live_status == "is_upcoming":
        return {"status": "pending_premiere", "release_date": video.release_date}
    subtitle_dir = RAW / "youtube-subtitles"
    subtitle_dir.mkdir(parents=True, exist_ok=True)
    before = set(subtitle_dir.glob(f"{video.video_id}*.vtt"))
    cp = run(
        [
            "yt-dlp",
            "--js-runtimes",
            yt_dlp_js_runtime_arg(),
            "--remote-components",
            "ejs:github",
            "--skip-download",
            "--write-subs",
            "--write-auto-subs",
            "--sub-langs",
            "en.*",
            "--sub-format",
            "vtt",
            "-o",
            str(subtitle_dir / f"{video.video_id}.%(ext)s"),
            video.url,
        ],
        timeout=360,
    )
    if cp.returncode != 0:
        if not allow_browser_fallback:
            return {
                "status": "caption_acquisition_pending",
                "yt_dlp_error": (cp.stderr or cp.stdout)[-1600:],
            }
        chrome = try_import_captions_with_chrome_agent(video)
        if chrome.get("status") == "captions_imported":
            return chrome
        chrome["yt_dlp_error"] = (cp.stderr or cp.stdout)[-1600:]
        return chrome
    after = set(subtitle_dir.glob(f"{video.video_id}*.vtt"))
    candidates = sorted(after - before) or sorted(after)
    if not candidates:
        if not allow_browser_fallback:
            return {
                "status": "caption_acquisition_pending",
                "attempt_status": "no_captions_found",
            }
        return {"status": "no_captions_found"}
    text = vtt_to_text(candidates[0]).strip()
    if not text:
        return {"status": "empty_caption_file", "caption_path": str(candidates[0].relative_to(ROOT))}
    target = transcript_path(video.video_id)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text + "\n", encoding="utf-8")
    return {
        "status": "captions_imported",
        "path": str(target.relative_to(ROOT)),
        "caption_path": str(candidates[0].relative_to(ROOT)),
        "word_count": len(text.split()),
    }


def try_import_captions_with_chrome_agent(video: VideoEntry) -> dict[str, object]:
    chrome_project = Path("/garage/projects/agents/chrome-agent-python")
    helper = ROOT / "scripts" / "extract_youtube_caption_with_chrome_agent.py"
    if not chrome_project.exists() or not helper.exists():
        return {"status": "chrome_agent_unavailable"}
    target = transcript_path(video.video_id)
    cp = subprocess.run(
        [
            "uv",
            "run",
            "python",
            str(helper),
            "--video-id",
            video.video_id,
            "--output",
            str(target),
        ],
        cwd=chrome_project,
        text=True,
        capture_output=True,
        timeout=120,
    )
    if cp.stdout:
        print(cp.stdout[-4000:], flush=True)
    if cp.stderr:
        print(cp.stderr[-4000:], file=sys.stderr, flush=True)
    if cp.returncode != 0 or not target.exists():
        return {"status": "chrome_caption_import_failed", "error": (cp.stderr or cp.stdout)[-1600:]}
    text = target.read_text(encoding="utf-8", errors="ignore")
    return {"status": "captions_imported", "path": str(target.relative_to(ROOT)), "source": "chrome_agent", "word_count": len(text.split())}


def explicit_no_slides_evidence(video_id: str) -> str:
    path = transcript_path(video_id)
    if not path.exists():
        return ""
    opening = path.read_text(encoding="utf-8", errors="ignore")[:12000]
    opening = opening.replace("\u2019", "'")
    for pattern in NO_SLIDES_PATTERNS:
        match = pattern.search(opening)
        if match:
            return re.sub(r"\s+", " ", match.group(0)).strip()
    return ""


def no_slides_reconciliation_needed(video_id: str, known_no_slides: set[str]) -> bool:
    if not explicit_no_slides_evidence(video_id):
        return False
    return (
        slides_path(video_id).exists()
        or standard_slide_references_exist(video_id)
        or video_id not in known_no_slides
    )


def standard_slide_reference_markers(video_id: str) -> tuple[str, ...]:
    return (
        f"youtube-{video_id}-slides",
        f"assets/slides/{video_id}/",
        f"Slide-derived themes for `youtube-{video_id}`",
    )


def strip_standard_slide_references(markdown: str, video_id: str) -> str:
    """Remove references to a retired standard slide extraction only."""

    markers = standard_slide_reference_markers(video_id)
    source_marker = f"- Source video: `youtube-{video_id}`"
    parts = re.split(r"(\n{2,})", markdown)
    kept: list[str] = []
    for index, part in enumerate(parts):
        if index % 2:
            kept.append(part)
            continue
        if source_marker in part and any(marker in part for marker in markers):
            kept.append("")
            continue
        lines = [line for line in part.splitlines() if not any(marker in line for marker in markers)]
        kept.append("\n".join(lines))
    cleaned = "".join(kept)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.rstrip() + "\n"


def standard_slide_references_exist(video_id: str) -> bool:
    markers = standard_slide_reference_markers(video_id)
    for path in WIKI.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        if any(marker in text for marker in markers):
            return True
    return False


def retire_standard_slide_references(video_id: str) -> list[str]:
    changed: list[str] = []
    for path in WIKI.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        updated = strip_standard_slide_references(text, video_id)
        if updated == text:
            continue
        path.write_text(updated, encoding="utf-8")
        changed.append(str(path.relative_to(ROOT)))
    return changed


def retire_standard_slide_artifacts(video_id: str) -> list[str]:
    if not re.fullmatch(r"[A-Za-z0-9_-]{6,32}", video_id):
        raise ValueError(f"unsafe YouTube video id for slide cleanup: {video_id!r}")
    paths = [
        slides_path(video_id),
        WIKI / "assets" / "slides" / video_id,
        RAW / "slide-ocr" / video_id,
    ]
    removed: list[str] = []
    for path in paths:
        if path.is_symlink() or path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)
        else:
            continue
        try:
            removed.append(str(path.relative_to(ROOT)))
        except ValueError:
            removed.append(str(path))
    retire_standard_slide_references(video_id)
    return removed


def try_extract_slides(video: VideoEntry, matched_talks: list[dict[str, str]], *, enabled: bool) -> dict[str, object]:
    no_slides_evidence = explicit_no_slides_evidence(video.video_id)
    if no_slides_evidence:
        return {
            "status": NO_SLIDES_STATUS,
            "reason": "explicit_transcript_statement",
            "evidence": no_slides_evidence,
            "removed_artifacts": retire_standard_slide_artifacts(video.video_id),
        }
    if slides_path(video.video_id).exists():
        return {"status": "already_extracted", "path": str(slides_path(video.video_id).relative_to(ROOT))}
    if not enabled:
        return {"status": "skipped_by_configuration"}
    if video.live_status == "is_upcoming":
        return {"status": "pending_premiere", "release_date": video.release_date}
    cmd = [sys.executable, "scripts/extract_video_slides.py", "--scene-detect", f"--video-id={video.video_id}", "--max-slides", "32"]
    outputs: list[str] = []
    for _attempt in range(2):
        cp = run(cmd, timeout=1500)
        outputs.append((cp.stderr or cp.stdout)[-1600:])
        if slides_path(video.video_id).exists():
            return {"status": "slide_extraction_ran", "path": str(slides_path(video.video_id).relative_to(ROOT))}
    return {"status": "slide_extraction_failed", "error": "\n".join(outputs)[-2400:]}


def update_channel_snapshot(entries: list[VideoEntry]) -> bool:
    payload = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "channel_id": CHANNEL_ID,
        "source_url": CHANNEL_RSS,
        "entries": [
            {
                "id": entry.video_id,
                "title": entry.title,
                "url": entry.url,
                "published": entry.published,
                "published_date": entry.published_date.isoformat(),
                "updated": entry.updated,
                "channel": OFFICIAL_CHANNEL,
                "source": "official_youtube_rss",
            }
            for entry in entries
        ],
    }
    existing = load_json(RSS_SNAPSHOT, {})
    stable_keys = ("id", "title", "url", "published", "published_date", "channel", "source")
    old_entries = [tuple(item.get(key) for key in stable_keys) for item in existing.get("entries", [])] if isinstance(existing, dict) else []
    new_entries = [tuple(item.get(key) for key in stable_keys) for item in payload["entries"]]
    if old_entries == new_entries:
        return False
    write_json(RSS_SNAPSHOT, payload)
    return True


def wiki_maker_executable() -> str:
    override = os.environ.get(WIKI_MAKER_ENV, "").strip()
    if override:
        candidate = Path(override).expanduser()
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate.resolve())
        resolved = shutil.which(override)
        if resolved:
            return resolved
        raise RuntimeError(f"{WIKI_MAKER_ENV} does not name an executable: {override}")

    sibling = ROOT.parent / "wiki-from-topic-maker" / ".venv" / "bin" / "wiki-from-topic-maker"
    if sibling.is_file() and os.access(sibling, os.X_OK):
        return str(sibling)
    resolved = shutil.which("wiki-from-topic-maker")
    if resolved:
        return resolved
    raise RuntimeError(
        "wiki-from-topic-maker is unavailable; set "
        f"{WIKI_MAKER_ENV} to the installed executable"
    )


def update_source_paths(video_ids: list[str]) -> list[Path]:
    candidates = [OFFICIAL_VIDEO_MANIFEST]
    for video_id in sorted(set(video_ids)):
        candidates.append(transcript_path(video_id))
        candidates.extend(sorted((RAW / "youtube-subtitles").glob(f"{video_id}*.vtt")))
    return sorted({path for path in candidates if path.is_file()})


def playable_manifest_projection(payload: object) -> dict[str, dict[str, object]]:
    if not isinstance(payload, dict):
        return {}
    return {
        str(item["id"]): item
        for item in payload.get("videos", [])
        if isinstance(item, dict)
        and item.get("id")
        and item.get("mediaType") in PLAYABLE_MEDIA_TYPES
    }


def run_enrichment(_imported_transcripts: int, video_ids: list[str]) -> list[dict[str, object]]:
    cmd = [
        wiki_maker_executable(),
        "update",
        str(ROOT),
        "--change-type",
        "media",
    ]
    for path in update_source_paths(video_ids):
        cmd.extend(["--source", str(path.relative_to(ROOT))])
    cmd.append("--json")
    cp = run(cmd, timeout=7200)
    return [{"cmd": cmd, "returncode": cp.returncode}]


def maybe_commit_and_push(enabled: bool, message: str) -> dict[str, object]:
    if not enabled:
        return {"enabled": False}
    branch = run(["git", "branch", "--show-current"], timeout=60)
    current_branch = branch.stdout.strip()
    if branch.returncode != 0 or current_branch != "main":
        return {
            "enabled": True,
            "blocked": True,
            "reason": "auto-push requires the checked-out main branch",
            "branch": current_branch,
        }
    status = run(["git", "status", "--porcelain"], timeout=60)
    if not status.stdout.strip():
        return {"enabled": True, "changed": False}
    add_paths = [path for path in ["raw", "wiki", "scripts", "package.json", "package-lock.json"] if (ROOT / path).exists()]
    run(["git", "add", *add_paths], timeout=120)
    staged = run(["git", "diff", "--cached", "--quiet"], timeout=60)
    if staged.returncode == 0:
        return {"enabled": True, "changed": False, "note": "no publishable staged changes"}
    commit = run(["git", "commit", "-m", message], timeout=120)
    if commit.returncode != 0:
        return {"enabled": True, "changed": True, "commit_returncode": commit.returncode, "error": commit.stderr[-1000:]}
    push = run(["git", "push", "origin", "HEAD:main"], timeout=300)
    return {"enabled": True, "changed": True, "commit_returncode": commit.returncode, "push_returncode": push.returncode}


def auto_push_preflight() -> dict[str, object]:
    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=60,
    )
    branch = subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=60,
    )
    current_branch = branch.stdout.strip()
    if status.returncode != 0 or branch.returncode != 0:
        return {
            "ok": False,
            "reason": "git preflight failed",
            "git_status_returncode": status.returncode,
            "git_branch_returncode": branch.returncode,
            "branch": current_branch,
        }
    if current_branch != "main":
        return {
            "ok": False,
            "reason": "auto-push requires the checked-out main branch",
            "branch": current_branch,
        }
    if status.stdout.strip():
        return {
            "ok": False,
            "reason": "auto-push requires a clean pre-run worktree",
            "branch": current_branch,
            "worktree_status": status.stdout.splitlines(),
        }
    return {"ok": True, "branch": current_branch}


def write_status(report: dict[str, object]) -> None:
    write_json(STATUS_JSON, report)
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    for item in report.get("processed", []) or []:
        rows.append(
            "<tr>"
            f"<td>{html.escape(str(item.get('published_date', '')))}</td>"
            f"<td><code>{html.escape(str(item.get('id', '')))}</code></td>"
            f"<td>{html.escape(str(item.get('title', '')))}</td>"
            f"<td>{html.escape(str(item.get('resource_status', '')))}</td>"
            f"<td>{html.escape(str((item.get('transcript') or {}).get('status', '')))}</td>"
            f"<td>{html.escape(str((item.get('slides') or {}).get('status', '')))}</td>"
            "</tr>"
        )
    STATUS_HTML.write_text(
        f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>AIE WF2026 YouTube monitor status</title>
<style>
body {{ font: 16px/1.5 system-ui, sans-serif; margin: 40px; color: #17202a; background: #f7f8f4; }}
main {{ max-width: 1080px; background: #fff; border: 1px solid #d9ded6; border-radius: 12px; padding: 28px; }}
code {{ background: #eef2ec; padding: 2px 5px; border-radius: 4px; }}
table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
th, td {{ text-align: left; border-bottom: 1px solid #d9ded6; padding: 8px; vertical-align: top; }}
.state {{ color: #0f766e; font-weight: 800; }}
</style>
</head>
<body>
<main>
<p class="state">{html.escape(str(report.get('state')))}</p>
<h1>AIE WF2026 YouTube monitor</h1>
<p>Checked at: <code>{html.escape(str(report.get('checked_at')))}</code></p>
<p>Latest official video date: <code>{html.escape(str(report.get('latest_published_date')))}</code>; active cutoff date: <code>{html.escape(str(report.get('active_cutoff_date')))}</code>.</p>
<p>{html.escape(str(report.get('message', '')))}</p>
<table>
<thead><tr><th>Date</th><th>ID</th><th>Title</th><th>Resource</th><th>Transcript</th><th>Slides</th></tr></thead>
<tbody>{''.join(rows) or '<tr><td colspan="6">No newly processed videos in this run.</td></tr>'}</tbody>
</table>
</main>
</body>
</html>
""",
        encoding="utf-8",
    )


def open_status_page() -> None:
    if not os.environ.get("DISPLAY"):
        return
    opener = shutil.which("xdg-open") or shutil.which("firefox")
    if opener:
        subprocess.Popen([opener, str(STATUS_HTML)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def stop_timer_if_present() -> None:
    if shutil.which("systemctl"):
        subprocess.run(["systemctl", "--user", "disable", "--now", "aie-wf2026-youtube-monitor.timer"], text=True, capture_output=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--playlist-only",
        action="store_true",
        help="Manually synchronize every official WF26 playlist item, bypassing RSS and the timer cutoff.",
    )
    parser.add_argument("--no-slides", action="store_true", help="Skip slide extraction attempts for new videos.")
    push = parser.add_mutually_exclusive_group()
    push.add_argument(
        "--auto-push",
        dest="auto_push",
        action="store_true",
        help="Commit and push successful import changes from a clean main checkout.",
    )
    push.add_argument(
        "--no-auto-push",
        dest="auto_push",
        action="store_false",
        help="Never commit or push, overriding the service environment.",
    )
    parser.set_defaults(auto_push=None)
    parser.add_argument("--open-status", action="store_true", help="Open the status page after this run.")
    args = parser.parse_args(argv)

    checked_at = datetime.now(timezone.utc)
    auto_push = (
        args.auto_push
        if args.auto_push is not None
        else False
        if args.playlist_only
        else os.environ.get("AIE_WF2026_MONITOR_AUTO_PUSH") == "1"
    )
    if auto_push and not args.dry_run:
        preflight = auto_push_preflight()
        if not preflight.get("ok"):
            report = {
                "checked_at": checked_at.isoformat(),
                "channel_id": CHANNEL_ID,
                "state": "blocked",
                "message": f"Monitor skipped: {preflight.get('reason')}; no files were changed.",
                "publish_preflight": preflight,
                "processed": [],
                "dry_run": False,
            }
            print(json.dumps(report, sort_keys=True))
            return 2

    talks = read_talk_pages()
    playlist_entries: list[PlaylistEntry] = []
    if args.playlist_only:
        snapshot_changed = False
        playlist_entries, discovery = fetch_official_playlist(talks)
        discovered_rows = []
        event_rows = [
            (item.video, list(item.matched_talks))
            for item in playlist_entries
            if item.video is not None
        ]
    else:
        entries = fetch_rss()
        snapshot_changed = False if args.dry_run else update_channel_snapshot(entries)
        rss_event_rows = event_entries(entries, talks)
        discovered_rows, discovery = discover_recent_channel_event_rows(talks)
        combined_rows = {entry.video_id: (entry, matched) for entry, matched in rss_event_rows}
        combined_rows.update({entry.video_id: (entry, matched) for entry, matched in discovered_rows})
        event_rows = list(combined_rows.values())
    scheduled_manifest_ids = scheduled_manifest_video_ids()
    pending_manifest_ids = pending_manifest_video_ids()
    manifest_before = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    manifest_changed = update_official_video_manifest(
        discovered_rows,
        playlist_entries=playlist_entries,
        write=not args.dry_run,
    )
    manifest_after = (
        load_json(OFFICIAL_VIDEO_MANIFEST, {}) if not args.dry_run else manifest_before
    )
    known_no_slides_ids = no_slides_manifest_video_ids()
    playable_evidence_changed = (
        not args.dry_run
        and playable_manifest_projection(manifest_before)
        != playable_manifest_projection(manifest_after)
    )
    today = checked_at.date()
    cutoff = today - timedelta(days=6)
    latest_date = max((entry.published_date for entry, _matched in event_rows), default=None)

    report: dict[str, object] = {
        "checked_at": checked_at.isoformat(),
        "channel_id": CHANNEL_ID,
        "active_cutoff_date": cutoff.isoformat(),
        "latest_published_date": latest_date.isoformat() if latest_date else "",
        "processed": [],
        "dry_run": args.dry_run,
        "mode": "playlist_only" if args.playlist_only else "scheduled_monitor",
        "auto_push": auto_push,
        "manifest_changed": manifest_changed,
        "channel_discovery": discovery,
    }

    if not args.playlist_only and (latest_date is None or latest_date < cutoff):
        report.update(
            {
                "state": "stopped",
                "message": "No confirmed AI Engineer World's Fair 2026 event video was published within the last seven calendar dates; monitor disabled.",
            }
        )
        if args.dry_run:
            print(json.dumps(report, sort_keys=True))
        else:
            write_status(report)
            stop_timer_if_present()
            open_status_page()
        return 0

    recent_rows = (
        event_rows
        if args.playlist_only
        else [(entry, matched) for entry, matched in event_rows if entry.published_date >= cutoff]
    )
    process_rows = [
        (entry, matched)
        for entry, matched in recent_rows
        if not resource_path(entry.video_id).exists()
        or resource_schedule_projection_needed(entry.video_id, matched)
        or (
            entry.video_id in scheduled_manifest_ids
            and entry.live_status != "is_upcoming"
        )
        or (
            entry.video_id in pending_manifest_ids
            and entry.has_english_captions
            and not transcript_path(entry.video_id).exists()
        )
        or (
            args.playlist_only
            and entry.live_status != "is_upcoming"
            and no_slides_reconciliation_needed(entry.video_id, known_no_slides_ids)
        )
        or (
            args.playlist_only
            and entry.live_status != "is_upcoming"
            and (
                not transcript_path(entry.video_id).exists()
                or (
                    not args.no_slides
                    and os.environ.get("AIE_WF2026_MONITOR_SKIP_SLIDES") != "1"
                    and entry.video_id not in known_no_slides_ids
                    and not slides_path(entry.video_id).exists()
                )
            )
        )
    ]
    processed: list[dict[str, object]] = []
    transcript_imports = 0
    acquisition_changed = manifest_changed

    for entry, matched in process_rows:
        transcript = {"status": "dry_run"}
        slides = {"status": "dry_run"}
        resource_status = "dry_run"
        talk_updates = 0
        if not args.dry_run:
            transcript = try_import_captions(
                entry, allow_browser_fallback=not args.playlist_only
            )
            if args.playlist_only and (
                str(transcript.get("status")) in CAPTION_FAILURE_STATUSES
                or str(transcript.get("status", "")).endswith("_failed")
            ):
                transcript = {
                    **transcript,
                    "attempt_status": transcript.get("status"),
                    "status": "caption_acquisition_pending",
                }
            if transcript.get("status") == "captions_imported":
                transcript_imports += 1
            slides = try_extract_slides(entry, matched, enabled=not args.no_slides and os.environ.get("AIE_WF2026_MONITOR_SKIP_SLIDES") != "1")
            if args.playlist_only and str(slides.get("status", "")).endswith("_failed"):
                slides = {
                    **slides,
                    "attempt_status": slides.get("status"),
                    "status": "slide_acquisition_pending",
                }
            resource_changed = write_resource_page(
                entry,
                matched,
                str(transcript.get("status")),
                str(slides.get("status")),
                association_evidence=(
                    "official_wf26_playlist_membership"
                    if args.playlist_only
                    else "official_channel_plus_schedule_text"
                ),
            )
            talk_updates = update_talk_pages(entry, matched)
            resource_status = "created_or_updated" if resource_changed else "unchanged"
            item_changed = any(
                (
                    transcript.get("status") == "captions_imported",
                    slides.get("status") == "slide_extraction_ran",
                    slides.get("status") == NO_SLIDES_STATUS,
                    resource_changed,
                    talk_updates > 0,
                )
            )
            acquisition_changed = acquisition_changed or item_changed
            playable_evidence_changed = playable_evidence_changed or (
                entry.live_status != "is_upcoming" and item_changed
            )
        processed.append(
            {
                "id": entry.video_id,
                "title": entry.title,
                "url": entry.url,
                "published": entry.published,
                "published_date": entry.published_date.isoformat(),
                "matched_talks": [{"id": talk["id"], "title": talk["title"]} for talk in matched],
                "resource_status": resource_status,
                "talk_updates": talk_updates,
                "transcript": transcript,
                "slides": slides,
            }
        )

    unavailable_entries = [item for item in playlist_entries if item.video is None]
    for item in unavailable_entries:
        resource_status = "dry_run"
        if not args.dry_run:
            resource_changed = write_unavailable_resource_page(item)
            resource_status = "created_or_updated" if resource_changed else "unchanged"
            acquisition_changed = acquisition_changed or resource_changed
        processed.append(
            {
                "id": item.video_id,
                "title": item.playlist_title,
                "url": f"https://www.youtube.com/watch?v={item.video_id}",
                "published": "",
                "published_date": "",
                "matched_talks": [],
                "resource_status": resource_status,
                "talk_updates": 0,
                "transcript": {"status": "unavailable", "reason": item.availability},
                "slides": {"status": "unavailable", "reason": item.availability},
            }
        )

    report["processed"] = processed
    if not args.dry_run:
        manifest_before_artifact_refresh = load_json(OFFICIAL_VIDEO_MANIFEST, {})
        artifact_manifest_changed = refresh_manifest_artifact_statuses(processed)
        if artifact_manifest_changed:
            manifest_after_artifact_refresh = load_json(OFFICIAL_VIDEO_MANIFEST, {})
            manifest_changed = True
            acquisition_changed = True
            playable_evidence_changed = playable_evidence_changed or (
                playable_manifest_projection(manifest_before_artifact_refresh)
                != playable_manifest_projection(manifest_after_artifact_refresh)
            )
            report["manifest_changed"] = True
        item_failures = media_item_failures(processed)
        report["item_failures"] = item_failures
        report["failure_count"] = len(item_failures)
        if item_failures:
            every_component_failed = bool(processed) and all(
                str(item.get("transcript", {}).get("status")) in CAPTION_FAILURE_STATUSES
                and str(item.get("slides", {}).get("status")) in SLIDE_FAILURE_STATUSES
                for item in processed
            )
            failure_state = "failed" if every_component_failed else "degraded"
            report.update(
                {
                    "state": failure_state,
                    "status": failure_state,
                    "message": "One or more monitor media-import items failed; changes were not published and the timer will retry.",
                    "recent_entry_count": len(recent_rows),
                    "new_entry_count": len(process_rows),
                }
            )
            write_status(report)
            return 1
        report["playable_evidence_changed"] = playable_evidence_changed
        if playable_evidence_changed:
            private_policy = {
                "status": "delegated_to_unified_maker_dag",
                "adapter": "credibility_policy",
            }
        else:
            private_policy = {
                "status": "not_needed",
                "reason": "no admitted or updated playable evidence changed",
            }
        report["private_credibility_v2"] = private_policy
        enrichment = (
            run_enrichment(
                transcript_imports,
                [entry.video_id for entry, _matched in process_rows]
                + [item.video_id for item in unavailable_entries],
            )
            if playable_evidence_changed
            else []
        )
        report["enrichment"] = enrichment
        enrichment_failed = any(item.get("returncode") != 0 for item in enrichment)
        if enrichment_failed:
            report.update(
                {
                    "state": "degraded",
                    "message": "A monitor enrichment command failed; changes were not published and the timer will retry.",
                    "recent_entry_count": len(recent_rows),
                    "new_entry_count": len(process_rows),
                }
            )
            write_status(report)
            return 1
        report["publish"] = maybe_commit_and_push(
            auto_push and (acquisition_changed or snapshot_changed),
            "Import new official AI Engineer YouTube videos",
        )
        publish = report["publish"]
        if publish.get("blocked") or publish.get("commit_returncode", 0) != 0 or publish.get("push_returncode", 0) != 0:
            report.update(
                {
                    "state": "degraded",
                    "message": "Monitor publishing failed; generated changes remain local and the timer will retry.",
                    "recent_entry_count": len(recent_rows),
                    "new_entry_count": len(process_rows),
                }
            )
            write_status(report)
            return 1

    report.update(
        {
            "state": "active",
            "message": (
                f"Synchronized the official WF26 playlist and processed {len(processed)} items."
                if args.playlist_only
                else f"Confirmed AI Engineer World's Fair 2026 event videos are still being published within the last seven calendar dates. Processed {len(processed)} new RSS entries; monitor remains active."
            ),
            "recent_entry_count": len(recent_rows) + len(unavailable_entries),
            "new_entry_count": len(process_rows),
            "acquisition_changed": acquisition_changed,
            "playable_evidence_changed": playable_evidence_changed,
        }
    )
    if args.dry_run:
        print(json.dumps(report, sort_keys=True))
    else:
        write_status(report)
        if args.open_status:
            open_status_page()
    return 0


def media_item_failures(processed: list[dict[str, object]]) -> list[dict[str, str]]:
    failures: list[dict[str, str]] = []
    for item in processed:
        for component, failure_statuses in (
            ("transcript", CAPTION_FAILURE_STATUSES),
            ("slides", SLIDE_FAILURE_STATUSES),
        ):
            result = item.get(component)
            if not isinstance(result, dict):
                continue
            status = str(result.get("status") or "")
            if status not in failure_statuses and not status.endswith("_failed"):
                continue
            failures.append(
                {
                    "id": str(item.get("id") or ""),
                    "component": component,
                    "status": status,
                    "error": str(result.get("error") or result.get("yt_dlp_error") or ""),
                }
            )
    return failures


def run_entrypoint(argv: list[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    try:
        return main(arguments)
    except Exception as exc:
        previous = load_json(STATUS_JSON, {})
        report = {
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "channel_id": CHANNEL_ID,
            "state": "degraded",
            "status": "degraded",
            "message": "The monitor failed before completing. The systemd service will retry automatically.",
            "error": {"type": type(exc).__name__, "message": str(exc)},
            "previous_checked_at": previous.get("checked_at", "") if isinstance(previous, dict) else "",
            "processed": [],
            "dry_run": "--dry-run" in arguments,
        }
        if report["dry_run"]:
            print(json.dumps(report, sort_keys=True))
        else:
            write_status(report)
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    raise SystemExit(run_entrypoint())
