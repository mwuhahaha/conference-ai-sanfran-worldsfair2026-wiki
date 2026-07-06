#!/usr/bin/env python3
"""Link slide-only dense decks into talk/resource pages and surface OCR terms."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
SLIDES = WIKI / "slides"
TALKS = WIKI / "talks"
RESOURCES = WIKI / "resources"
SPEAKER_MAP = ROOT / "raw" / "sources" / "speaker-video-map.json"

STOP_WORDS = {
    "about", "after", "agent", "agents", "also", "because", "before", "being", "build", "building",
    "can", "could", "data", "does", "from", "have", "into", "like", "more", "most", "need",
    "only", "other", "over", "part", "should", "slide", "slides", "that", "their", "them",
    "then", "there", "these", "this", "through", "using", "what", "when", "where", "which",
    "while", "with", "without", "your",
}
WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9._/-]{2,}")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n")


def page_title(path: Path) -> str:
    text = path.read_text(errors="ignore")
    match = re.search(r'^title:\s+"?(.*?)"?\s*$', text, re.M)
    return match.group(1).strip() if match else path.stem


def upsert_section(path: Path, heading: str, body: str) -> bool:
    if not path.exists():
        return False
    text = path.read_text(errors="ignore")
    block = f"\n## {heading}\n{body.rstrip()}\n"
    pattern = re.compile(rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    if pattern.search(text):
        next_text = pattern.sub(lambda _m: block, text)
    else:
        next_text = text.rstrip() + block
    if next_text != text:
        write(path, next_text)
        return True
    return False


def slide_count(video_id: str) -> int:
    page = SLIDES / f"youtube-{video_id}-dense-slides.md"
    if not page.exists():
        return 0
    return len(re.findall(r"!\[\[assets/dense-slides/", page.read_text(errors="ignore")))


def collect_slide_ocr_text(video_id: str) -> str:
    chunks = []
    for stem in [
        f"youtube-{video_id}-dense-slides",
        f"youtube-{video_id}-reconstructed-slides",
        f"youtube-{video_id}-slides",
    ]:
        path = SLIDES / f"{stem}.md"
        if not path.exists():
            continue
        text = path.read_text(errors="ignore")
        quoted = []
        for line in text.splitlines():
            if line.startswith("> "):
                quoted.append(line[2:].strip())
        chunks.append("\n".join(quoted))
    return "\n".join(chunks)


def top_terms(text: str, limit: int = 18) -> list[str]:
    counts = Counter()
    for word in WORD_RE.findall(text):
        clean = word.strip("._/-").lower()
        if len(clean) < 4 or clean in STOP_WORDS:
            continue
        if clean.isdigit():
            continue
        counts[clean] += 1
    return [word for word, _count in counts.most_common(limit)]


def dense_deck_link(video_id: str) -> str:
    return f"[[youtube-{video_id}-dense-slides]]"


def related_slide_links(video_id: str) -> list[str]:
    links = []
    for stem in [
        f"youtube-{video_id}-dense-slides",
        f"youtube-{video_id}-reconstructed-slides",
        f"youtube-{video_id}-slides",
    ]:
        if (SLIDES / f"{stem}.md").exists():
            links.append(f"[[{stem}]]")
    return links


def load_video_to_talks() -> dict[str, list[dict]]:
    rows = json.loads(SPEAKER_MAP.read_text())
    by_title = defaultdict(list)
    for path in TALKS.glob("*.md"):
        by_title[page_title(path)].append(path)

    mapping: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        video = row.get("related_video") or {}
        video_id = video.get("video_id")
        if not video_id:
            continue
        for talk_path in by_title.get(str(row.get("title") or "").strip(), []):
            mapping[video_id].append({"path": talk_path, "row": row, "video": video})
    return mapping


def add_resource_related_talks(mapping: dict[str, list[dict]]) -> dict[str, list[dict]]:
    for resource in RESOURCES.glob("youtube-*.md"):
        video_id = resource.stem.removeprefix("youtube-")
        text = resource.read_text(errors="ignore")
        for match in re.finditer(r"\[\[([^]|]+)(?:\|[^\]]+)?\]\]", text):
            target = match.group(1).strip()
            talk_path = TALKS / f"{target}.md"
            if not talk_path.exists():
                continue
            existing = {str(item["path"]) for item in mapping.get(video_id, [])}
            if str(talk_path) not in existing:
                mapping[video_id].append({"path": talk_path, "row": {}, "video": {"video_id": video_id}})
    return mapping


def update_resource_page(video_id: str, links: list[str]) -> bool:
    resource = RESOURCES / f"youtube-{video_id}.md"
    if not resource.exists():
        return False
    body = "\n".join(f"- {link}" for link in links)
    return upsert_section(resource, "Extracted Slides", body)


def main() -> int:
    video_to_talks = add_resource_related_talks(load_video_to_talks())
    updated_talks = 0
    updated_resources = 0
    viable_decks = 0

    for dense_page in sorted(SLIDES.glob("youtube-*-dense-slides.md")):
        text = dense_page.read_text(errors="ignore")
        video_match = re.search(r'^video_id:\s+"?(.*?)"?\s*$', text, re.M)
        video_id = video_match.group(1).strip() if video_match else dense_page.stem.removeprefix("youtube-").removesuffix("-dense-slides")
        count = slide_count(video_id)
        if count <= 0:
            continue
        viable_decks += 1
        links = related_slide_links(video_id)
        if update_resource_page(video_id, links):
            updated_resources += 1

        ocr_text = collect_slide_ocr_text(video_id)
        terms = top_terms(ocr_text)
        terms_line = ", ".join(f"`{term}`" for term in terms) if terms else "No reliable slide OCR terms extracted yet."
        link_lines = "\n".join(f"- {link}" for link in links)
        body = "\n".join(
            [
                f"- Slide-only cropped deck: {dense_deck_link(video_id)} ({count} viable slide images).",
                "- Related slide/OCR pages:",
                link_lines,
                f"- Slide-derived terms: {terms_line}",
            ]
        )
        for entry in video_to_talks.get(video_id, []):
            if upsert_section(entry["path"], "Slide Evidence", body):
                updated_talks += 1

    print(json.dumps({
        "viable_dense_decks": viable_decks,
        "updated_talk_pages": updated_talks,
        "updated_resource_pages": updated_resources,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
