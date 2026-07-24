import importlib.util
import json
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "generate_talk_synthesis.py"
SPEC = importlib.util.spec_from_file_location("generate_talk_synthesis_test", SCRIPT)
SYNTHESIS = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(SYNTHESIS)


EVIDENCE = (
    "The verifier checks every proposed action against a versioned policy before "
    "the agent can change production state."
)
SECOND_EVIDENCE = (
    "Teams should preserve the trace, the proposed diff, and the reviewer decision "
    "so failures can improve the next evaluation."
)
THIRD_EVIDENCE = (
    "A bounded credential expires after one run and prevents unrelated tools from "
    "inheriting authority they were never granted."
)
TRANSCRIPT = " ".join(
    [
        "Welcome to the session and thank you for joining us.",
        EVIDENCE,
        SECOND_EVIDENCE,
        THIRD_EVIDENCE,
        (
            "The speaker calls this evidence-gated execution and demonstrates it "
            "with Codex, an explicit approval policy, and a replayable evaluation."
        ),
    ]
    * 5
)


def valid_payload() -> dict:
    return {
        "summary": (
            "The talk presents evidence-gated execution as an architecture for "
            "controlling agents that can alter production systems. It separates "
            "proposed action from authorization, evaluates the proposal against a "
            "versioned policy, and preserves the resulting trace and reviewer "
            "decision. The practical consequence is a replayable control loop in "
            "which narrow credentials limit blast radius while failures become "
            "inputs to later evaluations."
        ),
        "takeaways": [
            {"text": "Gate proposed actions with an explicit versioned policy.", "evidenceExcerpt": EVIDENCE},
            {"text": "Keep traces and review decisions as evaluation evidence.", "evidenceExcerpt": SECOND_EVIDENCE},
            {"text": "Use per-run credentials to constrain inherited authority.", "evidenceExcerpt": THIRD_EVIDENCE},
        ],
        "claims": [
            {
                "text": "A versioned policy can prevent an agent from directly changing production state.",
                "evidenceExcerpt": EVIDENCE,
                "support": "explicit",
            },
            {
                "text": "Replayable traces let observed failures improve later evaluations.",
                "evidenceExcerpt": SECOND_EVIDENCE,
                "support": "strong",
            },
        ],
        "topics": [
            {
                "name": "Agent authorization",
                "description": "Policy evaluation that separates a proposed agent action from permission to execute it.",
                "evidenceExcerpt": EVIDENCE,
            },
            {
                "name": "Evaluation evidence",
                "description": "Traces, diffs, and reviewer decisions retained to make agent failures replayable.",
                "evidenceExcerpt": SECOND_EVIDENCE,
            },
        ],
        "tools": [
            {
                "name": "Codex",
                "description": "The named agent used in the talk's evidence-gated execution demonstration.",
                "evidenceExcerpt": (
                    "The speaker calls this evidence-gated execution and demonstrates "
                    "it with Codex, an explicit approval policy, and a replayable evaluation."
                ),
            }
        ],
        "methods": [
            {
                "name": "Evidence-gated execution",
                "description": "A reusable control loop that evaluates proposed actions before execution and retains the decision evidence.",
                "evidenceExcerpt": EVIDENCE,
            }
        ],
        "questions": [
            {
                "question": "Which evidence should be mandatory before an agent may change production?",
                "whyItMatters": "The control only works when policy authors define the trace and review evidence needed for authorization.",
                "evidenceExcerpt": SECOND_EVIDENCE,
            }
        ],
        "methodNotes": (
            "The digest distinguishes attributed speaker claims from independent "
            "verification and binds every derived item to transcript wording."
        ),
    }


def configure_project(tmp_path: Path, monkeypatch) -> tuple[Path, Path, Path]:
    root = tmp_path / "project"
    wiki = root / "wiki"
    raw = root / "raw" / "sources"
    transcript_dir = raw / "youtube-transcripts"
    for directory in (
        wiki / "talks",
        wiki / "resources",
        wiki / "topics",
        wiki / "tools",
        wiki / "patterns",
        wiki / "questions",
        wiki / "highlights",
        wiki / "claims",
        transcript_dir,
    ):
        directory.mkdir(parents=True, exist_ok=True)
    manifest = raw / "official-wf26-video-manifest.json"
    monkeypatch.setattr(SYNTHESIS, "ROOT", root)
    monkeypatch.setattr(SYNTHESIS, "WIKI", wiki)
    monkeypatch.setattr(SYNTHESIS, "RAW", raw)
    monkeypatch.setattr(SYNTHESIS, "OFFICIAL_VIDEO_MANIFEST", manifest)
    monkeypatch.setattr(SYNTHESIS, "TRANSCRIPT_DIRS", [transcript_dir])
    return root, wiki, raw


def write_talk_fixture(wiki: Path, raw: Path) -> tuple[str, str]:
    talk_id = "2026-07-01-example-evidence-gated-execution"
    video_id = "EXAMPLE0001"
    (wiki / "talks" / f"{talk_id}.md").write_text(
        "---\n"
        'title: "Evidence-Gated Execution"\n'
        'speakers: ["Example Speaker"]\n'
        "---\n"
        "# Evidence-Gated Execution\n\n"
        "## Conference Context\n"
        "- Official schedule fixture.\n\n"
        "## Session Description\n"
        "A session about authorization and evaluation evidence.\n\n"
        "## Synthesis\n"
        "### Synthesized Breakdown\n"
        "Hello and welcome to the session.\n\n"
        "## Media Evidence\n"
        "Pending.\n\n"
        "## Evidence Graph\n"
        "Pending.\n",
        encoding="utf-8",
    )
    (raw / "youtube-transcripts" / f"{video_id}.txt").write_text(
        TRANSCRIPT,
        encoding="utf-8",
    )
    (raw / "official-wf26-video-manifest.json").write_text(
        json.dumps(
            {
                "videos": [
                    {
                        "id": video_id,
                        "title": "Evidence-Gated Execution",
                        "mediaType": "talk_recording",
                        "videoAvailability": "public",
                        "playlistAvailability": "available",
                        "matchedTalks": [talk_id],
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    return talk_id, video_id


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


def test_official_recording_map_fails_closed_on_both_availability_fields(
    tmp_path,
    monkeypatch,
) -> None:
    manifest = tmp_path / "manifest.json"
    manifest.write_text(
        """
        {"videos": [
          {"id": "PLAYABLE001", "mediaType": "talk_recording",
           "videoAvailability": "public", "playlistAvailability": "available",
           "matchedTalks": ["valid-talk"]},
          {"id": "PRIVATE0001", "mediaType": "talk_recording",
           "videoAvailability": "private", "playlistAvailability": "available",
           "matchedTalks": ["private-talk"]},
          {"id": "PLAYLISTBAD", "mediaType": "talk_recording",
           "videoAvailability": "public", "playlistAvailability": "unavailable",
           "matchedTalks": ["unavailable-talk"]}
        ]}
        """,
        encoding="utf-8",
    )
    monkeypatch.setattr(SYNTHESIS, "OFFICIAL_VIDEO_MANIFEST", manifest)

    assert SYNTHESIS.official_recording_ids_by_talk() == {
        "valid-talk": ["PLAYABLE001"]
    }


def test_semantic_contract_accepts_exact_evidence_and_rejects_invention() -> None:
    payload = valid_payload()
    SYNTHESIS.validate_payload(payload, TRANSCRIPT)

    payload["topics"][0]["evidenceExcerpt"] = (
        "This sentence was never present in the source transcript at all."
    )
    try:
        SYNTHESIS.validate_payload(payload, TRANSCRIPT)
    except ValueError as error:
        assert "not verbatim transcript evidence" in str(error)
    else:
        raise AssertionError("invented evidence must fail the semantic contract")


def test_semantic_contract_rejects_greeting_summary() -> None:
    payload = valid_payload()
    payload["summary"] = (
        "Hello everyone. Thank you for joining this very exciting conference "
        "session where we will discuss several interesting things in detail. "
        "Welcome to the stage and please enjoy this long presentation together "
        "with all of the other attendees who are here today."
    )
    try:
        SYNTHESIS.validate_payload(payload, TRANSCRIPT)
    except ValueError as error:
        assert "greeting" in str(error)
    else:
        raise AssertionError("greeting-led summaries must fail closed")


def test_cross_topic_validation_rejects_thin_cluster_but_keeps_valid_corpus() -> None:
    candidates = [
        {
            "candidateId": f"T{index:04d}",
            "talkId": f"talk-{index}",
        }
        for index in range(1, 18)
    ]
    candidates.append({"candidateId": "T0018", "talkId": "talk-1"})
    raw_clusters = []
    for index in range(8):
        first = index * 2 + 1
        raw_clusters.append(
            {
                "canonicalTopic": f"Valid topic {index}",
                "synthesis": (
                    "Two different talks describe the same reusable engineering "
                    "idea. Their descriptions also expose a meaningful variation "
                    "in how that shared idea is applied."
                ),
                "preferredExistingTopicSlug": "",
                "memberIds": [f"T{first:04d}", f"T{first + 1:04d}"],
            }
        )
    raw_clusters.append(
        {
            "canonicalTopic": "Thin same-talk topic",
            "synthesis": (
                "These two candidates came from only one scheduled talk. They "
                "must not be promoted as cross-talk conference synthesis."
            ),
            "preferredExistingTopicSlug": "",
            "memberIds": ["T0001", "T0018"],
        }
    )

    result = SYNTHESIS.validate_cross_topic_payload(
        {"clusters": raw_clusters},
        candidates,
        [],
    )

    assert len(result["clusters"]) == 8
    assert result["rejectedClusters"] == [
        {
            "canonicalTopic": "Thin same-talk topic",
            "reason": "fewer_than_two_distinct_talks",
            "memberIds": ["T0018"],
        }
    ]


def test_build_jobs_requires_a_usable_transcript(tmp_path, monkeypatch) -> None:
    _root, wiki, raw = configure_project(tmp_path, monkeypatch)
    talk_id, video_id = write_talk_fixture(wiki, raw)
    (raw / "youtube-transcripts" / f"{video_id}.txt").unlink()

    jobs, failures, selected = SYNTHESIS.build_jobs(
        model="test-model",
        max_transcript_chars=50_000,
    )

    assert jobs == []
    assert selected == {talk_id}
    assert failures == [
        f"matched playable recording has no usable transcript: {video_id} -> {talk_id}"
    ]


def test_generated_semantic_pages_include_required_article_contract_sections() -> None:
    evidence = "- [[example-talk]]\n  - Transcript: [[youtube-EXAMPLE0001-transcript]]"
    required = {
        "topics": ("Significance", "Applied Use", "Connections", "Evidence Graph"),
        "tools": (),
        "patterns": ("Pattern", "When To Use", "Implementation Moves", "Source Evidence"),
        "questions": ("Context", "Working Answer", "Evidence", "Next Questions"),
    }

    for category, headings in required.items():
        rendered = SYNTHESIS.new_generated_page(
            title="Example",
            category=category,
            overview="An evidence-bound example derived from two official talk transcripts.",
            evidence_section=evidence,
        )
        assert "## Transcript Digest Evidence" in rendered
        assert "## Evidence Boundary" in rendered
        for heading in headings:
            assert f"## {heading}" in rendered


def test_main_materializes_semantic_layers_and_reuses_bound_cache(
    tmp_path,
    monkeypatch,
) -> None:
    root, wiki, raw = configure_project(tmp_path, monkeypatch)
    talk_id, video_id = write_talk_fixture(wiki, raw)
    question_slug = (
        "which-evidence-should-be-mandatory-before-an-agent-may-change-production"
    )
    (wiki / "patterns" / "evidence-gated-execution.md").write_text(
        "# Evidence-gated execution\n",
        encoding="utf-8",
    )
    (wiki / "questions" / f"{question_slug}.md").write_text(
        "# Which evidence should be mandatory before an agent may change production?\n",
        encoding="utf-8",
    )
    (wiki / "tools" / "codex.md").write_text(
        "# Codex\n",
        encoding="utf-8",
    )
    calls = []

    def synthesize(job, *, timeout_seconds):
        calls.append((job["video_id"], timeout_seconds))
        return valid_payload()

    monkeypatch.setattr(SYNTHESIS, "run_codex_digest", synthesize)
    monkeypatch.setattr(
        SYNTHESIS,
        "obtain_cross_topic_synthesis",
        lambda *_args, **_kwargs: (
            {
                "payload": {
                    "clusters": [
                        {
                            "canonicalTopic": "Agent authorization",
                            "synthesis": (
                                "The candidates describe policy evaluation that "
                                "separates proposed action from authority to execute. "
                                "They also connect authorization to retained evidence."
                            ),
                            "preferredExistingTopicSlug": "",
                            "memberIds": ["T0001", "T0002"],
                        }
                    ]
                }
            },
            False,
        ),
    )
    assert (
        SYNTHESIS.main(
            [
                "--all",
                "--model",
                "test-model",
                "--workers",
                "1",
                "--timeout-seconds",
                "60",
                "--max-transcript-chars",
                "50000",
            ]
        )
        == 0
    )
    assert calls == [(video_id, 60)]

    talk = (wiki / "talks" / f"{talk_id}.md").read_text()
    assert "## Synthesis" in talk
    assert "### Transcript-Backed Summary" in talk
    assert "Hello and welcome to the session." not in talk
    assert "[[agent-authorization|Agent authorization]]" in talk
    assert "[[codex|Codex]]" in talk
    assert "[[evidence-gated-execution|Evidence-gated execution]]" in talk
    assert "### Semantic Digestion Status" in talk
    assert (wiki / "topics" / "agent-authorization.md").is_file()
    assert (wiki / "tools" / "codex.md").is_file()
    assert (wiki / "patterns" / "evidence-gated-execution.md").is_file()
    assert (
        wiki
        / "questions"
        / f"{question_slug}.md"
    ).is_file()
    assert (wiki / "highlights" / f"transcript-{talk_id}.md").is_file()
    assert (wiki / "claims" / f"transcript-{talk_id}.md").is_file()
    cache = (
        wiki
        / "resources"
        / "talk-digests"
        / f"{video_id}--{talk_id}.json"
    )
    envelope = json.loads(cache.read_text())
    assert envelope["inputSha256"].startswith("sha256:")
    assert envelope["payloadSha256"].startswith("sha256:")
    assert envelope["model"] == "test-model"
    assert "OPENAI_API_KEY" not in envelope

    before = {
        path.relative_to(root): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }

    def no_second_call(*_args, **_kwargs):
        raise AssertionError("valid content-addressed cache should be reused")

    monkeypatch.setattr(SYNTHESIS, "run_codex_digest", no_second_call)
    assert (
        SYNTHESIS.main(
            [
                "--all",
                "--model",
                "test-model",
                "--workers",
                "1",
                "--timeout-seconds",
                "60",
                "--max-transcript-chars",
                "50000",
            ]
        )
        == 0
    )
    after = {
        path.relative_to(root): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }
    assert after == before


def test_main_fails_without_sentence_or_keyword_fallback(
    tmp_path,
    monkeypatch,
) -> None:
    _root, wiki, raw = configure_project(tmp_path, monkeypatch)
    talk_id, _video_id = write_talk_fixture(wiki, raw)
    before = (wiki / "talks" / f"{talk_id}.md").read_text()

    def fail(_job, *, timeout_seconds):
        raise RuntimeError(f"model unavailable after {timeout_seconds}s")

    monkeypatch.setattr(SYNTHESIS, "run_codex_digest", fail)
    result = SYNTHESIS.main(
        [
            "--all",
            "--model",
            "test-model",
            "--workers",
            "1",
            "--timeout-seconds",
            "60",
            "--max-transcript-chars",
            "50000",
        ]
    )

    assert result == 1
    assert (wiki / "talks" / f"{talk_id}.md").read_text() == before
    assert not (wiki / "resources" / "talk-digests").exists()
