import importlib.util
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    path = ROOT / "scripts" / name
    scripts_path = str(path.parent)
    if scripts_path not in sys.path:
        sys.path.insert(0, scripts_path)
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


def test_stale_pending_and_unavailable_transcripts_cannot_become_primary():
    module = load_script("generate_transcript_markdown_pages.py")
    videos = [
        {"id": "recording01", "mediaType": "talk_recording", "videoAvailability": "public"},
        {"id": "stream00001", "mediaType": "event_livestream"},
        {"id": "premiere001", "mediaType": "scheduled_premiere", "videoAvailability": "public"},
        {"id": "private0001", "mediaType": "unavailable_playlist_item"},
        {"id": "privateCut1", "mediaType": "talk_recording", "videoAvailability": "private"},
        {
            "id": "playlistBad",
            "mediaType": "talk_recording",
            "videoAvailability": "public",
            "playlistAvailability": "unavailable",
        },
        {
            "id": "playlistUnk",
            "mediaType": "event_livestream",
            "videoAvailability": "public",
            "playlistAvailability": "unknown",
        },
    ]

    assert module.official_manifest_video_ids(videos) == {
        "recording01",
        "stream00001",
    }


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
        lambda _video_id, **_kwargs: {
            "transcript_words": 0,
            "slide_lines": ["hello"],
            "slide_keywords": ["hello"],
            "resource_exists": True,
            "source_role": "supporting context only",
            "transcript_path": None,
            "slide_pages": ["youtube-support0001-slides"],
            "keywords": [],
            "attribution": "",
        },
    )
    rendered = module.render_evidence_section(["support0001"])

    assert "role: supporting context only" in rendered
    assert "Evidence links for `youtube-support0001` (supporting context only)" in rendered
    assert "Slide-derived themes" not in rendered
    assert "slide-derived text signals" not in rendered


def test_official_event_video_ids_exclude_nonplayable_manifest_rows():
    module = load_script("enrich_all_articles_from_sources.py")
    module.official_event_video_ids.cache_clear()
    module.official_video_manifest = lambda: {
        "recording01": {
            "mediaType": "talk_recording",
            "matchedTalks": ["example-talk"],
        },
        "stream00001": {"mediaType": "event_livestream"},
        "premiere001": {"mediaType": "scheduled_premiere"},
        "private0001": {"mediaType": "unavailable_playlist_item"},
        "privateCut1": {
            "mediaType": "talk_recording",
            "videoAvailability": "private",
            "playlistAvailability": "available",
            "matchedTalks": ["example-talk"],
        },
        "playlistBad": {
            "mediaType": "talk_recording",
            "videoAvailability": "public",
            "playlistAvailability": "unavailable",
            "matchedTalks": ["example-talk"],
        },
        "playlistUnk": {
            "mediaType": "event_livestream",
            "videoAvailability": "public",
            "playlistAvailability": "unknown",
        },
    }

    assert module.official_event_video_ids() == frozenset(
        {"recording01", "stream00001"}
    )
    assert module.official_recording_ids_for_talk("example-talk") == ["recording01"]
    module.official_event_video_ids.cache_clear()


def test_active_source_enrichment_demotes_retired_topic_primary_marker(
    tmp_path, monkeypatch
):
    module = load_script("enrich_all_articles_from_sources.py")
    page = tmp_path / "topic.md"
    page.write_text(
        "# Topic\n\n"
        "- Valid (verified event YouTube resource; via [[youtube-validVid001]])\n"
        "- Retired (verified event YouTube resource; via [[youtube-o-zkvb0iFDQ]])\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        module, "official_event_video_ids", lambda: frozenset({"validVid001"})
    )

    assert module.reconcile_retired_topic_connection_roles(page) is True
    assert module.reconcile_retired_topic_connection_roles(page) is False
    text = page.read_text(encoding="utf-8")
    assert "verified event YouTube resource; via [[youtube-validVid001]]" in text
    assert "related YouTube resource; via [[youtube-o-zkvb0iFDQ]]" in text


def test_talk_evidence_excludes_unmatched_official_event_media_and_stale_blocks(
    monkeypatch,
):
    module = load_script("enrich_all_articles_from_sources.py")
    exact_id = "AAAAAAAAAAA"
    broad_id = "BBBBBBBBBBB"
    supporting_id = "CCCCCCCCCCC"
    manifest = {
        exact_id: {
            "mediaType": "talk_recording",
            "matchedTalks": ["example-talk"],
        },
        broad_id: {"mediaType": "event_livestream"},
    }
    monkeypatch.setattr(module, "official_video_manifest", lambda: manifest)
    monkeypatch.setattr(
        module,
        "official_event_video_ids",
        lambda: frozenset(manifest),
    )
    monkeypatch.setattr(module, "has_video_evidence", lambda _video_id: True)
    markdown = (
        "# Example Talk\n\n"
        "## Media Evidence\n"
        f"- [[youtube-{supporting_id}]] - related context.\n\n"
        f"- [[youtube-{broad_id}]] - stale ordinary broad-stream link.\n\n"
        f"- Source video: `youtube-{broad_id}`\n"
        f"- Slide deck: [[youtube-{broad_id}-slides]].\n\n"
        "## Transcript Markdown\n"
        f"- [[youtube-{broad_id}-transcript]] - broad stream.\n\n"
        "## Recording Search Status\n"
        f"The broad stream [[youtube-{broad_id}]] was checked.\n"
    )

    cleaned = module.strip_unmatched_event_media(markdown, "example-talk")
    selected = module.talk_evidence_video_ids("example-talk", cleaned)

    assert selected == [exact_id, supporting_id]
    assert f"Source video: `youtube-{broad_id}`" not in cleaned
    assert f"youtube-{broad_id}-transcript" not in cleaned
    assert f"The broad stream [[youtube-{broad_id}]] was checked." in cleaned

    repaired = module.ensure_talk_media_evidence(
        cleaned,
        "example-talk",
        selected,
    )
    assert "## Media Evidence" in repaired
    assert f"[[youtube-{exact_id}]] - dedicated official event recording" in repaired
    media_section = repaired.split("## Media Evidence\n", 1)[1].split(
        "\n## ", 1
    )[0]
    assert f"youtube-{broad_id}" not in media_section
    assert f"youtube-{supporting_id}" in media_section


def test_generated_evidence_is_not_reingested_as_source_text() -> None:
    module = load_script("enrich_all_articles_from_sources.py")
    markdown = (
        "---\ntitle: Example\n---\n# Example\n\n"
        "## Connections\n- [[example-talk]]\n\n"
        "## Evidence Graph\n"
        "- `youtube-BBBBBBBBBBB` - stale generated source.\n\n"
        "## Evidence Boundary\n- Keep layers labeled.\n"
    )

    source_text = module.source_text_for_enrichment(markdown)

    assert "[[example-talk]]" in source_text
    assert "youtube-BBBBBBBBBBB" not in source_text
    assert "## Evidence Boundary" in source_text

    talk_source_text = module.source_text_for_enrichment(
        markdown
        + "\n## Media Evidence\n- [[youtube-CCCCCCCCCCC]]\n"
        + "\n## Transcript Markdown\n- [[youtube-BBBBBBBBBBB-transcript]]\n"
        + "\n## Slides\n- [[youtube-BBBBBBBBBBB-slides]]\n"
        + "\n## Synthesis\n- [[youtube-BBBBBBBBBBB]]\n",
        module.TALK_GENERATED_SOURCE_HEADINGS,
    )
    assert "youtube-BBBBBBBBBBB" not in talk_source_text
    assert "youtube-CCCCCCCCCCC" not in talk_source_text


def test_topic_enrichment_preserves_privately_gated_official_media_ids(
    tmp_path, monkeypatch
):
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
    stale = "EEEEEEEEEEE"
    (wiki / "resources" / f"youtube-{stale}.md").write_text("# Stale Resource\n")
    topic.write_text(
        "# Coding Agents\n\n## Primary Sources\n"
        + "\n".join(f"- [[youtube-{video_id}]]" for video_id in official)
        + "\n\n## Evidence Graph\n"
        + f"- [[youtube-{stale}]] - stale generated source.\n"
    )
    monkeypatch.setattr(module, "WIKI", wiki)
    monkeypatch.setattr(
        module,
        "official_event_video_ids",
        lambda: frozenset(official),
    )
    monkeypatch.setattr(
        module,
        "private_credibility_v2_policy",
        lambda: {
            "topicVideoWritingDecisions": {
                "coding-agents": {
                    video_id: {"writingDisposition": "attribute_to_source"}
                    for video_id in official
                }
            }
        },
    )

    assert module.enrich_topic(topic)
    enriched = topic.read_text()

    for video_id in official:
        assert f"[[youtube-{video_id}]]" in enriched
        assert f"`youtube-{video_id}`" in enriched
    assert f"[[youtube-{stale}]]" not in enriched


def test_topic_without_private_policy_does_not_admit_global_official_media(
    tmp_path, monkeypatch
):
    module = load_script("enrich_all_articles_from_sources.py")
    wiki = tmp_path / "wiki"
    topic = wiki / "topics" / "voice-agents.md"
    (wiki / "topics").mkdir(parents=True)
    (wiki / "talks").mkdir()
    (wiki / "resources").mkdir()
    unrelated = "AAAAAAAAAAA"
    (wiki / "resources" / f"youtube-{unrelated}.md").write_text(
        "# Closing Keynote: Garry Tan\n"
    )
    (wiki / "talks" / "voice-overview.md").write_text(
        "# Voice Agents Overview\n\n"
        "## Media Evidence\n"
        f"- [[youtube-{unrelated}]] - stale generated source.\n"
    )
    topic.write_text("# Voice Agents\n\n## Overview\nRealtime speech systems.\n")
    monkeypatch.setattr(module, "WIKI", wiki)
    monkeypatch.setattr(
        module, "official_event_video_ids", lambda: frozenset({unrelated})
    )
    monkeypatch.setattr(module, "private_credibility_v2_policy", lambda: {})

    assert module.enrich_topic(topic)
    enriched = topic.read_text()

    assert unrelated not in enriched
    assert "No linked video, transcript, or slide source" in enriched


def test_topic_generated_source_sections_cannot_bypass_private_gate(
    tmp_path, monkeypatch
):
    module = load_script("enrich_all_articles_from_sources.py")
    wiki = tmp_path / "wiki"
    topic = wiki / "topics" / "voice-agents.md"
    (wiki / "topics").mkdir(parents=True)
    (wiki / "talks").mkdir()
    (wiki / "resources").mkdir()
    stale_official = "AAAAAAAAAAA"
    stale_supporting = "BBBBBBBBBBB"
    for video_id in (stale_official, stale_supporting):
        (wiki / "resources" / f"youtube-{video_id}.md").write_text(
            "# Voice-adjacent legacy source\n"
        )
    topic.write_text(
        "# Voice Agents\n\n## Overview\nRealtime speech systems.\n\n"
        "## Source Coverage\n"
        f"- [[youtube-{stale_official}]]\n"
        f"- [[youtube-{stale_supporting}]]\n\n"
        "## Slide-Derived Supporting Decks\n"
        f"- [[youtube-{stale_official}-slides]]\n"
    )
    monkeypatch.setattr(module, "WIKI", wiki)
    monkeypatch.setattr(
        module,
        "official_event_video_ids",
        lambda: frozenset({stale_official}),
    )
    monkeypatch.setattr(module, "private_credibility_v2_policy", lambda: {})

    assert module.enrich_topic(topic)
    evidence = topic.read_text().split("## Evidence Graph", 1)[1]

    assert stale_official not in evidence
    assert stale_supporting not in evidence


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


def test_relevant_video_selection_fails_closed_without_policy_or_direct_link(
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
    monkeypatch.setattr(module, "private_credibility_v2_policy", lambda: {})
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

    assert forward == reverse == ["strongcode1"]


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


def test_event_resource_classifier_separates_playlist_recordings_and_unavailable_items():
    module = load_script("classify_video_resource_sources.py")
    page = "# Recording\n\n## What It Is\nOld text.\n\n## Link\nSource.\n"

    playlist_role, playlist_lines = module.classification(
        "AAAAAAAAAAA",
        set(),
        {"AAAAAAAAAAA"},
        set(),
        set(),
        {"AAAAAAAAAAA"},
        set(),
    )
    unavailable_role, unavailable_lines = module.classification(
        "BBBBBBBBBBB",
        set(),
        set(),
        set(),
        set(),
        {"BBBBBBBBBBB"},
        {"BBBBBBBBBBB"},
    )

    assert playlist_role == "primary event playlist recording"
    assert any("playlist membership" in line for line in playlist_lines)
    assert "Playlist membership establishes event association" in module.rewrite_what_it_is(
        page, playlist_role
    )
    assert unavailable_role == "official event unavailable playlist item"
    assert any("do not use this placeholder" in line for line in unavailable_lines)
    unavailable = module.rewrite_what_it_is(page, unavailable_role)
    assert "no content or schedule claim" in unavailable
    assert "primary event video source" not in "\n".join(unavailable_lines)


def test_event_resource_classifier_honors_explicit_no_slides_status():
    module = load_script("classify_video_resource_sources.py")

    role, lines = module.classification(
        "NOSLIDES001",
        set(),
        {"NOSLIDES001"},
        set(),
        set(),
        {"NOSLIDES001"},
        set(),
        {"NOSLIDES001"},
    )

    assert role == "primary event playlist recording"
    assert "no slide deck" in " ".join(lines).lower()
    assert "slide content" not in " ".join(lines).lower()


def test_event_resource_classifier_rebuilds_slide_registry_from_existing_pages(
    tmp_path,
    monkeypatch,
):
    module = load_script("classify_video_resource_sources.py")
    wiki = tmp_path / "wiki"
    slides = wiki / "slides"
    slides.mkdir(parents=True)
    (slides / "youtube-AAAAAAAAAAA-slides.md").write_text(
        '---\ntitle: "Current Deck"\n---\n# Current Deck\n\n'
        "![[assets/slides/AAAAAAAAAAA/slide-001.jpg]]\n"
    )
    (slides / "registry.json").write_text(
        '[{"id":"youtube-BBBBBBBBBBB-slides","path":"missing"}]\n'
    )
    monkeypatch.setattr(module, "WIKI", wiki)

    assert module.rebuild_slide_registry() == 1
    registry = json.loads((slides / "registry.json").read_text())
    assert registry == [
        {
            "id": "youtube-AAAAAAAAAAA-slides",
            "title": "Current Deck",
            "path": "wiki/slides/youtube-AAAAAAAAAAA-slides.md",
            "slide_count": 1,
        }
    ]


def test_manifest_media_type_sets_do_not_promote_private_or_premiere_as_cut(tmp_path, monkeypatch):
    module = load_script("classify_video_resource_sources.py")
    manifest = tmp_path / "official-wf26-video-manifest.json"
    channel_streams = tmp_path / "aidotengineer-channel-streams-latest.json"
    manifest.write_text(
        json.dumps(
            {
                "videos": [
                    {"id": "recording01", "mediaType": "talk_recording"},
                    {"id": "stream00001", "mediaType": "event_livestream"},
                    {"id": "premiere001", "mediaType": "scheduled_premiere"},
                    {"id": "private0001", "mediaType": "unavailable_playlist_item"},
                    {
                        "id": "blockedCut1",
                        "mediaType": "talk_recording",
                        "videoAvailability": "private",
                        "playlistAvailability": "available",
                    },
                ]
            }
        ),
        encoding="utf-8",
    )
    channel_streams.write_text(
        json.dumps(
            {
                "entries": [
                    {
                        "id": "heuristic01",
                        "title": "AI Engineer World's Fair 2026 Livestream",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(module, "OFFICIAL_VIDEO_MANIFEST", manifest)
    monkeypatch.setattr(module, "RAW", tmp_path)
    monkeypatch.setattr(module, "confirmed_event_cut_ids", lambda: {"legacyHeuristic"})

    assert module.official_wf_cut_ids() == {"recording01"}
    assert module.official_wf_livestream_ids() == {"stream00001"}
    assert module.official_wf_premiere_ids() == {"premiere001"}
    assert module.official_wf_unavailable_ids() == {"blockedCut1", "private0001"}


def test_media_source_layer_override_tracks_non_playable_state():
    module = load_script("classify_video_resource_sources.py")
    page = '---\ntitle: "Media"\ncategory: "resources"\n---\n# Media\n'

    scheduled = module.reconcile_media_source_layers(
        page, "primary event scheduled premiere"
    )
    assert 'sourceLayers: ["supporting_context"]' in scheduled

    unavailable = module.reconcile_media_source_layers(
        scheduled, "official event unavailable playlist item"
    )
    assert unavailable.count('sourceLayers: ["supporting_context"]') == 1

    playable = module.reconcile_media_source_layers(
        unavailable, "primary event cut video"
    )
    assert "sourceLayers:" not in playable

    supporting = module.reconcile_media_source_layers(
        unavailable, "supporting external video"
    )
    assert 'sourceLayers: ["supporting_context"]' in supporting


def test_livestream_inventory_separates_title_discovery_from_primary_admission(
    tmp_path, monkeypatch
):
    module = load_script("generate_livestream_inventory.py")
    raw = tmp_path / "raw" / "sources"
    wiki = tmp_path / "wiki"
    raw.mkdir(parents=True)
    (raw / "aidotengineer-channel-streams-latest.json").write_text(
        json.dumps(
            {
                "entries": [
                    {"id": "manifest001", "title": "Main Stage Stream"},
                    {
                        "id": "heuristic01",
                        "title": "AI Engineer World's Fair 2026 Livestream",
                    },
                ]
            }
        ),
        encoding="utf-8",
    )
    manifest = raw / "official-wf26-video-manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "videos": [
                    {"id": "manifest001", "mediaType": "event_livestream"}
                ]
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(module, "RAW", raw)
    monkeypatch.setattr(module, "WIKI", wiki)
    monkeypatch.setattr(module, "RESOURCES", wiki / "resources")
    monkeypatch.setattr(module, "SLIDES", wiki / "slides")
    monkeypatch.setattr(module, "OFFICIAL_VIDEO_MANIFEST", manifest)

    rows = {row["video_id"]: row for row in module.stream_rows()}

    assert rows["manifest001"]["primary_wf26"] is True
    assert rows["heuristic01"]["worldsfair"] is True
    assert rows["heuristic01"]["primary_wf26"] is False


def write_static_media_fixture(root):
    search_rows = []
    for category in ("resources", "transcripts", "slides"):
        source_dir = root / "wiki" / category
        if not source_dir.is_dir():
            continue
        for source in source_dir.glob("youtube-*.md"):
            target = root / "dist" / "md" / category / source.name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
            rendered = root / "dist" / category / source.stem / "index.html"
            rendered.parent.mkdir(parents=True, exist_ok=True)
            rendered.write_text(
                f"<html><main>{source.read_text(encoding='utf-8')}</main></html>",
                encoding="utf-8",
            )
            search_rows.append(
                {
                    "title": source.stem,
                    "url": f"/{category}/{source.stem}/",
                    "category": category,
                    "excerpt": source.read_text(encoding="utf-8"),
                }
            )
    search = root / "dist" / "search" / "index.html"
    search.parent.mkdir(parents=True, exist_ok=True)
    search.write_text(
        '<script id="search-index" type="application/json">'
        + json.dumps(search_rows)
        + "</script>",
        encoding="utf-8",
    )


def test_primary_media_role_audit_checks_markers_segments_and_transcripts(
    tmp_path, monkeypatch
):
    module = load_script("audit_primary_media_roles.py")
    monkeypatch.setattr(module, "DURABLE_RETIRED_IDS", set())
    root = tmp_path / "project"
    raw = root / "raw" / "sources"
    topics = root / "wiki" / "topics"
    resources = root / "wiki" / "resources"
    transcripts = root / "wiki" / "transcripts"
    for path in (raw, topics, resources, transcripts):
        path.mkdir(parents=True)
    (raw / "official-wf26-video-manifest.json").write_text(
        json.dumps(
            {
                "videos": [
                    {"id": "recording01", "mediaType": "talk_recording"},
                    {"id": "stream00001", "mediaType": "event_livestream"},
                    {"id": "premiere001", "mediaType": "scheduled_premiere"},
                    {
                        "id": "privateCut1",
                        "mediaType": "talk_recording",
                        "videoAvailability": "private",
                        "playlistAvailability": "available",
                    },
                    {
                        "id": "missingCut1",
                        "mediaType": "talk_recording",
                        "videoAvailability": "public",
                        "playlistAvailability": "unavailable",
                    },
                ]
            }
        ),
        encoding="utf-8",
    )
    topic = topics / "example.md"
    topic.write_text(
        "- verified event YouTube resource; via [[youtube-premiere001]]\n"
        "- verified event YouTube resource; via [[youtube-orphan00001]]\n",
        encoding="utf-8",
    )
    (raw / "livestream-talk-segments.json").write_text(
        json.dumps([{"video_id": "recording01"}]), encoding="utf-8"
    )
    (transcripts / "registry.json").write_text(
        json.dumps(
            [
                {
                    "videoId": "premiere001",
                    "sourceRole": "primary_event_evidence",
                }
            ]
        ),
        encoding="utf-8",
    )
    retired = resources / "youtube-retired0001.md"
    retired.write_text("# Retired\n\nSupporting context only.\n", encoding="utf-8")
    write_static_media_fixture(root)

    failed = module.audit_corpus(
        root, phase="pre-agent", retired_ids={"retired0001"}
    )
    assert {issue["code"] for issue in failed["issues"]} == {
        "canonical_non_admitted_primary_reference",
        "segment_stream_not_admitted",
        "transcript_primary_role_not_admitted",
    }
    assert {issue.get("video_id") for issue in failed["issues"]} >= {
        "premiere001",
        "orphan00001",
    }
    assert "privateCut1" not in failed["admitted_primary_ids"]
    assert "missingCut1" not in failed["admitted_primary_ids"]

    topic.write_text(
        "- related YouTube resource; via [[youtube-premiere001]]\n"
        "- related YouTube resource; via [[youtube-orphan00001]]\n",
        encoding="utf-8",
    )
    (raw / "livestream-talk-segments.json").write_text(
        json.dumps([{"video_id": "stream00001"}]), encoding="utf-8"
    )
    (transcripts / "registry.json").write_text(
        json.dumps(
            [{"videoId": "premiere001", "sourceRole": "context_only"}]
        ),
        encoding="utf-8",
    )

    assert (
        module.audit_corpus(
            root, phase="pre-agent", retired_ids={"retired0001"}
        )["ok"]
        is True
    )


def test_primary_media_role_audit_checks_exact_livestream_segment_projection(
    tmp_path,
):
    module = load_script("audit_primary_media_roles.py")
    root = tmp_path / "project"
    talks = root / "wiki" / "talks"
    talks.mkdir(parents=True)
    manifest = [
        {
            "id": "stream00001",
            "mediaType": "event_livestream",
        },
        {
            "id": "dedicated01",
            "mediaType": "talk_recording",
            "playlistAvailability": "available",
            "videoAvailability": "public",
            "matchedTalks": ["now-dedicated"],
        },
    ]
    segments = [
        {
            "talk_slug": "current-segment",
            "video_id": "stream00001",
            "start_seconds": 11668,
            "confidence": "high",
        },
        {
            "talk_slug": "now-dedicated",
            "video_id": "stream00001",
            "start_seconds": 200,
            "confidence": "high",
        },
    ]
    (talks / "current-segment.md").write_text(
        "# Current\n", encoding="utf-8"
    )
    (talks / "now-dedicated.md").write_text(
        "# Dedicated\n\n## Livestream Segment\n"
        "- https://www.youtube.com/watch?v=stream00001&t=200s\n",
        encoding="utf-8",
    )
    (talks / "removed-segment.md").write_text(
        "# Removed\n\n## Livestream Segment\n"
        "- https://www.youtube.com/watch?v=stream00001&t=300s\n",
        encoding="utf-8",
    )

    issues = []
    module.audit_livestream_segment_projections(
        root,
        manifest=manifest,
        segments=segments,
        talks_dir=talks,
        issues=issues,
        code_prefix="canonical",
    )

    assert {
        (issue["path"], tuple(map(tuple, issue["missing_segments"])), tuple(map(tuple, issue["extra_segments"])))
        for issue in issues
    } == {
        ("wiki/talks/current-segment.md", (("stream00001", 11668),), ()),
        ("wiki/talks/now-dedicated.md", (), (("stream00001", 200),)),
        ("wiki/talks/removed-segment.md", (), (("stream00001", 300),)),
    }

    (talks / "current-segment.md").write_text(
        "# Current\n\n## Livestream Segment\n"
        "- https://www.youtube.com/watch?v=stream00001&t=11668s\n",
        encoding="utf-8",
    )
    (talks / "now-dedicated.md").write_text("# Dedicated\n", encoding="utf-8")
    (talks / "removed-segment.md").write_text("# Removed\n", encoding="utf-8")
    issues = []
    module.audit_livestream_segment_projections(
        root,
        manifest=manifest,
        segments=segments,
        talks_dir=talks,
        issues=issues,
        code_prefix="canonical",
    )

    assert issues == []


def test_primary_media_role_audit_infers_retired_ids_and_checks_static_and_agent(
    tmp_path, monkeypatch
):
    module = load_script("audit_primary_media_roles.py")
    retired_id = "retired0001"
    monkeypatch.setattr(module, "DURABLE_RETIRED_IDS", {retired_id})
    root = tmp_path / "project"
    raw = root / "raw" / "sources"
    resources = root / "wiki" / "resources"
    transcripts = root / "wiki" / "transcripts"
    for path in (raw, resources, transcripts):
        path.mkdir(parents=True)
    (raw / "official-wf26-video-manifest.json").write_text(
        json.dumps(
            {"videos": [{"id": "recording01", "mediaType": "talk_recording"}]}
        ),
        encoding="utf-8",
    )
    (raw / "livestream-talk-segments.json").write_text("[]\n", encoding="utf-8")
    (resources / f"youtube-{retired_id}.md").write_text(
        "# Retired\n\nThis is a primary event video source.\n",
        encoding="utf-8",
    )
    (transcripts / f"youtube-{retired_id}-transcript.md").write_text(
        "# Transcript\n\nSource role: primary event evidence.\n\n## Transcript\nbody\n",
        encoding="utf-8",
    )
    (transcripts / "registry.json").write_text(
        json.dumps(
            [
                {
                    "videoId": retired_id,
                    "sourceRole": "primary_event_evidence",
                }
            ]
        ),
        encoding="utf-8",
    )
    write_static_media_fixture(root)
    agent = root / "dist" / "agent"
    agent.mkdir(parents=True)
    (agent / "pages.jsonl").write_text(
        json.dumps(
            {
                "sourcePath": f"wiki/resources/youtube-{retired_id}.md",
                "sourceRoles": ["official_primary"],
                "summary": "This is a primary event video source.",
            }
        )
        + "\n",
        encoding="utf-8",
    )
    (agent / "evidence.jsonl").write_text(
        json.dumps(
            {
                "locator": f"https://www.youtube.com/watch?v={retired_id}",
                "sourceRole": "primary_event_evidence",
                "excerpt": "This is a primary event video source.",
            }
        )
        + "\n",
        encoding="utf-8",
    )

    failed = module.audit_corpus(root, phase="full")
    assert retired_id in failed["known_media_ids"]
    assert retired_id in failed["retired_ids"]
    assert {
        "canonical_non_admitted_file_primary_context",
        "static_non_admitted_file_primary_context",
        "static_non_admitted_html_primary_context",
        "static_search_non_admitted_primary_context",
        "transcript_primary_role_not_admitted",
        "agent_page_non_admitted_primary_role",
        "agent_page_non_admitted_primary_context",
        "agent_evidence_non_admitted_primary_role",
        "agent_evidence_non_admitted_primary_context",
    } <= {issue["code"] for issue in failed["issues"]}

    (resources / f"youtube-{retired_id}.md").write_text(
        "# Retired\n\nSupporting context only.\n", encoding="utf-8"
    )
    (transcripts / f"youtube-{retired_id}-transcript.md").write_text(
        "# Transcript\n\nSupporting context only.\n\n## Transcript\nbody\n",
        encoding="utf-8",
    )
    (transcripts / "registry.json").write_text(
        json.dumps([{"videoId": retired_id, "sourceRole": "context_only"}]),
        encoding="utf-8",
    )
    write_static_media_fixture(root)
    (agent / "pages.jsonl").write_text(
        json.dumps(
            {
                "sourcePath": f"wiki/resources/youtube-{retired_id}.md",
                "sourceRoles": ["context_only"],
                "summary": "Supporting context only.",
            }
        )
        + "\n",
        encoding="utf-8",
    )
    (agent / "evidence.jsonl").write_text(
        json.dumps(
            {
                "locator": f"https://www.youtube.com/watch?v={retired_id}",
                "sourceRole": "context_only",
                "excerpt": "Supporting context only.",
            }
        )
        + "\n",
        encoding="utf-8",
    )

    assert module.audit_corpus(root, phase="full")["ok"] is True


def test_primary_media_role_audit_binds_agent_claims_to_owned_media_ids(
    tmp_path, monkeypatch
):
    module = load_script("audit_primary_media_roles.py")
    monkeypatch.setattr(module, "DURABLE_RETIRED_IDS", set())
    root = tmp_path / "project"
    raw = root / "raw" / "sources"
    resources = root / "wiki" / "resources"
    transcripts = root / "wiki" / "transcripts"
    talks = root / "wiki" / "talks"
    for path in (raw, resources, transcripts, talks):
        path.mkdir(parents=True)
    (raw / "official-wf26-video-manifest.json").write_text(
        json.dumps(
            {"videos": [{"id": "recording01", "mediaType": "talk_recording"}]}
        ),
        encoding="utf-8",
    )
    (raw / "livestream-talk-segments.json").write_text("[]\n", encoding="utf-8")
    (transcripts / "registry.json").write_text("[]\n", encoding="utf-8")
    (talks / "schedule.md").write_text("# Schedule\n", encoding="utf-8")
    (resources / "livestream-inventory.md").write_text(
        "# Livestream Inventory\n", encoding="utf-8"
    )
    non_admitted = {
        "bounded0001",
        "conflict001",
        "history0001",
        "ownedbad001",
        "related0001",
    }
    for video_id in non_admitted:
        (resources / f"youtube-{video_id}.md").write_text(
            f"# {video_id}\n\nSupporting context only.\n", encoding="utf-8"
        )
    write_static_media_fixture(root)

    agent = root / "dist" / "agent"
    agent.mkdir(parents=True)
    safe_pages = [
        {
            "id": "page:schedule",
            "sourcePath": "wiki/talks/schedule.md",
            "renderedPath": "talks/schedule/",
            "sourceLayers": ["official_schedule"],
            "sourceRoles": ["primary_event_evidence"],
            "summary": (
                "Official schedule facts are primary event evidence. "
                "Related video [[youtube-related0001]] is supporting context."
            ),
        },
        {
            "id": "page:corpus",
            "sourcePath": "wiki/resources/livestream-inventory.md",
            "renderedPath": "resources/livestream-inventory/",
            "sourceRoles": ["context_only"],
            "summary": "Historical livestream inventory.",
        },
        {
            "id": "page:bounded",
            "sourcePath": "wiki/resources/youtube-bounded0001.md",
            "renderedPath": "resources/youtube-bounded0001/",
            "sourceRoles": ["context_only"],
            "summary": (
                "This is not a primary event video; it is supporting context only."
            ),
        },
    ]
    safe_evidence = [
        {
            "pageId": "page:corpus",
            "locator": "https://www.youtube.com/watch?v=history0001",
            "sourceRole": "context_only",
            "excerpt": (
                "Confirmed WF26 livestreams are primary event video sources; prior "
                "livestreams are historical/supporting context."
            ),
        },
        {
            "pageId": "page:bounded",
            "locator": "https://www.youtube.com/watch?v=bounded0001",
            "sourceRole": "context_only",
            "excerpt": (
                "This is not a primary event video; it is supporting context only."
            ),
        },
    ]
    (agent / "pages.jsonl").write_text(
        "".join(json.dumps(row) + "\n" for row in safe_pages), encoding="utf-8"
    )
    (agent / "evidence.jsonl").write_text(
        "".join(json.dumps(row) + "\n" for row in safe_evidence), encoding="utf-8"
    )

    assert module.audit_corpus(
        root, phase="full", retired_ids=non_admitted
    )["ok"] is True

    unsafe_page = {
        "id": "page:owned",
        "sourcePath": "wiki/resources/youtube-ownedbad001.md",
        "renderedPath": "resources/youtube-ownedbad001/",
        "sourceRoles": ["primary_event_evidence"],
        "summary": "This is a primary event video source.",
    }
    unsafe_evidence = {
        "pageId": "page:owned",
        "locator": "https://www.youtube.com/watch?v=ownedbad001",
        "sourceRole": "primary_event_evidence",
        "excerpt": "This is a primary event video source.",
    }
    contradictory_page = {
        "id": "page:conflict",
        "sourcePath": "wiki/resources/youtube-conflict001.md",
        "renderedPath": "resources/youtube-conflict001/",
        "sourceRoles": ["context_only"],
        "summary": (
            "This is a primary event video source. Use supporting context elsewhere."
        ),
    }
    contradictory_evidence = {
        "pageId": "page:conflict",
        "locator": "https://www.youtube.com/watch?v=conflict001",
        "sourceRole": "context_only",
        "excerpt": (
            "This is a primary event video source. Use supporting context elsewhere."
        ),
    }
    (agent / "pages.jsonl").write_text(
        "".join(
            json.dumps(row) + "\n"
            for row in [*safe_pages, unsafe_page, contradictory_page]
        ),
        encoding="utf-8",
    )
    (agent / "evidence.jsonl").write_text(
        "".join(
            json.dumps(row) + "\n"
            for row in [*safe_evidence, unsafe_evidence, contradictory_evidence]
        ),
        encoding="utf-8",
    )

    failed = module.audit_corpus(root, phase="full", retired_ids=non_admitted)
    assert {
        "agent_page_non_admitted_primary_role",
        "agent_page_non_admitted_primary_context",
        "agent_evidence_non_admitted_primary_role",
        "agent_evidence_non_admitted_primary_context",
    } <= {issue["code"] for issue in failed["issues"]}
    context_issues = {
        (issue["code"], issue.get("video_id")) for issue in failed["issues"]
    }
    assert (
        "agent_page_non_admitted_primary_context",
        "conflict001",
    ) in context_issues
    assert (
        "agent_evidence_non_admitted_primary_context",
        "conflict001",
    ) in context_issues


def test_primary_media_id_parser_does_not_treat_transcript_directory_as_id():
    module = load_script("audit_primary_media_roles.py")

    assert module.extract_media_ids(
        "raw/sources/youtube-transcripts/recording01.txt",
        {"recording01", "transcripts"},
    ) == {"recording01"}


def test_primary_media_role_audit_detects_topic_slide_session_projection_drift(
    tmp_path,
):
    module = load_script("audit_primary_media_roles.py")
    root = tmp_path / "project"
    topics = root / "wiki" / "topics"
    slides = root / "wiki" / "slides"
    topics.mkdir(parents=True)
    slides.mkdir(parents=True)
    (slides / "youtube-partvideo01-slides.md").write_text(
        "# Part deck\n\n"
        "## Related Scheduled Sessions\n"
        "- [[part-1]] — Part 1\n\n"
        "## Extracted Slides\nOCR\n",
        encoding="utf-8",
    )
    (slides / "youtube-othervideo1-slides.md").write_text(
        "# Other deck\n\n"
        "## Related Scheduled Sessions\n"
        "- [[other-talk]] — Independent Deck Talk\n\n"
        "## Extracted Slides\nOCR\n",
        encoding="utf-8",
    )
    topic = topics / "topic.md"
    topic.write_text(
        "# Topic\n\n"
        "## Slide-Derived Scheduled Session Signals\n"
        "- [[part-1]] — Part 1\n"
        "- [[stale-talk]] — stale owned edge\n\n"
        "## Slide-Derived Supporting Decks\n"
        "- [[youtube-partvideo01-slides]] — part deck\n"
        "- [[youtube-othervideo1-slides]] — other deck\n\n"
        "## Connections\n"
        "- [[stale-talk]] — independent manual edge remains out of scope\n",
        encoding="utf-8",
    )

    issues = []
    module.audit_topic_slide_session_projections(
        root,
        topics_dir=topics,
        slides_dir=slides,
        issues=issues,
        code_prefix="canonical",
    )

    assert issues == [
        {
            "code": "canonical_topic_slide_session_projection_mismatch",
            "path": "wiki/topics/topic.md",
            "extra_talks": ["stale-talk"],
            "missing_talks": ["other-talk"],
        }
    ]

    topic.write_text(
        topic.read_text(encoding="utf-8").replace(
            "- [[stale-talk]] — stale owned edge",
            "- [[other-talk]] — Independent Deck Talk",
            1,
        ),
        encoding="utf-8",
    )
    issues = []
    module.audit_topic_slide_session_projections(
        root,
        topics_dir=topics,
        slides_dir=slides,
        issues=issues,
        code_prefix="canonical",
    )
    assert issues == []
    assert "independent manual edge" in topic.read_text(encoding="utf-8")

    orphan = topics / "orphan.md"
    orphan.write_text(
        "# Orphan\n\n"
        "## Slide-Derived Scheduled Session Signals\n"
        "- [[stale-talk]] — stale generator-owned edge\n\n"
        "## Connections\n"
        "- [[manual-only]] — independent manual edge\n",
        encoding="utf-8",
    )
    issues = []
    module.audit_topic_slide_session_projections(
        root,
        topics_dir=topics,
        slides_dir=slides,
        issues=issues,
        code_prefix="canonical",
    )
    assert issues == [
        {
            "code": "canonical_topic_slide_session_projection_mismatch",
            "path": "wiki/topics/orphan.md",
            "extra_talks": ["stale-talk"],
            "missing_talks": [],
        }
    ]
