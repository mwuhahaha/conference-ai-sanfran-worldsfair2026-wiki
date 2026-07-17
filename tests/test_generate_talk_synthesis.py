import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "generate_talk_synthesis.py"
SPEC = importlib.util.spec_from_file_location("generate_talk_synthesis_test", SCRIPT)
SYNTHESIS = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(SYNTHESIS)


def test_schedule_fallback_uses_description_without_embedded_headings() -> None:
    markdown = (
        "# Example Talk\n\n"
        "## Conference Context\n"
        "- Date/time: 2026-07-01\n\n"
        "## Session Description\n"
        "The session explains a bounded agent workflow. "
        "It demonstrates a verification gate.\n\n"
        "## Media Evidence\n"
        "No recording yet.\n"
    )

    description = SYNTHESIS.section_body(markdown, "Session Description")
    summary = SYNTHESIS.first_sentences(description, 4)

    assert summary == (
        "The session explains a bounded agent workflow. "
        "It demonstrates a verification gate."
    )
    assert "# Example Talk" not in summary
    assert "## Conference Context" not in summary


def test_first_sentences_ignores_fenced_headings() -> None:
    text = "```bash\n# comment\n```\nA real sentence. Another real sentence."

    assert (
        SYNTHESIS.first_sentences(text, 2) == "A real sentence. Another real sentence."
    )


def test_curated_synopsis_extracts_ai_native_company_operating_model() -> None:
    transcript = (
        "A skill file is an employee. Work moves between latent space and "
        "deterministic space. A company brain is the library plus the librarian. "
        "The primitive is memory plus hygiene, with provenance and contradiction "
        "checks. Never do one-off work; skillify it."
    )

    synopsis = SYNTHESIS.curated_synopsis("What Do We Build Now?", transcript)

    assert "how work is wired" in synopsis
    assert "latent space" in synopsis
    assert "deterministic systems" in synopsis
    assert "provenance" in synopsis
    assert "reusable skills" in synopsis


def test_dedicated_cut_drives_synthesis_and_livestream_remains_labeled_context(
    tmp_path,
    monkeypatch,
) -> None:
    root = tmp_path / "project"
    wiki = root / "wiki"
    cut_dir = root / "raw" / "sources" / "youtube-transcripts"
    livestream_dir = root / "raw" / "sources" / "youtube-livestream-transcripts"
    for directory in (wiki / "topics", wiki / "tools", cut_dir, livestream_dir):
        directory.mkdir(parents=True, exist_ok=True)
    for topic in ("agent-memory", "mcp", "ai-sandboxes"):
        (wiki / "topics" / f"{topic}.md").write_text(f"# {topic}\n")

    cut_id = "CUTVIDEO001"
    livestream_id = "LIVESTRM001"
    (cut_dir / f"{cut_id}.txt").write_text(
        "Dedicated cut opening. The company brain depends on context engineering "
        "and memory hygiene. This is the cut conclusion."
    )
    (livestream_dir / f"{livestream_id}.txt").write_text(
        "Livestream boilerplate. MCP sandbox authentication fills the broad stream."
    )
    monkeypatch.setattr(SYNTHESIS, "ROOT", root)
    monkeypatch.setattr(SYNTHESIS, "WIKI", wiki)
    monkeypatch.setattr(
        SYNTHESIS,
        "TRANSCRIPT_DIRS",
        [cut_dir, livestream_dir],
    )
    talk = wiki / "talks" / "example-talk.md"
    markdown = (
        "---\n"
        'title: "Example Talk"\n'
        "---\n"
        "# Example Talk\n\n"
        "## Session Description\n"
        "A bounded official description.\n\n"
        "## Topics Covered\n"
        "- [[mcp]]\n"
        f"- [[youtube-{livestream_id}-transcript]]\n"
        f"- [[youtube-{cut_id}-transcript]]\n"
    )

    heading, section, _concepts = SYNTHESIS.section_for(
        talk,
        markdown,
        {},
        {},
        {talk.stem: [cut_id]},
    )

    assert heading == "Synthesis"
    assert "Dedicated cut opening." in section
    assert (
        "Livestream boilerplate."
        not in section.split("### Speaker And Company Context", 1)[0]
    )
    assert "- [[agent-memory]]" in section
    assert "- [[mcp]]" not in section
    assert "- [[ai-sandboxes]]" not in section
    assert "dedicated official recording transcript" in section
    assert "official livestream context transcript" in section
    assert section.index(f"youtube-{cut_id}-transcript") < section.index(
        f"youtube-{livestream_id}-transcript"
    )


def test_unmatched_livestream_cannot_drive_session_synthesis(
    tmp_path,
    monkeypatch,
) -> None:
    root = tmp_path / "project"
    wiki = root / "wiki"
    livestream_dir = root / "raw" / "sources" / "youtube-livestream-transcripts"
    for directory in (wiki / "topics", wiki / "tools", livestream_dir):
        directory.mkdir(parents=True, exist_ok=True)
    for topic in ("agent-memory", "agentic-web", "mcp"):
        (wiki / "topics" / f"{topic}.md").write_text(f"# {topic}\n")

    livestream_id = "LIVESTRM001"
    (livestream_dir / f"{livestream_id}.txt").write_text(
        "Unrelated keynote material about memory hygiene and context graphs."
    )
    monkeypatch.setattr(SYNTHESIS, "ROOT", root)
    monkeypatch.setattr(SYNTHESIS, "WIKI", wiki)
    monkeypatch.setattr(SYNTHESIS, "TRANSCRIPT_DIRS", [livestream_dir])
    monkeypatch.setattr(SYNTHESIS, "broad_event_video_ids", lambda: {livestream_id})
    talk = wiki / "talks" / "browser-talk.md"
    markdown = (
        "---\n"
        'title: "Browser Talk"\n'
        "---\n"
        "# Browser Talk\n\n"
        "## Session Description\n"
        "Programmatic browser automation through MCP makes the agentic web repeatable.\n\n"
        f"## Recording Search Status\n- Broad stream [[youtube-{livestream_id}]].\n"
    )

    heading, section, _concepts = SYNTHESIS.section_for(
        talk,
        markdown,
        {},
        {},
        {},
    )

    assert heading == "Synthesis"
    assert "Programmatic browser automation" in section
    assert "Unrelated keynote material" not in section
    assert "youtube-LIVESTRM001-transcript" not in section
    assert "- [[agent-memory]]" not in section
    assert "- [[ai-sandboxes]]" not in section
    assert "- [[agentic-web]]" in section
    assert "- [[mcp]]" in section
