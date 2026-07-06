"""Enrich the World's Fair wiki from cached YouTube transcripts.

This pass is intentionally deterministic: it creates/updates resource pages,
quote pages, and topic support sections from transcript text already fetched
into raw/sources/youtube-transcripts or raw/sources/youtube-livestream-transcripts.
"""

from __future__ import annotations

import html
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "sources"
WIKI = ROOT / "wiki"
RESOURCES = WIKI / "resources"
TOPICS = WIKI / "topics"
QUOTES = WIKI / "quotes"

STOPWORDS = {
    "about", "after", "again", "agent", "agents", "also", "because", "being", "build", "building",
    "could", "doing", "going", "have", "here", "just", "like", "make", "model", "models", "more",
    "need", "needs", "really", "right", "should", "show", "some", "talk", "than", "that", "their",
    "them", "then", "there", "these", "they", "thing", "things", "this", "those", "through", "using",
    "video", "want", "were", "what", "when", "where", "which", "with", "would", "your",
}

TOPIC_RULES = [
    ("agent-evaluations", "Agent Evaluations", ["eval", "evaluation", "benchmark", "rubric", "judge", "score", "regression", "quality"]),
    ("agent-memory", "Agent Memory", ["memory", "context", "state", "recall", "long horizon", "knowledge graph", "cache"]),
    ("agent-security", "Agent Security", ["security", "permission", "sandbox", "auth", "secret", "attack", "supply chain", "guardrail"]),
    ("ai-sandboxes", "AI Sandboxes", ["sandbox", "environment", "isolation", "container", "runtime", "browser", "computer use"]),
    ("autoresearch", "AutoResearch", ["research", "autoresearch", "scientist", "paper", "experiment", "hypothesis"]),
    ("coding-agents", "Coding Agents", ["code", "coding", "pull request", "diff", "ide", "repo", "software engineer", "swe"]),
    ("inference-engineering", "Inference Engineering", ["inference", "gpu", "latency", "throughput", "token", "tokens", "vllm", "serving"]),
    ("mcp", "MCP", ["mcp", "model context protocol", "tool", "tools", "server", "client", "apps"]),
    ("software-factories", "Software Factories", ["software factory", "factory", "self improving", "autonomous engineering", "sdlc"]),
    ("voice-agents", "Voice Agents", ["voice", "audio", "speech", "transcription", "realtime", "conversation"]),
    ("agentic-search", "Agentic Search", ["search", "retrieval", "rag", "hybrid", "bm25", "vector", "web data"]),
]


def slugify(value: str, *, max_len: int = 90) -> str:
    value = value.lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:max_len].strip("-") or "untitled"


def md_escape(value: str | None) -> str:
    return (value or "").replace("|", "\\|").strip()


def frontmatter(data: dict) -> str:
    lines = ["---"]
    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {json.dumps(item, ensure_ascii=False)}")
        else:
            lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines)


def read_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(errors="ignore"))


def load_new_videos() -> dict[str, dict]:
    videos: dict[str, dict] = {}
    metadata: dict[str, dict] = {}
    discovered: set[str] = set()
    for path in [RAW / "new-video-discovery-2026-07-06.json", RAW / "aidotengineer-channel-videos-latest.json", RAW / "aidotengineer-channel-streams-latest.json"]:
        data = read_json(path, {})
        entries = []
        if isinstance(data, dict):
            new_entries = []
            new_entries.extend(data.get("new_cut_videos") or [])
            new_entries.extend(data.get("new_wf26_streams") or [])
            entries.extend(new_entries)
            entries.extend(data.get("entries") or [])
            if path.name.startswith("new-video-discovery"):
                for entry in new_entries:
                    vid = entry.get("id") or entry.get("video_id")
                    if vid:
                        discovered.add(vid)
        elif isinstance(data, list):
            entries.extend(data)
        for entry in entries:
            vid = entry.get("id") or entry.get("video_id")
            if vid:
                metadata[vid] = entry

    wanted = set(discovered)
    for base in [RAW / "youtube-transcripts", RAW / "youtube-livestream-transcripts"]:
        if base.exists():
            wanted.update(path.stem for path in base.glob("*.txt") if path.stat().st_size > 200)

    for vid in sorted(wanted):
        entry = metadata.get(vid, {})
        title = entry.get("title") or entry.get("youtube_title")
        if not title:
            resource = RESOURCES / f"youtube-{vid}.md"
            if resource.exists():
                match = re.search(r"^#\s+(.+)$", resource.read_text(errors="ignore"), re.M)
                title = match.group(1).strip() if match else None
        videos[vid] = {
            "video_id": vid,
            "youtube_title": title or vid,
            "youtube_url": entry.get("url") or entry.get("webpage_url") or f"https://www.youtube.com/watch?v={vid}",
            "duration": entry.get("duration"),
            "source_kind": "channel_stream" if (RAW / "youtube-livestream-transcripts" / f"{vid}.txt").exists() else "channel_video",
        }
    return videos


def transcript_path(video_id: str) -> Path | None:
    for base in [RAW / "youtube-transcripts", RAW / "youtube-livestream-transcripts"]:
        path = base / f"{video_id}.txt"
        if path.exists() and path.stat().st_size > 200:
            return path
    return None


def title_speaker(title: str) -> tuple[str, list[str], str]:
    parts = re.split(r"\s+[—-]\s+", title, maxsplit=1)
    talk = parts[0].strip()
    speaker_blob = parts[1].strip() if len(parts) > 1 else ""
    speaker_blob = re.sub(r"\b(ft\.|with|w/)\b", "", speaker_blob, flags=re.I)
    speakers = []
    for bit in re.split(r",|&| and ", speaker_blob):
        bit = re.sub(r"\([^)]*\)", "", bit).strip()
        bit = re.sub(r"\b(Anthropic|Google|AWS|Cloudflare|Stripe|RunPod|Snorkel|GitHub|OpenClaw|OpenGov|Modal|Cline|Postman|Nvidia|Databricks|YouTube|AI|Inc|Labs?)\b.*", "", bit).strip()
        if 2 <= len(bit.split()) <= 4 and bit:
            speakers.append(bit)
    company = ""
    if "," in speaker_blob:
        company = speaker_blob.split(",")[-1].strip()
    return talk, speakers[:3], company


def session_slug(session: dict) -> str:
    registry = read_json(WIKI / "talks" / "registry.json", [])
    by_title = {item.get("title", "").lower(): item.get("id") for item in registry}
    return by_title.get(session.get("title", "").lower()) or slugify(f"{session.get('title', '')}")


def normalize(value: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", value.lower()) if len(w) > 2 and w not in STOPWORDS}


def related_sessions(video: dict, sessions: list[dict]) -> list[tuple[int, dict]]:
    title = video["youtube_title"]
    talk_title, speakers, _company = title_speaker(title)
    title_terms = normalize(talk_title)
    speaker_terms = {s.lower() for s in speakers}
    matches = []
    for session in sessions:
        score = 0
        stitle = session.get("title", "")
        overlap = len(title_terms & normalize(stitle))
        if overlap:
            score += overlap * 3
        for speaker in session.get("speakers") or []:
            low = speaker.lower()
            if low in title.lower() or any(low == ss for ss in speaker_terms):
                score += 80
        if score >= 9:
            matches.append((score, session))
    return sorted(matches, key=lambda item: item[0], reverse=True)[:5]


def transcript_summary(text: str) -> list[str]:
    words = normalize(text)
    counts = Counter(w for w in words if len(w) > 3)
    top = [w for w, _ in counts.most_common(10)]
    return top[:8]


def topic_hits(title: str, text: str) -> list[tuple[str, str, int]]:
    hay = f"{title}\n{text[:25000]}".lower()
    hits = []
    for slug, label, keys in TOPIC_RULES:
        score = 0
        for key in keys:
            score += hay.count(key.lower())
        if score:
            hits.append((slug, label, score))
    return sorted(hits, key=lambda row: row[2], reverse=True)[:4]


def split_sentences(text: str) -> list[str]:
    compact = re.sub(r"\s+", " ", text).strip()
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", compact) if s.strip()]


QUOTE_PATTERNS = [
    r"\bthe (hard|important|interesting|weird|scary|funny) part\b",
    r"\bwhat (we|you|I) learned\b",
    r"\bthe problem is\b",
    r"\bthe key is\b",
    r"\bwe need to\b",
    r"\byou need to\b",
    r"\bnot just\b",
    r"\bin production\b",
    r"\btrust\b",
    r"\bevaluation\b",
    r"\bsecurity\b",
    r"\bmemory\b",
    r"\bcontext\b",
]


def quote_candidates(video_id: str, video: dict, text: str, topics: list[tuple[str, str, int]]) -> list[dict]:
    candidates = []
    topic_slug = topics[0][0] if topics else "resources"
    topic_label = topics[0][1] if topics else "Supporting Resources"
    for sentence in split_sentences(text):
        words = sentence.split()
        if len(words) < 12 or len(words) > 42:
            continue
        low = sentence.lower()
        score = sum(5 for pat in QUOTE_PATTERNS if re.search(pat, low))
        score += min(10, len(set(normalize(sentence)) & set(normalize(video["youtube_title"]))) * 2)
        if score >= 5:
            candidates.append({
                "quote": sentence,
                "score": score,
                "video_id": video_id,
                "video_title": video["youtube_title"],
                "topic": topic_slug,
                "topic_label": topic_label,
            })
    dedup = []
    seen = set()
    for row in sorted(candidates, key=lambda r: r["score"], reverse=True):
        key = re.sub(r"[^a-z0-9]+", " ", row["quote"].lower())[:100]
        if key in seen:
            continue
        seen.add(key)
        dedup.append(row)
        if len(dedup) >= 3:
            break
    return dedup


def upsert_section(path: Path, heading: str, body: str) -> None:
    text = path.read_text(errors="ignore") if path.exists() else ""
    section = f"## {heading}\n{body.strip()}\n"
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    if pattern.search(text):
        text = pattern.sub(section, text).rstrip() + "\n"
    else:
        text = text.rstrip() + "\n\n" + section
    path.write_text(text, encoding="utf-8")


def write_resource(video_id: str, video: dict, text: str, topics: list[tuple[str, str, int]], matches: list[tuple[int, dict]]) -> None:
    RESOURCES.mkdir(parents=True, exist_ok=True)
    words = len(text.split())
    topic_links = ", ".join(f"[[{slug}|{label}]]" for slug, label, _score in topics) or "None detected"
    keywords = ", ".join(f"`{w}`" for w in transcript_summary(text))
    source_kind = "WF26 livestream" if video.get("source_kind") == "channel_stream" else "AI Engineer cut video"
    lines = [
        frontmatter({
            "title": video["youtube_title"],
            "category": "resources",
            "sourceLabels": ["Public YouTube metadata", "YouTube transcript"],
            "videoId": video_id,
            "last_enriched": datetime.now(timezone.utc).isoformat(),
        }),
        f"# {video['youtube_title']}",
        "",
        "## What It Is",
        f"A public AI Engineer YouTube {source_kind} used as supporting material for the AI Engineer World's Fair 2026 wiki.",
        "",
        "## Transcript Status",
        f"Cached transcript text is available at `raw/sources/{'youtube-livestream-transcripts' if video.get('source_kind') == 'channel_stream' else 'youtube-transcripts'}/{video_id}.txt` ({words:,} words).",
        "",
        "## Topic Signals",
        f"- {topic_links}",
        f"- Transcript keywords: {keywords or 'none'}",
        "",
        "## Link",
        f"[YouTube]({video['youtube_url']})",
    ]
    if matches:
        lines.extend(["", "## Related Scheduled Sessions"])
        for score, session in matches:
            lines.append(f"- [[{session_slug(session)}]] — {md_escape(session.get('title'))} (match score {score})")
    page = RESOURCES / f"youtube-{video_id}.md"
    existing = page.read_text(errors="ignore") if page.exists() else ""
    preserved_sections = set()
    for section in ["Extracted Slides", "Dense Slide Evidence", "Reconstructed Slide Deck"]:
        m = re.search(rf"^## {re.escape(section)}\n.*?(?=^## |\Z)", existing, re.M | re.S)
        if m:
            lines.extend(["", m.group(0).strip()])
            preserved_sections.add(section)
    if "Extracted Slides" not in preserved_sections and (WIKI / "slides" / f"youtube-{video_id}-slides.md").exists():
        lines.extend(["", "## Extracted Slides", f"- [[youtube-{video_id}-slides]]"])
    page.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def non_article_supporting_media(video: dict) -> bool:
    title = (video.get("youtube_title") or "").lower()
    return "vibe reel" in title


def write_non_transcript_resource(video_id: str, video: dict, reason: str) -> None:
    RESOURCES.mkdir(parents=True, exist_ok=True)
    lines = [
        frontmatter({
            "title": video["youtube_title"],
            "category": "resources",
            "sourceLabels": ["Public YouTube metadata"],
            "videoId": video_id,
            "last_enriched": datetime.now(timezone.utc).isoformat(),
        }),
        f"# {video['youtube_title']}",
        "",
        "## What It Is",
        "A public AI Engineer YouTube supporting media item connected to AI Engineer World's Fair 2026.",
        "",
        "## Transcript Status",
        reason,
        "",
        "## Link",
        f"[YouTube]({video['youtube_url']})",
    ]
    page = RESOURCES / f"youtube-{video_id}.md"
    existing = page.read_text(errors="ignore") if page.exists() else ""
    preserved_sections = set()
    for section in ["Extracted Slides", "Dense Slide Evidence", "Reconstructed Slide Deck"]:
        m = re.search(rf"^## {re.escape(section)}\n.*?(?=^## |\Z)", existing, re.M | re.S)
        if m:
            lines.extend(["", m.group(0).strip()])
            preserved_sections.add(section)
    if "Extracted Slides" not in preserved_sections and (WIKI / "slides" / f"youtube-{video_id}-slides.md").exists():
        lines.extend(["", "## Extracted Slides", f"- [[youtube-{video_id}-slides]]"])
    page.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_quote_pages(quotes: list[dict]) -> None:
    QUOTES.mkdir(parents=True, exist_ok=True)
    index_lines = [
        frontmatter({"title": "Quotes", "category": "quotes", "sourceLabels": ["YouTube transcript"]}),
        "# Quotes",
        "",
        "Transcript-backed pull quotes surfaced from AI Engineer World's Fair 2026 supporting videos and livestreams. These are short excerpts selected for navigation and should be checked against the linked transcript/resource context before reuse.",
        "",
        "## Index",
    ]
    by_topic: dict[str, list[dict]] = defaultdict(list)
    for row in quotes:
        by_topic[row["topic"]].append(row)
    for topic, rows in sorted(by_topic.items()):
        index_lines.extend(["", f"### [[{topic}|{rows[0]['topic_label']}]]"])
        for index, row in enumerate(sorted(rows, key=lambda r: r["score"], reverse=True)[:12], start=1):
            qslug = slugify(row["quote"], max_len=70)
            page_id = f"quote-{row['video_id']}-{index:02d}-{qslug}"
            index_lines.append(f"- [[{page_id}]] — {md_escape(row['video_title'])}")
            (QUOTES / f"{page_id}.md").write_text(
                "\n".join([
                    frontmatter({
                        "title": row["quote"][:80],
                        "category": "quotes",
                        "sourceLabels": ["YouTube transcript"],
                        "videoId": row["video_id"],
                        "topic": row["topic"],
                    }),
                    f"# {row['quote'][:80]}",
                    "",
                    f"> {row['quote']}",
                    "",
                    "## Source",
                    f"- [[youtube-{row['video_id']}]] — {md_escape(row['video_title'])}",
                    f"- Related topic: [[{row['topic']}|{row['topic_label']}]]",
                ]).rstrip() + "\n",
                encoding="utf-8",
            )
    (WIKI / "quotes.md").write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")
    registry = [
        {"id": p.stem, "title": p.stem.removeprefix("quote-"), "path": f"wiki/quotes/{p.name}"}
        for p in sorted(QUOTES.glob("*.md"))
    ]
    (QUOTES / "registry.json").write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8")


def update_topic_pages(topic_resources: dict[str, list[dict]], topic_quotes: dict[str, list[dict]]) -> None:
    TOPICS.mkdir(parents=True, exist_ok=True)
    existing_registry = read_json(TOPICS / "registry.json", [])
    known = {item.get("id"): item.get("title") for item in existing_registry}
    for slug, label, _keys in TOPIC_RULES:
        path = TOPICS / f"{slug}.md"
        if not path.exists():
            path.write_text(
                "\n".join([
                    frontmatter({"title": label, "category": "topics", "sourceLabels": ["Transcript-derived supporting context"]}),
                    f"# {label}",
                    "",
                    "## Why It Matters Here",
                    "This topic page is generated from schedule, transcript, and slide-resource signals in the AI Engineer World's Fair 2026 wiki.",
                ]) + "\n",
                encoding="utf-8",
            )
        resources = topic_resources.get(slug, [])
        quotes = topic_quotes.get(slug, [])
        support = []
        if resources:
            support.append("### Transcript-backed resources")
            for row in sorted(resources, key=lambda r: r["score"], reverse=True)[:18]:
                support.append(f"- [[youtube-{row['video_id']}]] — {md_escape(row['title'])}")
        if quotes:
            support.extend(["", "### Quote signals"])
            for row in sorted(quotes, key=lambda r: r["score"], reverse=True)[:8]:
                support.append(f"- “{md_escape(row['quote'])}” — [[youtube-{row['video_id']}]]")
        if support:
            upsert_section(path, "Transcript And Resource Support", "\n".join(support))
        known.setdefault(slug, label)
    registry = [{"id": slug, "title": title or slug.replace("-", " ").title(), "path": f"wiki/topics/{slug}.md"} for slug, title in sorted(known.items()) if slug]
    (TOPICS / "registry.json").write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8")


def update_resource_registry() -> None:
    rows = []
    for page in sorted(RESOURCES.glob("*.md")):
        if page.name == "registry.json":
            continue
        title = page.stem.replace("-", " ").title()
        text = page.read_text(errors="ignore")
        m = re.search(r"^title:\s*(.+)$", text, re.M)
        if m:
            title = m.group(1).strip().strip('"')
        rows.append({"id": page.stem, "title": title, "path": f"wiki/resources/{page.name}"})
    (RESOURCES / "registry.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> int:
    sessions = read_json(RAW / "official-sessions.json", {}).get("sessions", [])
    videos = load_new_videos()
    quote_rows = []
    topic_resources: dict[str, list[dict]] = defaultdict(list)
    topic_quotes: dict[str, list[dict]] = defaultdict(list)
    processed = []
    missing = []
    skipped_non_article = []
    for video_id, video in sorted(videos.items(), key=lambda item: item[1]["youtube_title"].lower()):
        path = transcript_path(video_id)
        if not path:
            if non_article_supporting_media(video):
                write_non_transcript_resource(
                    video_id,
                    video,
                    "No article transcript is expected for this non-talk event reel; it is kept as supporting media rather than topic evidence.",
                )
                skipped_non_article.append({"video_id": video_id, "title": video["youtube_title"], "reason": "non-talk event reel"})
                continue
            missing.append(video_id)
            continue
        text = path.read_text(errors="ignore")
        topics = topic_hits(video["youtube_title"], text)
        matches = related_sessions(video, sessions)
        write_resource(video_id, video, text, topics, matches)
        for slug, label, score in topics:
            topic_resources[slug].append({"video_id": video_id, "title": video["youtube_title"], "score": score})
        qrows = quote_candidates(video_id, video, text, topics)
        quote_rows.extend(qrows)
        for row in qrows:
            topic_quotes[row["topic"]].append(row)
        processed.append({"video_id": video_id, "title": video["youtube_title"], "topics": topics, "matches": [session_slug(s) for _score, s in matches], "quotes": len(qrows), "words": len(text.split())})
    write_quote_pages(quote_rows)
    update_topic_pages(topic_resources, topic_quotes)
    update_resource_registry()
    report = {
        "processed": processed,
        "missing_transcripts": missing,
        "skipped_non_article": skipped_non_article,
        "quote_count": len(quote_rows),
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    (RAW / "transcript-enrichment-report-2026-07-06.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"processed": len(processed), "missing": missing, "quotes": len(quote_rows)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
