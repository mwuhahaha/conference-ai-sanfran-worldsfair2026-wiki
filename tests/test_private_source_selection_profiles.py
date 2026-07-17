import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_enrichment_script():
    path = ROOT / "scripts" / "enrich_all_articles_from_sources.py"
    spec = importlib.util.spec_from_file_location(
        "enrich_all_articles_from_sources_private_profile_test",
        path,
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def configure_private_profile(module, tmp_path, monkeypatch):
    profile_path = tmp_path / "private-policy.json"
    profile_path.write_text(
        json.dumps(
            {
                "sourceSelectionProfiles": [
                    {
                        "topic": "test-topic",
                        "titleTerms": ["private evidence phrase"],
                        "approvedSupportingMediaIds": ["APPROVED001"],
                        "blockedSupportingMediaIds": ["BLOCKED0001"],
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(module, "PRIVATE_POLICY_PROFILE", profile_path)
    module.private_source_selection_profile.cache_clear()


def prepare_resources(module, tmp_path, monkeypatch):
    wiki = tmp_path / "wiki"
    resources = wiki / "resources"
    resources.mkdir(parents=True)
    titles = {
        "APPROVED001": "A General Product Demonstration",
        "BLOCKED0001": "Private Evidence Phrase Benchmark",
        "LEXICAL0001": "Private Evidence Phrase Retrieval",
        "LEXICAL0002": "Private Evidence Phrase Systems",
        "NOISE000001": "Unrelated Interface Design",
    }
    for video_id, title in titles.items():
        (resources / f"youtube-{video_id}.md").write_text(
            f"# {title}\n",
            encoding="utf-8",
        )
    monkeypatch.setattr(module, "WIKI", wiki)
    monkeypatch.setattr(module, "TRANSCRIPT_DIRS", [])
    monkeypatch.setattr(module, "official_event_video_ids", lambda: frozenset())
    return titles


def test_private_profile_controls_selection_with_a_deterministic_cap(
    tmp_path,
    monkeypatch,
):
    module = load_enrichment_script()
    configure_private_profile(module, tmp_path, monkeypatch)
    titles = prepare_resources(module, tmp_path, monkeypatch)
    candidates = list(titles)
    kwargs = {
        "article_slug": "test-topic",
        "article_title": "Test Topic",
        "article_text": "# Test Topic\n\nA bounded synthesis article.\n",
        "association_pages": [],
        "supporting_limit": 2,
    }

    forward = module.select_relevant_video_ids(candidates, **kwargs)
    reverse = module.select_relevant_video_ids(list(reversed(candidates)), **kwargs)

    assert forward == reverse == ["APPROVED001", "LEXICAL0001"]
    assert "APPROVED001" in forward
    assert "LEXICAL0001" in forward
    assert "BLOCKED0001" not in forward
    assert len(forward) == 2


def test_private_profile_metadata_does_not_leak_into_public_evidence_text(
    tmp_path,
    monkeypatch,
):
    module = load_enrichment_script()
    configure_private_profile(module, tmp_path, monkeypatch)
    titles = prepare_resources(module, tmp_path, monkeypatch)
    selected = module.select_relevant_video_ids(
        list(titles),
        article_slug="test-topic",
        article_title="Test Topic",
        article_text="# Test Topic\n",
        association_pages=[],
        supporting_limit=2,
    )

    rendered = module.render_evidence_section(selected, max_supporting=2)

    # Selected IDs remain ordinary source citations; internal policy does not.
    assert "`youtube-APPROVED001`" in rendered
    assert "`youtube-LEXICAL0001`" in rendered
    assert "private evidence phrase" not in rendered.lower()
    assert "approvedSupportingMediaIds" not in rendered
    assert "blockedSupportingMediaIds" not in rendered
    assert "BLOCKED0001" not in rendered
    assert "LEXICAL0002" not in rendered


def test_topic_policy_requires_an_exact_topic_video_decision(
    tmp_path,
    monkeypatch,
):
    module = load_enrichment_script()
    policy_path = tmp_path / "writing-policy.json"
    policy_path.write_text(
        json.dumps(
            {
                "topicVideoWritingDecisions": {
                    "coding-agents": {
                        "MATCHED0001": {
                            "writingDisposition": "attribute_to_source",
                            "attribution": "source_attributed",
                        }
                    }
                },
                "videoWritingDecisions": {
                    "MATCHED0001": {
                        "writingDisposition": "attribute_to_source",
                        "attribution": "source_attributed",
                    },
                    "OTHER000001": {
                        "writingDisposition": "attribute_to_source",
                        "attribution": "source_attributed",
                    },
                },
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(module, "PRIVATE_CREDIBILITY_V2_POLICY", policy_path)
    module.private_credibility_v2_policy.cache_clear()
    monkeypatch.setattr(
        module,
        "official_event_video_ids",
        lambda: frozenset({"MATCHED0001", "OTHER000001"}),
    )
    monkeypatch.setattr(
        module,
        "private_source_selection_profile",
        lambda _slug: ((), frozenset(), frozenset()),
    )

    selected = module.select_relevant_video_ids(
        ["OTHER000001", "MATCHED0001"],
        article_slug="coding-agents",
        article_title="Coding Agents",
        article_text="# Coding Agents\n",
        association_pages=[],
        supporting_limit=0,
    )

    assert selected == ["MATCHED0001"]
    assert module.private_writing_decision("coding-agents", "OTHER000001")
    assert not module.private_topic_video_writing_decision(
        "coding-agents", "OTHER000001"
    )


def test_entity_policy_changes_attribution_without_exposing_private_metadata(
    tmp_path,
    monkeypatch,
):
    module = load_enrichment_script()
    wiki = tmp_path / "wiki"
    company = wiki / "companies" / "example-co.md"
    (wiki / "companies").mkdir(parents=True)
    (wiki / "talks").mkdir()
    company.write_text("# Example Co\n", encoding="utf-8")
    monkeypatch.setattr(module, "WIKI", wiki)
    monkeypatch.setattr(
        module,
        "private_credibility_v2_policy",
        lambda: {
            "companyWritingDecisions": {
                "example-co": {
                    "writingDisposition": "attribute_to_source",
                    "attribution": "source_attributed",
                }
            }
        },
    )

    assert module.enrich_person_or_company(company, "companies")
    rendered = company.read_text(encoding="utf-8")

    assert "attributed to the official event program" in rendered
    assert "not an endorsement" in rendered
    assert "score" not in rendered.lower()
    assert "weight" not in rendered.lower()
    assert "rank" not in rendered.lower()
