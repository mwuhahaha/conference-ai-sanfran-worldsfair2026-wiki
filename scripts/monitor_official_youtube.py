#!/usr/bin/env python3
"""Monitor the official AI Engineer YouTube channel for WF2026 videos.

This is intentionally project-local. Recurring discovery reconciles the
owner-validated official WF26 playlist with date-gated RSS/channel candidates.
For new official videos, it creates wiki resource pages immediately, tries
captions/transcript import, hands the result to the checked-in wiki-maker update
profile, and records pending failures instead of treating YouTube 429/IP-blocking
as fatal.
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
import time
import traceback
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date, datetime, timezone
from hashlib import sha256
from pathlib import Path
from urllib.request import Request, urlopen
from uuid import uuid4


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "sources"
WIKI = ROOT / "wiki"
STATE_DIR = ROOT / ".ops" / "state" / "youtube-monitor"
STATUS_JSON = STATE_DIR / "status.json"
STATUS_HTML = STATE_DIR / "status.html"
TRANSACTION_JOURNAL = STATE_DIR / "mutation-transaction.json"
TRANSACTION_BACKUPS = STATE_DIR / "mutation-transaction"
PUBLISH_SYNC_JOURNAL = STATE_DIR / "publish-sync.json"
RSS_SNAPSHOT = RAW / "official-youtube-rss-latest.json"
OFFICIAL_VIDEO_MANIFEST = RAW / "official-wf26-video-manifest.json"
CHANNEL_ID = "UCLKPca3kwwd-B59HNr-_lvA"
CHANNEL_RSS = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
OFFICIAL_CHANNEL = "AI Engineer"
OFFICIAL_PLAYLIST_ID = "PLDyBmFH9HlVc"
OFFICIAL_PLAYLIST_URL = f"https://www.youtube.com/playlist?list={OFFICIAL_PLAYLIST_ID}"
WF26_EVENT_START_DATE = date(2026, 6, 29)
WF26_NON_PLAYLIST_MEDIA_END_DATE = date(2026, 12, 31)
OFFICIAL_PLAYLIST_BASELINE_IDS = (
    "iCj_ATyThvc",
    "ZSQb5fzRFPw",
    "q4Tr-DknG2M",
    "uU5Gv2h8-9g",
    "8G_1-3IO4ZQ",
    "0vphxNt4wyk",
    "APqXGyCoGW4",
    "n97BCfyFIvw",
    "c35YoMdnI78",
    "-CnA2lGfymY",
    "OqM67QG_Ikk",
    "V-EDrhIhHzQ",
    "KB41dTlX1Uc",
    "uIiA6DquRiE",
    "1P1hJ36rxM0",
    "YZQsWVeN3rE",
    "Cz4v1WHVyZc",
    "RGSFUqzqErE",
    "ZyIoTOAbRfs",
    "VrpEyglYgeU",
    "WkBPX-oDMnA",
    "ZpK5PWX2YRM",
    "pMggiOb18tc",
    "xUnRQ9vLXxo",
    "Z2Erdirpudo",
    "eBUyTS7SzV4",
    "9fubhllmsBU",
    "Z3fP-eMEx-8",
    "PXXNCtfKZs0",
)
OFFICIAL_PLAYLIST_SCHEDULE_OVERRIDES = {
    "1EZdpEhwmNc": (
        "2026-06-29-manoj-nair-through-the-ai-fog-the-architectural-decision-the-next-24-months-of-agentic-security-depends-on",
    ),
    "YnNF55QV0zs": (
        "2026-06-30-ishan-anand-will-ai-predict-people-like-we-predict-the-weather-alternate-title-a-field-guide-to-synthetic-personas-for-market-research",
    ),
    "xUnRQ9vLXxo": ("2026-07-01-theo-browne-closing-keynote-theo-browne",),
}
EXPLICIT_WF26_OFFICIAL_LIVESTREAM_IDS = frozenset(
    {
        "4sX_He5c4sI",
        "I2cbIws9j10",
        "htM02KMNZnk",
    }
)
CAPTION_FAILURE_STATUSES = {
    "chrome_agent_unavailable",
    "chrome_caption_import_failed",
    "empty_caption_file",
}
SLIDE_FAILURE_STATUSES = {"slide_extraction_failed"}
WIKI_MAKER_ENV = "WIKI_FROM_TOPIC_MAKER"
WIKI_MAKER_REPLAN_REQUIRED = (
    "update inputs changed after the deterministic plan; plan again"
)
PLAYABLE_MEDIA_TYPES = {"event_livestream", "talk_recording"}
NO_SLIDES_STATUS = "no_slides"
NO_SLIDES_PATTERNS = (
    re.compile(r"\b(?:i|we)\s+(?:have|had)\s+no\s+(?:slides?|slide\s+deck)\b", re.I),
    re.compile(r"\b(?:i|we)\s+(?:do\s+not|don't)\s+have\s+(?:any\s+)?slides?\b", re.I),
    re.compile(r"\bthere(?:'s|\s+is)\s+no\s+(?:slides?|slide\s+deck)\b", re.I),
)


@dataclass
class VideoEntry:
    video_id: str
    title: str
    published: str
    updated: str
    url: str
    description: str = ""
    live_status: str = ""
    release_date: str = ""
    has_english_captions: bool = False
    channel_id: str = ""
    availability: str = ""

    @property
    def published_date(self) -> date:
        return datetime.fromisoformat(self.published.replace("Z", "+00:00")).date()


@dataclass(frozen=True)
class PlaylistEntry:
    video_id: str
    playlist_index: int
    playlist_title: str
    availability: str
    video: VideoEntry | None
    matched_talks: tuple[dict[str, str], ...] = ()
    metadata_error: str = ""


def run(
    cmd: list[str],
    *,
    timeout: int = 600,
    check: bool = False,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    print("+", " ".join(cmd), flush=True)
    cp = subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=timeout,
        env=env,
    )
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


def generated_recording_block_pattern(video_id: str) -> re.Pattern[str]:
    """Match only the three lines emitted by ``update_talk_pages`` for a video."""

    return re.compile(
        rf"(?m)^- \[\[youtube-{re.escape(video_id)}(?:\|[^\]\n]+)?\]\][^\n]*\n"
        r"^- Evidence status:[^\n]*\n"
        r"^- Boundary:[^\n]*(?:\n|\Z)"
    )


def reconcile_official_recording_section(
    text: str, video_id: str, generated_body: str | None
) -> str:
    """Reconcile one generated video block without overwriting manual section content."""

    section_pattern = re.compile(
        r"(?m)(?P<prefix>^|\n)## Official YouTube Recording\n"
        r"(?P<body>.*?)(?=\n## |\Z)",
        re.S,
    )
    section = section_pattern.search(text)
    if not section:
        if generated_body is None:
            return text
        return text.rstrip() + f"\n\n## Official YouTube Recording\n{generated_body.rstrip()}\n"

    existing_body = section.group("body")
    remaining_body = generated_recording_block_pattern(video_id).sub("", existing_body)
    if generated_body is not None:
        remaining_body = remaining_body.rstrip()
        separator = "\n\n" if remaining_body else ""
        replacement_body = f"{remaining_body}{separator}{generated_body.rstrip()}\n"
    elif remaining_body.strip():
        replacement_body = remaining_body
    else:
        replacement_body = ""

    if replacement_body:
        replacement = (
            f"{section.group('prefix')}## Official YouTube Recording\n{replacement_body}"
        )
    else:
        replacement = "" if section.group("prefix") == "" else "\n"
    return text[: section.start()] + replacement + text[section.end() :]


def normalize_title(value: str) -> str:
    value = value.lower()
    value = re.sub(r"@[a-z0-9_.-]+", " ", value)
    value = re.sub(r"\b(ai|the|a|an|and|with|for|to|of|in|on|your|you)\b", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def fetch_rss(attempts: int = 3) -> list[VideoEntry]:
    if attempts < 1:
        raise ValueError("attempts must be at least 1")

    errors: list[str] = []
    for attempt in range(1, attempts + 1):
        try:
            request = Request(CHANNEL_RSS, headers={"User-Agent": "AIE-WF2026-Wiki-Monitor/1.0"})
            xml = urlopen(request, timeout=30).read()
            root = ET.fromstring(xml)
            break
        except Exception as exc:  # Network and feed errors are retried together.
            errors.append(f"attempt {attempt}: {type(exc).__name__}: {exc}")
            if attempt < attempts:
                time.sleep(2 ** attempt)
    else:
        raise RuntimeError("official YouTube RSS fetch failed after retries: " + "; ".join(errors))

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


def _atomic_write_bytes(path: Path, value: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp-{uuid4().hex}")
    try:
        temporary.write_bytes(value)
        os.replace(temporary, path)
    finally:
        if temporary.exists() or temporary.is_symlink():
            temporary.unlink()


def _remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


class MonitorMutationTransaction:
    """Durably restore monitor-owned canonical mutations after a failed run."""

    SCHEMA_VERSION = 1

    def __init__(self, root: Path, state_dir: Path, payload: dict[str, object] | None = None):
        self.root = Path(os.path.abspath(root))
        self.state_dir = Path(os.path.abspath(state_dir))
        self.journal_path = self.state_dir / TRANSACTION_JOURNAL.name
        self.backup_root = self.state_dir / TRANSACTION_BACKUPS.name
        self.payload = payload or {
            "schemaVersion": self.SCHEMA_VERSION,
            "status": "active",
            "root": str(self.root),
            "startedAt": datetime.now(timezone.utc).isoformat(),
            "pathSnapshots": {},
            "rootSnapshots": {},
            "globSnapshots": {},
            "nextSnapshotOrder": 1,
        }

    @classmethod
    def load(cls, root: Path, state_dir: Path) -> "MonitorMutationTransaction | None":
        journal = Path(state_dir) / TRANSACTION_JOURNAL.name
        if not journal.is_file():
            return None
        payload = json.loads(journal.read_text(encoding="utf-8"))
        if not isinstance(payload, dict) or payload.get("schemaVersion") != cls.SCHEMA_VERSION:
            raise RuntimeError("unsupported monitor mutation transaction journal")
        transaction = cls(root, state_dir, payload)
        if payload.get("root") != str(transaction.root):
            raise RuntimeError("monitor mutation transaction root does not match this checkout")
        return transaction

    def _relative(self, path: Path) -> str:
        absolute = Path(os.path.abspath(path))
        try:
            relative = absolute.relative_to(self.root)
        except ValueError as exc:
            raise ValueError(f"transaction path escapes the project root: {path}") from exc
        return relative.as_posix()

    def _persist(self) -> None:
        self.state_dir.mkdir(parents=True, exist_ok=True)
        _atomic_write_bytes(
            self.journal_path,
            (json.dumps(self.payload, indent=2, sort_keys=True) + "\n").encode("utf-8"),
        )

    def _backup_path(self, namespace: str, relative: str) -> Path:
        digest = sha256(relative.encode("utf-8")).hexdigest()
        return self.backup_root / namespace / digest

    def _next_snapshot_order(self) -> int:
        order = int(self.payload.get("nextSnapshotOrder", 1))
        self.payload["nextSnapshotOrder"] = order + 1
        return order

    def _snapshot(self, path: Path, backup: Path) -> dict[str, object]:
        if path.is_symlink():
            return {"kind": "symlink", "target": os.readlink(path)}
        if path.is_file():
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, backup)
            return {"kind": "file", "backup": str(backup.relative_to(self.state_dir))}
        if path.is_dir():
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(path, backup, symlinks=True)
            return {"kind": "directory", "backup": str(backup.relative_to(self.state_dir))}
        return {"kind": "missing"}

    def track_path(self, path: Path) -> None:
        absolute = Path(os.path.abspath(path))
        if absolute == self.state_dir or self.state_dir in absolute.parents:
            return
        relative = self._relative(absolute)
        snapshots = self.payload["pathSnapshots"]
        assert isinstance(snapshots, dict)
        if relative in snapshots:
            return
        order = self._next_snapshot_order()
        snapshots[relative] = {"status": "preparing", "order": order}
        self._persist()
        snapshot = self._snapshot(
            absolute, self._backup_path("paths", relative)
        )
        snapshots[relative] = {"status": "ready", "order": order, **snapshot}
        self._persist()

    def track_glob(self, parent: Path, pattern: str) -> None:
        relative_parent = self._relative(parent)
        key = f"{relative_parent}\0{pattern}"
        globs = self.payload["globSnapshots"]
        assert isinstance(globs, dict)
        if key in globs:
            return
        baseline = []
        for path in sorted(parent.glob(pattern)) if parent.is_dir() else []:
            self.track_path(path)
            baseline.append(self._relative(path))
        globs[key] = {
            "parent": relative_parent,
            "pattern": pattern,
            "baseline": baseline,
        }
        self._persist()

    def backup_canonical_root(self, path: Path) -> None:
        relative = self._relative(path)
        snapshots = self.payload["rootSnapshots"]
        assert isinstance(snapshots, dict)
        if relative in snapshots:
            return
        order = self._next_snapshot_order()
        snapshots[relative] = {"status": "preparing", "order": order}
        self._persist()
        snapshot = self._snapshot(path, self._backup_path("roots", relative))
        snapshots[relative] = {"status": "ready", "order": order, **snapshot}
        self._persist()

    def _restore_snapshot(self, path: Path, snapshot: dict[str, object]) -> None:
        kind = snapshot.get("kind")
        if kind == "missing":
            _remove_path(path)
            return
        if kind == "symlink":
            _remove_path(path)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.symlink_to(str(snapshot["target"]))
            return
        backup = self.state_dir / str(snapshot["backup"])
        if kind == "file":
            _atomic_write_bytes(path, backup.read_bytes())
            shutil.copystat(backup, path, follow_symlinks=False)
            return
        if kind != "directory":
            raise RuntimeError(f"unsupported transaction snapshot kind: {kind}")
        replacement = path.with_name(f".{path.name}.rollback-{uuid4().hex}")
        displaced = path.with_name(f".{path.name}.displaced-{uuid4().hex}")
        shutil.copytree(backup, replacement, symlinks=True)
        try:
            if path.exists() or path.is_symlink():
                os.replace(path, displaced)
            os.replace(replacement, path)
            _remove_path(displaced)
        except Exception:
            if not (path.exists() or path.is_symlink()) and (
                displaced.exists() or displaced.is_symlink()
            ):
                os.replace(displaced, path)
            raise
        finally:
            _remove_path(replacement)

    def rollback(self) -> dict[str, object]:
        errors: list[str] = []
        restored: list[str] = []
        glob_snapshots = self.payload.get("globSnapshots", {})
        if isinstance(glob_snapshots, dict):
            for snapshot in glob_snapshots.values():
                if not isinstance(snapshot, dict):
                    continue
                parent = self.root / str(snapshot.get("parent") or "")
                pattern = str(snapshot.get("pattern") or "")
                baseline = set(snapshot.get("baseline") or [])
                try:
                    for path in sorted(parent.glob(pattern)) if parent.is_dir() else []:
                        if self._relative(path) not in baseline:
                            _remove_path(path)
                except Exception as exc:
                    errors.append(f"glob {parent}/{pattern}: {exc}")

        # Overlapping snapshots are restored newest-first so the earliest
        # observed baseline wins. This handles both a directly tracked path
        # followed by a root snapshot and a late path snapshot taken after an
        # external adapter mutated an already tracked root.
        snapshot_restores: list[
            tuple[int, int, str, dict[str, object]]
        ] = []
        path_snapshots = self.payload.get("pathSnapshots", {})
        if isinstance(path_snapshots, dict):
            for relative, snapshot in path_snapshots.items():
                if not isinstance(snapshot, dict) or snapshot.get("status") != "ready":
                    continue
                snapshot_restores.append(
                    (int(snapshot.get("order", 0)), 0, relative, snapshot)
                )
        root_snapshots = self.payload.get("rootSnapshots", {})
        if isinstance(root_snapshots, dict):
            for relative, snapshot in root_snapshots.items():
                if not isinstance(snapshot, dict) or snapshot.get("status") != "ready":
                    continue
                snapshot_restores.append(
                    (int(snapshot.get("order", 0)), 1, relative, snapshot)
                )
        for _order, _root_tiebreaker, relative, snapshot in sorted(
            snapshot_restores,
            reverse=True,
        ):
            try:
                self._restore_snapshot(self.root / relative, snapshot)
                restored.append(relative)
            except Exception as exc:
                errors.append(f"{relative}: {exc}")

        self.payload["status"] = "rollback_failed" if errors else "rolled_back"
        self.payload["rolledBackAt"] = datetime.now(timezone.utc).isoformat()
        self.payload["rollbackErrors"] = errors
        if errors:
            self._persist()
        else:
            self._cleanup()
        return {
            "status": self.payload["status"],
            "restoredPathCount": len(set(restored)),
            "errors": errors,
        }

    def commit(self) -> None:
        self._cleanup()

    def _cleanup(self) -> None:
        if self.journal_path.exists():
            self.journal_path.unlink()
        if self.backup_root.exists():
            shutil.rmtree(self.backup_root)


_ACTIVE_TRANSACTION: MonitorMutationTransaction | None = None


def begin_monitor_transaction() -> MonitorMutationTransaction:
    global _ACTIVE_TRANSACTION
    if _ACTIVE_TRANSACTION is not None:
        raise RuntimeError("a monitor mutation transaction is already active")
    _ACTIVE_TRANSACTION = MonitorMutationTransaction(ROOT, STATE_DIR)
    return _ACTIVE_TRANSACTION


def recover_monitor_transaction() -> dict[str, object] | None:
    transaction = MonitorMutationTransaction.load(ROOT, STATE_DIR)
    if transaction is None:
        return None
    return transaction.rollback()


def commit_recovered_monitor_transaction() -> dict[str, object] | None:
    transaction = MonitorMutationTransaction.load(ROOT, STATE_DIR)
    if transaction is None:
        return None
    transaction.commit()
    return {"status": "committed_after_verified_publish"}


def finish_monitor_transaction(transaction: MonitorMutationTransaction) -> None:
    global _ACTIVE_TRANSACTION
    transaction.commit()
    if _ACTIVE_TRANSACTION is transaction:
        _ACTIVE_TRANSACTION = None


def rollback_monitor_transaction(
    transaction: MonitorMutationTransaction,
) -> dict[str, object]:
    global _ACTIVE_TRANSACTION
    result = transaction.rollback()
    if _ACTIVE_TRANSACTION is transaction:
        _ACTIVE_TRANSACTION = None
    return result


def write_text(path: Path, value: str, *, encoding: str = "utf-8") -> None:
    if _ACTIVE_TRANSACTION is not None:
        _ACTIVE_TRANSACTION.track_path(path)
    _atomic_write_bytes(path, value.encode(encoding))


def remove_path(path: Path) -> None:
    if _ACTIVE_TRANSACTION is not None:
        _ACTIVE_TRANSACTION.track_path(path)
    _remove_path(path)


def write_json(path: Path, payload: object) -> None:
    write_text(
        path,
        json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
    )


def resource_path(video_id: str) -> Path:
    return WIKI / "resources" / f"youtube-{video_id}.md"


def transcript_path(video_id: str) -> Path:
    return RAW / "youtube-transcripts" / f"{video_id}.txt"


def slides_path(video_id: str) -> Path:
    return WIKI / "slides" / f"youtube-{video_id}-slides.md"


def resource_schedule_projection_needed(
    video_id: str, matched_talks: list[dict[str, str]]
) -> bool:
    path = resource_path(video_id)
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="ignore")
    if matched_talks:
        return any(f"[[{talk['id']}" not in text for talk in matched_talks)
    section = re.search(r"^## Matched Schedule Pages\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return bool(section and re.search(r"^- \[\[[^\]]+\]\]", section.group(1), re.M))


def resource_playlist_projection_needed(video_id: str) -> bool:
    """Return whether an existing resource omits its canonical playlist boundary."""

    path = resource_path(video_id)
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="ignore")
    return "Official WF26 playlist membership" not in text


def talk_page_projection_needed(
    video_id: str, matched_talks: list[dict[str, str]]
) -> bool:
    desired_paths = {Path(talk["path"]) for talk in matched_talks}
    candidate_paths = desired_paths | set((WIKI / "talks").glob("*.md"))
    pattern = generated_recording_block_pattern(video_id)
    for path in candidate_paths:
        if not path.exists():
            continue
        has_generated_block = bool(pattern.search(path.read_text(encoding="utf-8", errors="ignore")))
        if has_generated_block != (path in desired_paths):
            return True
    return False


def frontmatter_speaker_names(text: str) -> list[str]:
    match = re.search(r"^speakers:[ \t]*(.*)$", text, re.M)
    if not match:
        return []
    inline = match.group(1).strip()
    if inline:
        return parse_speaker_names(inline)
    tail = text[match.end() :]
    names: list[str] = []
    for line in tail.splitlines():
        item = re.match(r"^[ \t]+-[ \t]+(.+?)\s*$", line)
        if item:
            names.append(item.group(1).strip().strip('"\''))
            continue
        if line.strip():
            break
    return names


def read_talk_pages() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted((WIKI / "talks").glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        title_match = re.search(r'^title:\s*"?(.+?)"?\s*$', text, re.M)
        description_match = re.search(r"^## Session Description\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        title = title_match.group(1).strip().strip('"') if title_match else path.stem.replace("-", " ").title()
        speakers = json.dumps(frontmatter_speaker_names(text), ensure_ascii=False)
        rows.append(
            {
                "id": path.stem,
                "path": str(path),
                "title": title,
                "speakers": speakers,
                "description": description_match.group(1).strip() if description_match else "",
                "text": text,
            }
        )
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
        title_overlap = set(talk_norm.split()) & set(video_norm.split())
        title_ratio = len(title_overlap) / max(1, min(len(set(talk_norm.split())), len(set(video_norm.split()))))
        score = 0
        if talk_norm and talk_norm in video_norm:
            score += 10
        elif video_norm and video_norm in talk_norm:
            score += 8
        else:
            if len(title_overlap) >= 4:
                score += len(title_overlap)
        speaker_overlap = speaker_tokens(talk["speakers"]) & video_tokens
        if speaker_overlap:
            score += min(6, len(speaker_overlap) * 2)
        if score >= 7 and len(title_overlap) >= 2 and title_ratio >= 0.75:
            scored.append((score, talk))
    scored.sort(key=lambda item: (-item[0], item[1]["title"]))
    return [talk for _score, talk in scored[:3]]


def explicit_wf26_event_title(video: VideoEntry) -> bool:
    title = video.title.lower()
    if re.search(r"\b(?:wf26|wf2026)\s*:", title):
        return True
    if ("world" in title and "fair" in title and "2026" in title) or ("worldsfair" in title and "2026" in title):
        return any(marker in title for marker in ("livestream", "keynote", "talk", "session", "workshop", "recording"))
    return False


def non_playlist_media_date_allowed(video: VideoEntry) -> bool:
    """Bound heuristic channel matching to the WF26 recording year.

    Canonical playlist membership is handled by ``fetch_official_playlist`` and
    deliberately bypasses this heuristic gate. This gate applies only when text
    matching is being used to infer event association for a channel upload.
    """

    if excluded_non_wf26_event_title(video):
        return False
    published = video.published_date
    if explicit_wf26_event_title(video):
        return published >= WF26_EVENT_START_DATE
    return WF26_EVENT_START_DATE <= published <= WF26_NON_PLAYLIST_MEDIA_END_DATE


def parse_speaker_names(value: str) -> list[str]:
    try:
        parsed = json.loads(value)
    except (json.JSONDecodeError, TypeError):
        parsed = []
    if isinstance(parsed, list):
        return [str(item).strip() for item in parsed if str(item).strip()]
    return []


def normalize_evidence_text(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", value.lower())).strip()


def phrase_present(phrase: str, blob: str) -> bool:
    return bool(phrase) and f" {phrase} " in f" {blob} "


def verified_schedule_matches(video: VideoEntry, talks: list[dict[str, str]]) -> list[dict[str, str]]:
    """Match rewritten official-channel titles using schedule text, not popularity signals."""
    strict = strict_schedule_matches(video, talks)
    matched = {talk["id"]: talk for talk in strict}
    override_ids = set(OFFICIAL_PLAYLIST_SCHEDULE_OVERRIDES.get(video.video_id, ()))
    for talk in talks:
        if talk["id"] in override_ids:
            matched[talk["id"]] = talk
    evidence_blob = normalize_evidence_text(f"{video.title}\n{video.description}")
    description_blob = normalize_evidence_text(video.description)
    description_candidates: list[dict[str, str]] = []
    for talk in talks:
        if talk["id"] in matched:
            continue
        speaker_names = parse_speaker_names(talk.get("speakers", ""))
        if not any(phrase_present(normalize_evidence_text(name), evidence_blob) for name in speaker_names):
            continue
        title_phrase = normalize_evidence_text(talk["title"])
        schedule_description = normalize_evidence_text(talk.get("description", ""))
        title_signal = len(title_phrase) >= 12 and phrase_present(title_phrase, evidence_blob)
        description_signal = len(schedule_description) >= 120 and schedule_description[:120] in description_blob
        if title_signal:
            matched[talk["id"]] = talk
        elif description_signal:
            description_candidates.append(talk)
    # Description matching is a fallback for materially rewritten video titles.
    # Never let a shared schedule description broaden an already title-bound or
    # explicitly overridden match to sibling sessions.
    if not matched:
        matched.update({talk["id"]: talk for talk in description_candidates})
    return sorted(matched.values(), key=lambda item: item["title"])


def yt_dlp_binary() -> str:
    command = shutil.which("yt-dlp")
    if command:
        return command
    local = Path.home() / ".local" / "bin" / "yt-dlp"
    return str(local) if local.exists() else "yt-dlp"


def video_entry_from_metadata(payload: dict[str, object]) -> VideoEntry:
    upload_date = str(payload.get("upload_date") or payload.get("release_date") or "")
    if not re.fullmatch(r"\d{8}", upload_date):
        raise ValueError(f"video metadata has no usable upload/release date: {payload.get('id')}")
    published_date = datetime.strptime(upload_date, "%Y%m%d").date().isoformat()
    release_raw = str(payload.get("release_date") or "")
    release_date = datetime.strptime(release_raw, "%Y%m%d").date().isoformat() if re.fullmatch(r"\d{8}", release_raw) else ""
    languages = set((payload.get("subtitles") or {}).keys()) | set((payload.get("automatic_captions") or {}).keys())
    video_id = str(payload.get("id") or "")
    return VideoEntry(
        video_id=video_id,
        title=str(payload.get("title") or video_id),
        published=f"{published_date}T00:00:00+00:00",
        updated=f"{published_date}T00:00:00+00:00",
        url=str(payload.get("webpage_url") or f"https://www.youtube.com/watch?v={video_id}"),
        description=str(payload.get("description") or ""),
        live_status=str(payload.get("live_status") or ""),
        release_date=release_date,
        has_english_captions=any(lang == "en" or lang.startswith("en-") for lang in languages),
        channel_id=str(payload.get("channel_id") or ""),
        availability=str(payload.get("availability") or ""),
    )


def opaque_unavailable_metadata(payload: dict[str, object]) -> bool:
    """Recognize yt-dlp's metadata-only placeholder for an unavailable video."""

    video_id = str(payload.get("id") or "").strip()
    title = str(payload.get("title") or "").strip().casefold()
    placeholder_titles = {
        "",
        "[deleted video]",
        "[private video]",
        f"youtube video #{video_id}".casefold(),
    }
    identifying_fields = (
        "channel_id",
        "upload_date",
        "release_date",
        "timestamp",
        "release_timestamp",
        "description",
        "live_status",
    )
    return bool(video_id) and title in placeholder_titles and not any(
        payload.get(field) for field in identifying_fields
    )


def fetch_video_metadata(video_id: str) -> VideoEntry:
    cp = subprocess.run(
        [
            yt_dlp_binary(),
            "--no-playlist",
            "--no-cache-dir",
            "--skip-download",
            "--ignore-no-formats-error",
            "--no-warnings",
            "--dump-single-json",
            f"https://www.youtube.com/watch?v={video_id}",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=180,
    )
    if cp.returncode != 0:
        raise RuntimeError(f"yt-dlp metadata failed for {video_id}: {(cp.stderr or cp.stdout)[-1200:]}")
    payload = json.loads(cp.stdout)
    if not isinstance(payload, dict):
        raise RuntimeError(f"yt-dlp returned no metadata for {video_id}")
    if opaque_unavailable_metadata(payload):
        raise RuntimeError(
            f"yt-dlp metadata reports unavailable video: {video_id} "
            "(opaque metadata placeholder)"
        )
    try:
        return video_entry_from_metadata(payload)
    except ValueError as exc:
        probe = subprocess.run(
            [
                yt_dlp_binary(),
                "--no-playlist",
                "--no-cache-dir",
                "--skip-download",
                f"https://www.youtube.com/watch?v={video_id}",
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=180,
        )
        unavailable_error = (probe.stderr or probe.stdout)[-1600:]
        if "private video" in unavailable_error.lower():
            raise RuntimeError(f"yt-dlp metadata reports Private video: {video_id}") from exc
        if "unavailable" in unavailable_error.lower() or "deleted" in unavailable_error.lower():
            raise RuntimeError(
                f"yt-dlp metadata reports unavailable video: {video_id}"
            ) from exc
        raise


def metadata_unavailable_reason(error: Exception) -> str:
    message = str(error).lower()
    if "private video" in message:
        return "private"
    if (
        "video unavailable" in message
        or "unavailable video" in message
        or "deleted video" in message
    ):
        return "unavailable"
    return ""


def fetch_official_playlist(
    talks: list[dict[str, str]],
) -> tuple[list[PlaylistEntry], dict[str, object]]:
    """Enumerate the official WF26 playlist without losing private entries."""
    cp = subprocess.run(
        [
            yt_dlp_binary(),
            "--flat-playlist",
            "--ignore-errors",
            "--no-cache-dir",
            "--no-warnings",
            "--dump-single-json",
            OFFICIAL_PLAYLIST_URL,
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=300,
    )
    if cp.returncode != 0:
        raise RuntimeError(
            "official WF26 playlist enumeration failed: "
            + (cp.stderr or cp.stdout)[-1600:]
        )
    try:
        payload = json.loads(cp.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("official WF26 playlist returned invalid JSON") from exc
    if not isinstance(payload, dict) or payload.get("id") != OFFICIAL_PLAYLIST_ID:
        raise RuntimeError("official WF26 playlist identity mismatch")
    if payload.get("channel_id") != CHANNEL_ID:
        raise RuntimeError("official WF26 playlist owner channel mismatch")
    raw_entries = payload.get("entries")
    if not isinstance(raw_entries, list):
        raise RuntimeError("official WF26 playlist has no entries array")

    ids: list[str] = []
    for item in raw_entries:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            raise RuntimeError("official WF26 playlist contains an invalid entry")
        video_id = str(item["id"])
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
            raise RuntimeError(f"official WF26 playlist contains invalid video ID: {video_id}")
        ids.append(video_id)
    if len(ids) != len(set(ids)):
        raise RuntimeError("official WF26 playlist contains duplicate video IDs")
    baseline_ids = set(OFFICIAL_PLAYLIST_BASELINE_IDS)
    missing_baseline = sorted(baseline_ids - set(ids))
    if missing_baseline:
        raise RuntimeError(
            "official WF26 playlist is missing baseline items: "
            + ", ".join(missing_baseline)
        )
    new_since_baseline = sorted(set(ids) - baseline_ids)

    entries: list[PlaylistEntry] = []
    unavailable = 0
    for index, item in enumerate(raw_entries, start=1):
        video_id = str(item["id"])
        playlist_title = str(item.get("title") or "").strip()
        try:
            video = fetch_video_metadata(video_id)
        except Exception as exc:
            reason = metadata_unavailable_reason(exc)
            if not reason:
                raise RuntimeError(
                    f"official WF26 playlist metadata failed for {video_id}: {exc}"
                ) from exc
            unavailable += 1
            entries.append(
                PlaylistEntry(
                    video_id=video_id,
                    playlist_index=index,
                    playlist_title=playlist_title,
                    availability=reason,
                    video=None,
                    metadata_error=str(exc)[-1600:],
                )
            )
            continue
        if video.channel_id != CHANNEL_ID:
            raise RuntimeError(
                f"official WF26 playlist video owner mismatch for {video_id}"
            )
        entries.append(
            PlaylistEntry(
                video_id=video_id,
                playlist_index=index,
                playlist_title=playlist_title,
                availability=video.availability or "available",
                video=video,
                matched_talks=tuple(verified_schedule_matches(video, talks)),
            )
        )

    return entries, {
        "status": "ok",
        "playlist_id": OFFICIAL_PLAYLIST_ID,
        "playlist_title": str(payload.get("title") or ""),
        "playlist_count": len(entries),
        "baseline_count": len(OFFICIAL_PLAYLIST_BASELINE_IDS),
        "new_since_baseline_count": len(new_since_baseline),
        "new_since_baseline_ids": new_since_baseline,
        "visible_count": len(entries) - unavailable,
        "unavailable_count": unavailable,
    }


def manifest_video_ids() -> set[str]:
    payload = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    if not isinstance(payload, dict):
        return set()
    return {str(item.get("id")) for item in payload.get("videos", []) if isinstance(item, dict) and item.get("id")}


def revalidate_manifest_non_playlist_rows(
    talks: list[dict[str, str]],
) -> tuple[list[tuple[VideoEntry, list[dict[str, str]]]], dict[str, object]]:
    """Revalidate durable non-playlist primary admissions from fresh metadata.

    The bounded recent-channel scan cannot prove that an older retained row is
    still a WF26 recording. Re-fetch those rows directly so a successful full
    reconciliation can retire stale, wrong-year, or otherwise unbound primary
    admissions without treating absence from the recent window as evidence.
    """

    payload = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    videos = payload.get("videos", []) if isinstance(payload, dict) else []
    candidates = [
        item
        for item in videos
        if isinstance(item, dict)
        and item.get("id")
        and item.get("playlistId") != OFFICIAL_PLAYLIST_ID
        and not (
            str(item.get("id")) in EXPLICIT_WF26_OFFICIAL_LIVESTREAM_IDS
            and item.get("mediaType") == "event_livestream"
            and item.get("associationEvidence") == "explicit_wf26_official_livestream"
        )
    ]
    rows: list[tuple[VideoEntry, list[dict[str, str]]]] = []
    rejected: list[dict[str, str]] = []
    metadata_errors: list[dict[str, str]] = []
    for item in sorted(candidates, key=lambda row: str(row.get("id"))):
        video_id = str(item["id"])
        try:
            video = fetch_video_metadata(video_id)
        except Exception as exc:
            metadata_errors.append({"id": video_id, "error": str(exc)[-1200:]})
            continue
        if video.channel_id != CHANNEL_ID:
            rejected.append(
                {
                    "id": video_id,
                    "upload_date": video.published_date.isoformat(),
                    "reason": "official_channel_owner_mismatch",
                }
            )
            continue
        if excluded_non_wf26_event_title(video):
            rejected.append(
                {
                    "id": video_id,
                    "upload_date": video.published_date.isoformat(),
                    "reason": "explicit_non_wf26_event_title",
                }
            )
            continue
        if not non_playlist_media_date_allowed(video):
            rejected.append(
                {
                    "id": video_id,
                    "upload_date": video.published_date.isoformat(),
                    "reason": "outside_wf26_date_gate",
                }
            )
            continue
        matched = verified_schedule_matches(video, talks)
        if not matched and not explicit_wf26_event_title(video):
            rejected.append(
                {
                    "id": video_id,
                    "upload_date": video.published_date.isoformat(),
                    "reason": "wf26_event_binding_not_reverified",
                }
            )
            continue
        rows.append((video, matched))
    return rows, {
        "status": "ok" if not metadata_errors else "metadata_incomplete",
        "candidate_count": len(candidates),
        "revalidated_count": len(rows),
        "rejected": rejected,
        "metadata_errors": metadata_errors,
    }


def scheduled_manifest_video_ids() -> set[str]:
    payload = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    if not isinstance(payload, dict):
        return set()
    return {
        str(item.get("id"))
        for item in payload.get("videos", [])
        if isinstance(item, dict)
        and item.get("id")
        and item.get("mediaType") == "scheduled_premiere"
    }


def pending_manifest_video_ids() -> set[str]:
    payload = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    if not isinstance(payload, dict):
        return set()
    return {
        str(item.get("id"))
        for item in payload.get("videos", [])
        if isinstance(item, dict)
        and item.get("id")
        and (item.get("mediaType") == "scheduled_premiere" or item.get("transcriptStatus") == "pending")
    }


def no_slides_manifest_video_ids() -> set[str]:
    payload = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    if not isinstance(payload, dict):
        return set()
    return {
        str(item.get("id"))
        for item in payload.get("videos", [])
        if isinstance(item, dict)
        and item.get("id")
        and item.get("slideStatus") == NO_SLIDES_STATUS
    }


def discover_recent_channel_event_rows(
    talks: list[dict[str, str]], *, limit: int = 100
) -> tuple[list[tuple[VideoEntry, list[dict[str, str]]]], dict[str, object]]:
    """Inspect recent official-channel titles, fetching details only for roster candidates."""
    cp = subprocess.run(
        [
            yt_dlp_binary(),
            "--flat-playlist",
            "--playlist-end",
            str(limit),
            "--dump-single-json",
            "https://www.youtube.com/@aiDotEngineer/videos",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=300,
    )
    if cp.returncode != 0:
        return [], {"status": "channel_scan_failed", "error": (cp.stderr or cp.stdout)[-1200:]}
    payload = json.loads(cp.stdout)
    if not isinstance(payload, dict) or payload.get("channel_id") != CHANNEL_ID:
        return [], {"status": "channel_identity_mismatch"}
    channel_entries = payload.get("entries")
    if not isinstance(channel_entries, list):
        return [], {"status": "channel_entries_invalid"}

    known_ids = manifest_video_ids()
    pending_ids = pending_manifest_video_ids()
    speaker_phrases = {
        normalize_evidence_text(name)
        for talk in talks
        for name in parse_speaker_names(talk.get("speakers", ""))
        if name
    }
    rows: list[tuple[VideoEntry, list[dict[str, str]]]] = []
    metadata_errors: list[dict[str, str]] = []
    date_rejected_ids: list[str] = []
    candidates = 0
    for item in channel_entries:
        if not isinstance(item, dict) or not item.get("id"):
            continue
        if item.get("id") in known_ids and item.get("id") not in pending_ids:
            continue
        lightweight = VideoEntry(
            video_id=str(item["id"]),
            title=str(item.get("title") or item["id"]),
            published="1970-01-01T00:00:00+00:00",
            updated="1970-01-01T00:00:00+00:00",
            url=str(item.get("url") or f"https://www.youtube.com/watch?v={item['id']}"),
        )
        title_blob = normalize_evidence_text(lightweight.title)
        roster_candidate = any(phrase_present(phrase, title_blob) for phrase in speaker_phrases)
        if (
            not roster_candidate
            and not strict_schedule_matches(lightweight, talks)
            and not explicit_wf26_event_title(lightweight)
        ):
            continue
        candidates += 1
        try:
            video = fetch_video_metadata(lightweight.video_id)
        except Exception as exc:
            metadata_errors.append({"id": lightweight.video_id, "error": str(exc)})
            continue
        if excluded_non_wf26_event_title(video):
            date_rejected_ids.append(video.video_id)
            continue
        if not non_playlist_media_date_allowed(video):
            date_rejected_ids.append(video.video_id)
            continue
        matched = verified_schedule_matches(video, talks)
        if matched or explicit_wf26_event_title(video):
            rows.append((video, matched))
    return rows, {
        "status": "ok",
        "scanned": min(limit, len(channel_entries)),
        "metadata_candidates": candidates,
        "verified_event_videos": len(rows),
        "date_rejected_ids": sorted(date_rejected_ids),
        "metadata_errors": metadata_errors,
    }


def authoritative_non_playlist_reconciliation_ready(
    channel_discovery: dict[str, object],
    retained_revalidation: dict[str, object],
) -> bool:
    """Return whether stale primary rows may be pruned fail closed."""

    return (
        channel_discovery.get("status") == "ok"
        and not channel_discovery.get("metadata_errors")
        and retained_revalidation.get("status") == "ok"
        and not retained_revalidation.get("metadata_errors")
    )


def update_official_video_manifest(
    rows: list[tuple[VideoEntry, list[dict[str, str]]]],
    *,
    playlist_entries: list[PlaylistEntry] | None = None,
    prune_stale_non_playlist: bool = False,
    write: bool = True,
) -> bool:
    payload = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    if not isinstance(payload, dict):
        payload = {}
    videos = {
        str(item.get("id")): item
        for item in payload.get("videos", [])
        if isinstance(item, dict) and item.get("id")
    }
    row_matches = {
        video.video_id: matched
        for video, matched in rows
    }
    changed = False
    if prune_stale_non_playlist:
        authoritative_ids = set(row_matches) | {
            item.video_id for item in (playlist_entries or [])
        }
        for video_id, item in list(videos.items()):
            explicitly_retained_stream = (
                video_id in EXPLICIT_WF26_OFFICIAL_LIVESTREAM_IDS
                and item.get("mediaType") == "event_livestream"
                and item.get("associationEvidence")
                == "explicit_wf26_official_livestream"
            )
            if video_id in authoritative_ids or explicitly_retained_stream:
                continue
            del videos[video_id]
            changed = True
    for video, matched in rows:
        existing = dict(videos.get(video.video_id) or {})
        entry = {
            **existing,
            "id": video.video_id,
            "title": video.title,
            "mediaType": "scheduled_premiere" if video.live_status == "is_upcoming" else "talk_recording",
            "associationEvidence": (
                "official_wf26_playlist_membership"
                if existing.get("playlistId") == OFFICIAL_PLAYLIST_ID
                else (
                    "official_channel_plus_schedule_text"
                    if matched
                    else "official_channel_explicit_wf26_title"
                )
            ),
            "matchedTalks": [talk["id"] for talk in matched],
            "uploadDate": video.published_date.isoformat(),
            "releaseDate": video.release_date,
            "transcriptStatus": (
                "cached"
                if transcript_path(video.video_id).exists()
                else "available_on_youtube"
                if video.has_english_captions
                else "pending"
            ),
        }
        if videos.get(video.video_id) != entry:
            videos[video.video_id] = entry
            changed = True

    for item in playlist_entries or []:
        existing = dict(videos.get(item.video_id) or {})
        matched_talks = [
            talk["id"]
            for talk in row_matches.get(item.video_id, list(item.matched_talks))
        ]
        if item.video is None:
            matched_talks = list(existing.get("matchedTalks") or [])
            entry = {
                **existing,
                "id": item.video_id,
                "mediaType": "unavailable_playlist_item",
                "associationEvidence": "official_wf26_playlist_membership",
                "matchedTalks": matched_talks,
                "playlistId": OFFICIAL_PLAYLIST_ID,
                "playlistIndex": item.playlist_index,
                "playlistAvailability": "unavailable",
                "videoAvailability": "unknown",
                "unavailableReason": item.availability,
                "transcriptStatus": (
                    "cached" if transcript_path(item.video_id).exists() else "unavailable"
                ),
                "slideStatus": (
                    "cached" if slides_path(item.video_id).exists() else "unavailable"
                ),
            }
            if item.playlist_title:
                entry["playlistTitle"] = item.playlist_title
                entry.setdefault("title", item.playlist_title)
        else:
            video = item.video
            media_type = (
                "scheduled_premiere"
                if video.live_status == "is_upcoming"
                else "talk_recording"
            )
            entry = {
                **existing,
                "id": item.video_id,
                "title": video.title,
                "playlistTitle": item.playlist_title or video.title,
                "mediaType": media_type,
                "associationEvidence": "official_wf26_playlist_membership",
                "matchedTalks": matched_talks,
                "playlistId": OFFICIAL_PLAYLIST_ID,
                "playlistIndex": item.playlist_index,
                "playlistAvailability": "available",
                "videoAvailability": item.availability,
                "uploadDate": video.published_date.isoformat(),
                "releaseDate": video.release_date,
                "transcriptStatus": (
                    "cached"
                    if transcript_path(item.video_id).exists()
                    else "available_on_youtube"
                    if video.has_english_captions
                    else "pending"
                ),
                "slideStatus": (
                    "cached"
                    if slides_path(item.video_id).exists()
                    else NO_SLIDES_STATUS
                    if existing.get("slideStatus") == NO_SLIDES_STATUS
                    else "pending"
                ),
            }
            entry.pop("unavailableReason", None)
        if videos.get(item.video_id) != entry:
            videos[item.video_id] = entry
            changed = True
    if not changed:
        return False
    payload.update(
        {
            "schemaVersion": 1,
            "sourceBoundary": (
                "Official WF26 playlist membership establishes event association; "
                "the official schedule remains canonical for session titles, speakers, "
                "dates, rooms, tracks, and affiliations."
            ),
            "videos": sorted(
                videos.values(),
                key=lambda entry: (
                    0 if entry.get("playlistId") == OFFICIAL_PLAYLIST_ID else 1,
                    int(entry.get("playlistIndex") or 100000),
                    str(entry.get("uploadDate", "")),
                    str(entry.get("id", "")),
                ),
            ),
        }
    )
    if write:
        write_json(OFFICIAL_VIDEO_MANIFEST, payload)
    return True


def refresh_manifest_artifact_statuses(
    processed: list[dict[str, object]], *, write: bool = True
) -> bool:
    """Reconcile processed manifest rows with artifacts produced in this run."""
    payload = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    if not isinstance(payload, dict):
        return False
    videos = payload.get("videos")
    if not isinstance(videos, list):
        return False
    by_id = {
        str(item.get("id")): item
        for item in videos
        if isinstance(item, dict) and item.get("id")
    }
    changed = False
    for processed_item in processed:
        video_id = str(processed_item.get("id") or "")
        manifest_item = by_id.get(video_id)
        if not manifest_item:
            continue
        transcript_result = processed_item.get("transcript")
        transcript_status = (
            str(transcript_result.get("status") or "")
            if isinstance(transcript_result, dict)
            else ""
        )
        if transcript_path(video_id).exists():
            desired_transcript_status = "cached"
        elif transcript_status == "unavailable":
            desired_transcript_status = "unavailable"
        elif transcript_status == "pending_premiere":
            desired_transcript_status = "pending"
        else:
            desired_transcript_status = ""
        if (
            desired_transcript_status
            and manifest_item.get("transcriptStatus") != desired_transcript_status
        ):
            manifest_item["transcriptStatus"] = desired_transcript_status
            changed = True

        slide_result = processed_item.get("slides")
        slide_status = (
            str(slide_result.get("status") or "")
            if isinstance(slide_result, dict)
            else ""
        )
        if slide_status == NO_SLIDES_STATUS:
            desired_slide_status = NO_SLIDES_STATUS
        elif slides_path(video_id).exists():
            desired_slide_status = "cached"
        elif slide_status == "unavailable":
            desired_slide_status = "unavailable"
        elif slide_status == "pending_premiere":
            desired_slide_status = "pending"
        else:
            desired_slide_status = ""
        if desired_slide_status and manifest_item.get("slideStatus") != desired_slide_status:
            manifest_item["slideStatus"] = desired_slide_status
            changed = True

    if changed and write:
        write_json(OFFICIAL_VIDEO_MANIFEST, payload)
    return changed


def excluded_non_wf26_event_title(video: VideoEntry) -> bool:
    """Reject official-channel uploads that clearly point at another event/scope."""
    title = video.title.lower()
    other_event_markers = [
        "miami",
        "world's fair 2025",
        "worlds fair 2025",
        "worldsfair 2025",
        "wf25",
        "wf2025",
        "world's fair 2024",
        "worlds fair 2024",
        "worldsfair 2024",
        "wf24",
        "wf2024",
        "summit",
    ]
    return any(marker in title for marker in other_event_markers)


def title_tokens(value: str) -> set[str]:
    value = normalize_title(value)
    # Short numeric tokens can be the only discriminator between a sequence of
    # scheduled sessions (for example, "Part 1", "Part 2", and "Part 3").
    # Dropping them makes otherwise distinct titles look identical and can
    # attach one recording to every session in the sequence.
    return {
        token
        for token in value.split()
        if len(token) >= 3 or token.isdigit()
    }


def strict_schedule_matches(video: VideoEntry, talks: list[dict[str, str]]) -> list[dict[str, str]]:
    """Return only high-confidence matches to actual WF2026 scheduled talks.

    This is intentionally stricter than match_talks(). The monitor is allowed to
    import only official-channel WF26 event videos. A loose speaker/title overlap
    is useful for review, but not enough to create first-class event evidence.
    """
    if excluded_non_wf26_event_title(video):
        return []
    video_norm = normalize_title(video.title)
    video_title_tokens = title_tokens(video.title)
    video_speaker_tokens = speaker_tokens(video.title)
    matched: list[tuple[float, dict[str, str]]] = []
    for talk in talks:
        talk_norm = normalize_title(talk["title"])
        talk_title_tokens = title_tokens(talk["title"])
        if not talk_norm or not talk_title_tokens:
            continue
        speaker_overlap = speaker_tokens(talk["speakers"]) & video_speaker_tokens
        exact_title = talk_norm in video_norm
        overlap = talk_title_tokens & video_title_tokens
        coverage = len(overlap) / max(1, len(talk_title_tokens))
        if exact_title and speaker_overlap:
            matched.append((1.0, talk))
        elif coverage >= 0.9 and len(overlap) >= 4 and speaker_overlap:
            matched.append((coverage, talk))
    matched.sort(key=lambda item: (-item[0], item[1]["title"]))
    return [talk for _score, talk in matched[:3]]


def event_entries(entries: list[VideoEntry], talks: list[dict[str, str]]) -> list[tuple[VideoEntry, list[dict[str, str]]]]:
    rows = []
    for entry in entries:
        if not non_playlist_media_date_allowed(entry):
            continue
        if excluded_non_wf26_event_title(entry):
            continue
        matched = strict_schedule_matches(entry, talks)
        if explicit_wf26_event_title(entry) or matched:
            rows.append((entry, matched))
    return rows


def deduplicate_event_rows(
    *row_groups: list[tuple[VideoEntry, list[dict[str, str]]]],
) -> list[tuple[VideoEntry, list[dict[str, str]]]]:
    """Prefer later metadata while retaining every independently verified talk match."""

    combined: dict[str, tuple[VideoEntry, list[dict[str, str]]]] = {}
    first_seen_ids: list[str] = []
    for rows in row_groups:
        for entry, matched in rows:
            previous = combined.get(entry.video_id)
            if previous is None:
                first_seen_ids.append(entry.video_id)
            previous_matches = previous[1] if previous else []
            matches_by_id = {
                str(talk["id"]): talk
                for talk in [*previous_matches, *matched]
                if talk.get("id")
            }
            combined[entry.video_id] = (entry, list(matches_by_id.values()))
    return [combined[video_id] for video_id in first_seen_ids]


def write_resource_page(
    video: VideoEntry,
    matched_talks: list[dict[str, str]],
    transcript_status: str,
    slide_status: str,
    *,
    association_evidence: str = "official_channel_plus_schedule_text",
) -> bool:
    path = resource_path(video.video_id)
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    old_enriched = re.search(r'^last_enriched:\s*"?([^"\n]+)', old, re.M)
    enriched_at = old_enriched.group(1) if old_enriched else datetime.now(timezone.utc).isoformat()
    playlist_admitted = association_evidence == "official_wf26_playlist_membership"
    explicit_title_admitted = association_evidence == "official_channel_explicit_wf26_title"
    talk_lines = []
    if matched_talks:
        for talk in matched_talks:
            talk_lines.append(f"- [[{talk['id']}|{talk['title']}]]")
    else:
        reason = (
            "official WF26 playlist membership"
            if playlist_admitted
            else "the official-channel title explicitly identifies it as WF26 / World's Fair 2026 event media"
        )
        talk_lines.append(
            "- No exact schedule-page match has been assigned; event association comes from "
            f"{reason}. Do not infer schedule fields from the video title."
        )
    transcript_line = (
        f"Cached transcript text is available at `raw/sources/youtube-transcripts/{video.video_id}.txt`."
        if transcript_path(video.video_id).exists()
        else f"Transcript import status: {transcript_status}."
    )
    if slide_status == NO_SLIDES_STATUS:
        slide_line = "- No slide deck was used; the cached transcript explicitly reports no slides."
    elif slides_path(video.video_id).exists():
        slide_line = f"- [[youtube-{video.video_id}-slides]]"
    else:
        slide_line = f"- Slide extraction status: {slide_status}."
    upcoming = video.live_status == "is_upcoming"
    if upcoming:
        media_description = (
            "A scheduled official AI Engineer YouTube premiere admitted through the official "
            "WF26 playlist. The page records association metadata only until the premiere is "
            "playable; transcript and slide evidence remain pending."
            if playlist_admitted
            else (
                "A scheduled official AI Engineer YouTube premiere whose official-channel title explicitly identifies it as AI Engineer World's Fair 2026 media. No exact schedule-page match is inferred; transcript and slide evidence remain unavailable until the premiere is playable."
                if explicit_title_admitted
                else "A scheduled official AI Engineer YouTube premiere independently matched to an AI Engineer World's Fair San Francisco 2026 session. The page records the pending media source now; transcript and slide evidence remain unavailable until the premiere is playable."
            )
        )
    else:
        media_description = (
            "An official AI Engineer YouTube recording admitted through the official WF26 "
            "playlist. Playlist membership establishes event association; official schedule "
            "pages remain canonical for schedule metadata."
            if playlist_admitted
            else (
                "An official AI Engineer YouTube recording whose official-channel title explicitly identifies it as AI Engineer World's Fair 2026 media. No exact schedule-page match is inferred; official schedule pages remain canonical for schedule metadata."
                if explicit_title_admitted
                else "An official AI Engineer YouTube recording independently matched to an AI Engineer World's Fair San Francisco 2026 session. Official schedule pages remain canonical for schedule metadata."
            )
        )
    release_line = f"- Scheduled premiere date: {video.release_date}." if upcoming and video.release_date else ""
    if upcoming:
        source_role_line = "- Source role: official event-video association metadata for a scheduled premiere."
        use_line = (
            "- Use: association and premiere-state metadata only until the recording is playable; "
            "do not use this page as recording, transcript, or slide-content evidence."
        )
    else:
        source_role_line = "- Source role: primary event video source for AI Engineer World's Fair San Francisco 2026."
        use_line = (
            "- Use: use as media and transcript evidence for the event recording; no slide deck "
            "is claimed, and schedule facts remain tied to the official schedule pages."
            if slide_status == NO_SLIDES_STATUS
            else "- Use: use as media/transcript/slide evidence for the event recording; keep schedule "
            "facts tied to the official schedule pages."
        )
    text = "\n".join(
        [
            frontmatter(
                {
                    "title": video.title,
                    "category": "resources",
                    "sourceLabels": (
                        ["Official AI Engineer YouTube channel", "Official WF26 playlist membership"]
                        if playlist_admitted
                        else (
                            ["Official AI Engineer YouTube channel", "Explicit WF26 title metadata"]
                            if explicit_title_admitted
                            else ["Official AI Engineer YouTube channel", "Official-channel video metadata"]
                        )
                    ),
                    "videoId": video.video_id,
                    "publishedDate": video.published_date.isoformat(),
                    "last_enriched": enriched_at,
                    **(
                        {"sourceLayers": ["supporting_context"]}
                        if upcoming
                        else {}
                    ),
                }
            ).rstrip(),
            f"# {video.title}",
            "",
            "## What It Is",
            media_description,
            "",
            "## Source Classification",
            source_role_line,
            (
                f"- Admission: official playlist `{OFFICIAL_PLAYLIST_ID}` membership."
                if playlist_admitted
                else (
                    "- Admission: official-channel title explicitly identifies WF26 / World's Fair 2026 event media; no exact schedule match is inferred."
                    if explicit_title_admitted
                    else "- Admission: official-channel metadata independently matched to schedule evidence."
                )
            ),
            f"- Published date: {video.published_date.isoformat()}",
            release_line,
            f"- Channel/source: {OFFICIAL_CHANNEL}.",
            use_line,
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
    if old == text + "\n":
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    write_text(path, text + "\n")
    return True


def write_unavailable_resource_page(item: PlaylistEntry) -> bool:
    path = resource_path(item.video_id)
    title = f"Official WF26 Playlist Item {item.video_id} (Unavailable)"
    text = "\n".join(
        [
            frontmatter(
                {
                    "title": title,
                    "category": "resources",
                    "sourceLabels": ["Official WF26 playlist membership"],
                    "videoId": item.video_id,
                    "playlistId": OFFICIAL_PLAYLIST_ID,
                    "availability": item.availability,
                    "sourceLayers": ["supporting_context"],
                }
            ).rstrip(),
            f"# {title}",
            "",
            "## What It Is",
            "An unavailable item retained from the official AI Engineer WF26 playlist. Playlist membership establishes event association only; no title, speaker, transcript, slide, or schedule claim is made.",
            "",
            "## Source Classification",
            "- Source role: official WF26 playlist association metadata only.",
            f"- Playlist position: {item.playlist_index}.",
            f"- Availability: {item.availability}.",
            "- Use: do not use this placeholder as content, transcript, slide, or schedule evidence.",
            "",
            "## Transcript Status",
            "Unavailable; no transcript content was acquired.",
            "",
            "## Extracted Slides",
            "Unavailable; no slide content was acquired.",
            "",
            "## Link",
            f"[YouTube](https://www.youtube.com/watch?v={item.video_id})",
        ]
    ) + "\n"
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if old == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    write_text(path, text)
    return True


def update_talk_pages(video: VideoEntry, matched_talks: list[dict[str, str]]) -> int:
    updated = 0
    transcript_bits = []
    if transcript_path(video.video_id).exists():
        transcript_bits.append(f"[[youtube-{video.video_id}-transcript]]")
    if slides_path(video.video_id).exists():
        transcript_bits.append(f"[[youtube-{video.video_id}-slides]]")
    evidence = "; ".join(transcript_bits) if transcript_bits else "transcript/slide enrichment pending"
    media_line = (
        f"- [[youtube-{video.video_id}]] — scheduled official AI Engineer YouTube premiere for {video.release_date or 'a pending date'}."
        if video.live_status == "is_upcoming"
        else f"- [[youtube-{video.video_id}]] — official AI Engineer YouTube channel recording published {video.published_date.isoformat()}."
    )
    boundary_line = (
        "- Boundary: use this link as event-association and premiere-state metadata only until "
        "the recording is playable; do not use it as recording, transcript, or slide-content evidence."
        if video.live_status == "is_upcoming"
        else "- Boundary: use this recording as media evidence; keep date/time/room facts tied to the official schedule."
    )
    body = "\n".join(
        [
            media_line,
            f"- Evidence status: {evidence}.",
            boundary_line,
        ]
    )
    desired_paths = {Path(talk["path"]) for talk in matched_talks}
    candidate_paths = desired_paths | set((WIKI / "talks").glob("*.md"))
    for path in sorted(candidate_paths):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        new_text = reconcile_official_recording_section(
            text,
            video.video_id,
            body if path in desired_paths else None,
        )
        if new_text != text:
            write_text(path, new_text)
            updated += 1
    return updated


def retire_primary_event_projections(video_ids: list[str]) -> dict[str, object]:
    """Demote retired manifest rows without deleting useful source artifacts."""

    safe_ids = sorted(set(video_ids))
    for video_id in safe_ids:
        if not re.fullmatch(r"[A-Za-z0-9_-]{6,32}", video_id):
            raise ValueError(f"unsafe retired YouTube video id: {video_id!r}")
    talk_updates = 0
    for path in sorted((WIKI / "talks").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        updated = text
        for video_id in safe_ids:
            updated = reconcile_official_recording_section(updated, video_id, None)
        if updated != text:
            write_text(path, updated)
            talk_updates += 1
    if not safe_ids:
        return {"video_ids": [], "talk_updates": 0, "resource_updates": 0}
    if _ACTIVE_TRANSACTION is not None:
        _ACTIVE_TRANSACTION.backup_canonical_root(WIKI)
    command = [sys.executable, "scripts/classify_video_resource_sources.py"]
    for video_id in safe_ids:
        command.extend(["--video-id", video_id])
    completed = run(command, timeout=900, check=True)
    classifier_summary = None
    for line in reversed(completed.stdout.splitlines()):
        try:
            candidate = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(candidate, dict) and isinstance(candidate.get("updated"), int):
            classifier_summary = candidate
            break
    if classifier_summary is None:
        raise RuntimeError("resource classifier did not emit an updated count")
    return {
        "video_ids": safe_ids,
        "talk_updates": talk_updates,
        "resource_updates": classifier_summary["updated"],
        "resource_classifier": classifier_summary,
        "classifier_returncode": completed.returncode,
    }


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


def try_import_captions(
    video: VideoEntry, *, allow_browser_fallback: bool = True
) -> dict[str, object]:
    if transcript_path(video.video_id).exists():
        return {"status": "already_cached", "path": str(transcript_path(video.video_id).relative_to(ROOT))}
    if video.live_status == "is_upcoming":
        return {"status": "pending_premiere", "release_date": video.release_date}
    subtitle_dir = RAW / "youtube-subtitles"
    subtitle_dir.mkdir(parents=True, exist_ok=True)
    if _ACTIVE_TRANSACTION is not None:
        _ACTIVE_TRANSACTION.track_path(transcript_path(video.video_id))
        _ACTIVE_TRANSACTION.track_glob(subtitle_dir, f"{video.video_id}*.vtt")
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
        if not allow_browser_fallback:
            return {
                "status": "caption_acquisition_pending",
                "yt_dlp_error": (cp.stderr or cp.stdout)[-1600:],
            }
        chrome = try_import_captions_with_chrome_agent(video)
        if chrome.get("status") == "captions_imported":
            return chrome
        chrome["yt_dlp_error"] = (cp.stderr or cp.stdout)[-1600:]
        return chrome
    after = set(subtitle_dir.glob(f"{video.video_id}*.vtt"))
    candidates = sorted(after - before) or sorted(after)
    if not candidates:
        if not allow_browser_fallback:
            return {
                "status": "caption_acquisition_pending",
                "attempt_status": "no_captions_found",
            }
        return {"status": "no_captions_found"}
    text = vtt_to_text(candidates[0]).strip()
    if not text:
        return {"status": "empty_caption_file", "caption_path": str(candidates[0].relative_to(ROOT))}
    target = transcript_path(video.video_id)
    target.parent.mkdir(parents=True, exist_ok=True)
    write_text(target, text + "\n")
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
    if _ACTIVE_TRANSACTION is not None:
        _ACTIVE_TRANSACTION.track_path(target)
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


def explicit_no_slides_evidence(video_id: str) -> str:
    path = transcript_path(video_id)
    if not path.exists():
        return ""
    opening = path.read_text(encoding="utf-8", errors="ignore")[:12000]
    opening = opening.replace("\u2019", "'")
    for pattern in NO_SLIDES_PATTERNS:
        match = pattern.search(opening)
        if match:
            return re.sub(r"\s+", " ", match.group(0)).strip()
    return ""


def no_slides_reconciliation_needed(video_id: str, known_no_slides: set[str]) -> bool:
    if not explicit_no_slides_evidence(video_id):
        return False
    return (
        slides_path(video_id).exists()
        or standard_slide_references_exist(video_id)
        or video_id not in known_no_slides
    )


def standard_slide_reference_markers(video_id: str) -> tuple[str, ...]:
    return (
        f"youtube-{video_id}-slides",
        f"assets/slides/{video_id}/",
        f"Slide-derived themes for `youtube-{video_id}`",
    )


def strip_standard_slide_references(markdown: str, video_id: str) -> str:
    """Remove references to a retired standard slide extraction only."""

    markers = standard_slide_reference_markers(video_id)
    source_marker = f"- Source video: `youtube-{video_id}`"
    parts = re.split(r"(\n{2,})", markdown)
    kept: list[str] = []
    for index, part in enumerate(parts):
        if index % 2:
            kept.append(part)
            continue
        if source_marker in part and any(marker in part for marker in markers):
            kept.append("")
            continue
        lines = [line for line in part.splitlines() if not any(marker in line for marker in markers)]
        kept.append("\n".join(lines))
    cleaned = "".join(kept)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.rstrip() + "\n"


def standard_slide_references_exist(video_id: str) -> bool:
    markers = standard_slide_reference_markers(video_id)
    for path in WIKI.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        if any(marker in text for marker in markers):
            return True
    return False


def retire_standard_slide_references(video_id: str) -> list[str]:
    changed: list[str] = []
    for path in WIKI.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        updated = strip_standard_slide_references(text, video_id)
        if updated == text:
            continue
        write_text(path, updated)
        changed.append(str(path.relative_to(ROOT)))
    return changed


def retire_standard_slide_artifacts(video_id: str) -> list[str]:
    if not re.fullmatch(r"[A-Za-z0-9_-]{6,32}", video_id):
        raise ValueError(f"unsafe YouTube video id for slide cleanup: {video_id!r}")
    paths = [
        slides_path(video_id),
        WIKI / "assets" / "slides" / video_id,
        RAW / "slide-ocr" / video_id,
    ]
    removed: list[str] = []
    for path in paths:
        if path.is_symlink() or path.is_file():
            remove_path(path)
        elif path.is_dir():
            remove_path(path)
        else:
            continue
        try:
            removed.append(str(path.relative_to(ROOT)))
        except ValueError:
            removed.append(str(path))
    retire_standard_slide_references(video_id)
    return removed


def try_extract_slides(video: VideoEntry, matched_talks: list[dict[str, str]], *, enabled: bool) -> dict[str, object]:
    no_slides_evidence = explicit_no_slides_evidence(video.video_id)
    if no_slides_evidence:
        return {
            "status": NO_SLIDES_STATUS,
            "reason": "explicit_transcript_statement",
            "evidence": no_slides_evidence,
            "removed_artifacts": retire_standard_slide_artifacts(video.video_id),
        }
    if slides_path(video.video_id).exists():
        return {"status": "already_extracted", "path": str(slides_path(video.video_id).relative_to(ROOT))}
    if not enabled:
        return {"status": "skipped_by_configuration"}
    if video.live_status == "is_upcoming":
        return {"status": "pending_premiere", "release_date": video.release_date}
    if _ACTIVE_TRANSACTION is not None:
        _ACTIVE_TRANSACTION.backup_canonical_root(WIKI)
        _ACTIVE_TRANSACTION.track_path(RAW / "slide-ocr" / video.video_id)
        _ACTIVE_TRANSACTION.track_path(RAW / "slide-extraction-failures.json")
    cmd = [sys.executable, "scripts/extract_video_slides.py", "--scene-detect", f"--video-id={video.video_id}", "--max-slides", "32"]
    outputs: list[str] = []
    for _attempt in range(2):
        cp = run(cmd, timeout=1500)
        outputs.append((cp.stderr or cp.stdout)[-1600:])
        if slides_path(video.video_id).exists():
            return {"status": "slide_extraction_ran", "path": str(slides_path(video.video_id).relative_to(ROOT))}
    return {"status": "slide_extraction_failed", "error": "\n".join(outputs)[-2400:]}


def update_channel_snapshot(entries: list[VideoEntry]) -> bool:
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
    existing = load_json(RSS_SNAPSHOT, {})
    stable_keys = ("id", "title", "url", "published", "published_date", "channel", "source")
    old_entries = [tuple(item.get(key) for key in stable_keys) for item in existing.get("entries", [])] if isinstance(existing, dict) else []
    new_entries = [tuple(item.get(key) for key in stable_keys) for item in payload["entries"]]
    if old_entries == new_entries:
        return False
    write_json(RSS_SNAPSHOT, payload)
    return True


def wiki_maker_executable() -> str:
    override = os.environ.get(WIKI_MAKER_ENV, "").strip()
    if override:
        candidate = Path(override).expanduser()
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate.resolve())
        resolved = shutil.which(override)
        if resolved:
            return resolved
        raise RuntimeError(f"{WIKI_MAKER_ENV} does not name an executable: {override}")

    pinned = ROOT / "scripts" / "run_pinned_wiki_maker.py"
    if pinned.is_file() and os.access(pinned, os.X_OK):
        return str(pinned)
    sibling = ROOT.parent / "wiki-from-topic-maker" / ".venv" / "bin" / "wiki-from-topic-maker"
    if sibling.is_file() and os.access(sibling, os.X_OK):
        return str(sibling)
    resolved = shutil.which("wiki-from-topic-maker")
    if resolved:
        return resolved
    raise RuntimeError(
        "wiki-from-topic-maker is unavailable; set "
        f"{WIKI_MAKER_ENV} to the installed executable"
    )


def update_source_paths(video_ids: list[str]) -> list[Path]:
    candidates = [OFFICIAL_VIDEO_MANIFEST]
    for video_id in sorted(set(video_ids)):
        candidates.append(transcript_path(video_id))
        candidates.extend(sorted((RAW / "youtube-subtitles").glob(f"{video_id}*.vtt")))
    return sorted({path for path in candidates if path.is_file()})


def playable_manifest_projection(payload: object) -> dict[str, dict[str, object]]:
    if not isinstance(payload, dict):
        return {}
    return {
        str(item["id"]): item
        for item in payload.get("videos", [])
        if isinstance(item, dict)
        and item.get("id")
        and item.get("mediaType") in PLAYABLE_MEDIA_TYPES
    }


def content_completion_summary(payload: object) -> dict[str, object]:
    """Summarize association and local content coverage for the current manifest."""

    raw_videos = payload.get("videos", []) if isinstance(payload, dict) else []
    if not isinstance(raw_videos, list):
        raw_videos = []
    videos = [
        item
        for item in raw_videos
        if isinstance(item, dict) and item.get("id")
    ]
    video_ids = {str(item["id"]) for item in videos}
    associated = [item for item in videos if item.get("associationEvidence")]
    playable = [item for item in videos if item.get("mediaType") in PLAYABLE_MEDIA_TYPES]
    scheduled = [item for item in videos if item.get("mediaType") == "scheduled_premiere"]
    unavailable = [
        item for item in videos if item.get("mediaType") == "unavailable_playlist_item"
    ]

    transcript_complete_ids = {
        str(item["id"])
        for item in playable
        if transcript_path(str(item["id"])).exists()
    }
    transcript_unavailable_ids = {
        str(item["id"])
        for item in playable
        if str(item.get("transcriptStatus") or "") == "unavailable"
        and str(item["id"]) not in transcript_complete_ids
    }
    slide_complete_ids = {
        str(item["id"])
        for item in playable
        if slides_path(str(item["id"])).exists()
        or str(item.get("slideStatus") or "") == NO_SLIDES_STATUS
    }
    slide_unavailable_ids = {
        str(item["id"])
        for item in playable
        if str(item.get("slideStatus") or "") == "unavailable"
        and str(item["id"]) not in slide_complete_ids
    }
    playable_ids = {str(item["id"]) for item in playable}
    fully_enriched_ids = transcript_complete_ids & slide_complete_ids
    baseline_ids = set(OFFICIAL_PLAYLIST_BASELINE_IDS)
    represented_baseline_ids = video_ids & baseline_ids
    missing_baseline_ids = baseline_ids - represented_baseline_ids
    unassociated_count = len(videos) - len(associated)

    if not videos:
        association_state = "empty"
    elif unassociated_count or missing_baseline_ids:
        association_state = "partial"
    else:
        association_state = "complete"

    transcript_pending_count = len(
        playable_ids - transcript_complete_ids - transcript_unavailable_ids
    )
    slide_pending_count = len(playable_ids - slide_complete_ids - slide_unavailable_ids)
    if not playable:
        transcript_state = "not_applicable"
        slide_state = "not_applicable"
    else:
        transcript_state = (
            "complete"
            if len(transcript_complete_ids) == len(playable_ids)
            else "partial"
        )
        slide_state = (
            "complete" if len(slide_complete_ids) == len(playable_ids) else "partial"
        )

    content_is_complete = bool(videos) and all(
        (
            association_state == "complete",
            len(fully_enriched_ids) == len(playable_ids),
            not scheduled,
            not unavailable,
        )
    )
    return {
        "state": "complete" if content_is_complete else "partial" if videos else "empty",
        "scope": "current_manifest_and_local_artifacts",
        "media_association": {
            "state": association_state,
            "manifest_count": len(videos),
            "associated_count": len(associated),
            "unassociated_count": unassociated_count,
            "playable_count": len(playable),
            "scheduled_premiere_count": len(scheduled),
            "unavailable_count": len(unavailable),
            "playlist_baseline_count": len(baseline_ids),
            "playlist_baseline_represented_count": len(represented_baseline_ids),
            "playlist_baseline_missing_count": len(missing_baseline_ids),
        },
        "transcripts": {
            "state": transcript_state,
            "eligible_count": len(playable),
            "complete_count": len(transcript_complete_ids),
            "pending_count": transcript_pending_count,
            "unavailable_count": len(transcript_unavailable_ids),
        },
        "slides": {
            "state": slide_state,
            "eligible_count": len(playable),
            "complete_count": len(slide_complete_ids),
            "pending_count": slide_pending_count,
            "unavailable_count": len(slide_unavailable_ids),
        },
        "fully_enriched_playable_count": len(fully_enriched_ids),
        "partial_playable_count": len(playable_ids - fully_enriched_ids),
    }


def content_completion_message(summary: dict[str, object]) -> str:
    transcripts = summary.get("transcripts")
    slides = summary.get("slides")
    media = summary.get("media_association")
    transcripts = transcripts if isinstance(transcripts, dict) else {}
    slides = slides if isinstance(slides, dict) else {}
    media = media if isinstance(media, dict) else {}
    return (
        f"Content acquisition is {summary.get('state', 'unknown')}: "
        f"{transcripts.get('complete_count', 0)}/{transcripts.get('eligible_count', 0)} "
        "playable transcripts and "
        f"{slides.get('complete_count', 0)}/{slides.get('eligible_count', 0)} "
        "playable slide outcomes are resolved; "
        f"{media.get('scheduled_premiere_count', 0)} premieres and "
        f"{media.get('unavailable_count', 0)} unavailable media items remain."
    )


def rollback_failed_monitor_run(
    report: dict[str, object], transaction: MonitorMutationTransaction | None
) -> None:
    if transaction is None:
        return
    rollback = rollback_monitor_transaction(transaction)
    report["mutation_rollback"] = rollback
    if rollback.get("errors"):
        report["state"] = "failed"
        report["status"] = "failed"
        report["message"] = (
            f"{report.get('message', '')} Canonical rollback is incomplete; "
            "the next monitor start will retry recovery before acquisition."
        ).strip()


def run_enrichment(_imported_transcripts: int, video_ids: list[str]) -> list[dict[str, object]]:
    if _ACTIVE_TRANSACTION is not None:
        _ACTIVE_TRANSACTION.backup_canonical_root(WIKI)
        _ACTIVE_TRANSACTION.backup_canonical_root(ROOT / "dist")
        _ACTIVE_TRANSACTION.backup_canonical_root(
            RAW / "attendance-calibration"
        )
        _ACTIVE_TRANSACTION.track_path(ROOT / "agent-index.json")
        _ACTIVE_TRANSACTION.track_path(ROOT / "agent-index.md")
    attendance_sync = [
        sys.executable,
        "scripts/generate_attendance_calibration.py",
        "--sync-current",
    ]
    attendance = run(attendance_sync, timeout=900)
    results = [{"cmd": attendance_sync, "returncode": attendance.returncode}]
    if attendance.returncode != 0:
        return results

    cmd = [
        wiki_maker_executable(),
        "update",
        str(ROOT),
        "--change-type",
        "media",
    ]
    for path in update_source_paths(video_ids):
        cmd.extend(["--source", str(path.relative_to(ROOT))])
    cmd.append("--json")
    cp = run(cmd, timeout=7200)
    maker_result: dict[str, object] = {
        "cmd": cmd,
        "returncode": cp.returncode,
    }
    combined_output = f"{cp.stdout or ''}\n{cp.stderr or ''}"
    if cp.returncode != 0 and WIKI_MAKER_REPLAN_REQUIRED in combined_output:
        retry = run(cmd, timeout=7200)
        maker_result.update(
            {
                "attempts": 2,
                "first_returncode": cp.returncode,
                "returncode": retry.returncode,
                "retry_reason": "deterministic_inputs_changed",
            }
        )
        cp = retry
    results.append(maker_result)
    if cp.returncode != 0:
        return results

    canonical_checks = [
        [sys.executable, "scripts/livestream_segment_projection.py", "--check"],
        [sys.executable, "scripts/generate_attendance_calibration.py", "--check-current"],
        [
            sys.executable,
            "scripts/audit_primary_media_roles.py",
            "--phase",
            "full",
            "--root",
            ".",
        ],
    ]
    for check_cmd in canonical_checks:
        check = run(check_cmd, timeout=900)
        results.append({"cmd": check_cmd, "returncode": check.returncode})
        if check.returncode != 0:
            break
    return results


def publish_sync_journal_path() -> Path:
    return STATE_DIR / PUBLISH_SYNC_JOURNAL.name


def _write_publish_sync(payload: dict[str, object]) -> None:
    write_json(publish_sync_journal_path(), payload)


def _clear_publish_sync() -> None:
    publish_sync_journal_path().unlink(missing_ok=True)


def _retry_git(
    command: list[str], *, attempts: int = 3, timeout: int = 60
) -> subprocess.CompletedProcess[str]:
    result: subprocess.CompletedProcess[str] | None = None
    for attempt in range(attempts):
        result = run(command, timeout=timeout)
        if result.returncode == 0:
            return result
        if attempt + 1 < attempts:
            time.sleep(0.2 * (attempt + 1))
    assert result is not None
    return result


def _finalize_local_publish_sync(
    payload: dict[str, object], *, verify_remote: bool
) -> dict[str, object]:
    base_commit = str(payload.get("baseCommit") or "")
    candidate_commit = str(payload.get("candidateCommit") or "")
    if not re.fullmatch(r"[0-9a-f]{40,64}", base_commit) or not re.fullmatch(
        r"[0-9a-f]{40,64}", candidate_commit
    ):
        raise RuntimeError("publish sync journal contains invalid commit IDs")
    branch = run(["git", "branch", "--show-current"], timeout=60)
    if branch.returncode != 0 or branch.stdout.strip() != "main":
        raise RuntimeError("publish sync recovery requires the checked-out main branch")
    head = run(["git", "rev-parse", "HEAD"], timeout=60)
    current_head = head.stdout.strip()
    if head.returncode != 0 or current_head not in {base_commit, candidate_commit}:
        raise RuntimeError(
            "local main moved outside the monitor publish transaction; refusing to overwrite it"
        )

    if verify_remote:
        remote = run(["git", "ls-remote", "origin", "refs/heads/main"], timeout=120)
        remote_head = remote.stdout.split(maxsplit=1)[0] if remote.stdout.strip() else ""
        if remote.returncode != 0:
            raise RuntimeError("cannot verify the remote main commit for publish recovery")
        if remote_head != candidate_commit:
            if payload.get("phase") == "candidate_prepared":
                _clear_publish_sync()
                return {
                    "status": "candidate_not_published",
                    "candidateCommit": candidate_commit,
                }
            raise RuntimeError("remote main does not match the published monitor candidate")

    if current_head == base_commit:
        update_ref = _retry_git(
            [
                "git",
                "update-ref",
                "refs/heads/main",
                candidate_commit,
                base_commit,
            ]
        )
        if update_ref.returncode != 0:
            return {
                "status": "local_sync_pending",
                "candidateCommit": candidate_commit,
                "localRefReturncode": update_ref.returncode,
            }

    index_tree = run(["git", "write-tree"], timeout=60)
    base_tree = run(["git", "rev-parse", f"{base_commit}^{{tree}}"], timeout=60)
    candidate_tree = run(
        ["git", "rev-parse", f"{candidate_commit}^{{tree}}"], timeout=60
    )
    if any(item.returncode != 0 for item in (index_tree, base_tree, candidate_tree)):
        raise RuntimeError("cannot inspect the local index during publish recovery")
    if index_tree.stdout.strip() not in {
        base_tree.stdout.strip(),
        candidate_tree.stdout.strip(),
    }:
        raise RuntimeError(
            "the local index contains user-staged changes; refusing to replace it"
        )
    refresh_index = _retry_git(["git", "read-tree", candidate_commit])
    if refresh_index.returncode != 0:
        return {
            "status": "local_sync_pending",
            "candidateCommit": candidate_commit,
            "localIndexReturncode": refresh_index.returncode,
        }
    _clear_publish_sync()
    return {"status": "synchronized", "candidateCommit": candidate_commit}


def recover_monitor_publish_sync() -> dict[str, object] | None:
    path = publish_sync_journal_path()
    if not path.is_file():
        return None
    payload = load_json(path, {})
    if not isinstance(payload, dict) or payload.get("schemaVersion") != 1:
        raise RuntimeError("invalid monitor publish sync journal")
    return _finalize_local_publish_sync(payload, verify_remote=True)


def maybe_commit_and_push(enabled: bool, message: str) -> dict[str, object]:
    if not enabled:
        return {"enabled": False}
    branch = run(["git", "branch", "--show-current"], timeout=60)
    current_branch = branch.stdout.strip()
    if branch.returncode != 0 or current_branch != "main":
        return {
            "enabled": True,
            "blocked": True,
            "reason": "auto-push requires the checked-out main branch",
            "branch": current_branch,
        }
    status = run(["git", "status", "--porcelain"], timeout=60)
    if not status.stdout.strip():
        return {"enabled": True, "changed": False}
    add_paths = [
        path
        for path in [
            "raw",
            "wiki",
            "scripts",
            "package.json",
            "package-lock.json",
            "agent-index.json",
            "agent-index.md",
        ]
        if (ROOT / path).exists()
    ]
    base = run(["git", "rev-parse", "HEAD"], timeout=60)
    if base.returncode != 0:
        return {
            "enabled": True,
            "changed": True,
            "commit_returncode": base.returncode,
            "error": base.stderr[-1000:],
        }

    STATE_DIR.mkdir(parents=True, exist_ok=True)
    temporary_index = STATE_DIR / f"publish-index-{uuid4().hex}.index"
    git_env = os.environ.copy()
    git_env["GIT_INDEX_FILE"] = str(temporary_index)
    try:
        read_tree = run(["git", "read-tree", base.stdout.strip()], timeout=60, env=git_env)
        if read_tree.returncode != 0:
            return {
                "enabled": True,
                "changed": True,
                "commit_returncode": read_tree.returncode,
                "error": read_tree.stderr[-1000:],
            }
        added = run(["git", "add", "--all", "--", *add_paths], timeout=120, env=git_env)
        if added.returncode != 0:
            return {
                "enabled": True,
                "changed": True,
                "commit_returncode": added.returncode,
                "error": added.stderr[-1000:],
            }
        staged = run(
            ["git", "diff", "--cached", "--quiet", "--", *add_paths],
            timeout=60,
            env=git_env,
        )
        if staged.returncode == 0:
            return {
                "enabled": True,
                "changed": False,
                "note": "no publishable staged changes",
            }
        if staged.returncode != 1:
            return {
                "enabled": True,
                "changed": True,
                "commit_returncode": staged.returncode,
                "error": staged.stderr[-1000:],
            }
        tree = run(["git", "write-tree"], timeout=60, env=git_env)
        if tree.returncode != 0:
            return {
                "enabled": True,
                "changed": True,
                "commit_returncode": tree.returncode,
                "error": tree.stderr[-1000:],
            }
        commit = run(
            [
                "git",
                "commit-tree",
                tree.stdout.strip(),
                "-p",
                base.stdout.strip(),
                "-m",
                message,
            ],
            timeout=120,
        )
        if commit.returncode != 0:
            return {
                "enabled": True,
                "changed": True,
                "commit_returncode": commit.returncode,
                "error": commit.stderr[-1000:],
            }
        commit_id = commit.stdout.strip()
        publish_sync = {
            "schemaVersion": 1,
            "phase": "candidate_prepared",
            "baseCommit": base.stdout.strip(),
            "candidateCommit": commit_id,
            "createdAt": datetime.now(timezone.utc).isoformat(),
        }
        _write_publish_sync(publish_sync)
        push = run(
            ["git", "push", "origin", f"{commit_id}:refs/heads/main"], timeout=300
        )
        if push.returncode != 0:
            _clear_publish_sync()
            return {
                "enabled": True,
                "changed": True,
                "commit_returncode": 0,
                "push_returncode": push.returncode,
                "base_commit": base.stdout.strip(),
                "candidate_commit": commit_id,
                "error": push.stderr[-1000:],
            }
        publish_sync["phase"] = "remote_published"
        publish_sync["publishedAt"] = datetime.now(timezone.utc).isoformat()
        _write_publish_sync(publish_sync)
        if _ACTIVE_TRANSACTION is not None:
            finish_monitor_transaction(_ACTIVE_TRANSACTION)
        local_sync = _finalize_local_publish_sync(publish_sync, verify_remote=False)
        return {
            "enabled": True,
            "changed": True,
            "commit_returncode": 0,
            "push_returncode": 0,
            "local_sync": local_sync,
            "base_commit": base.stdout.strip(),
            "commit": commit_id,
        }
    finally:
        if temporary_index.exists():
            temporary_index.unlink()


def auto_push_preflight() -> dict[str, object]:
    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=60,
    )
    branch = subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=60,
    )
    current_branch = branch.stdout.strip()
    if status.returncode != 0 or branch.returncode != 0:
        return {
            "ok": False,
            "reason": "git preflight failed",
            "git_status_returncode": status.returncode,
            "git_branch_returncode": branch.returncode,
            "branch": current_branch,
        }
    if current_branch != "main":
        return {
            "ok": False,
            "reason": "auto-push requires the checked-out main branch",
            "branch": current_branch,
        }
    if status.stdout.strip():
        return {
            "ok": False,
            "reason": "auto-push requires a clean pre-run worktree",
            "branch": current_branch,
            "worktree_status": status.stdout.splitlines(),
        }
    return {"ok": True, "branch": current_branch}


def write_status(report: dict[str, object]) -> None:
    write_json(STATUS_JSON, report)
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    completion = report.get("content_completion")
    completion = completion if isinstance(completion, dict) else {}
    media = completion.get("media_association")
    media = media if isinstance(media, dict) else {}
    transcripts = completion.get("transcripts")
    transcripts = transcripts if isinstance(transcripts, dict) else {}
    slides = completion.get("slides")
    slides = slides if isinstance(slides, dict) else {}
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
    write_text(
        STATUS_HTML,
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
<p>Latest official video date: <code>{html.escape(str(report.get('latest_published_date')))}</code>. Reconciliation has no age-based auto-expiry.</p>
<p>Content completion: <code>{html.escape(str(completion.get('state', 'unknown')))}</code>. Associated media: {html.escape(str(media.get('associated_count', 0)))}/{html.escape(str(media.get('manifest_count', 0)))}; playable media: {html.escape(str(media.get('playable_count', 0)))}; premieres: {html.escape(str(media.get('scheduled_premiere_count', 0)))}; unavailable: {html.escape(str(media.get('unavailable_count', 0)))}.</p>
<p>Transcripts: {html.escape(str(transcripts.get('complete_count', 0)))}/{html.escape(str(transcripts.get('eligible_count', 0)))} complete. Slide outcomes: {html.escape(str(slides.get('complete_count', 0)))}/{html.escape(str(slides.get('eligible_count', 0)))} complete.</p>
<p>{html.escape(str(report.get('message', '')))}</p>
<table>
<thead><tr><th>Date</th><th>ID</th><th>Title</th><th>Resource</th><th>Transcript</th><th>Slides</th></tr></thead>
<tbody>{''.join(rows) or '<tr><td colspan="6">No newly processed videos in this run.</td></tr>'}</tbody>
</table>
</main>
</body>
</html>
""",
    )


def open_status_page() -> None:
    if not os.environ.get("DISPLAY"):
        return
    opener = shutil.which("xdg-open") or shutil.which("firefox")
    if opener:
        subprocess.Popen([opener, str(STATUS_HTML)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--playlist-only",
        action="store_true",
        help="Use only official WF26 playlist discovery and playlist-specific acquisition behavior.",
    )
    parser.add_argument("--no-slides", action="store_true", help="Skip slide extraction attempts for new videos.")
    push = parser.add_mutually_exclusive_group()
    push.add_argument(
        "--auto-push",
        dest="auto_push",
        action="store_true",
        help="Commit and push successful import changes from a clean main checkout.",
    )
    push.add_argument(
        "--no-auto-push",
        dest="auto_push",
        action="store_false",
        help="Never commit or push, overriding the service environment.",
    )
    parser.set_defaults(auto_push=None)
    parser.add_argument("--open-status", action="store_true", help="Open the status page after this run.")
    args = parser.parse_args(argv)

    checked_at = datetime.now(timezone.utc)
    recovery: dict[str, object] | None = None
    publish_recovery: dict[str, object] | None = None
    if not args.dry_run:
        try:
            publish_recovery = recover_monitor_publish_sync()
            if publish_recovery and publish_recovery.get("status") == "local_sync_pending":
                report = {
                    "checked_at": checked_at.isoformat(),
                    "channel_id": CHANNEL_ID,
                    "state": "blocked",
                    "status": "blocked",
                    "message": "A previously published monitor commit is still pending local checkout synchronization; no acquisition work started.",
                    "publish_recovery": publish_recovery,
                    "processed": [],
                    "dry_run": False,
                }
                print(json.dumps(report, sort_keys=True))
                return 2
            if publish_recovery and publish_recovery.get("status") == "synchronized":
                recovery = commit_recovered_monitor_transaction()
            else:
                recovery = recover_monitor_transaction()
        except Exception as exc:
            report = {
                "checked_at": checked_at.isoformat(),
                "channel_id": CHANNEL_ID,
                "state": "blocked",
                "status": "blocked",
                "message": "Monitor transaction recovery failed; no acquisition work started.",
                "error": {"type": type(exc).__name__, "message": str(exc)},
                "processed": [],
                "dry_run": False,
            }
            print(json.dumps(report, sort_keys=True))
            return 2
        if recovery and recovery.get("errors"):
            report = {
                "checked_at": checked_at.isoformat(),
                "channel_id": CHANNEL_ID,
                "state": "blocked",
                "status": "blocked",
                "message": "Monitor transaction recovery is incomplete; no acquisition work started.",
                "transaction_recovery": recovery,
                "processed": [],
                "dry_run": False,
            }
            print(json.dumps(report, sort_keys=True))
            return 2
    auto_push = (
        args.auto_push
        if args.auto_push is not None
        else False
        if args.playlist_only
        else os.environ.get("AIE_WF2026_MONITOR_AUTO_PUSH") == "1"
    )
    if auto_push and not args.dry_run:
        preflight = auto_push_preflight()
        if not preflight.get("ok"):
            report = {
                "checked_at": checked_at.isoformat(),
                "channel_id": CHANNEL_ID,
                "state": "blocked",
                "message": f"Monitor skipped: {preflight.get('reason')}; no files were changed.",
                "publish_preflight": preflight,
                "processed": [],
                "dry_run": False,
            }
            print(json.dumps(report, sort_keys=True))
            return 2

    transaction = None if args.dry_run else begin_monitor_transaction()

    talks = read_talk_pages()
    playlist_entries, playlist_discovery = fetch_official_playlist(talks)
    playlist_event_rows = [
        (item.video, list(item.matched_talks))
        for item in playlist_entries
        if item.video is not None
    ]
    if args.playlist_only:
        snapshot_changed = False
        channel_discovery: dict[str, object] = {"status": "not_run_playlist_only"}
        retained_rows: list[tuple[VideoEntry, list[dict[str, str]]]] = []
        retained_revalidation: dict[str, object] = {
            "status": "not_run_playlist_only"
        }
        event_rows = playlist_event_rows
    else:
        entries = fetch_rss()
        snapshot_changed = False if args.dry_run else update_channel_snapshot(entries)
        rss_event_rows = event_entries(entries, talks)
        discovered_rows, channel_discovery = discover_recent_channel_event_rows(talks)
        retained_rows, retained_revalidation = revalidate_manifest_non_playlist_rows(
            talks
        )
        event_rows = deduplicate_event_rows(
            rss_event_rows,
            discovered_rows,
            retained_rows,
            playlist_event_rows,
        )
    authoritative_non_playlist_reconciliation = (
        not args.playlist_only
        and authoritative_non_playlist_reconciliation_ready(
            channel_discovery, retained_revalidation
        )
    )
    playlist_video_ids = {item.video_id for item in playlist_entries}
    scheduled_manifest_ids = scheduled_manifest_video_ids()
    pending_manifest_ids = pending_manifest_video_ids()
    manifest_before = load_json(OFFICIAL_VIDEO_MANIFEST, {})
    manifest_changed = update_official_video_manifest(
        event_rows,
        playlist_entries=playlist_entries,
        prune_stale_non_playlist=authoritative_non_playlist_reconciliation,
        write=not args.dry_run,
    )
    manifest_after = (
        load_json(OFFICIAL_VIDEO_MANIFEST, {}) if not args.dry_run else manifest_before
    )
    manifest_before_videos = (
        manifest_before.get("videos", []) if isinstance(manifest_before, dict) else []
    )
    manifest_after_videos = (
        manifest_after.get("videos", []) if isinstance(manifest_after, dict) else []
    )
    manifest_before_ids = {
        str(item.get("id"))
        for item in manifest_before_videos
        if isinstance(item, dict) and item.get("id")
    }
    manifest_after_ids = {
        str(item.get("id"))
        for item in manifest_after_videos
        if isinstance(item, dict) and item.get("id")
    }
    retired_primary_ids = sorted(manifest_before_ids - manifest_after_ids)
    retired_primary_projection = (
        retire_primary_event_projections(retired_primary_ids)
        if retired_primary_ids and not args.dry_run
        else {
            "video_ids": retired_primary_ids,
            "status": "dry_run" if args.dry_run and retired_primary_ids else "not_needed",
        }
    )
    known_no_slides_ids = no_slides_manifest_video_ids()
    playable_evidence_changed = (
        not args.dry_run
        and playable_manifest_projection(manifest_before)
        != playable_manifest_projection(manifest_after)
    )
    latest_date = max((entry.published_date for entry, _matched in event_rows), default=None)

    report: dict[str, object] = {
        "checked_at": checked_at.isoformat(),
        "channel_id": CHANNEL_ID,
        "active_cutoff_date": None,
        "latest_published_date": latest_date.isoformat() if latest_date else "",
        "processed": [],
        "dry_run": args.dry_run,
        "mode": "playlist_only" if args.playlist_only else "scheduled_monitor",
        "auto_push": auto_push,
        "manifest_changed": manifest_changed,
        "retired_primary_projection": retired_primary_projection,
        "channel_discovery": channel_discovery,
        "retained_non_playlist_revalidation": retained_revalidation,
        "authoritative_non_playlist_reconciliation": (
            authoritative_non_playlist_reconciliation
        ),
        "playlist_discovery": playlist_discovery,
        "reconciliation_policy": {
            "auto_expiry": False,
            "date_cutoff": None,
            "scope": (
                "owner-validated official WF26 playlist media plus eligible "
                "date/title-gated official-channel media"
            ),
        },
        "content_completion": content_completion_summary(manifest_after),
    }
    if recovery is not None:
        report["transaction_recovery"] = recovery
    if publish_recovery is not None:
        report["publish_recovery"] = publish_recovery

    reconciliation_rows = event_rows
    process_rows = [
        (entry, matched)
        for entry, matched in reconciliation_rows
        if not resource_path(entry.video_id).exists()
        or resource_schedule_projection_needed(entry.video_id, matched)
        or (
            entry.video_id in playlist_video_ids
            and resource_playlist_projection_needed(entry.video_id)
        )
        or talk_page_projection_needed(entry.video_id, matched)
        or (
            entry.video_id in scheduled_manifest_ids
            and entry.live_status != "is_upcoming"
        )
        or (
            entry.video_id in pending_manifest_ids
            and entry.has_english_captions
            and not transcript_path(entry.video_id).exists()
        )
        or (
            args.playlist_only
            and entry.live_status != "is_upcoming"
            and no_slides_reconciliation_needed(entry.video_id, known_no_slides_ids)
        )
        or (
            args.playlist_only
            and entry.live_status != "is_upcoming"
            and (
                not transcript_path(entry.video_id).exists()
                or (
                    not args.no_slides
                    and os.environ.get("AIE_WF2026_MONITOR_SKIP_SLIDES") != "1"
                    and entry.video_id not in known_no_slides_ids
                    and not slides_path(entry.video_id).exists()
                )
            )
        )
    ]
    processed: list[dict[str, object]] = []
    transcript_imports = 0
    acquisition_changed = manifest_changed

    for entry, matched in process_rows:
        transcript = {"status": "dry_run"}
        slides = {"status": "dry_run"}
        resource_status = "dry_run"
        talk_updates = 0
        if not args.dry_run:
            transcript = try_import_captions(
                entry, allow_browser_fallback=not args.playlist_only
            )
            if args.playlist_only and (
                str(transcript.get("status")) in CAPTION_FAILURE_STATUSES
                or str(transcript.get("status", "")).endswith("_failed")
            ):
                transcript = {
                    **transcript,
                    "attempt_status": transcript.get("status"),
                    "status": "caption_acquisition_pending",
                }
            if transcript.get("status") == "captions_imported":
                transcript_imports += 1
            slides = try_extract_slides(entry, matched, enabled=not args.no_slides and os.environ.get("AIE_WF2026_MONITOR_SKIP_SLIDES") != "1")
            if args.playlist_only and str(slides.get("status", "")).endswith("_failed"):
                slides = {
                    **slides,
                    "attempt_status": slides.get("status"),
                    "status": "slide_acquisition_pending",
                }
            resource_changed = write_resource_page(
                entry,
                matched,
                str(transcript.get("status")),
                str(slides.get("status")),
                association_evidence=(
                    "official_wf26_playlist_membership"
                    if entry.video_id in playlist_video_ids
                    else (
                        "official_channel_plus_schedule_text"
                        if matched
                        else "official_channel_explicit_wf26_title"
                    )
                ),
            )
            talk_updates = update_talk_pages(entry, matched)
            resource_status = "created_or_updated" if resource_changed else "unchanged"
            item_changed = any(
                (
                    transcript.get("status") == "captions_imported",
                    slides.get("status") == "slide_extraction_ran",
                    slides.get("status") == NO_SLIDES_STATUS,
                    resource_changed,
                    talk_updates > 0,
                )
            )
            acquisition_changed = acquisition_changed or item_changed
            playable_evidence_changed = playable_evidence_changed or (
                entry.live_status != "is_upcoming" and item_changed
            )
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

    unavailable_entries = [item for item in playlist_entries if item.video is None]
    for item in unavailable_entries:
        resource_status = "dry_run"
        if not args.dry_run:
            resource_changed = write_unavailable_resource_page(item)
            resource_status = "created_or_updated" if resource_changed else "unchanged"
            acquisition_changed = acquisition_changed or resource_changed
        processed.append(
            {
                "id": item.video_id,
                "title": item.playlist_title,
                "url": f"https://www.youtube.com/watch?v={item.video_id}",
                "published": "",
                "published_date": "",
                "matched_talks": [],
                "resource_status": resource_status,
                "talk_updates": 0,
                "transcript": {"status": "unavailable", "reason": item.availability},
                "slides": {"status": "unavailable", "reason": item.availability},
            }
        )

    report["processed"] = processed
    if not args.dry_run:
        manifest_before_artifact_refresh = load_json(OFFICIAL_VIDEO_MANIFEST, {})
        artifact_manifest_changed = refresh_manifest_artifact_statuses(processed)
        if artifact_manifest_changed:
            manifest_after_artifact_refresh = load_json(OFFICIAL_VIDEO_MANIFEST, {})
            manifest_changed = True
            acquisition_changed = True
            playable_evidence_changed = playable_evidence_changed or (
                playable_manifest_projection(manifest_before_artifact_refresh)
                != playable_manifest_projection(manifest_after_artifact_refresh)
            )
            report["manifest_changed"] = True
        report["content_completion"] = content_completion_summary(
            load_json(OFFICIAL_VIDEO_MANIFEST, {})
        )
        item_failures = media_item_failures(processed)
        report["item_failures"] = item_failures
        report["failure_count"] = len(item_failures)
        if item_failures:
            every_component_failed = bool(processed) and all(
                str(item.get("transcript", {}).get("status")) in CAPTION_FAILURE_STATUSES
                and str(item.get("slides", {}).get("status")) in SLIDE_FAILURE_STATUSES
                for item in processed
            )
            failure_state = "failed" if every_component_failed else "degraded"
            report.update(
                {
                    "state": failure_state,
                    "status": failure_state,
                    "message": "One or more monitor media-import items failed; changes were not published and the timer will retry.",
                    "recent_entry_count": len(reconciliation_rows),
                    "reconciled_entry_count": len(reconciliation_rows),
                    "new_entry_count": len(process_rows),
                }
            )
            rollback_failed_monitor_run(report, transaction)
            write_status(report)
            return 1
        report["playable_evidence_changed"] = playable_evidence_changed
        if playable_evidence_changed:
            private_policy = {
                "status": "delegated_to_unified_maker_dag",
                "adapter": "credibility_policy",
            }
        else:
            private_policy = {
                "status": "not_needed",
                "reason": "no admitted or updated playable evidence changed",
            }
        report["private_credibility_v2"] = private_policy
        enrichment = (
            run_enrichment(
                transcript_imports,
                [entry.video_id for entry, _matched in process_rows]
                + [item.video_id for item in unavailable_entries],
            )
            if playable_evidence_changed
            else []
        )
        report["enrichment"] = enrichment
        enrichment_failed = any(item.get("returncode") != 0 for item in enrichment)
        if enrichment_failed:
            report.update(
                {
                    "state": "degraded",
                    "message": "A monitor enrichment command failed; changes were not published and the timer will retry.",
                    "recent_entry_count": len(reconciliation_rows),
                    "reconciled_entry_count": len(reconciliation_rows),
                    "new_entry_count": len(process_rows),
                }
            )
            rollback_failed_monitor_run(report, transaction)
            write_status(report)
            return 1
        report["publish"] = maybe_commit_and_push(
            auto_push and (acquisition_changed or snapshot_changed),
            "Import new official AI Engineer YouTube videos",
        )
        publish = report["publish"]
        if publish.get("blocked") or publish.get("commit_returncode", 0) != 0 or publish.get("push_returncode", 0) != 0:
            report.update(
                {
                    "state": "degraded",
                    "message": "Monitor publishing failed; canonical changes will be rolled back and the timer will retry.",
                    "recent_entry_count": len(reconciliation_rows),
                    "reconciled_entry_count": len(reconciliation_rows),
                    "new_entry_count": len(process_rows),
                }
            )
            rollback_failed_monitor_run(report, transaction)
            write_status(report)
            return 1

        local_sync = publish.get("local_sync")
        if (
            isinstance(local_sync, dict)
            and local_sync.get("status") != "synchronized"
        ):
            report.update(
                {
                    "state": "degraded",
                    "status": "degraded",
                    "message": "The monitor commit was published, but local checkout synchronization is pending; startup recovery will retry before new acquisition.",
                    "recent_entry_count": len(reconciliation_rows),
                    "reconciled_entry_count": len(reconciliation_rows),
                    "new_entry_count": len(process_rows),
                }
            )
            if transaction is not None:
                finish_monitor_transaction(transaction)
            write_status(report)
            return 1

        if transaction is not None:
            finish_monitor_transaction(transaction)

    report.update(
        {
            "state": "active",
            "message": (
                f"Synchronized the official WF26 playlist and processed {len(processed)} items. "
                if args.playlist_only
                else f"Recurring official WF26 reconciliation processed {len(processed)} items and remains eligible for late releases. "
            )
            + content_completion_message(report["content_completion"]),
            "recent_entry_count": len(reconciliation_rows) + len(unavailable_entries),
            "reconciled_entry_count": len(reconciliation_rows)
            + len(unavailable_entries),
            "new_entry_count": len(process_rows),
            "acquisition_changed": acquisition_changed,
            "playable_evidence_changed": playable_evidence_changed,
        }
    )
    if args.dry_run:
        print(json.dumps(report, sort_keys=True))
    else:
        write_status(report)
        if args.open_status:
            open_status_page()
    return 0


def media_item_failures(processed: list[dict[str, object]]) -> list[dict[str, str]]:
    failures: list[dict[str, str]] = []
    for item in processed:
        for component, failure_statuses in (
            ("transcript", CAPTION_FAILURE_STATUSES),
            ("slides", SLIDE_FAILURE_STATUSES),
        ):
            result = item.get(component)
            if not isinstance(result, dict):
                continue
            status = str(result.get("status") or "")
            if status not in failure_statuses and not status.endswith("_failed"):
                continue
            failures.append(
                {
                    "id": str(item.get("id") or ""),
                    "component": component,
                    "status": status,
                    "error": str(result.get("error") or result.get("yt_dlp_error") or ""),
                }
            )
    return failures


def run_entrypoint(argv: list[str] | None = None) -> int:
    global _ACTIVE_TRANSACTION
    arguments = list(sys.argv[1:] if argv is None else argv)
    try:
        return main(arguments)
    except Exception as exc:
        rollback = None
        if _ACTIVE_TRANSACTION is not None:
            if publish_sync_journal_path().is_file():
                rollback = {
                    "status": "deferred_to_publish_recovery",
                    "errors": [],
                }
                _ACTIVE_TRANSACTION = None
            else:
                try:
                    rollback = rollback_monitor_transaction(_ACTIVE_TRANSACTION)
                except Exception as rollback_exc:
                    rollback = {
                        "status": "rollback_failed",
                        "errors": [str(rollback_exc)],
                    }
        previous = load_json(STATUS_JSON, {})
        report = {
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "channel_id": CHANNEL_ID,
            "state": "degraded",
            "status": "degraded",
            "message": "The monitor failed before completing. The systemd service will retry automatically.",
            "error": {"type": type(exc).__name__, "message": str(exc)},
            "previous_checked_at": previous.get("checked_at", "") if isinstance(previous, dict) else "",
            "processed": [],
            "dry_run": "--dry-run" in arguments,
        }
        if rollback is not None:
            report["mutation_rollback"] = rollback
        if report["dry_run"]:
            print(json.dumps(report, sort_keys=True))
        else:
            write_status(report)
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    raise SystemExit(run_entrypoint())
