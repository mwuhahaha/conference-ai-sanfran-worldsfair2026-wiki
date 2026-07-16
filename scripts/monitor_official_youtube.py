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
CAPTION_FAILURE_STATUSES = {
    "chrome_agent_unavailable",
    "chrome_caption_import_failed",
    "empty_caption_file",
}
SLIDE_FAILURE_STATUSES = {"slide_extraction_failed"}
WIKI_MAKER_ENV = "WIKI_FROM_TOPIC_MAKER"


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

    @property
    def published_date(self) -> date:
        return datetime.fromisoformat(self.published.replace("Z", "+00:00")).date()


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
    )


def fetch_video_metadata(video_id: str) -> VideoEntry:
    cp = subprocess.run(
        [
            yt_dlp_binary(),
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
    return video_entry_from_metadata(payload)


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


def update_official_video_manifest(rows: list[tuple[VideoEntry, list[dict[str, str]]]]) -> bool:
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
        entry = {
            "id": video.video_id,
            "title": video.title,
            "mediaType": "scheduled_premiere" if video.live_status == "is_upcoming" else "talk_recording",
            "associationEvidence": "official_channel_plus_schedule_text",
            "matchedTalks": [talk["id"] for talk in matched],
            "uploadDate": video.published_date.isoformat(),
            "releaseDate": video.release_date,
            "transcriptStatus": "available_on_youtube" if video.has_english_captions else "pending",
        }
        if videos.get(video.video_id) != entry:
            videos[video.video_id] = entry
            changed = True
    if not changed:
        return False
    payload.update(
        {
            "schemaVersion": 1,
            "sourceBoundary": "Only official AI Engineer channel media independently associated with the WF2026 schedule is primary event video evidence.",
            "videos": sorted(videos.values(), key=lambda item: (str(item.get("uploadDate", "")), str(item.get("id", "")))),
        }
    )
    write_json(OFFICIAL_VIDEO_MANIFEST, payload)
    return True


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
        short_title = len(talk_title_tokens) < 4
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


def write_resource_page(video: VideoEntry, matched_talks: list[dict[str, str]], transcript_status: str, slide_status: str) -> bool:
    path = resource_path(video.video_id)
    talk_lines = []
    if matched_talks:
        for talk in matched_talks:
            talk_lines.append(f"- [[{talk['id']}|{talk['title']}]]")
    else:
        talk_lines.append("- No exact schedule-page match has been assigned yet; this was admitted only because the official-channel title explicitly identifies it as WF26 / World's Fair 2026 event media.")
    transcript_line = (
        f"Cached transcript text is available at `raw/sources/youtube-transcripts/{video.video_id}.txt`."
        if transcript_path(video.video_id).exists()
        else f"Transcript import status: {transcript_status}."
    )
    slide_line = f"- [[youtube-{video.video_id}-slides]]" if slides_path(video.video_id).exists() else f"- Slide extraction status: {slide_status}."
    upcoming = video.live_status == "is_upcoming"
    media_description = (
        "A scheduled official AI Engineer YouTube premiere independently matched to an AI Engineer World's Fair San Francisco 2026 session. The page records the pending media source now; transcript and slide evidence remain unavailable until the premiere is playable."
        if upcoming
        else "An official AI Engineer YouTube recording independently matched to an AI Engineer World's Fair San Francisco 2026 session. Official schedule pages remain canonical for schedule metadata."
    )
    release_line = f"- Scheduled premiere date: {video.release_date}." if upcoming and video.release_date else ""
    text = "\n".join(
        [
            frontmatter(
                {
                    "title": video.title,
                    "category": "resources",
                    "sourceLabels": ["Official AI Engineer YouTube channel", "Official-channel video metadata"],
                    "videoId": video.video_id,
                    "publishedDate": video.published_date.isoformat(),
                    "last_enriched": datetime.now(timezone.utc).isoformat(),
                }
            ).rstrip(),
            f"# {video.title}",
            "",
            "## What It Is",
            media_description,
            "",
            "## Source Classification",
            "- Source role: primary event video source for AI Engineer World's Fair San Francisco 2026.",
            f"- Published date: {video.published_date.isoformat()}",
            release_line,
            f"- Channel/source: {OFFICIAL_CHANNEL}.",
            "- Use: use as media/transcript/slide evidence for the event recording; keep schedule facts tied to the official schedule pages.",
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
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if old == text + "\n":
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text + "\n", encoding="utf-8")
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
    body = "\n".join(
        [
            media_line,
            f"- Evidence status: {evidence}.",
            "- Boundary: use this recording as media evidence; keep date/time/room facts tied to the official schedule.",
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


def try_import_captions(video: VideoEntry) -> dict[str, object]:
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
        chrome = try_import_captions_with_chrome_agent(video)
        if chrome.get("status") == "captions_imported":
            return chrome
        chrome["yt_dlp_error"] = (cp.stderr or cp.stdout)[-1600:]
        return chrome
    after = set(subtitle_dir.glob(f"{video.video_id}*.vtt"))
    candidates = sorted(after - before) or sorted(after)
    if not candidates:
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


def try_extract_slides(video: VideoEntry, matched_talks: list[dict[str, str]], *, enabled: bool) -> dict[str, object]:
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
    push = run(["git", "push", "origin", "main"], timeout=300)
    return {"enabled": True, "changed": True, "commit_returncode": commit.returncode, "push_returncode": push.returncode}


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
    parser.add_argument("--no-slides", action="store_true", help="Skip slide extraction attempts for new videos.")
    parser.add_argument("--auto-push", action="store_true", help="Commit and push successful import changes to origin/main.")
    parser.add_argument("--open-status", action="store_true", help="Open the status page after this run.")
    args = parser.parse_args(argv)

    checked_at = datetime.now(timezone.utc)
    auto_push = args.auto_push or os.environ.get("AIE_WF2026_MONITOR_AUTO_PUSH") == "1"
    if auto_push and not args.dry_run:
        initial_status = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=60,
        )
        if initial_status.returncode != 0 or initial_status.stdout.strip():
            report = {
                "checked_at": checked_at.isoformat(),
                "channel_id": CHANNEL_ID,
                "state": "blocked",
                "message": "Monitor skipped because the publish worktree was not clean; no files were changed.",
                "worktree_status": initial_status.stdout.splitlines(),
                "git_status_returncode": initial_status.returncode,
                "processed": [],
                "dry_run": False,
            }
            write_status(report)
            return 2

    entries = fetch_rss()
    snapshot_changed = False if args.dry_run else update_channel_snapshot(entries)
    talks = read_talk_pages()
    rss_event_rows = event_entries(entries, talks)
    discovered_rows, discovery = discover_recent_channel_event_rows(talks)
    combined_rows = {entry.video_id: (entry, matched) for entry, matched in rss_event_rows}
    combined_rows.update({entry.video_id: (entry, matched) for entry, matched in discovered_rows})
    event_rows = list(combined_rows.values())
    scheduled_manifest_ids = scheduled_manifest_video_ids()
    pending_manifest_ids = pending_manifest_video_ids()
    manifest_changed = False if args.dry_run else update_official_video_manifest(discovered_rows)
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
        "channel_discovery": discovery,
    }

    if latest_date is None or latest_date < cutoff:
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

    recent_rows = [(entry, matched) for entry, matched in event_rows if entry.published_date >= cutoff]
    process_rows = [
        (entry, matched)
        for entry, matched in recent_rows
        if not resource_path(entry.video_id).exists()
        or (
            entry.video_id in scheduled_manifest_ids
            and entry.live_status != "is_upcoming"
        )
        or (
            entry.video_id in pending_manifest_ids
            and entry.has_english_captions
            and not transcript_path(entry.video_id).exists()
        )
    ]
    processed: list[dict[str, object]] = []
    transcript_imports = 0

    for entry, matched in process_rows:
        transcript = {"status": "dry_run"}
        slides = {"status": "dry_run"}
        resource_status = "dry_run"
        talk_updates = 0
        if not args.dry_run:
            transcript = try_import_captions(entry)
            if transcript.get("status") == "captions_imported":
                transcript_imports += 1
            slides = try_extract_slides(entry, matched, enabled=not args.no_slides and os.environ.get("AIE_WF2026_MONITOR_SKIP_SLIDES") != "1")
            resource_changed = write_resource_page(entry, matched, str(transcript.get("status")), str(slides.get("status")))
            talk_updates = update_talk_pages(entry, matched)
            resource_status = "created_or_updated" if resource_changed else "unchanged"
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

    report["processed"] = processed
    if not args.dry_run:
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
        enrichment = run_enrichment(transcript_imports, [entry.video_id for entry, _matched in process_rows]) if process_rows else []
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
            auto_push and (bool(process_rows) or snapshot_changed or manifest_changed),
            "Import new official AI Engineer YouTube videos",
        )
        publish = report["publish"]
        if publish.get("commit_returncode", 0) != 0 or publish.get("push_returncode", 0) != 0:
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
            "message": f"Confirmed AI Engineer World's Fair 2026 event videos are still being published within the last seven calendar dates. Processed {len(processed)} new RSS entries; monitor remains active.",
            "recent_entry_count": len(recent_rows),
            "new_entry_count": len(process_rows),
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
