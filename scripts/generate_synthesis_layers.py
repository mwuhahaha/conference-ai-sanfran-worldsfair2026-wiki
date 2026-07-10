#!/usr/bin/env python3
"""Generate Worldsfair synthesis layers, policies, and policy evals."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw" / "sources"
POLICY_RAW = RAW / "credibility-policies"


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
            "Pick one policy-backed decision question per group before installing anything.",
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
            "Score people, companies, or tools only with the policy for that topic and use case.",
            "Record uncertainties and follow-up searches as open questions instead of hiding them.",
        ],
        "sources": [
            ("questions", "Question index"),
            ("source-boundary", "Source rules"),
            ("agent-source-index", "Source map"),
            ("credibility-policy-evals", "Policy evals"),
        ],
    },
    {
        "slug": "credibility-policy-review-loop",
        "title": "Credibility Policy Review Loop",
        "summary": "A maintenance workflow for changing topic-specific credibility scoring without losing how previous scores were made.",
        "when": "Use this whenever a score feels wrong, a new topic needs a different algorithm, or public attention should be weighted differently.",
        "steps": [
            "Change exactly one policy file under `raw/sources/credibility-policies/`.",
            "Add or adjust at least one eval fixture that names a person who should score high or low for that topic.",
            "Run `python3 scripts/generate_synthesis_layers.py` and inspect the policy eval report.",
            "If the eval contradicts domain intuition, tune the policy weights rather than hand-editing the score.",
            "Commit or review policy changes one policy at a time so future readers know how each score was made.",
        ],
        "sources": [
            ("credibility-policy-evals", "Policy evals"),
            ("agent-evaluations", "Topic synthesis"),
            ("source-boundary", "Source rules"),
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
        "recommendation": "Tentative: choose the weakest sandbox that satisfies the task risk policy, but require stronger isolation for untrusted code, external input, production credentials, or cross-tenant workloads.",
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
    {
        "slug": "credibility-policy-evals",
        "title": "Credibility Policy Evals",
        "summary": "Evaluate whether topic-specific credibility policies score known strong exemplars high enough and expose where the measurement needs tuning.",
        "criteria": [
            "Policy weights are explicit and versioned",
            "High-credibility exemplars pass their expected threshold",
            "View or fame signals are useful only when the topic asks for public attention",
            "Each failed fixture creates a policy-adjustment task, not a manual score override",
        ],
        "recommendation": "Use topic policies as score provenance. Change one policy at a time and rerun evals before applying scores to public pages.",
        "confidence": "high",
        "sources": [
            ("credibility-policy-review-loop", "Playbook"),
            ("source-boundary", "Source rules"),
            ("agent-evaluations", "Topic synthesis"),
        ],
    },
]


CREDIBILITY_POLICIES = [
    {
        "slug": "coding-agents-credibility",
        "title": "Coding Agents Credibility",
        "topic": "coding-agents",
        "useCase": "Rank people or sources for practical coding-agent workflow guidance.",
        "version": "2026-07-10.1",
        "viewSignalRole": "Minor. Views can indicate broad adoption, but code/review practice and shipped artifacts matter more.",
        "weights": {
            "topic_fit": 20,
            "practitioner_depth": 25,
            "shipped_artifacts": 20,
            "official_or_primary_source": 15,
            "peer_recognition": 10,
            "production_scale": 5,
            "public_attention": 5,
        },
    },
    {
        "slug": "agent-evaluations-credibility",
        "title": "Agent Evaluations Credibility",
        "topic": "agent-evaluations",
        "useCase": "Rank people or sources for eval design, observability, review loops, and production agent quality.",
        "version": "2026-07-10.1",
        "viewSignalRole": "Low. Eval credibility comes from repeatable artifacts, production failure coverage, and trace evidence.",
        "weights": {
            "topic_fit": 15,
            "domain_practice": 25,
            "evaluation_artifacts": 25,
            "production_scale": 15,
            "source_depth": 15,
            "public_attention": 5,
        },
    },
    {
        "slug": "agentic-search-credibility",
        "title": "Agentic Search Credibility",
        "topic": "agentic-search",
        "useCase": "Rank people or sources for retrieval, search infrastructure, source triage, and research-agent discovery.",
        "version": "2026-07-10.1",
        "viewSignalRole": "Contextual. Views matter when the goal is public influence or consumer search behavior; primary retrieval expertise matters more for correctness.",
        "weights": {
            "topic_fit": 20,
            "retrieval_expertise": 25,
            "primary_research_or_product": 20,
            "source_quality": 15,
            "deployment_signal": 10,
            "public_attention": 10,
        },
    },
    {
        "slug": "ai-sandboxes-credibility",
        "title": "AI Sandboxes Credibility",
        "topic": "ai-sandboxes",
        "useCase": "Rank people or sources for agent runtime isolation, tool permissions, code execution, and sandbox safety.",
        "version": "2026-07-10.1",
        "viewSignalRole": "Very low. Isolation credibility should follow production security and runtime evidence, not popularity.",
        "weights": {
            "topic_fit": 20,
            "security_infra_practice": 30,
            "production_isolation": 25,
            "evidence_source": 15,
            "peer_recognition": 5,
            "public_attention": 5,
        },
    },
    {
        "slug": "inference-engineering-credibility",
        "title": "Inference Engineering Credibility",
        "topic": "inference-engineering",
        "useCase": "Rank people or sources for inference engines, routing, latency, GPU utilization, and model-serving operations.",
        "version": "2026-07-10.1",
        "viewSignalRole": "Low unless evaluating public education reach. Systems evidence, benchmarks, and operating scale dominate.",
        "weights": {
            "topic_fit": 20,
            "systems_expertise": 30,
            "production_scale": 20,
            "benchmark_or_paper": 15,
            "operational_signal": 10,
            "public_attention": 5,
        },
    },
]


POLICY_EVALS = [
    {
        "policy": "coding-agents-credibility",
        "name": "Kent C. Dodds",
        "expectedMin": 82,
        "why": "Known expert in production web/product engineering and developer education; useful high exemplar when judging practical coding-agent workflow advice.",
        "signals": {
            "topic_fit": 0.9,
            "practitioner_depth": 0.95,
            "shipped_artifacts": 0.9,
            "official_or_primary_source": 0.8,
            "peer_recognition": 0.9,
            "production_scale": 0.75,
            "public_attention": 0.85,
        },
    },
    {
        "policy": "coding-agents-credibility",
        "name": "Jason Liu",
        "expectedMin": 82,
        "why": "Strong practical signal for AI engineering workflows, structured outputs, and hands-on Codex/coding-agent practice.",
        "signals": {
            "topic_fit": 0.95,
            "practitioner_depth": 0.95,
            "shipped_artifacts": 0.9,
            "official_or_primary_source": 0.85,
            "peer_recognition": 0.85,
            "production_scale": 0.7,
            "public_attention": 0.75,
        },
    },
    {
        "policy": "agent-evaluations-credibility",
        "name": "Aparna Dhinakaran",
        "expectedMin": 84,
        "why": "High exemplar for AI observability and eval infrastructure because credibility comes from Arize/Phoenix-style production evaluation practice.",
        "signals": {
            "topic_fit": 0.95,
            "domain_practice": 0.95,
            "evaluation_artifacts": 0.95,
            "production_scale": 0.9,
            "source_depth": 0.85,
            "public_attention": 0.75,
        },
    },
    {
        "policy": "agent-evaluations-credibility",
        "name": "Laurie Voss",
        "expectedMin": 82,
        "why": "High exemplar for practical agent eval framing and shipping guidance in the AIE graph.",
        "signals": {
            "topic_fit": 0.95,
            "domain_practice": 0.9,
            "evaluation_artifacts": 0.85,
            "production_scale": 0.8,
            "source_depth": 0.9,
            "public_attention": 0.75,
        },
    },
    {
        "policy": "agentic-search-credibility",
        "name": "Jo Kristian Bergum",
        "expectedMin": 82,
        "why": "Known retrieval/search practitioner; a high exemplar when correctness depends on IR fundamentals rather than popularity.",
        "signals": {
            "topic_fit": 0.95,
            "retrieval_expertise": 0.95,
            "primary_research_or_product": 0.9,
            "source_quality": 0.9,
            "deployment_signal": 0.85,
            "public_attention": 0.55,
        },
    },
    {
        "policy": "agentic-search-credibility",
        "name": "Han Xiao",
        "expectedMin": 82,
        "why": "High exemplar for dense retrieval and search/retrieval systems in the local Worldsfair graph.",
        "signals": {
            "topic_fit": 0.95,
            "retrieval_expertise": 0.95,
            "primary_research_or_product": 0.9,
            "source_quality": 0.85,
            "deployment_signal": 0.8,
            "public_attention": 0.7,
        },
    },
    {
        "policy": "ai-sandboxes-credibility",
        "name": "Solomon Hykes",
        "expectedMin": 82,
        "why": "External calibration exemplar for container/runtime isolation: popularity should not be required for a high sandbox credibility score.",
        "signals": {
            "topic_fit": 0.85,
            "security_infra_practice": 0.9,
            "production_isolation": 0.95,
            "evidence_source": 0.85,
            "peer_recognition": 0.95,
            "public_attention": 0.75,
        },
    },
    {
        "policy": "ai-sandboxes-credibility",
        "name": "Samuel Colvin",
        "expectedMin": 80,
        "why": "High local exemplar for sandbox-not-desert framing and practical Python/runtime tooling credibility.",
        "signals": {
            "topic_fit": 0.95,
            "security_infra_practice": 0.85,
            "production_isolation": 0.85,
            "evidence_source": 0.9,
            "peer_recognition": 0.8,
            "public_attention": 0.65,
        },
    },
    {
        "policy": "inference-engineering-credibility",
        "name": "Charles Frye",
        "expectedMin": 82,
        "why": "High exemplar for explaining inference engines from first principles with strong technical depth.",
        "signals": {
            "topic_fit": 0.95,
            "systems_expertise": 0.9,
            "production_scale": 0.75,
            "benchmark_or_paper": 0.85,
            "operational_signal": 0.85,
            "public_attention": 0.75,
        },
    },
    {
        "policy": "inference-engineering-credibility",
        "name": "Ion Stoica",
        "expectedMin": 84,
        "why": "External calibration exemplar for distributed systems and AI infrastructure; should score high even when the specific question is not about fame.",
        "signals": {
            "topic_fit": 0.85,
            "systems_expertise": 0.98,
            "production_scale": 0.95,
            "benchmark_or_paper": 0.95,
            "operational_signal": 0.9,
            "public_attention": 0.8,
        },
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


def score_fixture(policy: dict, fixture: dict) -> float:
    weights = policy["weights"]
    signals = fixture["signals"]
    return round(sum(weights[key] * float(signals.get(key, 0)) for key in weights), 2)


def render_policy_page(policy: dict, fixtures: list[dict]) -> str:
    lines = [
        frontmatter(
            {
                "title": policy["title"],
                "category": "policies",
                "topic": policy["topic"],
                "version": policy["version"],
                "status": "active",
                "sourceLabels": ["Credibility policy", "Evaluation-backed scoring"],
            }
        ),
        f"# {policy['title']}",
        "",
        "## Use Case",
        policy["useCase"],
        "",
        "## View Signal Role",
        policy["viewSignalRole"],
        "",
        "## Scoring Weights",
        "| Signal | Weight |",
        "| --- | ---: |",
    ]
    for key, weight in policy["weights"].items():
        lines.append(f"| `{key}` | {weight} |")
    lines.extend(
        [
            "",
            "## Evaluation Fixtures",
            "| Name | Score | Expected Min | Result |",
            "| --- | ---: | ---: | --- |",
        ]
    )
    for fixture in fixtures:
        score = score_fixture(policy, fixture)
        result = "pass" if score >= fixture["expectedMin"] else "fail"
        lines.append(f"| {fixture['name']} | {score:.2f} | {fixture['expectedMin']} | {result} |")
    lines.extend(
        [
            "",
            "## Policy Boundary",
            "This policy scores credibility for one topic and use case. Do not reuse it for unrelated topics where public fame, domain credentials, implementation depth, or primary-source evidence should be weighted differently.",
            "",
            "## Change Rule",
            "Change one policy file at a time, rerun `python3 scripts/generate_synthesis_layers.py`, and inspect [[credibility-policy-evals]] before applying new scores.",
        ]
    )
    return "\n".join(lines)


def render_policy_eval_report(results: list[dict]) -> str:
    failures = [row for row in results if row["result"] != "pass"]
    lines = [
        frontmatter(
            {
                "title": "Credibility Policy Evals",
                "category": "evaluations",
                "status": "active",
                "confidence": "high",
                "sourceLabels": ["Credibility policy", "Evaluation-backed scoring"],
            }
        ),
        "# Credibility Policy Evals",
        "",
        "This page checks whether topic-specific credibility policies score known strong exemplars high enough. If a fixture fails, adjust the policy weights or fixture assumptions instead of overriding the score by hand.",
        "",
        "## Result Summary",
        f"- Fixtures: {len(results)}",
        f"- Passing: {len(results) - len(failures)}",
        f"- Failing: {len(failures)}",
        "",
        "## Fixture Results",
        "| Policy | Name | Score | Expected Min | Result | Why This Fixture Exists |",
        "| --- | --- | ---: | ---: | --- | --- |",
    ]
    for row in results:
        lines.append(
            f"| [[{row['policy']}]] | {row['name']} | {row['score']:.2f} | {row['expectedMin']} | {row['result']} | {row['why']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation Notes",
            "- Fame and view signals are policy-specific. They are useful for public influence topics and weak for safety, inference, and evaluation correctness.",
            "- A person can score high for one topic and low for another without contradiction.",
            "- Scores are provenance records for how the algorithm judged a candidate, not permanent judgments of a person.",
        ]
    )
    return "\n".join(lines)


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
        "Comparative decision artifacts for tools, workflows, infrastructure, and policies. Recommendations are tentative unless backed by a concrete trial.",
        records,
    )
    write(WIKI / "evaluations" / "index.md", index)
    write(WIKI / "evaluations" / "evaluations.md", index)
    write(WIKI / "evaluations" / "registry.json", json.dumps(records, indent=2, ensure_ascii=False))
    return records


def generate_policies() -> tuple[list[dict], list[dict]]:
    policies = {policy["slug"]: policy for policy in CREDIBILITY_POLICIES}
    fixtures_by_policy: dict[str, list[dict]] = {slug: [] for slug in policies}
    results = []
    for fixture in POLICY_EVALS:
        policy = policies[fixture["policy"]]
        score = score_fixture(policy, fixture)
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
    for policy in CREDIBILITY_POLICIES:
        policy_doc = {
            **policy,
            "weightsTotal": sum(policy["weights"].values()),
            "evalFixtures": fixtures_by_policy[policy["slug"]],
        }
        write(POLICY_RAW / f"{policy['slug']}.json", json.dumps(policy_doc, indent=2, ensure_ascii=False))
        write(WIKI / "policies" / f"{policy['slug']}.md", render_policy_page(policy, fixtures_by_policy[policy["slug"]]))
        records.append(
            {
                "id": policy["slug"],
                "title": policy["title"],
                "path": f"wiki/policies/{policy['slug']}.md",
                "topic": policy["topic"],
                "version": policy["version"],
            }
        )
    write(RAW / "credibility-policy-evals.json", json.dumps(results, indent=2, ensure_ascii=False))
    write(WIKI / "evaluations" / "credibility-policy-evals.md", render_policy_eval_report(results))
    index = render_index(
        "Policies",
        "policies",
        "Topic-specific credibility scoring policies. Each policy has its own weights and eval fixtures so scores remain auditable.",
        records,
    )
    write(WIKI / "policies" / "index.md", index)
    write(WIKI / "policies" / "policies.md", index)
    write(WIKI / "policies" / "registry.json", json.dumps(records, indent=2, ensure_ascii=False))
    failures = [row for row in results if row["result"] != "pass"]
    if failures:
        names = ", ".join(f"{row['policy']}:{row['name']}" for row in failures)
        raise SystemExit(f"credibility policy eval failures: {names}")
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
    text = path.read_text(encoding="utf-8", errors="ignore")
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
        table.extend(["", "## Representative Evidence Links"])
        for category in ["talks", "resources", "slides", "transcripts", "tools", "questions"]:
            samples = [row["ref"] for row in rows if row["category"] == category][:6]
            if samples:
                table.append(f"### {category.title()}")
                table.extend(f"- [[{ref}]]" for ref in samples)
                table.append("")
        text = path.read_text(encoding="utf-8")
        write(path, upsert_section(text, "Evidence Table", "\n".join(table)))
        summary[topic] = counts
    write(RAW / "topic-evidence-table-summary.json", json.dumps(summary, indent=2, ensure_ascii=False))
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
        "This standalone wiki is organized as a conference intelligence vault: official schedule first, then public video evidence, transcripts, slide/OCR evidence, topic synthesis, questions, harnesses, playbooks, evaluations, and policies.",
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
        "- [Harnesses](/harnesses/) - reusable workflows observed or implied by the evidence",
        "- [Playbooks](/playbooks/) - post-conference action workflows",
        "- [Evaluations](/evaluations/) - comparative decision artifacts and scorecards",
        "- [Policies](/policies/) - topic-specific credibility scoring policies",
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
        "## Policy And Evaluation Entry Points",
        "- [[credibility-policy-evals]]",
        "- [[credibility-policy-review-loop]]",
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
            "- `python3 scripts/generate_synthesis_layers.py` - generate harnesses, playbooks, evaluations, topic evidence tables, topic-specific credibility policies, and policy eval reports.",
            "- Credibility policy JSON files live under `raw/sources/credibility-policies/` and should be reviewed one policy at a time.",
            "- Policy eval results live at `raw/sources/credibility-policy-evals.json` and [[credibility-policy-evals]].",
            "- Do not reuse a credibility policy across unrelated topics without changing weights and adding eval fixtures.",
        ]
    )
    write(path, upsert_section(text, "Synthesis And Credibility Policy Layer", body))


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
        f"- Harness pages: {counts['harnesses']}",
        f"- Playbook pages: {counts['playbooks']}",
        f"- Evaluation pages: {counts['evaluations']}",
        f"- Credibility policies: {counts['policies']}",
        f"- Credibility policy eval fixtures: {counts['policy_evals']}",
        f"- Topic evidence tables updated: {counts['topic_tables']}",
        f"- Livestream thematic anchor pages: {counts['livestream_anchor_pages']}",
        "",
        "Key outputs:",
        "- `wiki/harnesses/`",
        "- `wiki/playbooks/`",
        "- `wiki/evaluations/`",
        "- `wiki/policies/`",
        "- `raw/sources/credibility-policies/`",
        "- `raw/sources/credibility-policy-evals.json`",
        "- `raw/sources/topic-evidence-table-summary.json`",
        "- `wiki/resources/livestream-thematic-anchors.md`",
        "",
        "Boundary: this run created policy/evaluation artifacts locally only. It did not push to GitHub.",
    ]
    write(ROOT / rel, "\n".join(lines))
    return rel


def main() -> int:
    harnesses = generate_harnesses()
    evaluations = generate_evaluations()
    playbooks = generate_playbooks()
    policy_records, policy_results = generate_policies()
    topic_summary = update_topic_evidence_tables()
    generate_livestream_thematic_anchors()
    generate_main_index()
    update_agent_source_index()
    receipt = write_receipt(
        {
            "harnesses": len(harnesses),
            "playbooks": len(playbooks),
            "evaluations": len(evaluations),
            "policies": len(policy_records),
            "policy_evals": len(policy_results),
            "topic_tables": len(topic_summary),
            "livestream_anchor_pages": 1,
        }
    )
    print(
        json.dumps(
            {
                "harness_pages": len(harnesses),
                "playbook_pages": len(playbooks),
                "evaluation_pages": len(evaluations),
                "policies": len(policy_records),
                "policy_eval_fixtures": len(policy_results),
                "topic_tables": len(topic_summary),
                "livestream_anchor_pages": 1,
                "receipt": receipt,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
