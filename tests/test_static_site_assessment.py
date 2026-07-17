from __future__ import annotations

import hashlib
import sys
from pathlib import Path
from unittest.mock import patch

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import export_static_site  # noqa: E402


LIMITED = {
    "schemaVersion": 1,
    "claimId": "claim:event-listing",
    "subjectId": "person:example",
    "domain": "people page evidence coverage",
    "intendedUse": "attributed_context",
    "asOf": "2026-07-17T12:00:00.000000Z",
    "state": "limited",
    "basis": "official_primary_canonical",
    "message": "This page is limited to source-attributed facts; independent support for broader claims may be limited.",
    "publicSourceIds": ["source:official-wf26-event-record"],
}

PENDING = {
    **LIMITED,
    "state": "pending",
    "basis": "no_admitted_evidence",
    "message": "This page has not yet received enough admitted evidence for a source assessment.",
    "publicSourceIds": [],
}

STRONG = {
    **LIMITED,
    "state": "strong",
    "basis": "independently_supported",
    "message": "Material claims on this page have strong independent evidence coverage.",
}

CONTESTED = {
    **LIMITED,
    "state": "contested",
    "basis": "sources_disagree",
    "message": "Sources materially disagree; review the dated citations before relying on the disputed claims.",
}

BODY = "# Example\n\nPublic body text."


def assessed_frontmatter(capsule: dict, body: str = BODY) -> dict:
    return {
        "sourceAssessment": capsule,
        "sourceAssessmentBodySha256": "sha256:"
        + hashlib.sha256(body.strip().encode("utf-8")).hexdigest(),
    }


def test_exporter_hides_ordinary_limited_assessment_from_humans() -> None:
    rendered = export_static_site.render_source_assessment(
        assessed_frontmatter(LIMITED), BODY
    )

    assert rendered == ""


def test_exporter_renders_only_fixed_low_boundary_message() -> None:
    rendered = export_static_site.render_source_assessment(
        assessed_frontmatter(PENDING), BODY
    )

    assert "source-assessment--pending" in rendered
    assert "Evidence note." in rendered
    assert "not yet received enough admitted evidence" in rendered
    assert "claim:event-listing" not in rendered
    assert "publicSourceIds" not in rendered


@pytest.mark.parametrize(
    ("capsule", "css_class", "message"),
    [
        (STRONG, "source-assessment--strong", "strong independent evidence"),
        (CONTESTED, "source-assessment--contested", "Sources materially disagree"),
    ],
)
def test_exporter_renders_fixed_high_and_contested_messages(
    capsule: dict, css_class: str, message: str
) -> None:
    rendered = export_static_site.render_source_assessment(
        assessed_frontmatter(capsule), BODY
    )

    assert css_class in rendered
    assert message in rendered
    assert "claim:event-listing" not in rendered


def test_page_parser_keeps_assessment_out_of_body_excerpt_and_search(tmp_path: Path) -> None:
    wiki = tmp_path / "wiki"
    page = wiki / "people/example.md"
    page.parent.mkdir(parents=True)
    page.write_text(
        "---\ntitle: Example\ncategory: people\nsourceAssessment:\n"
        + "\n".join(f"  {key}: {value!r}" for key, value in LIMITED.items())
        + "\nsourceAssessmentBodySha256: "
        + assessed_frontmatter(LIMITED)["sourceAssessmentBodySha256"]
        + "\n---\n"
        + BODY
        + "\n"
    )

    with patch.object(export_static_site, "WIKI", wiki):
        parsed = export_static_site.parse_page(page)

    assert parsed.frontmatter["sourceAssessment"]["state"] == "limited"
    assert "sourceAssessment" not in parsed.body
    assert "sourceAssessment" not in parsed.excerpt
    assert parsed.excerpt.endswith("Public body text.")


def test_exporter_rejects_private_fields_and_alias_collision() -> None:
    unsafe = {**LIMITED, "totalPoints": 99}
    with pytest.raises(ValueError, match="invalid public source assessment"):
        export_static_site.render_source_assessment(
            assessed_frontmatter(unsafe), BODY
        )

    with pytest.raises(ValueError, match="cannot both be present"):
        export_static_site.render_source_assessment(
            {
                **assessed_frontmatter(LIMITED),
                "evidenceAssessment": LIMITED,
            },
            BODY,
        )


def test_exporter_rejects_stale_assessment_after_body_change() -> None:
    with pytest.raises(ValueError, match="stale for the current page body"):
        export_static_site.render_source_assessment(
            assessed_frontmatter(LIMITED), BODY + "\n\nNew evidence."
        )
