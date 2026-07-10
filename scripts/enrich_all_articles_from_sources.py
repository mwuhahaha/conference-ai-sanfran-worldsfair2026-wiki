#!/usr/bin/env python3
"""General source-backed enrichment for wiki articles.

Every article is eligible for source-derived evidence from schedule pages,
linked videos, transcripts, and slide material. Generated article text uses
neutral source/evidence language.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw" / "sources"
WORDLIST_PATHS = [
    Path("/usr/share/dict/words"),
    Path("/usr/share/dict/american-english"),
]

TRANSCRIPT_DIRS = [
    RAW / "youtube-transcripts",
    RAW / "external-youtube-transcripts",
    RAW / "youtube-livestream-transcripts",
]

STOPWORDS = {
    "about", "actually", "after", "again", "agent", "agents", "all", "also", "because", "basically",
    "being", "build", "building", "could", "different", "every", "example", "from", "going", "have",
    "good", "here", "in", "into", "just", "kind", "know", "like", "make", "more", "much", "need",
    "needs", "only", "other", "people", "really", "right", "same", "slide", "slides", "some",
    "something", "sort", "talk", "that", "their", "there", "these", "them", "then", "they", "thing",
    "things", "think", "this", "those", "through", "time", "using", "very", "video", "videos",
    "want", "were", "what", "when", "where", "which", "will", "with", "work", "would", "yeah",
    "you", "your",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_words() -> set[str]:
    for path in WORDLIST_PATHS:
        if path.exists():
            return {
                word.strip().lower()
                for word in read(path).splitlines()
                if word.strip().isalpha() and len(word.strip()) >= 3
            }
    return set()


ENGLISH_WORDS = load_words()


def split_frontmatter(text: str) -> tuple[str, str, dict[str, str]]:
    if not text.startswith("---\n"):
        return "", text, {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text, {}
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return text[: end + 5], text[end + 5 :].lstrip(), fields


def title_of(path: Path) -> str:
    text = read(path)
    _fm, body, fields = split_frontmatter(text)
    if fields.get("title"):
        return fields["title"]
    match = re.search(r"^#\s+(.+)$", body, re.M)
    return match.group(1).strip() if match else path.stem.replace("-", " ").title()


def upsert_section(markdown: str, heading: str, body: str) -> str:
    fm, content, _fields = split_frontmatter(markdown)
    replacement = f"## {heading}\n{body.strip()}\n"
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    if pattern.search(content):
        content = pattern.sub(lambda _match: replacement, content).rstrip() + "\n"
    else:
        content = content.rstrip() + "\n\n" + replacement
    return fm + content


def remove_section(markdown: str, heading: str) -> str:
    fm, content, _fields = split_frontmatter(markdown)
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    content = pattern.sub("", content).rstrip() + "\n"
    return fm + content.lstrip()


def remove_pending_transcript_note(markdown: str) -> str:
    """Drop the original schedule-only placeholder once richer evidence exists."""
    fm, content, _fields = split_frontmatter(markdown)
    pattern = re.compile(r"^## Notes\n(.*?)(?=^## |\Z)", re.M | re.S)
    match = pattern.search(content)
    if not match:
        return markdown
    lines = [
        line
        for line in match.group(1).splitlines()
        if "Pending transcript synthesis when an official recording or confirmed matching video is available." not in line
    ]
    body = "\n".join(line for line in lines if line.strip()).strip()
    replacement = f"## Notes\n{body}\n" if body else ""
    content = pattern.sub(replacement, content).rstrip() + "\n"
    return fm + content.lstrip()


def video_ids(text: str) -> list[str]:
    ids = set(re.findall(r"(?:watch\?v=|youtu\.be/)([A-Za-z0-9_-]{11})", text))
    ids.update(re.findall(r"youtube-([A-Za-z0-9_-]{11})(?=[\]\)\s/#-]|$)", text))
    return sorted(video_id for video_id in ids if has_video_evidence(video_id))


def has_video_evidence(video_id: str) -> bool:
    if (WIKI / "resources" / f"youtube-{video_id}.md").exists():
        return True
    if any((folder / f"{video_id}.txt").exists() for folder in TRANSCRIPT_DIRS):
        return True
    return any((WIKI / "slides" / f"youtube-{video_id}-{suffix}.md").exists() for suffix in ["slides", "dense-slides", "reconstructed-slides"])


def wikilinks(text: str) -> list[str]:
    links = []
    for raw in re.findall(r"\[\[([^\]]+)\]\]", text):
        target = raw.split("|", 1)[0].strip()
        if target:
            links.append(target)
    return links


def transcript_text(video_id: str) -> tuple[Path | None, str]:
    for folder in TRANSCRIPT_DIRS:
        path = folder / f"{video_id}.txt"
        if path.exists():
            return path, read(path)
    return None, ""


def compact_line(value: str) -> str:
    value = re.sub(r"\s+", " ", value.replace("->", "→")).strip(" -•\t")
    return value


def useful_line(value: str, *, strict: bool = False) -> bool:
    value = compact_line(value)
    if len(value) < 8 or len(value) > 180:
        return False
    if "\\" in value:
        return False
    if re.match(r"^[^\w(]", value):
        return False
    low = re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()
    words = low.split()
    if not words:
        return False
    noise_words = {"a", "c", "ee", "ae", "oo", "sb", "ss"}
    if sum(1 for word in words if word in noise_words) >= 2:
        return False
    if len(words[0]) == 1:
        return False
    if "world ss" in low:
        return False
    if len(words) <= 4 and words[-1] in STOPWORDS:
        return False
    if not any(word not in STOPWORDS for word in words):
        return False
    noisy_phrases = [
        "innovation partner",
        "platinum sponsor",
        "platinum sponsors",
        "presented by",
        "presenting sponsor",
        "world s fair",
        "worldsfair",
        "ai engineer",
        "aiengineer",
        "alengineer",
    ]
    if any(phrase in low for phrase in noisy_phrases) and len(words) <= 8:
        return False
    if len(words) == 1 and not any(ch.isdigit() for ch in low):
        return False
    if len(words) < 3 and not any(ch.isdigit() for ch in value) and not any(mark in value for mark in [":", "/", "→", "-"]):
        return False
    if strict and len(words) < 4 and not any(ch.isdigit() for ch in value):
        return False
    short_words = sum(1 for word in words if len(word) <= 2)
    if len(words) >= 4 and short_words / len(words) > 0.55:
        return False
    if re.search(r"\b(?:e{3,}|a{3,}|o{3,})\b", low):
        return False
    letters = sum(ch.isalpha() for ch in value)
    if letters < 5:
        return False
    if re.fullmatch(r"[\W\d_]+", value):
        return False
    return True


def display_slide_line(value: str) -> bool:
    if not useful_line(value, strict=True):
        return False
    tokens = re.findall(r"[A-Za-z][A-Za-z']{2,}", value)
    if not tokens:
        return False
    if any(len(token) > 24 for token in tokens):
        return False
    known = 0
    checked = 0
    for token in tokens:
        bare = token.strip("'").lower()
        if len(bare) < 4:
            continue
        if token.isupper() and len(token) <= 6:
            known += 1
            checked += 1
            continue
        if bare in ENGLISH_WORDS:
            known += 1
        checked += 1
    return checked == 0 or (known / checked) >= 0.55


def extract_block_text(markdown: str, *, strict: bool = False) -> list[str]:
    lines: list[str] = []
    capture = False
    for line in markdown.splitlines():
        stripped = line.rstrip()
        if stripped in {"Slide text:", "OCR text:"}:
            capture = True
            continue
        if capture:
            if stripped.startswith(">"):
                clean = compact_line(stripped.lstrip("> "))
                if useful_line(clean, strict=strict):
                    lines.append(clean)
                continue
            if not stripped:
                continue
            capture = False
    return dedupe(lines)


def classification_text(video_id: str) -> list[str]:
    lines: list[str] = []
    for audit in sorted((RAW / "slide-ai-classification").glob(f"*/{video_id}/audit.json")):
        data = json.loads(read(audit))
        for item in data.get("accepted", []):
            for line in str(item.get("text") or "").splitlines():
                clean = compact_line(line)
                if useful_line(clean):
                    lines.append(clean)
    return dedupe(lines)


def slide_text(video_id: str) -> list[str]:
    classified = classification_text(video_id)
    if classified:
        return classified[:10]
    lines: list[str] = []
    for suffix in ["dense-slides", "reconstructed-slides"]:
        page = WIKI / "slides" / f"youtube-{video_id}-{suffix}.md"
        if page.exists():
            lines.extend(extract_block_text(read(page)))
    page = WIKI / "slides" / f"youtube-{video_id}-slides.md"
    if page.exists():
        lines.extend(extract_block_text(read(page), strict=True))
    return dedupe(lines)


def dedupe(items: list[str], limit: int = 20) -> list[str]:
    seen = set()
    result = []
    for item in items:
        key = re.sub(r"\W+", "", item.lower())
        if not key or key in seen:
            continue
        seen.add(key)
        result.append(item)
        if len(result) >= limit:
            break
    return result


def keyword_summary(text: str, limit: int = 8) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9-]{3,}", text.lower())
    counts = Counter(w for w in words if w not in STOPWORDS)
    return [word for word, _count in counts.most_common(limit)]


def slide_keyword_summary(lines: list[str], limit: int = 8) -> list[str]:
    words = []
    for line in lines:
        for word in re.findall(r"[A-Za-z][A-Za-z'-]{3,}", line.lower()):
            word = word.strip("-'")
            if word in STOPWORDS:
                continue
            if word in ENGLISH_WORDS or word in {"agentic", "playwright", "browserbase", "stagehand", "openclaw", "mcp"}:
                words.append(word)
    counts = Counter(words)
    return [word for word, _count in counts.most_common(limit)]


def evidence_for_video(video_id: str) -> dict:
    tpath, transcript = transcript_text(video_id)
    slides = [line for line in slide_text(video_id) if display_slide_line(line)]
    resource = WIKI / "resources" / f"youtube-{video_id}.md"
    return {
        "video_id": video_id,
        "transcript_path": tpath,
        "transcript_words": len(transcript.split()) if transcript else 0,
        "keywords": keyword_summary(transcript, 8) if transcript else [],
        "slide_lines": slides[:10],
        "slide_keywords": slide_keyword_summary(slides, 8),
        "resource_exists": resource.exists(),
        "slide_pages": [
            f"youtube-{video_id}-{suffix}"
            for suffix in ["slides", "dense-slides", "reconstructed-slides"]
            if (WIKI / "slides" / f"youtube-{video_id}-{suffix}.md").exists()
        ],
    }


def slide_page_summary(page_id: str) -> dict:
    path = WIKI / "slides" / f"{page_id}.md"
    text = read(path)
    images = re.findall(r"!\[\[([^\]]+\.(?:jpg|jpeg|png|webp))(?:\|[^\]]+)?\]\]", text, flags=re.I)
    recreation_count = len(re.findall(r"open HTML recreation", text))
    no_visible = "No slide-like frames are visible after AI slide classification" in text
    title = title_of(path) if path.exists() else page_id
    return {
        "page_id": page_id,
        "title": title,
        "images": images,
        "recreation_count": recreation_count,
        "no_visible": no_visible,
    }


def render_talk_slides_section(video_ids_: list[str]) -> str:
    if not video_ids_:
        return ""
    lines: list[str] = []
    found = False
    for video_id in video_ids_[:6]:
        ev = evidence_for_video(video_id)
        slide_pages = ev["slide_pages"]
        if not slide_pages:
            continue
        found = True
        lines.append(f"- Source video: `youtube-{video_id}`")

        preferred = sorted(
            slide_pages,
            key=lambda page_id: (
                0 if page_id.endswith("-dense-slides") else 1 if page_id.endswith("-reconstructed-slides") else 2,
                page_id,
            ),
        )
        primary = preferred[0]
        summary = slide_page_summary(primary)
        bits = []
        if summary["images"]:
            bits.append(f"{len(summary['images'])} visible slide image(s)")
        if summary["recreation_count"]:
            bits.append(f"{summary['recreation_count']} HTML recreation(s)")
        if summary["no_visible"]:
            bits.append("no readable content slides after AI classification")
        detail = "; ".join(bits) if bits else "slide evidence page"
        lines.append(f"- Slide deck: [[{primary}|{summary['title']}]] — {detail}.")
        for image in summary["images"][:3]:
            lines.append(f"![[{image}]]")

        alternates = [page_id for page_id in slide_pages if page_id != primary]
        if alternates:
            links = ", ".join(f"[[{page_id}|{title_of(WIKI / 'slides' / f'{page_id}.md')}]]" for page_id in alternates)
            lines.append(f"- Additional slide evidence: {links}")
        if ev["slide_keywords"]:
            lines.append(f"- Slide-derived themes for `youtube-{video_id}`: {', '.join(ev['slide_keywords'])}.")
    return "\n".join(lines) if found else ""


def render_evidence_section(video_ids_: list[str], *, include_title: bool = True) -> str:
    if not video_ids_:
        return "No linked video, transcript, or slide source has been attached yet."
    lines: list[str] = []
    for video_id in video_ids_[:6]:
        ev = evidence_for_video(video_id)
        if not ev["transcript_words"] and not ev["slide_lines"] and not ev["resource_exists"] and not ev["slide_pages"]:
            continue
        if include_title:
            bits = []
            if ev["transcript_words"]:
                bits.append(f"{ev['transcript_words']:,} transcript words")
            if ev["slide_lines"]:
                bits.append(f"{len(ev['slide_lines'])} slide-derived text signals")
            lines.append(f"- `youtube-{video_id}` — " + ("; ".join(bits) if bits else "source page linked"))
        if ev["keywords"]:
            lines.append(f"- Transcript signals for `youtube-{video_id}`: {', '.join(ev['keywords'])}.")
        if ev["slide_keywords"]:
            lines.append(f"- Slide-derived themes for `youtube-{video_id}`: {', '.join(ev['slide_keywords'])}.")
        links = []
        if ev["resource_exists"]:
            links.append(f"[[youtube-{video_id}]]")
        if ev["transcript_path"]:
            links.append(f"[[youtube-{video_id}-transcript]]")
        links.extend(f"[[{page}]]" for page in ev["slide_pages"])
        if links:
            lines.append(f"- Evidence links for `youtube-{video_id}`: {', '.join(links)}")
    return "\n".join(lines) if lines else "No linked video, transcript, or slide source has been attached yet."


def enrich_talk(path: Path) -> bool:
    text = read(path)
    ids = video_ids(text)
    new_text = remove_pending_transcript_note(text) if ids else text
    slides_section = render_talk_slides_section(ids)
    new_text = upsert_section(new_text, "Slides", slides_section) if slides_section else remove_section(new_text, "Slides")
    section = [
        "This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.",
        "",
        "### Source Signals",
        render_evidence_section(ids),
        "",
        "### Article Use",
        "Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.",
    ]
    new_text = upsert_section(new_text, "Source-Derived Enrichment", "\n".join(section))
    if new_text != text:
        write(path, new_text)
        return True
    return False


def page_mentions_for(slug: str, title: str, folders: list[str], limit: int = 12) -> list[Path]:
    needles = {slug.lower(), title.lower()}
    parts = [part for part in re.split(r"[^a-z0-9]+", slug.lower()) if len(part) > 3]
    paths = []
    for folder in folders:
        for path in sorted((WIKI / folder).glob("*.md")):
            hay = read(path).lower()
            if any(needle and needle in hay for needle in needles) or sum(part in hay for part in parts) >= 2:
                paths.append(path)
                if len(paths) >= limit:
                    return paths
    return paths


def collect_video_ids_from_pages(paths: list[Path]) -> list[str]:
    ids: list[str] = []
    for path in paths:
        ids.extend(video_ids(read(path)))
    return dedupe(ids, limit=8)


def enrich_topic(path: Path) -> bool:
    text = read(path)
    title = title_of(path)
    related = [WIKI / "talks" / f"{target}.md" for target in wikilinks(text) if (WIKI / "talks" / f"{target}.md").exists()]
    related.extend(page_mentions_for(path.stem, title, ["talks"], limit=8))
    related = dedupe_paths(related, 10)
    ids = collect_video_ids_from_pages(related)
    lines = [
        "This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.",
        "",
        "### Talk Evidence",
    ]
    if related:
        for talk in related[:10]:
            lines.append(f"- [[{talk.stem}|{title_of(talk)}]]")
    else:
        lines.append("- No related talks were found by link or text match in this pass.")
    lines.extend(["", "### Slide And Transcript Signals", render_evidence_section(ids)])
    new_text = upsert_section(text, "Source-Derived Enrichment", "\n".join(lines))
    if new_text != text:
        write(path, new_text)
        return True
    return False


def dedupe_paths(paths: list[Path], limit: int) -> list[Path]:
    seen = set()
    out = []
    for path in paths:
        if path in seen or not path.exists():
            continue
        seen.add(path)
        out.append(path)
        if len(out) >= limit:
            break
    return out


def enrich_person_or_company(path: Path, kind: str) -> bool:
    text = read(path)
    links = [target for target in wikilinks(text) if (WIKI / "talks" / f"{target}.md").exists()]
    talk_paths = [WIKI / "talks" / f"{target}.md" for target in links]
    if not talk_paths:
        talk_paths = page_mentions_for(path.stem, title_of(path), ["talks"], limit=8)
    talk_paths = dedupe_paths(talk_paths, 10)
    ids = collect_video_ids_from_pages(talk_paths)
    label = "person" if kind == "people" else "organization"
    lines = [
        f"This section summarizes how this {label} appears across the conference source graph: scheduled sessions, linked videos, transcripts, and slide-derived evidence.",
        "",
        "### Related Sessions",
    ]
    if talk_paths:
        for talk in talk_paths[:10]:
            lines.append(f"- [[{talk.stem}|{title_of(talk)}]]")
    else:
        lines.append("- No related scheduled session was found in this pass.")
    lines.extend(["", "### Slide And Transcript Signals", render_evidence_section(ids)])
    new_text = upsert_section(text, "Source-Derived Enrichment", "\n".join(lines))
    if new_text != text:
        write(path, new_text)
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--talks", action="store_true")
    parser.add_argument("--topics", action="store_true")
    parser.add_argument("--people", action="store_true")
    parser.add_argument("--companies", action="store_true")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    if not any([args.talks, args.topics, args.people, args.companies, args.all]):
        args.all = True

    counts = defaultdict(int)
    targets: list[tuple[str, Path]] = []
    if args.all or args.talks:
        targets.extend(("talks", p) for p in sorted((WIKI / "talks").glob("*.md")))
    if args.all or args.topics:
        targets.extend(("topics", p) for p in sorted((WIKI / "topics").glob("*.md")) if p.name != "index.md")
    if args.all or args.people:
        targets.extend(("people", p) for p in sorted((WIKI / "people").glob("*.md")) if p.name != "index.md")
    if args.all or args.companies:
        targets.extend(("companies", p) for p in sorted((WIKI / "companies").glob("*.md")) if p.name != "index.md")
    if args.limit:
        targets = targets[: args.limit]

    for kind, path in targets:
        changed = False
        if kind == "talks":
            changed = enrich_talk(path)
        elif kind == "topics":
            changed = enrich_topic(path)
        elif kind in {"people", "companies"}:
            changed = enrich_person_or_company(path, kind)
        if changed:
            counts[kind] += 1

    print(json.dumps({"updated": dict(counts), "processed": len(targets)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
