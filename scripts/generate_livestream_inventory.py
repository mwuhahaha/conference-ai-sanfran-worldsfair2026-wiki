#!/usr/bin/env python3
"""Generate livestream corpus inventory pages for the World's Fair wiki."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "sources"
WIKI = ROOT / "wiki"
RESOURCES = WIKI / "resources"
SLIDES = WIKI / "slides"
OFFICIAL_VIDEO_MANIFEST = RAW / "official-wf26-video-manifest.json"


def read_json(path: Path, fallback):
    if not path.exists():
        return fallback
    return json.loads(path.read_text(errors="ignore"))


def frontmatter(fields: dict) -> str:
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, list):
            lines.append(f"{key}: [{', '.join(json.dumps(str(item), ensure_ascii=False) for item in value)}]")
        else:
            lines.append(f"{key}: {json.dumps(str(value), ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-") or "untitled"


def is_worldsfair_stream(title: str) -> bool:
    low = title.lower()
    return "world" in low and "fair" in low or "wf2026" in low or "wf26" in low


def official_wf26_livestream_ids() -> set[str]:
    """Return the manifest-authorized primary WF26 livestream set."""

    payload = read_json(OFFICIAL_VIDEO_MANIFEST, {})
    videos = payload.get("videos", []) if isinstance(payload, dict) else []
    return {
        str(item["id"])
        for item in videos
        if isinstance(item, dict)
        and isinstance(item.get("id"), str)
        and item.get("mediaType") == "event_livestream"
    }


def stream_year(title: str) -> str:
    for year in ["2026", "2025", "2024", "2023"]:
        if year in title:
            return year
    if "wf26" in title.lower():
        return "2026"
    return "unknown"


def word_count(path: Path) -> int:
    if not path.exists():
        return 0
    return len(path.read_text(errors="ignore").split())


def page_title(path: Path) -> str:
    if not path.exists():
        return ""
    text = path.read_text(errors="ignore")
    match = re.search(r"^title:\s*\"?([^\"\n]+)\"?", text, re.M)
    if match:
        return match.group(1).strip()
    match = re.search(r"^#\s+(.+)$", text, re.M)
    return match.group(1).strip() if match else path.stem


def stream_rows() -> list[dict]:
    blob = read_json(RAW / "aidotengineer-channel-streams-latest.json", {})
    entries = blob.get("entries") if isinstance(blob, dict) else blob
    rows = []
    primary_wf26_ids = official_wf26_livestream_ids()
    for entry in entries or []:
        video_id = entry.get("id") or entry.get("video_id")
        title = entry.get("title") or video_id or "Untitled"
        if not video_id:
            continue
        transcript = RAW / "youtube-livestream-transcripts" / f"{video_id}.txt"
        standard = SLIDES / f"youtube-{video_id}-slides.md"
        dense = SLIDES / f"youtube-{video_id}-dense-slides.md"
        reconstructed = SLIDES / f"youtube-{video_id}-reconstructed-slides.md"
        resource = RESOURCES / f"youtube-{video_id}.md"
        rows.append(
            {
                "video_id": video_id,
                "title": title,
                "url": entry.get("url") or entry.get("webpage_url") or f"https://www.youtube.com/watch?v={video_id}",
                "year": stream_year(title),
                "worldsfair": is_worldsfair_stream(title),
                "primary_wf26": video_id in primary_wf26_ids,
                "transcript_path": f"raw/sources/youtube-livestream-transcripts/{video_id}.txt" if transcript.exists() else "",
                "transcript_words": word_count(transcript),
                "resource_page": f"wiki/resources/youtube-{video_id}.md" if resource.exists() else "",
                "standard_slide_page": f"wiki/slides/youtube-{video_id}-slides.md" if standard.exists() else "",
                "standard_slide_count": len(re.findall(r"!\[\[assets/slides/", standard.read_text(errors="ignore"))) if standard.exists() else 0,
                "dense_slide_page": f"wiki/slides/youtube-{video_id}-dense-slides.md" if dense.exists() else "",
                "dense_slide_count": len(re.findall(r"!\[\[assets/dense-slides/", dense.read_text(errors="ignore"))) if dense.exists() else 0,
                "reconstructed_slide_page": f"wiki/slides/youtube-{video_id}-reconstructed-slides.md" if reconstructed.exists() else "",
                "reconstructed_slide_count": len(re.findall(r"!\[\[assets/reconstructed-slides/", reconstructed.read_text(errors="ignore"))) if reconstructed.exists() else 0,
                "resource_title": page_title(resource),
            }
        )
    return rows


def link_or_status(row: dict, key: str, label: str, missing: str = "not present") -> str:
    if not row.get(key):
        return missing
    return f"[[{Path(row[key]).stem}|{label}]]"


def write_ai_livestream_corpus(rows: list[dict]) -> None:
    worldsfair = [row for row in rows if row["worldsfair"]]
    lines = [
        frontmatter(
            {
                "title": "AI Engineer Livestream Corpus",
                "category": "resources",
                "sourceLabels": ["Public YouTube metadata", "Livestream corpus audit"],
            }
        ),
        "# AI Engineer Livestream Corpus",
        "",
        "This page inventories AI Engineer channel livestreams. World's Fair San Francisco 2026 livestreams are primary event video sources for media, transcript, and slide evidence; prior World's Fair or other AIE streams are historical/supporting context and should be labeled as such when used.",
        "",
        "## Coverage Summary",
        f"- Channel livestream entries collected: {len(rows)}",
        f"- World's Fair-related livestream entries: {len(worldsfair)}",
        f"- Manifest-authorized World's Fair 2026 livestream entries: {sum(1 for row in rows if row['primary_wf26'])}",
        f"- Livestream transcript caches present: {sum(1 for row in rows if row['transcript_words'])}",
        f"- Livestreams with standard slide pages: {sum(1 for row in rows if row['standard_slide_count'])}",
        f"- Livestreams with dense slide pages: {sum(1 for row in rows if row['dense_slide_count'])}",
        f"- Livestreams with reconstructed slide pages: {sum(1 for row in rows if row['reconstructed_slide_count'])}",
        "",
        "## World's Fair 2026 Livestreams",
    ]
    for row in [r for r in rows if r["primary_wf26"]]:
        transcript = f"{row['transcript_words']:,} transcript words" if row["transcript_words"] else "no cached transcript"
        slides = []
        if row["standard_slide_count"]:
            slides.append(f"{row['standard_slide_count']} standard frames")
        if row["dense_slide_count"]:
            slides.append(f"{row['dense_slide_count']} dense crops")
        if row["reconstructed_slide_count"]:
            slides.append(f"{row['reconstructed_slide_count']} reconstructed crops")
        slide_text = "; ".join(slides) if slides else "no slide deck yet"
        lines.append(f"- [[youtube-{row['video_id']}]] — [{row['title']}]({row['url']}); {transcript}; {slide_text}")
    lines.extend(["", "## Other World's Fair Track Streams"])
    for row in [r for r in rows if r["worldsfair"] and not r["primary_wf26"]]:
        lines.append(
            f"- [{row['title']}]({row['url']}) — {row['year']} title-discovered "
            "supporting context; not admitted as primary WF26 media by the official manifest"
        )
    lines.extend(
        [
            "",
            "## Use Guidance",
            "- Use only manifest-authorized World's Fair San Francisco 2026 livestreams as primary event video sources for what was said or shown in the recording.",
            "- Use older World's Fair track streams only as historical or conceptual context, not as evidence for 2026 session facts.",
            "- When a stream has transcript but no slides, run `scripts/extract_video_slides.py --video-id <id>` and then rebuild.",
            "- When a stream has neither transcript nor slides, fetch captions first; use local Whisper only when public captions are absent.",
        ]
    )
    write(RESOURCES / "ai-engineer-livestream-corpus.md", "\n".join(lines))


def write_worldsfair_page(rows: list[dict]) -> None:
    wf26 = [row for row in rows if row["primary_wf26"]]
    lines = [
        frontmatter(
            {
                "title": "World's Fair 2026 Official Livestreams",
                "category": "resources",
                "sourceLabels": ["Public YouTube metadata", "YouTube transcript helper", "Local slide OCR", "Livestream corpus audit"],
            }
        ),
        "# World's Fair 2026 Official Livestreams",
        "",
        "## What It Is",
        "Official AI Engineer YouTube livestream recordings discovered from the channel's Streams tab for World's Fair 2026 in San Francisco.",
        "",
        "## Livestream Recordings",
    ]
    for row in wf26:
        lines.append(f"- [[youtube-{row['video_id']}]] — {row['title']}")
    lines.extend(["", "## Transcript And Slide Coverage"])
    for row in wf26:
        transcript = f"{row['transcript_words']:,} transcript words" if row["transcript_words"] else "no cached transcript"
        deck_bits = []
        if row["standard_slide_count"]:
            deck_bits.append(f"[[youtube-{row['video_id']}-slides]] ({row['standard_slide_count']} standard frames)")
        if row["dense_slide_count"]:
            deck_bits.append(f"[[youtube-{row['video_id']}-dense-slides]] ({row['dense_slide_count']} dense crops)")
        if row["reconstructed_slide_count"]:
            deck_bits.append(f"[[youtube-{row['video_id']}-reconstructed-slides]] ({row['reconstructed_slide_count']} reconstructed crops)")
        decks = "; ".join(deck_bits) if deck_bits else "no slide deck currently present"
        lines.append(f"- [[youtube-{row['video_id']}]] — {transcript}; {decks}.")
    lines.extend(
        [
            "- YouTube transcript helper returned usable transcript text for all three streams, so Whisper fallback was available but not needed for these livestreams in this run.",
            "",
            "## Room And Track Coverage Check",
            "As of 2026-07-08, the AI Engineer channel Streams tab exposes three World's Fair 2026 livestream recordings in this wiki's source set. They are broad program/main-stage streams, not room-specific recordings for every parallel track.",
            "",
            "The highlighted session [[2026-06-30-corey-gallon-the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans]] was scheduled for 2026-06-30 at 12:05pm in Computer Use / Track 7. Channel searches for Track 7, Computer Use, Corey Gallon, and the Dark Arts title did not find a room livestream or exact session cut. The three cached livestream transcripts were also searched for Corey/Gallon/Dark Arts/chrome-agent/distinctive description phrases; no match was found.",
            "",
            "If a later Track 7 room upload appears, it should be added here and used to revisit the Dark Arts article first.",
            "",
            "## Related Corpus",
            "- [[ai-engineer-livestream-corpus]]",
            "",
            "## Related Subjects",
            "- [[autoresearch]]",
            "- [[software-factories]]",
            "- [[coding-agents]]",
            "- [[inference-engineering]]",
            "- [[agent-evaluations]]",
            "- [[agent-memory]]",
            "- [[slide-library]]",
        ]
    )
    write(RESOURCES / "worldsfair-2026-livestreams.md", "\n".join(lines))


def main() -> int:
    rows = stream_rows()
    write(RAW / "livestream-corpus-audit.json", json.dumps({"streams": rows}, indent=2, ensure_ascii=False))
    write_ai_livestream_corpus(rows)
    write_worldsfair_page(rows)
    print(
        json.dumps(
            {
                "streams": len(rows),
                "worldsfair": sum(1 for row in rows if row["worldsfair"]),
                "primary_wf26": sum(1 for row in rows if row["primary_wf26"]),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
