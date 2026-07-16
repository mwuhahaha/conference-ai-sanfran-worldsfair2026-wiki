#!/usr/bin/env python3
"""Audit third-party wiki connections without mutating public wiki content."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable, Mapping
from urllib.parse import urlsplit

try:
    from wiki_from_topic_maker.public_artifact_policy import scan_public_artifacts as _shared_scan_public_artifacts
except ModuleNotFoundError as exc:
    if exc.name not in {"wiki_from_topic_maker", "wiki_from_topic_maker.public_artifact_policy"}:
        raise
    _shared_scan_public_artifacts = None

from third_party_connection_policy import INTERNAL_DIR, assess_connection, normalize_url, write_internal_policy


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw" / "sources"
REPORT_PATH = INTERNAL_DIR / "latest-audit.json"
URL_RE = re.compile(r'https?://[^\s)\]>"\']+')
PROFILE_HOSTS = {"linkedin.com", "x.com", "twitter.com"}
OFFICIAL_HOSTS = {"ai.engineer", "aie-wf.sentry.dev", "aie-worldsfair2026.plusrobot.ai"}
PARKED_SITE_MARKERS = {
    "domain is available for acquisition",
    "buy this domain",
    "for sale",
    "spaceship",
}
EXTERNAL_REPORT_FORBIDDEN_KEYS = {
    "company_hits",
    "event_marker",
    "known_in_official_channel_cache",
    "limits",
    "operator_promotion",
    "phrase_overlap",
    "reasons",
    "recapish",
    "score",
    "speaker_hits",
    "talkish",
    "title_overlap",
    "usefulness",
}
PUBLIC_COMPANY_FORBIDDEN_KEYS = {"fetchConfidence"}
EXTERNAL_SECTION_RE = re.compile(
    r"^## External (?:Video Discovery|Secondary Source Candidates)\n.*?(?=^## |\Z)",
    re.M | re.S,
)
PUBLIC_RANKING_LINE_PATTERNS = (
    ("numeric confidence", re.compile(r"^\s*-\s+Confidence(?: label)?:\s*[^\n]*\(\s*\d", re.M | re.I)),
    ("match reasons", re.compile(r"^\s*-\s+(?:Match evidence|Reasons):", re.M | re.I)),
    ("calibration rules", re.compile(r"^## Matching Rules\s*$", re.M)),
)
PUBLIC_ARTIFACT_SUFFIXES = {".md", ".markdown", ".json", ".jsonl", ".html", ".htm"}
PRIVATE_ARTIFACT_DIRECTORIES = {".git", ".ops", "__pycache__", "node_modules"}
RANKING_METADATA_TERMS = {
    "score", "scores", "scoring", "rank", "ranks", "ranking", "weight", "weights",
    "weighted", "calibration", "calibrated", "confidence",
}
INTERNAL_KEY_CONTEXT_TERMS = {
    "internal", "match", "matched", "matching", "candidate", "retrieval", "relevance",
    "credibility", "ranking",
}
MATCH_DETAIL_TERMS = {
    "basis", "company", "confidence", "evidence", "overlap", "rank", "reasons", "score",
    "signals", "speakers", "terms", "title", "weight",
}
CALIBRATION_DETAIL_TERMS = {"fixture", "marker", "policy", "rank", "rules", "score", "weight"}
GENERIC_RANKING_KEYS = {"score", "rank", "weight"}
INTERNAL_JSON_CONTAINER_TERMS = {
    "match", "matches", "matched", "matching", "candidate", "candidates", "retrieval", "relevance",
}
CAMEL_BOUNDARY_RE = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
NUMERIC_VALUE_RE = re.compile(r"^[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[-+]?\d+)?%?$", re.I)
INTERNAL_TEXT_RE = re.compile(
    r"\(\s*(?:internal|match|matching|candidate|ranking|retrieval|relevance|credibility)"
    r"[ _-]+(?:score|rank|ranking|weight|calibration)\s*(?:[:=]|is)?\s*[-+]?(?:\d+(?:\.\d*)?|\.\d+)"
    r"|^\s*(?:[-*+]\s*)?(?:internal|match|matching|candidate|ranking|retrieval|relevance|credibility)"
    r"[ _-]+(?:score|rank|ranking|weight|calibration)\s*(?:[:=]|is)?\s*[-+]?(?:\d+(?:\.\d*)?|\.\d+)%?\s*$"
    r"|^\s*#{1,6}\s+matching rules\s*$",
    re.I | re.M,
)
HTML_ATTRIBUTE_RE = re.compile(r"\b([a-zA-Z_:][\w:.-]*)\s*=\s*([\"'])(.*?)\2", re.S)
INTERNAL_RELATIONSHIP_TEXT_RE = re.compile(
    r"\b(?:speaker|topic|title|candidate)[ _-]+match(?:ed|ing)?\b"
    r"|\b(?:match|matching|candidate|retrieval|relevance)\b.{0,80}"
    r"\b(?:basis|rationale|reason|related)\b",
    re.I,
)


@dataclass(frozen=True)
class FallbackPublicArtifactIssue:
    path: Path
    artifact_format: str
    code: str
    location: str
    marker: str


@dataclass(frozen=True)
class FallbackPublicArtifactScanResult:
    checked_files: tuple[Path, ...]
    issues: tuple[FallbackPublicArtifactIssue, ...]

    @property
    def ok(self) -> bool:
        return not self.issues


def load_json(path: Path, fallback):
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8", errors="ignore"))


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", value)).strip("-")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return fields


def urls(text: str) -> set[str]:
    return {match.group(0).rstrip("/.,;:#") for match in URL_RE.finditer(text)}


def host(value: str) -> str:
    return (urlsplit(value).hostname or "").lower().removeprefix("www.")


def package_project_names(text: str) -> set[str]:
    """Return owner-controlled package names that can corroborate a repository."""
    names: set[str] = set()
    for value in urls(text):
        parts = urlsplit(value)
        if host(value) != "pypi.org":
            continue
        segments = [segment for segment in parts.path.split("/") if segment]
        if len(segments) >= 2 and segments[0].lower() == "project":
            names.add(slugify(segments[1]))
    return names


def severity_rank(value: str) -> int:
    return {"critical": 0, "high": 1, "medium": 2, "low": 3}.get(value, 4)


def finding(
    severity: str,
    kind: str,
    path: Path,
    reason: str,
    *,
    url: str = "",
    evidence: list[str] | None = None,
    project_root: Path = ROOT,
) -> dict:
    return {
        "severity": severity,
        "kind": kind,
        "page": str(path.relative_to(project_root)),
        "url": url,
        "reason": reason,
        "evidence": evidence or [],
    }


def forbidden_json_key_paths(value, forbidden: set[str], prefix: str = "$") -> list[str]:
    """Return structural key paths without treating ordinary prose as a leak."""
    paths: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{prefix}.{key}"
            if key in forbidden:
                paths.append(child_path)
            paths.extend(forbidden_json_key_paths(child, forbidden, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            paths.extend(forbidden_json_key_paths(child, forbidden, f"{prefix}[{index}]"))
    return paths


def public_ranking_markers(text: str) -> list[str]:
    """Find generated ranking syntax while ignoring prose uses of confidence."""
    return [label for label, pattern in PUBLIC_RANKING_LINE_PATTERNS if pattern.search(text)]


def _fallback_key_terms(value: str) -> tuple[str, ...]:
    separated = CAMEL_BOUNDARY_RE.sub("_", value.removeprefix("data-").strip())
    return tuple(term for term in re.split(r"[^a-zA-Z0-9]+", separated.lower()) if term)


def _fallback_forbidden_key(value: str, metadata_value: Any = None) -> bool:
    terms = set(_fallback_key_terms(value))
    if not terms or _fallback_categorical_internal_boundary(terms, metadata_value):
        return False
    if terms == {"confidence", "score"}:
        return True
    if terms & {"match", "matching", "retrieval", "relevance", "credibility", "ranking"}:
        if isinstance(metadata_value, (int, float)) and not isinstance(metadata_value, bool):
            return True
    if "calibration" in terms and terms & CALIBRATION_DETAIL_TERMS:
        return True
    if terms & {"match", "matched", "matching"} and terms & MATCH_DETAIL_TERMS:
        return True
    return bool(terms & INTERNAL_KEY_CONTEXT_TERMS and terms & RANKING_METADATA_TERMS)


def _fallback_categorical_internal_boundary(terms: set[str], value: Any) -> bool:
    return bool(
        {"internal", "only"} <= terms
        and isinstance(value, (bool, str))
        and (value is True or str(value).strip().lower() == "true")
    )


def _fallback_numeric_confidence(key: str, value: Any) -> bool:
    terms = set(_fallback_key_terms(key))
    if "confidence" not in terms:
        return False
    if not terms & INTERNAL_KEY_CONTEXT_TERMS and terms != {"confidence", "score"}:
        return False
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return True
    return isinstance(value, str) and bool(NUMERIC_VALUE_RE.fullmatch(value.strip()))


def _fallback_generic_ranking_key(value: str) -> bool:
    terms = _fallback_key_terms(value)
    return len(terms) == 1 and terms[0] in GENERIC_RANKING_KEYS


def _fallback_container_proves_internal_matching(value: str) -> bool:
    terms = set(_fallback_key_terms(value))
    return bool(
        terms & INTERNAL_JSON_CONTAINER_TERMS
        or {"related", "video"} <= terms
    )


def _fallback_mapping_proves_internal_matching(value: Mapping[Any, Any]) -> bool:
    for key, child in value.items():
        terms = set(_fallback_key_terms(str(key)))
        if "matched" in terms and not isinstance(child, Mapping):
            return True
        if not isinstance(child, Mapping) and (
            {"speaker", "hit"} <= terms or {"topic", "overlap"} <= terms
        ):
            return True
        if "basis" in terms and terms & {"match", "matching"}:
            return True
        if (
            terms & {"relationship", "rationale", "reason"}
            and isinstance(child, str)
            and INTERNAL_RELATIONSHIP_TEXT_RE.search(child)
        ):
            return True
    return False


def _fallback_files(roots: Iterable[Path]) -> tuple[Path, ...]:
    found: set[Path] = set()
    for root in roots:
        if root.name in PRIVATE_ARTIFACT_DIRECTORIES:
            continue
        paths = (root,) if root.is_file() else root.rglob("*") if root.is_dir() else ()
        for path in paths:
            if not path.is_file() or path.suffix.lower() not in PUBLIC_ARTIFACT_SUFFIXES:
                continue
            if any(part in PRIVATE_ARTIFACT_DIRECTORIES for part in path.relative_to(root).parts):
                continue
            found.add(path)
    return tuple(sorted(found))


def _fallback_json_issues(
    path: Path,
    value: Any,
    location: str = "$",
    *,
    internal_context: bool = False,
) -> list[FallbackPublicArtifactIssue]:
    issues: list[FallbackPublicArtifactIssue] = []
    if isinstance(value, Mapping):
        mapping_context = internal_context or _fallback_mapping_proves_internal_matching(value)
        for key, child in value.items():
            child_location = f"{location}.{key}"
            if _fallback_forbidden_key(str(key), child):
                issues.append(FallbackPublicArtifactIssue(path, "json", "internal_metadata_key", child_location, str(key)))
            elif mapping_context and _fallback_generic_ranking_key(str(key)):
                issues.append(FallbackPublicArtifactIssue(path, "json", "internal_metadata_key", child_location, str(key)))
            elif _fallback_numeric_confidence(str(key), child):
                issues.append(FallbackPublicArtifactIssue(path, "json", "numeric_confidence", child_location, str(child)))
            issues.extend(
                _fallback_json_issues(
                    path,
                    child,
                    child_location,
                    internal_context=(
                        mapping_context or _fallback_container_proves_internal_matching(str(key))
                    ),
                )
            )
    elif isinstance(value, list):
        for index, child in enumerate(value):
            issues.extend(
                _fallback_json_issues(
                    path,
                    child,
                    f"{location}[{index}]",
                    internal_context=internal_context,
                )
            )
    elif isinstance(value, str):
        for match in INTERNAL_TEXT_RE.finditer(value):
            issues.append(FallbackPublicArtifactIssue(path, "json", "internal_metadata_text", location, match.group(0)))
    return issues


class _FallbackArtifactHTMLParser(HTMLParser):
    def __init__(self, path: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.path = path
        self.issues: list[FallbackPublicArtifactIssue] = []
        self.blockquote_depth = 0
        self.json_script_depth = 0
        self.json_script_chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "blockquote":
            self.blockquote_depth += 1
        attrs_map = {name: value for name, value in attrs}
        if tag == "script" and (attrs_map.get("type") or "").lower() in {
            "application/json",
            "application/ld+json",
        }:
            self.json_script_depth += 1
        for name, value in attrs:
            if _fallback_forbidden_key(name, value or ""):
                self.issues.append(FallbackPublicArtifactIssue(
                    self.path,
                    "html",
                    "internal_html_attribute",
                    f"line {self.getpos()[0]}",
                    name,
                ))
            elif _fallback_numeric_confidence(name, value or ""):
                self.issues.append(FallbackPublicArtifactIssue(
                    self.path,
                    "html",
                    "numeric_confidence",
                    f"line {self.getpos()[0]}",
                    value or "",
                ))
        if tag == "meta":
            metadata_name = attrs_map.get("name") or attrs_map.get("property") or ""
            metadata_value = attrs_map.get("content") or ""
            if _fallback_forbidden_key(metadata_name, metadata_value):
                self.issues.append(FallbackPublicArtifactIssue(
                    self.path,
                    "html",
                    "internal_html_metadata",
                    f"line {self.getpos()[0]}",
                    metadata_name,
                ))
            elif _fallback_numeric_confidence(metadata_name, metadata_value):
                self.issues.append(FallbackPublicArtifactIssue(
                    self.path,
                    "html",
                    "numeric_confidence",
                    f"line {self.getpos()[0]}",
                    metadata_value,
                ))

    def handle_endtag(self, tag: str) -> None:
        if tag == "blockquote" and self.blockquote_depth:
            self.blockquote_depth -= 1
        if tag == "script" and self.json_script_depth:
            raw = "".join(self.json_script_chunks).strip()
            if raw:
                try:
                    value = json.loads(raw)
                except json.JSONDecodeError as exc:
                    self.issues.append(FallbackPublicArtifactIssue(
                        self.path,
                        "html",
                        "invalid_json",
                        f"embedded JSON line {exc.lineno}, column {exc.colno}",
                        exc.msg,
                    ))
                else:
                    for issue in _fallback_json_issues(self.path, value):
                        self.issues.append(FallbackPublicArtifactIssue(
                            self.path,
                            "html",
                            issue.code,
                            f"embedded JSON {issue.location}",
                            issue.marker,
                        ))
            self.json_script_chunks.clear()
            self.json_script_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.json_script_depth:
            self.json_script_chunks.append(data)
            return
        if self.blockquote_depth:
            return
        for match in INTERNAL_TEXT_RE.finditer(data):
            self.issues.append(FallbackPublicArtifactIssue(
                self.path,
                "html",
                "internal_metadata_text",
                f"line {self.getpos()[0]}",
                match.group(0),
            ))


def _fallback_text_issues(path: Path, text: str, artifact_format: str) -> list[FallbackPublicArtifactIssue]:
    issues: list[FallbackPublicArtifactIssue] = []
    if artifact_format == "html":
        parser = _FallbackArtifactHTMLParser(path)
        parser.feed(text)
        parser.close()
        return parser.issues
    if artifact_format == "markdown":
        lines = text.splitlines()
        in_frontmatter = bool(lines and lines[0].strip() == "---")
        for line_number, line in enumerate(lines, start=1):
            if line_number == 1 and in_frontmatter:
                continue
            if in_frontmatter and line.strip() == "---":
                in_frontmatter = False
                continue
            if in_frontmatter:
                key, separator, value = line.partition(":")
                if separator and _fallback_forbidden_key(key.strip(), value.strip()):
                    issues.append(FallbackPublicArtifactIssue(path, "markdown", "internal_frontmatter_key", f"line {line_number}", key.strip()))
                elif separator and _fallback_numeric_confidence(key.strip(), value.strip()):
                    issues.append(FallbackPublicArtifactIssue(path, "markdown", "numeric_confidence", f"line {line_number}", value.strip()))
                continue
            if line.lstrip().startswith(">"):
                continue
            for match in INTERNAL_TEXT_RE.finditer(line):
                issues.append(FallbackPublicArtifactIssue(path, "markdown", "internal_metadata_text", f"line {line_number}", match.group(0)))
    for match in HTML_ATTRIBUTE_RE.finditer(text):
        name, _quote, value = match.groups()
        line_number = text.count("\n", 0, match.start()) + 1
        if _fallback_forbidden_key(name, value):
            issues.append(FallbackPublicArtifactIssue(path, artifact_format, "internal_html_attribute", f"line {line_number}", name))
        elif _fallback_numeric_confidence(name, value):
            issues.append(FallbackPublicArtifactIssue(path, artifact_format, "numeric_confidence", f"line {line_number}", value))
    return issues


def _fallback_scan_public_artifacts(roots: tuple[Path, ...]) -> FallbackPublicArtifactScanResult:
    files = _fallback_files(roots)
    issues: list[FallbackPublicArtifactIssue] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        suffix = path.suffix.lower()
        if suffix in {".json", ".jsonl"}:
            rows = (
                ((line_number, line) for line_number, line in enumerate(text.splitlines(), start=1) if line.strip())
                if suffix == ".jsonl"
                else ((1, text),)
            )
            for line_number, raw in rows:
                try:
                    value = json.loads(raw)
                except json.JSONDecodeError as exc:
                    issues.append(FallbackPublicArtifactIssue(
                        path,
                        "json",
                        "invalid_json",
                        f"line {line_number + exc.lineno - 1}, column {exc.colno}",
                        exc.msg,
                    ))
                    continue
                prefix = f"$line[{line_number}]" if suffix == ".jsonl" else "$"
                issues.extend(_fallback_json_issues(path, value, prefix))
        else:
            artifact_format = "html" if suffix in {".html", ".htm"} else "markdown"
            issues.extend(_fallback_text_issues(path, text, artifact_format))
    ordered = tuple(sorted(issues, key=lambda issue: (str(issue.path), issue.location, issue.code, issue.marker)))
    return FallbackPublicArtifactScanResult(files, ordered)


def scan_publishable_artifacts(project_root: Path = ROOT):
    """Scan every public wiki, static, and raw-source Markdown/JSON/HTML artifact."""
    roots = (project_root / "wiki", project_root / "dist", project_root / "raw" / "sources")
    if _shared_scan_public_artifacts is not None:
        return _shared_scan_public_artifacts(roots)
    return _fallback_scan_public_artifacts(roots)


def _public_artifact_finding(issue, project_root: Path) -> dict:
    raw_source = _is_raw_source_path(issue.path, project_root)
    return finding(
        "critical",
        (
            f"raw_source_internal_ranking_{issue.artifact_format}"
            if raw_source
            else f"public_internal_ranking_{issue.artifact_format}"
        ),
        issue.path,
        (
            "A raw source artifact contains structurally identified internal matching or ranking metadata."
            if raw_source
            else "A publishable artifact contains structurally identified internal ranking or calibration metadata."
        ),
        evidence=[f"{issue.code} at {issue.location}: {issue.marker}"],
        project_root=project_root,
    )


def _is_raw_source_path(path: Path, project_root: Path) -> bool:
    try:
        path.relative_to(project_root / "raw" / "sources")
    except ValueError:
        return False
    return True


def audit_public_ranking_artifacts(
    findings: list[dict],
    counters: Counter,
    project_root: Path = ROOT,
) -> int:
    leak_count = 0
    raw = project_root / "raw" / "sources"
    json_targets = (
        (raw / "external-video-discovery-latest.json", EXTERNAL_REPORT_FORBIDDEN_KEYS),
        (raw / "company-profiles.json", PUBLIC_COMPANY_FORBIDDEN_KEYS),
    )
    for path, forbidden in json_targets:
        if not path.exists():
            continue
        key_paths = forbidden_json_key_paths(load_json(path, {}), forbidden)
        if not key_paths:
            counters["public_json_without_internal_ranking_keys"] += 1
            continue
        leak_count += len(key_paths)
        findings.append(finding(
            "critical",
            "raw_source_internal_ranking_key",
            path,
            "A public JSON artifact contains internal ranking or calibration keys that belong only under ignored .ops state.",
            evidence=key_paths[:25],
            project_root=project_root,
        ))

    scan = scan_publishable_artifacts(project_root)
    raw_files = {path for path in scan.checked_files if _is_raw_source_path(path, project_root)}
    public_files = set(scan.checked_files) - raw_files
    raw_affected_files = {
        issue.path for issue in scan.issues if _is_raw_source_path(issue.path, project_root)
    }
    public_affected_files = {issue.path for issue in scan.issues} - raw_affected_files
    counters["publishable_artifact_files_scanned"] += len(public_files)
    counters["publishable_artifact_files_without_internal_ranking"] += (
        len(public_files) - len(public_affected_files)
    )
    counters["raw_source_artifact_files_scanned"] += len(raw_files)
    counters["raw_source_artifact_files_without_internal_ranking"] += (
        len(raw_files) - len(raw_affected_files)
    )
    counters["raw_source_internal_ranking_findings"] += sum(
        1 for issue in scan.issues if _is_raw_source_path(issue.path, project_root)
    )
    leak_count += len(scan.issues)
    findings.extend(_public_artifact_finding(issue, project_root) for issue in scan.issues)
    return leak_count


def official_speaker_sources() -> tuple[dict[str, set[str]], dict[str, dict]]:
    speakers = load_json(RAW / "official-speakers.json", {}).get("speakers", [])
    sources: dict[str, set[str]] = {}
    records = {}
    for speaker in speakers:
        slug = slugify(speaker.get("name", ""))
        sources[slug] = {
            normalize_url(speaker[key])
            for key in ("linkedin", "twitter", "website", "blog")
            if speaker.get(key)
        }
        records[slug] = speaker
    return sources, records


def official_sessions_by_title() -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for session in load_json(RAW / "official-sessions.json", {}).get("sessions", []):
        grouped[session.get("title", "")].append(session)
    return grouped


def audit_people(findings: list[dict], counters: Counter) -> None:
    official_sources, _records = official_speaker_sources()
    profile_owners: dict[str, list[Path]] = defaultdict(list)
    for path in sorted((WIKI / "people").glob("*.md")):
        if path.name in {"index.md", "people.md"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        expected = official_sources.get(path.stem, set())
        for value in urls(text):
            normalized = normalize_url(value)
            if host(value) not in PROFILE_HOSTS:
                continue
            profile_owners[normalized].append(path)
            if normalized in expected:
                counters["official_roster_profile_matches"] += 1
            elif path.stem in official_sources:
                assessment = assess_connection({"exact_name_only": True}, identity_required=True)
                findings.append(finding(
                    "high",
                    "person_profile_not_in_official_roster",
                    path,
                    "The social profile is attached to an official speaker page but is not one of that speaker's exact official-roster URLs.",
                    url=value,
                    evidence=[assessment["identity_status"], assessment["disposition"]],
                ))
            else:
                findings.append(finding("medium", "profile_for_non_roster_person", path, "The profile belongs to a page not matched to the official speaker roster.", url=value))
    for value, paths in profile_owners.items():
        unique = sorted(set(paths))
        if len(unique) > 1:
            for path in unique:
                findings.append(finding(
                    "critical",
                    "duplicate_person_profile_identity_collision",
                    path,
                    "The same external profile URL is assigned to multiple person pages; this is an identity collision, not evidence that the people are connected.",
                    url=value,
                    evidence=[str(other.relative_to(ROOT)) for other in unique if other != path],
                ))


def audit_talk_sources(findings: list[dict], counters: Counter) -> None:
    sessions = official_sessions_by_title()
    speaker_sources, speaker_records = official_speaker_sources()
    for path in sorted((WIKI / "talks").glob("*.md")):
        if path.name in {"index.md", "talks.md"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        fields = frontmatter(text)
        matched = sessions.get(fields.get("title", ""), [])
        official_urls = set()
        official_speakers = set()
        for session in matched:
            official_urls.update(normalize_url(value) for value in urls(session.get("description", "")))
            official_speakers.update(session.get("speakers") or [])
        for speaker in official_speakers:
            official_urls.update(speaker_sources.get(slugify(speaker), set()))
        for value in urls(text):
            normalized = normalize_url(value)
            domain = host(value)
            if domain in OFFICIAL_HOSTS or normalized in official_urls:
                counters["talk_sources_backed_by_canonical_data"] += 1
                continue
            if domain == "github.com":
                repo_name = slugify(urlsplit(value).path.rstrip("/").split("/")[-1])
                session_names_tool = any(
                    repo_name and repo_name in slugify(str(session.get("description") or ""))
                    for session in matched
                )
                if repo_name in package_project_names(text) and session_names_tool:
                    counters["talk_repositories_with_package_provenance"] += 1
                    continue
                assessment = assess_connection({"exact_name_only": True}, identity_required=True, event_claim=True)
                findings.append(finding(
                    "high",
                    "repository_not_in_canonical_session_sources",
                    path,
                    "A GitHub repository is presented on a scheduled talk page, but the exact repository URL is absent from the official session description and official speaker profile sources.",
                    url=value,
                    evidence=[assessment["identity_status"], assessment["event_status"], assessment["disposition"]],
                ))
            elif domain in PROFILE_HOSTS:
                findings.append(finding("high", "talk_profile_not_in_canonical_sources", path, "A social profile on the talk page is not an exact official-roster URL for a scheduled speaker.", url=value))


def normalized_company_name(value: str) -> str:
    value = re.sub(r"\([^)]*\)", " ", value).replace("&", " and ")
    value = re.sub(r"\b(inc|llc|ltd|labs|lab|ai|technologies|technology|company|corp|corporation)\b", " ", value, flags=re.I)
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def compact_brand(value: str) -> str:
    """Keep brand terms such as AI/Labs while ignoring punctuation and spacing."""
    return re.sub(r"[^a-z0-9]+", "", re.sub(r"\([^)]*\)", " ", value).lower())


def metadata_corroborates_company(company: str, metadata: str) -> bool:
    company_core = normalized_company_name(company)
    metadata_core = normalized_company_name(metadata)
    company_brand = compact_brand(company)
    metadata_brand = compact_brand(metadata)
    return bool(
        (company_core and company_core in metadata_core)
        or (company_brand and company_brand in metadata_brand)
    )


def official_tool_maintainer_evidence(tool_name: str, official_descriptions: str) -> bool:
    """Require both roster ownership language and a canonical session mention."""
    tool_slug = slugify(tool_name)
    if not tool_slug or tool_slug not in slugify(official_descriptions):
        return False
    _sources, records = official_speaker_sources()
    for speaker in records.values():
        affiliation = slugify(str(speaker.get("company") or ""))
        role_and_bio = slugify(" ".join(
            str(speaker.get(key) or "") for key in ("role", "bio")
        ))
        ownership_language = any(term in role_and_bio for term in ("creator", "maintainer", "author"))
        if affiliation == tool_slug and tool_slug in role_and_bio and ownership_language:
            return True
    return False


def audit_company_profiles(findings: list[dict], counters: Counter) -> None:
    profiles = load_json(RAW / "company-profiles.json", {})
    for slug, profile in sorted(profiles.items()):
        website = profile.get("website") or ""
        if not website:
            continue
        path = WIKI / "companies" / f"{slug}.md"
        status = profile.get("fetchStatus") or "unknown"
        confidence = profile.get("fetchConfidence")
        origin = profile.get("origin") or ""
        metadata = profile.get("fetchedMetadata") or {}
        title_blob = " ".join(str(metadata.get(key) or "") for key in ("title", "site_name", "description", "h1"))
        company = frontmatter(path.read_text(errors="ignore")).get("title", slug.replace("-", " ")) if path.exists() else slug.replace("-", " ")
        metadata_lower = title_blob.lower()
        if status != "fetched":
            findings.append(finding(
                "medium",
                "company_site_attached_without_successful_validation",
                path,
                f"The company site remains attached even though automated validation status is {status!r}; this is a validation gap, not proof the URL is false.",
                url=website,
                evidence=[origin],
            ))
        elif "domain-guess" in origin and any(marker in metadata_lower for marker in PARKED_SITE_MARKERS):
            findings.append(finding(
                "high",
                "domain_guess_resolves_to_parked_site",
                path,
                "A guessed domain was accepted even though the fetched homepage identifies a parked or for-sale site.",
                url=website,
                evidence=[title_blob[:240]],
            ))
        elif "domain-guess" in origin and not metadata_corroborates_company(company, title_blob):
            findings.append(finding(
                "medium",
                "domain_guess_without_company_name_corroboration",
                path,
                "A guessed domain lacks owner-controlled homepage metadata corroborating the company name. It must be reviewed for a same-name-domain collision.",
                url=website,
                evidence=[title_blob[:240]],
            ))
        elif isinstance(confidence, (int, float)) and confidence < 70:
            findings.append(finding("medium", "low_confidence_company_site", path, "The attached company site has a legacy discovery score below 70 and needs source-level review.", url=website, evidence=[str(confidence), origin]))
        else:
            counters["company_profiles_without_static_red_flags"] += 1


def audit_malformed_urls(findings: list[dict]) -> None:
    for path in sorted(WIKI.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for value in urls(text):
            domain = host(value)
            if domain.endswith(".con") or not domain or " " in value:
                findings.append(finding(
                    "low" if path.parent.name == "slides" else "high",
                    "malformed_external_url",
                    path,
                    "The URL is malformed. On OCR/slide pages this is likely transcription noise; elsewhere it may be a broken third-party connection.",
                    url=value,
                ))


def audit_tool_repositories(findings: list[dict], counters: Counter) -> None:
    official_descriptions = "\n".join(
        str(session.get("description") or "")
        for sessions in official_sessions_by_title().values()
        for session in sessions
    ).lower()
    for path in sorted((WIKI / "tools").glob("*.md")):
        if path.name in {"index.md", "tools.md"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        fields = frontmatter(text)
        repositories = [value for value in urls(text) if host(value) == "github.com"]
        if not repositories:
            continue
        if fields.get("status") == "external comparison" and "not first-class AIE evidence" in text:
            counters["explicit_external_comparison_repositories"] += len(repositories)
            continue
        for value in repositories:
            tool_name = fields.get("title", path.stem).lower()
            corroborated = (
                "pypi.org" in text
                or "crates.io" in text
                or "npmjs.com" in text
                or official_tool_maintainer_evidence(tool_name, official_descriptions)
            )
            official_event_evidence = bool(tool_name and tool_name in official_descriptions)
            assessment = assess_connection(
                {
                    "primary_owner_metadata": corroborated,
                    "official_event_evidence": official_event_evidence,
                    "exact_name_only": not corroborated,
                },
                identity_required=True,
                event_claim=official_event_evidence or "Official" in fields.get("sourceLabels", ""),
            )
            if assessment["disposition"] == "hold_for_review":
                findings.append(finding(
                    "medium",
                    "tool_repository_requires_identity_review",
                    path,
                    "The repository is linked from a tool page without a second owner-controlled package/source proving the repository identity. A matching tool name alone is insufficient.",
                    url=value,
                    evidence=[assessment["identity_status"], assessment["event_status"]],
                ))
            else:
                counters["tool_repositories_with_owner_corroboration"] += 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Run without writing the internal report and policy.")
    args = parser.parse_args()
    findings: list[dict] = []
    counters: Counter = Counter()
    audit_people(findings, counters)
    audit_talk_sources(findings, counters)
    audit_company_profiles(findings, counters)
    audit_malformed_urls(findings)
    audit_tool_repositories(findings, counters)
    public_ranking_leaks = audit_public_ranking_artifacts(findings, counters)
    findings.sort(key=lambda row: (severity_rank(row["severity"]), row["kind"], row["page"], row["url"]))
    payload = {
        "schemaVersion": 1,
        "visibility": "internal-only",
        "mutationBoundary": "This audit reports candidates only and does not edit wiki pages or relationships.",
        "summary": {
            "findings": len(findings),
            "bySeverity": dict(Counter(row["severity"] for row in findings)),
            "byKind": dict(Counter(row["kind"] for row in findings)),
            "verifiedOrBoundedSignals": dict(counters),
        },
        "findings": findings,
    }
    if not args.check:
        write_internal_policy()
        INTERNAL_DIR.mkdir(parents=True, exist_ok=True)
        REPORT_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({**payload["summary"], "written": not args.check}, sort_keys=True))
    return 1 if args.check and public_ranking_leaks else 0


if __name__ == "__main__":
    raise SystemExit(main())
