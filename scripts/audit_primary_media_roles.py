#!/usr/bin/env python3
"""Fail closed when non-playable media is projected as primary WF26 evidence.

``pre-agent`` audits canonical Markdown and the just-exported static product.
``full`` repeats those checks and also audits the generated agent records.  The
maker runs the first phase after static export; operators run the second phase
after the agent product has been rebuilt.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable


PLAYABLE_MEDIA_TYPES = {"talk_recording", "event_livestream"}
PLAYABLE_VIDEO_AVAILABILITIES = {"", "public", "unlisted"}
PLAYABLE_PLAYLIST_AVAILABILITIES = {"", "available"}
PRIMARY_SOURCE_ROLES = {"official_primary", "primary_event_evidence"}
CONTEXT_MARKERS = ("supporting", "context", "not part of the confirmed")
CONTEXTUALIZED_CLAIM_PATTERNS = (
    re.compile(r"\bsupporting[\s/_-]+context\b", re.I),
    re.compile(r"\bcontext[\s_-]+only\b", re.I),
    re.compile(r"\bhistorical(?:[\s/_-]+or)?[\s/_-]+supporting\b", re.I),
    re.compile(r"\bnot (?:a )?primary\b", re.I),
    re.compile(r"\bnot part of the confirmed\b", re.I),
    re.compile(r"\boutside the confirmed\b", re.I),
    re.compile(r"\brelated (?:youtube )?(?:video|recording|resource)\b", re.I),
)

# These two artifacts were explicitly retired from the WF26 primary set after
# authoritative playlist/channel reconciliation.  Keeping the IDs here makes
# deletion of every surviving reference fail closed instead of making the
# retirement invisible to an inference-only audit.
DURABLE_RETIRED_IDS = {"o-zkvb0iFDQ", "sRpqPgKeXNk"}

VIDEO_ID_RE = r"[A-Za-z0-9_-]{11}"
EXACT_RESOURCE_NAME = re.compile(rf"^youtube-({VIDEO_ID_RE})\.md$")
EXACT_TRANSCRIPT_NAME = re.compile(rf"^youtube-({VIDEO_ID_RE})-transcript\.md$")
EXACT_DERIVED_NAME = re.compile(
    rf"^youtube-({VIDEO_ID_RE})-(?:slides|dense-slides|reconstructed-slides)\.md$"
)
WATCH_URL_PATTERN = re.compile(
    rf"(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?[^\s<>'\"]*?\bv=|youtu\.be/)"
    rf"({VIDEO_ID_RE})(?=$|[^A-Za-z0-9_-])",
    re.IGNORECASE,
)
WIKILINK_PATTERN = re.compile(rf"\[\[youtube-({VIDEO_ID_RE})(?=[\]|#])")
YOUTUBE_TOKEN_PATTERN = re.compile(
    rf"youtube-(?!transcripts(?:/|$))({VIDEO_ID_RE})(?=(?:\||\]\]|-(?:transcript|slides|dense-slides|"
    rf"reconstructed-slides)(?:\.md|/|\b)|\.md|/|[`\)\s.,;:#]|$))"
)
RAW_TRANSCRIPT_PATTERN = re.compile(
    rf"(?:^|/)(?:external-youtube-transcripts|youtube-livestream-transcripts|"
    rf"youtube-transcripts)/({VIDEO_ID_RE})\.txt(?=$|[^A-Za-z0-9_-])"
)
PRIMARY_CLAIM_PATTERNS = (
    re.compile(r"\bprimary[\s_-]+event(?:[\s_-]+(?:video|evidence|source))?\b", re.I),
    re.compile(r"\bverified event youtube resource\b", re.I),
    re.compile(r"\bdedicated official recording\b", re.I),
    re.compile(r"\bofficial recording transcript\b", re.I),
    re.compile(r"\bofficial_primary\b", re.I),
    re.compile(r"\bprimary_event_evidence\b", re.I),
    re.compile(r"\bsource role:\s*primary\b", re.I),
)


class SearchIndexParser(HTMLParser):
    """Collect the JSON payload of the static search-index script element."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.in_search_index = False
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.casefold() != "script":
            return
        attributes = {key.casefold(): value for key, value in attrs}
        if attributes.get("id") == "search-index":
            self.in_search_index = True

    def handle_endtag(self, tag: str) -> None:
        if tag.casefold() == "script" and self.in_search_index:
            self.in_search_index = False

    def handle_data(self, data: str) -> None:
        if self.in_search_index:
            self.parts.append(data)


class VisibleTextParser(HTMLParser):
    """Extract visible text without script/style payloads from one page."""

    def __init__(self) -> None:
        super().__init__()
        self.hidden_depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        del attrs
        if tag.casefold() in {"script", "style"}:
            self.hidden_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.casefold() in {"script", "style"} and self.hidden_depth:
            self.hidden_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.hidden_depth:
            self.parts.append(data)


def read_json(path: Path, fallback):
    if not path.is_file():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def manifest_rows(root: Path) -> list[dict]:
    path = root / "raw/sources/official-wf26-video-manifest.json"
    if not path.is_file():
        raise FileNotFoundError(f"official media manifest is required: {path}")
    payload = read_json(path, {})
    rows = payload.get("videos") if isinstance(payload, dict) else None
    if not isinstance(rows, list):
        raise ValueError("official media manifest must contain a videos array")
    return [row for row in rows if isinstance(row, dict)]


def valid_video_id(value: object) -> str | None:
    text = str(value or "")
    return text if re.fullmatch(VIDEO_ID_RE, text) else None


def video_id_from_media_filename(path: Path) -> str | None:
    for pattern in (EXACT_RESOURCE_NAME, EXACT_TRANSCRIPT_NAME, EXACT_DERIVED_NAME):
        match = pattern.fullmatch(path.name)
        if match:
            return match.group(1)
    return None


def extract_watch_ids(text: str) -> set[str]:
    return {match.group(1) for match in WATCH_URL_PATTERN.finditer(text)}


def extract_media_ids(text: str, known_media_ids: set[str]) -> set[str]:
    """Extract explicit references, then intersect ambiguous tokens with known IDs.

    The intersection is deliberate: a bare ``youtube-<11 chars>`` expression
    otherwise mistakes the directory name ``youtube-transcripts`` for a video
    ID.  Exact watch URLs, wiki links, and raw transcript paths remain explicit
    reference forms, but are also intersected so every audit decision comes
    from the deterministic corpus inventory.
    """

    candidates = extract_watch_ids(text)
    candidates.update(match.group(1) for match in WIKILINK_PATTERN.finditer(text))
    candidates.update(match.group(1) for match in RAW_TRANSCRIPT_PATTERN.finditer(text))
    candidates.update(match.group(1) for match in YOUTUBE_TOKEN_PATTERN.finditer(text))
    return candidates & known_media_ids


def has_primary_claim(text: str) -> bool:
    return any(pattern.search(text) for pattern in PRIMARY_CLAIM_PATTERNS)


def contextualizes_as_non_primary(text: str) -> bool:
    """Return whether prose explicitly bounds a reference as non-primary."""

    return any(pattern.search(text) for pattern in CONTEXTUALIZED_CLAIM_PATTERNS)


def claim_units(text: str) -> list[str]:
    """Split flattened Markdown into sentence/list units for claim ownership."""

    return [
        unit
        for unit in re.split(r"(?:\n+|(?<=[.!?])\s+|\s+-\s+)", text)
        if unit
    ]


def has_uncontextualized_primary_claim(text: str) -> bool:
    """Detect a positive primary assertion not bounded in the same claim unit."""

    return any(
        has_primary_claim(unit) and not contextualizes_as_non_primary(unit)
        for unit in claim_units(text)
    )


def primary_reference_ids(
    text: str,
    *,
    known_ids: set[str],
    admitted: set[str],
) -> set[str]:
    """Bind primary assertions to IDs in the same sentence or list item.

    Agent summaries flatten Markdown lists, so `` - `` is treated as a claim
    boundary as well as newlines and sentence endings.  This prevents a page's
    own primary role from leaking onto an incidental, explicitly related video
    elsewhere in its summary.
    """

    video_ids: set[str] = set()
    for unit in claim_units(text):
        if not has_primary_claim(unit) or contextualizes_as_non_primary(unit):
            continue
        video_ids.update(extract_media_ids(unit, known_ids) - admitted)
    return video_ids


def context_prefix(text: str, *, category: str) -> str:
    if category == "transcripts":
        return text.partition("## Transcript")[0]
    if category == "slides":
        candidates = [
            index
            for marker in ("\n## Slide", "\n## OCR", "\n![[assets/")
            if (index := text.find(marker)) >= 0
        ]
        return text[: min(candidates)] if candidates else text
    return text


def visible_html_text(path: Path) -> str:
    parser = VisibleTextParser()
    parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
    return html.unescape(" ".join(parser.parts))


def load_search_records(path: Path) -> list[dict]:
    parser = SearchIndexParser()
    parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
    payload = "".join(parser.parts).strip()
    if not payload:
        raise ValueError("static search index payload is missing")
    rows = json.loads(payload)
    if not isinstance(rows, list):
        raise ValueError("static search index payload must be an array")
    return [row for row in rows if isinstance(row, dict)]


def iter_text_paths(root: Path) -> Iterable[Path]:
    for base, pattern in (
        (root / "wiki", "*.md"),
        (root / "dist/md", "*.md"),
    ):
        if base.is_dir():
            yield from base.rglob(pattern)
    for path in (
        root / "dist/search/index.html",
        root / "dist/agent/pages.jsonl",
        root / "dist/agent/evidence.jsonl",
    ):
        if path.is_file():
            yield path


def collect_known_media_ids(
    root: Path,
    rows: list[dict],
    registry: list[dict],
    *,
    expected_retired_ids: set[str],
) -> set[str]:
    known = set(expected_retired_ids)
    for row in rows:
        if video_id := valid_video_id(row.get("id")):
            known.add(video_id)
    for row in registry:
        if video_id := valid_video_id(row.get("videoId")):
            known.add(video_id)
    for base in (root / "wiki", root / "dist/md"):
        if not base.is_dir():
            continue
        for path in base.rglob("youtube-*.md"):
            if video_id := video_id_from_media_filename(path):
                known.add(video_id)
    for directory_name in (
        "external-youtube-transcripts",
        "youtube-livestream-transcripts",
        "youtube-transcripts",
    ):
        directory = root / "raw/sources" / directory_name
        if not directory.is_dir():
            continue
        for path in directory.glob("*.txt"):
            if video_id := valid_video_id(path.stem):
                known.add(video_id)
    for path in iter_text_paths(root):
        text = path.read_text(encoding="utf-8", errors="ignore")
        known.update(extract_watch_ids(text))
        known.update(match.group(1) for match in WIKILINK_PATTERN.finditer(text))
        known.update(match.group(1) for match in RAW_TRANSCRIPT_PATTERN.finditer(text))
    return known


def add_issue(
    issues: list[dict[str, object]],
    code: str,
    path: Path,
    root: Path,
    **details,
) -> None:
    issues.append(
        {
            "code": code,
            "path": str(path.relative_to(root)),
            **details,
        }
    )


def section_body(text: str, heading: str) -> str | None:
    match = re.search(
        rf"\n## {re.escape(heading)}\n(.*?)(?=\n## |\Z)", text, re.S
    )
    return match.group(1) if match else None


def section_wikilinks(body: str | None) -> set[str]:
    if body is None:
        return set()
    return {
        raw.split("|", 1)[0].split("#", 1)[0].strip()
        for raw in re.findall(r"\[\[([^\]]+)", body)
        if raw.split("|", 1)[0].split("#", 1)[0].strip()
    }


def audit_topic_slide_session_projections(
    root: Path,
    *,
    topics_dir: Path,
    slides_dir: Path,
    issues: list[dict[str, object]],
    code_prefix: str,
) -> None:
    """Compare only generator-owned topic session edges with their listed decks."""

    if not topics_dir.is_dir():
        return
    for topic_path in sorted(topics_dir.glob("*.md")):
        text = topic_path.read_text(encoding="utf-8", errors="ignore")
        deck_section = section_body(text, "Slide-Derived Supporting Decks")
        signal_section = section_body(
            text, "Slide-Derived Scheduled Session Signals"
        )
        if deck_section is None and signal_section is None:
            continue
        deck_targets = {
            target
            for target in section_wikilinks(deck_section)
            if re.fullmatch(rf"youtube-{VIDEO_ID_RE}-slides", target)
        }
        expected: set[str] = set()
        incomplete = False
        for target in sorted(deck_targets):
            slide_page = slides_dir / f"{target}.md"
            if not slide_page.is_file():
                add_issue(
                    issues,
                    f"{code_prefix}_topic_slide_deck_missing",
                    topic_path,
                    root,
                    deck=target,
                )
                incomplete = True
                continue
            related = section_body(
                slide_page.read_text(encoding="utf-8", errors="ignore"),
                "Related Scheduled Sessions",
            )
            if related is None:
                add_issue(
                    issues,
                    f"{code_prefix}_slide_related_sessions_missing",
                    slide_page,
                    root,
                    topic=topic_path.stem,
                )
                incomplete = True
                continue
            expected.update(section_wikilinks(related))
        if incomplete:
            continue
        actual = section_wikilinks(signal_section)
        extra = sorted(actual - expected)
        missing = sorted(expected - actual)
        if extra or missing:
            add_issue(
                issues,
                f"{code_prefix}_topic_slide_session_projection_mismatch",
                topic_path,
                root,
                extra_talks=extra,
                missing_talks=missing,
            )


def audit_livestream_segment_projections(
    root: Path,
    *,
    manifest: list[dict],
    segments: list[dict],
    talks_dir: Path,
    issues: list[dict[str, object]],
    code_prefix: str,
) -> None:
    """Require exact current broad-stream timestamps on their owned talk pages."""

    dedicated_talks = {
        str(slug)
        for video in manifest
        if video.get("mediaType") == "talk_recording"
        and video.get("playlistAvailability") == "available"
        and video.get("videoAvailability") in {"public", "unlisted"}
        and isinstance(video.get("matchedTalks"), list)
        for slug in video["matchedTalks"]
        if isinstance(slug, str) and slug
    }
    expected_by_talk: dict[str, set[tuple[str, int]]] = {}
    for row in segments:
        slug = str(row.get("talk_slug") or "")
        video_id = str(row.get("video_id") or "")
        seconds = row.get("start_seconds")
        if (
            row.get("confidence") != "high"
            or not slug
            or not valid_video_id(video_id)
            or not isinstance(seconds, int)
            or seconds < 0
            or slug in dedicated_talks
        ):
            continue
        expected_by_talk.setdefault(slug, set()).add((video_id, seconds))

    if not talks_dir.is_dir():
        return
    paths = {path.stem: path for path in sorted(talks_dir.glob("*.md"))}
    for slug in sorted(set(paths) | set(expected_by_talk)):
        path = paths.get(slug, talks_dir / f"{slug}.md")
        expected = expected_by_talk.get(slug, set())
        if not path.is_file():
            add_issue(
                issues,
                f"{code_prefix}_livestream_segment_talk_missing",
                path,
                root,
                expected_segments=sorted([list(value) for value in expected]),
            )
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        heading_count = len(re.findall(r"(?m)^## Livestream Segment\s*$", text))
        body = section_body(text, "Livestream Segment")
        actual = {
            (match.group(1), int(match.group(2)))
            for match in re.finditer(
                rf"youtube\.com/watch\?v=({VIDEO_ID_RE})&t=(\d+)s",
                body or "",
            )
        }
        if heading_count != (1 if expected else 0) or actual != expected:
            add_issue(
                issues,
                f"{code_prefix}_livestream_segment_projection_mismatch",
                path,
                root,
                heading_count=heading_count,
                extra_segments=sorted([list(value) for value in actual - expected]),
                missing_segments=sorted([list(value) for value in expected - actual]),
            )


def audit_markdown_tree(
    root: Path,
    base: Path,
    *,
    known_ids: set[str],
    admitted: set[str],
    manifest_ids: set[str],
    issues: list[dict[str, object]],
    code_prefix: str,
) -> None:
    if not base.is_dir():
        add_issue(issues, f"{code_prefix}_markdown_root_missing", base, root)
        return
    for path in sorted(base.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        category = path.parent.name
        scan_text = context_prefix(text, category=category)
        file_video_id = video_id_from_media_filename(path)

        if file_video_id and file_video_id not in admitted and has_primary_claim(scan_text):
            add_issue(
                issues,
                f"{code_prefix}_non_admitted_file_primary_context",
                path,
                root,
                video_id=file_video_id,
            )
        if (
            category == "resources"
            and file_video_id
            and file_video_id not in manifest_ids
            and not any(marker in text.casefold() for marker in CONTEXT_MARKERS)
        ):
            add_issue(
                issues,
                f"{code_prefix}_non_manifest_resource_not_contextualized",
                path,
                root,
                video_id=file_video_id,
            )

        for line_number, line in enumerate(scan_text.splitlines(), start=1):
            if not has_primary_claim(line):
                continue
            for video_id in sorted(extract_media_ids(line, known_ids) - admitted):
                add_issue(
                    issues,
                    f"{code_prefix}_non_admitted_primary_reference",
                    path,
                    root,
                    line=line_number,
                    video_id=video_id,
                )


def audit_static_product(
    root: Path,
    *,
    manifest: list[dict],
    segments: list[dict],
    known_ids: set[str],
    admitted: set[str],
    manifest_ids: set[str],
    issues: list[dict[str, object]],
) -> None:
    static_md = root / "dist/md"
    audit_markdown_tree(
        root,
        static_md,
        known_ids=known_ids,
        admitted=admitted,
        manifest_ids=manifest_ids,
        issues=issues,
        code_prefix="static",
    )
    audit_topic_slide_session_projections(
        root,
        topics_dir=static_md / "topics",
        slides_dir=static_md / "slides",
        issues=issues,
        code_prefix="static",
    )
    audit_livestream_segment_projections(
        root,
        manifest=manifest,
        segments=segments,
        talks_dir=static_md / "talks",
        issues=issues,
        code_prefix="static",
    )

    canonical_media_paths: list[Path] = []
    for category in ("resources", "transcripts", "slides"):
        directory = root / "wiki" / category
        if not directory.is_dir():
            continue
        canonical_media_paths.extend(
            path
            for path in directory.glob("youtube-*.md")
            if video_id_from_media_filename(path)
        )

    expected_search_urls: dict[str, str] = {}
    for canonical in sorted(canonical_media_paths):
        relative = canonical.relative_to(root / "wiki")
        exported_md = static_md / relative
        video_id = video_id_from_media_filename(canonical)
        if not exported_md.is_file():
            add_issue(
                issues,
                "static_media_markdown_missing",
                exported_md,
                root,
                video_id=video_id,
            )
        elif canonical.read_bytes() != exported_md.read_bytes():
            add_issue(
                issues,
                "static_media_markdown_stale",
                exported_md,
                root,
                video_id=video_id,
            )

        html_path = root / "dist" / relative.parent / relative.stem / "index.html"
        if not html_path.is_file():
            add_issue(
                issues,
                "static_media_html_missing",
                html_path,
                root,
                video_id=video_id,
            )
        elif video_id not in admitted and has_primary_claim(visible_html_text(html_path)):
            add_issue(
                issues,
                "static_non_admitted_html_primary_context",
                html_path,
                root,
                video_id=video_id,
            )
        expected_search_urls[f"/{relative.parent.as_posix()}/{relative.stem}/"] = str(video_id)

    search_path = root / "dist/search/index.html"
    if not search_path.is_file():
        add_issue(issues, "static_search_index_missing", search_path, root)
        return
    try:
        search_rows = load_search_records(search_path)
    except (json.JSONDecodeError, ValueError) as exc:
        add_issue(
            issues,
            "static_search_index_invalid",
            search_path,
            root,
            detail=str(exc),
        )
        return

    rows_by_url: dict[str, list[dict]] = {}
    for row in search_rows:
        url = str(row.get("url") or "")
        rows_by_url.setdefault(url, []).append(row)
        record_text = "\n".join(
            str(row.get(key) or "") for key in ("url", "title", "excerpt")
        )
        for video_id in sorted(extract_media_ids(record_text, known_ids) - admitted):
            if has_primary_claim(str(row.get("excerpt") or "")):
                add_issue(
                    issues,
                    "static_search_non_admitted_primary_context",
                    search_path,
                    root,
                    video_id=video_id,
                    url=url,
                )
    for url, video_id in sorted(expected_search_urls.items()):
        count = len(rows_by_url.get(url, []))
        if count != 1:
            add_issue(
                issues,
                "static_media_search_record_count",
                search_path,
                root,
                video_id=video_id,
                url=url,
                count=count,
            )


def audit_jsonl(
    path: Path,
    root: Path,
    *,
    known_ids: set[str],
    admitted: set[str],
    issues: list[dict[str, object]],
    kind: str,
    page_media_ids: dict[str, set[str]] | None = None,
) -> dict[str, set[str]]:
    owned_media_by_page: dict[str, set[str]] = {}
    if not path.is_file():
        add_issue(issues, f"agent_{kind}_missing", path, root)
        return owned_media_by_page
    for line_number, line in enumerate(
        path.read_text(encoding="utf-8", errors="ignore").splitlines(), start=1
    ):
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            add_issue(
                issues,
                f"invalid_agent_{kind}_json",
                path,
                root,
                line=line_number,
            )
            continue
        if not isinstance(row, dict):
            add_issue(
                issues,
                f"invalid_agent_{kind}_record",
                path,
                root,
                line=line_number,
            )
            continue

        if kind == "page":
            roles_value = row.get("sourceRoles")
            roles = (
                {str(role) for role in roles_value}
                if isinstance(roles_value, list)
                else set()
            )
            identity_text = "\n".join(
                [
                    str(row.get("sourcePath") or ""),
                    str(row.get("renderedPath") or ""),
                ]
            )
            primary_text = str(row.get("summary") or "")
            role_ids = extract_media_ids(identity_text, known_ids) - admitted
            page_id = str(row.get("id") or "")
            if page_id:
                owned_media_by_page[page_id] = set(role_ids)
        else:
            roles = {str(row.get("sourceRole") or "")}
            locator_text = str(row.get("locator") or "")
            primary_text = str(row.get("excerpt") or "")
            role_ids = extract_media_ids(locator_text, known_ids) - admitted

        for video_id in sorted(role_ids):
            if roles & PRIMARY_SOURCE_ROLES:
                add_issue(
                    issues,
                    f"agent_{kind}_non_admitted_primary_role",
                    path,
                    root,
                    line=line_number,
                    video_id=video_id,
                    source_roles=sorted(roles),
                )

        if kind == "page":
            identity_ids = set(role_ids)
        else:
            page_id = str(row.get("pageId") or "")
            identity_ids = set(role_ids)
            identity_ids.update((page_media_ids or {}).get(page_id, set()))

        context_ids = primary_reference_ids(
            primary_text,
            known_ids=known_ids,
            admitted=admitted,
        )
        if (
            identity_ids
            and has_uncontextualized_primary_claim(primary_text)
        ):
            context_ids.update(identity_ids)

        for video_id in sorted(context_ids):
            add_issue(
                issues,
                f"agent_{kind}_non_admitted_primary_context",
                path,
                root,
                line=line_number,
                video_id=video_id,
            )

    return owned_media_by_page


def audit_corpus(
    root: Path,
    *,
    phase: str = "full",
    retired_ids: set[str] | None = None,
) -> dict:
    if phase not in {"pre-agent", "full"}:
        raise ValueError(f"unsupported audit phase: {phase}")
    root = root.resolve()
    expected_retired = DURABLE_RETIRED_IDS | (retired_ids or set())
    rows = manifest_rows(root)
    manifest_ids = {
        video_id
        for row in rows
        if (video_id := valid_video_id(row.get("id"))) is not None
    }
    admitted = {
        str(row["id"])
        for row in rows
        if valid_video_id(row.get("id"))
        and row.get("mediaType") in PLAYABLE_MEDIA_TYPES
        and str(row.get("videoAvailability") or "").casefold()
        in PLAYABLE_VIDEO_AVAILABILITIES
        and str(row.get("playlistAvailability") or "").casefold()
        in PLAYABLE_PLAYLIST_AVAILABILITIES
    }
    streams = {
        str(row["id"])
        for row in rows
        if str(row.get("id") or "") in admitted
        and row.get("mediaType") == "event_livestream"
    }
    issues: list[dict[str, object]] = []

    manifest_id_list = [
        video_id
        for row in rows
        if (video_id := valid_video_id(row.get("id"))) is not None
    ]
    duplicates = sorted(
        {video_id for video_id in manifest_id_list if manifest_id_list.count(video_id) > 1}
    )
    for video_id in duplicates:
        add_issue(
            issues,
            "duplicate_manifest_video_id",
            root / "raw/sources/official-wf26-video-manifest.json",
            root,
            video_id=video_id,
        )

    registry_path = root / "wiki/transcripts/registry.json"
    registry_payload = read_json(registry_path, [])
    if not isinstance(registry_payload, list):
        add_issue(issues, "transcript_registry_invalid", registry_path, root)
        registry: list[dict] = []
    else:
        registry = [row for row in registry_payload if isinstance(row, dict)]

    known_ids = collect_known_media_ids(
        root,
        rows,
        registry,
        expected_retired_ids=expected_retired,
    )
    non_admitted = known_ids - admitted
    non_manifest = known_ids - manifest_ids

    audit_markdown_tree(
        root,
        root / "wiki",
        known_ids=known_ids,
        admitted=admitted,
        manifest_ids=manifest_ids,
        issues=issues,
        code_prefix="canonical",
    )
    audit_topic_slide_session_projections(
        root,
        topics_dir=root / "wiki/topics",
        slides_dir=root / "wiki/slides",
        issues=issues,
        code_prefix="canonical",
    )

    segment_path = root / "raw/sources/livestream-talk-segments.json"
    segments = read_json(segment_path, [])
    if isinstance(segments, list):
        for index, row in enumerate(segments):
            if not isinstance(row, dict):
                continue
            video_id = str(row.get("video_id") or "")
            if video_id and video_id not in streams:
                add_issue(
                    issues,
                    "segment_stream_not_admitted",
                    segment_path,
                    root,
                    index=index,
                    video_id=video_id,
                )
    projection_segments = (
        [row for row in segments if isinstance(row, dict)]
        if isinstance(segments, list)
        else []
    )
    audit_livestream_segment_projections(
        root,
        manifest=rows,
        segments=projection_segments,
        talks_dir=root / "wiki/talks",
        issues=issues,
        code_prefix="canonical",
    )

    for index, row in enumerate(registry):
        video_id = str(row.get("videoId") or "")
        source_role = str(row.get("sourceRole") or "")
        if source_role in PRIMARY_SOURCE_ROLES and video_id not in admitted:
            add_issue(
                issues,
                "transcript_primary_role_not_admitted",
                registry_path,
                root,
                index=index,
                video_id=video_id,
                source_role=source_role,
            )

    for video_id in sorted(expected_retired):
        resource = root / "wiki/resources" / f"youtube-{video_id}.md"
        if not resource.is_file():
            add_issue(
                issues,
                "retired_supporting_resource_missing",
                resource,
                root,
                video_id=video_id,
            )

    audit_static_product(
        root,
        manifest=rows,
        segments=projection_segments,
        known_ids=known_ids,
        admitted=admitted,
        manifest_ids=manifest_ids,
        issues=issues,
    )

    if phase == "full":
        page_media_ids = audit_jsonl(
            root / "dist/agent/pages.jsonl",
            root,
            known_ids=known_ids,
            admitted=admitted,
            issues=issues,
            kind="page",
        )
        audit_jsonl(
            root / "dist/agent/evidence.jsonl",
            root,
            known_ids=known_ids,
            admitted=admitted,
            issues=issues,
            kind="evidence",
            page_media_ids=page_media_ids,
        )

    return {
        "ok": not issues,
        "phase": phase,
        "known_media_ids": sorted(known_ids),
        "manifest_ids": sorted(manifest_ids),
        "admitted_primary_ids": sorted(admitted),
        "admitted_stream_ids": sorted(streams),
        "non_admitted_ids": sorted(non_admitted),
        "retired_ids": sorted(non_manifest),
        "durable_retired_ids": sorted(expected_retired),
        "issues": issues,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--phase", choices=("pre-agent", "full"), default="full")
    parser.add_argument("--retired-video-id", action="append", default=[])
    args = parser.parse_args()
    report = audit_corpus(
        args.root,
        phase=args.phase,
        retired_ids=set(args.retired_video_id),
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
