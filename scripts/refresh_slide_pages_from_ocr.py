#!/usr/bin/env python3
"""Refresh slide markdown OCR blocks from current raw OCR text files."""

from __future__ import annotations

import re
from pathlib import Path

from markdown_blocks import blockquote


ROOT = Path(__file__).resolve().parents[1]
SLIDE_PAGES = ROOT / "wiki" / "slides"
SLIDE_ASSETS = ROOT / "wiki" / "assets" / "slides"
SLIDE_OCR = ROOT / "raw" / "sources" / "slide-ocr"


def upsert_section(path: Path, heading: str, body: str) -> None:
    text = path.read_text()
    block = f"\n## {heading}\n{body.rstrip()}\n"
    pattern = re.compile(rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    if pattern.search(text):
        text = pattern.sub(lambda _match: block, text)
    else:
        text = text.rstrip() + block
    path.write_text(text.rstrip() + "\n")


def refresh_page(page: Path) -> bool:
    match = re.match(r"youtube-(.+)-slides\.md$", page.name)
    if not match or page.name.endswith("-reconstructed-slides.md"):
        return False
    video_id = match.group(1)
    image_dir = SLIDE_ASSETS / video_id
    if not image_dir.exists():
        return False
    lines = []
    slides = sorted(image_dir.glob("*.jpg"))
    if not slides:
        lines.append("No slide-like frames were extracted in this run.")
    for slide in slides:
        rel = slide.relative_to(ROOT / "wiki")
        lines.append(f"![[{rel.as_posix()}]]")
        ocr_path = SLIDE_OCR / video_id / f"{slide.stem}.txt"
        text = ocr_path.read_text(errors="ignore").strip() if ocr_path.exists() else ""
        if text:
            lines.extend(["", "OCR text:", "", blockquote(text), ""])
    upsert_section(page, "Extracted Slides", "\n".join(lines))
    return True


def main() -> int:
    count = 0
    for page in sorted(SLIDE_PAGES.glob("youtube-*-slides.md")):
        if refresh_page(page):
            count += 1
    print(f"refreshed {count} slide pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
