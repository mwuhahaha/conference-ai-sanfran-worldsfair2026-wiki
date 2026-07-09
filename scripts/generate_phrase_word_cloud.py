#!/usr/bin/env python3
"""Generate a phrase-preserving corpus word cloud for the wiki."""

from __future__ import annotations

import html
import json
import math
import random
import re
from collections import Counter
from pathlib import Path

from PIL import ImageFont


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw" / "sources"
ASSETS = WIKI / "assets"
OUT_SVG = ASSETS / "worldsfair-phrase-word-cloud-v2.svg"
OUT_JSON = RAW / "worldsfair-phrase-word-cloud.json"
OUT_PAGE = WIKI / "resources" / "worldsfair-phrase-word-cloud.md"

WIDTH = 1400
HEIGHT = 860
MAX_TERMS = 115
FONT_PATHS = [
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
]

STOPWORDS = {
    "about", "above", "after", "again", "against", "agent", "agents", "all", "also", "and", "any",
    "are", "around", "because", "been", "before", "being", "between", "both", "build", "building",
    "but", "can", "cannot", "come", "could", "day", "demo", "did", "does", "doing", "done", "each",
    "even", "ever", "every", "from", "get", "gets", "getting", "give", "going", "had", "has",
    "have", "how", "into", "just", "kind", "know", "like", "make", "many", "more", "most", "much",
    "need", "new", "not", "now", "off", "one", "only", "onto", "other", "our", "out", "over",
    "really", "right", "said", "same", "see", "show", "some", "something", "talk", "talks", "than",
    "that", "the", "their", "them", "then", "there", "these", "they", "thing", "things", "this",
    "those", "through", "time", "use", "used", "user", "users", "using", "very", "want", "way",
    "what", "when", "where", "which", "while", "will", "with", "work", "works", "would", "yeah",
    "you", "your",
}

STOPWORDS.update(
    {
        "actually", "caption", "captions", "category", "channel", "conference", "confirmed", "date",
        "description", "doesn", "don", "engineering", "here", "https", "isn", "linkedin", "official",
        "people", "profile", "public", "recording", "related", "relevant", "role", "room", "roster",
        "schedule", "session", "sessions", "source", "sourcelabels", "speaker", "speakers", "status",
        "that'll", "that's", "title", "track", "transcript", "type", "video", "we're", "worldsfair",
        "youtube",
        "across", "back", "basically", "better", "call", "could", "different", "does", "doesn't",
        "don't", "everything", "example", "first", "found", "good", "here's", "it's", "let's",
        "little", "look", "maybe", "next", "okay", "part", "real", "should", "start", "still",
        "take", "that's", "there's", "think", "three", "today", "well", "were", "we've", "without",
        "working", "you're",
    }
)

CORE_PHRASES = {
    "agentic web", "ai engineer", "world's fair", "model context protocol", "mcp apps", "mcp ui",
    "context engineering", "computer use", "coding agents", "software engineering", "software factory",
    "software factories", "agent security", "agent memory", "agentic search", "self-driving production",
    "production ai", "ai agents", "language models", "large language models", "foundation models",
    "open source", "open weights", "local ai", "human handoff", "human in the loop", "multi agent",
    "multi-agent", "knowledge graph", "vector search", "reinforcement learning", "post training",
    "inference systems", "eval harness", "developer tools", "browser automation", "web automation",
    "ai native", "ai-native", "agent ready", "agent-ready", "nearly headless", "reachability over format",
    "agent ready accessibility", "mcp app runtime", "tool calling", "function calling", "prompt injection",
    "secure sandbox", "enterprise ai", "main stage", "search retrieval", "long horizon", "voice agents",
    "video generation", "world models", "robotics", "financial services", "healthcare", "government ai",
}

REQUIRED_PHRASES = [
    "agentic web",
    "model context protocol",
    "self-driving production",
    "agentic search",
    "browser automation",
    "nearly headless",
    "mcp apps",
    "context engineering",
    "computer use",
    "reinforcement learning",
]


def read_json(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8", errors="ignore"))


def frontmatter_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                if line.startswith("title:"):
                    return line.split(":", 1)[1].strip().strip('"')
    match = re.search(r"^#\s+(.+)$", text, re.M)
    return match.group(1).strip() if match else path.stem.replace("-", " ")


def normalize(value: str) -> str:
    value = html.unescape(value).lower()
    value = value.replace("world’s", "world's")
    value = re.sub(r"[^a-z0-9+' -]+", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def add_phrase_candidates(phrases: set[str]) -> None:
    for category in ["topics", "tools", "companies"]:
        folder = WIKI / category
        if folder.exists():
            for path in folder.glob("*.md"):
                if path.name == "index.md":
                    continue
                title = normalize(frontmatter_title(path))
                if 2 <= len(title.split()) <= 5:
                    phrases.add(title)

    sessions = read_json(RAW / "official-sessions.json") or {}
    for item in sessions.get("sessions", []):
        for key in ["title", "track", "room"]:
            value = normalize(str(item.get(key) or ""))
            if 2 <= len(value.split()) <= 7:
                phrases.add(value)
        for speaker in item.get("speakers", []):
            value = normalize(str(speaker))
            if len(value.split()) == 2:
                phrases.add(value)


def source_texts() -> list[tuple[str, str, int]]:
    rows: list[tuple[str, str, int]] = []

    official_parts: list[str] = []
    sessions = read_json(RAW / "official-sessions.json") or {}
    for item in sessions.get("sessions", []):
        for key in ["title", "description", "track"]:
            official_parts.append(str(item.get(key) or ""))
        official_parts.extend(str(speaker) for speaker in item.get("speakers", []))
    speakers = read_json(RAW / "official-speakers.json") or {}
    for item in speakers.get("speakers", []):
        for key in ["name", "role", "company", "bio"]:
            official_parts.append(str(item.get(key) or ""))
    companies = read_json(RAW / "company-profiles.json") or {}
    company_rows = companies.get("companies", []) if isinstance(companies, dict) else []
    for item in company_rows:
        if isinstance(item, dict):
            for value in item.values():
                if isinstance(value, str):
                    official_parts.append(value)
                elif isinstance(value, list):
                    official_parts.extend(str(part) for part in value if isinstance(part, str))
    rows.append(("official-source-fields", "\n".join(official_parts), 3))

    for folder_name in ["youtube-transcripts", "youtube-livestream-transcripts", "external-youtube-transcripts"]:
        folder = RAW / folder_name
        for path in sorted(folder.glob("*.txt")):
            rows.append((str(path.relative_to(ROOT)), path.read_text(encoding="utf-8", errors="ignore"), 1))

    slide_dir = RAW / "slide-ocr"
    for path in sorted(slide_dir.glob("*/*.txt")):
        rows.append((str(path.relative_to(ROOT)), path.read_text(encoding="utf-8", errors="ignore"), 2))

    return rows


def phrase_pattern(phrases: set[str]) -> re.Pattern[str]:
    escaped = [re.escape(phrase).replace(r"\ ", r"\s+") for phrase in sorted(phrases, key=len, reverse=True)]
    return re.compile(r"\b(" + "|".join(escaped) + r")\b", re.I)


def score_terms(rows: list[tuple[str, str, int]], phrases: set[str]) -> tuple[Counter[str], int]:
    counts: Counter[str] = Counter()
    total_words = 0
    pattern = phrase_pattern(phrases)
    for _name, text, weight in rows:
        text = normalize(text)
        total_words += len(text.split())

        phrase_hits: Counter[str] = Counter()

        def repl(match: re.Match[str]) -> str:
            phrase = normalize(match.group(1))
            phrase_hits[phrase] += weight * 3
            return " " + phrase.replace(" ", "_") + " "

        replaced = pattern.sub(repl, text)
        counts.update(phrase_hits)
        tokens = re.findall(r"[a-z][a-z0-9+'_-]{2,}", replaced)
        for token in tokens:
            if "_" in token:
                continue
            if token in STOPWORDS or token.isdigit():
                continue
            counts[token] += weight

    for token in list(counts):
        if len(token) < 4 and "_" not in token:
            del counts[token]
    return counts, total_words


def display_term(term: str) -> str:
    value = term.replace("_", " ")
    replacements = {
        "ai": "AI",
        "mcp": "MCP",
        "llm": "LLM",
        "api": "API",
        "ui": "UI",
        "vs": "VS",
    }
    value = re.sub(r"\b(ai|mcp|llm|api|ui|vs)\b", lambda match: replacements[match.group(1)], value)
    return value


def term_rank(term: str, count: int) -> float:
    words = term.replace("_", " ").split()
    if term in REQUIRED_PHRASES:
        count *= 8
    if len(words) > 1:
        return count * (2.6 + min(len(words), 5) * 0.35)
    return count


def select_terms(counts: Counter[str]) -> list[tuple[str, int]]:
    ranked = sorted(counts.items(), key=lambda item: term_rank(item[0], item[1]), reverse=True)
    selected = ranked[:MAX_TERMS]
    selected_terms = {term for term, _count in selected}
    for phrase in REQUIRED_PHRASES:
        if phrase not in counts or phrase in selected_terms:
            continue
        for index in range(len(selected) - 1, -1, -1):
            if len(selected[index][0].split()) == 1:
                selected[index] = (phrase, counts[phrase])
                selected_terms.add(phrase)
                break
    return sorted(selected, key=lambda item: term_rank(item[0], item[1]), reverse=True)


def rects_overlap(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> bool:
    return not (a[2] < b[0] or a[0] > b[2] or a[3] < b[1] or a[1] > b[3])


def render_svg(terms: list[tuple[str, int]]) -> str:
    font_path = next(path for path in FONT_PATHS if path.exists())
    max_count = max(count for _term, count in terms)
    min_count = min(count for _term, count in terms)
    palette = ["#0f766e", "#1d4ed8", "#b45309", "#7c3aed", "#be123c", "#047857", "#334155", "#9333ea"]
    rng = random.Random(20260709)
    placed: list[tuple[str, int, int, int, str]] = []
    boxes: list[tuple[int, int, int, int]] = []

    for index, (term, count) in enumerate(terms):
        if max_count == min_count:
            size = 32
        else:
            size = int(17 + 64 * (math.log(count) - math.log(min_count)) / (math.log(max_count) - math.log(min_count)))
        label = display_term(term)
        font = ImageFont.truetype(str(font_path), size=size)
        bbox = font.getbbox(label)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        if width > WIDTH - 80:
            scale = (WIDTH - 80) / width
            size = max(14, int(size * scale))
            font = ImageFont.truetype(str(font_path), size=size)
            bbox = font.getbbox(label)
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]

        found = False
        for step in range(1600):
            angle = step * 0.42
            radius = 4 + step * 0.55
            jitter_x = rng.randint(-10, 10)
            jitter_y = rng.randint(-8, 8)
            cx = WIDTH // 2 + int(math.cos(angle) * radius) + jitter_x
            cy = HEIGHT // 2 + int(math.sin(angle) * radius * 0.58) + jitter_y
            x = cx - width // 2
            y = cy - height // 2
            pad = 5
            rect = (x - pad, y - pad, x + width + pad, y + height + pad)
            if rect[0] < 24 or rect[1] < 34 or rect[2] > WIDTH - 24 or rect[3] > HEIGHT - 32:
                continue
            if any(rects_overlap(rect, other) for other in boxes):
                continue
            color = palette[(index + len(term)) % len(palette)]
            placed.append((label, x, y + height, size, color))
            boxes.append(rect)
            found = True
            break
        if not found and len(placed) > 70:
            continue

    texts = [
        f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}">{html.escape(label)}</text>'
        for label, x, y, size, color in placed
    ]
    return "\n".join(
        [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">',
            "<title id=\"title\">AI Engineer World's Fair 2026 Phrase Word Cloud</title>",
            "<desc id=\"desc\">Phrase-preserving word cloud generated from transcripts, slides, official schedule data, and wiki source pages.</desc>",
            '<rect width="100%" height="100%" fill="#f8fafc"/>',
            '<g font-family="DejaVu Sans, Arial, sans-serif" font-weight="700">',
            *texts,
            "</g>",
            "</svg>",
            "",
        ]
    )


def page_markdown(top_terms: list[tuple[str, int]], rows: list[tuple[str, str, int]], total_words: int) -> str:
    transcript_count = sum(1 for name, _text, _weight in rows if "transcripts/" in name)
    slide_count = sum(1 for name, _text, _weight in rows if "slide-ocr/" in name)
    official_count = sum(1 for name, _text, _weight in rows if name.startswith("official-"))
    top_phrase_lines = []
    for term, count in top_terms[:40]:
        label = display_term(term)
        if " " in label:
            top_phrase_lines.append(f"- {label} ({count})")
    return "\n".join(
        [
            "---",
            'title: "Worldsfair Phrase Word Cloud"',
            'category: "resources"',
            'sourceLabels: ["Official schedule", "Transcript evidence", "Local slide OCR", "Phrase-preserving corpus analysis"]',
            "---",
            "",
            "# Worldsfair Phrase Word Cloud",
            "",
            "![[" + str(OUT_SVG.relative_to(WIKI)) + "]]",
            "",
            "## Corpus",
            f"- Official/source JSON files: {official_count}",
            f"- Transcript files: {transcript_count}",
            f"- Slide OCR files: {slide_count}",
            f"- Approximate normalized corpus words: {total_words:,}",
            "",
            "## Phrase Handling",
            "Common conference phrases, topic names, tool names, company names, speaker names, session titles, and schedule labels were matched before token scoring, so phrases such as agentic web, MCP Apps, model context protocol, and self-driving production are kept together.",
            "",
            "## Top Phrase Terms",
            *top_phrase_lines,
            "",
            "## Source Artifact",
            f"- `{OUT_JSON.relative_to(ROOT)}`",
        ]
    ).rstrip() + "\n"


def main() -> int:
    phrases = {normalize(p) for p in CORE_PHRASES}
    add_phrase_candidates(phrases)
    phrases = {p for p in phrases if 2 <= len(p.split()) <= 7 and not any(part in STOPWORDS for part in [p])}
    rows = source_texts()
    counts, total_words = score_terms(rows, phrases)
    top_terms = select_terms(counts)

    ASSETS.mkdir(parents=True, exist_ok=True)
    OUT_SVG.write_text(render_svg(top_terms), encoding="utf-8")
    OUT_PAGE.write_text(page_markdown(top_terms, rows, total_words), encoding="utf-8")
    OUT_JSON.write_text(
        json.dumps(
            {
                "generatedBy": "scripts/generate_phrase_word_cloud.py",
                "sourceCounts": {
                    "documents": len(rows),
                    "approxWords": total_words,
                    "phraseCandidates": len(phrases),
                },
                "terms": [{"term": display_term(term), "count": count} for term, count in top_terms],
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"page": str(OUT_PAGE.relative_to(ROOT)), "svg": str(OUT_SVG.relative_to(ROOT)), "terms": len(top_terms)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
