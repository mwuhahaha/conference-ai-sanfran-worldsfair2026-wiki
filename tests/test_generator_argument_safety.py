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
    manifest.write_text(
        json.dumps(
            {
                "videos": [
                    {"id": "recording01", "mediaType": "talk_recording"},
                    {"id": "premiere001", "mediaType": "scheduled_premiere"},
                    {"id": "private0001", "mediaType": "unavailable_playlist_item"},
                ]
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(module, "OFFICIAL_VIDEO_MANIFEST", manifest)
    monkeypatch.setattr(module, "confirmed_event_cut_ids", lambda: set())

    assert module.official_wf_cut_ids() == {"recording01"}
    assert module.official_wf_premiere_ids() == {"premiere001"}
    assert module.official_wf_unavailable_ids() == {"private0001"}
