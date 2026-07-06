#!/usr/bin/env python3
"""Dense slide fallback using PySceneDetect scene cuts plus local crop/dedupe."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path

import importlib.util


ROOT = Path(__file__).resolve().parents[1]
VIDEO_CACHE = ROOT / "raw" / "video-cache"
DENSE_ROOT = ROOT / "raw" / "sources" / "dense-scenedetect"
DENSE_ASSETS = ROOT / "wiki" / "assets" / "dense-slides"
DENSE_OCR = ROOT / "raw" / "sources" / "dense-slide-ocr"
CAPTURED_FRAME_ROOT = ROOT / "raw" / "slide-frames-tmp"
SLIDE_PAGES = ROOT / "wiki" / "slides"
AUDIT_PATH = ROOT / "raw" / "sources" / "dense-scenedetect-audit.json"

RECON_SPEC = importlib.util.spec_from_file_location("reconstruct_video_slides", ROOT / "scripts" / "reconstruct_video_slides.py")
recon = importlib.util.module_from_spec(RECON_SPEC)
assert RECON_SPEC.loader
RECON_SPEC.loader.exec_module(recon)

try:
    from rapidocr_onnxruntime import RapidOCR
except Exception:  # pragma: no cover
    RapidOCR = None


TITLE_CARD_RE = re.compile(
    r"\b(presenting\s+sponsor|sponsor|google\s+deepmind|ai\s+engineer|world'?s?\s+fair|aie\b|presented\s+by)\b",
    re.I,
)
SCREEN_SHARE_RE = re.compile(
    r"\b(stop\s*share|shop\s*share|talking:|nyc|central|docs\.google|presentation|gemini|file\s*edit\s*view)\b",
    re.I,
)


def run(cmd: list[str], *, timeout: int | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=timeout)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n")


def image_box(image, box: tuple[int, int, int, int]):
    x, y, w, h = box
    return image.crop((x, y, x + w, y + h))


def slide_text_score(text: str) -> int:
    return len(recon.words(str(text or "")))


def is_title_or_sponsor_card(text: str) -> bool:
    return bool(TITLE_CARD_RE.search(str(text or "")))


def has_screen_share_chrome(text: str) -> bool:
    return bool(SCREEN_SHARE_RE.search(str(text or "")))


def trim_screen_share_chrome(image):
    width, height = image.size
    # Zoom/browser screen-share bars are consistently in the top band. Keep the
    # slide content and discard the conferencing/browser chrome when present.
    top = int(height * 0.07)
    return image.crop((0, top, width, height))


def visual_slide_signal(image_bgr) -> tuple[bool, dict, str]:
    gray = recon.cv2.cvtColor(image_bgr, recon.cv2.COLOR_BGR2GRAY)
    hsv = recon.cv2.cvtColor(image_bgr, recon.cv2.COLOR_BGR2HSV)
    edges = recon.cv2.Canny(gray, 50, 150)
    edge_density = float(recon.np.count_nonzero(edges)) / float(edges.size)
    dark_ratio = float(recon.np.mean(gray < 35))
    bright_ratio = float(recon.np.mean(gray > 210))
    saturated_ratio = float(recon.np.mean(hsv[:, :, 1] > 60))
    bottom = hsv[int(hsv.shape[0] * 0.93) :, :, :]
    left = gray[:, : int(gray.shape[1] * 0.2)]
    center = gray[:, int(gray.shape[1] * 0.2) : int(gray.shape[1] * 0.8)]
    center_narrow = gray[:, int(gray.shape[1] * 0.35) : int(gray.shape[1] * 0.65)]
    bottom_blue_ratio = float(
        recon.np.mean(
            (bottom[:, :, 0] > 85)
            & (bottom[:, :, 0] < 135)
            & (bottom[:, :, 1] > 50)
            & (bottom[:, :, 2] > 50)
        )
    )
    left_bright_ratio = float(recon.np.mean(left > 210))
    center_bright_ratio = float(recon.np.mean(center > 210))
    center_narrow_bright_ratio = float(recon.np.mean(center_narrow > 210))
    features = {
        "edge_density": round(edge_density, 4),
        "dark_ratio": round(dark_ratio, 4),
        "bright_ratio": round(bright_ratio, 4),
        "saturated_ratio": round(saturated_ratio, 4),
        "bottom_blue_ratio": round(bottom_blue_ratio, 4),
        "left_bright_ratio": round(left_bright_ratio, 4),
        "center_bright_ratio": round(center_bright_ratio, 4),
        "center_narrow_bright_ratio": round(center_narrow_bright_ratio, 4),
    }

    if dark_ratio > 0.55:
        return False, features, "rejected-mostly-dark-card"
    if bright_ratio > 0.88 and edge_density < 0.032:
        return False, features, "rejected-mostly-blank-screen"
    if bright_ratio > 0.65 and 0.18 < bottom_blue_ratio < 0.55:
        return False, features, "rejected-browser-editor-demo"
    if bottom_blue_ratio > 0.18 and bright_ratio < 0.45 and saturated_ratio < 0.12:
        return False, features, "rejected-document-viewer-demo"
    if 0.25 < bright_ratio < 0.5 and saturated_ratio < 0.08 and edge_density < 0.035:
        return False, features, "rejected-document-viewer-demo"
    if saturated_ratio < 0.08 and left_bright_ratio < 0.12 and center_narrow_bright_ratio > 0.7:
        return False, features, "rejected-document-viewer-demo"
    if left_bright_ratio > 0.75 and center_bright_ratio < 0.45 and edge_density > 0.07:
        return False, features, "rejected-slide-editor-view"
    if bright_ratio > 0.34 and edge_density > 0.025:
        return True, features, "visual-bright-slide"
    if saturated_ratio > 0.75 and dark_ratio < 0.12 and edge_density > 0.04:
        return True, features, "visual-dark-theme-slide"
    if edge_density > 0.09 and bright_ratio > 0.45:
        return True, features, "visual-dense-code-or-document-slide"
    return False, features, "rejected-no-clear-slide-surface"


def strict_visible_slide_crop(scene_image: Path, ocr) -> tuple[object | None, dict | None, str, float, str]:
    source = recon.Image.open(scene_image).convert("RGB")
    width, height = source.size
    image_bgr = recon.cv2.imread(str(scene_image))
    if image_bgr is None:
        return None, None, "", 0.0, "rejected-unreadable-frame"
    visual_ok, visual_features, visual_reason = visual_slide_signal(image_bgr)
    if not visual_ok:
        return None, None, "", 0.0, visual_reason

    best_kind, best_box, best_score = recon.candidate_boxes(image_bgr)[0]
    meta = {
        "source": scene_image.name,
        "kind": best_kind,
        "box": list(best_box),
        "score": round(float(best_score), 2),
        "visual_features": visual_features,
    }

    selected = trim_screen_share_chrome(source)
    selected_meta = {
        **meta,
        "kind": "visible-slide-crop",
        "box": [0, int(height * 0.07), width, height - int(height * 0.07)],
        "strict_reason": visual_reason,
    }
    selected_text, selected_confidence = recon.rapid_ocr_image(ocr, selected) if ocr else ("", 0.0)
    if selected_text and is_title_or_sponsor_card(selected_text):
        return None, None, selected_text, selected_confidence, "rejected-title-or-sponsor-card"
    if ocr and selected_text and slide_text_score(selected_text) < 4:
        return None, None, selected_text, selected_confidence, "rejected-no-visible-slide-text"
    selected_meta = {
        **selected_meta,
        "screen_share_chrome": has_screen_share_chrome(selected_text),
    }
    return selected, selected_meta, selected_text, selected_confidence, "accepted"


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


def video_metadata_by_id() -> dict[str, dict]:
    return recon.video_metadata_by_id()


def ensure_h264_proxy(video_id: str) -> Path:
    source = VIDEO_CACHE / f"{video_id}.mp4"
    if not source.exists():
        raise RuntimeError(f"missing cached video: {source}")
    proxy = DENSE_ROOT / video_id / f"{video_id}-h264.mp4"
    if proxy.exists() and proxy.stat().st_size > 1024 * 1024:
        return proxy
    proxy.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-i",
        str(source),
        "-an",
        "-vf",
        "scale=960:-2",
        "-c:v",
        "libx264",
        "-preset",
        "ultrafast",
        "-crf",
        "28",
        str(proxy),
    ]
    cp = run(cmd, timeout=1800)
    if cp.returncode != 0:
        raise RuntimeError(f"ffmpeg proxy failed for {video_id}: {cp.stderr[-2000:]}")
    return proxy


def run_scenedetect(video_id: str, proxy: Path, *, threshold: float) -> Path:
    out_dir = DENSE_ROOT / video_id / "scene-images"
    if out_dir.exists():
        for old in out_dir.glob("*"):
            if old.is_file():
                old.unlink()
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "scenedetect",
        "-i",
        str(proxy),
        "-o",
        str(out_dir),
        "detect-content",
        "--threshold",
        str(threshold),
        "list-scenes",
        "save-images",
        "--num-images",
        "1",
        "--jpeg",
        "--filename",
        "scene-$SCENE_NUMBER-frame-$FRAME_NUMBER",
    ]
    cp = run(cmd, timeout=1800)
    if cp.returncode != 0:
        raise RuntimeError(f"scenedetect failed for {video_id}: {cp.stderr[-2000:]}")
    return out_dir


def dense_filter(video_id: str, scene_dir: Path, *, max_slides: int, use_ocr: bool, slide_only: bool, source_mode: str) -> dict:
    out_dir = DENSE_ASSETS / video_id
    ocr_dir = DENSE_OCR / video_id
    out_dir.mkdir(parents=True, exist_ok=True)
    ocr_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("*.jpg"):
        old.unlink()
    for old in ocr_dir.glob("*.txt"):
        old.unlink()

    ocr = RapidOCR() if use_ocr and RapidOCR is not None else None
    hashes: list[int] = []
    selected = []
    rejected = []
    frame_paths = sorted(scene_dir.glob("*.jpg"))
    for scene_image in frame_paths:
        if slide_only:
            crop, meta, text, confidence, disposition = strict_visible_slide_crop(scene_image, ocr)
            if crop is None or meta is None:
                rejected.append({"source": scene_image.name, "reason": disposition, "ocr_text": text})
                continue
        else:
            crop, meta, text, confidence = recon.crop_slide_region(scene_image, ocr=ocr, ocr_select=bool(ocr), ocr_select_candidates=2)
        ahash = recon.average_hash(crop)
        if any(recon.hamming(ahash, previous) <= 6 for previous in hashes[-24:]):
            continue
        if text and selected:
            prev_words = set(recon.words(str(selected[-1].get("ocr_text", "")).lower()))
            now_words = set(recon.words(text.lower()))
            if prev_words and now_words and len(prev_words & now_words) / max(len(prev_words | now_words), 1) > 0.88:
                continue
        output = out_dir / f"slide-{len(selected) + 1:03d}.jpg"
        crop.save(output, "JPEG", quality=90, optimize=True)
        if text:
            write(ocr_dir / f"{output.stem}.txt", text)
        hashes.append(ahash)
        selected.append({**meta, "output": output.name, "ocr_text": text, "ocr_confidence": round(float(confidence), 4)})
        if len(selected) >= max_slides:
            break
    return {
        "video_id": video_id,
        "scene_images": len(frame_paths),
        "slides": selected,
        "rejected": rejected,
        "slide_only": slide_only,
        "ocr_enabled": bool(ocr),
        "source_mode": source_mode,
    }


def write_dense_page(video_id: str, video: dict, result: dict) -> Path:
    page = SLIDE_PAGES / f"youtube-{video_id}-dense-slides.md"
    title = f"Dense Slides: {video.get('youtube_title') or video_id}"
    source_labels = ["Local OpenCV slide-region detection"]
    if result.get("source_mode") == "scenedetect":
        source_labels.insert(0, "PySceneDetect scene detection")
    else:
        source_labels.insert(0, "Captured video frames")
    if result.get("ocr_enabled"):
        source_labels.append("Local RapidOCR")
    source_sentence = "PySceneDetect finds visual scene changes from the cached video" if result.get("source_mode") == "scenedetect" else "The existing captured video frame set supplies candidate frames"
    method = f"This deck is slide-only. {source_sentence}, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images."
    if result.get("ocr_enabled"):
        method = f"This deck is slide-only. {source_sentence}, then local OpenCV/RapidOCR rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and OCRs the cropped slide images."
    lines = [
        frontmatter(
            {
                "title": title,
                "category": "slides",
                "video_id": video_id,
                "sourceLabels": source_labels,
            }
        ),
        f"# {title}",
        "",
        "## Source Video",
        f"[{md_label(video.get('youtube_title') or video_id)}]({video.get('youtube_url') or f'https://www.youtube.com/watch?v={video_id}'})",
        "",
        "## Method",
        method,
        "",
        "## Cropped Visible Slides",
    ]
    for item in result["slides"]:
        image_path = f"assets/dense-slides/{video_id}/{item['output']}"
        lines.append(f"![[{image_path}]]")
        lines.append("")
        lines.append(f"- Source scene image: `{item['source']}`")
        lines.append(f"- Crop: `{item['kind']}` `{item['box']}` score `{item['score']}`")
        if item.get("strict_reason"):
            lines.append(f"- Slide-only rule: `{item['strict_reason']}`")
        text = (item.get("ocr_text") or "").strip()
        if text:
            lines.extend(["", "OCR text:", "", "> " + text.replace("\n", "\n> "), ""])
    write(page, "\n".join(lines))
    return page


def remove_dense_page(video_id: str) -> None:
    page = SLIDE_PAGES / f"youtube-{video_id}-dense-slides.md"
    if page.exists():
        page.unlink()


def update_registry() -> None:
    rows = []
    for page in sorted(SLIDE_PAGES.glob("youtube-*-dense-slides.md")):
        text = page.read_text()
        title_match = re.search(r'^title: "?(.*?)"?$', text, re.M)
        rows.append(
            {
                "id": page.stem,
                "title": title_match.group(1) if title_match else page.stem,
                "path": f"wiki/slides/{page.name}",
                "slide_count": len(re.findall(r"!\[\[assets/dense-slides/", text)),
            }
        )
    write(SLIDE_PAGES / "dense-registry.json", json.dumps(rows, indent=2, ensure_ascii=False))


def update_dense_library() -> None:
    registry_path = SLIDE_PAGES / "dense-registry.json"
    rows = json.loads(registry_path.read_text()) if registry_path.exists() else []
    lines = [
        frontmatter({"title": "Dense Slide Library", "category": "slides", "sourceLabels": ["Captured video frames", "Local OpenCV slide-region detection"]}),
        "# Dense Slide Library",
        "",
        "This indexes slide-only cropped decks produced from captured video frames. Use these when the wiki needs actual visible slide images rather than speaker shots, title cards, or demo/browser frames.",
        "",
        "## Coverage",
        f"- Dense decks: {len(rows)}",
        f"- Dense slide images: {len(list(DENSE_ASSETS.rglob('*.jpg')))}",
        "",
        "## Decks",
    ]
    for row in rows:
        count = row.get("slide_count", 0)
        lines.append(f"- [[{row['id']}]] — {count} slide-only {'image' if count == 1 else 'images'}")
    write(SLIDE_PAGES / "dense-slide-library.md", "\n".join(lines))


def upsert_section(path: Path, heading: str, body: str) -> None:
    if not path.exists():
        return
    text = path.read_text()
    block = f"\n## {heading}\n{body.rstrip()}\n"
    pattern = re.compile(rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    if pattern.search(text):
        text = pattern.sub(lambda _m: block, text)
    else:
        text = text.rstrip() + block
    write(path, text)


def update_original_pages(video_id: str) -> None:
    link = f"[[youtube-{video_id}-dense-slides]]"
    for page in [
        SLIDE_PAGES / f"youtube-{video_id}-slides.md",
        SLIDE_PAGES / f"youtube-{video_id}-reconstructed-slides.md",
    ]:
        upsert_section(page, "Dense Scene-Detected Slide Candidates", f"- {link}")


def remove_original_page_dense_links(video_id: str) -> None:
    link = f"[[youtube-{video_id}-dense-slides]]"
    for page in [
        SLIDE_PAGES / f"youtube-{video_id}-slides.md",
        SLIDE_PAGES / f"youtube-{video_id}-reconstructed-slides.md",
    ]:
        if not page.exists():
            continue
        text = page.read_text()
        next_text = text.replace(f"\n## Dense Scene-Detected Slide Candidates\n- {link}\n", "\n")
        next_text = next_text.replace(f"\n## Dense Scene-Detected Slide Candidates\n- {link}", "\n")
        if next_text != text:
            write(page, next_text)


def update_audit(result: dict) -> None:
    payload = {"videos": []}
    if AUDIT_PATH.exists():
        try:
            payload = json.loads(AUDIT_PATH.read_text())
        except Exception:
            payload = {"videos": []}
    payload["videos"] = [item for item in payload.get("videos", []) if item.get("video_id") != result["video_id"]]
    payload["videos"].append(result)
    payload["videoCount"] = len(payload["videos"])
    write(AUDIT_PATH, json.dumps(payload, indent=2, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--video-id", action="append", default=[])
    parser.add_argument("--all-cached", action="store_true")
    parser.add_argument("--threshold", type=float, default=18.0)
    parser.add_argument("--max-slides", type=int, default=80)
    parser.add_argument("--no-ocr", action="store_true")
    parser.add_argument("--include-non-slide-candidates", action="store_true")
    parser.add_argument("--reuse-scenes", action="store_true")
    parser.add_argument("--use-captured-frames", action="store_true")
    args = parser.parse_args()

    videos = video_metadata_by_id()
    ids = args.video_id
    if args.all_cached:
        ids = sorted({path.stem for path in VIDEO_CACHE.glob("*.mp4")})
    if not ids:
        raise SystemExit("pass at least one --video-id or --all-cached")
    if not shutil.which("scenedetect"):
        raise SystemExit("scenedetect is not installed")

    for video_id in ids:
        print(f"dense scan {video_id}", flush=True)
        if args.use_captured_frames:
            scene_dir = CAPTURED_FRAME_ROOT / video_id
            if not scene_dir.exists():
                raise RuntimeError(f"missing captured frame directory: {scene_dir}")
            source_mode = "captured-frames"
        else:
            proxy = ensure_h264_proxy(video_id)
            scene_dir = DENSE_ROOT / video_id / "scene-images"
            if not (args.reuse_scenes and scene_dir.exists() and list(scene_dir.glob("scene-*.jpg"))):
                scene_dir = run_scenedetect(video_id, proxy, threshold=args.threshold)
            source_mode = "scenedetect"
        result = dense_filter(
            video_id,
            scene_dir,
            max_slides=args.max_slides,
            use_ocr=not args.no_ocr,
            slide_only=not args.include_non_slide_candidates,
            source_mode=source_mode,
        )
        if result["slides"]:
            write_dense_page(video_id, videos.get(video_id, {"video_id": video_id}), result)
            update_original_pages(video_id)
        else:
            remove_dense_page(video_id)
            remove_original_page_dense_links(video_id)
        update_audit(result)
        print(
            f"  scene images: {result['scene_images']}; slide-only crops: {len(result['slides'])}; rejected: {len(result.get('rejected', []))}",
            flush=True,
        )
    update_registry()
    update_dense_library()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
