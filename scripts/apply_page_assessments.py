#!/usr/bin/env python3
"""Assess entity-page evidence coverage and publish categorical capsules.

The numeric ledger is private. Public Markdown receives only the maker's
allowlisted ``sourceAssessment`` capsule, which describes evidence coverage for
the page's material claims rather than a person's or organization's reputation.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
from dataclasses import dataclass
from datetime import datetime, time, timezone
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
from urllib.parse import urlsplit

import yaml

from wiki_from_topic_maker.credibility_v2 import (
    AssessmentCoverageRecord,
    AssessmentCoverageStatus,
    AssessmentReceiptBinding,
    AssessmentScope,
    AssessmentTargetKind,
    AssessmentTargetRole,
    AssessmentUse,
    ClaimRecord,
    EvidenceKind,
    ObservationStance,
    OfficialPrimaryInclusionBasis,
    ProceduralStatus,
    PublicAssessmentBasis,
    PublicAssessmentCapsule,
    PublicAssessmentState,
    ScoreEvidence,
    ScoreReceipt,
    ScoreRuleset,
    SourceRole,
    evaluate_score,
    stable_credibility_id,
    validate_assessment_coverage,
    write_private_score_receipt,
)


ROOT = Path(__file__).resolve().parents[1]
TARGET_CATEGORIES = ("companies", "people", "tools", "topics")
SUBJECT_KINDS = {
    "companies": "company",
    "people": "person",
    "tools": "tool",
    "topics": "concept",
}
PRIVATE_ROOT = Path(".ops/state/cache/wiki-maker/credibility-v2")
PAGE_ASSESSMENT_ROOT = PRIVATE_ROOT / "page-assessments"
ACTIVE_RULESET = PRIVATE_ROOT / "scoring-policies/active.json"
OFFICIAL_EVENT_URL = "https://ai.engineer/worldsfair"
FALLBACK_AS_OF = datetime(2026, 7, 2, tzinfo=timezone.utc)

MARKDOWN_LINK_RE = re.compile(
    r"(?<!!)\[([^\]]+)\]\((https://[^\s)]+)\)", re.IGNORECASE
)
COMPARISON_MARKERS = ("comparison", "derived-only", "external context")
CONTESTED_LABEL_MARKERS = ("contradiction", "contested", "disputed")
DERIVED_LABEL_MARKERS = (
    "highlight",
    "local slide ocr",
    "slide/video-derived",
    "synthesis",
    "topic synthesis",
    "transcript",
    "video frames",
    "youtube metadata",
)
INDEPENDENT_REPORT_LABELS = {
    "public research article",
    "y combinator profile",
}
REPOSITORY_LABELS = {"public github project", "public repository"}
FIRST_PARTY_LABELS = {
    "public company site",
    "public professional profile",
    "justice ai unit official site",
    "justice ai unit public site",
}
SOCIAL_OR_PLATFORM_HOSTS = {
    "github.com",
    "linkedin.com",
    "pypi.org",
    "x.com",
    "youtube.com",
    "youtu.be",
}


@dataclass(frozen=True)
class Link:
    label: str
    url: str

    @property
    def host(self) -> str:
        return (urlsplit(self.url).hostname or "").casefold().removeprefix("www.")


@dataclass(frozen=True)
class EvidenceCandidate:
    kind: EvidenceKind
    source_role: SourceRole
    source_id: str
    source_url: str
    locator: str
    cluster_id: str
    explanation: str
    publisher: str
    evidence_sha256: str
    observed_at: datetime
    stance: ObservationStance = ObservationStance.SUPPORTS
    procedural_status: ProceduralStatus = ProceduralStatus.NOT_APPLICABLE
    human_review_required: bool = False

    @property
    def independent(self) -> bool:
        return self.source_role in {
            SourceRole.INDEPENDENT_PRIMARY,
            SourceRole.INDEPENDENT_SECONDARY,
        }


def _canonical_digest(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return "sha256:" + sha256(encoded).hexdigest()


def _official_record_candidate(
    root: Path,
    *,
    page_id: str,
    category: str,
    title: str,
    labels: Sequence[str],
    as_of: datetime,
) -> EvidenceCandidate | None:
    """Bind an official label to an exact checked-in schedule/roster record."""

    title_key = title.casefold().strip()
    candidates: tuple[tuple[Path, str, str], ...]
    if category == "people":
        candidates = ((root / "raw/sources/official-speakers.json", "speakers", "name"),)
    elif category == "companies":
        candidates = ((root / "raw/sources/official-speakers.json", "speakers", "company"),)
    else:
        candidates = ((root / "raw/sources/official-sessions.json", "sessions", "_text"),)
    for path, collection_key, field in candidates:
        payload = _load_json(path, {})
        rows = payload.get(collection_key, []) if isinstance(payload, Mapping) else []
        if not isinstance(rows, list):
            continue
        matched: Mapping[str, Any] | None = None
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            if field == "_text":
                haystack = " ".join(
                    str(row.get(key) or "") for key in ("title", "description", "track")
                )
                pattern = rf"(?<![A-Za-z0-9]){re.escape(title_key)}(?![A-Za-z0-9])"
                if re.search(pattern, haystack.casefold()):
                    matched = row
                    break
            elif str(row.get(field) or "").casefold().strip() == title_key:
                matched = row
                break
        if matched is None:
            continue
        relative = path.relative_to(root).as_posix()
        return EvidenceCandidate(
            kind=EvidenceKind.DIRECT_PRIMARY_RECORD,
            source_role=SourceRole.OFFICIAL_PRIMARY,
            source_id=f"source:official-wf26-{path.stem}",
            source_url=OFFICIAL_EVENT_URL,
            locator=f"{relative}#{collection_key}:{title}",
            cluster_id=f"cluster:official-wf26-{path.stem}",
            explanation=(
                f"The checked-in official {path.stem} record establishes only the "
                f"event-scoped source association for {page_id}; labels: {', '.join(labels)}."
            ),
            publisher="AI Engineer",
            evidence_sha256=_canonical_digest(matched),
            observed_at=as_of,
        )
    return None


def _official_media_candidates(
    root: Path,
    *,
    page_id: str,
    body: str,
    as_of: datetime,
) -> tuple[EvidenceCandidate, ...]:
    manifest = _load_json(
        root / "raw/sources/official-wf26-video-manifest.json",
        {},
    )
    rows = manifest.get("videos", []) if isinstance(manifest, Mapping) else []
    by_id = {
        str(row.get("id")): row
        for row in rows
        if isinstance(row, Mapping)
        and re.fullmatch(r"[A-Za-z0-9_-]{11}", str(row.get("id") or ""))
    }
    referenced_ids = sorted(
        set(re.findall(r"youtube-([A-Za-z0-9_-]{11})", body)) & set(by_id)
    )
    accepted_associations = {
        "explicit_wf26_official_livestream",
        "official_channel_explicit_wf26_title",
        "official_channel_plus_schedule_text",
        "official_wf26_playlist_membership",
    }
    candidates: list[EvidenceCandidate] = []
    for video_id in referenced_ids:
        row = by_id[video_id]
        if (
            str(row.get("associationEvidence") or "") not in accepted_associations
            or str(row.get("mediaType") or "")
            not in {"talk_recording", "event_livestream"}
            or str(row.get("videoAvailability") or "") not in {"public", "unlisted"}
        ):
            continue
        candidates.append(
            EvidenceCandidate(
                kind=EvidenceKind.DIRECT_PRIMARY_RECORD,
                source_role=SourceRole.OFFICIAL_PRIMARY,
                source_id=f"source:official-wf26-youtube-{video_id}",
                source_url=f"https://www.youtube.com/watch?v={video_id}",
                locator=(
                    "raw/sources/official-wf26-video-manifest.json"
                    f"#videos[id={video_id}]"
                ),
                cluster_id=f"cluster:official-wf26-video-{video_id}",
                explanation=(
                    f"The exact manifest record and page link establish that {page_id} "
                    "cites an official WF26 recording. This does not independently "
                    "validate claims made in the recording or derived transcript/OCR."
                ),
                publisher="AI Engineer",
                evidence_sha256=_canonical_digest(row),
                observed_at=as_of,
            )
        )
    return tuple(candidates)


def _provider_url_matches(provider_id: str, receipt_url: str, public_url: str) -> bool:
    left = urlsplit(receipt_url)
    right = urlsplit(public_url)
    if provider_id == "github_rest" and right.hostname == "github.com":
        expected = "/repos/" + right.path.strip("/")
        return left.hostname == "api.github.com" and left.path.rstrip("/") == expected
    return (
        (left.hostname or "").casefold().removeprefix("www.")
        == (right.hostname or "").casefold().removeprefix("www.")
        and left.path.rstrip("/") == right.path.rstrip("/")
    )


def _verified_provider_candidate(
    root: Path,
    *,
    page_id: str,
    subject_id: str,
    link: Link,
    kind: EvidenceKind,
    source_role: SourceRole,
    explanation: str,
    allowed_providers: Sequence[str],
) -> EvidenceCandidate | None:
    receipts = root / PRIVATE_ROOT / "receipts/provider-fetch"
    for path in sorted(receipts.glob("*.json")):
        payload = _load_json(path, {})
        if not isinstance(payload, Mapping):
            continue
        provider_id = str(payload.get("providerId") or "")
        if (
            payload.get("outcome") != "success"
            or payload.get("subjectId") != subject_id
            or provider_id not in allowed_providers
        ):
            continue
        receipt_url = str(payload.get("finalUrl") or payload.get("requestUrl") or "")
        if not _provider_url_matches(provider_id, receipt_url, link.url):
            continue
        cache_relative = str(payload.get("cachePath") or "")
        cache_path = (root / cache_relative).resolve()
        private_root = (root / PRIVATE_ROOT).resolve()
        try:
            cache_path.relative_to(private_root)
        except ValueError:
            continue
        expected = str(payload.get("responseSha256") or "").removeprefix("sha256:")
        if not cache_path.is_file() or sha256(cache_path.read_bytes()).hexdigest() != expected:
            continue
        observed_at = _parse_datetime(payload.get("retrievedAt"))
        if observed_at is None:
            continue
        return EvidenceCandidate(
            kind=kind,
            source_role=source_role,
            source_id=_host_source_id(provider_id, link.host),
            source_url=link.url,
            locator=f"{path.relative_to(root).as_posix()} -> {cache_relative}",
            cluster_id=(
                f"cluster:{provider_id}-{link.host}-"
                f"{urlsplit(link.url).path.strip('/').casefold()}"
            ),
            explanation=f"{explanation} Verified provider bytes are bound to {page_id}.",
            publisher=link.host,
            evidence_sha256=f"sha256:{expected}",
            observed_at=observed_at,
        )
    return None


@dataclass(frozen=True)
class PageAssessment:
    page_id: str
    subject_id: str
    category: str
    claim: ClaimRecord
    assessment_snapshot_id: str
    state: PublicAssessmentState
    basis: PublicAssessmentBasis
    capsule: PublicAssessmentCapsule
    bindings: tuple[AssessmentReceiptBinding, ...]
    receipt_id: str
    coverage_status: AssessmentCoverageStatus
    official_primary_inclusion: bool
    independent_support: bool
    ignored: tuple[dict[str, str], ...]
    rendered_markdown: str


def _parse_datetime(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    text = value.strip()
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
            return datetime.combine(
                datetime.strptime(text, "%Y-%m-%d").date(),
                time.min,
                tzinfo=timezone.utc,
            )
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def assessment_as_of(root: Path) -> datetime:
    """Return a deterministic timestamp from checked-in source observations."""

    candidates: list[datetime] = []
    manifest = _load_json(
        root / "raw/sources/official-wf26-video-manifest.json", {}
    )
    if isinstance(manifest, Mapping):
        for key in ("checkedAt", "generatedAt", "retrievedAt", "updatedAt"):
            if parsed := _parse_datetime(manifest.get(key)):
                candidates.append(parsed)
        videos = manifest.get("videos", [])
        if isinstance(videos, list):
            for item in videos:
                if not isinstance(item, Mapping):
                    continue
                # ``releaseDate`` can be a future premiere. ``uploadDate`` is
                # the observed channel date and cannot time-travel the ledger.
                if parsed := _parse_datetime(item.get("uploadDate")):
                    candidates.append(parsed)
    provider_receipts = root / PRIVATE_ROOT / "receipts/provider-fetch"
    for path in sorted(provider_receipts.glob("*.json")):
        payload = _load_json(path, {})
        if not isinstance(payload, Mapping) or payload.get("outcome") != "success":
            continue
        if parsed := _parse_datetime(payload.get("retrievedAt")):
            candidates.append(parsed)
    return max(candidates, default=FALLBACK_AS_OF)


def _load_json(path: Path, fallback: Any) -> Any:
    if not path.is_file():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def _frontmatter_and_body(raw: str) -> tuple[dict[str, Any], str, int]:
    if not raw.startswith("---\n"):
        raise ValueError("assessed wiki pages require YAML frontmatter")
    end = raw.find("\n---\n", 4)
    if end < 0:
        raise ValueError("wiki page frontmatter has no closing boundary")
    loaded = yaml.safe_load(raw[4:end]) or {}
    if not isinstance(loaded, Mapping):
        raise ValueError("wiki frontmatter must be a mapping")
    return dict(loaded), raw[end + 5 :], end


def _labels(frontmatter: Mapping[str, Any]) -> tuple[str, ...]:
    value = frontmatter.get("sourceLabels", [])
    if isinstance(value, str):
        return (value.strip(),) if value.strip() else ()
    if not isinstance(value, list):
        return ()
    return tuple(sorted({str(item).strip() for item in value if str(item).strip()}))


def _links(frontmatter: Mapping[str, Any], body: str) -> tuple[Link, ...]:
    links = {Link(label.strip(), url.rstrip(".,;")) for label, url in MARKDOWN_LINK_RE.findall(body)}
    for key in (
        "blog",
        "linkedin",
        "repository",
        "twitter",
        "website",
    ):
        value = frontmatter.get(key)
        if isinstance(value, str) and value.startswith("https://"):
            links.add(Link(key, value.rstrip(".,;")))
    return tuple(sorted(links, key=lambda item: (item.url, item.label.casefold())))


def _host_source_id(role: str, host: str) -> str:
    normalized = re.sub(r"[^a-z0-9.-]+", "-", host.casefold()).strip("-")
    return f"source:{role}-{normalized or 'unknown'}"


def _choose_link(
    links: Sequence[Link],
    *,
    hosts: Iterable[str] = (),
    label_terms: Iterable[str] = (),
    excluded_hosts: Iterable[str] = (),
) -> Link | None:
    required_hosts = {item.casefold().removeprefix("www.") for item in hosts}
    excluded = {item.casefold().removeprefix("www.") for item in excluded_hosts}
    terms = tuple(item.casefold() for item in label_terms)
    for link in links:
        host_match = not required_hosts or any(
            link.host == host or link.host.endswith(f".{host}")
            for host in required_hosts
        )
        term_match = not terms or any(term in link.label.casefold() for term in terms)
        excluded_match = any(
            link.host == host or link.host.endswith(f".{host}") for host in excluded
        )
        if host_match and term_match and not excluded_match:
            return link
    return None


def _page_candidates(
    root: Path,
    page_id: str,
    subject_id: str,
    category: str,
    frontmatter: Mapping[str, Any],
    body: str,
    *,
    as_of: datetime,
) -> tuple[tuple[EvidenceCandidate, ...], tuple[dict[str, str], ...], bool]:
    labels = _labels(frontmatter)
    lowered_labels = {item.casefold(): item for item in labels}
    links = _links(frontmatter, body)
    candidates: list[EvidenceCandidate] = []
    admitted_urls: set[str] = set()
    admitted_labels: set[str] = set()

    official_labels = tuple(
        label
        for label in labels
        if label.casefold().startswith("official ")
        or label.casefold() == "official schedule"
    )
    if official_labels:
        official = _official_record_candidate(
            root,
            page_id=page_id,
            category=category,
            title=str(frontmatter.get("title") or ""),
            labels=official_labels,
            as_of=as_of,
        )
        if official is not None:
            candidates.append(official)
            admitted_labels.update(official_labels)

    media_candidates = _official_media_candidates(
        root,
        page_id=page_id,
        body=body,
        as_of=as_of,
    )
    if media_candidates:
        candidates.extend(media_candidates)
        admitted_labels.update(
            label
            for label in labels
            if any(marker in label.casefold() for marker in DERIVED_LABEL_MARKERS)
        )

    owner_website = str(frontmatter.get("website") or "")
    owner_host = (
        (urlsplit(owner_website).hostname or "").casefold().removeprefix("www.")
        if owner_website.startswith("https://")
        else ""
    )

    if lowered_labels.keys() & FIRST_PARTY_LABELS:
        link = _choose_link(links, hosts=(owner_host,)) if owner_host else None
        if link is None:
            link = _choose_link(
                links,
                label_terms=("official site", "website", "profile", "linkedin"),
            )
        if link is not None:
            verified = _verified_provider_candidate(
                root,
                page_id=page_id,
                subject_id=subject_id,
                link=link,
                kind=EvidenceKind.OWNER_ASSERTION,
                source_role=SourceRole.FIRST_PARTY,
                explanation="Owner-controlled public material provides attributed context.",
                allowed_providers=("owner_web",),
            )
            if verified is not None:
                candidates.append(verified)
                admitted_urls.add(link.url)
                admitted_labels.update(
                    original
                    for lowered, original in lowered_labels.items()
                    if lowered in FIRST_PARTY_LABELS
                )

    if lowered_labels.keys() & REPOSITORY_LABELS:
        link = _choose_link(links, hosts=("github.com", "gitlab.com"))
        if link is not None:
            verified = _verified_provider_candidate(
                root,
                page_id=page_id,
                subject_id=subject_id,
                link=link,
                kind=EvidenceKind.REPRODUCIBLE_ARTIFACT,
                source_role=SourceRole.FIRST_PARTY,
                explanation=(
                    "The linked public repository is inspectable technical context; "
                    "it is not independent endorsement."
                ),
                allowed_providers=("github_rest",),
            )
            if verified is not None:
                candidates.append(verified)
                admitted_urls.add(link.url)
                admitted_labels.update(
                    original
                    for lowered, original in lowered_labels.items()
                    if lowered in REPOSITORY_LABELS
                )

    ignored: list[dict[str, str]] = []
    for label in labels:
        if label not in admitted_labels:
            lowered = label.casefold()
            if any(marker in lowered for marker in DERIVED_LABEL_MARKERS):
                reason = "derived_or_transcript_layer_not_promoted"
            elif any(marker in lowered for marker in COMPARISON_MARKERS):
                reason = "comparison_context_not_promoted"
            elif any(marker in lowered for marker in CONTESTED_LABEL_MARKERS):
                reason = "disagreement_label_without_cited_contradiction"
            else:
                reason = "unclassified_source_label"
            ignored.append(
                {"pageId": page_id, "kind": "source_label", "value": label, "reason": reason}
            )
    contradicting = frontmatter.get("contradictingSources", [])
    if isinstance(contradicting, list):
        for value in contradicting:
            if isinstance(value, str) and value.startswith("https://"):
                ignored.append(
                    {
                        "pageId": page_id,
                        "kind": "contradicting_source",
                        "value": value,
                        "reason": "source_content_not_observed",
                    }
                )
    for link in links:
        if link.url not in admitted_urls:
            ignored.append(
                {
                    "pageId": page_id,
                    "kind": "public_link",
                    "value": link.url,
                    "reason": "link_not_independently_classified",
                }
            )

    status = str(frontmatter.get("status") or "").casefold()
    comparison_only = any(
        marker in status or any(marker in label.casefold() for label in labels)
        for marker in COMPARISON_MARKERS
    )
    ordered_candidates = tuple(
        sorted(
            candidates,
            key=lambda item: (
                item.kind.value,
                item.cluster_id,
                item.source_url,
                item.locator,
            ),
        )
    )
    ordered_ignored = tuple(
        sorted(ignored, key=lambda item: (item["pageId"], item["kind"], item["value"], item["reason"]))
    )
    return ordered_candidates, ordered_ignored, comparison_only


def _factor_selections(
    ruleset: ScoreRuleset,
    candidate: EvidenceCandidate,
) -> tuple[tuple[str, str], ...]:
    rule = ruleset.rule_for(candidate.kind)
    choices: dict[str, set[str]] = {}
    for choice in rule.factor_choices:
        choices.setdefault(choice.factor_id, set()).add(choice.choice_id)
    authority = {
        SourceRole.OFFICIAL_PRIMARY: "official_original",
        SourceRole.INDEPENDENT_PRIMARY: "independent_documented",
        SourceRole.INDEPENDENT_SECONDARY: "independent_documented",
        SourceRole.FIRST_PARTY: "first_party_or_indirect",
    }.get(candidate.source_role, "unusable")
    values = {
        "claim_relevance": "exact",
        "method_quality": "strong",
        "source_authority": authority,
    }
    selected: list[tuple[str, str]] = []
    for factor_id, allowed in sorted(choices.items()):
        value = values.get(factor_id)
        if value in allowed:
            selected.append((factor_id, value))
        elif len(allowed) == 1:
            selected.append((factor_id, next(iter(allowed))))
        else:
            raise ValueError(
                f"ruleset has no deterministic selection for {factor_id!r} on {candidate.kind.value}"
            )
    return tuple(selected)


def _score_evidence(
    candidate: EvidenceCandidate,
    *,
    claim: ClaimRecord,
    ruleset: ScoreRuleset,
) -> ScoreEvidence:
    source_version_id = stable_credibility_id(
        "source-version",
        candidate.source_id,
        candidate.source_url,
        candidate.evidence_sha256,
        candidate.observed_at.isoformat(),
    )
    observation_id = stable_credibility_id(
        "observation", claim.claim_id, source_version_id, candidate.locator, candidate.stance.value
    )
    return ScoreEvidence.create(
        claim_id=claim.claim_id,
        subject_id=claim.subject_id,
        kind=candidate.kind,
        stance=candidate.stance,
        source_id=candidate.source_id,
        source_version_id=source_version_id,
        observation_id=observation_id,
        independence_cluster_id=candidate.cluster_id,
        source_url=candidate.source_url,
        evidence_locator=candidate.locator,
        evidence_sha256=candidate.evidence_sha256,
        source_role=candidate.source_role,
        procedural_status=candidate.procedural_status,
        evidence_at=candidate.observed_at,
        observed_at=candidate.observed_at,
        factor_selections=_factor_selections(ruleset, candidate),
        explanation=candidate.explanation,
        source_publisher=candidate.publisher,
        human_review_required=candidate.human_review_required,
    )


def _rewrite_source_assessment(
    raw: str,
    capsule: Mapping[str, Any] | None,
    *,
    body_sha256: str | None = None,
) -> str:
    frontmatter, _body, end = _frontmatter_and_body(raw)
    if "evidenceAssessment" in frontmatter:
        raise ValueError(
            "legacy evidenceAssessment frontmatter must be removed before sourceAssessment is generated"
        )
    header_lines = raw[4:end].splitlines()
    output: list[str] = []
    skipping = False
    for line in header_lines:
        top_level = bool(line) and not line[0].isspace()
        if top_level and line.startswith("sourceAssessment:"):
            skipping = True
            continue
        if skipping and top_level:
            skipping = False
        if top_level and line.startswith("sourceAssessmentBodySha256:"):
            continue
        if not skipping:
            output.append(line)
    if capsule is not None:
        if not re.fullmatch(r"sha256:[0-9a-f]{64}", body_sha256 or ""):
            raise ValueError("source assessment body digest is required")
        rendered_capsule = yaml.safe_dump(
            {"sourceAssessment": dict(capsule)},
            allow_unicode=False,
            default_flow_style=False,
            sort_keys=False,
            width=120,
        ).rstrip()
        output.append(rendered_capsule)
        output.append(f"sourceAssessmentBodySha256: {body_sha256}")
    header = "\n".join(output).strip("\n")
    return f"---\n{header}\n---\n{raw[end + 5:]}"


def _atomic_write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
            handle.write(value)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def _atomic_write_json(path: Path, value: Any) -> None:
    _atomic_write_text(
        path,
        json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
    )


def load_ruleset(root: Path) -> ScoreRuleset:
    path = root / ACTIVE_RULESET
    if not path.is_file():
        raise FileNotFoundError(f"private scoring ruleset is required: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError("private scoring ruleset must be a JSON object")
    return ScoreRuleset.from_dict(payload)


def _assess_page(
    root: Path,
    path: Path,
    *,
    ruleset: ScoreRuleset,
    as_of: datetime,
) -> PageAssessment:
    raw = path.read_text(encoding="utf-8")
    frontmatter, body, _end = _frontmatter_and_body(raw)
    category = path.parent.name
    page_id = path.relative_to(root / "wiki").with_suffix("").as_posix()
    subject_id = f"{SUBJECT_KINDS[category]}:{path.stem}"
    claim = ClaimRecord.create(
        subject_id=subject_id,
        predicate="has verified source associations for material page evidence",
        object_value=True,
        qualifiers={
            "assessmentKind": "page_evidence_coverage",
            "category": category,
            "pageId": page_id,
        },
    )
    candidates, ignored, comparison_only = _page_candidates(
        root,
        page_id,
        subject_id,
        category,
        frontmatter,
        body,
        as_of=as_of,
    )
    evidence = tuple(
        _score_evidence(candidate, claim=claim, ruleset=ruleset)
        for candidate in candidates
    )
    body_digest = sha256(body.strip().encode("utf-8")).hexdigest()
    snapshot_id = stable_credibility_id(
        "assessment-snapshot",
        claim.claim_id,
        as_of.isoformat(),
        body_digest,
        [item.evidence_id for item in evidence],
    )
    use = (
        AssessmentUse.COMPARISON_CONTEXT
        if comparison_only
        else AssessmentUse.PUBLIC_ASSERTION
        if len(
            {
                item.independence_cluster_id
                for item in evidence
                if item.source_role
                in {
                    SourceRole.INDEPENDENT_PRIMARY,
                    SourceRole.INDEPENDENT_SECONDARY,
                }
            }
        )
        >= 2
        else AssessmentUse.ATTRIBUTED_CONTEXT
    )
    scope = AssessmentScope.create(
        claim_id=claim.claim_id,
        subject_id=claim.subject_id,
        assessment_snapshot_id=snapshot_id,
        domain=f"{category} page evidence coverage",
        use=use,
        as_of=as_of,
    )
    receipt = evaluate_score(scope, ruleset, evidence)
    receipt_files = write_private_score_receipt(root, receipt, ruleset)
    if not receipt_files.replay_valid:
        raise ValueError(f"private receipt failed replay: {receipt.receipt_id}")

    official_evidence = next(
        (item for item in evidence if item.source_role is SourceRole.OFFICIAL_PRIMARY),
        None,
    )
    official_primary_inclusion = official_evidence is not None
    if official_evidence is not None:
        OfficialPrimaryInclusionBasis(scope=scope, evidence=official_evidence)

    independent_clusters = {
        item.independence_cluster_id
        for item in evidence
        if item.source_role in {
            SourceRole.INDEPENDENT_PRIMARY,
            SourceRole.INDEPENDENT_SECONDARY,
        }
        and item.stance is ObservationStance.SUPPORTS
    }
    has_contradiction = any(item.stance is ObservationStance.REFUTES for item in evidence)
    independent_support = bool(independent_clusters)
    coverage_status = (
        AssessmentCoverageStatus.ASSESSED
        if receipt.line_items
        else AssessmentCoverageStatus.NO_ADMITTED_EVIDENCE
    )
    if coverage_status is AssessmentCoverageStatus.NO_ADMITTED_EVIDENCE:
        state = PublicAssessmentState.PENDING
        basis = PublicAssessmentBasis.NO_ADMITTED_EVIDENCE
    elif has_contradiction:
        state = PublicAssessmentState.CONTESTED
        basis = PublicAssessmentBasis.SOURCES_DISAGREE
    elif len(independent_clusters) >= 2 and not comparison_only:
        state = PublicAssessmentState.STRONG
        basis = PublicAssessmentBasis.INDEPENDENTLY_SUPPORTED
    else:
        state = PublicAssessmentState.LIMITED
        basis = (
            PublicAssessmentBasis.OFFICIAL_PRIMARY_CANONICAL
            if official_primary_inclusion
            else PublicAssessmentBasis.SOURCE_ATTRIBUTED
        )
    capsule = PublicAssessmentCapsule.create(
        scope=scope,
        state=state,
        basis=basis,
        public_source_ids=tuple(sorted({item.source_id for item in evidence})),
    )
    updated = _rewrite_source_assessment(
        raw,
        capsule.as_dict(),
        body_sha256=f"sha256:{body_digest}",
    )

    bindings = tuple(
        AssessmentReceiptBinding(
            target_id=target_id,
            target_kind=target_kind,
            receipt_id=receipt.receipt_id,
            scope_id=scope.scope_id,
            claim_id=claim.claim_id,
            subject_id=subject_id,
        )
        for target_kind, target_id in (
            (AssessmentTargetKind.ENTITY, subject_id),
            (AssessmentTargetKind.PAGE, f"page:{page_id}"),
        )
    )
    return PageAssessment(
        page_id=page_id,
        subject_id=subject_id,
        category=category,
        claim=claim,
        assessment_snapshot_id=snapshot_id,
        state=state,
        basis=basis,
        capsule=capsule,
        bindings=bindings,
        receipt_id=receipt.receipt_id,
        coverage_status=coverage_status,
        official_primary_inclusion=official_primary_inclusion,
        independent_support=independent_support,
        ignored=ignored,
        rendered_markdown=updated,
    )


def apply_page_assessments(
    root: Path = ROOT,
    *,
    minimum_pages: int = 0,
) -> dict[str, Any]:
    root = root.resolve()
    ruleset = load_ruleset(root)
    as_of = assessment_as_of(root)
    category_paths = tuple(
        sorted(
            path
            for category in TARGET_CATEGORIES
            for path in (root / "wiki" / category).glob("*.md")
        )
    )
    page_paths = tuple(
        path
        for path in category_paths
        if path.stem not in {"index", path.parent.name}
    )
    excluded_paths = tuple(path for path in category_paths if path not in page_paths)
    if len(page_paths) < minimum_pages:
        raise ValueError(
            f"entity-page inventory shrank below the required floor: {len(page_paths)} < {minimum_pages}"
        )
    assessments = tuple(
        _assess_page(root, path, ruleset=ruleset, as_of=as_of)
        for path in page_paths
    )
    if len(assessments) != len(page_paths):
        raise ValueError("not every inventoried entity page produced an assessment")
    receipts_by_id = {}
    for assessment in assessments:
        receipt_path = (
            root
            / PRIVATE_ROOT
            / "receipts/scoring"
            / f"{assessment.receipt_id.rsplit(':', 1)[-1]}.json"
        )
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        receipts_by_id[assessment.receipt_id] = ScoreReceipt.from_dict(receipt)

    records: list[AssessmentCoverageRecord] = []
    for assessment in assessments:
        for target_kind, target_id in (
            (AssessmentTargetKind.ENTITY, assessment.subject_id),
            (AssessmentTargetKind.PAGE, f"page:{assessment.page_id}"),
        ):
            records.append(
                AssessmentCoverageRecord.create(
                    target_id=target_id,
                    target_kind=target_kind,
                    target_role=AssessmentTargetRole.EVIDENCE_BEARING,
                    status=assessment.coverage_status,
                    bindings=tuple(
                        binding
                        for binding in assessment.bindings
                        if binding.target_kind is target_kind
                        and binding.target_id == target_id
                    ),
                )
            )
    records.extend(
        AssessmentCoverageRecord.create(
            target_id=(
                "page:" + path.relative_to(root / "wiki").with_suffix("").as_posix()
            ),
            target_kind=AssessmentTargetKind.PAGE,
            target_role=AssessmentTargetRole.NAVIGATION,
            status=AssessmentCoverageStatus.NOT_APPLICABLE,
        )
        for path in excluded_paths
    )
    validate_assessment_coverage(
        records,
        tuple(receipts_by_id.values()),
        require_complete=True,
    )
    covered_pages = {
        record.target_id.removeprefix("page:")
        for record in records
        if record.target_kind is AssessmentTargetKind.PAGE
    }
    expected_pages = {
        *(assessment.page_id for assessment in assessments),
        *(
            path.relative_to(root / "wiki").with_suffix("").as_posix()
            for path in excluded_paths
        ),
    }
    if covered_pages != expected_pages:
        missing = sorted(expected_pages - covered_pages)
        raise ValueError(
            "category pages without explicit assessment coverage: "
            + ", ".join(missing)
        )

    # Public pages are updated only after every assessment, binding, and
    # coverage contract has validated. A failed run may leave private receipts
    # for audit/replay, but it cannot leave a partially projected public corpus.
    for assessment in assessments:
        path = root / "wiki" / f"{assessment.page_id}.md"
        if path.read_text(encoding="utf-8") != assessment.rendered_markdown:
            _atomic_write_text(path, assessment.rendered_markdown)
    for path in excluded_paths:
        raw = path.read_text(encoding="utf-8")
        updated = _rewrite_source_assessment(raw, None)
        if updated != raw:
            _atomic_write_text(path, updated)

    private_output = root / PAGE_ASSESSMENT_ROOT
    inventory = {
        "schemaVersion": 1,
        "visibility": "internal-only",
        "assessmentKind": "page_evidence_coverage",
        "asOf": as_of.isoformat().replace("+00:00", "Z"),
        "targetCategories": list(TARGET_CATEGORIES),
        "pageCount": len(assessments),
        "excludedNonEntityPages": [
            path.relative_to(root / "wiki").as_posix() for path in excluded_paths
        ],
        "pages": [
            {
                "pageId": item.page_id,
                "subjectId": item.subject_id,
                "category": item.category,
                "claim": item.claim.as_dict(),
                "assessmentSnapshotId": item.assessment_snapshot_id,
                "assessmentStatus": item.coverage_status.value,
                "receiptId": item.receipt_id,
                "state": item.state.value,
                "basis": item.basis.value,
                "officialPrimaryInclusionValidated": item.official_primary_inclusion,
                "independentSupport": item.independent_support,
            }
            for item in assessments
        ],
    }
    coverage = {
        "schemaVersion": 1,
        "visibility": "internal-only",
        "recordCount": len(records),
        "records": [record.as_dict() for record in sorted(records, key=lambda item: (item.target_kind.value, item.target_id))],
    }
    ignored = {
        "schemaVersion": 1,
        "visibility": "internal-only",
        "assessmentKind": "page_evidence_coverage",
        "items": [entry for item in assessments for entry in item.ignored],
    }
    _atomic_write_json(private_output / "inventory.json", inventory)
    _atomic_write_json(private_output / "coverage-bindings.json", coverage)
    _atomic_write_json(private_output / "ignored-evidence.json", ignored)

    counts = {
        state.value: sum(item.state is state for item in assessments)
        for state in PublicAssessmentState
    }
    result = {
        "schemaVersion": 1,
        "pageCount": len(assessments),
        "coverageRecordCount": len(records),
        "excludedNonEntityPageCount": len(excluded_paths),
        "states": counts,
        "assessmentCoverageStatuses": {
            status.value: sum(
                item.coverage_status is status for item in assessments
            )
            for status in (
                AssessmentCoverageStatus.ASSESSED,
                AssessmentCoverageStatus.NO_ADMITTED_EVIDENCE,
            )
        },
        "privateInventory": str(private_output / "inventory.json"),
    }
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--minimum-pages", type=int, default=0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = apply_page_assessments(args.root, minimum_pages=args.minimum_pages)
    print(json.dumps(result, ensure_ascii=True, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
