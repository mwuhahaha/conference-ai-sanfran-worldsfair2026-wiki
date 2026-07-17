import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "enrich_company_pages.py"
if str(SCRIPT.parent) not in sys.path:
    sys.path.insert(0, str(SCRIPT.parent))
SPEC = importlib.util.spec_from_file_location("enrich_company_pages_test", SCRIPT)
COMPANIES = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(COMPANIES)


def company_page(profile: dict) -> dict:
    return {
        "title": "Example Co",
        "aliases": [],
        "people": [],
        "sessions": [],
        "profile": profile,
    }


def test_held_profile_cannot_reach_company_article() -> None:
    profile = {
        "website": "https://wrong.example/",
        "summary": "Unrelated same-name business.",
        "sourceLinks": [
            {"label": "Wrong business", "url": "https://wrong.example/"}
        ],
    }

    safe = COMPANIES.publishable_profile(
        profile,
        {"writingDisposition": "omit"},
    )
    rendered = COMPANIES.render_company_page(
        "example-co",
        company_page(safe),
    )

    assert safe == {}
    assert "wrong.example" not in rendered
    assert "Unrelated same-name business" not in rendered
    assert "without a validated identity path" in rendered


def test_owner_profile_is_attributed_after_identity_gate() -> None:
    profile = {
        "website": "https://example.com/",
        "summary": "Example Co states that it builds clinical documentation tools.",
        "sourceLinks": [
            {"label": "Example Co", "url": "https://example.com/"}
        ],
        "sourceLabels": ["Public company site"],
    }

    safe = COMPANIES.publishable_profile(
        profile,
        {"writingDisposition": "attribute_to_source"},
    )
    rendered = COMPANIES.render_company_page(
        "example-co",
        company_page(safe),
    )

    assert "https://example.com/" in rendered
    assert "attributed owner context" in rendered
    assert "not independent validation or endorsement" in rendered


def test_publishable_profile_is_an_allowlisted_public_projection() -> None:
    profile = {
        "website": "https://example.com/",
        "summary": (
            "Example Co states that it builds clinical documentation tools. "
            "The public company site was fetched for homepage metadata."
        ),
        "origin": (
            "The official speaker roster connects Example Co to Example Person. "
            "The public company site was discovered by domain-guess and fetched "
            "for homepage metadata."
        ),
        "why_it_matters": (
            "Example Co has one official speaker and one scheduled session."
        ),
        "sourceLabels": [
            "Official speaker roster",
            "Public company site",
            "Automated company profile fetch",
            "Automated discovery",
            "Company profile candidate",
            "Manual company URL override",
        ],
        "sourceLinks": [
            {
                "label": "Example Co",
                "url": "https://example.com/",
                "validationStatus": "accepted",
                "candidateScore": 99,
            },
            {
                "label": "Company profile candidate",
                "url": "https://example.com/about",
            },
            {"label": "Unsafe", "url": "http://example.com/unsafe"},
        ],
        "notes": ["Automated company profile fetch status: fetched."],
        "fetchStatus": "fetched",
        "fetchedMetadata": {"title": "Example Co"},
        "validation": {"status": "accepted"},
        "originMethod": "domain-guess",
        "privateDecision": {"writingDisposition": "attribute_to_source"},
    }

    safe = COMPANIES.publishable_profile(
        profile,
        {"writingDisposition": "attribute_to_source"},
    )
    rendered = COMPANIES.render_company_page(
        "example-co",
        company_page(safe),
    )

    assert set(safe) == {
        "website",
        "summary",
        "origin",
        "why_it_matters",
        "sourceLabels",
        "sourceLinks",
    }
    assert safe["summary"] == (
        "Example Co states that it builds clinical documentation tools."
    )
    assert safe["origin"] == (
        "The official speaker roster connects Example Co to Example Person."
    )
    assert safe["sourceLabels"] == [
        "Official speaker roster",
        "Public company site",
    ]
    assert safe["sourceLinks"] == [
        {"label": "Example Co", "url": "https://example.com/"},
        {"url": "https://example.com/about"},
    ]
    assert profile["fetchStatus"] == "fetched"
    assert "clinical documentation tools" in rendered
    assert "official speaker roster connects" in rendered
    assert "domain-guess" not in rendered
    assert "Automated company profile fetch" not in rendered
    assert "Manual company URL override" not in rendered
    assert "fetchStatus" not in rendered
    assert "candidateScore" not in rendered


def test_manual_override_origin_keeps_separate_official_roster_context() -> None:
    safe = COMPANIES.publishable_profile(
        {
            "summary": "Example Co builds owner-described workflow tools.",
            "origin": (
                "The official speaker roster connects Example Co to Example Person. "
                "The public source was attached through a manual URL override "
                "because the fetched homepage metadata was incomplete."
            ),
            "sourceLabels": [
                "Official conference schedule",
                "Manual company URL override",
                "Public company site",
            ],
            "notes": ["Keep this private acquisition note."],
        },
        {"writingDisposition": "assert_with_citations"},
    )

    assert safe == {
        "summary": "Example Co builds owner-described workflow tools.",
        "origin": (
            "The official speaker roster connects Example Co to Example Person."
        ),
        "sourceLabels": [
            "Official conference schedule",
            "Public company site",
        ],
    }


def test_owner_description_with_product_validation_language_is_preserved() -> None:
    description = (
        "Example Co says its API fetches records for clinical validation workflows."
    )

    safe = COMPANIES.publishable_profile(
        {"summary": description},
        {"writingDisposition": "attribute_to_source"},
    )

    assert safe["summary"] == description


def test_profile_candidates_prefer_private_state_with_legacy_fallback(
    tmp_path: Path,
    monkeypatch,
) -> None:
    private = tmp_path / ".ops/state/cache/company-profile-candidates.json"
    legacy = tmp_path / "raw/sources/company-profiles.json"
    legacy.parent.mkdir(parents=True)
    legacy.write_text(json.dumps({"legacy": {"website": "https://legacy.example"}}))
    monkeypatch.setattr(COMPANIES, "PRIVATE_COMPANY_PROFILES", private)
    monkeypatch.setattr(COMPANIES, "LEGACY_COMPANY_PROFILES", legacy)

    assert "legacy" in COMPANIES.load_company_profile_candidates()

    private.parent.mkdir(parents=True)
    private.write_text(json.dumps({"private": {"website": "https://private.example"}}))

    assert COMPANIES.load_company_profile_candidates() == {
        "private": {"website": "https://private.example"}
    }
    assert COMPANIES.load_company_profile_candidates(legacy) == {
        "legacy": {"website": "https://legacy.example"}
    }


def test_held_profile_cannot_survive_in_curated_company_page(tmp_path: Path) -> None:
    wiki = tmp_path / "wiki"
    companies = wiki / "companies"
    companies.mkdir(parents=True)
    (companies / "example-co.md").write_text(
        "# Example Co\n\n[Wrong owner](https://wrong.example/)\n",
        encoding="utf-8",
    )
    profiles = {
        "example-co": {
            "website": "https://wrong.example/",
            "summary": "Unrelated same-name business with no validated identity path.",
        }
    }
    decisions = {"example-co": {"writingDisposition": "omit"}}

    leaks = COMPANIES.held_profile_public_leaks(
        profiles,
        decisions,
        wiki_root=wiki,
    )

    assert leaks == {"example-co": ("https://wrong.example/",)}


def test_attributed_profile_is_not_treated_as_public_leak(tmp_path: Path) -> None:
    wiki = tmp_path / "wiki"
    companies = wiki / "companies"
    companies.mkdir(parents=True)
    (companies / "example-co.md").write_text(
        "# Example Co\n\n[Owner](https://example.com/)\n",
        encoding="utf-8",
    )

    assert (
        COMPANIES.held_profile_public_leaks(
            {"example-co": {"website": "https://example.com/"}},
            {"example-co": {"writingDisposition": "attribute_to_source"}},
            wiki_root=wiki,
        )
        == {}
    )
