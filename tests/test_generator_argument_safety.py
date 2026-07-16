import importlib.util
import json
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(name.removesuffix(".py"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    "script",
    ["generate_transcript_markdown_pages.py", "generate_synthesis_layers.py"],
)
@pytest.mark.parametrize("argv", [["--help"], ["--unknown-option"]])
def test_help_and_unknown_arguments_exit_before_generating(script, argv, monkeypatch):
    module = load_script(script)

    def unexpected(*_args, **_kwargs):
        raise AssertionError("generator ran before argument validation")

    for name in (
        "load_titles",
        "generate_claims",
        "generate_patterns",
        "generate_harnesses",
    ):
        if hasattr(module, name):
            monkeypatch.setattr(module, name, unexpected)

    with pytest.raises(SystemExit):
        module.main(argv)


def test_transcript_selection_can_be_bounded_to_admitted_video_ids(tmp_path, monkeypatch):
    module = load_script("generate_transcript_markdown_pages.py")
    transcripts = tmp_path / "transcripts"
    transcripts.mkdir()
    (transcripts / "AAAAAAAAAAA.txt").write_text("admitted")
    (transcripts / "BBBBBBBBBBB.txt").write_text("supporting")
    monkeypatch.setattr(module, "TRANSCRIPT_DIRS", [(transcripts, "fixture")])

    selected = module.transcript_paths({"AAAAAAAAAAA"})

    assert [path.stem for path, _label in selected] == ["AAAAAAAAAAA"]


def test_manifest_registry_preserves_supporting_pages_with_explicit_context_role(
    tmp_path, monkeypatch
):
    module = load_script("generate_transcript_markdown_pages.py")
    root = tmp_path / "project"
    out_dir = root / "wiki" / "transcripts"
    out_dir.mkdir(parents=True)
    supporting_id = "BBBBBBBBBBB"
    supporting_page = out_dir / f"youtube-{supporting_id}-transcript.md"
    supporting_page.write_text(
        "---\nwordCount: 2\n---\n# Transcript: Supporting\n\nSupporting text.\n"
    )
    (out_dir / "registry.json").write_text(
        "[{\"id\": \"youtube-BBBBBBBBBBB-transcript\", "
        "\"title\": \"Transcript: Supporting\", "
        "\"path\": \"wiki/transcripts/youtube-BBBBBBBBBBB-transcript.md\", "
        "\"videoId\": \"BBBBBBBBBBB\", \"wordCount\": 2, "
        "\"sourceLabel\": \"Cached transcript markdown\"}]\n"
    )
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "WIKI", root / "wiki")
    official = {
        "id": "youtube-AAAAAAAAAAA-transcript",
        "title": "Transcript: Official",
        "path": "wiki/transcripts/youtube-AAAAAAAAAAA-transcript.md",
        "videoId": "AAAAAAAAAAA",
        "wordCount": 3,
        "sourceLabel": "Official event recording transcript",
    }
    (out_dir / "youtube-AAAAAAAAAAA-transcript.md").write_text(
        "---\nwordCount: 3\n---\n# Transcript: Official\n\nOfficial event text.\n"
    )

    module.write_registry([official], official_video_ids={"AAAAAAAAAAA"})
    first_registry = (out_dir / "registry.json").read_text()
    module.write_registry([official], official_video_ids={"AAAAAAAAAAA"})
    catalog = json.loads((out_dir / "registry.json").read_text())
    index = (out_dir / "index.md").read_text()

    assert (out_dir / "registry.json").read_text() == first_registry
    assert {record["videoId"] for record in catalog} == {
        "AAAAAAAAAAA",
        "BBBBBBBBBBB",
    }
    roles = {record["videoId"]: record["sourceRole"] for record in catalog}
    assert roles == {
        "AAAAAAAAAAA": "primary_event_evidence",
        "BBBBBBBBBBB": "context_only",
    }
    assert "## Official WF26 Event Transcripts" in index
    assert "## Supporting Context Transcripts" in index


def test_synthesis_summary_is_private_state_not_a_public_raw_source():
    module = load_script("generate_synthesis_layers.py")

    assert module.INTERNAL_SYNTHESIS_DIR == (
        ROOT / ".ops" / "state" / "cache" / "synthesis-layers"
    )
    assert not (ROOT / "raw" / "sources" / "topic-evidence-table-summary.json").exists()


def test_topic_source_coverage_replaces_legacy_sections_without_self_reinforcement(
    tmp_path, monkeypatch
):
    module = load_script("generate_synthesis_layers.py")
    wiki = tmp_path / "wiki"
    (wiki / "topics").mkdir(parents=True)
    (wiki / "talks").mkdir()
    (wiki / "resources").mkdir()
    (wiki / "talks" / "talk-a.md").write_text("# Talk A\n")
    (wiki / "resources" / "video-a.md").write_text("# Video A\n")
    topic = wiki / "topics" / "test-topic.md"
    topic.write_text(
        "# Test Topic\n\n"
        "## Connections\n- [[talk-a]]\n- [[video-a]]\n\n"
        "## Source Coverage\n- [[stale-source]]\n\n"
        "## Evidence Table\n- [[stale-table]]\n\n"
        "## Representative Evidence Links\n- [[stale-representative]]\n"
    )
    monkeypatch.setattr(module, "WIKI", wiki)
    monkeypatch.setattr(module, "INTERNAL_SYNTHESIS_DIR", tmp_path / "private")
    monkeypatch.setattr(module, "TOPICS_FOR_EVIDENCE_TABLES", ["test-topic"])

    first_summary = module.update_topic_evidence_tables()
    first = topic.read_text()
    second_summary = module.update_topic_evidence_tables()

    assert first_summary == second_summary == {
        "test-topic": {"talks": 1, "resources": 1}
    }
    assert topic.read_text() == first
    assert first.count("## Source Coverage") == 1
    assert "## Evidence Table" not in first
    assert "## Representative Evidence Links" not in first
    assert "stale-" not in first


def test_media_signal_priority_preserves_official_ids_and_labels_sparse_context(
    monkeypatch,
):
    module = load_script("enrich_all_articles_from_sources.py")
    official = ["AAAAAAAAAAA", "BBBBBBBBBBB", "CCCCCCCCCCC"]
    monkeypatch.setattr(
        module,
        "official_event_video_ids",
        lambda: frozenset(official),
    )

    prioritized = module.prioritize_video_ids(
        ["support0001", *official, "support0002"],
        supporting_limit=0,
    )
    assert prioritized == official
    assert module.prioritize_video_ids(
        ["support0001", *official, "support0002"],
        supporting_limit=1,
    ) == [*official, "support0001"]

    monkeypatch.setattr(
        module,
        "evidence_for_video",
        lambda _video_id: {
            "transcript_words": 0,
            "slide_lines": ["hello"],
            "slide_keywords": ["hello"],
            "resource_exists": True,
            "source_role": "supporting context only",
            "transcript_path": None,
            "slide_pages": ["youtube-support0001-slides"],
            "keywords": [],
        },
    )
    rendered = module.render_evidence_section(["support0001"])

    assert "role: supporting context only" in rendered
    assert "Evidence links for `youtube-support0001` (supporting context only)" in rendered
    assert "Slide-derived themes" not in rendered
    assert "slide-derived text signals" not in rendered


def test_topic_enrichment_preserves_existing_official_media_ids(tmp_path, monkeypatch):
    module = load_script("enrich_all_articles_from_sources.py")
    wiki = tmp_path / "wiki"
    topic = wiki / "topics" / "coding-agents.md"
    (wiki / "topics").mkdir(parents=True)
    (wiki / "talks").mkdir()
    (wiki / "resources").mkdir()
    official = ["AAAAAAAAAAA", "BBBBBBBBBBB", "CCCCCCCCCCC", "DDDDDDDDDDD"]
    for video_id in official:
        (wiki / "resources" / f"youtube-{video_id}.md").write_text(
            f"# Resource {video_id}\n"
        )
    topic.write_text(
        "# Coding Agents\n\n## Evidence Graph\n"
        + "\n".join(f"- [[youtube-{video_id}]]" for video_id in official)
        + "\n"
    )
    monkeypatch.setattr(module, "WIKI", wiki)
    monkeypatch.setattr(
        module,
        "official_event_video_ids",
        lambda: frozenset(official),
    )

    assert module.enrich_topic(topic)
    enriched = topic.read_text()

    for video_id in official:
        assert f"[[youtube-{video_id}]]" in enriched
        assert f"`youtube-{video_id}`" in enriched


@pytest.mark.parametrize(
    ("slug", "title", "strong_id", "strong_title", "weak_title"),
    [
        (
            "coding-agents",
            "Coding Agents",
            "strongcode1",
            "Recursive Coding Agents in Production",
            "From Text to Vision to Voice",
        ),
        (
            "mcp",
            "Model Context Protocol",
            "strongmcp01",
            "MCP Apps and Model Context Protocol",
            "General AI Engineering Keynote",
        ),
    ],
)
def test_topic_media_budget_prefers_semantic_evidence_over_first_found_sources(
    tmp_path,
    monkeypatch,
    slug,
    title,
    strong_id,
    strong_title,
    weak_title,
):
    module = load_script("enrich_all_articles_from_sources.py")
    wiki = tmp_path / "wiki"
    topic = wiki / "topics" / f"{slug}.md"
    (wiki / "topics").mkdir(parents=True)
    (wiki / "talks").mkdir()
    (wiki / "resources").mkdir()
    topic.write_text(f"# {title}\n")
    weak_ids = [f"weakvideo{index:02d}" for index in range(1, 10)]
    for index, video_id in enumerate(weak_ids):
        (wiki / "resources" / f"youtube-{video_id}.md").write_text(
            f"# {weak_title}\n"
        )
        (wiki / "talks" / f"{index:02d}-weak-session.md").write_text(
            f"# General Session {index}\n\n"
            f"- [[{slug}]]\n"
            f"- https://www.youtube.com/watch?v={video_id}\n"
        )
    (wiki / "resources" / f"youtube-{strong_id}.md").write_text(
        f"# {strong_title}\n"
    )
    (wiki / "talks" / "99-strong-session.md").write_text(
        f"# {strong_title}\n\n"
        f"- [[{slug}]]\n"
        f"- https://www.youtube.com/watch?v={strong_id}\n"
    )
    monkeypatch.setattr(module, "WIKI", wiki)
    monkeypatch.setattr(module, "official_event_video_ids", lambda: frozenset())
    monkeypatch.setattr(
        module,
        "private_source_selection_profile",
        lambda _slug: ((), frozenset(), frozenset()),
    )

    assert module.enrich_topic(topic)
    enriched = topic.read_text()

    assert f"`youtube-{strong_id}`" in enriched
    assert sum(f"`youtube-{video_id}`" in enriched for video_id in weak_ids) == 7
    assert enriched.count("role: supporting context only") == 8
    assert "relevance score" not in enriched.lower()


def test_relevant_video_selection_is_deterministic_and_keeps_all_official_ids(
    tmp_path, monkeypatch
):
    module = load_script("enrich_all_articles_from_sources.py")
    wiki = tmp_path / "wiki"
    (wiki / "resources").mkdir(parents=True)
    candidates = {
        "weakvideo01": "General AI Engineering",
        "strongcode1": "Production Coding Agents",
        "weakvideo02": "Multimodal Product Interfaces",
    }
    for video_id, title in candidates.items():
        (wiki / "resources" / f"youtube-{video_id}.md").write_text(f"# {title}\n")
    monkeypatch.setattr(module, "WIKI", wiki)
    official = ["AAAAAAAAAAA", "BBBBBBBBBBB"]
    monkeypatch.setattr(
        module, "official_event_video_ids", lambda: frozenset(official)
    )
    monkeypatch.setattr(
        module,
        "private_source_selection_profile",
        lambda _slug: ((), frozenset(), frozenset()),
    )

    kwargs = {
        "article_slug": "coding-agents",
        "article_title": "Coding Agents",
        "article_text": "# Coding Agents\n",
        "association_pages": [],
        "supporting_limit": 1,
    }
    forward = module.select_relevant_video_ids(
        [*official, *candidates], **kwargs
    )
    reverse = module.select_relevant_video_ids(
        [*reversed(official), *reversed(candidates)], **kwargs
    )

    assert set(forward[:2]) == set(official)
    assert set(reverse[:2]) == set(official)
    assert forward[-1] == reverse[-1] == "strongcode1"
    assert len(forward) == len(official) + 1


def test_relevant_video_selection_does_not_fill_budget_with_unrelated_context(
    tmp_path, monkeypatch
):
    module = load_script("enrich_all_articles_from_sources.py")
    wiki = tmp_path / "wiki"
    (wiki / "resources").mkdir(parents=True)
    candidates = {
        "evalsource1": "The Art of Benchmarking Evaluations",
        "weakvideo01": "From Text to Voice",
        "weakvideo02": "A General Product Keynote",
        "weakvideo03": "Designing Consumer Interfaces",
    }
    for video_id, title in candidates.items():
        (wiki / "resources" / f"youtube-{video_id}.md").write_text(f"# {title}\n")
    monkeypatch.setattr(module, "WIKI", wiki)
    monkeypatch.setattr(module, "official_event_video_ids", lambda: frozenset())
    monkeypatch.setattr(
        module,
        "private_source_selection_profile",
        lambda _slug: ((), frozenset(), frozenset()),
    )

    selected = module.select_relevant_video_ids(
        list(candidates),
        article_slug="agent-evaluations",
        article_title="Agent Evaluations",
        article_text=(
            "# Agent Evaluations\n\n"
            "## Overview\nUse benchmarks, regression suites, and task rubrics.\n"
        ),
        association_pages=[],
        supporting_limit=3,
    )

    assert selected == ["evalsource1"]


def test_relevant_video_selection_uses_article_concepts_and_word_variants(
    tmp_path, monkeypatch
):
    module = load_script("enrich_all_articles_from_sources.py")
    wiki = tmp_path / "wiki"
    (wiki / "resources").mkdir(parents=True)
    candidates = {
        "vibecontext": "A Month of Vibe Coding",
        "semantic001": "Benchmarking Semantic Code Retrieval",
        "localindex1": "Building a Local Code Index",
    }
    for video_id, title in candidates.items():
        (wiki / "resources" / f"youtube-{video_id}.md").write_text(f"# {title}\n")
    monkeypatch.setattr(module, "WIKI", wiki)
    monkeypatch.setattr(module, "official_event_video_ids", lambda: frozenset())
    monkeypatch.setattr(
        module,
        "private_source_selection_profile",
        lambda _slug: ((), frozenset(), frozenset()),
    )

    selected = module.select_relevant_video_ids(
        list(candidates),
        article_slug="agentic-search",
        article_title="Agentic Search",
        article_text=(
            "# Agentic Search\n\n"
            "## Overview\nSemantic retrieval and local indexes improve search coverage.\n"
        ),
        association_pages=[],
        supporting_limit=2,
    )

    assert set(selected) == {"semantic001", "localindex1"}


def test_event_resource_classifier_preserves_specific_admission_provenance():
    module = load_script("classify_video_resource_sources.py")
    page = "# Recording\n\n## What It Is\nOld text.\n\n## Link\nSource.\n"

    cut = module.rewrite_what_it_is(page, "primary event cut video")
    livestream = module.rewrite_what_it_is(page, "primary event livestream")
    _role, cut_lines = module.classification(
        "AAAAAAAAAAA",
        set(),
        {"AAAAAAAAAAA"},
        set(),
        set(),
    )

    assert "verified against" in cut
    assert "scheduled session" in cut
    assert "explicitly identified" in livestream
    assert "official schedule pages remain canonical" in cut
    assert any("verified against scheduled-session" in line for line in cut_lines)
