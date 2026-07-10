#!/usr/bin/env python3
"""Monitor the official AI Engineer YouTube channel for WF2026 videos.

This is intentionally project-local. It uses the public YouTube RSS feed for
date-gated discovery because that path exposes stable published dates without
requiring fragile full video extraction. For new official videos, it creates
wiki resource pages immediately, tries captions/transcript import, runs the
existing enrichment/build pipeline where possible, and records pending failures
instead of treating YouTube 429/IP-blocking as fatal.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date, datetime, timezone, timedelta
from pathlib import Path
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "sources"
WIKI = ROOT / "wiki"
STATE_DIR = ROOT / ".ops" / "state" / "youtube-monitor"
STATUS_JSON = STATE_DIR / "status.json"
STATUS_HTML = STATE_DIR / "status.html"
RSS_SNAPSHOT = RAW / "official-youtube-rss-latest.json"
CHANNEL_ID = "UCLKPca3kwwd-B59HNr-_lvA"
CHANNEL_RSS = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
OFFICIAL_CHANNEL = "AI Engineer"


@dataclass
class VideoEntry:
    video_id: str
    title: str
    published: str
    updated: str
    url: str

    @property
    def published_date(self) -> date:
        return datetime.fromisoformat(self.published.replace("Z", "+00:00")).date()


def run(cmd: list[str], *, timeout: int = 600, check: bool = False) -> subprocess.CompletedProcess[str]:
    print("+", " ".join(cmd), flush=True)
    cp = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=timeout)
    if cp.stdout:
        print(cp.stdout[-4000:], flush=True)
    if cp.stderr:
        print(cp.stderr[-4000:], file=sys.stderr, flush=True)
    if check and cp.returncode != 0:
        raise RuntimeError(f"command failed ({cp.returncode}): {' '.join(cmd)}\n{cp.stderr[-2000:]}")
    return cp


def slugify(value: str) -> str:
    value = value.lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def yaml_value(value: object) -> str:
    if isinstance(value, list):
        return "[" + ", ".join(json.dumps(str(item), ensure_ascii=False) for item in value) + "]"
    return json.dumps(str(value), ensure_ascii=False)


def frontmatter(fields: dict[str, object]) -> str:
    lines = ["---"]
    for key, value in fields.items():
        lines.append(f"{key}: {yaml_value(value)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def upsert_section(text: str, heading: str, body: str) -> str:
    block = f"\n## {heading}\n{body.rstrip()}\n"
    pattern = re.compile(rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    if pattern.search(text):
        return pattern.sub(block, text).rstrip() + "\n"
    return text.rstrip() + block


def normalize_title(value: str) -> str:
    value = value.lower()
    value = re.sub(r"@[a-z0-9_.-]+", " ", value)
    value = re.sub(r"\b(ai|the|a|an|and|with|for|to|of|in|on|your|you)\b", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def fetch_rss() -> list[VideoEntry]:
    xml = urlopen(CHANNEL_RSS, timeout=30).read()
    root = ET.fromstring(xml)
    ns = {"atom": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}
    entries: list[VideoEntry] = []
    for entry in root.findall("atom:entry", ns):
        video_id = entry.findtext("yt:videoId", namespaces=ns)
        title = entry.findtext("atom:title", namespaces=ns)
        published = entry.findtext("atom:published", namespaces=ns)
        updated = entry.findtext("atom:updated", namespaces=ns) or published
        if not video_id or not title or not published:
            continue
        entries.append(
            VideoEntry(
                video_id=video_id,
                title=title,
                published=published,
                updated=updated or published,
                url=f"https://www.youtube.com/watch?v={video_id}",
            )
        )
    return entries


def load_json(path: Path, default: object) -> object:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def resource_path(video_id: str) -> Path:
    return WIKI / "resources" / f"youtube-{video_id}.md"


def transcript_path(video_id: str) -> Path:
    return RAW / "youtube-transcripts" / f"{video_id}.txt"


def slides_path(video_id: str) -> Path:
    return WIKI / "slides" / f"youtube-{video_id}-slides.md"


def read_talk_pages() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted((WIKI / "talks").glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        title_match = re.search(r'^title:\s*"?(.+?)"?\s*$', text, re.M)
        speakers_match = re.search(r"^speakers:\s*(.+?)\s*$", text, re.M)
        title = title_match.group(1).strip().strip('"') if title_match else path.stem.replace("-", " ").title()
        speakers = speakers_match.group(1) if speakers_match else ""
        rows.append({"id": path.stem, "path": str(path), "title": title, "speakers": speakers, "text": text})
    return rows


def speaker_tokens(value: str) -> set[str]:
    value = re.sub(r"[\[\]\",]", " ", value)
    tokens = {token.lower() for token in re.findall(r"[A-Za-z][A-Za-z'-]{2,}", value)}
    return {token for token in tokens if token not in {"and", "the", "with", "for", "from"}}


def match_talks(video: VideoEntry, talks: list[dict[str, str]]) -> list[dict[str, str]]:
    video_norm = normalize_title(video.title)
    video_tokens = speaker_tokens(video.title)
    scored: list[tuple[int, dict[str, str]]] = []
    for talk in talks:
        talk_norm = normalize_title(talk["title"])
        score = 0
        if talk_norm and talk_norm in video_norm:
            score += 10
        elif video_norm and video_norm in talk_norm:
            score += 8
        else:
            overlap = set(talk_norm.split()) & set(video_norm.split())
            if len(overlap) >= 4:
                score += len(overlap)
        speaker_overlap = speaker_tokens(talk["speakers"]) & video_tokens
        if speaker_overlap:
            score += min(6, len(speaker_overlap) * 2)
        if score >= 7:
            scored.append((score, talk))
    scored.sort(key=lambda item: (-item[0], item[1]["title"]))
    return [talk for _score, talk in scored[:3]]


def write_resource_page(video: VideoEntry, matched_talks: list[dict[str, str]], transcript_status: str, slide_status: str) -> bool:
    path = resource_path(video.video_id)
    talk_lines = []
    if matched_talks:
        for talk in matched_talks:
            talk_lines.append(f"- [[{talk['id']}|{talk['title']}]]")
    else:
        talk_lines.append("- No exact schedule-page match has been assigned yet; use as official channel media evidence until matched.")
    transcript_line = (
        f"Cached transcript text is available at `raw/sources/youtube-transcripts/{video.video_id}.txt`."
        if transcript_path(video.video_id).exists()
        else f"Transcript import status: {transcript_status}."
    )
    slide_line = f"- [[youtube-{video.video_id}-slides]]" if slides_path(video.video_id).exists() else f"- Slide extraction status: {slide_status}."
    text = "\n".join(
        [
            frontmatter(
                {
                    "title": video.title,
                    "category": "resources",
                    "sourceLabels": ["Official AI Engineer YouTube channel", "Public YouTube RSS metadata"],
                    "videoId": video.video_id,
                    "publishedDate": video.published_date.isoformat(),
                    "last_enriched": datetime.now(timezone.utc).isoformat(),
                }
            ).rstrip(),
            f"# {video.title}",
            "",
            "## What It Is",
            "An official AI Engineer YouTube video connected to AI Engineer World's Fair 2026 monitoring. This is a public media source; official schedule pages remain canonical for schedule metadata.",
            "",
            "## Source Classification",
            "- Source role: official AI Engineer YouTube channel media evidence.",
            f"- Published date: {video.published_date.isoformat()}",
            f"- Channel/source: {OFFICIAL_CHANNEL}.",
            "- Use: evidence for what the published recording, transcript, and captured slides show. Keep schedule facts tied to the official schedule pages.",
            "",
            "## Matched Schedule Pages",
            *talk_lines,
            "",
            "## Transcript Status",
            transcript_line,
            "",
            "## Extracted Slides",
            slide_line,
            "",
            "## Link",
            f"[YouTube]({video.url})",
        ]
    )
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if old == text + "\n":
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text + "\n", encoding="utf-8")
    return True


def update_talk_pages(video: VideoEntry, matched_talks: list[dict[str, str]]) -> int:
    updated = 0
    transcript_bits = []
    if transcript_path(video.video_id).exists():
        transcript_bits.append(f"[[youtube-{video.video_id}-transcript]]")
    if slides_path(video.video_id).exists():
        transcript_bits.append(f"[[youtube-{video.video_id}-slides]]")
    evidence = "; ".join(transcript_bits) if transcript_bits else "transcript/slide enrichment pending"
    body = "\n".join(
        [
            f"- [[youtube-{video.video_id}]] — official AI Engineer YouTube channel recording published {video.published_date.isoformat()}.",
            f"- Evidence status: {evidence}.",
            "- Boundary: use this recording as media evidence; keep date/time/room facts tied to the official schedule.",
        ]
    )
    for talk in matched_talks:
        path = Path(talk["path"])
        text = path.read_text(encoding="utf-8")
        new_text = upsert_section(text, "Official YouTube Recording", body)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
    return updated


def yt_dlp_js_runtime_arg() -> str:
    node = shutil.which("node")
    if not node:
        for candidate in sorted(Path("/home/dylan/.nvm/versions/node").glob("*/bin/node"), reverse=True):
            if candidate.exists():
                node = str(candidate)
                break
    return f"node:{node}" if node else "node"


def vtt_to_text(path: Path) -> str:
    lines: list[str] = []
    seen: set[str] = set()
    for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.strip()
        if not line or line == "WEBVTT" or "-->" in line or line.isdigit() or line.startswith(("Kind:", "Language:")):
            continue
        line = re.sub(r"<[^>]+>", "", line)
        line = re.sub(r"\s+", " ", line).strip()
        if line and line not in seen:
            seen.add(line)
            lines.append(line)
    return " ".join(lines)


def try_import_captions(video: VideoEntry) -> dict[str, object]:
    if transcript_path(video.video_id).exists():
        return {"status": "already_cached", "path": str(transcript_path(video.video_id).relative_to(ROOT))}
    subtitle_dir = RAW / "youtube-subtitles"
    subtitle_dir.mkdir(parents=True, exist_ok=True)
    before = set(subtitle_dir.glob(f"{video.video_id}*.vtt"))
    cp = run(
        [
            "yt-dlp",
            "--js-runtimes",
            yt_dlp_js_runtime_arg(),
            "--remote-components",
            "ejs:github",
            "--skip-download",
            "--write-subs",
            "--write-auto-subs",
            "--sub-langs",
            "en.*",
            "--sub-format",
            "vtt",
            "-o",
            str(subtitle_dir / f"{video.video_id}.%(ext)s"),
            video.url,
        ],
        timeout=360,
    )
    if cp.returncode != 0:
        chrome = try_import_captions_with_chrome_agent(video)
        if chrome.get("status") == "captions_imported":
            return chrome
        chrome["yt_dlp_error"] = (cp.stderr or cp.stdout)[-1600:]
        return chrome
    after = set(subtitle_dir.glob(f"{video.video_id}*.vtt"))
    candidates = sorted(after - before) or sorted(after)
    if not candidates:
        return {"status": "no_captions_found"}
    text = vtt_to_text(candidates[0]).strip()
    if not text:
        return {"status": "empty_caption_file", "caption_path": str(candidates[0].relative_to(ROOT))}
    target = transcript_path(video.video_id)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text + "\n", encoding="utf-8")
    return {
        "status": "captions_imported",
        "path": str(target.relative_to(ROOT)),
        "caption_path": str(candidates[0].relative_to(ROOT)),
        "word_count": len(text.split()),
    }


def try_import_captions_with_chrome_agent(video: VideoEntry) -> dict[str, object]:
    chrome_project = Path("/garage/projects/agents/chrome-agent-python")
    helper = ROOT / "scripts" / "extract_youtube_caption_with_chrome_agent.py"
    if not chrome_project.exists() or not helper.exists():
        return {"status": "chrome_agent_unavailable"}
    target = transcript_path(video.video_id)
    cp = subprocess.run(
        [
            "uv",
            "run",
            "python",
            str(helper),
            "--video-id",
            video.video_id,
            "--output",
            str(target),
        ],
        cwd=chrome_project,
        text=True,
        capture_output=True,
        timeout=120,
    )
    if cp.stdout:
        print(cp.stdout[-4000:], flush=True)
    if cp.stderr:
        print(cp.stderr[-4000:], file=sys.stderr, flush=True)
    if cp.returncode != 0 or not target.exists():
        return {"status": "chrome_caption_import_failed", "error": (cp.stderr or cp.stdout)[-1600:]}
    text = target.read_text(encoding="utf-8", errors="ignore")
    return {"status": "captions_imported", "path": str(target.relative_to(ROOT)), "source": "chrome_agent", "word_count": len(text.split())}


def try_extract_slides(video: VideoEntry, matched_talks: list[dict[str, str]], *, enabled: bool) -> dict[str, object]:
    if slides_path(video.video_id).exists():
        return {"status": "already_extracted", "path": str(slides_path(video.video_id).relative_to(ROOT))}
    if not enabled:
        return {"status": "skipped_by_configuration"}
    cmd = [sys.executable, "scripts/extract_video_slides.py", "--scene-detect", "--video-id", video.video_id, "--max-slides", "32"]
    cp = run(cmd, timeout=1500)
    if cp.returncode != 0:
        return {"status": "slide_extraction_failed", "error": (cp.stderr or cp.stdout)[-1600:]}
    return {"status": "slide_extraction_ran", "path": str(slides_path(video.video_id).relative_to(ROOT)) if slides_path(video.video_id).exists() else ""}


def update_channel_snapshot(entries: list[VideoEntry]) -> None:
    payload = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "channel_id": CHANNEL_ID,
        "source_url": CHANNEL_RSS,
        "entries": [
            {
                "id": entry.video_id,
                "title": entry.title,
                "url": entry.url,
                "published": entry.published,
                "published_date": entry.published_date.isoformat(),
                "updated": entry.updated,
                "channel": OFFICIAL_CHANNEL,
                "source": "official_youtube_rss",
            }
            for entry in entries
        ],
    }
    write_json(RSS_SNAPSHOT, payload)


def run_enrichment(imported_transcripts: int) -> list[dict[str, object]]:
    commands: list[list[str]] = []
    if imported_transcripts:
        commands.extend(
            [
                [sys.executable, "scripts/generate_transcript_markdown_pages.py"],
                [sys.executable, "scripts/enrich_from_youtube_transcripts.py"],
                [sys.executable, "scripts/generate_talk_synthesis.py", "--all"],
                [sys.executable, "scripts/generate_tool_inventory.py"],
                [sys.executable, "scripts/generate_question_layer.py"],
                [sys.executable, "scripts/generate_highlights.py"],
                [sys.executable, "scripts/generate_synthesis_layers.py"],
            ]
        )
    commands.extend(
        [
            [sys.executable, "scripts/normalize_article_shapes.py"],
            ["npm", "run", "build"],
        ]
    )
    results = []
    for cmd in commands:
        cp = run(cmd, timeout=1800)
        results.append({"cmd": cmd, "returncode": cp.returncode})
        if cp.returncode != 0:
            break
    return results


def maybe_commit_and_push(enabled: bool, message: str) -> dict[str, object]:
    if not enabled:
        return {"enabled": False}
    status = run(["git", "status", "--porcelain"], timeout=60)
    if not status.stdout.strip():
        return {"enabled": True, "changed": False}
    add_paths = [path for path in ["raw", "wiki", "scripts", "package.json", "package-lock.json"] if (ROOT / path).exists()]
    run(["git", "add", *add_paths], timeout=120)
    staged = run(["git", "diff", "--cached", "--quiet"], timeout=60)
    if staged.returncode == 0:
        return {"enabled": True, "changed": False, "note": "no publishable staged changes"}
    commit = run(["git", "commit", "-m", message], timeout=120)
    if commit.returncode != 0:
        return {"enabled": True, "changed": True, "commit_returncode": commit.returncode, "error": commit.stderr[-1000:]}
    push = run(["git", "push", "origin", "main"], timeout=300)
    return {"enabled": True, "changed": True, "commit_returncode": commit.returncode, "push_returncode": push.returncode}


def write_status(report: dict[str, object]) -> None:
    write_json(STATUS_JSON, report)
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    for item in report.get("processed", []) or []:
        rows.append(
            "<tr>"
            f"<td>{html.escape(str(item.get('published_date', '')))}</td>"
            f"<td><code>{html.escape(str(item.get('id', '')))}</code></td>"
            f"<td>{html.escape(str(item.get('title', '')))}</td>"
            f"<td>{html.escape(str(item.get('resource_status', '')))}</td>"
            f"<td>{html.escape(str((item.get('transcript') or {}).get('status', '')))}</td>"
            f"<td>{html.escape(str((item.get('slides') or {}).get('status', '')))}</td>"
            "</tr>"
        )
    STATUS_HTML.write_text(
        f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>AIE WF2026 YouTube monitor status</title>
<style>
body {{ font: 16px/1.5 system-ui, sans-serif; margin: 40px; color: #17202a; background: #f7f8f4; }}
main {{ max-width: 1080px; background: #fff; border: 1px solid #d9ded6; border-radius: 12px; padding: 28px; }}
code {{ background: #eef2ec; padding: 2px 5px; border-radius: 4px; }}
table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
th, td {{ text-align: left; border-bottom: 1px solid #d9ded6; padding: 8px; vertical-align: top; }}
.state {{ color: #0f766e; font-weight: 800; }}
</style>
</head>
<body>
<main>
<p class="state">{html.escape(str(report.get('state')))}</p>
<h1>AIE WF2026 YouTube monitor</h1>
<p>Checked at: <code>{html.escape(str(report.get('checked_at')))}</code></p>
<p>Latest official video date: <code>{html.escape(str(report.get('latest_published_date')))}</code>; active cutoff date: <code>{html.escape(str(report.get('active_cutoff_date')))}</code>.</p>
<p>{html.escape(str(report.get('message', '')))}</p>
<table>
<thead><tr><th>Date</th><th>ID</th><th>Title</th><th>Resource</th><th>Transcript</th><th>Slides</th></tr></thead>
<tbody>{''.join(rows) or '<tr><td colspan="6">No newly processed videos in this run.</td></tr>'}</tbody>
</table>
</main>
</body>
</html>
""",
        encoding="utf-8",
    )


def open_status_page() -> None:
    if not os.environ.get("DISPLAY"):
        return
    opener = shutil.which("xdg-open") or shutil.which("firefox")
    if opener:
        subprocess.Popen([opener, str(STATUS_HTML)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def stop_timer_if_present() -> None:
    if shutil.which("systemctl"):
        subprocess.run(["systemctl", "--user", "disable", "--now", "aie-wf2026-youtube-monitor.timer"], text=True, capture_output=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-slides", action="store_true", help="Skip slide extraction attempts for new videos.")
    parser.add_argument("--auto-push", action="store_true", help="Commit and push successful import changes to origin/main.")
    parser.add_argument("--open-status", action="store_true", help="Open the status page after this run.")
    args = parser.parse_args()

    checked_at = datetime.now(timezone.utc)
    entries = fetch_rss()
    update_channel_snapshot(entries)
    today = checked_at.date()
    cutoff = today - timedelta(days=6)
    latest_date = max((entry.published_date for entry in entries), default=None)

    report: dict[str, object] = {
        "checked_at": checked_at.isoformat(),
        "channel_id": CHANNEL_ID,
        "active_cutoff_date": cutoff.isoformat(),
        "latest_published_date": latest_date.isoformat() if latest_date else "",
        "processed": [],
        "dry_run": args.dry_run,
    }

    if latest_date is None or latest_date < cutoff:
        report.update(
            {
                "state": "stopped",
                "message": "No official AI Engineer video was published within the last seven calendar dates; monitor disabled.",
            }
        )
        write_status(report)
        stop_timer_if_present()
        open_status_page()
        return 0

    talks = read_talk_pages()
    recent = [entry for entry in entries if entry.published_date >= cutoff]
    new_entries = [entry for entry in recent if not resource_path(entry.video_id).exists()]
    processed: list[dict[str, object]] = []
    transcript_imports = 0

    for entry in new_entries:
        matched = match_talks(entry, talks)
        transcript = {"status": "dry_run"}
        slides = {"status": "dry_run"}
        resource_status = "dry_run"
        talk_updates = 0
        if not args.dry_run:
            transcript = try_import_captions(entry)
            if transcript.get("status") == "captions_imported":
                transcript_imports += 1
            slides = try_extract_slides(entry, matched, enabled=not args.no_slides and os.environ.get("AIE_WF2026_MONITOR_SKIP_SLIDES") != "1")
            resource_changed = write_resource_page(entry, matched, str(transcript.get("status")), str(slides.get("status")))
            talk_updates = update_talk_pages(entry, matched)
            resource_status = "created_or_updated" if resource_changed else "unchanged"
        processed.append(
            {
                "id": entry.video_id,
                "title": entry.title,
                "url": entry.url,
                "published": entry.published,
                "published_date": entry.published_date.isoformat(),
                "matched_talks": [{"id": talk["id"], "title": talk["title"]} for talk in matched],
                "resource_status": resource_status,
                "talk_updates": talk_updates,
                "transcript": transcript,
                "slides": slides,
            }
        )

    report["processed"] = processed
    if not args.dry_run:
        enrichment = run_enrichment(transcript_imports)
        report["enrichment"] = enrichment
        auto_push = args.auto_push or os.environ.get("AIE_WF2026_MONITOR_AUTO_PUSH") == "1"
        report["publish"] = maybe_commit_and_push(auto_push, "Import new official AI Engineer YouTube videos")

    report.update(
        {
            "state": "active",
            "message": f"Official videos are still being published within the last seven calendar dates. Processed {len(processed)} new RSS entries; monitor remains active.",
            "recent_entry_count": len(recent),
            "new_entry_count": len(new_entries),
        }
    )
    write_status(report)
    if args.open_status:
        open_status_page()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
