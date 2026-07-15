#!/usr/bin/env python3
"""Discover non-official YouTube videos that may be secondary sources for talks.

The tool searches beyond the AI Engineer channel, scores candidate videos against
the official World's Fair schedule, and writes a reviewable evidence report. It
is intentionally conservative: high-confidence matches are secondary sources,
not official recordings, unless a human later verifies otherwise.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from third_party_connection_policy import INTERNAL_DIR, write_internal_policy


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "sources"
WIKI = ROOT / "wiki"
REPORT = RAW / "external-video-discovery-latest.json"
INTERNAL_REPORT = INTERNAL_DIR / "external-video-discovery-internal.json"
REPORT_MD = WIKI / "resources" / "external-video-discovery.md"
OFFICIAL_CHANNELS = {"AI Engineer", "AI Engineer and Theo - t3․gg"}
DEFAULT_QUERIES = [
    "AI Engineer Worldsfair 2026 talk",
    '"AI Engineer" "World\'s Fair" "2026"',
    '"WF2026" "AI Engineer"',
]
RECAP_WORDS = {
    "briefing",
    "compilation",
    "recap",
    "vlog",
    "irl",
    "visits",
    "visit",
    "crew",
    "booth",
    "conference",
    "day",
    "highlights",
    "impressed",
    "digest",
    "news",
    "videos",
}
TALK_HINTS = {
    "talk",
    "keynote",
    "workshop",
    "session",
    "fireside",
    "panel",
    "pitch",
}


def run(cmd: list[str], *, timeout: int = 120) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=timeout)


def load_json(path: Path, fallback: Any) -> Any:
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def public_report(report: dict[str, Any]) -> dict[str, Any]:
    """Remove numeric ranking internals while preserving reviewable source labels."""
    sanitized = {
        key: json.loads(json.dumps(report[key]))
        for key in ("checked_at", "queries", "query_errors", "tool")
        if key in report
    }
    sanitized["results"] = []
    for row in report.get("results", []):
        best = row.get("best_match") or {}
        sanitized["results"].append({
            "video": json.loads(json.dumps(row.get("video") or {})),
            "confidence": row.get("confidence"),
            "transcript_status": row.get("transcript_status"),
            "official_channel": row.get("official_channel"),
            "best_match": {"session": json.loads(json.dumps(best.get("session") or {}))},
        })
    sanitized["policy"] = {
        "high_confidence_is_secondary_source_only": True,
        "identity_and_event_association_require_separate_review": True,
        "numeric_ranking_is_internal_only": True,
    }
    return sanitized


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    return text[: end + 5], text[end + 5 :].lstrip()


def upsert_section(markdown: str, heading: str, section: str) -> str:
    fm, body = split_frontmatter(markdown)
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    replacement = f"## {heading}\n{section.strip()}\n"
    if pattern.search(body):
        body = pattern.sub(replacement, body).rstrip() + "\n"
    else:
        body = body.rstrip() + "\n\n" + replacement
    return fm + body


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-") or "untitled"


def normalize(value: str) -> str:
    value = value.lower()
    value = value.replace("worldsfair", "worlds fair").replace("world’s", "worlds").replace("world's", "worlds")
    value = value.replace("wf26", "wf2026")
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def tokens(value: str) -> set[str]:
    stop = {
        "a",
        "an",
        "and",
        "are",
        "at",
        "by",
        "for",
        "from",
        "in",
        "is",
        "of",
        "on",
        "or",
        "the",
        "to",
        "with",
        "your",
    }
    return {tok for tok in normalize(value).split() if len(tok) > 2 and tok not in stop}


def content_sequence(value: str) -> list[str]:
    content = tokens(value)
    return [tok for tok in normalize(value).split() if tok in content]


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def title_core(title: str) -> str:
    """Keep the likely talk title, dropping speaker/uploader/event suffixes."""
    core = re.split(r"\s+[—–]\s+|\s+\|\s+", title, maxsplit=1)[0]
    core = re.sub(r"\bAI Engineer\b.*$", "", core, flags=re.I).strip(" -|")
    return core or title


def ordered_phrase_ratio(candidate: str, official: str) -> float:
    cand_seq = content_sequence(candidate)
    off_seq = content_sequence(official)
    if not cand_seq or not off_seq:
        return 0.0
    best = 0
    for i in range(len(off_seq)):
        for j in range(len(cand_seq)):
            k = 0
            while i + k < len(off_seq) and j + k < len(cand_seq) and off_seq[i + k] == cand_seq[j + k]:
                k += 1
            best = max(best, k)
    denom = max(3, min(len(off_seq), 8))
    return min(1.0, best / denom)


def lead_phrase_hit(candidate: str, official: str, length: int = 3) -> bool:
    official_seq = content_sequence(official)
    candidate_seq = content_sequence(candidate)
    if len(official_seq) < length:
        return False
    lead = official_seq[:length]
    return any(candidate_seq[i : i + length] == lead for i in range(0, len(candidate_seq) - length + 1))


@dataclass
class Session:
    slug: str
    title: str
    speakers: list[str]
    companies: list[str]
    day: str
    time: str
    room: str
    track: str
    title_norm: str
    title_tokens: set[str]


def load_sessions() -> list[Session]:
    sessions_blob = load_json(RAW / "official-sessions.json", {})
    speakers_blob = load_json(RAW / "official-speakers.json", {})
    company_by_speaker = {item.get("name"): item.get("company", "") for item in speakers_blob.get("speakers", [])}
    sessions = []
    for item in sessions_blob.get("sessions", []):
        title = item.get("title", "")
        speakers = [str(s) for s in item.get("speakers", []) if s]
        companies = sorted({company_by_speaker.get(s, "") for s in speakers if company_by_speaker.get(s, "")})
        day = item.get("day", "")
        speaker_slug = slugify(speakers[0] if speakers else "session")
        slug = f"{date_prefix(day)}-{speaker_slug}-{slugify(title)}"[:150].rstrip("-")
        sessions.append(
            Session(
                slug=slug,
                title=title,
                speakers=speakers,
                companies=companies,
                day=day,
                time=item.get("time", ""),
                room=item.get("room", ""),
                track=item.get("track", ""),
                title_norm=normalize(title),
                title_tokens=tokens(title),
            )
        )
    return sessions


def date_prefix(day: str) -> str:
    if "June 28" in day or "Day 0" in day:
        return "2026-06-28"
    if "June 29" in day or "Day 1" in day:
        return "2026-06-29"
    if "June 30" in day or "Day 2" in day:
        return "2026-06-30"
    if "July 1" in day or "Day 3" in day:
        return "2026-07-01"
    if "July 2" in day or "Day 4" in day:
        return "2026-07-02"
    return "2026-06-29"


def ytsearch(query: str, limit: int, timeout: int) -> list[dict[str, Any]]:
    cp = run(["yt-dlp", "--dump-single-json", "--flat-playlist", "--no-warnings", f"ytsearch{limit}:{query}"], timeout=timeout)
    if cp.returncode != 0:
        return [{"error": cp.stderr[-1000:], "query": query}]
    data = json.loads(cp.stdout)
    return [entry for entry in data.get("entries", []) if isinstance(entry, dict)]


def video_url(video_id: str) -> str:
    return f"https://www.youtube.com/watch?v={video_id}"


def fetch_metadata(video_id: str) -> dict[str, Any]:
    cp = run(["yt-dlp", "--dump-single-json", "--no-warnings", "--skip-download", video_url(video_id)], timeout=120)
    if cp.returncode != 0:
        return {"id": video_id, "metadata_error": cp.stderr[-1000:]}
    data = json.loads(cp.stdout)
    keep = [
        "id",
        "title",
        "uploader",
        "channel",
        "channel_id",
        "duration",
        "description",
        "webpage_url",
        "upload_date",
        "timestamp",
        "view_count",
        "availability",
        "live_status",
    ]
    return {key: data.get(key) for key in keep}


def score_video(video: dict[str, Any], sessions: list[Session]) -> dict[str, Any]:
    title = str(video.get("title") or "")
    core_title = title_core(title)
    uploader = str(video.get("uploader") or video.get("channel") or "")
    description = str(video.get("description") or "")
    text = " ".join([title, uploader, description[:2000]])
    text_norm = normalize(text)
    title_norm = normalize(title)
    text_tokens = tokens(text)
    event_marker = any(marker in text_norm for marker in ["ai engineer worlds fair", "ai engineer world fair", "aie worlds fair", "wf2026", "worldsfair 2026"])
    official = uploader in OFFICIAL_CHANNELS
    recapish = bool(tokens(title) & RECAP_WORDS) and not (tokens(title) & TALK_HINTS)
    talkish = bool(tokens(title) & TALK_HINTS) or " — " in title or " - " in title

    best: dict[str, Any] | None = None
    for session in sessions:
        title_overlap = max(jaccard(tokens(title), session.title_tokens), jaccard(tokens(core_title), session.title_tokens))
        phrase_overlap = ordered_phrase_ratio(core_title, session.title)
        full_title_hit = bool(session.title_norm and session.title_norm in title_norm)
        speaker_hits = [s for s in session.speakers if normalize(s) and normalize(s) in text_norm]
        company_hits = [c for c in session.companies if normalize(c) and normalize(c) in text_norm]
        score = 0.0
        reasons = []
        if event_marker:
            score += 0.22
            reasons.append("event marker in title/metadata")
        if full_title_hit:
            score += 0.48
            reasons.append("official talk title appears in video title")
        elif lead_phrase_hit(core_title, session.title):
            score += 0.42
            reasons.append("leading official title phrase appears in video title")
        elif phrase_overlap >= 0.55:
            score += 0.42
            reasons.append(f"strong ordered title phrase match {phrase_overlap:.2f}")
        elif phrase_overlap >= 0.34:
            score += 0.28
            reasons.append(f"ordered title phrase match {phrase_overlap:.2f}")
        elif title_overlap >= 0.42:
            score += 0.32
            reasons.append(f"title token overlap {title_overlap:.2f}")
        elif title_overlap >= 0.25:
            score += 0.18
            reasons.append(f"partial title token overlap {title_overlap:.2f}")
        if speaker_hits:
            score += min(0.24, 0.12 * len(speaker_hits))
            reasons.append("speaker match: " + ", ".join(speaker_hits[:3]))
        if company_hits:
            score += min(0.16, 0.08 * len(company_hits))
            reasons.append("company match: " + ", ".join(company_hits[:3]))
        if talkish:
            score += 0.08
            reasons.append("talk/session-shaped title")
        if official:
            score -= 0.35
            reasons.append("official channel; not an external secondary source")
        duration = video.get("duration")
        if isinstance(duration, (int, float)):
            if 480 <= duration <= 7200:
                score += 0.08
                reasons.append("plausible talk/workshop duration")
            elif duration < 240:
                score -= 0.12
                reasons.append("short video; likely clip/recap")
        if recapish:
            score -= 0.28
            reasons.append("recap/vlog/event-footage language")
        score = max(0.0, min(score, 1.0))
        evidence_has_identity = full_title_hit or lead_phrase_hit(core_title, session.title) or bool(speaker_hits) or bool(company_hits) or title_overlap >= 0.42
        if not evidence_has_identity and score > 0.55:
            score = 0.55
            reasons.append("capped: generic phrase match without speaker/company/strong title identity")
        candidate = {
            "score": round(score, 3),
            "session": {
                "slug": session.slug,
                "title": session.title,
                "speakers": session.speakers,
                "companies": session.companies,
                "day": session.day,
                "time": session.time,
                "room": session.room,
                "track": session.track,
            },
            "title_overlap": round(title_overlap, 3),
            "phrase_overlap": round(phrase_overlap, 3),
            "speaker_hits": speaker_hits,
            "company_hits": company_hits,
            "reasons": reasons,
        }
        if best is None or candidate["score"] > best["score"]:
            best = candidate

    confidence = "reject"
    usefulness = "noise_or_event_context"
    if best and best["score"] >= 0.78 and event_marker and not official and not recapish:
        confidence = "high"
        usefulness = "secondary_source_candidate_for_talk"
    elif best and best["score"] >= 0.56 and not official:
        confidence = "medium"
        usefulness = "needs_human_review_or_context_source"
    elif event_marker and not official:
        confidence = "low"
        usefulness = "event_context_only"

    return {
        "confidence": confidence,
        "usefulness": usefulness,
        "best_match": best,
        "event_marker": event_marker,
        "official_channel": official,
        "recapish": recapish,
        "talkish": talkish,
    }


def download_captions(video_id: str, target_dir: Path) -> Path | None:
    target_dir.mkdir(parents=True, exist_ok=True)
    before = set(target_dir.glob(f"{video_id}*.vtt"))
    cp = run(
        [
            "yt-dlp",
            "--skip-download",
            "--write-subs",
            "--write-auto-subs",
            "--sub-langs",
            "en.*",
            "--sub-format",
            "vtt",
            "-o",
            str(target_dir / f"{video_id}.%(ext)s"),
            video_url(video_id),
        ],
        timeout=300,
    )
    if cp.returncode != 0:
        return None
    after = set(target_dir.glob(f"{video_id}*.vtt"))
    new = sorted(after - before) or sorted(after)
    return new[0] if new else None


def vtt_to_text(path: Path) -> str:
    lines = []
    seen = set()
    for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.strip()
        if not line or line == "WEBVTT" or "-->" in line or line.isdigit() or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        line = re.sub(r"<[^>]+>", "", line)
        line = re.sub(r"\s+", " ", line).strip()
        if line and line not in seen:
            seen.add(line)
            lines.append(line)
    return " ".join(lines)


def yt_dlp_js_runtime_arg() -> str:
    node = shutil.which("node")
    if not node:
        for candidate in sorted(Path("/home/dylan/.nvm/versions/node").glob("*/bin/node"), reverse=True):
            if candidate.exists():
                node = str(candidate)
                break
    return f"node:{node}" if node else "node"


def whisper_transcribe(video_id: str, model_name: str) -> str:
    from faster_whisper import WhisperModel

    audio_dir = ROOT / "raw" / "external-audio-cache"
    audio_dir.mkdir(parents=True, exist_ok=True)
    output = audio_dir / f"{video_id}.mp3"
    cp = run(
        [
            "yt-dlp",
            "--js-runtimes",
            yt_dlp_js_runtime_arg(),
            "--remote-components",
            "ejs:github",
            "-f",
            "ba[ext=m4a]/ba/bestaudio",
            "-x",
            "--audio-format",
            "mp3",
            "--audio-quality",
            "5",
            "-o",
            str(audio_dir / f"{video_id}.%(ext)s"),
            video_url(video_id),
        ],
        timeout=900,
    )
    if cp.returncode != 0:
        raise RuntimeError(cp.stderr[-1600:])
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    segments, _info = model.transcribe(str(output), beam_size=5, vad_filter=True)
    return " ".join(segment.text.strip() for segment in segments if segment.text.strip())


def import_high_confidence(results: list[dict[str, Any]], *, whisper: bool, model: str) -> None:
    subtitle_dir = RAW / "external-youtube-subtitles"
    transcript_dir = RAW / "external-youtube-transcripts"
    transcript_dir.mkdir(parents=True, exist_ok=True)
    for row in results:
        if row.get("confidence") != "high":
            continue
        video_id = row["video"]["id"]
        target = transcript_dir / f"{video_id}.txt"
        if target.exists():
            row["transcript_status"] = {"status": "already_cached", "path": str(target.relative_to(ROOT))}
            continue
        sub = download_captions(video_id, subtitle_dir)
        if sub:
            text = vtt_to_text(sub)
            target.write_text(text.strip() + "\n", encoding="utf-8")
            row["transcript_status"] = {
                "status": "captions_imported",
                "path": str(target.relative_to(ROOT)),
                "caption_path": str(sub.relative_to(ROOT)),
                "word_count": len(text.split()),
            }
            continue
        if whisper:
            try:
                text = whisper_transcribe(video_id, model)
                target.write_text(text.strip() + "\n", encoding="utf-8")
                row["transcript_status"] = {"status": "whisper_imported", "path": str(target.relative_to(ROOT)), "word_count": len(text.split())}
            except Exception as exc:  # noqa: BLE001 - report failure without killing entire discovery.
                row["transcript_status"] = {"status": "whisper_failed", "error": str(exc)[-1200:]}
        else:
            row["transcript_status"] = {"status": "no_captions_found_whisper_not_requested"}


def render_wiki(report: dict[str, Any]) -> str:
    rows = report.get("results", [])
    high = [r for r in rows if r.get("confidence") == "high"]
    medium = [r for r in rows if r.get("confidence") == "medium"]
    context = [r for r in rows if r.get("confidence") == "low"]
    lines = [
        "---",
        'title: "External YouTube Video Discovery"',
        'category: "resources"',
        'sourceLabels: ["yt-dlp search", "Secondary source triage", "Official schedule matching"]',
        "---",
        "",
        "# External YouTube Video Discovery",
        "",
        "This page is generated by `scripts/discover_external_event_videos.py`. It searches YouTube beyond the official AI Engineer channel and reviews candidates against the official World's Fair schedule. High-confidence rows are still **secondary sources only** until a human verifies the recording against the official schedule and source video.",
        "",
        "## Latest Run",
        f"- Checked at: `{report.get('checked_at')}`",
        f"- Queries: {len(report.get('queries', []))}",
        f"- Unique videos reviewed: {len(rows)}",
        f"- High-confidence secondary-source candidates: {len(high)}",
        f"- Medium-confidence review candidates: {len(medium)}",
        f"- Low-confidence event-context videos: {len(context)}",
        "",
        "## Review Boundary",
        "- Confidence labels are qualitative review states, not publication approval or endorsement.",
        "- Matched talk labels identify the official session considered during review; they do not prove that a candidate is the event recording.",
        "- External videos remain secondary sources unless a human verifies their identity and event association.",
        "",
        "## High Confidence",
    ]
    if not high:
        lines.append("- No high-confidence external talk videos found in the latest run.")
    for row in high:
        lines.extend(render_candidate(row))
    lines.append("")
    lines.append("## Medium Confidence")
    if not medium:
        lines.append("- No medium-confidence candidates found in the latest run.")
    for row in medium[:25]:
        lines.extend(render_candidate(row))
    lines.append("")
    lines.append("## Event Context / Low Confidence")
    if not context:
        lines.append("- No low-confidence event-context videos found in the latest run.")
    for row in context[:25]:
        video = row.get("video", {})
        lines.append(f"- [{video.get('title')}]({video.get('webpage_url') or video_url(video.get('id', ''))}) — {video.get('uploader')} — event-context candidate")
    lines.append("")
    lines.append("## Source Artifact")
    lines.append("- `raw/sources/external-video-discovery-latest.json`")
    return "\n".join(lines)


def update_talk_pages(report: dict[str, Any]) -> int:
    by_slug: dict[str, list[dict[str, Any]]] = {}
    for row in report.get("results", []):
        if row.get("confidence") != "high":
            continue
        match = (row.get("best_match") or {}).get("session") or {}
        if match.get("slug"):
            by_slug.setdefault(match["slug"], []).append(row)

    updated = 0
    for slug, rows in by_slug.items():
        path = WIKI / "talks" / f"{slug}.md"
        if not path.exists():
            continue
        lines = [
            "These videos were discovered outside the official AI Engineer channel and matched by the external-video discovery tool. Treat them as secondary sources only until manually verified against the official event recording.",
            "",
        ]
        for row in rows:
            video = row.get("video", {})
            best = row.get("best_match") or {}
            transcript = row.get("transcript_status") or {}
            lines.append(f"- [{video.get('title')}]({video.get('webpage_url') or video_url(video.get('id', ''))})")
            lines.append(f"  - Uploader: {video.get('uploader') or video.get('channel')}")
            lines.append(f"  - Confidence label: {row.get('confidence')}")
            if transcript:
                status = transcript.get("status")
                path_text = f" `{transcript.get('path')}`" if transcript.get("path") else ""
                lines.append(f"  - Transcript status: {status}{path_text}")
                transcript_md = WIKI / "transcripts" / f"youtube-{video.get('id')}-transcript.md"
                if transcript_md.exists():
                    lines.append(f"  - Transcript markdown: [[youtube-{video.get('id')}-transcript]]")
        text = path.read_text(encoding="utf-8")
        new_text = upsert_section(text, "External Secondary Source Candidates", "\n".join(lines))
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
    return updated


def render_candidate(row: dict[str, Any]) -> list[str]:
    video = row.get("video", {})
    match = (row.get("best_match") or {}).get("session") or {}
    best = row.get("best_match") or {}
    transcript = row.get("transcript_status") or {}
    lines = [
        f"- [{video.get('title')}]({video.get('webpage_url') or video_url(video.get('id', ''))})",
        f"  - Uploader: {video.get('uploader') or video.get('channel')}",
        f"  - Confidence label: {row.get('confidence')}",
        f"  - Matched talk: [[{match.get('slug')}|{match.get('title')}]]",
        f"  - Schedule: {match.get('day')} · {match.get('time')} · {match.get('room') or match.get('track')}",
    ]
    if transcript:
        lines.append(f"  - Transcript status: {transcript.get('status')} {transcript.get('path', '')}".rstrip())
    return lines


def discover(args: argparse.Namespace) -> dict[str, Any]:
    sessions = load_sessions()
    entries_by_id: dict[str, dict[str, Any]] = {}
    query_errors = []
    for query in args.query or DEFAULT_QUERIES:
        for entry in ytsearch(query, args.limit, args.search_timeout):
            if entry.get("error"):
                query_errors.append(entry)
                continue
            video_id = entry.get("id")
            if video_id:
                entries_by_id.setdefault(video_id, entry)

    known_ids = set()
    for source in ["aidotengineer-channel-videos-latest.json", "aidotengineer-channel-streams-latest.json"]:
        blob = load_json(RAW / source, {})
        items = blob.get("entries", []) if isinstance(blob, dict) else blob
        for item in items:
            if isinstance(item, dict) and item.get("id"):
                known_ids.add(item["id"])

    results = []
    for video_id, flat in sorted(entries_by_id.items()):
        meta = fetch_metadata(video_id) if args.fetch_metadata else {
            "id": video_id,
            "title": flat.get("title"),
            "uploader": flat.get("uploader") or flat.get("channel"),
            "channel": flat.get("channel"),
            "duration": flat.get("duration"),
            "webpage_url": flat.get("url") or video_url(video_id),
        }
        score = score_video(meta, sessions)
        if video_id in known_ids:
            score["known_in_official_channel_cache"] = True
        row = {"video": meta, **score}
        if row["confidence"] != "reject" or args.include_rejects:
            results.append(row)

    results.sort(key=lambda row: ((row.get("best_match") or {}).get("score", 0), row.get("confidence") == "high"), reverse=True)
    if args.import_high_confidence:
        import_high_confidence(results, whisper=args.whisper, model=args.model)

    return {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "tool": "scripts/discover_external_event_videos.py",
        "queries": args.query or DEFAULT_QUERIES,
        "limits": {"per_query": args.limit, "metadata": args.fetch_metadata},
        "policy": {
            "high_confidence_is_secondary_source_only": True,
            "official_channel_results_are_penalized": True,
            "recap_or_vlog_language_is_penalized_for_talk_matching": True,
        },
        "query_errors": query_errors,
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", action="append", help="YouTube search query. Repeatable. Defaults to event-oriented queries.")
    parser.add_argument("--limit", type=int, default=10, help="ytsearch result count per query.")
    parser.add_argument("--search-timeout", type=int, default=45, help="Timeout in seconds for each yt-dlp ytsearch query.")
    parser.add_argument("--fetch-metadata", action="store_true", help="Fetch full per-video yt-dlp metadata. Slower, but improves descriptions/durations.")
    parser.add_argument("--include-rejects", action="store_true", help="Include rejected/noise candidates in JSON output.")
    parser.add_argument("--import-high-confidence", action="store_true", help="Fetch captions for high-confidence secondary-source candidates.")
    parser.add_argument("--update-talk-pages", action="store_true", help="Add high-confidence secondary-source candidates to matched talk pages.")
    parser.add_argument("--whisper", action="store_true", help="Use faster-whisper when high-confidence videos have no captions.")
    parser.add_argument("--model", default="base.en", help="faster-whisper model for --whisper.")
    parser.add_argument("--write-wiki", action="store_true", help="Write wiki/resources/external-video-discovery.md.")
    args = parser.parse_args()

    report = discover(args)
    write_internal_policy()
    write(INTERNAL_REPORT, json.dumps(report, indent=2, ensure_ascii=False))
    sanitized = public_report(report)
    write(REPORT, json.dumps(sanitized, indent=2, ensure_ascii=False))
    if args.write_wiki:
        write(REPORT_MD, render_wiki(sanitized))
    talk_pages_updated = update_talk_pages(report) if args.update_talk_pages else 0
    print(
        json.dumps(
            {
                "results": len(report["results"]),
                "high": sum(1 for row in report["results"] if row.get("confidence") == "high"),
                "medium": sum(1 for row in report["results"] if row.get("confidence") == "medium"),
                "low": sum(1 for row in report["results"] if row.get("confidence") == "low"),
                "report": str(REPORT.relative_to(ROOT)),
                "talk_pages_updated": talk_pages_updated,
                "wiki": str(REPORT_MD.relative_to(ROOT)) if args.write_wiki else None,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
