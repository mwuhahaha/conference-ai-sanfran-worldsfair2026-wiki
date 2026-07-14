#!/usr/bin/env python3
"""Audit third-party wiki connections without mutating public wiki content."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit

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


def severity_rank(value: str) -> int:
    return {"critical": 0, "high": 1, "medium": 2, "low": 3}.get(value, 4)


def finding(severity: str, kind: str, path: Path, reason: str, *, url: str = "", evidence: list[str] | None = None) -> dict:
    return {
        "severity": severity,
        "kind": kind,
        "page": str(path.relative_to(ROOT)),
        "url": url,
        "reason": reason,
        "evidence": evidence or [],
    }


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
            corroborated = "pypi.org" in text or "crates.io" in text or "npmjs.com" in text
            tool_name = fields.get("title", path.stem).lower()
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
