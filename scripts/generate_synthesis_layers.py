#!/usr/bin/env python3
"""Generate Worldsfair synthesis layers and private quality-gate receipts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
PRIVATE_QUALITY_DIR = ROOT / ".ops" / "state" / "cache" / "wiki-maker" / "private-quality"
PRIVATE_POLICY_PROFILE = ROOT / ".ops" / "state" / "cache" / "wiki-maker" / "private-policy.json"
INTERNAL_SYNTHESIS_DIR = ROOT / ".ops" / "state" / "cache" / "synthesis-layers"


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-") or "untitled"


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


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def wiki_stems() -> set[str]:
    return {path.stem for path in WIKI.rglob("*.md")}


def existing_refs(refs: list[tuple[str, str]]) -> list[tuple[str, str]]:
    stems = wiki_stems()
    return [(slug, label) for slug, label in refs if slug in stems]


def upsert_section(text: str, heading: str, body: str) -> str:
    section = f"\n## {heading}\n{body.rstrip()}\n"
    pattern = re.compile(rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    if pattern.search(text):
        return pattern.sub(section, text)
    return text.rstrip() + "\n" + section


def without_sections(text: str, headings: tuple[str, ...]) -> str:
    alternatives = "|".join(re.escape(heading) for heading in headings)
    pattern = re.compile(
        rf"\n## (?:{alternatives})\n.*?(?=\n## |\Z)",
        re.S,
    )
    return pattern.sub("", text).rstrip() + "\n"


def replace_owned_section(
    text: str,
    heading: str,
    body: str,
    *,
    legacy_headings: tuple[str, ...] = (),
) -> str:
    cleaned = without_sections(text, (heading, *legacy_headings))
    return upsert_section(cleaned, heading, body)


HARNESS_PAGES = [
    {
        "slug": "agent-eval-gate",
        "title": "Agent Eval Gate",
        "summary": "A release gate for coding or tool-using agents that checks task success, policy adherence, regression risk, and human-review handoff before broader rollout.",
        "observed": [
            "The Evals track treats evaluation as operating infrastructure, not a post-demo report.",
            "Coding-agent talks repeatedly connect automated work to review, quality gates, traces, and production rollout decisions.",
            "Slide and transcript evidence warns that static benchmarks are insufficient for agents that keep changing behavior.",
        ],
        "steps": [
            "Define the exact action boundary the agent is allowed to cross.",
            "Collect golden tasks, adversarial tasks, and regression tasks for that boundary.",
            "Score task completion separately from policy adherence, latency/cost budget, and reviewability.",
            "Require evidence artifacts: trace, diff, test output, source citations, and final human decision.",
            "Version the gate policy and attach each run to the agent/model/tooling version that produced it.",
        ],
        "sources": [
            ("agent-evaluations", "Topic synthesis"),
            ("how-should-coding-agents-be-evaluated-before-production-use", "Question layer"),
            ("2026-06-29-laurie-voss-from-vibes-to-production-evaluating-and-shipping-ai-agents-that-work-101", "Official schedule"),
            ("2026-06-30-philipp-schmid-don-t-ship-skills-without-evals", "Official schedule"),
            ("2026-06-29-nnenna-ndukwe-how-to-build-quality-gates-into-agentic-coding-workflows", "Official schedule"),
            ("youtube-Xfl50508LZM-slides", "Slide/OCR evidence"),
        ],
    },
    {
        "slug": "coding-agent-code-review-loop",
        "title": "Coding Agent Code Review Loop",
        "summary": "A workflow for letting agents produce code while preserving reviewer comprehension, test evidence, rollback paths, and issue-specific context.",
        "observed": [
            "Software-factory and coding-agent sessions frame review as a loop across prompt, diff, tests, trace, and user impact.",
            "Several talks separate code generation from the discipline needed to decide whether generated code should land.",
            "The conference graph links coding agents to context engines, PR analysis, quality gates, and team adoption.",
        ],
        "steps": [
            "Start with a task contract that names files, tests, owner, and done criteria.",
            "Have the agent produce a diff plus a short evidence bundle rather than only a prose summary.",
            "Run deterministic checks and an LLM review against policy-specific failure modes.",
            "Ask the human reviewer to inspect the riskiest changed behavior, not every generated token.",
            "Record what passed, what failed, and which reviewer decision changed the policy.",
        ],
        "sources": [
            ("coding-agents", "Topic synthesis"),
            ("software-factories", "Topic synthesis"),
            ("what-makes-a-codebase-agent-ready", "Question layer"),
            ("2026-06-29-daksh-gupta-what-we-learned-by-analyzing-1m-ai-generated-prs", "Official schedule"),
            ("2026-06-29-itamar-friedman-the-last-human-code-review-building-trust-in-ai-generated-code", "Official schedule"),
            ("2026-06-30-alex-volkov-the-z-l-continuum-should-ai-engineers-still-read-code", "Official schedule"),
        ],
    },
    {
        "slug": "context-graph-ingest",
        "title": "Context Graph Ingest",
        "summary": "A harness for turning documents, talks, repositories, profiles, and transcripts into a source-labeled graph that agents can retrieve without losing provenance.",
        "observed": [
            "Context graph, GraphRAG, memory, and retrieval sessions emphasize relationships rather than isolated chunks.",
            "The wiki already separates official schedule facts, supporting videos, transcripts, OCR, and public source-of-source context.",
            "Search and memory talks show that source reachability and relationship quality are part of agent performance.",
        ],
        "steps": [
            "Ingest sources by source type and preserve the original file or URL for every claim.",
            "Extract entities, relationships, and claim snippets into separate reviewable records.",
            "Score retrieval by whether it returns the right source for the question, not only similar text.",
            "Keep stale or weak sources reachable but labeled, so agents do not treat every edge equally.",
            "Promote stable graph patterns into topic pages, evaluations, or playbooks only after review.",
        ],
        "sources": [
            ("agent-memory", "Topic synthesis"),
            ("agentic-search", "Topic synthesis"),
            ("what-context-graph-and-memory-architecture-is-practical", "Question layer"),
            ("2026-06-30-gil-feig-why-your-company-needs-a-context-graph-and-how-to-build-it", "Official schedule"),
            ("2026-06-29-nyah-macklin-rag-needs-a-map-using-graphrag-to-retrieve-connected-context", "Official schedule"),
            ("2026-07-01-daniel-chalef-citation-needed-provenance-for-llm-built-knowledge-graphs", "Official schedule"),
        ],
    },
    {
        "slug": "sandboxed-agent-execution",
        "title": "Sandboxed Agent Execution",
        "summary": "A runtime boundary for agents that can run code, touch files, browse, call tools, or influence production systems.",
        "observed": [
            "Sandbox talks argue that agent reliability depends on designed execution environments, not only model prompting.",
            "Security sessions connect permissions, provenance, network access, and rollback to agent safety.",
            "The strongest source layer is official schedule plus event recordings and slide evidence; OCR-only details remain supporting evidence.",
        ],
        "steps": [
            "Classify the task risk before choosing process, container, microVM, network, and secret boundaries.",
            "Default to no ambient credentials and explicit network egress rules.",
            "Capture commands, diffs, artifacts, resource usage, and exit conditions.",
            "Require human approval before production mutation unless the policy explicitly allows autonomous action.",
            "Retain incident evidence so sandbox policy can be tightened after failures.",
        ],
        "sources": [
            ("ai-sandboxes", "Topic synthesis"),
            ("agent-security", "Topic synthesis"),
            ("what-security-boundaries-should-agents-have", "Question layer"),
            ("2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert", "Official schedule"),
            ("2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale", "Official schedule"),
            ("2026-06-30-ivan-burazin-kubernetes-is-not-your-sandbox", "Official schedule"),
        ],
    },
    {
        "slug": "transcript-slide-synthesis-loop",
        "title": "Transcript Slide Synthesis Loop",
        "summary": "A repeatable way to combine schedule metadata, transcripts, slide OCR, reconstructed slides, and topic pages without promoting weak evidence into confident claims.",
        "observed": [
            "This wiki has stronger media evidence than Miami: transcripts, stage frames, reconstructed crops, dense slides, and OCR audits.",
            "The source-boundary page requires official facts, supporting video context, transcript evidence, and OCR evidence to stay labeled.",
            "Several evaluation talks emphasize that outputs need traceable evidence, not only polished summaries.",
        ],
        "steps": [
            "Anchor the page with official schedule facts first.",
            "Add transcript-backed claims only when the transcript is linked and speaker/session matching is clear enough.",
            "Use reconstructed slide crops before full-stage OCR when slide text matters.",
            "Mark OCR-only claims as OCR-derived unless reviewed against the image.",
            "Regenerate dependent topic, tool, question, and evaluation indexes after source changes.",
        ],
        "sources": [
            ("source-boundary", "Source rules"),
            ("agent-source-index", "Source map"),
            ("slide-library", "Slide evidence"),
            ("reconstructed-slide-library", "Slide evidence"),
            ("dense-slide-library", "Slide evidence"),
            ("worldsfair-2026-livestreams", "Livestream resource"),
        ],
    },
]


PLAYBOOK_PAGES = [
    {
        "slug": "post-conference-tool-trial-plan",
        "title": "Post-Conference Tool Trial Plan",
        "summary": "A structured plan for deciding which Worldsfair tools deserve hands-on trials after the event.",
        "when": "Use this after a conference pass surfaces many plausible tools but not enough direct operational evidence to adopt one.",
        "steps": [
            "Group tools by job: coding agents, eval/observability, retrieval/context, sandbox/runtime, inference, and voice/multimodal.",
            "Pick one source-backed decision question per group before installing anything.",
            "Define a small local task and a scoring sheet for each group.",
            "Run a trial only when the tool has source evidence and a clear user workflow in this wiki.",
            "Write the result back as an evaluation page with confidence and open questions.",
        ],
        "sources": [
            ("tools", "Tool index"),
            ("agent-evaluations", "Topic synthesis"),
            ("coding-agents", "Topic synthesis"),
            ("ai-sandboxes", "Topic synthesis"),
            ("inference-engineering", "Topic synthesis"),
        ],
    },
    {
        "slug": "source-grounded-conference-briefing",
        "title": "Source-Grounded Conference Briefing",
        "summary": "A briefing workflow for turning the conference wiki into a decision memo without losing source boundaries.",
        "when": "Use this when preparing an executive summary, research memo, or next-build plan from the Worldsfair corpus.",
        "steps": [
            "Start from a question page rather than a broad topic when possible.",
            "Collect official schedule links, primary event media, supporting videos, transcripts, and slide pages separately.",
            "Write claims in a table that names the source layer for each claim.",
            "Use source labels and confidence notes when comparing people, companies, or tools.",
            "Record uncertainties and follow-up searches as open questions instead of hiding them.",
        ],
        "sources": [
            ("questions", "Question index"),
            ("source-boundary", "Source rules"),
            ("agent-source-index", "Source map"),
        ],
    },
]


EVALUATION_PAGES = [
    {
        "slug": "coding-agent-platforms",
        "title": "Coding Agent Platforms",
        "summary": "Compare coding-agent platforms by whether they help a team ship reviewed, testable, reversible changes rather than only generating code quickly.",
        "criteria": [
            "Repository context retrieval and task planning",
            "Diff quality, test execution, and review evidence",
            "Sandboxing, permissions, and rollback controls",
            "Team workflow fit across IDE, CLI, cloud, and CI",
            "Traceability for why a change was made",
        ],
        "recommendation": "Tentative: trial platforms against one real repository workflow using the agent-eval-gate and code-review-loop harnesses before choosing a default.",
        "confidence": "medium",
        "sources": [
            ("coding-agents", "Topic synthesis"),
            ("software-factories", "Topic synthesis"),
            ("codex", "Tool inventory"),
            ("claude-agent-sdk", "Tool inventory"),
            ("cursor", "Tool inventory"),
            ("github-copilot", "Tool inventory"),
            ("coding-agent-code-review-loop", "Harness"),
        ],
    },
    {
        "slug": "eval-observability-tools",
        "title": "Eval And Observability Tools",
        "summary": "Compare eval and observability tooling by whether it connects user outcomes, traces, policy checks, and regression tests into one improvement loop.",
        "criteria": [
            "Custom eval authoring and versioning",
            "Trace and span quality for agent workflows",
            "Dataset management and failure clustering",
            "Human review ergonomics",
            "Production feedback loop support",
        ],
        "recommendation": "Tentative: require a trial that reproduces one production-like failure and shows how the tool would prevent or detect it next time.",
        "confidence": "medium",
        "sources": [
            ("agent-evaluations", "Topic synthesis"),
            ("arize", "Tool inventory"),
            ("braintrust", "Tool inventory"),
            ("langfuse", "Tool inventory"),
            ("agent-eval-gate", "Harness"),
            ("2026-06-30-soumya-gupta-building-closed-loop-evals-for-a-multimodal-agent-at-uber-scale", "Official schedule"),
        ],
    },
    {
        "slug": "mcp-server-patterns",
        "title": "MCP Server Patterns",
        "summary": "Evaluate MCP/server patterns by whether they expose useful actions, context, and policy boundaries to agents without becoming an ungoverned tool surface.",
        "criteria": [
            "Tool contract clarity and schema quality",
            "Human-readable and agent-readable context",
            "Permission, auth, and approval boundaries",
            "Observability of tool use",
            "Failure behavior when the model chooses poorly",
        ],
        "recommendation": "Tentative: prefer narrow, policy-backed servers with explicit review paths before broad agent tool catalogs.",
        "confidence": "medium-low",
        "sources": [
            ("mcp", "Topic synthesis"),
            ("mcp", "Tool inventory"),
            ("mcp-apps", "Tool inventory"),
            ("what-security-boundaries-should-agents-have", "Question layer"),
            ("2026-06-30-session-ai-agents-don-t-read-your-policy-docs-they-hit-your-apis", "Official schedule"),
        ],
    },
    {
        "slug": "local-vs-hosted-inference",
        "title": "Local Vs Hosted Inference",
        "summary": "Compare local and hosted inference by workload, latency budget, privacy boundary, operational ownership, and model-routing needs.",
        "criteria": [
            "Latency and throughput under realistic agent loops",
            "Data privacy and deployment environment",
            "Model availability and routing flexibility",
            "Operational burden and GPU utilization",
            "Cost attribution per user-visible task",
        ],
        "recommendation": "Tentative: use hosted inference for fast iteration and broad model access, then move bounded workloads local or dedicated only when privacy, latency, or utilization evidence justifies it.",
        "confidence": "medium",
        "sources": [
            ("inference-engineering", "Topic synthesis"),
            ("what-latency-and-cost-budget-is-right-for-agent-systems", "Question layer"),
            ("vllm", "Tool inventory"),
            ("openrouter", "Tool inventory"),
            ("modal", "Tool inventory"),
            ("2026-07-01-qianru-lao-routing-llm-inference-in-production-from-engine-signals-to-policy", "Official schedule"),
        ],
    },
    {
        "slug": "sandbox-providers",
        "title": "Sandbox Providers",
        "summary": "Compare sandbox providers by isolation strength, developer ergonomics, traceability, network/secret policy, and fit for code-running agents.",
        "criteria": [
            "Isolation boundary: process, container, VM, or microVM",
            "Network, filesystem, and secret controls",
            "Startup latency and task throughput",
            "Artifact capture and replay",
            "Integration with review and approval gates",
        ],
        "recommendation": "Tentative: choose the weakest sandbox that satisfies the task risk boundary, but require stronger isolation for untrusted code, external input, production credentials, or cross-tenant workloads.",
        "confidence": "medium",
        "sources": [
            ("ai-sandboxes", "Topic synthesis"),
            ("agent-security", "Topic synthesis"),
            ("sandboxed-agent-execution", "Harness"),
            ("docker", "Tool inventory"),
            ("daytona", "Tool inventory"),
            ("browserbase", "Tool inventory"),
            ("2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert", "Official schedule"),
        ],
    },
]


TOPICS_FOR_EVIDENCE_TABLES = [
    "agent-evaluations",
    "coding-agents",
    "software-factories",
    "agentic-search",
    "agent-memory",
    "agent-security",
    "ai-sandboxes",
    "inference-engineering",
    "mcp",
    "autoresearch",
    "voice-agents",
]


LIVESTREAM_ANCHORS = [
    {
        "video": "youtube-4sX_He5c4sI",
        "title": "WF2026 Autoresearch And Keynotes",
        "summary": "This stream is the primary event-video source for the Autoresearch and keynote arc: automated research, dense retrieval, model improvement, evaluation, and research-agent workflows.",
        "transcript": "youtube-4sX_He5c4sI-transcript",
        "slides": ["youtube-4sX_He5c4sI-slides", "youtube-4sX_He5c4sI-dense-slides", "youtube-4sX_He5c4sI-reconstructed-slides"],
        "anchors": [
            ("Autoresearch workflow", ["autoresearch", "agentic-search", "agent-evaluations"]),
            ("Retrieval and test-time compute", ["2026-06-30-han-xiao-autoresearch-for-dense-retrieval-test-time-compute-with-frozen-embedding-models", "agentic-search"]),
            ("Evaluation as research control loop", ["agent-evaluations", "2026-06-30-laurie-voss-evals-track-intro"]),
            ("Memory and continual learning", ["agent-memory", "what-context-graph-and-memory-architecture-is-practical"]),
        ],
        "slide_claims": [
            "Use this stream to connect autoresearch claims to retrieval, source comparison, and evaluation loops rather than treating it as a generic keynote recording.",
            "The reconstructed slide deck is high-signal for broad event framing but still needs image review before using small OCR details as final claims.",
        ],
    },
    {
        "video": "youtube-htM02KMNZnk",
        "title": "WF2026 Software Factories And Keynotes",
        "summary": "This stream is the primary event-video source for the Software Factories/keynote arc: coding agents, verifiers, sandboxes, software-factory operations, and production AI engineering.",
        "transcript": "youtube-htM02KMNZnk-transcript",
        "slides": ["youtube-htM02KMNZnk-slides", "youtube-htM02KMNZnk-dense-slides", "youtube-htM02KMNZnk-reconstructed-slides"],
        "anchors": [
            ("Software factories", ["software-factories", "when-do-software-factories-outperform-individual-ide-agents"]),
            ("Coding-agent quality gates", ["coding-agents", "agent-eval-gate", "coding-agent-code-review-loop"]),
            ("Sandboxes and runtime isolation", ["ai-sandboxes", "sandboxed-agent-execution"]),
            ("Inference and operating budget", ["inference-engineering", "what-latency-and-cost-budget-is-right-for-agent-systems"]),
        ],
        "slide_claims": [
            "Use this stream to connect software-factory claims to verifier, sandbox, review, and rollout infrastructure.",
            "The reconstructed slide deck is high-signal for keynote framing and company/program themes; keep slide-derived details labeled until reviewed against the image.",
        ],
    },
]


CLAIM_PAGES = [
    {
        "slug": "agent-work-needs-runtime-boundaries",
        "title": "Agent Work Needs Runtime Boundaries",
        "claim": "World's Fair 2026 evidence supports the claim that useful agentic work needs explicit runtime boundaries around tools, credentials, filesystem access, network reach, and review paths.",
        "confidence": "high",
        "why": "The security and sandboxing threads repeatedly connect agent usefulness to containment, provenance, and least-privilege execution rather than only to model quality.",
        "sources": [
            ("agent-security", "Topic synthesis"),
            ("ai-sandboxes", "Topic synthesis"),
            ("sandboxed-agent-execution", "Harness synthesis"),
            ("what-security-boundaries-should-agents-have", "Question layer"),
            ("2026-06-29-steve-yegge-agentic-security-permissions-provenance-and-the-agent-supply-chain", "Official schedule"),
            ("2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale", "Official schedule"),
            ("2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert", "Official schedule"),
        ],
        "boundary": "This is a synthesis claim backed by linked local pages. It is not a direct quote from a single speaker, and implementation details should be checked against the cited source layer before reuse.",
    },
    {
        "slug": "evals-are-operational-gates",
        "title": "Evals Are Operational Gates",
        "claim": "The conference corpus supports treating evals as operational gates for agent behavior, release decisions, and review routing, not only as after-the-fact benchmark reports.",
        "confidence": "high",
        "why": "Evaluation pages, coding-agent workflow pages, and quality-gate talks converge on the need to stop or route agent work when evidence is missing or checks fail.",
        "sources": [
            ("agent-evaluations", "Topic synthesis"),
            ("agent-eval-gate", "Harness synthesis"),
            ("coding-agent-code-review-loop", "Harness synthesis"),
            ("how-should-coding-agents-be-evaluated-before-production-use", "Question layer"),
            ("2026-06-29-nnenna-ndukwe-how-to-build-quality-gates-into-agentic-coding-workflows", "Official schedule"),
            ("2026-06-29-laurie-voss-from-vibes-to-production-evaluating-and-shipping-ai-agents-that-work-101", "Official schedule"),
            ("2026-06-30-philipp-schmid-don-t-ship-skills-without-evals", "Official schedule"),
        ],
        "boundary": "This claim summarizes a recurring evidence pattern. It should not be used as proof that every cited talk made the same recommendation in the same words.",
    },
    {
        "slug": "provenance-is-part-of-context",
        "title": "Provenance Is Part Of Context",
        "claim": "For WF2026 synthesis pages, provenance is part of the useful context: agents and readers need to know which layer produced a fact before they can safely act on it.",
        "confidence": "medium-high",
        "why": "The wiki's source-boundary layer, context graph pages, and transcript/slide synthesis loop all treat source labels as necessary metadata rather than publishing polish.",
        "sources": [
            ("source-boundary", "Source rules"),
            ("agent-source-index", "Navigation/source map"),
            ("context-graph-ingest", "Harness synthesis"),
            ("transcript-slide-synthesis-loop", "Harness synthesis"),
            ("what-context-graph-and-memory-architecture-is-practical", "Question layer"),
            ("2026-07-01-daniel-chalef-citation-needed-provenance-for-llm-built-knowledge-graphs", "Official schedule"),
        ],
        "boundary": "This is a wiki-system and conference-synthesis claim. Official schedule facts, transcript evidence, OCR evidence, and synthesis should remain labeled separately.",
    },
]


PATTERN_PAGES = [
    {
        "slug": "evidence-gated-agent-workflow",
        "title": "Evidence-Gated Agent Workflow",
        "summary": "A pattern for letting agents act only when the workflow can name the source evidence, acceptance gate, and review path attached to the action.",
        "when": "Use this when an agent can change code, call tools, retrieve external context, or produce a decision that another system may rely on.",
        "steps": [
            "Define the task boundary and the evidence required before the agent starts.",
            "Attach eval or policy checks that can stop, route, or downgrade the result.",
            "Keep source links, traces, diffs, screenshots, or transcript/slide references with the output.",
            "Require human approval when the evidence bundle is incomplete or the action crosses a high-risk boundary.",
        ],
        "sources": [
            ("agent-work-needs-runtime-boundaries", "Claim synthesis"),
            ("evals-are-operational-gates", "Claim synthesis"),
            ("agent-eval-gate", "Harness synthesis"),
            ("coding-agent-code-review-loop", "Harness synthesis"),
            ("agent-security", "Topic synthesis"),
        ],
    },
    {
        "slug": "source-labeled-synthesis",
        "title": "Source-Labeled Synthesis",
        "summary": "A pattern for high-level wiki pages that synthesize across official schedule, event video, transcripts, slides, OCR, public supporting context, and comparison fixtures without flattening them into one confidence layer.",
        "when": "Use this when a topic, claim, pattern, briefing, or evaluation summarizes multiple source layers and could otherwise overstate weak evidence.",
        "steps": [
            "Anchor dates, speakers, titles, rooms, and affiliations in official schedule pages.",
            "Use official WF2026 event media as first-class video evidence when present.",
            "Label transcript, slide, OCR, and comparison-context material separately.",
            "Promote only reviewed recurring evidence into claims, patterns, evaluations, or playbooks.",
        ],
        "sources": [
            ("source-boundary", "Source rules"),
            ("agent-source-index", "Navigation/source map"),
            ("transcript-slide-synthesis-loop", "Harness synthesis"),
            ("source-grounded-conference-briefing", "Playbook synthesis"),
            ("aie-wiki-generation-delta", "Comparison context"),
        ],
    },
    {
        "slug": "sandboxed-delegation",
        "title": "Sandboxed Delegation",
        "summary": "A pattern for delegating agent work into constrained execution environments whose tools, permissions, lifetime, and evidence trail are set before the work begins.",
        "when": "Use this for coding agents, browser agents, MCP tools, data agents, and any system where a model can affect files, services, credentials, or external state.",
        "steps": [
            "Choose the smallest execution boundary that can perform the task.",
            "Pass only task-specific credentials, files, network routes, and tool permissions.",
            "Capture commands, tool calls, artifacts, and verification outputs.",
            "Expire the environment and credentials after the run unless the policy explicitly permits persistence.",
        ],
        "sources": [
            ("agent-work-needs-runtime-boundaries", "Claim synthesis"),
            ("sandboxed-agent-execution", "Harness synthesis"),
            ("ai-sandboxes", "Topic synthesis"),
            ("agent-security", "Topic synthesis"),
            ("2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale", "Official schedule"),
            ("2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert", "Official schedule"),
        ],
    },
]


def render_source_list(refs: list[tuple[str, str]]) -> list[str]:
    refs = existing_refs(refs)
    if not refs:
        return ["- No local source links found; keep this page provisional."]
    return [f"- [[{slug}]] - {label}" for slug, label in refs]


def render_harness(page: dict) -> str:
    return "\n".join(
        [
            frontmatter(
                {
                    "title": page["title"],
                    "category": "harnesses",
                    "status": "seeded",
                    "sourceLabels": sorted({label for _, label in existing_refs(page["sources"])}),
                }
            ),
            f"# {page['title']}",
            "",
            "## Purpose",
            page["summary"],
            "",
            "## Observed At AIE",
            *[f"- {item}" for item in page["observed"]],
            "",
            "## Recommended Implementation Steps",
            *[f"- {item}" for item in page["steps"]],
            "",
            "## Source Evidence",
            *render_source_list(page["sources"]),
            "",
            "## Evidence Boundary",
            "This is a reusable workflow synthesized from the linked conference evidence. Treat it as a recommended implementation pattern, not as a direct quote from any single talk.",
        ]
    )


def render_claim(page: dict) -> str:
    return "\n".join(
        [
            frontmatter(
                {
                    "title": page["title"],
                    "category": "claims",
                    "status": "seeded",
                    "confidence": page["confidence"],
                    "sourceLabels": sorted({label for _, label in existing_refs(page["sources"])}),
                }
            ),
            f"# {page['title']}",
            "",
            "## Claim",
            page["claim"],
            "",
            "## Why It Is Supported",
            page["why"],
            "",
            "## Source Evidence",
            *render_source_list(page["sources"]),
            "",
            "## Confidence",
            page["confidence"],
            "",
            "## Evidence Boundary",
            page["boundary"],
        ]
    )


def render_pattern(page: dict) -> str:
    return "\n".join(
        [
            frontmatter(
                {
                    "title": page["title"],
                    "category": "patterns",
                    "status": "seeded",
                    "sourceLabels": sorted({label for _, label in existing_refs(page["sources"])}),
                }
            ),
            f"# {page['title']}",
            "",
            "## Pattern",
            page["summary"],
            "",
            "## When To Use",
            page["when"],
            "",
            "## Implementation Moves",
            *[f"- {item}" for item in page["steps"]],
            "",
            "## Source Evidence",
            *render_source_list(page["sources"]),
            "",
            "## Evidence Boundary",
            "This is a reusable pattern synthesized from linked conference evidence. Treat it as an engineering abstraction, not as an official event claim or a direct quote.",
        ]
    )


def render_playbook(page: dict) -> str:
    return "\n".join(
        [
            frontmatter(
                {
                    "title": page["title"],
                    "category": "playbooks",
                    "status": "seeded",
                    "sourceLabels": sorted({label for _, label in existing_refs(page["sources"])}),
                }
            ),
            f"# {page['title']}",
            "",
            "## Purpose",
            page["summary"],
            "",
            "## When To Use",
            page["when"],
            "",
            "## Steps",
            *[f"- {item}" for item in page["steps"]],
            "",
            "## Source Evidence",
            *render_source_list(page["sources"]),
            "",
            "## Evidence Boundary",
            "This playbook is a post-conference action layer. It should cite sources for motivation while keeping implementation advice separate from observed event evidence.",
        ]
    )


def render_evaluation(page: dict) -> str:
    return "\n".join(
        [
            frontmatter(
                {
                    "title": page["title"],
                    "category": "evaluations",
                    "status": "tentative",
                    "confidence": page["confidence"],
                    "sourceLabels": sorted({label for _, label in existing_refs(page["sources"])}),
                }
            ),
            f"# {page['title']}",
            "",
            "## Decision Question",
            page["summary"],
            "",
            "## Criteria",
            *[f"- {item}" for item in page["criteria"]],
            "",
            "## Source Evidence",
            *render_source_list(page["sources"]),
            "",
            "## Tentative Recommendation",
            page["recommendation"],
            "",
            "## Confidence",
            f"{page['confidence']}. No recommendation should be treated as final without a hands-on trial or source-backed comparison for the concrete use case.",
            "",
            "## Open Questions",
            "- Which current project workflow is the evaluation being applied to?",
            "- Which failure mode would make the recommendation wrong?",
            "- Which source or trial result would change the score?",
        ]
    )


def render_index(title: str, category: str, intro: str, records: list[dict]) -> str:
    lines = [
        frontmatter({"title": title, "category": category}),
        f"# {title}",
        "",
        intro,
        "",
        "## Index",
    ]
    for record in sorted(records, key=lambda item: item["title"].lower()):
        suffix = f" ({record.get('confidence')})" if record.get("confidence") else ""
        lines.append(f"- [[{record['id']}]] - {record['title']}{suffix}")
    return "\n".join(lines)


def evaluate_private_fixture(policy: dict, fixture: dict) -> float:
    weights = policy["weights"]
    signals = fixture["signals"]
    return round(sum(weights[key] * float(signals.get(key, 0)) for key in weights), 2)


def load_private_policy_profile() -> dict:
    if not PRIVATE_POLICY_PROFILE.exists():
        return {"policies": [], "evalFixtures": []}
    return json.loads(PRIVATE_POLICY_PROFILE.read_text(encoding="utf-8"))


def generate_harnesses() -> list[dict]:
    records = []
    for page in HARNESS_PAGES:
        write(WIKI / "harnesses" / f"{page['slug']}.md", render_harness(page))
        records.append({"id": page["slug"], "title": page["title"], "path": f"wiki/harnesses/{page['slug']}.md"})
    index = render_index(
        "Harnesses",
        "harnesses",
        "Reusable AI engineering workflows synthesized from Worldsfair evidence. Each page separates observed AIE evidence from recommended implementation steps.",
        records,
    )
    write(WIKI / "harnesses" / "index.md", index)
    write(WIKI / "harnesses" / "harnesses.md", index)
    write(WIKI / "harnesses" / "registry.json", json.dumps(records, indent=2, ensure_ascii=False))
    return records


def generate_claims() -> list[dict]:
    records = []
    for page in CLAIM_PAGES:
        write(WIKI / "claims" / f"{page['slug']}.md", render_claim(page))
        records.append(
            {
                "id": page["slug"],
                "title": page["title"],
                "path": f"wiki/claims/{page['slug']}.md",
                "confidence": page["confidence"],
            }
        )
    index = render_index(
        "Claims",
        "claims",
        "Evidence-backed synthesis claims extracted from repeated World's Fair 2026 themes. Each claim keeps source layers and confidence visible.",
        records,
    )
    write(WIKI / "claims" / "index.md", index)
    write(WIKI / "claims" / "claims.md", index)
    write(WIKI / "claims" / "registry.json", json.dumps(records, indent=2, ensure_ascii=False))
    return records


def generate_patterns() -> list[dict]:
    records = []
    for page in PATTERN_PAGES:
        write(WIKI / "patterns" / f"{page['slug']}.md", render_pattern(page))
        records.append({"id": page["slug"], "title": page["title"], "path": f"wiki/patterns/{page['slug']}.md"})
    index = render_index(
        "Patterns",
        "patterns",
        "Reusable AI engineering patterns synthesized from linked World's Fair 2026 evidence.",
        records,
    )
    write(WIKI / "patterns" / "index.md", index)
    write(WIKI / "patterns" / "patterns.md", index)
    write(WIKI / "patterns" / "registry.json", json.dumps(records, indent=2, ensure_ascii=False))
    return records


def generate_playbooks() -> list[dict]:
    records = []
    for page in PLAYBOOK_PAGES:
        write(WIKI / "playbooks" / f"{page['slug']}.md", render_playbook(page))
        records.append({"id": page["slug"], "title": page["title"], "path": f"wiki/playbooks/{page['slug']}.md"})
    index = render_index(
        "Playbooks",
        "playbooks",
        "Practical post-conference workflows derived from the sourced Worldsfair wiki.",
        records,
    )
    write(WIKI / "playbooks" / "index.md", index)
    write(WIKI / "playbooks" / "playbooks.md", index)
    write(WIKI / "playbooks" / "registry.json", json.dumps(records, indent=2, ensure_ascii=False))
    return records


def generate_evaluations() -> list[dict]:
    records = []
    for page in EVALUATION_PAGES:
        write(WIKI / "evaluations" / f"{page['slug']}.md", render_evaluation(page))
        records.append(
            {
                "id": page["slug"],
                "title": page["title"],
                "path": f"wiki/evaluations/{page['slug']}.md",
                "confidence": page["confidence"],
            }
        )
    index = render_index(
        "Evaluations",
        "evaluations",
        "Comparative decision artifacts for tools, workflows, and infrastructure. Recommendations are tentative unless backed by a concrete trial.",
        records,
    )
    write(WIKI / "evaluations" / "index.md", index)
    write(WIKI / "evaluations" / "evaluations.md", index)
    write(WIKI / "evaluations" / "registry.json", json.dumps(records, indent=2, ensure_ascii=False))
    return records


def generate_private_quality_receipts() -> tuple[list[dict], list[dict]]:
    profile = load_private_policy_profile()
    policies = {policy["slug"]: policy for policy in profile.get("policies", [])}
    fixtures_by_policy: dict[str, list[dict]] = {slug: [] for slug in policies}
    results = []
    for fixture in profile.get("evalFixtures", []):
        policy = policies[fixture["policy"]]
        score = evaluate_private_fixture(policy, fixture)
        result = "pass" if score >= fixture["expectedMin"] else "fail"
        row = {
            "policy": fixture["policy"],
            "name": fixture["name"],
            "score": score,
            "expectedMin": fixture["expectedMin"],
            "result": result,
            "why": fixture["why"],
        }
        results.append(row)
        fixtures_by_policy[fixture["policy"]].append(fixture)

    records = []
    for policy in profile.get("policies", []):
        policy_doc = {
            **policy,
            "weightsTotal": sum(policy["weights"].values()),
            "evalFixtures": fixtures_by_policy[policy["slug"]],
        }
        write(PRIVATE_QUALITY_DIR / "policies" / f"{policy['slug']}.json", json.dumps(policy_doc, indent=2, ensure_ascii=False))
        records.append(
            {
                "id": policy["slug"],
                "title": policy["title"],
                "path": f".ops/state/cache/wiki-maker/private-quality/policies/{policy['slug']}.json",
                "topic": policy["topic"],
                "version": policy["version"],
            }
        )
    write(PRIVATE_QUALITY_DIR / "check-results.json", json.dumps(results, indent=2, ensure_ascii=False))
    write(PRIVATE_QUALITY_DIR / "registry.json", json.dumps(records, indent=2, ensure_ascii=False))
    failures = [row for row in results if row["result"] != "pass"]
    if failures:
        names = ", ".join(f"{row['policy']}:{row['name']}" for row in failures)
        raise SystemExit(f"private quality-gate failures: {names}")
    return records, results


def categorize_ref(slug: str) -> str:
    for category in ["talks", "resources", "slides", "transcripts", "questions", "tools", "evaluations", "harnesses", "playbooks"]:
        if (WIKI / category / f"{slug}.md").exists():
            return category
    if slug.startswith("youtube-") and slug.endswith("-slides"):
        return "slides"
    if slug.startswith("youtube-"):
        return "resources"
    return "other"


def topic_evidence_rows(topic_slug: str) -> list[dict]:
    path = WIKI / "topics" / f"{topic_slug}.md"
    if not path.exists():
        return []
    text = without_sections(
        path.read_text(encoding="utf-8", errors="ignore"),
        ("Source Coverage", "Evidence Table", "Representative Evidence Links"),
    )
    refs = []
    for raw in re.findall(r"\[\[([^\]]+)\]\]", text):
        target = raw.split("|", 1)[0].split("#", 1)[0].strip()
        if target and target != topic_slug:
            refs.append(target)
    seen = set()
    rows = []
    for ref in refs:
        if ref in seen:
            continue
        seen.add(ref)
        rows.append({"ref": ref, "category": categorize_ref(ref)})
    return rows


def update_topic_evidence_tables() -> dict:
    summary = {}
    for topic in TOPICS_FOR_EVIDENCE_TABLES:
        path = WIKI / "topics" / f"{topic}.md"
        if not path.exists():
            continue
        rows = topic_evidence_rows(topic)
        counts = {}
        for row in rows:
            counts[row["category"]] = counts.get(row["category"], 0) + 1
        table = [
            "This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.",
            "",
            "| Evidence type | Count | Review note |",
            "| --- | ---: | --- |",
        ]
        review_notes = {
            "talks": "Official schedule pages; use for titles, speakers, tracks, and stated talk framing.",
            "resources": "Video/resource pages; check source status before treating as primary event evidence.",
            "slides": "OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed.",
            "transcripts": "Transcript markdown; check session matching and caption quality.",
            "tools": "Derived inventory pages; use as entity context, not independent proof.",
            "questions": "Research questions that collect follow-up evidence.",
            "evaluations": "Decision artifacts; recommendations are tentative.",
            "harnesses": "Reusable workflows synthesized from evidence.",
            "playbooks": "Action workflows synthesized from evidence.",
            "other": "Related pages outside the main evidence categories.",
        }
        for category in sorted(counts):
            table.append(f"| {category} | {counts[category]} | {review_notes.get(category, review_notes['other'])} |")
        table.append("")
        for category in ["talks", "resources", "slides", "transcripts", "tools", "questions"]:
            samples = [row["ref"] for row in rows if row["category"] == category][:6]
            if samples:
                table.append(f"### {category.title()}")
                table.extend(f"- [[{ref}]]" for ref in samples)
                table.append("")
        text = path.read_text(encoding="utf-8")
        write(
            path,
            replace_owned_section(
                text,
                "Source Coverage",
                "\n".join(table),
                legacy_headings=("Evidence Table", "Representative Evidence Links"),
            ),
        )
        summary[topic] = counts
    write(
        INTERNAL_SYNTHESIS_DIR / "topic-evidence-table-summary.json",
        json.dumps(summary, indent=2, ensure_ascii=False),
    )
    return summary


def generate_livestream_thematic_anchors() -> None:
    lines = [
        frontmatter(
            {
                "title": "Livestream Thematic Anchors",
                "category": "resources",
                "sourceLabels": ["YouTube livestream captions", "Reconstructed slide evidence", "Topic synthesis"],
            }
        ),
        "# Livestream Thematic Anchors",
        "",
        "This page splits the broad official Worldsfair livestreams into thematic anchors without copying full transcripts into the wiki. Use it as a routing layer into transcript markdown, slide decks, topics, questions, harnesses, and evaluations.",
        "",
    ]
    summary_lines = [
        "Thematic anchors now exist for the two high-signal official Worldsfair livestreams with reconstructed slide decks:",
        "",
    ]
    for stream in LIVESTREAM_ANCHORS:
        lines.extend(
            [
                f"## {stream['title']}",
                stream["summary"],
                "",
                "### Source Links",
                f"- Video/resource page: [[{stream['video']}]]",
                f"- Transcript markdown: [[{stream['transcript']}]]",
                *[f"- Slide deck: [[{slug}]]" for slug in stream["slides"] if slug in wiki_stems()],
                "",
                "### Thematic Anchors",
            ]
        )
        for title, refs in stream["anchors"]:
            existing = [ref for ref in refs if ref in wiki_stems()]
            links = ", ".join(f"[[{ref}]]" for ref in existing) if existing else "No local links yet"
            lines.append(f"- {title}: {links}")
        lines.extend(["", "### Slide-Derived Claim Boundary"])
        lines.extend(f"- {claim}" for claim in stream["slide_claims"])
        lines.append("")
        summary_lines.append(f"- [[{stream['video']}]] - {stream['title']}; anchors: {len(stream['anchors'])}; reconstructed slide deck linked.")
    write(WIKI / "resources" / "livestream-thematic-anchors.md", "\n".join(lines))

    resource = WIKI / "resources" / "worldsfair-2026-livestreams.md"
    if resource.exists():
        text = resource.read_text(encoding="utf-8")
        summary_lines.extend(
            [
                "",
                "Use [[livestream-thematic-anchors]] before quoting or summarizing the livestreams; it keeps transcript, slide, and topic evidence separated.",
            ]
        )
        write(resource, upsert_section(text, "Thematic Anchors", "\n".join(summary_lines)))


def generate_main_index() -> None:
    lines = [
        "# AI Engineer World's Fair 2026 Index",
        "",
        "## Start Here",
        "This standalone wiki is organized as a conference intelligence vault: official schedule first, then public video evidence, transcripts, slide/OCR evidence, topic synthesis, questions, claims, patterns, harnesses, playbooks, and evaluations.",
        "",
        "- Public landing page: [[overview]]",
        "- Evidence rules: [[source-boundary]]",
        "- Agent source map: [[agent-source-index]]",
        "- Talk/video/transcript map: [[talk-video-transcript-map]]",
        "- Static source repository: [mwuhahaha/conference-ai-sanfran-worldsfair2026-wiki](https://github.com/mwuhahaha/conference-ai-sanfran-worldsfair2026-wiki)",
        "- Official event site: [AI Engineer World's Fair 2026](https://www.ai.engineer/worldsfair/2026)",
        "",
        "## Conference Map",
        "- [[2026-06-28-new-engineer-orientation]]",
        "- [[2026-06-29-workshop-day-and-welcome-reception]]",
        "- [[2026-06-30-keynotes-and-breakouts]]",
        "- [[2026-07-01-world-cup-and-multi-track-programming]]",
        "- [[2026-07-02-final-day-and-last-chance-expo]]",
        "",
        "## Intelligence Layers",
        "- [Topics](/topics/) - content-derived themes and evidence tables",
        "- [Tools](/tools/) - high-confidence tool, model, platform, and protocol inventory",
        "- [Questions](/questions/) - open research and implementation questions",
        "- [Claims](/claims/) - evidence-backed synthesis claims",
        "- [Patterns](/patterns/) - reusable AI engineering patterns",
        "- [Harnesses](/harnesses/) - reusable workflows observed or implied by the evidence",
        "- [Playbooks](/playbooks/) - post-conference action workflows",
        "- [Evaluations](/evaluations/) - comparative decision artifacts and scorecards",
        "",
        "## Major Themes",
        "- [[coding-agents]]",
        "- [[software-factories]]",
        "- [[agent-evaluations]]",
        "- [[agentic-search]]",
        "- [[agent-memory]]",
        "- [[agent-security]]",
        "- [[ai-sandboxes]]",
        "- [[inference-engineering]]",
        "- [[mcp]]",
        "- [[autoresearch]]",
        "- [[voice-agents]]",
        "",
        "## Evidence Libraries",
        "- [[slide-library]]",
        "- [[reconstructed-slide-library]]",
        "- [[dense-slide-library]]",
        "- [Transcripts](/transcripts/)",
        "- [[worldsfair-2026-livestreams]]",
        "- [[livestream-thematic-anchors]]",
        "- [[external-video-discovery]]",
        "- [[room-attendance-calibration]]",
        "- [[video-attendance-visibility]]",
        "",
        "## Claim And Evaluation Entry Points",
        "- [[agent-work-needs-runtime-boundaries]]",
        "- [[evidence-gated-agent-workflow]]",
        "- [[agent-eval-gate]]",
        "- [[coding-agent-platforms]]",
        "- [[eval-observability-tools]]",
        "- [[local-vs-hosted-inference]]",
        "- [[sandbox-providers]]",
        "",
        "## Exhaustive Listings",
        "Use category pages for exhaustive listings instead of this guide: [Talks](/talks/), [People](/people/), [Companies](/companies/), [Resources](/resources/), [Slides](/slides/), [Transcripts](/transcripts/), [Tools](/tools/), and [Topics](/topics/).",
    ]
    write(WIKI / "index.md", "\n".join(lines))


def update_agent_source_index() -> None:
    path = WIKI / "resources" / "agent-source-index.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    body = "\n".join(
        [
            "- `python3 scripts/generate_synthesis_layers.py` - generate claims, patterns, harnesses, playbooks, evaluations, topic evidence tables, and livestream thematic anchors.",
            "- The same generator also seeds evidence-backed claims and reusable patterns when the local evidence graph supports them.",
        ]
    )
    write(path, upsert_section(text, "Synthesis Layer", body))


def write_receipt(counts: dict) -> str:
    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rel = f".ops/state/runs/{now}-synthesis-layers.md"
    lines = [
        "---",
        "type: run-receipt",
        "scope: project-local",
        "status: complete",
        f"updated: {datetime.now(timezone.utc).isoformat()}",
        "source: generate_synthesis_layers.py",
        "---",
        "",
        "# Synthesis Layers Run",
        "",
        "Generated the remaining Worldsfair AIE synthesis layers:",
        f"- Claim pages: {counts['claims']}",
        f"- Pattern pages: {counts['patterns']}",
        f"- Harness pages: {counts['harnesses']}",
        f"- Playbook pages: {counts['playbooks']}",
        f"- Evaluation pages: {counts['evaluations']}",
        f"- Topic evidence tables updated: {counts['topic_tables']}",
        f"- Livestream thematic anchor pages: {counts['livestream_anchor_pages']}",
        f"- Private quality policies checked: {counts['private_quality_policies']}",
        f"- Private quality fixtures checked: {counts['private_quality_checks']}",
        "",
        "Key outputs:",
        "- `wiki/harnesses/`",
        "- `wiki/claims/`",
        "- `wiki/patterns/`",
        "- `wiki/playbooks/`",
        "- `wiki/evaluations/`",
        "- `wiki/resources/livestream-thematic-anchors.md`",
        "- `.ops/state/cache/synthesis-layers/topic-evidence-table-summary.json` (internal; ignored)",
        "- `.ops/state/cache/wiki-maker/private-quality/` (internal only; ignored)",
        "",
        "Boundary: private quality artifacts are not emitted to public wiki pages, raw public sources, the static site, or the agent index.",
    ]
    write(ROOT / rel, "\n".join(lines))
    return rel


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Regenerate evidence-backed synthesis layers and private receipts."
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    parse_args(argv)
    claims = generate_claims()
    patterns = generate_patterns()
    harnesses = generate_harnesses()
    evaluations = generate_evaluations()
    playbooks = generate_playbooks()
    private_policy_records, private_check_results = generate_private_quality_receipts()
    topic_summary = update_topic_evidence_tables()
    generate_livestream_thematic_anchors()
    generate_main_index()
    update_agent_source_index()
    receipt = write_receipt(
        {
            "harnesses": len(harnesses),
            "claims": len(claims),
            "patterns": len(patterns),
            "playbooks": len(playbooks),
            "evaluations": len(evaluations),
            "private_quality_policies": len(private_policy_records),
            "private_quality_checks": len(private_check_results),
            "topic_tables": len(topic_summary),
            "livestream_anchor_pages": 1,
        }
    )
    print(
        json.dumps(
            {
                "harness_pages": len(harnesses),
                "claim_pages": len(claims),
                "pattern_pages": len(patterns),
                "playbook_pages": len(playbooks),
                "evaluation_pages": len(evaluations),
                "private_quality_policies": len(private_policy_records),
                "private_quality_checks": len(private_check_results),
                "topic_tables": len(topic_summary),
                "livestream_anchor_pages": 1,
                "receipt": receipt,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
