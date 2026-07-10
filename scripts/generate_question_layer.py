#!/usr/bin/env python3
"""Generate the first-pass AIE questions layer."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"


QUESTIONS = [
    {
        "slug": "how-should-coding-agents-be-evaluated-before-production-use",
        "title": "How should coding agents be evaluated before production use?",
        "summary": "Coding agents need evaluation gates before they can safely change code, trigger workflows, or influence production systems.",
        "sources": [
            ("agent-evaluations", "Topic synthesis"),
            ("coding-agents", "Topic synthesis"),
            ("software-factories", "Topic synthesis"),
            ("claude-agent-sdk", "Tool inventory"),
            ("arize", "Tool inventory"),
            ("braintrust", "Tool inventory"),
            ("2026-06-29-laurie-voss-from-vibes-to-production-evaluating-and-shipping-ai-agents-that-work-101", "Official schedule"),
            ("2026-06-30-philipp-schmid-don-t-ship-skills-without-evals", "Official schedule"),
            ("youtube-Xfl50508LZM-slides", "Slide/OCR evidence"),
            ("youtube-bk0TmxoZlUY-slides", "Slide/OCR evidence"),
        ],
    },
    {
        "slug": "what-makes-a-codebase-agent-ready",
        "title": "What makes a codebase agent-ready?",
        "summary": "Agent-ready codebases need navigable context, clear ownership boundaries, runnable checks, useful traces, and interfaces that agents can operate without guessing.",
        "sources": [
            ("coding-agents", "Topic synthesis"),
            ("software-factories", "Topic synthesis"),
            ("codex", "Tool inventory"),
            ("sourcegraph-amp", "Tool inventory"),
            ("cursor", "Tool inventory"),
            ("2026-06-30-peter-werry-how-to-generate-mergeable-code-with-a-context-engine", "Official schedule"),
            ("2026-06-30-ajay-prakash-500-skills-zero-fine-tuning-linkedin-s-playbook-for-ai-agents-that-actually-know-your-codebase", "Official schedule"),
            ("2026-06-29-aditya-khandelwal-agents-codebases-and-teams-what-it-actually-takes-to-ship-together", "Official schedule"),
            ("2026-06-29-owen-halpert-give-your-coding-agents-the-power-of-turbogrep", "Official schedule"),
            ("2026-07-01-anirban-chatterjee-guide-verify-solve-the-engineering-discipline-agentic-development-demands", "Official schedule"),
            ("youtube-5ID22ACI7IM-slides", "Slide/OCR evidence"),
            ("youtube-ShuJ_CN6zr4-slides", "Slide/OCR evidence"),
            ("youtube-F_RyElT_gJk-slides", "Slide/OCR evidence"),
        ],
    },
    {
        "slug": "when-do-software-factories-outperform-individual-ide-agents",
        "title": "When do software factories outperform individual IDE agents?",
        "summary": "The software-factory question asks when agentic work should move from single-developer tools into orchestrated pipelines with review, deployment, memory, and organizational controls.",
        "sources": [
            ("software-factories", "Topic synthesis"),
            ("coding-agents", "Topic synthesis"),
            ("agent-evaluations", "Topic synthesis"),
            ("worldsfair-2026-livestreams", "YouTube resource"),
            ("youtube-htM02KMNZnk", "YouTube resource"),
            ("youtube-htM02KMNZnk-slides", "Slide/OCR evidence"),
            ("2026-06-30-suraj-gupta-warp-building-self-improving-agent-software-factories", "Official schedule"),
            ("2026-06-29-zach-lloyd-self-improving-software-factories-the-new-open-source-model", "Official schedule"),
            ("2026-06-29-tereza-t-kov-rise-of-the-software-factory", "Official schedule"),
        ],
    },
    {
        "slug": "what-context-graph-and-memory-architecture-is-practical",
        "title": "What context graph and memory architecture is practical?",
        "summary": "The conference graph repeatedly asks how agents should retrieve, preserve, update, and reason over context without stuffing everything into a prompt.",
        "sources": [
            ("agent-memory", "Topic synthesis"),
            ("agentic-search", "Topic synthesis"),
            ("autoresearch", "Topic synthesis"),
            ("neo4j", "Tool inventory"),
            ("zep", "Tool inventory"),
            ("graphrag", "Tool inventory"),
            ("2026-06-29-louis-fran-ois-bouchard-context-engineering-in-2026-compaction-memory-and-cost", "Official schedule"),
            ("2026-06-30-gil-feig-why-your-company-needs-a-context-graph-and-how-to-build-it", "Official schedule"),
            ("2026-06-30-prukalpa-sankar-wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents", "Official schedule"),
            ("2026-06-30-stefania-druga-memory-harnesses-for-long-running-research-agents", "Official schedule"),
            ("youtube-4sX_He5c4sI", "YouTube resource"),
            ("youtube-4sX_He5c4sI-slides", "Slide/OCR evidence"),
            ("youtube-B9h9ovW5H9U-slides", "Slide/OCR evidence"),
        ],
    },
    {
        "slug": "what-security-boundaries-should-agents-have",
        "title": "What security boundaries should agents have?",
        "summary": "Agents that can use tools, browse, write code, and affect production need boundaries around identity, permissions, execution, audit, and rollback.",
        "sources": [
            ("agent-security", "Topic synthesis"),
            ("ai-sandboxes", "Topic synthesis"),
            ("mcp", "Topic synthesis"),
            ("arrakis", "Tool inventory"),
            ("docker", "Tool inventory"),
            ("tailscale-aperture", "Tool inventory"),
            ("2026-06-29-javier-garza-ai-security-engineer-foundations-certificate", "Official schedule"),
            ("2026-06-29-moritz-johner-we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night", "Official schedule"),
            ("2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale", "Official schedule"),
            ("2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert", "Official schedule"),
            ("youtube-wsFd22SL1s8-slides", "Slide/OCR evidence"),
            ("youtube-BM2JX9hqsVQ-slides", "Slide/OCR evidence"),
            ("youtube-JhJKgRAmfIU-slides", "Slide/OCR evidence"),
        ],
    },
    {
        "slug": "what-latency-and-cost-budget-is-right-for-agent-systems",
        "title": "What latency and cost budget is right for agent systems?",
        "summary": "Agent systems turn inference into a product constraint: latency, throughput, routing, local versus hosted execution, and token cost shape what can be shipped.",
        "sources": [
            ("inference-engineering", "Topic synthesis"),
            ("vllm", "Tool inventory"),
            ("modal", "Tool inventory"),
            ("openrouter", "Tool inventory"),
            ("tokenspeed", "Tool inventory"),
            ("2026-06-29-charles-frye-what-is-an-inference-engine-anyway", "Official schedule"),
            ("2026-06-29-du-an-lightfoot-agents-that-own-their-inference-building-production-ai-agents-on-dedicated-gpus", "Official schedule"),
            ("2026-07-01-qianru-lao-routing-llm-inference-in-production-from-engine-signals-to-policy", "Official schedule"),
            ("2026-06-30-jesse-hall-latency-is-a-budget-humanlike-is-the-goal", "Official schedule"),
            ("2026-07-01-sujee-maniyam-optimizing-open-models-for-production-grade-inference", "Official schedule"),
            ("youtube-DeFF3J8T5Pk-slides", "Slide/OCR evidence"),
            ("youtube-ESbWpPT_9-o-slides", "Slide/OCR evidence"),
            ("youtube-sRpqPgKeXNk-slides", "Slide/OCR evidence"),
        ],
    },
]


def yaml_list(items: list[str]) -> str:
    return "[" + ", ".join(json.dumps(str(item), ensure_ascii=False) for item in items) + "]"


def frontmatter(fields: dict) -> str:
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, list):
            lines.append(f"{key}: {yaml_list(value)}")
        elif value is None:
            continue
        else:
            lines.append(f"{key}: {json.dumps(str(value), ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def existing_sources(sources: list[tuple[str, str]]) -> list[tuple[str, str]]:
    stems = {path.stem for path in WIKI.rglob("*.md")}
    return [(slug, label) for slug, label in sources if slug in stems]


def render_question(question: dict) -> str:
    sources = existing_sources(question["sources"])
    labels = sorted({label for _, label in sources})
    status = "active" if len(sources) >= 3 else "provisional"
    lines = [
        frontmatter(
            {
                "title": question["title"],
                "category": "questions",
                "status": status,
                "sourceLabels": labels,
            }
        ),
        f"# {question['title']}",
        "",
        "## Why This Question Matters",
        question["summary"],
        "",
        "## Current Working Answer",
        "This page is a first-pass research question, not a final recommendation. Use the linked evidence to refine the answer as more exact session recordings, transcripts, and reviewed slide readings become available.",
        "",
        "## Source Evidence",
    ]
    for slug, label in sources:
        lines.append(f"- [[{slug}]] — {label}")
    if len(sources) < 3:
        lines.extend(["", "## Evidence Status", "Provisional: fewer than three local source pages are currently linked."])
    lines.extend(
        [
            "",
            "## Follow-Up",
            "- Extract specific claims from the linked source pages.",
            "- Separate official schedule evidence from supporting YouTube, transcript, and OCR evidence.",
            "- Convert stable answers into playbooks, harnesses, or evaluations where appropriate.",
        ]
    )
    return "\n".join(lines)


def render_index(records: list[dict]) -> str:
    lines = [
        frontmatter({"title": "Questions", "category": "questions"}),
        "# Questions",
        "",
        "This category tracks open research and implementation questions raised by AI Engineer World's Fair 2026.",
        "",
        "Each question links to source evidence and should remain provisional until the answer is grounded in reviewed talks, transcripts, slide evidence, or public supporting sources.",
        "",
        "## Question Index",
    ]
    for record in records:
        lines.append(f"- [[{record['id']}]] — {record['title']} ({record['status']}, {record['sourceCount']} source links)")
    return "\n".join(lines)


def main() -> int:
    records = []
    for question in QUESTIONS:
        sources = existing_sources(question["sources"])
        status = "active" if len(sources) >= 3 else "provisional"
        path = WIKI / "questions" / f"{question['slug']}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_question(question).rstrip() + "\n")
        records.append(
            {
                "id": question["slug"],
                "title": question["title"],
                "path": f"wiki/questions/{question['slug']}.md",
                "status": status,
                "sourceCount": len(sources),
            }
        )
    records.sort(key=lambda item: item["title"].lower())
    (WIKI / "questions" / "registry.json").write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n")
    index_text = render_index(records).rstrip() + "\n"
    (WIKI / "questions" / "index.md").write_text(index_text)
    (WIKI / "questions" / "questions.md").write_text(index_text)
    print(json.dumps({"question_pages": len(records)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
