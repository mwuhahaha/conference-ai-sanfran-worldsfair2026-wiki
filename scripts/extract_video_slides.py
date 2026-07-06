#!/usr/bin/env python3
"""Extract slide-like frames from related AI Engineer YouTube videos.

The script downloads a low-resolution copy of each related video, samples frames,
deduplicates visually similar frames, writes images under wiki/assets/slides/,
creates wiki/slides/*.md pages, and links those slide pages from related resources
and talks.
"""

from __future__ import annotations

import argparse
import os
import json
import re
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageStat


ROOT = Path(__file__).resolve().parents[1]
VIDEO_CACHE = ROOT / "raw" / "video-cache"
FRAME_TMP = ROOT / "raw" / "slide-frames-tmp"
SLIDE_ASSETS = ROOT / "wiki" / "assets" / "slides"
SLIDE_PAGES = ROOT / "wiki" / "slides"
SLIDE_OCR = ROOT / "raw" / "sources" / "slide-ocr"
WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9'._/-]{2,}")


def run(cmd: list[str], *, timeout: int | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=timeout)


def run_ocr(cmd: list[str], *, timeout: int | None = None) -> subprocess.CompletedProcess:
    env = os.environ.copy()
    local_root = ROOT / ".local" / "ocr" / "root"
    if (local_root / "usr" / "bin" / "tesseract").exists():
        lib_path = str(local_root / "usr" / "lib" / "x86_64-linux-gnu")
        env["LD_LIBRARY_PATH"] = lib_path + (":" + env["LD_LIBRARY_PATH"] if env.get("LD_LIBRARY_PATH") else "")
        env["TESSDATA_PREFIX"] = str(local_root / "usr" / "share" / "tesseract-ocr" / "4.00" / "tessdata")
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=timeout, env=env)


def load_json(path: Path):
    return json.loads(path.read_text())


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-") or "untitled"


def frontmatter(fields: dict) -> str:
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, list):
            lines.append(f"{key}: [{', '.join(json.dumps(str(v), ensure_ascii=False) for v in value)}]")
        elif value is not None:
            lines.append(f"{key}: {json.dumps(str(value), ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def md_label(value: str) -> str:
    return str(value or "").replace("[", "(").replace("]", ")").replace("|", "/")


def resolve_tesseract() -> str | None:
    local = ROOT / ".local" / "ocr" / "root" / "usr" / "bin" / "tesseract"
    if local.exists():
        return str(local)
    return shutil.which("tesseract")


def video_ids_from_map() -> list[str]:
    rows = load_json(ROOT / "raw" / "sources" / "speaker-video-map.json")
    seen: list[str] = []
    for row in rows:
        video_id = (row.get("related_video") or {}).get("video_id")
        if video_id and video_id not in seen:
            seen.append(video_id)
    return seen


def yt_dlp_js_runtime_arg() -> str:
    node = shutil.which("node")
    if not node:
        for candidate in sorted(Path("/home/dylan/.nvm/versions/node").glob("*/bin/node"), reverse=True):
            if candidate.exists():
                node = str(candidate)
                break
    return f"node:{node}" if node else "node"


def video_metadata_by_id() -> dict[str, dict]:
    rows = load_json(ROOT / "raw" / "sources" / "speaker-video-map.json")
    videos = {}
    for row in rows:
        video = row.get("related_video") or {}
        video_id = video.get("video_id")
        if video_id:
            videos.setdefault(video_id, video)
    for source_path in [
        ROOT / "raw" / "sources" / "new-video-discovery-2026-07-06.json",
        ROOT / "raw" / "sources" / "aidotengineer-channel-streams-latest.json",
        ROOT / "raw" / "sources" / "aidotengineer-channel-videos-latest.json",
    ]:
        if not source_path.exists():
            continue
        payload = load_json(source_path)
        entries = []
        entries.extend(payload.get("new_cut_videos") or [])
        entries.extend(payload.get("new_wf26_streams") or [])
        entries.extend(payload.get("entries") or [])
        for entry in entries:
            video_id = entry.get("id")
            if not video_id:
                continue
            videos.setdefault(
                video_id,
                {
                    "video_id": video_id,
                    "youtube_title": entry.get("title") or video_id,
                    "youtube_url": entry.get("url") or f"https://www.youtube.com/watch?v={video_id}",
                    "duration": entry.get("duration"),
                    "source_kind": "channel_stream" if "streams" in source_path.name else "channel_video",
                },
            )
    return videos


def related_sessions_by_video() -> dict[str, list[dict]]:
    rows = load_json(ROOT / "raw" / "sources" / "speaker-video-map.json")
    grouped: dict[str, list[dict]] = {}
    for row in rows:
        video = row.get("related_video") or {}
        video_id = video.get("video_id")
        if video_id:
            grouped.setdefault(video_id, []).append(row)
    return grouped


def download_video(video_id: str) -> Path:
    VIDEO_CACHE.mkdir(parents=True, exist_ok=True)
    output = VIDEO_CACHE / f"{video_id}.mp4"
    if output.exists() and output.stat().st_size > 1024 * 1024:
        return output
    url = f"https://www.youtube.com/watch?v={video_id}"
    cmd = [
        "yt-dlp",
        "--js-runtimes",
        yt_dlp_js_runtime_arg(),
        "--remote-components",
        "ejs:github",
        "-f",
        "bv*[height<=480][ext=mp4]+ba[ext=m4a]/b[height<=480][ext=mp4]/b[height<=480]/worst",
        "--merge-output-format",
        "mp4",
        "-o",
        str(output),
        url,
    ]
    cp = run(cmd, timeout=900)
    if cp.returncode != 0:
        raise RuntimeError(f"yt-dlp failed for {video_id}: {cp.stderr[-2000:]}")
    return output


def sample_frames(video_path: Path, video_id: str, interval: int, timeout: int = 3600) -> Path:
    frame_dir = FRAME_TMP / video_id
    if frame_dir.exists():
        for old in frame_dir.glob("*.jpg"):
            old.unlink()
    frame_dir.mkdir(parents=True, exist_ok=True)
    pattern = frame_dir / "frame-%05d.jpg"
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(video_path),
        "-vf",
        f"fps=1/{interval},scale=960:-1",
        "-q:v",
        "3",
        str(pattern),
    ]
    cp = run(cmd, timeout=timeout)
    if cp.returncode != 0:
        raise RuntimeError(f"ffmpeg failed for {video_path}: {cp.stderr[-2000:]}")
    return frame_dir


def average_hash(path: Path, size: int = 8) -> int:
    image = Image.open(path).convert("L").resize((size, size))
    pixels = list(image.getdata())
    avg = sum(pixels) / len(pixels)
    bits = 0
    for pixel in pixels:
        bits = (bits << 1) | int(pixel > avg)
    return bits


def hamming(left: int, right: int) -> int:
    return (left ^ right).bit_count()


def is_low_information(path: Path) -> bool:
    image = Image.open(path).convert("L").resize((128, 72))
    stat = ImageStat.Stat(image)
    mean = stat.mean[0]
    stddev = stat.stddev[0]
    return mean < 8 or mean > 248 or stddev < 4


def select_slides(frame_dir: Path, video_id: str, max_slides: int) -> list[Path]:
    out_dir = SLIDE_ASSETS / video_id
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("*.jpg"):
        old.unlink()
    selected: list[Path] = []
    selected_hashes: list[int] = []
    for frame in sorted(frame_dir.glob("*.jpg")):
        if is_low_information(frame):
            continue
        ahash = average_hash(frame)
        if any(hamming(ahash, previous) <= 7 for previous in selected_hashes[-12:]):
            continue
        selected_hashes.append(ahash)
        output = out_dir / f"slide-{len(selected) + 1:03d}.jpg"
        Image.open(frame).save(output, "JPEG", quality=88, optimize=True)
        selected.append(output)
        if len(selected) >= max_slides:
            break
    return selected


def preprocess_for_ocr(slide: Path) -> Path:
    out_dir = SLIDE_OCR / "_preprocessed"
    out_dir.mkdir(parents=True, exist_ok=True)
    output = out_dir / slide.name
    image = Image.open(slide).convert("L")
    width, height = image.size
    image = image.resize((width * 2, height * 2))
    image = image.point(lambda p: 255 if p > 170 else 0)
    image.save(output)
    return output


def ocr_words(text: str) -> list[str]:
    return WORD_RE.findall(text or "")


def weak_ocr_text(text: str) -> bool:
    found = ocr_words(text)
    alpha = sum(ch.isalpha() for ch in text)
    return not text.strip() or len(found) < 8 or (len(text) < 80 and len(found) < 12) or (alpha < 35 and len(found) < 10)


def rapidocr_text(slide: Path) -> str:
    try:
        from rapidocr_onnxruntime import RapidOCR
    except Exception:
        return ""
    if not hasattr(rapidocr_text, "_engine"):
        rapidocr_text._engine = RapidOCR()  # type: ignore[attr-defined]
    result, _elapsed = rapidocr_text._engine(str(slide))  # type: ignore[attr-defined]
    if not result:
        return ""
    lines = []
    for item in result:
        text = re.sub(r"[ \t]+", " ", str(item[1] or "")).strip()
        try:
            confidence = float(item[2])
        except Exception:
            confidence = 0.0
        if confidence < 0.45:
            continue
        if not any("A" <= ch <= "Z" or "a" <= ch <= "z" for ch in text):
            continue
        if text:
            lines.append(text)
    return "\n".join(lines).strip()


def materially_better_ocr(original: str, candidate: str) -> bool:
    original_words = len(ocr_words(original))
    candidate_words = len(ocr_words(candidate))
    return (original_words < 3 and candidate_words >= 3) or candidate_words >= original_words + 4 or (
        len(candidate) >= len(original) + 60 and candidate_words >= original_words + 2
    )


def ocr_slides(video_id: str, slides: list[Path]) -> dict[str, str]:
    tesseract = resolve_tesseract()
    out_dir = SLIDE_OCR / video_id
    out_dir.mkdir(parents=True, exist_ok=True)
    results = {}
    if not tesseract:
        return results
    for slide in slides:
        target = out_dir / f"{slide.stem}.txt"
        if target.exists():
            text = target.read_text(errors="ignore").strip()
            results[slide.name] = text
            continue
        prepared = preprocess_for_ocr(slide)
        cp = run_ocr([tesseract, str(prepared), "stdout", "-l", "eng", "--psm", "6"], timeout=60)
        text = (cp.stdout or "").strip()
        # Retry with sparse text mode for stage frames where the projected slide is only part of the image.
        if len(text) < 20:
            cp = run_ocr([tesseract, str(prepared), "stdout", "-l", "eng", "--psm", "11"], timeout=60)
            text = (cp.stdout or "").strip()
        if weak_ocr_text(text):
            better_text = rapidocr_text(slide)
            if better_text and materially_better_ocr(text, better_text):
                text = better_text
        target.write_text(text + ("\n" if text else ""))
        results[slide.name] = text
    return results


def talk_slug(session: dict) -> str:
    # Match build_worldsfair_wiki.py output when possible by reading talk registry.
    title = session.get("title", "")
    registry = load_json(ROOT / "wiki" / "talks" / "registry.json")
    for item in registry:
        if item.get("title") == title:
            return item["id"]
    return slugify(title)


def write_slide_page(video_id: str, video: dict, sessions: list[dict], slides: list[Path], ocr_text: dict[str, str]) -> Path:
    SLIDE_PAGES.mkdir(parents=True, exist_ok=True)
    page = SLIDE_PAGES / f"youtube-{video_id}-slides.md"
    title = f"Slides: {video.get('youtube_title') or video_id}"
    lines = [
        frontmatter(
            {
                "title": title,
                "category": "slides",
                "video_id": video_id,
                "sourceLabels": ["Public YouTube video frames", "Public YouTube metadata"],
            }
        ),
        f"# {title}",
        "",
        "## Source Video",
        f"[{md_label(video.get('youtube_title'))}]({video.get('youtube_url')})",
        "",
        "## Relationship To World's Fair 2026",
        "These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.",
        "",
        "## Related Scheduled Sessions",
    ]
    if sessions:
        for session in sessions:
            lines.append(f"- [[{talk_slug(session)}]] — {session.get('title')}")
    else:
        lines.append("- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.")
    lines.extend(["", "## Extracted Slides"])
    if not slides:
        lines.append("No slide-like frames were extracted in this run.")
    for slide in slides:
        rel = slide.relative_to(ROOT / "wiki")
        lines.append(f"![[{rel.as_posix()}]]")
        text = ocr_text.get(slide.name, "").strip()
        if text:
            compact = re.sub(r"\n{3,}", "\n\n", text)
            lines.append("")
            lines.append("OCR text:")
            lines.append("")
            lines.append("> " + compact.replace("\n", "\n> "))
            lines.append("")
    lines.extend(
        [
            "",
            "## Slide-Derived Subjects To Review",
            "Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.",
        ]
    )
    write(page, "\n".join(lines))
    return page


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n")


def upsert_section(path: Path, heading: str, body: str) -> None:
    text = path.read_text()
    block = f"\n## {heading}\n{body.rstrip()}\n"
    pattern = re.compile(rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    if pattern.search(text):
        text = pattern.sub(block, text)
    else:
        text = text.rstrip() + block
    path.write_text(text.rstrip() + "\n")


def update_resource_and_talk_pages(video_id: str, sessions: list[dict]) -> None:
    slide_link = f"[[youtube-{video_id}-slides]]"
    resource = ROOT / "wiki" / "resources" / f"youtube-{video_id}.md"
    if resource.exists():
        upsert_section(resource, "Extracted Slides", f"- {slide_link}")
    for session in sessions:
        talk = ROOT / "wiki" / "talks" / f"{talk_slug(session)}.md"
        if talk.exists():
            upsert_section(talk, "Supporting Slides", f"- {slide_link} — extracted from the related public AI Engineer video.")


SUBJECT_RULES = [
    ("agent-evaluations", "Agent Evaluations", ["eval", "judge", "quality", "observability", "trace"]),
    ("agent-memory", "Agent Memory", ["memory", "context", "recall"]),
    ("ai-sandboxes", "AI Sandboxes", ["sandbox", "environment", "container"]),
    ("mcp", "Model Context Protocol", ["mcp", "model context protocol"]),
    ("voice-agents", "Voice Agents", ["voice", "audio", "speech"]),
    ("inference-engineering", "Inference Engineering", ["inference", "gpu", "latency", "serving"]),
    ("agentic-search", "Agentic Search", ["search", "retrieval", "rag", "graphrag"]),
    ("coding-agents", "Coding Agents", ["codex", "coding", "code", "sdlc", "review"]),
    ("agent-security", "Agent Security", ["security", "auth", "permission", "provenance"]),
]


def update_subjects(processed: list[tuple[str, dict, list[dict], list[Path], dict[str, str]]]) -> None:
    topic_dir = ROOT / "wiki" / "topics"
    topic_dir.mkdir(parents=True, exist_ok=True)
    touched = {}
    for video_id, video, sessions, slides, ocr_text in processed:
        haystack = " ".join(
            [video.get("youtube_title", "") or ""]
            + [(s.get("title") or "") + " " + (s.get("description") or "") for s in sessions]
            + list(ocr_text.values())
        ).lower()
        for slug, title, keywords in SUBJECT_RULES:
            if any(keyword in haystack for keyword in keywords):
                touched.setdefault(slug, {"title": title, "items": []})
                touched[slug]["items"].append((video_id, video, sessions, slides, ocr_text))
    for slug, data in touched.items():
        lines = [
            frontmatter({"title": data["title"], "category": "topics", "sourceLabels": ["Slide/video-derived supporting context"]}),
            f"# {data['title']}",
            "",
            "## Why It Matters Here",
            "This subject appears in extracted slide/video context connected to AI Engineer World's Fair 2026 sessions.",
            "",
            "## Related Slide Decks",
        ]
        for video_id, video, sessions, slides, _ocr_text in data["items"]:
            lines.append(f"- [[youtube-{video_id}-slides]] — {md_label(video.get('youtube_title'))} ({len(slides)} extracted slide frames)")
        lines.extend(["", "## Related Scheduled Sessions"])
        seen = set()
        for _video_id, _video, sessions, _slides, _ocr_text in data["items"]:
            for session in sessions:
                slugged = talk_slug(session)
                if slugged not in seen:
                    seen.add(slugged)
                    lines.append(f"- [[{slugged}]] — {session.get('title')}")
        write(topic_dir / f"{slug}.md", "\n".join(lines))


def update_slide_registry(processed: list[tuple[str, dict, list[dict], list[Path]]]) -> None:
    registry = []
    for page in sorted(SLIDE_PAGES.glob("youtube-*-slides.md")):
        text = page.read_text()
        title_match = re.search(r'^title: "?(.*?)"?$', text, re.M)
        registry.append(
            {
                "id": page.stem,
                "title": title_match.group(1) if title_match else page.stem,
                "path": f"wiki/slides/{page.name}",
                "slide_count": len(re.findall(r"!\[\[assets/slides/", text)),
            }
        )
    write(SLIDE_PAGES / "registry.json", json.dumps(registry, indent=2, ensure_ascii=False))


def update_topic_registry() -> None:
    topic_dir = ROOT / "wiki" / "topics"
    registry = []
    for page in sorted(topic_dir.glob("*.md")):
        if page.name == "registry.json":
            continue
        text = page.read_text()
        title_match = re.search(r'^title: "?(.*?)"?$', text, re.M)
        registry.append(
            {
                "id": page.stem,
                "title": title_match.group(1) if title_match else page.stem,
                "path": f"wiki/topics/{page.name}",
            }
        )
    write(topic_dir / "registry.json", json.dumps(registry, indent=2, ensure_ascii=False))


def update_slide_library() -> None:
    rows = json.loads((SLIDE_PAGES / "registry.json").read_text()) if (SLIDE_PAGES / "registry.json").exists() else []
    lines = [
        frontmatter({"title": "Slide Library", "category": "slides", "sourceLabels": ["Public YouTube video frames", "Local OCR"]}),
        "# Slide Library",
        "",
        "This page summarizes extracted slide decks from speaker-matched AI Engineer YouTube videos. OCR is best-effort and should be checked against the embedded slide images.",
        "",
        "## Coverage",
        f"- Slide decks: {len(rows)}",
        f"- Extracted slide/frame images: {len(list(SLIDE_ASSETS.rglob('*.jpg')))}",
        f"- OCR text files: {len(list(SLIDE_OCR.glob('*/*.txt')))}",
        "",
        "## Decks",
    ]
    for row in rows:
        lines.append(f"- [[{row['id']}]] — {row.get('slide_count', 0)} extracted frames")
    lines.extend(["", "## OCR-Derived Subject Signals"])
    subject_hits = []
    for slug, title, keywords in SUBJECT_RULES:
        count = 0
        for path in SLIDE_OCR.glob("*/*.txt"):
            text = path.read_text(errors="ignore").lower()
            if any(keyword in text for keyword in keywords):
                count += 1
        if count:
            subject_hits.append((count, slug, title))
    for count, slug, title in sorted(subject_hits, reverse=True):
        topic_path = ROOT / "wiki" / "topics" / f"{slug}.md"
        if not topic_path.exists():
            write(
                topic_path,
                "\n".join(
                    [
                        frontmatter({"title": title, "category": "topics", "sourceLabels": ["Slide OCR"]}),
                        f"# {title}",
                        "",
                        "## Why It Matters Here",
                        "This subject was detected from OCR text in extracted YouTube slide frames.",
                        "",
                        "## Related Slide Library",
                        "- [[slide-library]]",
                    ]
                ),
            )
        lines.append(f"- [[{slug}]] — OCR keyword signal in {count} slide frames")
    failure_path = ROOT / "raw" / "sources" / "slide-extraction-failures.json"
    if failure_path.exists():
        try:
            failures = json.loads(failure_path.read_text())
        except Exception:
            failures = []
        if failures:
            lines.extend(["", "## Unresolved Video Failures"])
            for failure in failures:
                lines.append(f"- `{failure.get('video_id')}` — {failure.get('title') or 'Untitled'}")
    write(SLIDE_PAGES / "slide-library.md", "\n".join(lines))


def update_project_overview_with_slide_status() -> None:
    path = ROOT / "wiki" / "overview.md"
    if not path.exists():
        return
    deck_count = len(list(SLIDE_PAGES.glob("youtube-*-slides.md")))
    slide_count = len(list(SLIDE_ASSETS.rglob("*.jpg")))
    ocr_count = sum(1 for item in SLIDE_OCR.glob("*/*.txt") if item.read_text(errors="ignore").strip())
    body = "\n".join(
        [
            f"- [[slide-library]] tracks {deck_count} extracted video slide decks.",
            f"- {slide_count} slide/frame images are embedded in deck pages.",
            f"- {ocr_count} extracted frames have non-empty local OCR text.",
            "- OCR is best-effort because most videos are full-stage captures rather than direct slide exports.",
        ]
    )
    upsert_section(path, "Slide/OCR Coverage", body)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0, help="Number of distinct videos to process; 0 means all.")
    parser.add_argument("--start", type=int, default=0, help="Zero-based video offset.")
    parser.add_argument("--interval", type=int, default=20, help="Sample one frame every N seconds.")
    parser.add_argument("--max-slides", type=int, default=36)
    parser.add_argument("--no-ocr", action="store_true")
    parser.add_argument("--video-id", action="append", default=[])
    args = parser.parse_args()

    ids = args.video_id or video_ids_from_map()
    if args.start:
        ids = ids[args.start :]
    if args.limit:
        ids = ids[: args.limit]

    videos = video_metadata_by_id()
    sessions = related_sessions_by_video()
    processed = []
    failures = []
    for index, video_id in enumerate(ids, start=1):
        video = videos.get(video_id, {"video_id": video_id, "youtube_url": f"https://www.youtube.com/watch?v={video_id}"})
        print(f"[{index}/{len(ids)}] {video_id} {video.get('youtube_title', '')}", flush=True)
        try:
            video_path = download_video(video_id)
            frame_dir = sample_frames(video_path, video_id, args.interval)
            slides = select_slides(frame_dir, video_id, args.max_slides)
            ocr_text = {} if args.no_ocr else ocr_slides(video_id, slides)
            write_slide_page(video_id, video, sessions.get(video_id, []), slides, ocr_text)
            update_resource_and_talk_pages(video_id, sessions.get(video_id, []))
            processed.append((video_id, video, sessions.get(video_id, []), slides, ocr_text))
            ocr_count = sum(1 for text in ocr_text.values() if text.strip())
            print(f"  extracted {len(slides)} slide frames; OCR text on {ocr_count}", flush=True)
        except Exception as exc:
            failures.append({"video_id": video_id, "title": video.get("youtube_title", ""), "error": str(exc)})
            print(f"  failed: {exc}", flush=True)

    update_subjects(processed)
    update_slide_registry(processed)
    update_topic_registry()
    update_slide_library()
    update_project_overview_with_slide_status()
    if failures:
        failure_path = ROOT / "raw" / "sources" / "slide-extraction-failures.json"
        existing = []
        if failure_path.exists():
            try:
                existing = json.loads(failure_path.read_text())
            except Exception:
                existing = []
        failure_path.write_text(json.dumps(existing + failures, indent=2, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
