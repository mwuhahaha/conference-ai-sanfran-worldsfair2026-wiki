#!/usr/bin/env python3
"""Build private, claim-scoped writing policy for the WF26 update pipeline.

The reusable contracts/store/projection live in ``wiki-from-topic-maker``.
This adapter maps WF26 source roles into those contracts. It never emits a
global reputation score for a person, company, or idea, and it writes only
under the ignored private state root.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import parse_qs, unquote, urlsplit

from wiki_from_topic_maker.credibility_v2 import (
    AssessmentSnapshot,
    ClaimRecord,
    CredibilityStore,
    DimensionAssessment,
    DimensionName,
    DimensionStatus,
    EndorsementStatus,
    EventAssociationStatus,
    EvidenceCertainty,
    EvidenceDirectness,
    EvidenceObservation,
    IdentityStatus,
    ObservationStance,
    PROVIDER_REGISTRY,
    PublicationDisposition,
    ReasonCode,
    SourceVersion,
    project_writing_decision,
)


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "sources"
MANIFEST = RAW / "official-wf26-video-manifest.json"
SPEAKERS = RAW / "official-speakers.json"
SESSIONS = RAW / "official-sessions.json"
PRIVATE_COMPANY_PROFILES_RELATIVE = Path(
    ".ops/state/cache/wiki-maker/credibility-v2/company-profile-candidates.json"
)
LEGACY_COMPANY_PROFILES_RELATIVE = Path("raw/sources/company-profiles.json")
POLICY_PATH = (
    ROOT
    / ".ops"
    / "state"
    / "cache"
    / "wiki-maker"
    / "credibility-v2"
    / "writing-policy.json"
)
OFFICIAL_EVENT_URL = "https://ai.engineer/worldsfair"
PRIVATE_BROWSER_ROOT = (
    ROOT
    / ".ops"
    / "state"
    / "cache"
    / "wiki-maker"
    / "credibility-v2"
    / "browser"
)
PRIVATE_PROVIDER_CHECKS_RELATIVE = Path(
    ".ops/state/cache/wiki-maker/credibility-v2/provider-checks.json"
)
PRIVATE_PROVIDER_RECEIPTS_RELATIVE = Path(
    ".ops/state/cache/wiki-maker/credibility-v2/receipts/provider-fetch"
)

PROVIDER_CLAIM_SCOPES: dict[str, frozenset[str]] = {
    "github_rest": frozenset({"repository_metadata"}),
    "google_dns_doh": frozenset({"dns_record_observation"}),
    "owner_web": frozenset({"self_statement"}),
    "pypi": frozenset({"python_package_metadata"}),
    "rdap_registry": frozenset({"domain_registration_metadata"}),
    "wikimedia": frozenset({"encyclopedic_context"}),
}
PROVIDER_SEMANTIC_FIELDS: dict[str, frozenset[str]] = {
    "github_rest": frozenset({"archived", "disabled", "repository", "state"}),
    "google_dns_doh": frozenset({"answerCount", "rcode", "state"}),
    "owner_web": frozenset({"responseBytes", "state"}),
    "pypi": frozenset({"package", "state", "version"}),
    "rdap_registry": frozenset({"domain", "state"}),
    "wikimedia": frozenset({"candidateIds", "resultCount", "state"}),
}
SUCCESSFUL_PROVIDER_OUTCOMES = frozenset({"success", "cached"})
SOURCE_ADAPTER_VERSION = "wf26-source-adapter-v2"

PARKED_PROFILE_MARKERS = (
    "buy this domain",
    "domain is available",
    "domain is for sale",
    "for sale",
    "parkingcrew",
    "private inquiries for premium domains",
    "sedo",
    "spaceship",
)
UNUSABLE_PROFILE_MARKERS = (
    "description goes here",
    "lorem ipsum",
    "your company description goes here",
)
PROFILE_STOPWORDS = {
    "about",
    "agent",
    "agents",
    "agentic",
    "automation",
    "company",
    "conference",
    "data",
    "developer",
    "engineer",
    "engineering",
    "from",
    "into",
    "model",
    "platform",
    "production",
    "service",
    "services",
    "software",
    "solution",
    "solutions",
    "speaker",
    "system",
    "systems",
    "technology",
    "that",
    "their",
    "this",
    "using",
    "with",
    "world",
}

TOPIC_TERMS: dict[str, tuple[str, ...]] = {
    "agent-evaluations": (
        "agent eval",
        "evaluation",
        "evals",
        "quality gate",
        "llm as a judge",
        "benchmark",
    ),
    "agent-memory": (
        "agent memory",
        "persistent memory",
        "long term memory",
        "context graph",
        "memory layer",
    ),
    "agent-ready-accessibility": (
        "agent ready accessibility",
        "accessibility",
        "accessible interface",
        "semantic html",
    ),
    "agent-security": (
        "agent security",
        "prompt injection",
        "permission",
        "least privilege",
        "authentication",
        "authorization",
        "security boundary",
    ),
    "agentic-search": (
        "agentic search",
        "deep research",
        "retrieval",
        "search agent",
        "research agent",
    ),
    "agentic-web": (
        "agentic web",
        "web for agents",
        "agent ready web",
        "browser agent",
        "computer use",
    ),
    "ai-sandboxes": (
        "agent sandbox",
        "sandbox cloud",
        "isolated execution",
        "code sandbox",
        "microvm",
    ),
    "autoresearch": (
        "autoresearch",
        "automated research",
        "research loop",
        "recursive model improvement",
        "self improving model",
    ),
    "coding-agents": (
        "coding agent",
        "code agent",
        "claude code",
        "codex",
        "agentic coding",
        "code review agent",
    ),
    "inference-engineering": (
        "inference engineering",
        "inference engine",
        "inference latency",
        "kv cache",
        "throughput",
        "vllm",
        "triton kernel",
    ),
    "mcp-app-runtime": (
        "mcp apps",
        "mcp ui",
        "interactive mcp",
        "agentic app runtime",
        "sep 1865",
    ),
    "mcp": (
        "model context protocol",
        "mcp server",
        "mcp client",
        "mcp host",
        " mcp ",
    ),
    "nearly-headless-web": (
        "nearly headless",
        "human handoff",
        "human visible checkpoint",
    ),
    "reachability-over-format": (
        "reachability over format",
        "reachability is",
        "linked properly",
        "agent discovery",
    ),
    "software-factories": (
        "software factory",
        "software factories",
        "agentic sdlc",
        "parallel coding agents",
        "multi agent coding",
    ),
    "voice-agents": (
        "voice agent",
        "speech agent",
        "voice ai",
        "text to speech",
        "speech to speech",
        "conversational voice",
    ),
}


def load_json(path: Path, fallback: Any) -> Any:
    if not path.is_file():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def stable_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, separators=(",", ":"), sort_keys=True)


def content_digest(value: Any) -> str:
    return sha256(stable_json(value).encode("utf-8")).hexdigest()


def slugify(value: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", value.casefold())).strip("-")


def compact_brand(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", re.sub(r"\([^)]*\)", " ", value.casefold()))


def company_name_from_slug(value: str) -> str:
    name = value.replace("-", " ").title()
    return name.upper() if len(compact_brand(name)) <= 3 else name


def normalized_company_name(value: str) -> str:
    cleaned = re.sub(r"\([^)]*\)", " ", value).replace("&", " and ")
    cleaned = re.sub(
        r"\b(?:ai|company|corp|corporation|inc|lab|labs|llc|ltd|technologies|technology)\b",
        " ",
        cleaned,
        flags=re.I,
    )
    return re.sub(r"[^a-z0-9]+", "", cleaned.casefold())


def profile_tokens(value: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", value.casefold())
        if len(token) >= 5 and token not in PROFILE_STOPWORDS
    }


def host_for_url(value: str) -> str:
    try:
        return (urlsplit(value).hostname or "").casefold().removeprefix("www.")
    except ValueError:
        return ""


def related_hosts(left: str, right: str) -> bool:
    return bool(
        left
        and right
        and (
            left == right
            or left.endswith(f".{right}")
            or right.endswith(f".{left}")
        )
    )


def company_profile_source_path(
    root: Path,
    explicit: Path | None = None,
) -> Path:
    """Prefer private candidate state while retaining explicit legacy inputs."""

    if explicit is not None:
        return explicit if explicit.is_absolute() else root / explicit
    private = root / PRIVATE_COMPANY_PROFILES_RELATIVE
    if private.is_file():
        return private
    return root / LEGACY_COMPANY_PROFILES_RELATIVE


def host_materially_binds_company(company: str, host: str) -> bool:
    """Require an exact domain label for short brands and a strong match otherwise."""

    company_core = normalized_company_name(company)
    company_brand = compact_brand(company)
    compact_host = re.sub(r"[^a-z0-9]+", "", host)
    domain_label = re.sub(r"[^a-z0-9]+", "", host.split(".", 1)[0])
    if company_brand and len(company_brand) == 3:
        return company_brand == domain_label
    return bool(
        (company_brand and len(company_brand) >= 4 and company_brand in compact_host)
        or (company_core and len(company_core) >= 4 and company_core in compact_host)
    )


def official_company_identity_hosts(
    company: str,
    values: list[str],
) -> tuple[str, ...]:
    """Return event-published hosts whose names materially bind to a company."""

    hosts: set[str] = set()
    for value in values:
        for url in re.findall(r"https?://[^\s<>()\[\]{}]+", value):
            host = host_for_url(url.rstrip(".,;:'\""))
            if host and host_materially_binds_company(company, host):
                hosts.add(host)
    return tuple(sorted(hosts))


def explicitly_names_company(company: str, value: str) -> bool:
    """Match a company phrase in one official role/bio without fuzzy inference."""

    short_brand = len(compact_brand(company)) <= 3
    company_tokens = re.findall(
        r"[A-Za-z0-9]+",
        company if short_brand else company.casefold(),
    )
    if not company_tokens:
        return False
    pattern = r"(?<![A-Za-z0-9])" + r"[^A-Za-z0-9]+".join(
        re.escape(token) for token in company_tokens
    ) + r"(?![A-Za-z0-9])"
    flags = 0 if short_brand else re.IGNORECASE
    return re.search(pattern, value, flags) is not None


def official_roster_company_context(
    company: str,
    speakers: Iterable[dict[str, Any]],
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """Bind an owner website only when the same official record names the company."""

    hosts: set[str] = set()
    contexts: list[str] = []
    for speaker in speakers:
        role_bio = " ".join(
            str(speaker.get(key) or "") for key in ("role", "bio")
        ).strip()
        if not explicitly_names_company(company, role_bio):
            continue
        website = str(speaker.get("website") or "").strip()
        matched_hosts = official_company_identity_hosts(company, [website])
        if not matched_hosts:
            continue
        hosts.update(matched_hosts)
        contexts.append(" ".join(value for value in (role_bio, website) if value))
    return tuple(sorted(hosts)), tuple(contexts)


def official_roster_company_provider_bindings(
    company: str,
    speakers: Iterable[dict[str, Any]],
) -> tuple[dict[str, str], ...]:
    """Bind provider subjects to a company through one official roster row."""

    bindings: set[tuple[str, str]] = set()
    company_slug = slugify(company)
    for speaker in speakers:
        name = str(speaker.get("name") or "").strip()
        website = str(speaker.get("website") or "").strip()
        if not name or not website:
            continue
        hosts = official_company_identity_hosts(company, [website])
        if not hosts:
            continue
        role_bio = " ".join(
            str(speaker.get(key) or "") for key in ("role", "bio")
        ).strip()
        direct_affiliation = slugify(str(speaker.get("company") or "")) == company_slug
        if not direct_affiliation and not explicitly_names_company(company, role_bio):
            continue
        subject_id = f"person:{slugify(name)}"
        bindings.update((subject_id, host) for host in hosts)
    return tuple(
        {"subjectId": subject_id, "host": host}
        for subject_id, host in sorted(bindings)
    )


def _provider_target_host(
    provider_id: str,
    semantic_result: dict[str, Any],
    receipt: dict[str, Any],
) -> str:
    if provider_id == "rdap_registry":
        return str(semantic_result.get("domain") or "").casefold().removeprefix(
            "www."
        )
    if provider_id == "google_dns_doh":
        query = parse_qs(urlsplit(str(receipt.get("requestUrl") or "")).query)
        return str((query.get("name") or [""])[0]).casefold().removeprefix("www.")
    if provider_id == "owner_web":
        return host_for_url(
            str(receipt.get("finalUrl") or receipt.get("requestUrl") or "")
        )
    return ""


def load_provider_evidence(root: Path) -> dict[str, list[dict[str, Any]]]:
    """Load only private provider index and receipt metadata, never cache bodies."""

    index = load_json(root / PRIVATE_PROVIDER_CHECKS_RELATIVE, {})
    if not isinstance(index, dict) or index.get("visibility") != "internal-only":
        return {}
    receipt_root = root / PRIVATE_PROVIDER_RECEIPTS_RELATIVE
    receipts: dict[str, dict[str, Any]] = {}
    for path in sorted(receipt_root.glob("*.json")):
        receipt = load_json(path, {})
        if not isinstance(receipt, dict):
            continue
        request_id = str(receipt.get("requestId") or "")
        if request_id:
            receipts[request_id] = receipt

    by_subject: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for result in index.get("results", []):
        if not isinstance(result, dict):
            continue
        subject_id = str(result.get("subjectId") or "")
        plan_id = str(result.get("planId") or "")
        if not subject_id or not plan_id:
            continue
        for raw_evidence in result.get("evidence", []):
            if not isinstance(raw_evidence, dict):
                continue
            provider_id = str(raw_evidence.get("providerId") or "")
            request_id = str(raw_evidence.get("requestId") or "")
            receipt = receipts.get(request_id)
            if provider_id not in PROVIDER_CLAIM_SCOPES or receipt is None:
                continue
            if any(
                str(receipt.get(key) or "") != expected
                for key, expected in (
                    ("subjectId", subject_id),
                    ("planId", plan_id),
                    ("providerId", provider_id),
                )
            ):
                continue
            outcome = str(receipt.get("outcome") or raw_evidence.get("outcome") or "")
            if outcome != str(raw_evidence.get("outcome") or ""):
                continue
            scopes = sorted(
                PROVIDER_CLAIM_SCOPES[provider_id].intersection(
                    str(value)
                    for value in raw_evidence.get("claimScopes", [])
                    if isinstance(value, str)
                )
            )
            if not scopes:
                continue
            raw_semantic = raw_evidence.get("semanticResult")
            semantic_result = {
                key: value
                for key, value in (
                    raw_semantic.items()
                    if isinstance(raw_semantic, dict)
                    else ()
                )
                if key in PROVIDER_SEMANTIC_FIELDS[provider_id]
            }
            evidence = {
                "providerId": provider_id,
                "outcome": outcome,
                "claimScopes": scopes,
                "semanticResult": semantic_result,
                "requestId": request_id,
                "planId": plan_id,
                "retrievedAt": str(receipt.get("retrievedAt") or ""),
                "sourceBoundary": str(result.get("sourceBoundary") or ""),
                "sourcePath": str(result.get("sourcePath") or ""),
                "discoveryOnly": provider_id == "wikimedia",
                "publicationImpact": "none_without_separate_claim_assessment",
                "eventAssociationImpact": "none",
                "endorsementImpact": "none",
            }
            target_host = _provider_target_host(
                provider_id,
                semantic_result,
                receipt,
            )
            if target_host:
                evidence["targetHost"] = unquote(target_host)
            by_subject[subject_id].append(evidence)
    return {
        subject_id: sorted(
            evidence,
            key=lambda item: (item["providerId"], item["requestId"]),
        )
        for subject_id, evidence in sorted(by_subject.items())
    }


def provider_evidence_gate_states(
    evidence_by_subject: dict[str, list[dict[str, Any]]],
) -> dict[str, dict[str, Any]]:
    """Project provider metadata without assigning entity-level reputation."""

    states: dict[str, dict[str, Any]] = {}
    for subject_id, evidence in sorted(evidence_by_subject.items()):
        successful = [
            item
            for item in evidence
            if item.get("outcome") in SUCCESSFUL_PROVIDER_OUTCOMES
        ]
        wikimedia = [
            item for item in successful if item.get("providerId") == "wikimedia"
        ]
        empty_discovery = bool(wikimedia) and all(
            item.get("semanticResult", {}).get("resultCount") == 0
            for item in wikimedia
        )
        states[subject_id] = {
            "status": (
                "empty_discovery_result"
                if successful and len(successful) == len(wikimedia) and empty_discovery
                else "claim_scoped_metadata_available"
                if successful
                else "unavailable"
            ),
            "claimScopedEvidence": evidence,
            "globalReputationAssessment": "not_computed",
            "eventAssociationStatus": "not_claimed",
            "endorsementStatus": "not_endorsed",
            "automaticWritingImpact": "none",
        }
    return states


def company_provider_host_evidence(
    evidence_by_subject: dict[str, list[dict[str, Any]]],
    bindings: Iterable[dict[str, str]],
    *,
    identity_bound: bool,
) -> tuple[dict[str, Any], ...]:
    """Use provider checks only to corroborate an already bound owner host."""

    if not identity_bound:
        return ()
    rows: list[dict[str, Any]] = []
    for binding in bindings:
        subject_id = binding["subjectId"]
        bound_host = binding["host"]
        for evidence in evidence_by_subject.get(subject_id, []):
            provider_id = evidence.get("providerId")
            if provider_id not in {"owner_web", "google_dns_doh", "rdap_registry"}:
                continue
            target_host = str(evidence.get("targetHost") or "")
            if not target_host or not related_hosts(target_host, bound_host):
                continue
            semantic = evidence.get("semanticResult", {})
            state = semantic.get("state") if isinstance(semantic, dict) else None
            corroborates = bool(
                evidence.get("outcome") in SUCCESSFUL_PROVIDER_OUTCOMES
                and (
                    provider_id == "owner_web"
                    and state == "owner_content_available"
                    or provider_id == "rdap_registry"
                    and state == "registration_metadata_available"
                    or provider_id == "google_dns_doh"
                    and state == "dns_observed"
                    and semantic.get("rcode") == 0
                    and int(semantic.get("answerCount") or 0) > 0
                )
            )
            rows.append(
                {
                    "subjectId": subject_id,
                    "providerId": provider_id,
                    "claimScopes": evidence["claimScopes"],
                    "outcome": evidence["outcome"],
                    "targetHost": target_host,
                    "hostAvailabilityCorroborated": corroborates,
                    "requestId": evidence["requestId"],
                }
            )
    return tuple(
        sorted(rows, key=lambda item: (item["providerId"], item["requestId"]))
    )


def load_browser_profile_metadata(root: Path) -> dict[str, dict[str, Any]]:
    browser_root = (
        root
        / ".ops"
        / "state"
        / "cache"
        / "wiki-maker"
        / "credibility-v2"
        / "browser"
    )
    records: dict[str, tuple[str, dict[str, Any]]] = {}
    for path in sorted(browser_root.glob("run-*.json")):
        payload = load_json(path, {})
        generated_at = str(payload.get("generatedAt") or "")
        for record in payload.get("records", []):
            if not isinstance(record, dict) or record.get("outcome") != "browser_success":
                continue
            extraction = record.get("extraction")
            if not isinstance(extraction, dict) or not extraction.get("finalUrlExactOrigin"):
                continue
            for page in record.get("pages", []):
                if not isinstance(page, str) or not page.startswith("wiki/companies/"):
                    continue
                slug = Path(page).stem
                previous = records.get(slug)
                if previous is None or generated_at >= previous[0]:
                    records[slug] = (generated_at, extraction)
    return {slug: value for slug, (_generated, value) in records.items()}


def company_profile_gate(
    company: str,
    profile: dict[str, Any],
    official_context: str,
    *,
    official_identity_hosts: tuple[str, ...] = (),
    browser_metadata: dict[str, Any] | None = None,
) -> tuple[
    bool,
    tuple[ReasonCode, ...],
    dict[str, str],
    dict[str, Any],
]:
    """Screen one owner-site claim without turning discovery signals into proof."""

    website = str(profile.get("website") or "")
    static_metadata = profile.get("fetchedMetadata")
    metadata = dict(static_metadata) if isinstance(static_metadata, dict) else {}
    if browser_metadata:
        for source_key, target_key in (
            ("title", "title"),
            ("description", "description"),
            ("siteName", "site_name"),
            ("h1", "h1"),
        ):
            value = str(browser_metadata.get(source_key) or "").strip()
            if value:
                metadata[target_key] = value
    values = {
        key: re.sub(r"\s+", " ", str(metadata.get(key) or "")).strip()
        for key in ("title", "site_name", "description", "h1")
    }
    metadata_text = " ".join(values.values()).strip()
    lowered = metadata_text.casefold()
    host = host_for_url(website)
    domain_brand = re.sub(r"[^a-z0-9]+", "", host.split(".", 1)[0])
    company_brand = compact_brand(company)
    company_core = normalized_company_name(company)
    metadata_brand = compact_brand(metadata_text)
    full_brand_match = bool(company_brand and company_brand in metadata_brand)
    identity_match = bool(
        full_brand_match
        or company_core
        and len(company_core) >= 4
        and (
            company_core in metadata_brand
            or company_core == domain_brand
            or company_core in domain_brand
        )
    )
    context_overlap = profile_tokens(metadata_text) & profile_tokens(official_context)
    has_substantive_description = len(values["description"]) >= 24
    identity_host_match = any(
        related_hosts(host, official_host)
        for official_host in official_identity_hosts
    )
    signals = {
        "websiteHost": host,
        "officialIdentityHosts": list(official_identity_hosts),
        "identityHostMatch": identity_host_match,
        "fullBrandMatch": full_brand_match,
        "metadataIdentityMatch": identity_match,
        "substantiveDescription": has_substantive_description,
        "contextOverlapTerms": sorted(context_overlap),
    }

    if not website.startswith("https://"):
        return False, (ReasonCode.MISSING_EVIDENCE,), values, signals
    if any(marker in lowered for marker in PARKED_PROFILE_MARKERS):
        return False, (ReasonCode.ENTITY_COLLISION,), values, signals
    if not identity_host_match:
        return False, (ReasonCode.ID_NAME_ONLY,), values, signals
    if not identity_match:
        return False, (ReasonCode.ENTITY_COLLISION,), values, signals
    if any(marker in lowered for marker in UNUSABLE_PROFILE_MARKERS):
        return False, (ReasonCode.MISSING_EVIDENCE,), values, signals
    if not has_substantive_description:
        return False, (ReasonCode.MISSING_EVIDENCE,), values, signals
    return (
        True,
        (ReasonCode.ID_OWNER_EXACT, ReasonCode.SELF_INTERESTED_SOURCE),
        values,
        signals,
    )


def source_as_of(
    manifest: dict[str, Any], *observation_payloads: dict[str, Any]
) -> datetime:
    candidates: list[datetime] = []
    for payload in (manifest, *observation_payloads):
        for key in ("checkedAt", "checked_at", "generatedAt", "generated_at"):
            value = payload.get(key)
            if isinstance(value, str) and value:
                try:
                    candidates.append(
                        datetime.fromisoformat(value.replace("Z", "+00:00"))
                    )
                except ValueError:
                    pass
    for item in manifest.get("videos", []):
        if not isinstance(item, dict):
            continue
        media_type = str(item.get("mediaType") or "")
        date_keys = ("uploadDate",)
        if media_type not in {"scheduled_premiere", "unavailable_playlist_item"}:
            date_keys += ("releaseDate",)
        for key in date_keys:
            value = item.get(key)
            if not isinstance(value, str) or not value:
                continue
            try:
                candidates.append(datetime.fromisoformat(value).replace(tzinfo=timezone.utc))
            except ValueError:
                pass
    if not candidates:
        return datetime(1970, 1, 1, tzinfo=timezone.utc)
    return max(value.astimezone(timezone.utc) for value in candidates)


def transcript_path(root: Path, video_id: str) -> Path | None:
    for folder in (
        root / "raw" / "sources" / "youtube-transcripts",
        root / "raw" / "sources" / "youtube-livestream-transcripts",
    ):
        path = folder / f"{video_id}.txt"
        if path.is_file():
            return path
    return None


def video_source_text(root: Path, item: dict[str, Any]) -> tuple[str, Path | None]:
    video_id = str(item.get("id") or "")
    transcript = transcript_path(root, video_id)
    parts = [str(item.get("title") or "")]
    resource = root / "wiki" / "resources" / f"youtube-{video_id}.md"
    if resource.is_file():
        parts.append(resource.read_text(encoding="utf-8", errors="ignore"))
    if transcript:
        parts.append(transcript.read_text(encoding="utf-8", errors="ignore"))
    normalized = " " + re.sub(r"\s+", " ", "\n".join(parts).casefold()) + " "
    return normalized, transcript


def topic_matches(text: str, terms: Iterable[str]) -> tuple[str, ...]:
    matches = []
    for term in terms:
        normalized = " " + re.sub(r"\s+", " ", term.casefold()).strip() + " "
        if normalized in text:
            matches.append(term)
    return tuple(sorted(set(matches)))


def supported_dimension(
    name: DimensionName,
    observation_ids: Iterable[str],
    *reasons: ReasonCode,
) -> DimensionAssessment:
    return DimensionAssessment.create(
        name,
        DimensionStatus.SUPPORTED,
        observation_ids=observation_ids,
        reason_codes=reasons,
    )


def insufficient_dimension(
    name: DimensionName,
    *reasons: ReasonCode,
) -> DimensionAssessment:
    return DimensionAssessment.create(
        name,
        DimensionStatus.INSUFFICIENT,
        reason_codes=reasons,
    )


def contested_dimension(
    name: DimensionName,
    observation_ids: Iterable[str],
    *reasons: ReasonCode,
) -> DimensionAssessment:
    return DimensionAssessment.create(
        name,
        DimensionStatus.CONTESTED,
        observation_ids=observation_ids,
        reason_codes=reasons,
    )


def append_assessment(
    store: CredibilityStore,
    *,
    claim: ClaimRecord,
    observations: list[EvidenceObservation],
    as_of: datetime,
    identity_status: IdentityStatus,
    identity_required: bool,
    event_status: EventAssociationStatus,
    event_claimed: bool,
    publication: PublicationDisposition,
    independent: bool,
    provenance_reason: ReasonCode = ReasonCode.OFFICIAL_CANON_SCOPE_ONLY,
) -> AssessmentSnapshot:
    observation_ids = [item.observation_id for item in observations]
    dimensions = [
        supported_dimension(
            DimensionName.CLAIM_SUPPORT,
            observation_ids,
            ReasonCode.DIRECT_PRIMARY_RECORD,
        ),
        supported_dimension(
            DimensionName.INSTITUTIONAL_PROVENANCE,
            observation_ids,
            provenance_reason,
        ),
        (
            supported_dimension(
                DimensionName.INDEPENDENCE,
                observation_ids,
                ReasonCode.INDEPENDENT_CORROBORATION,
            )
            if independent
            else insufficient_dimension(
                DimensionName.INDEPENDENCE,
                ReasonCode.MISSING_EVIDENCE,
            )
        ),
    ]
    if identity_required:
        if identity_status is IdentityStatus.VERIFIED:
            identity_dimension = supported_dimension(
                DimensionName.IDENTITY,
                observation_ids,
                ReasonCode.ID_OWNER_EXACT,
            )
        elif identity_status is IdentityStatus.PROBABLE:
            identity_dimension = supported_dimension(
                DimensionName.IDENTITY,
                observation_ids,
                ReasonCode.SELF_INTERESTED_SOURCE,
            )
        elif identity_status is IdentityStatus.CONFLICT:
            identity_dimension = contested_dimension(
                DimensionName.IDENTITY,
                observation_ids,
                ReasonCode.ENTITY_COLLISION,
            )
        else:
            identity_dimension = insufficient_dimension(
                DimensionName.IDENTITY,
                ReasonCode.ID_NAME_ONLY,
            )
        dimensions.append(identity_dimension)
    snapshot = AssessmentSnapshot.create(
        claim_id=claim.claim_id,
        subject_id=claim.subject_id,
        as_of=as_of,
        dimensions=dimensions,
        identity_status=identity_status,
        identity_required=identity_required,
        event_status=event_status,
        event_claimed=event_claimed,
        comparison_only=False,
        publication_disposition=publication,
        endorsement_status=EndorsementStatus.NOT_ENDORSED,
        model_version="wf26-claim-policy-v2",
    )
    store.append_assessment(snapshot)
    return snapshot


def append_source(
    store: CredibilityStore,
    *,
    source_id: str,
    canonical_url: str,
    value: Any,
    as_of: datetime,
) -> SourceVersion:
    source = SourceVersion.create(
        source_id=f"{source_id}:{SOURCE_ADAPTER_VERSION}",
        canonical_url=canonical_url,
        content_sha256=content_digest(value),
        retrieved_at=as_of,
    )
    store.append_source_version(source)
    return source


def append_observation(
    store: CredibilityStore,
    *,
    claim: ClaimRecord,
    source: SourceVersion,
    span_id: str,
    cluster_id: str,
    as_of: datetime,
    directness: EvidenceDirectness = EvidenceDirectness.DIRECT,
    certainty: EvidenceCertainty = EvidenceCertainty.HIGH,
    reasons: Iterable[ReasonCode] = (ReasonCode.DIRECT_PRIMARY_RECORD,),
) -> EvidenceObservation:
    observation = EvidenceObservation.create(
        claim_id=claim.claim_id,
        subject_id=claim.subject_id,
        source_version_id=source.source_version_id,
        evidence_span_id=span_id,
        stance=ObservationStance.SUPPORTS,
        directness=directness,
        extraction_certainty=certainty,
        independence_cluster_id=cluster_id,
        observed_at=as_of,
        reason_codes=reasons,
        extractor_version=SOURCE_ADAPTER_VERSION,
    )
    store.append_observation(observation)
    return observation


def build_private_policy(
    root: Path = ROOT,
    *,
    company_profiles_path: Path | None = None,
) -> dict[str, Any]:
    root = root.resolve()
    raw = root / "raw" / "sources"
    manifest = load_json(raw / "official-wf26-video-manifest.json", {})
    speakers_payload = load_json(raw / "official-speakers.json", {})
    sessions_payload = load_json(raw / "official-sessions.json", {})
    provider_index = load_json(root / PRIVATE_PROVIDER_CHECKS_RELATIVE, {})
    browser_index = load_json(
        root
        / ".ops"
        / "state"
        / "cache"
        / "wiki-maker"
        / "credibility-v2"
        / "browser"
        / "latest.json",
        {},
    )
    as_of = source_as_of(manifest, provider_index, browser_index)
    store = CredibilityStore.for_project(root)
    speaker_rows = tuple(
        person
        for person in speakers_payload.get("speakers", [])
        if isinstance(person, dict)
    )
    provider_evidence = load_provider_evidence(root)
    provider_gate_states = provider_evidence_gate_states(provider_evidence)

    video_decisions: dict[str, dict[str, Any]] = {}
    people_decisions: dict[str, dict[str, Any]] = {}
    company_decisions: dict[str, dict[str, Any]] = {}
    company_profile_decisions: dict[str, dict[str, Any]] = {}
    company_profile_gates: dict[str, dict[str, Any]] = {}
    topic_video_decisions: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    topic_decisions: dict[str, dict[str, Any]] = {}

    videos = [item for item in manifest.get("videos", []) if isinstance(item, dict)]
    video_sources: dict[str, SourceVersion] = {}
    topic_observations: dict[str, list[EvidenceObservation]] = defaultdict(list)
    topic_source_ids: dict[str, list[str]] = defaultdict(list)

    for item in videos:
        video_id = str(item.get("id") or "")
        if not video_id:
            continue
        media_type = str(item.get("mediaType") or "unknown")
        association = str(item.get("associationEvidence") or "")
        unavailable = media_type == "unavailable_playlist_item"
        claim = ClaimRecord.create(
            subject_id=f"video:{video_id}",
            predicate="is associated with AI Engineer World's Fair 2026 media",
            object_value=True,
            qualifiers={
                "associationEvidence": association,
                "mediaType": media_type,
                "contentAvailable": not unavailable,
            },
        )
        store.append_claim(claim)
        source = append_source(
            store,
            source_id=f"official-video:{video_id}",
            canonical_url=f"https://www.youtube.com/watch?v={video_id}",
            value=item,
            as_of=as_of,
        )
        video_sources[video_id] = source
        observation = append_observation(
            store,
            claim=claim,
            source=source,
            span_id=f"manifest-video:{video_id}",
            cluster_id="official-ai-engineer-event-media",
            as_of=as_of,
            reasons=(ReasonCode.OFFICIAL_CANON_SCOPE_ONLY,),
        )
        snapshot = append_assessment(
            store,
            claim=claim,
            observations=[observation],
            as_of=as_of,
            identity_status=IdentityStatus.NOT_APPLICABLE,
            identity_required=False,
            event_status=EventAssociationStatus.VERIFIED,
            event_claimed=True,
            publication=PublicationDisposition.APPROVED,
            independent=False,
        )
        video_decisions[video_id] = project_writing_decision(
            snapshot,
            public_source_ids=(f"youtube-{video_id}",),
        ).as_dict()

        source_text, transcript = video_source_text(root, item)
        if unavailable or transcript is None:
            continue
        transcript_value = transcript.read_text(encoding="utf-8", errors="ignore")
        transcript_source = append_source(
            store,
            source_id=f"official-transcript:{video_id}",
            canonical_url=f"https://www.youtube.com/watch?v={video_id}",
            value=transcript_value,
            as_of=as_of,
        )
        for topic_slug, terms in TOPIC_TERMS.items():
            matches = topic_matches(source_text, terms)
            if not matches:
                continue
            topic_claim = ClaimRecord.create(
                subject_id=f"topic:{topic_slug}",
                predicate="recurs in official WF26 event media",
                object_value=True,
                qualifiers={"topic": topic_slug},
            )
            store.append_claim(topic_claim)
            topic_observation = append_observation(
                store,
                claim=topic_claim,
                source=transcript_source,
                span_id=f"topic-match:{topic_slug}:{video_id}",
                cluster_id=f"official-recording:{video_id}",
                as_of=as_of,
                directness=EvidenceDirectness.DERIVED,
                certainty=EvidenceCertainty.MEDIUM,
                reasons=(ReasonCode.OFFICIAL_CANON_SCOPE_ONLY,),
            )
            topic_observations[topic_slug].append(topic_observation)
            topic_source_ids[topic_slug].append(f"youtube-{video_id}")

            pair_snapshot = append_assessment(
                store,
                claim=topic_claim,
                observations=[topic_observation],
                as_of=as_of,
                identity_status=IdentityStatus.NOT_APPLICABLE,
                identity_required=False,
                event_status=EventAssociationStatus.VERIFIED,
                event_claimed=True,
                publication=PublicationDisposition.APPROVED,
                independent=False,
            )
            topic_video_decisions[topic_slug][video_id] = project_writing_decision(
                pair_snapshot,
                public_source_ids=(f"youtube-{video_id}",),
            ).as_dict()

    official_source = append_source(
        store,
        source_id="official-program-speakers",
        canonical_url=str(sessions_payload.get("website") or OFFICIAL_EVENT_URL),
        value=speakers_payload,
        as_of=as_of,
    )
    companies: dict[str, list[str]] = defaultdict(list)
    company_context: dict[str, list[str]] = defaultdict(list)
    person_companies: dict[str, str] = {}
    for person in speaker_rows:
        if not person.get("name"):
            continue
        name = str(person["name"])
        person_slug = slugify(name)
        company = str(person.get("company") or "")
        if company:
            companies[company].append(name)
            person_companies[name] = company
            company_context[company].extend(
                str(person.get(key) or "")
                for key in ("role", "bio", "website", "blog")
            )
        claim = ClaimRecord.create(
            subject_id=f"person:{person_slug}",
            predicate="is listed in the official WF26 speaker roster",
            object_value={
                "name": name,
                "role": str(person.get("role") or ""),
                "company": company,
            },
        )
        store.append_claim(claim)
        observation = append_observation(
            store,
            claim=claim,
            source=official_source,
            span_id=f"official-speaker:{person_slug}",
            cluster_id="official-wf26-program",
            as_of=as_of,
            reasons=(ReasonCode.ID_OWNER_EXACT, ReasonCode.OFFICIAL_CANON_SCOPE_ONLY),
        )
        snapshot = append_assessment(
            store,
            claim=claim,
            observations=[observation],
            as_of=as_of,
            identity_status=IdentityStatus.VERIFIED,
            identity_required=True,
            event_status=EventAssociationStatus.VERIFIED,
            event_claimed=True,
            publication=PublicationDisposition.APPROVED,
            independent=False,
        )
        people_decisions[person_slug] = project_writing_decision(
            snapshot,
            public_source_ids=("official-speakers",),
        ).as_dict()

    for session in sessions_payload.get("sessions", []):
        if not isinstance(session, dict):
            continue
        context = " ".join(
            str(session.get(key) or "")
            for key in ("title", "description", "track")
        )
        for speaker_name in session.get("speakers", []):
            company = person_companies.get(str(speaker_name))
            if company:
                company_context[company].append(context)

    company_names_by_slug: dict[str, str] = {}
    for company, names in companies.items():
        company_slug = slugify(company)
        company_names_by_slug[company_slug] = company
        claim = ClaimRecord.create(
            subject_id=f"company:{company_slug}",
            predicate="is represented in the official WF26 speaker roster",
            object_value={"company": company, "speakers": sorted(set(names))},
        )
        store.append_claim(claim)
        observation = append_observation(
            store,
            claim=claim,
            source=official_source,
            span_id=f"official-company:{company_slug}",
            cluster_id="official-wf26-program",
            as_of=as_of,
            reasons=(ReasonCode.OFFICIAL_CANON_SCOPE_ONLY,),
        )
        snapshot = append_assessment(
            store,
            claim=claim,
            observations=[observation],
            as_of=as_of,
            identity_status=IdentityStatus.NOT_APPLICABLE,
            identity_required=False,
            event_status=EventAssociationStatus.VERIFIED,
            event_claimed=True,
            publication=PublicationDisposition.APPROVED,
            independent=False,
        )
        company_decisions[company_slug] = project_writing_decision(
            snapshot,
            public_source_ids=("official-speakers",),
        ).as_dict()

    profiles_payload = load_json(
        company_profile_source_path(root, company_profiles_path),
        {},
    )
    browser_profile_metadata = load_browser_profile_metadata(root)
    if isinstance(profiles_payload, dict):
        for company_slug, raw_profile in sorted(profiles_payload.items()):
            if not isinstance(raw_profile, dict):
                continue
            company = company_names_by_slug.get(
                company_slug,
                company_name_from_slug(company_slug),
            )
            roster_hosts, roster_context = official_roster_company_context(
                company,
                speaker_rows,
            )
            official_context_values = [
                *company_context.get(company, ()),
                *roster_context,
            ]
            official_context = " ".join(official_context_values)
            affiliation_hosts = official_company_identity_hosts(
                company,
                list(company_context.get(company, ())),
            )
            accepted, gate_reasons, metadata, gate_signals = company_profile_gate(
                company,
                raw_profile,
                official_context,
                official_identity_hosts=tuple(
                    sorted(set(affiliation_hosts).union(roster_hosts))
                ),
                browser_metadata=browser_profile_metadata.get(company_slug),
            )
            provider_bindings = official_roster_company_provider_bindings(
                company,
                speaker_rows,
            )
            provider_host_evidence = company_provider_host_evidence(
                provider_evidence,
                provider_bindings,
                identity_bound=bool(gate_signals["identityHostMatch"]),
            )
            gate_signals["providerHostAvailabilityCorroborated"] = any(
                item["hostAvailabilityCorroborated"]
                for item in provider_host_evidence
            )
            company_profile_gates[company_slug] = {
                "status": "accepted_as_attributed_owner_context" if accepted else "held",
                "reasonCodes": [reason.value for reason in gate_reasons],
                "browserEvidenceUsed": company_slug in browser_profile_metadata,
                "providerEvidence": list(provider_host_evidence),
                "signals": gate_signals,
            }
            website = str(raw_profile.get("website") or "")
            if not website.startswith("https://"):
                continue
            claim = ClaimRecord.create(
                subject_id=f"company:{company_slug}",
                predicate="publishes owner-controlled organization context",
                object_value={
                    "title": metadata["title"],
                    "description": metadata["description"],
                    "siteName": metadata["site_name"],
                    "h1": metadata["h1"],
                },
                qualifiers={"website": website},
            )
            store.append_claim(claim)
            source = append_source(
                store,
                source_id=f"company-profile:{company_slug}",
                canonical_url=website,
                value={
                    "profile": raw_profile,
                    "browser": browser_profile_metadata.get(company_slug),
                },
                as_of=as_of,
            )
            observation = append_observation(
                store,
                claim=claim,
                source=source,
                span_id=f"company-owner-metadata:{company_slug}",
                cluster_id=f"owner-site:{urlsplit(website).hostname or company_slug}",
                as_of=as_of,
                directness=EvidenceDirectness.REPORTED,
                certainty=(
                    EvidenceCertainty.MEDIUM
                    if accepted
                    else EvidenceCertainty.LOW
                ),
                reasons=gate_reasons,
            )
            snapshot = append_assessment(
                store,
                claim=claim,
                observations=[observation],
                as_of=as_of,
                identity_status=(
                    IdentityStatus.VERIFIED
                    if accepted
                    else IdentityStatus.UNVERIFIED
                ),
                identity_required=True,
                event_status=EventAssociationStatus.NOT_CLAIMED,
                event_claimed=False,
                publication=(
                    PublicationDisposition.APPROVED
                    if accepted
                    else PublicationDisposition.HELD
                ),
                independent=False,
                provenance_reason=ReasonCode.SELF_INTERESTED_SOURCE,
            )
            company_profile_decisions[company_slug] = project_writing_decision(
                snapshot,
                public_source_ids=(f"company-profile-{company_slug}",),
            ).as_dict()

    for topic_slug, observations in sorted(topic_observations.items()):
        if not observations:
            continue
        claim = store.claim(observations[0].claim_id)
        if claim is None:
            continue
        clusters = {item.independence_cluster_id for item in observations}
        snapshot = append_assessment(
            store,
            claim=claim,
            observations=observations,
            as_of=as_of,
            identity_status=IdentityStatus.NOT_APPLICABLE,
            identity_required=False,
            event_status=EventAssociationStatus.VERIFIED,
            event_claimed=True,
            publication=PublicationDisposition.APPROVED,
            independent=len(clusters) >= 2,
        )
        topic_decisions[topic_slug] = project_writing_decision(
            snapshot,
            public_source_ids=tuple(sorted(set(topic_source_ids[topic_slug]))),
        ).as_dict()

    source_digest = content_digest(
        {
            "manifest": manifest,
            "speakers": speakers_payload,
            "sessionsIdentity": {
                "conference": sessions_payload.get("conference"),
                "scheduleVersion": sessions_payload.get("scheduleVersion"),
                "website": sessions_payload.get("website"),
            },
            "companyProfiles": profiles_payload,
            "browserProfileMetadata": browser_profile_metadata,
            "providerEvidenceGateStates": provider_gate_states,
        }
    )
    policy = {
        "schemaVersion": 1,
        "visibility": "internal-only",
        "sourceDigest": f"sha256:{source_digest}",
        "asOf": as_of.isoformat().replace("+00:00", "Z"),
        "database": str(store.database_path.relative_to(root)),
        "videoWritingDecisions": dict(sorted(video_decisions.items())),
        "topicWritingDecisions": dict(sorted(topic_decisions.items())),
        "topicVideoWritingDecisions": {
            topic: dict(sorted(rows.items()))
            for topic, rows in sorted(topic_video_decisions.items())
        },
        "peopleWritingDecisions": dict(sorted(people_decisions.items())),
        "companyWritingDecisions": dict(sorted(company_decisions.items())),
        "companyProfileWritingDecisions": dict(
            sorted(company_profile_decisions.items())
        ),
        "companyProfileGateStates": dict(sorted(company_profile_gates.items())),
        "providerEvidenceGateStates": provider_gate_states,
        "providerCapabilities": sorted(PROVIDER_REGISTRY),
        "policy": {
            "globalEntityReputationScores": False,
            "popularityAffectsClaimSupport": False,
            "eventCanonIsFieldScoped": True,
            "publicationImpliesEndorsement": False,
            "providerSuccessChangesPublicationAutomatically": False,
        },
    }
    return policy


def write_private_policy(root: Path = ROOT) -> tuple[Path, dict[str, Any]]:
    policy = build_private_policy(root)
    target = (
        root
        / ".ops"
        / "state"
        / "cache"
        / "wiki-maker"
        / "credibility-v2"
        / "writing-policy.json"
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(policy, indent=2, ensure_ascii=True, sort_keys=True) + "\n"
    if not target.is_file() or target.read_text(encoding="utf-8") != rendered:
        target.write_text(rendered, encoding="utf-8")
    return target, policy


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--check", action="store_true")
    parser.add_argument(
        "--company-profiles",
        type=Path,
        help=(
            "Explicit profile-candidate input. Defaults to private credibility-v2 "
            "state, with the legacy raw source retained as a read-only fallback."
        ),
    )
    args = parser.parse_args(argv)

    policy = build_private_policy(
        ROOT,
        company_profiles_path=args.company_profiles,
    )
    rendered = json.dumps(policy, indent=2, ensure_ascii=True, sort_keys=True) + "\n"
    changed = not POLICY_PATH.is_file() or POLICY_PATH.read_text(encoding="utf-8") != rendered
    if not args.check and changed:
        POLICY_PATH.parent.mkdir(parents=True, exist_ok=True)
        POLICY_PATH.write_text(rendered, encoding="utf-8")
    result = {
        "changed": changed,
        "path": str(POLICY_PATH.relative_to(ROOT)),
        "videos": len(policy["videoWritingDecisions"]),
        "people": len(policy["peopleWritingDecisions"]),
        "companies": len(policy["companyWritingDecisions"]),
        "companyProfiles": len(policy["companyProfileWritingDecisions"]),
        "topics": len(policy["topicWritingDecisions"]),
        "topicVideoLinks": sum(
            len(value) for value in policy["topicVideoWritingDecisions"].values()
        ),
    }
    print(json.dumps(result, sort_keys=True))
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
