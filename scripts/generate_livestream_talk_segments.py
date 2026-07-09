#!/usr/bin/env python3
"""Match timed livestream captions to scheduled talk pages.

The source captions are local VTT files produced by yt-dlp. This script keeps
only high-confidence matches, then writes timestamped livestream links into
talk and people pages.
"""

from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw" / "sources"
SUBS = RAW / "youtube-subtitles"

STREAMS = {
    "htM02KMNZnk": {
        "video_id": "htM02KMNZnk",
        "title": "WF2026: Software Factories & Keynotes (Day 1)",
        "vtt": SUBS / "htM02KMNZnk.en-orig.vtt",
    },
    "4sX_He5c4sI": {
        "video_id": "4sX_He5c4sI",
        "title": "WF2026: Autoresearch & Keynotes (Day 2)",
        "vtt": SUBS / "4sX_He5c4sI.en-orig.vtt",
    },
    "I2cbIws9j10": {
        "video_id": "I2cbIws9j10",
        "title": "WF26: Harness Engineering & Startup Battlefield (Day 3)",
        "vtt": SUBS / "I2cbIws9j10.en-orig.vtt",
    },
}

STOPWORDS = {
    "about",
    "after",
    "agent",
    "agents",
    "build",
    "building",
    "code",
    "from",
    "have",
    "into",
    "lessons",
    "more",
    "that",
    "their",
    "them",
    "this",
    "using",
    "what",
    "when",
    "where",
    "with",
    "without",
    "your",
}


@dataclass
class Cue:
    start: int
    text: str


@dataclass
class CaptionWindow:
    start: int
    text: str
    words: set[str]
    excerpt: str


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-") or "untitled"


def normalize(value: str) -> str:
    value = html.unescape(value or "").lower()
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def display_hms(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def parse_time(value: str) -> int:
    bits = value.split(".")[0].split(":")
    if len(bits) == 3:
        hours, minutes, seconds = bits
    else:
        hours, minutes, seconds = "0", bits[0], bits[1]
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)


def clean_vtt_text(block: str) -> str:
    block = html.unescape(block)
    block = re.sub(r"<\d\d:\d\d:\d\d\.\d+>", " ", block)
    block = re.sub(r"</?c[^>]*>", " ", block)
    block = re.sub(r"<[^>]+>", " ", block)
    block = block.replace("&gt;&gt;", " ")
    lines = []
    previous = ""
    for raw in block.splitlines():
        line = re.sub(r"\s+", " ", raw).strip()
        if not line or line == previous:
            continue
        previous = line
        lines.append(line)
    return " ".join(lines)


def parse_vtt(path: Path) -> list[Cue]:
    if not path.exists():
        return []
    cues: list[Cue] = []
    text = path.read_text(encoding="utf-8", errors="ignore")
    for block in re.split(r"\n\s*\n", text):
        match = re.search(r"(\d\d:\d\d:\d\d\.\d+|\d\d:\d\d\.\d+)\s+-->\s+(\d\d:\d\d:\d\d\.\d+|\d\d:\d\d\.\d+)", block)
        if not match:
            continue
        cue_text = block[match.end() :]
        if "\n" in cue_text:
            cue_text = cue_text.split("\n", 1)[1]
        cleaned = clean_vtt_text(cue_text)
        if cleaned:
            cues.append(Cue(start=parse_time(match.group(1)), text=cleaned))
    return cues


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    front = text[4:end]
    data: dict[str, object] = {}
    for line in front.splitlines():
        if ":" not in line:
            continue
        key, raw = line.split(":", 1)
        raw = raw.strip()
        try:
            data[key.strip()] = json.loads(raw)
        except json.JSONDecodeError:
            data[key.strip()] = raw.strip('"')
    return data


def load_talks() -> list[dict]:
    talks = []
    for path in sorted((WIKI / "talks").glob("*.md")):
        fm = parse_frontmatter(path)
        date = str(fm.get("date") or "")
        if not date.startswith("2026-"):
            continue
        speakers = fm.get("speakers") or []
        if isinstance(speakers, str):
            speakers = [speakers]
        speaker_names = [str(s) for s in speakers]
        talks.append(
            {
                "slug": path.stem,
                "path": path,
                "title": str(fm.get("title") or path.stem),
                "date": date,
                "time": str(fm.get("time") or ""),
                "track": str(fm.get("track") or ""),
                "room": str(fm.get("room") or ""),
                "speakers": speaker_names,
                "speaker_norms": [normalize(s) for s in speaker_names if normalize(s)],
            }
        )
    return talks


def title_terms(title: str) -> set[str]:
    terms = set()
    for token in normalize(title).split():
        if len(token) < 4 or token in STOPWORDS:
            continue
        terms.add(token)
    return terms


def speaker_score(speaker: str, speaker_norm: str, text: str) -> tuple[int, list[str]]:
    if not speaker_norm:
        return 0, []
    terms = speaker_norm.split()
    if speaker_norm in text:
        return 85, [speaker]
    if len(terms) >= 2 and all(term in text for term in terms):
        return 70, [speaker]
    if speaker_norm == "swyx" and "swyx" in text:
        return 85, [speaker]
    return 0, []


def build_windows(cues: list[Cue]) -> list[CaptionWindow]:
    windows: list[CaptionWindow] = []
    for index, cue in enumerate(cues):
        if index % 3:
            continue
        window_cues = cues[index : index + 40]
        raw = " ".join(item.text for item in window_cues)
        text = normalize(raw)
        if not text:
            continue
        windows.append(CaptionWindow(start=cue.start, text=text, words=set(text.split()), excerpt=raw[:360]))
    return windows


def build_speaker_index(windows: list[CaptionWindow], talks: list[dict]) -> dict[str, list[CaptionWindow]]:
    speaker_norms = sorted({speaker for talk in talks for speaker in talk["speaker_norms"]})
    first_token_index: dict[str, list[str]] = {}
    for speaker in speaker_norms:
        first = speaker.split()[0]
        first_token_index.setdefault(first, []).append(speaker)

    index: dict[str, list[CaptionWindow]] = {speaker: [] for speaker in speaker_norms}
    for window in windows:
        candidates: set[str] = set()
        for word in window.words:
            candidates.update(first_token_index.get(word, []))
        for speaker in candidates:
            parts = speaker.split()
            if speaker == "swyx":
                matched = "swyx" in window.words
            elif speaker in window.text:
                matched = True
            else:
                matched = len(parts) >= 2 and all(part in window.words for part in parts)
            if matched:
                index[speaker].append(window)
    return index


def title_only_match(talk: dict, windows: list[CaptionWindow]) -> dict | None:
    terms = title_terms(talk["title"])
    if len(terms) < 2:
        return None
    best: dict | None = None
    for window in windows:
        overlap = sorted(terms.intersection(window.words))
        if len(overlap) < 3 and " ".join(overlap[:2]) not in window.text:
            continue
        phrase = "lethal trifecta" if {"lethal", "trifecta"}.issubset(terms) else ""
        phrase_points = 95 if phrase and phrase in window.text else 0
        overlap_points = min(len(overlap) * 13, 75)
        score = phrase_points or overlap_points
        if score < 65:
            continue
        candidate = {
            "start_seconds": max(window.start - 10, 0),
            "score": score,
            "matched_speakers": [],
            "matched_title_terms": overlap[:12],
            "evidence_excerpt": window.excerpt,
            "basis": "title phrase",
        }
        if best is None or candidate["score"] > best["score"] or (
            candidate["score"] == best["score"] and candidate["start_seconds"] < best["start_seconds"]
        ):
            best = candidate
    return best


def best_match_for_talk(
    talk: dict,
    windows_by_speaker: dict[str, list[CaptionWindow]],
    all_windows: list[CaptionWindow],
) -> dict | None:
    terms = title_terms(talk["title"])
    best: dict | None = None
    seen_starts: set[int] = set()
    candidate_windows: list[CaptionWindow] = []
    for speaker_norm in talk["speaker_norms"]:
        for window in windows_by_speaker.get(speaker_norm, []):
            if window.start in seen_starts:
                continue
            seen_starts.add(window.start)
            candidate_windows.append(window)

    for window in candidate_windows:
        speaker_points = 0
        matched_speakers: list[str] = []
        for speaker, speaker_norm in zip(talk["speakers"], talk["speaker_norms"]):
            points, labels = speaker_score(speaker, speaker_norm, window.text)
            if points > speaker_points:
                speaker_points = points
                matched_speakers = labels
        if not speaker_points:
            continue
        overlap = sorted(terms.intersection(window.words))
        overlap_points = min(len(overlap) * 7, 45)
        title_phrase_points = 35 if normalize(talk["title"]) in window.text else 0
        score = speaker_points + overlap_points + title_phrase_points
        if score < 90:
            continue
        candidate = {
            "start_seconds": max(window.start - 10, 0),
            "score": score,
            "matched_speakers": matched_speakers,
            "matched_title_terms": overlap[:12],
            "evidence_excerpt": window.excerpt,
            "basis": "speaker and title",
        }
        if best is None or candidate["score"] > best["score"] or (
            candidate["score"] == best["score"] and candidate["start_seconds"] < best["start_seconds"]
        ):
            best = candidate
    return best


def upsert_section(path: Path, heading: str, body: str) -> None:
    text = path.read_text(encoding="utf-8")
    section = f"\n## {heading}\n{body.strip()}\n"
    pattern = re.compile(rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    if pattern.search(text):
        text = pattern.sub(section.rstrip(), text)
    else:
        text = text.rstrip() + section
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def remove_section(path: Path, heading: str) -> None:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    updated = pattern.sub("", text).rstrip() + "\n"
    if updated != text:
        path.write_text(updated, encoding="utf-8")


def write_resource(matches: list[dict]) -> None:
    lines = [
        "---",
        'title: "Livestream Talk Segments"',
        'category: "resources"',
        'sourceLabels: ["YouTube livestream captions", "Official conference schedule"]',
        "---",
        "",
        "# Livestream Talk Segments",
        "",
        "This page lists scheduled talks that were matched to a specific timestamp inside one of the broad AI Engineer World's Fair 2026 livestreams. Matches are generated from local timed YouTube captions and retained only when speaker names and talk-title terms agree in the same caption window.",
        "",
        "Use these as navigational evidence into the livestream, not as a substitute for a cut talk video when a dedicated recording exists.",
        "",
    ]
    by_stream: dict[str, list[dict]] = {}
    for row in matches:
        by_stream.setdefault(row["video_id"], []).append(row)
    for video_id in sorted(by_stream):
        stream_title = STREAMS[video_id]["title"]
        lines.extend(["", f"## {stream_title}", ""])
        for row in sorted(by_stream[video_id], key=lambda item: item["start_seconds"]):
            lines.append(
                f"- [[{row['talk_slug']}|{row['title']}]] — "
                f"[{row['start_hms']}]({row['url']}) "
                f"(score {row['confidence_score']}; matched: {', '.join(row['matched_speakers'] + row['matched_title_terms'])})"
            )
    (WIKI / "resources" / "livestream-talk-segments.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    talks = load_talks()
    for path in (WIKI / "talks").glob("*.md"):
        remove_section(path, "Livestream Segment")
    for path in (WIKI / "people").glob("*.md"):
        remove_section(path, "Livestream Appearances")

    windows_by_stream = {video_id: build_windows(parse_vtt(info["vtt"])) for video_id, info in STREAMS.items()}
    speaker_indexes = {
        video_id: build_speaker_index(windows, talks)
        for video_id, windows in windows_by_stream.items()
    }
    matches = []
    for talk in talks:
        best_stream_id = ""
        best_match = None
        for video_id, stream in STREAMS.items():
            match = best_match_for_talk(talk, speaker_indexes[video_id], windows_by_stream[video_id])
            if not match:
                continue
            if best_match is None or match["score"] > best_match["score"]:
                best_match = match
                best_stream_id = video_id
        if not best_match:
            continue
        stream = STREAMS[best_stream_id]
        match = best_match
        if not match:
            continue
        url = f"https://www.youtube.com/watch?v={stream['video_id']}&t={match['start_seconds']}s"
        row = {
            "talk_slug": talk["slug"],
            "title": talk["title"],
            "date": talk["date"],
            "time": talk["time"],
            "track": talk["track"],
            "room": talk["room"],
            "speakers": talk["speakers"],
            "video_id": stream["video_id"],
            "video_title": stream["title"],
            "start_seconds": match["start_seconds"],
            "start_hms": display_hms(match["start_seconds"]),
            "url": url,
            "confidence": "high",
            "confidence_score": match["score"],
            "matched_speakers": match["matched_speakers"],
            "matched_title_terms": match["matched_title_terms"],
            "match_basis": match["basis"],
            "evidence_excerpt": match["evidence_excerpt"],
        }
        matches.append(row)
        body = "\n".join(
            [
                f"- [Watch in livestream at {row['start_hms']}]({row['url']}) — {row['video_title']}.",
                f"- Match basis: {row['match_basis']}; timed captions matched "
                f"{', '.join(row['matched_speakers'] + row['matched_title_terms'])}.",
                "- Confidence: high automated match; prefer a dedicated cut-video recording when one exists.",
            ]
        )
        upsert_section(talk["path"], "Livestream Segment", body)

    by_person: dict[str, list[dict]] = {}
    for row in matches:
        for speaker in row["speakers"]:
            by_person.setdefault(speaker, []).append(row)

    for speaker, rows in by_person.items():
        path = WIKI / "people" / f"{slugify(speaker)}.md"
        if not path.exists():
            continue
        lines = []
        for row in sorted(rows, key=lambda item: (item["date"], item["start_seconds"])):
            lines.append(
                f"- [[{row['talk_slug']}|{row['title']}]] — "
                f"[watch at {row['start_hms']}]({row['url']}) in {row['video_title']}."
            )
        upsert_section(path, "Livestream Appearances", "\n".join(lines))

    output = RAW / "livestream-talk-segments.json"
    output.write_text(json.dumps(matches, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_resource(matches)
    print(json.dumps({"matches": len(matches), "output": str(output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
