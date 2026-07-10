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
from statistics import median
from collections import defaultdict
from pathlib import Path

import cv2
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
VIDEO_REPORT = OUT / "video-attendance-evidence.json"
VIDEO_OVERRIDES = OUT / "video-attendance-overrides.json"
WIKI_PAGE = WIKI / "resources" / "room-attendance-calibration.md"
VIDEO_WIKI_PAGE = WIKI / "resources" / "video-attendance-visibility.md"
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


def evidence_key(row: dict) -> str:
    segment = row.get("segment_start_seconds")
    if segment is None:
        return f"{row['video_id']}-full"
    return f"{row['video_id']}-t{segment}"


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
        label = f"{item.get('evidence_key', item['video_id'])} {item.get('time_seconds') or ''}"
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


def local_people_detector_count(path: Path) -> int:
    """Best-effort visible-person signal, not a publishable attendance count."""
    image = cv2.imread(str(path))
    if image is None:
        return 0
    height, width = image.shape[:2]
    scale = min(1.0, 960 / max(width, height))
    if scale < 1.0:
        image = cv2.resize(image, (int(width * scale), int(height * scale)))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_count = 0
    cascade_path = Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml"
    if cascade_path.exists():
        cascade = cv2.CascadeClassifier(str(cascade_path))
        faces = cascade.detectMultiScale(gray, scaleFactor=1.08, minNeighbors=5, minSize=(18, 18))
        face_count = len(faces)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    bodies, _ = hog.detectMultiScale(image, winStride=(8, 8), padding=(8, 8), scale=1.05)
    return max(face_count, len(bodies))


def icon_scale(count: int) -> int:
    if count <= 0:
        return 0
    return min(10, max(1, math.ceil(count / 5)))


def icon_string(count: int) -> str:
    return " ".join(["👤"] * count)


def load_video_overrides() -> dict:
    if not VIDEO_OVERRIDES.exists():
        return {}
    try:
        data = json.loads(VIDEO_OVERRIDES.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return data.get("videos", {}) if isinstance(data, dict) else {}


def build_video_attendance_report(room_report: dict) -> dict:
    videos: dict[str, dict] = {}
    overrides = load_video_overrides()
    for room, row in sorted(room_report["rooms"].items()):
        calibration = row["calibration"]
        evidence_by_key: dict[str, list[dict]] = defaultdict(list)
        for item in row["evidence"]:
            evidence_by_key[item.get("evidence_key", item["video_id"])].append(item)
        for video in row["used_videos"]:
            key = evidence_key(video)
            samples = evidence_by_key.get(key, [])
            detector_counts = []
            for sample in samples:
                frame_path = ROOT / sample["path"]
                if frame_path.exists():
                    detector_counts.append(local_people_detector_count(frame_path))
            max_count = max(detector_counts or [0])
            median_count = int(median(detector_counts)) if detector_counts else 0
            primary = video.get("source_kind") in {"worldsfair-livestream-segment", "candidate-session-video"}
            automated_candidate = (
                primary
                and calibration["use"] == "partial visible-area calibration"
                and max_count >= 8
                and sum(1 for count in detector_counts if count >= 5) >= 2
            )
            override = overrides.get(key, {})
            override_icons = int(override.get("display_icons") or 0) if isinstance(override, dict) else 0
            high_confidence = bool(override.get("publish") and 1 <= override_icons <= 10) if isinstance(override, dict) else False
            display_icons = override_icons if high_confidence else 0
            videos[key] = {
                "video_id": video["video_id"],
                "segment_start_seconds": video.get("segment_start_seconds"),
                "source_kind": video.get("source_kind"),
                "room": room,
                "track": video.get("track", ""),
                "title": video.get("title", ""),
                "talk_page": video.get("talk_page", ""),
                "sample_frames": len(samples),
                "detector_counts": detector_counts,
                "max_visible_signal": max_count,
                "median_visible_signal": median_count,
                "automated_candidate": automated_candidate,
                "confidence": "high" if high_confidence else "needs_review" if automated_candidate else "low",
                "display_icons": display_icons,
                "display": icon_string(display_icons) if display_icons else "",
                "publishable": bool(display_icons),
                "reason": (
                    "Published from explicit high-confidence review override as a capped icon-scale visible attendance signal."
                    if display_icons
                    else "No number shown because confidence is low, the automated signal still needs review, no people were confidently detected, or the visual evidence is only a room/camera proxy."
                ),
            }
    return {"videos": videos}


def upsert_section(text: str, heading: str, body: str) -> str:
    pattern = re.compile(rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    section = f"\n## {heading}\n{body.rstrip()}\n"
    if pattern.search(text):
        return pattern.sub(section, text)
    return text.rstrip() + "\n" + section


def write_video_wiki(video_report: dict) -> None:
    published = [row for row in video_report["videos"].values() if row["publishable"]]
    suppressed = [row for row in video_report["videos"].values() if not row["publishable"]]
    lines = [
        "---",
        'title: "Video Attendance Visibility"',
        'category: "resources"',
        'sourceLabels: ["Local video frame sampling", "Attendance calibration", "OpenCV visual signal"]',
        "---",
        "# Video Attendance Visibility",
        "",
        "This page records the conservative video-level attendance visibility pass. It is not an exact attendance count. A number is shown only when the visual signal is high confidence; zero and low-confidence estimates are suppressed.",
        "",
        "## Display Rule",
        "- Do not show a number when the estimate is zero.",
        "- Do not show a number when confidence is low or the source is only a supporting/camera-family proxy.",
        "- When confidence is high, show a capped icon scale from 1 to 10 person icons.",
        "- Automated detector output may nominate a candidate, but publication requires explicit high-confidence review.",
        "- The icon scale is a visible-attendance signal, not a precise count.",
        "",
        "## Published Icon Signals",
        "",
    ]
    if published:
        for row in sorted(published, key=lambda item: (item["room"], item["title"])):
            lines.append(f"- {row['display']} — {row['title']} (`{row['video_id']}`), {row['room']}; confidence: high.")
    else:
        lines.append("- No high-confidence video attendance icon signals are publishable in this pass.")
    lines.extend(["", "## Suppressed Video Signals", ""])
    for row in sorted(suppressed, key=lambda item: (item["room"], item["title"], item["video_id"])):
        segment = f" at {row['segment_start_seconds']}s" if row.get("segment_start_seconds") is not None else ""
        candidate = "; automated candidate awaiting review" if row.get("automated_candidate") else ""
        lines.append(
            f"- `{row['video_id']}`{segment} — {row['title']} ({row['room']}): suppressed; max local visible-person signal {row['max_visible_signal']}; confidence {row['confidence']}{candidate}."
        )
    lines.extend(
        [
            "",
            "## Method Boundary",
            "The local detector produces a review signal from sampled frames. It can miss people in dark rooms, count speakers instead of audience, and fail on slide-only captures. For that reason, only high-confidence results are displayed on talk pages.",
        ]
    )
    VIDEO_WIKI_PAGE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def apply_talk_attendance_sections(video_report: dict) -> None:
    by_talk: dict[str, list[dict]] = defaultdict(list)
    for row in video_report["videos"].values():
        if row.get("talk_page"):
            by_talk[row["talk_page"]].append(row)
    for rel_path, rows in by_talk.items():
        path = ROOT / rel_path
        if not path.exists():
            continue
        published = [row for row in rows if row["publishable"]]
        if not published:
            body = (
                "No high-confidence attendance icon signal is shown for this talk. "
                "The sampled video evidence was either low confidence, source-proxy-only, or did not expose a clear audience view."
            )
        else:
            body_lines = [
                "Visible attendance signal is shown as a capped 1-10 person-icon scale, not an exact count.",
                "",
            ]
            for row in published:
                body_lines.append(f"- {row['display']} — high confidence from `{row['video_id']}` sampled frames.")
            body = "\n".join(body_lines)
        text = path.read_text(encoding="utf-8")
        updated = upsert_section(text, "Attendance Visibility", body)
        if updated != text:
            path.write_text(updated, encoding="utf-8")


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
            key = evidence_key(row)
            out_dir = FRAME_OUT / room_slug / key
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
                            "evidence_key": key,
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
    video_report = build_video_attendance_report(report)
    VIDEO_REPORT.write_text(json.dumps(video_report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_video_wiki(video_report)
    apply_talk_attendance_sections(video_report)
    print(
        json.dumps(
            {
                "rooms": len(report["rooms"]),
                "room_report": str(REPORT.relative_to(ROOT)),
                "video_report": str(VIDEO_REPORT.relative_to(ROOT)),
                "room_wiki": str(WIKI_PAGE.relative_to(ROOT)),
                "video_wiki": str(VIDEO_WIKI_PAGE.relative_to(ROOT)),
                "published_video_icons": sum(1 for row in video_report["videos"].values() if row["publishable"]),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
