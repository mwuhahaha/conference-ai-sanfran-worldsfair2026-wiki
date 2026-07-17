#!/usr/bin/env python3
"""Run bounded, private Chrome checks for unresolved third-party site claims.

Chrome is a last-mile metadata reader for owner-controlled public pages whose
static validation was inconclusive. API/static providers remain preferred.
The tool never logs in, submits forms, solves challenges, follows discovered
links, or makes a publication decision. All live receipts stay under ignored
project state.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import ipaddress
import json
import re
import socket
import sys
import urllib.error
import urllib.request
import urllib.robotparser
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence
from urllib.parse import urljoin, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    ROOT / ".ops" / "state" / "cache" / "third-party-connections" / "latest-audit.json"
)
PRIVATE_OUTPUT_ROOT = (
    ROOT
    / ".ops"
    / "state"
    / "cache"
    / "wiki-maker"
    / "credibility-v2"
    / "browser"
)
CHROME_AGENT_PROJECT = Path("/garage/projects/agents/chrome-agent-python")
EXTRACTOR_VERSION = "wf26-owner-metadata-v1"
SELECTOR_CONTRACT_VERSION = "owner-metadata-dom-v1"
USER_AGENT = "WikiMakerCredibilityBrowser/1.0 (+https://aie-worldsfair2026.plusrobot.ai/)"
MAX_JOBS = 20
MAX_VISIBLE_TEXT = 8_000
MAX_ROBOTS_BYTES = 256 * 1024

TARGET_FINDING_KINDS = (
    "domain_guess_without_company_name_corroboration",
    "company_site_attached_without_successful_validation",
)
FINDING_KIND_ORDER = {kind: index for index, kind in enumerate(TARGET_FINDING_KINDS)}
SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}
SOCIAL_OR_AUTH_HOSTS = frozenset(
    {
        "accounts.google.com",
        "facebook.com",
        "instagram.com",
        "linkedin.com",
        "threads.net",
        "tiktok.com",
        "twitter.com",
        "x.com",
    }
)
API_OR_STATIC_PREFERRED_HOSTS = frozenset(
    {
        "api.github.com",
        "company-information.service.gov.uk",
        "crates.io",
        "doi.org",
        "github.com",
        "npmjs.com",
        "orcid.org",
        "pypi.org",
        "sec.gov",
        "wikidata.org",
        "wikipedia.org",
    }
)
DISALLOWED_HOST_SUFFIXES = (
    ".example",
    ".internal",
    ".invalid",
    ".local",
    ".localhost",
    ".onion",
    ".test",
)
AUTH_PATH_RE = re.compile(r"(?:^|/)(?:auth|login|log-in|signin|sign-in)(?:/|$)", re.I)
TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9._-]{1,63}", re.I)


def _import_maker_browser_contracts() -> tuple[Any, ...] | None:
    """Load the reusable maker contract in normal and Chrome-agent runtimes."""

    try:
        from wiki_from_topic_maker.credibility_v2 import (  # type: ignore[import-not-found]
            BrowserJob,
            BrowserJobPolicy,
            BrowserJobPurpose,
            BrowserOutcome,
            BrowserReceipt,
            validate_receipt_for_job,
        )
    except ModuleNotFoundError:
        sibling_source = ROOT.parent / "wiki-from-topic-maker" / "src"
        if sibling_source.is_dir() and str(sibling_source) not in sys.path:
            sys.path.insert(0, str(sibling_source))
        try:
            from wiki_from_topic_maker.credibility_v2 import (  # type: ignore[import-not-found,no-redef]
                BrowserJob,
                BrowserJobPolicy,
                BrowserJobPurpose,
                BrowserOutcome,
                BrowserReceipt,
                validate_receipt_for_job,
            )
        except ModuleNotFoundError:
            return None
    return (
        BrowserJob,
        BrowserJobPolicy,
        BrowserJobPurpose,
        BrowserOutcome,
        BrowserReceipt,
        validate_receipt_for_job,
    )


MAKER_CONTRACTS = _import_maker_browser_contracts()


@dataclass(frozen=True)
class AuditCandidate:
    requested_url: str
    pages: tuple[str, ...]
    finding_kinds: tuple[str, ...]
    severities: tuple[str, ...]


@dataclass(frozen=True)
class RobotsDecision:
    allowed: bool
    reason_code: str
    robots_url: str
    content_sha256: str | None = None


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_time(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, separators=(",", ":"), sort_keys=True)


def host_matches(host: str, domains: Iterable[str]) -> bool:
    return any(host == domain or host.endswith(f".{domain}") for domain in domains)


def normalize_origin(value: str) -> str:
    """Return one exact public HTTPS origin or raise ``ValueError``."""

    parts = urlsplit(value.strip())
    if parts.scheme.casefold() != "https" or not parts.hostname:
        raise ValueError("origin must be an absolute HTTPS URL")
    if parts.username or parts.password:
        raise ValueError("credentials are forbidden in browser origins")
    if parts.path not in ("", "/") or parts.query or parts.fragment:
        raise ValueError("allowlisted origins cannot contain a path, query, or fragment")
    try:
        port = parts.port
    except ValueError as exc:
        raise ValueError("origin port is invalid") from exc
    if port not in (None, 443):
        raise ValueError("only the standard HTTPS port is allowed")
    host = parts.hostname.casefold().rstrip(".")
    validate_public_hostname(host)
    return urlunsplit(("https", host, "", "", ""))


def origin_for_url(value: str) -> str:
    parts = urlsplit(value.strip())
    if parts.scheme.casefold() != "https" or not parts.hostname:
        raise ValueError("browser URL must be absolute HTTPS")
    if parts.username or parts.password:
        raise ValueError("credentials are forbidden in browser URLs")
    try:
        port = parts.port
    except ValueError as exc:
        raise ValueError("browser URL port is invalid") from exc
    if port not in (None, 443):
        raise ValueError("only the standard HTTPS port is allowed")
    host = parts.hostname.casefold().rstrip(".")
    validate_public_hostname(host)
    return urlunsplit(("https", host, "", "", ""))


def validate_public_hostname(host: str) -> None:
    if not host or "." not in host or host == "localhost":
        raise ValueError("browser hostname must be a public DNS name")
    if host.endswith(DISALLOWED_HOST_SUFFIXES):
        raise ValueError("browser hostname uses a non-public suffix")
    try:
        ipaddress.ip_address(host.strip("[]"))
    except ValueError:
        pass
    else:
        raise ValueError("literal IP browser targets are forbidden")
    try:
        encoded = host.encode("idna").decode("ascii")
    except UnicodeError as exc:
        raise ValueError("browser hostname is not valid IDNA") from exc
    if len(encoded) > 253 or any(not label or len(label) > 63 for label in encoded.split(".")):
        raise ValueError("browser hostname is invalid")


def validate_exact_origin(value: str, allowed_origins: Sequence[str]) -> bool:
    try:
        return origin_for_url(value) in allowed_origins
    except ValueError:
        return False


def classify_surface(url: str) -> str | None:
    """Return a terminal preflight reason for surfaces Chrome must not read."""

    try:
        origin_for_url(url)
    except ValueError:
        return "invalid_or_nonpublic_https_url"
    parts = urlsplit(url)
    host = (parts.hostname or "").casefold().rstrip(".")
    if host_matches(host, SOCIAL_OR_AUTH_HOSTS):
        return "social_or_auth_surface_refused"
    if host_matches(host, API_OR_STATIC_PREFERRED_HOSTS):
        return "api_or_static_provider_preferred"
    if host_matches(host, {"youtube.com", "youtu.be", "googlevideo.com"}):
        return "youtube_browser_automation_refused"
    if AUTH_PATH_RE.search(parts.path):
        return "login_path_refused"
    return None


def resolved_addresses_are_public(addresses: Iterable[str]) -> bool:
    values = tuple(addresses)
    if not values:
        return False
    try:
        parsed = tuple(ipaddress.ip_address(value) for value in values)
    except ValueError:
        return False
    return all(address.is_global for address in parsed)


def resolve_public_host(host: str) -> tuple[bool, str]:
    try:
        results = socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)
    except OSError:
        return False, "dns_resolution_failed"
    addresses = sorted({str(result[4][0]) for result in results})
    if not resolved_addresses_are_public(addresses):
        return False, "dns_resolved_nonpublic_address"
    return True, "dns_public_address_verified"


def load_audit_candidates(path: Path) -> list[AuditCandidate]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    findings = payload.get("findings", []) if isinstance(payload, dict) else []
    by_url: dict[str, dict[str, Any]] = {}
    for finding in findings:
        if not isinstance(finding, dict) or finding.get("kind") not in TARGET_FINDING_KINDS:
            continue
        url = str(finding.get("url") or "").strip()
        if not url:
            continue
        key = url.casefold()
        row = by_url.setdefault(
            key,
            {"url": url, "pages": set(), "finding_kinds": set(), "severities": set()},
        )
        page = str(finding.get("page") or "").strip()
        if page:
            row["pages"].add(page)
        row["finding_kinds"].add(str(finding["kind"]))
        severity = str(finding.get("severity") or "unknown").casefold()
        row["severities"].add(severity)
    candidates = [
        AuditCandidate(
            requested_url=row["url"],
            pages=tuple(sorted(row["pages"])),
            finding_kinds=tuple(
                sorted(
                    row["finding_kinds"],
                    key=lambda kind: (FINDING_KIND_ORDER.get(kind, 999), kind),
                )
            ),
            severities=tuple(
                sorted(
                    row["severities"],
                    key=lambda severity: (SEVERITY_ORDER.get(severity, 999), severity),
                )
            ),
        )
        for row in by_url.values()
    ]
    return sorted(
        candidates,
        key=lambda candidate: (
            min(SEVERITY_ORDER.get(value, 999) for value in candidate.severities),
            min(FINDING_KIND_ORDER.get(value, 999) for value in candidate.finding_kinds),
            candidate.requested_url.casefold(),
        ),
    )


def bounded_text_fingerprint(value: str) -> dict[str, Any]:
    """Fingerprint visible text without retaining the page's raw body text."""

    bounded = re.sub(r"\s+", " ", value).strip()[:MAX_VISIBLE_TEXT]
    tokens = sorted(set(token.casefold() for token in TOKEN_RE.findall(bounded)))
    token_hashes = sorted(
        hashlib.blake2b(token.encode("utf-8"), digest_size=6).hexdigest()
        for token in tokens
    )[:32]
    return {
        "boundedCharacters": len(bounded),
        "sha256": hashlib.sha256(bounded.encode("utf-8")).hexdigest(),
        "tokenHashes": token_hashes,
        "truncated": len(re.sub(r"\s+", " ", value).strip()) > MAX_VISIBLE_TEXT,
    }


def clean_metadata_text(value: Any, limit: int) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()[:limit]


def classify_extraction(data: dict[str, Any]) -> tuple[str, str]:
    if bool(data.get("challengeDetected")):
        return "challenge", "challenge_surface_detected"
    if bool(data.get("loginDetected")):
        return "login_required", "login_surface_detected"
    if bool(data.get("rateLimited")):
        return "rate_limited", "rate_limit_surface_detected"
    visible = " ".join(
        clean_metadata_text(data.get(key), 500)
        for key in ("title", "description", "siteName", "h1", "bodyText")
    ).strip()
    if not visible:
        return "content_unavailable", "empty_public_page_metadata"
    return "browser_success", "public_owner_metadata_extracted"


def sanitize_extraction(data: dict[str, Any], allowed_origins: Sequence[str]) -> dict[str, Any]:
    final_url = clean_metadata_text(data.get("finalUrl"), 2_048)
    canonical_url = clean_metadata_text(data.get("canonicalUrl"), 2_048)
    return {
        "finalUrl": final_url,
        "finalUrlExactOrigin": validate_exact_origin(final_url, allowed_origins),
        "title": clean_metadata_text(data.get("title"), 300),
        "canonicalUrl": canonical_url,
        "canonicalExactOrigin": bool(canonical_url)
        and validate_exact_origin(canonical_url, allowed_origins),
        "description": clean_metadata_text(data.get("description"), 600),
        "siteName": clean_metadata_text(data.get("siteName"), 200),
        "h1": clean_metadata_text(data.get("h1"), 300),
        "visibleTextFingerprint": bounded_text_fingerprint(str(data.get("bodyText") or "")),
    }


def robots_allows(robots_text: str, target_url: str) -> bool:
    parser = urllib.robotparser.RobotFileParser()
    parser.set_url(urljoin(origin_for_url(target_url) + "/", "robots.txt"))
    parser.parse(robots_text.splitlines())
    return parser.can_fetch(USER_AGENT, target_url)


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001, ANN201
        return None


def fetch_robots(target_url: str, timeout_seconds: int = 10) -> RobotsDecision:
    origin = origin_for_url(target_url)
    robots_url = origin + "/robots.txt"
    request = urllib.request.Request(robots_url, headers={"User-Agent": USER_AGENT})
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), _NoRedirect())
    try:
        with opener.open(request, timeout=timeout_seconds) as response:
            status = int(response.status)
            body = response.read(MAX_ROBOTS_BYTES + 1)
    except urllib.error.HTTPError as exc:
        if exc.code in (404, 410):
            return RobotsDecision(True, "robots_not_published", robots_url)
        if exc.code in (401, 403):
            return RobotsDecision(False, "robots_access_forbidden", robots_url)
        if exc.code == 429:
            return RobotsDecision(False, "robots_rate_limited", robots_url)
        if 300 <= exc.code < 400:
            return RobotsDecision(False, "robots_redirect_refused", robots_url)
        return RobotsDecision(False, "robots_unavailable", robots_url)
    except (OSError, TimeoutError):
        return RobotsDecision(False, "robots_unavailable", robots_url)
    if status != 200 or len(body) > MAX_ROBOTS_BYTES:
        return RobotsDecision(False, "robots_unavailable", robots_url)
    text = body.decode("utf-8", errors="replace")
    digest = hashlib.sha256(body).hexdigest()
    if not robots_allows(text, target_url):
        return RobotsDecision(False, "robots_disallow", robots_url, digest)
    return RobotsDecision(True, "robots_allow", robots_url, digest)


def make_browser_job(url: str, limit: int) -> Any | None:
    if MAKER_CONTRACTS is None:
        return None
    BrowserJob, BrowserJobPolicy, BrowserJobPurpose, _, _, _ = MAKER_CONTRACTS
    host = (urlsplit(url).hostname or "").casefold().rstrip(".")
    policy = BrowserJobPolicy(
        allowed_domains=(host,),
        max_jobs_per_run=limit,
        max_navigations_per_job=1,
        timeout_seconds=120,
        max_transient_retries=0,
        concurrency_per_domain=1,
        ephemeral_profile=True,
        allow_login=False,
        allow_form_submission=False,
        allow_downloads=False,
        allow_challenge_solving=False,
    )
    return BrowserJob.create(
        url=url,
        purpose=BrowserJobPurpose.PUBLIC_METADATA_EXTRACTION,
        extractor_version=EXTRACTOR_VERSION,
        policy=policy,
    )


EXTRACT_JS = r"""
() => {
  const norm = (value, limit) => String(value || '').replace(/\s+/g, ' ').trim().slice(0, limit);
  const meta = (...selectors) => {
    for (const selector of selectors) {
      const node = document.querySelector(selector);
      if (node && node.content) return norm(node.content, 600);
    }
    return '';
  };
  const title = norm(document.title, 300);
  const h1 = norm(document.querySelector('h1')?.innerText, 300);
  const bodyText = norm(document.body?.innerText, 8000);
  const surface = `${title} ${h1} ${bodyText.slice(0, 2400)}`.toLowerCase();
  const passwordField = Boolean(document.querySelector('input[type="password"]'));
  const loginHeading = /^(sign in|log in|login|authentication required)$/i.test(h1);
  const challengeDetected = /verify you are human|checking your browser|captcha|challenge-platform|cf-chl-/i.test(surface);
  const rateLimited = /too many requests|rate limit exceeded|temporarily rate limited/i.test(surface);
  return JSON.stringify({
    finalUrl: location.href,
    title,
    canonicalUrl: norm(document.querySelector('link[rel="canonical"]')?.href, 2048),
    description: meta('meta[name="description"]', 'meta[property="og:description"]'),
    siteName: meta('meta[property="og:site_name"]'),
    h1,
    bodyText,
    loginDetected: passwordField || loginHeading,
    challengeDetected,
    rateLimited
  });
}
"""


async def browser_extract(job: Any) -> tuple[dict[str, Any] | None, str | None]:
    try:
        from browser_use.browser import BrowserSession  # type: ignore[import-not-found]
    except ModuleNotFoundError:
        return None, "browser_runtime_unavailable"

    host = (urlsplit(job.url).hostname or "").casefold().rstrip(".")
    browser = BrowserSession(
        headless=True,
        allowed_domains=[host],
        prohibited_domains=list(sorted(SOCIAL_OR_AUTH_HOSTS)),
        accept_downloads=False,
        auto_download_pdfs=False,
        permissions=[],
        user_agent=USER_AGENT,
        keep_alive=False,
        enable_default_extensions=False,
        captcha_solver=False,
        wait_for_network_idle_page_load_time=2,
        minimum_wait_page_load_time=1,
        viewport={"width": 1280, "height": 900},
    )
    try:
        await browser.start()
        await browser.navigate_to(job.url)
        page = await browser.get_current_page()
        if page is None:
            return None, "browser_page_unavailable"
        raw = await page.evaluate(EXTRACT_JS)
        value = json.loads(raw) if isinstance(raw, str) else raw
        if not isinstance(value, dict):
            return None, "browser_extractor_contract_mismatch"
        return value, None
    except Exception:  # Browser/runtime errors are reduced to a private reason code.
        return None, "browser_navigation_failed"
    finally:
        try:
            await browser.stop()
        except Exception:
            pass


def base_record(candidate: AuditCandidate, *, job: Any | None, started_at: datetime) -> dict[str, Any]:
    candidate_id = hashlib.sha256(candidate.requested_url.encode("utf-8")).hexdigest()
    return {
        "candidateId": candidate_id,
        "jobId": job.job_id if job is not None else None,
        "requestedUrl": candidate.requested_url,
        "findingKinds": list(candidate.finding_kinds),
        "severities": list(candidate.severities),
        "pages": list(candidate.pages),
        "startedAt": iso_time(started_at),
    }


def terminal_record(
    candidate: AuditCandidate,
    *,
    reason_code: str,
    outcome: str,
    job: Any | None = None,
    started_at: datetime | None = None,
    robots: RobotsDecision | None = None,
) -> dict[str, Any]:
    started = started_at or utc_now()
    finished = utc_now()
    record = base_record(candidate, job=job, started_at=started)
    record.update(
        {
            "finishedAt": iso_time(finished),
            "outcome": outcome,
            "reasonCode": reason_code,
        }
    )
    if robots:
        record["robots"] = {
            "url": robots.robots_url,
            "reasonCode": robots.reason_code,
            "contentSha256": robots.content_sha256,
        }
    if job is not None:
        record["makerReceipt"] = maker_receipt(
            job,
            outcome_name=outcome,
            started_at=started,
            finished_at=finished,
        )
    return record


def build_dry_run_records(
    candidates: Sequence[AuditCandidate],
    *,
    allowed_origins: Sequence[str],
    limit: int,
    offset: int = 0,
) -> list[dict[str, Any]]:
    records = []
    selected, _ = select_candidate_slice(candidates, offset=offset, limit=limit)
    for candidate in selected:
        reason = classify_surface(candidate.requested_url)
        try:
            origin = origin_for_url(candidate.requested_url)
        except ValueError:
            origin = None
        if reason:
            state = reason
        elif origin not in allowed_origins:
            state = "exact_origin_allowlist_required"
        elif MAKER_CONTRACTS is None:
            state = "maker_browser_contract_unavailable"
        else:
            state = "eligible_for_robots_preflight"
        records.append(
            {
                "candidateId": hashlib.sha256(
                    candidate.requested_url.encode("utf-8")
                ).hexdigest(),
                "requestedUrl": candidate.requested_url,
                "exactOrigin": origin,
                "findingKinds": list(candidate.finding_kinds),
                "severities": list(candidate.severities),
                "pages": list(candidate.pages),
                "planState": state,
            }
        )
    return records


def select_candidate_slice(
    candidates: Sequence[AuditCandidate],
    *,
    offset: int,
    limit: int,
) -> tuple[list[AuditCandidate], dict[str, int]]:
    """Select one deterministic half-open candidate range."""

    if offset < 0:
        raise ValueError("offset must be nonnegative")
    if not 1 <= limit <= MAX_JOBS:
        raise ValueError(f"limit must be between 1 and {MAX_JOBS}")
    total = len(candidates)
    start = min(offset, total)
    end = min(offset + limit, total)
    return list(candidates[start:end]), {
        "startOffset": start,
        "endOffsetExclusive": end,
    }


def maker_receipt(
    job: Any,
    *,
    outcome_name: str,
    started_at: datetime,
    finished_at: datetime,
    final_url: str | None = None,
    content_sha256: str | None = None,
) -> dict[str, Any] | None:
    if MAKER_CONTRACTS is None:
        return None
    _, _, _, BrowserOutcome, BrowserReceipt, validate_receipt_for_job = MAKER_CONTRACTS
    outcome = BrowserOutcome(outcome_name)
    receipt = BrowserReceipt(
        job_id=job.job_id,
        outcome=outcome,
        started_at=started_at,
        finished_at=finished_at,
        final_url=final_url,
        content_sha256=content_sha256,
        selector_contract_version=SELECTOR_CONTRACT_VERSION,
        challenge_detected=outcome_name == "challenge",
        attempt=1,
    )
    validate_receipt_for_job(job, receipt)
    return receipt.as_dict()


async def run_candidate(
    candidate: AuditCandidate,
    *,
    allowed_origins: Sequence[str],
    limit: int,
) -> dict[str, Any]:
    started = utc_now()
    reason = classify_surface(candidate.requested_url)
    if reason:
        return terminal_record(
            candidate,
            reason_code=reason,
            outcome="blocked_by_policy",
            started_at=started,
        )
    origin = origin_for_url(candidate.requested_url)
    if origin not in allowed_origins:
        return terminal_record(
            candidate,
            reason_code="exact_origin_allowlist_required",
            outcome="blocked_by_policy",
            started_at=started,
        )
    job = make_browser_job(candidate.requested_url, limit)
    if job is None:
        return terminal_record(
            candidate,
            reason_code="maker_browser_contract_unavailable",
            outcome="blocked_by_policy",
            started_at=started,
        )
    host = (urlsplit(candidate.requested_url).hostname or "").casefold().rstrip(".")
    dns_allowed, dns_reason = resolve_public_host(host)
    if not dns_allowed:
        return terminal_record(
            candidate,
            reason_code=dns_reason,
            outcome="blocked_by_policy",
            job=job,
            started_at=started,
        )
    robots = fetch_robots(candidate.requested_url)
    if not robots.allowed:
        if robots.reason_code == "robots_disallow":
            outcome = "robots_disallow"
        elif robots.reason_code == "robots_rate_limited":
            outcome = "rate_limited"
        else:
            outcome = "terms_unknown"
        return terminal_record(
            candidate,
            reason_code=robots.reason_code,
            outcome=outcome,
            job=job,
            started_at=started,
            robots=robots,
        )
    try:
        data, runtime_error = await asyncio.wait_for(browser_extract(job), timeout=120)
    except asyncio.TimeoutError:
        data, runtime_error = None, "browser_timeout"
    if runtime_error or data is None:
        return terminal_record(
            candidate,
            reason_code=runtime_error or "browser_runtime_unavailable",
            outcome="transient_error",
            job=job,
            started_at=started,
            robots=robots,
        )
    outcome_name, reason_code = classify_extraction(data)
    extraction = sanitize_extraction(data, allowed_origins)
    if not extraction["finalUrlExactOrigin"]:
        return terminal_record(
            candidate,
            reason_code="cross_origin_redirect_refused",
            outcome="blocked_by_policy",
            job=job,
            started_at=started,
            robots=robots,
        )
    finished = utc_now()
    content_sha256 = None
    if outcome_name == "browser_success":
        content_sha256 = hashlib.sha256(canonical_json(extraction).encode("utf-8")).hexdigest()
    receipt = maker_receipt(
        job,
        outcome_name=outcome_name,
        started_at=started,
        finished_at=finished,
        final_url=extraction["finalUrl"],
        content_sha256=content_sha256,
    )
    record = base_record(candidate, job=job, started_at=started)
    record.update(
        {
            "finishedAt": iso_time(finished),
            "outcome": outcome_name,
            "reasonCode": reason_code,
            "dnsReasonCode": dns_reason,
            "robots": {
                "url": robots.robots_url,
                "reasonCode": robots.reason_code,
                "contentSha256": robots.content_sha256,
            },
            "extraction": extraction,
            "makerReceipt": receipt,
        }
    )
    return record


def require_private_output(path: Path, project_root: Path = ROOT) -> Path:
    private_root = (
        project_root
        / ".ops"
        / "state"
        / "cache"
        / "wiki-maker"
        / "credibility-v2"
        / "browser"
    ).resolve()
    resolved = path.resolve()
    if not resolved.is_relative_to(private_root):
        raise ValueError("browser receipts must remain under private credibility-v2 state")
    return resolved


def write_private_run(payload: dict[str, Any], *, now: datetime | None = None) -> Path:
    generated = now or utc_now()
    stamp = generated.strftime("%Y%m%dT%H%M%S%fZ")
    PRIVATE_OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    destination = require_private_output(PRIVATE_OUTPUT_ROOT / f"run-{stamp}.json")
    rendered = json.dumps(payload, ensure_ascii=True, indent=2, sort_keys=True) + "\n"
    temporary = destination.with_suffix(".tmp")
    temporary.write_text(rendered, encoding="utf-8")
    temporary.replace(destination)
    latest = require_private_output(PRIVATE_OUTPUT_ROOT / "latest.json")
    latest_tmp = latest.with_suffix(".tmp")
    latest_tmp.write_text(rendered, encoding="utf-8")
    latest_tmp.replace(latest)
    return destination


def strict_limit(value: str) -> int:
    try:
        parsed = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("limit must be an integer") from exc
    if not 1 <= parsed <= MAX_JOBS:
        raise argparse.ArgumentTypeError(f"limit must be between 1 and {MAX_JOBS}")
    return parsed


def strict_offset(value: str) -> int:
    try:
        parsed = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("offset must be an integer") from exc
    if parsed < 0:
        raise argparse.ArgumentTypeError("offset must be nonnegative")
    return parsed


def parse_allowed_origins(values: Sequence[str]) -> tuple[str, ...]:
    return tuple(sorted({normalize_origin(value) for value in values}))


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(
        description=(
            "Privately validate unresolved owner-site metadata with bounded Chrome-agent checks. "
            "API/static providers remain preferred."
        )
    )
    value.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    value.add_argument("--limit", type=strict_limit, default=10)
    value.add_argument("--offset", type=strict_offset, default=0)
    value.add_argument("--dry-run", action="store_true")
    value.add_argument(
        "--allow-origin",
        action="append",
        default=[],
        metavar="HTTPS_ORIGIN",
        help=(
            "Exact origin approved for a metadata-only check after applicable terms review; "
            "repeat for each origin."
        ),
    )
    return value


async def async_main(args: argparse.Namespace) -> tuple[dict[str, Any], Path | None]:
    input_path = args.input.resolve()
    candidates = load_audit_candidates(input_path)
    allowed_origins = parse_allowed_origins(args.allow_origin)
    generated = utc_now()
    selected_candidates, selected_range = select_candidate_slice(
        candidates,
        offset=args.offset,
        limit=args.limit,
    )
    common = {
        "schemaVersion": 1,
        "visibility": "internal-only",
        "generatedAt": iso_time(generated),
        "browserRole": "last-mile owner metadata validation after API/static checks",
        "input": str(input_path),
        "limit": args.limit,
        "offset": args.offset,
        "selectedRange": selected_range,
        "candidateCount": len(candidates),
        "targetFindingKinds": list(TARGET_FINDING_KINDS),
    }
    if args.dry_run:
        common.update(
            {
                "mode": "dry-run",
                "writesPerformed": False,
                "records": build_dry_run_records(
                    candidates,
                    allowed_origins=allowed_origins,
                    limit=args.limit,
                    offset=args.offset,
                ),
            }
        )
        return common, None

    records = []
    for candidate in selected_candidates:
        records.append(
            await run_candidate(
                candidate,
                allowed_origins=allowed_origins,
                limit=args.limit,
            )
        )
    common.update(
        {
            "mode": "live",
            "writesPerformed": True,
            "records": records,
        }
    )
    destination = write_private_run(common, now=generated)
    return common, destination


def main() -> int:
    args = parser().parse_args()
    payload, destination = asyncio.run(async_main(args))
    summary = {
        "mode": payload["mode"],
        "candidateCount": payload["candidateCount"],
        "offset": payload["offset"],
        "selectedRange": payload["selectedRange"],
        "selectedCount": len(payload["records"]),
        "output": str(destination) if destination else None,
        "records": payload["records"] if args.dry_run else None,
    }
    print(json.dumps(summary, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
