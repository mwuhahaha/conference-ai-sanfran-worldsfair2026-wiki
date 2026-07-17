import importlib.util
import json
import sys
from argparse import ArgumentTypeError
from pathlib import Path

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "run_credibility_browser_checks.py"
SPEC = importlib.util.spec_from_file_location("run_credibility_browser_checks_test", SCRIPT)
CHECKS = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = CHECKS
SPEC.loader.exec_module(CHECKS)


def write_audit(path: Path) -> None:
    path.write_text(
        json.dumps(
            {
                "findings": [
                    {
                        "kind": "company_site_attached_without_successful_validation",
                        "page": "wiki/companies/zeta.md",
                        "severity": "medium",
                        "url": "https://zeta.example.org/about",
                    },
                    {
                        "kind": "company_site_attached_without_successful_validation",
                        "page": "wiki/companies/alpha.md",
                        "severity": "medium",
                        "url": "https://alpha.example.org/",
                    },
                    {
                        "kind": "company_site_attached_without_successful_validation",
                        "page": "wiki/companies/alpha-duplicate.md",
                        "severity": "medium",
                        "url": "https://alpha.example.org/",
                    },
                    {
                        "kind": "domain_guess_without_company_name_corroboration",
                        "page": "wiki/companies/beta.md",
                        "severity": "medium",
                        "url": "https://beta.example.org/",
                    },
                    {
                        "kind": "company_site_attached_without_successful_validation",
                        "page": "wiki/companies/urgent.md",
                        "severity": "high",
                        "url": "https://urgent.example.org/",
                    },
                    {
                        "kind": "malformed_external_url",
                        "page": "wiki/companies/ignored.md",
                        "url": "https://ignored.example.org/",
                    },
                ]
            }
        ),
        encoding="utf-8",
    )


def test_audit_candidates_are_filtered_deduplicated_and_sorted(tmp_path: Path) -> None:
    audit = tmp_path / "audit.json"
    write_audit(audit)

    candidates = CHECKS.load_audit_candidates(audit)

    assert [candidate.requested_url for candidate in candidates] == [
        "https://urgent.example.org/",
        "https://beta.example.org/",
        "https://alpha.example.org/",
        "https://zeta.example.org/about",
    ]
    assert candidates[2].pages == (
        "wiki/companies/alpha-duplicate.md",
        "wiki/companies/alpha.md",
    )
    assert candidates[1].finding_kinds == (
        "domain_guess_without_company_name_corroboration",
    )


@pytest.mark.parametrize(
    ("value", "message"),
    [
        ("http://owner.example.org", "HTTPS"),
        ("https://user:secret@owner.example.org", "credentials"),
        ("https://localhost", "public DNS"),
        ("https://127.0.0.1", "literal IP"),
        ("https://owner.example.org:8443", "standard HTTPS"),
        ("https://owner.example.org/path", "cannot contain"),
    ],
)
def test_exact_origin_rejects_unsafe_values(value: str, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        CHECKS.normalize_origin(value)


def test_exact_origin_does_not_treat_www_as_equivalent() -> None:
    allowed = (CHECKS.normalize_origin("https://owner.example.org"),)

    assert CHECKS.validate_exact_origin("https://owner.example.org/about", allowed)
    assert not CHECKS.validate_exact_origin("https://www.owner.example.org/about", allowed)


@pytest.mark.parametrize(
    ("url", "reason"),
    [
        ("https://www.linkedin.com/company/example", "social_or_auth_surface_refused"),
        ("https://github.com/example/project", "api_or_static_provider_preferred"),
        ("https://owner.example.org/login", "login_path_refused"),
        ("https://www.youtube.com/watch?v=abc", "youtube_browser_automation_refused"),
    ],
)
def test_surfaces_with_better_or_forbidden_paths_are_refused(url: str, reason: str) -> None:
    assert CHECKS.classify_surface(url) == reason


def test_robots_parser_honors_path_rules() -> None:
    robots = "User-agent: *\nDisallow: /private\nAllow: /public\n"

    assert CHECKS.robots_allows(robots, "https://owner.example.org/public/about")
    assert not CHECKS.robots_allows(robots, "https://owner.example.org/private/about")


def test_visible_text_fingerprint_is_deterministic_and_does_not_retain_raw_text() -> None:
    text = "Secret-looking public page sentence about Example Company and agents."

    first = CHECKS.bounded_text_fingerprint(text)
    second = CHECKS.bounded_text_fingerprint(text)

    assert first == second
    assert "Secret-looking" not in json.dumps(first)
    assert len(first["sha256"]) == 64
    assert all(len(value) == 12 for value in first["tokenHashes"])


@pytest.mark.parametrize(
    ("data", "outcome", "reason"),
    [
        (
            {"challengeDetected": True},
            "challenge",
            "challenge_surface_detected",
        ),
        (
            {"loginDetected": True},
            "login_required",
            "login_surface_detected",
        ),
        (
            {"rateLimited": True},
            "rate_limited",
            "rate_limit_surface_detected",
        ),
        ({}, "content_unavailable", "empty_public_page_metadata"),
        (
            {"title": "Example Company"},
            "browser_success",
            "public_owner_metadata_extracted",
        ),
    ],
)
def test_extraction_outcomes_are_explicit(data: dict, outcome: str, reason: str) -> None:
    assert CHECKS.classify_extraction(data) == (outcome, reason)


def test_dry_run_is_bounded_and_requires_explicit_origin_allowlist(tmp_path: Path) -> None:
    audit = tmp_path / "audit.json"
    write_audit(audit)
    candidates = CHECKS.load_audit_candidates(audit)

    records = CHECKS.build_dry_run_records(candidates, allowed_origins=(), limit=1)

    assert len(records) == 1
    assert records[0]["planState"] == "exact_origin_allowlist_required"


def test_candidate_slice_is_deterministic_and_reports_effective_range(tmp_path: Path) -> None:
    audit = tmp_path / "audit.json"
    write_audit(audit)
    candidates = CHECKS.load_audit_candidates(audit)

    selected, selected_range = CHECKS.select_candidate_slice(
        candidates,
        offset=1,
        limit=2,
    )
    dry_records = CHECKS.build_dry_run_records(
        candidates,
        allowed_origins=(),
        offset=1,
        limit=2,
    )

    assert [candidate.requested_url for candidate in selected] == [
        "https://beta.example.org/",
        "https://alpha.example.org/",
    ]
    assert selected_range == {"startOffset": 1, "endOffsetExclusive": 3}
    assert [record["requestedUrl"] for record in dry_records] == [
        candidate.requested_url for candidate in selected
    ]


def test_candidate_slice_past_end_is_empty_and_bounded(tmp_path: Path) -> None:
    audit = tmp_path / "audit.json"
    write_audit(audit)
    candidates = CHECKS.load_audit_candidates(audit)

    selected, selected_range = CHECKS.select_candidate_slice(
        candidates,
        offset=100,
        limit=20,
    )

    assert selected == []
    assert selected_range == {"startOffset": 4, "endOffsetExclusive": 4}


def test_maker_browser_job_uses_locked_down_policy() -> None:
    job = CHECKS.make_browser_job("https://owner.example.org/about", limit=3)

    assert job is not None
    assert job.policy.max_jobs_per_run == 3
    assert job.policy.max_navigations_per_job == 1
    assert job.policy.ephemeral_profile is True
    assert job.policy.allow_login is False
    assert job.policy.allow_form_submission is False
    assert job.policy.allow_downloads is False
    assert job.policy.allow_challenge_solving is False


def test_terminal_browser_job_result_includes_reusable_maker_receipt() -> None:
    candidate = CHECKS.AuditCandidate(
        requested_url="https://owner.example.org/about",
        pages=("wiki/companies/owner.md",),
        finding_kinds=("company_site_attached_without_successful_validation",),
        severities=("medium",),
    )
    job = CHECKS.make_browser_job(candidate.requested_url, limit=1)

    record = CHECKS.terminal_record(
        candidate,
        reason_code="robots_disallow",
        outcome="robots_disallow",
        job=job,
    )

    assert record["makerReceipt"]["job_id"] == job.job_id
    assert record["makerReceipt"]["outcome"] == "robots_disallow"


def test_receipt_path_cannot_escape_private_state(tmp_path: Path) -> None:
    private = (
        tmp_path / ".ops/state/cache/wiki-maker/credibility-v2/browser/run.json"
    )
    public = tmp_path / "wiki/resources/browser-run.json"

    assert CHECKS.require_private_output(private, tmp_path) == private.resolve()
    with pytest.raises(ValueError, match="private"):
        CHECKS.require_private_output(public, tmp_path)


@pytest.mark.parametrize("value", ["0", "21", "-1", "many"])
def test_limit_is_strict(value: str) -> None:
    with pytest.raises(ArgumentTypeError):
        CHECKS.strict_limit(value)


@pytest.mark.parametrize("value", ["-1", "many", "1.5"])
def test_offset_is_strictly_nonnegative(value: str) -> None:
    with pytest.raises(ArgumentTypeError):
        CHECKS.strict_offset(value)


@pytest.mark.parametrize(("value", "expected"), [("0", 0), ("20", 20), ("38", 38)])
def test_offset_accepts_nonnegative_integers(value: str, expected: int) -> None:
    assert CHECKS.strict_offset(value) == expected
