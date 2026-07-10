#!/usr/bin/env python3
"""Build per-room attendance calibration evidence from local video/frame caches.

This does not claim exact attendance. It creates repeatable evidence artifacts:
sampled frames, per-room contact sheets, and a markdown calibration table that
can be reviewed by a human or a vision model before attendance estimates are
attached to talks.
"""

from __future__ import annotations

import json
import math
import re
import subprocess
from collections import defaultdict
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw" / "sources"
VIDEO_CACHE = ROOT / "raw" / "video-cache"
FRAME_CACHE = ROOT / "raw" / "slide-frames-tmp"
OUT = RAW / "attendance-calibration"
FRAME_OUT = OUT / "frames"
SHEET_OUT = OUT / "contact-sheets"
PUBLIC_ASSET_DIR = "attendance-calibration-v1"
ASSET_SHEET_OUT = WIKI / "assets" / PUBLIC_ASSET_DIR
REPORT = OUT / "room-calibration-evidence.json"
WIKI_PAGE = WIKI / "resources" / "room-attendance-calibration.md"
VALID_YOUTUBE_ID = re.compile(r"^[A-Za-z0-9_-]{11}$")


def slugify(value: str) -> str:
    value = value.lower().replace("&", "and")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-") or "unknown"


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    frontmatter: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"')
    return frontmatter


def collect_room_videos() -> dict[str, list[dict]]:
    videos: dict[str, dict[str, dict]] = defaultdict(dict)
    for path in sorted((WIKI / "talks").glob("*.md")):
        text = path.read_text(errors="ignore")
        fm = parse_frontmatter(text)
        room = fm.get("scheduleRoom") or fm.get("room") or "Unknown"
        track = fm.get("scheduleTrack") or fm.get("track") or ""
        title = fm.get("title") or path.stem
        candidates: list[dict] = []
        for match in re.finditer(r"youtube\.com/watch\?v=([A-Za-z0-9_-]{11})&t=(\d+)s", text):
            candidates.append(
                {
                    "video_id": match.group(1),
                    "source_kind": "worldsfair-livestream-segment",
                    "segment_start_seconds": int(match.group(2)),
                }
            )
        for line in text.splitlines():
            if "youtube.com/watch?v=" not in line:
                continue
            if "Watch in livestream" in line or "&t=" in line:
                continue
            match = re.search(r"youtube\.com/watch\?v=([A-Za-z0-9_-]{11})", line)
            if not match:
                continue
            source_kind = "supporting-related-video" if "speaker-match related prior/adjacent" in line else "candidate-session-video"
            candidates.append({"video_id": match.group(1), "source_kind": source_kind, "segment_start_seconds": None})
        seen = set()
        for candidate in candidates:
            video_id = candidate["video_id"]
            key = (video_id, candidate["source_kind"], candidate.get("segment_start_seconds"))
            if key in seen or not VALID_YOUTUBE_ID.match(video_id):
                continue
            seen.add(key)
            video_path = video_file(video_id)
            frame_dir = FRAME_CACHE / video_id
            videos[room].setdefault(
                f"{video_id}:{candidate['source_kind']}:{candidate.get('segment_start_seconds') or ''}",
                {
                    "video_id": video_id,
                    "title": title,
                    "track": track,
                    "talk_page": str(path.relative_to(ROOT)),
                    "source_kind": candidate["source_kind"],
                    "segment_start_seconds": candidate.get("segment_start_seconds"),
                    "video_cache": str(video_path.relative_to(ROOT)) if video_path else "",
                    "frame_cache": str(frame_dir.relative_to(ROOT)) if frame_dir.exists() else "",
                },
            )
    return {room: list(rows.values()) for room, rows in videos.items()}


def video_file(video_id: str) -> Path | None:
    for ext in [".mp4", ".webm", ".mkv", ".mov"]:
        path = VIDEO_CACHE / f"{video_id}{ext}"
        if path.exists() and path.stat().st_size > 0:
            return path
    return None


def score_candidate(row: dict) -> tuple[int, str]:
    source_rank = {
        "worldsfair-livestream-segment": 0,
        "candidate-session-video": 1,
        "supporting-related-video": 2,
    }.get(row.get("source_kind"), 3)
    media_rank = 0 if row.get("video_cache") else 1 if row.get("frame_cache") else 2
    return (source_rank, media_rank, row.get("title", ""))


def video_duration_seconds(video_path: Path) -> float | None:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(video_path),
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        return None
    try:
        duration = float(result.stdout.strip())
    except ValueError:
        return None
    return duration if duration > 0 else None


def extract_frame(video_path: Path, time_seconds: float, out_path: Path) -> bool:
    result = subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-ss",
            f"{time_seconds:.3f}",
            "-i",
            str(video_path),
            "-frames:v",
            "1",
            "-q:v",
            "3",
            str(out_path),
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return result.returncode == 0 and out_path.exists() and out_path.stat().st_size > 0


def sample_video(
    video_id: str,
    video_path: Path,
    out_dir: Path,
    samples: int,
    segment_start_seconds: int | None = None,
) -> list[dict]:
    out_dir.mkdir(parents=True, exist_ok=True)
    duration = video_duration_seconds(video_path)
    if not duration:
        return []
    positions = [0.08, 0.18, 0.30, 0.42, 0.55, 0.68, 0.80, 0.92][:samples]
    segment_offsets = [20, 75, 150, 240, 360, 540, 720, 900][:samples]
    rows = []
    for index, value in enumerate(segment_offsets if segment_start_seconds is not None else positions, start=1):
        if segment_start_seconds is not None:
            time_seconds = min(duration - 0.5, max(0.5, segment_start_seconds + value))
        else:
            time_seconds = min(duration - 0.5, max(0.5, duration * value))
        out_path = out_dir / f"{video_id}-{index:02d}.jpg"
        if not extract_frame(video_path, time_seconds, out_path):
            continue
        rows.append(
            {
                "path": str(out_path.relative_to(ROOT)),
                "source": "video-cache",
                "frame_index": None,
                "time_seconds": round(time_seconds, 1),
                "segment_start_seconds": segment_start_seconds,
            }
        )
    return rows


def sample_frame_cache(video_id: str, frame_dir: Path, out_dir: Path, samples: int) -> list[dict]:
    frames = sorted(frame_dir.glob("*.jpg"))
    if not frames:
        return []
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    if len(frames) <= samples:
        selected = frames
    else:
        selected = [frames[round(i * (len(frames) - 1) / (samples - 1))] for i in range(samples)]
    for index, source in enumerate(selected, start=1):
        out_path = out_dir / f"{video_id}-cache-{index:02d}.jpg"
        with Image.open(source) as img:
            img.convert("RGB").save(out_path, quality=86)
        rows.append({"path": str(out_path.relative_to(ROOT)), "source": "frame-cache", "time_seconds": None})
    return rows


def make_sheet(room: str, evidence: list[dict]) -> str:
    images = []
    for item in evidence:
        path = ROOT / item["path"]
        if not path.exists():
            continue
        try:
            img = Image.open(path).convert("RGB")
        except Exception:
            continue
        img.thumbnail((300, 170))
        tile = Image.new("RGB", (320, 220), "white")
        tile.paste(img, ((320 - img.width) // 2, 8))
        draw = ImageDraw.Draw(tile)
        label = f"{item['video_id']} {item.get('time_seconds') or ''}"
        draw.text((8, 184), label[:42], fill=(0, 0, 0))
        draw.text((8, 202), item.get("title", "")[:46], fill=(60, 60, 60))
        images.append(tile)
    if not images:
        return ""
    cols = 3
    rows = math.ceil(len(images) / cols)
    sheet = Image.new("RGB", (cols * 320, rows * 220 + 42), "white")
    draw = ImageDraw.Draw(sheet)
    draw.text((10, 10), f"{room} attendance calibration evidence", fill=(0, 0, 0))
    for i, tile in enumerate(images):
        x = (i % cols) * 320
        y = 42 + (i // cols) * 220
        sheet.paste(tile, (x, y))
    SHEET_OUT.mkdir(parents=True, exist_ok=True)
    ASSET_SHEET_OUT.mkdir(parents=True, exist_ok=True)
    out_path = SHEET_OUT / f"{slugify(room)}.jpg"
    asset_path = ASSET_SHEET_OUT / out_path.name
    sheet.save(out_path, quality=88)
    sheet.save(asset_path, quality=88)
    return str(asset_path.relative_to(WIKI))


def inferred_calibration(room: str, evidence_count: int, primary_videos: int, supporting_videos: int) -> dict:
    if primary_videos:
        use = "partial visible-area calibration"
    elif supporting_videos:
        use = "camera-family proxy only"
    else:
        use = "not enough visual evidence"
    confidence = "medium-low" if primary_videos else "low"
    if room == "Main Stage":
        return {
            "room_family": "large keynote/plenary room",
            "camera_model": "front-of-room stage camera with occasional wide audience visibility in livestream/cut footage",
            "coverage": "front/center audience is sometimes visible; rear and far side seating usually hidden",
            "confidence": confidence,
            "use": use,
            "attendance_method": "count visible seats/heads in wide shots, then scale by visible-room fraction; cap against large-room keynote capacity once venue capacity is verified",
        }
    if room.startswith("Expo Stage"):
        return {
            "room_family": "expo-floor stage",
            "camera_model": "open-stage camera; audience may stand or sit outside fixed rows",
            "coverage": "visible crowd varies strongly with booth traffic and camera pan",
            "confidence": confidence,
            "use": use,
            "attendance_method": "estimate occupied standing/seating area from wide shots using sparse/medium/dense standing density bands",
        }
    if room.startswith("Leadership"):
        return {
            "room_family": "leadership breakout room",
            "camera_model": "speaker/slide camera with limited audience views",
            "coverage": "audience evidence is sparse; use only wide or reverse shots",
            "confidence": confidence,
            "use": use,
            "attendance_method": "prefer manual frame review; use detected visible rows only as a lower bound",
        }
    if room in {"Networking Room", "Leadership Lounge"}:
        return {
            "room_family": "lounge/networking room",
            "camera_model": "event/livestream context rather than stable talk capture",
            "coverage": "camera evidence is likely partial and movement-heavy",
            "confidence": "low",
            "use": "lower-bound visible-area calibration",
            "attendance_method": "estimate active participants in visible area; do not infer total attendance without room-specific capacity",
        }
    return {
        "room_family": "breakout track room",
        "camera_model": "fixed speaker/slide camera; audience usually off-axis, with occasional wide shots",
        "coverage": "front rows or side aisles may be visible; full room usually hidden",
        "confidence": confidence,
        "use": use,
        "attendance_method": "count visible rows/heads where available, scale by estimated visible-room fraction, and cap by verified track-room capacity",
    }


def write_wiki(report: dict) -> None:
    lines = [
        "---",
        'title: "Room Attendance Calibration"',
        'category: "resources"',
        'sourceLabels: ["Official conference schedule", "Local video frame sampling", "Attendance calibration"]',
        "---",
        "# Room Attendance Calibration",
        "",
        "This page is a calibration layer for future attendance estimates. It does not publish final attendance counts. It groups scheduled rooms by available video evidence, camera behavior, and the estimation method that should be used for that room.",
        "",
        "## Method",
        "- Use official schedule room labels as canonical room IDs.",
        "- Use local low-resolution video caches and sampled frame caches only as visual evidence.",
        "- Treat visible people counts as lower bounds unless the frame clearly covers the whole audience area.",
        "- Use confidence bands, not exact counts.",
        "",
        "## Calibration Summary",
        "",
    ]
    for room in sorted(report["rooms"]):
        row = report["rooms"][room]
        cal = row["calibration"]
        sheet = f" [contact sheet](/{row['contact_sheet']})" if row.get("contact_sheet") else ""
        lines.append(
            f"- **{room}**: {cal['room_family']}; primary videos {row['primary_videos']}, supporting videos {row['supporting_videos']}, evidence frames {row['evidence_frames']}; use: {cal['use']}; confidence: {cal['confidence']}.{sheet}"
        )
    lines.extend(
        [
            "",
        "## Calibration Table",
        "| Room | Room family | Primary videos | Supporting videos | Evidence frames | Use | Confidence | Contact sheet |",
        "| --- | --- | ---: | ---: | ---: | --- | --- | --- |",
        ]
    )
    for room in sorted(report["rooms"]):
        row = report["rooms"][room]
        cal = row["calibration"]
        sheet = f"[sheet](/{row['contact_sheet']})" if row.get("contact_sheet") else ""
        lines.append(
            f"| {room} | {cal['room_family']} | {row['primary_videos']} | {row['supporting_videos']} | {row['evidence_frames']} | {cal['use']} | {cal['confidence']} | {sheet} |"
        )
    lines.extend(
        [
            "",
            "## Room Notes",
            "",
        ]
    )
    for room in sorted(report["rooms"]):
        row = report["rooms"][room]
        cal = row["calibration"]
        lines.append(f"### {room}")
        lines.append(f"- Camera model: {cal['camera_model']}")
        lines.append(f"- Coverage: {cal['coverage']}")
        lines.append(f"- Attendance method: {cal['attendance_method']}")
        lines.append("")
    lines.extend(["", "## Evidence Videos", ""])
    for room in sorted(report["rooms"]):
        row = report["rooms"][room]
        lines.append(f"### {room}")
        for video in row["used_videos"]:
            segment = ""
            if video.get("segment_start_seconds") is not None:
                segment = f" at {video['segment_start_seconds']}s"
            lines.append(
                f"- `{video['video_id']}`{segment} — {video['source_kind']}; {video['title']} ({video['talk_page']})"
            )
        if not row["used_videos"]:
            lines.append("- No local visual evidence available yet.")
        lines.append("")
    lines.extend(
        [
            "",
            "## Estimation Bands",
            "- Sparse seated room: many gaps; use visible occupied seats directly where rows are clear.",
            "- Medium seated room: most front/middle rows occupied with visible gaps; scale visible rows by room coverage.",
            "- Dense seated room: rows appear nearly full; cap by verified room seat capacity instead of extrapolating from detections.",
            "- Expo standing crowd: use standing density bands per visible square meter only when floor area is visible; otherwise report a lower bound.",
            "",
            "## Evidence Boundary",
            "The table is derived from sampled video frames and schedule metadata. It should be reviewed before any talk page receives an attendance estimate.",
        ]
    )
    WIKI_PAGE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    room_videos = collect_room_videos()
    report = {"rooms": {}}
    for room, rows in sorted(room_videos.items()):
        selected = sorted(rows, key=score_candidate)[:3]
        room_slug = slugify(room)
        evidence = []
        used = []
        for row in selected:
            video_id = row["video_id"]
            video_path = video_file(video_id)
            frame_dir = FRAME_CACHE / video_id
            out_dir = FRAME_OUT / room_slug / video_id
            samples = []
            if video_path:
                samples = sample_video(video_id, video_path, out_dir, 6, row.get("segment_start_seconds"))
            elif frame_dir.exists():
                samples = sample_frame_cache(video_id, frame_dir, out_dir, 6)
            if samples:
                used.append(row)
                for sample in samples:
                    sample.update(
                        {
                            "video_id": video_id,
                            "title": row["title"],
                            "track": row["track"],
                            "source_kind": row.get("source_kind"),
                        }
                    )
                evidence.extend(samples)
        primary_videos = sum(1 for row in used if row.get("source_kind") in {"worldsfair-livestream-segment", "candidate-session-video"})
        supporting_videos = sum(1 for row in used if row.get("source_kind") == "supporting-related-video")
        sheet = make_sheet(room, evidence)
        report["rooms"][room] = {
            "selected_videos": selected,
            "used_videos": used,
            "videos_used": len(used),
            "primary_videos": primary_videos,
            "supporting_videos": supporting_videos,
            "evidence_frames": len(evidence),
            "evidence": evidence,
            "contact_sheet": sheet,
            "calibration": inferred_calibration(room, len(evidence), primary_videos, supporting_videos),
        }
    OUT.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_wiki(report)
    print(json.dumps({"rooms": len(report["rooms"]), "report": str(REPORT.relative_to(ROOT)), "wiki": str(WIKI_PAGE.relative_to(ROOT))}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
