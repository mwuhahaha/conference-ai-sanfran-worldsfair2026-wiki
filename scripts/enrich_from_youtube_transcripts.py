"""Enrich the World's Fair wiki from cached YouTube transcripts.

This pass is intentionally deterministic: it creates/updates resource pages,
quote pages, and topic support sections from transcript text already fetched
into raw/sources/youtube-transcripts or raw/sources/youtube-livestream-transcripts.
"""

from __future__ import annotations

import html
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "sources"
WIKI = ROOT / "wiki"
RESOURCES = WIKI / "resources"
TOPICS = WIKI / "topics"
QUOTES = WIKI / "quotes"

STOPWORDS = {
    "about", "after", "again", "agent", "agents", "also", "because", "being", "build", "building",
    "could", "doing", "going", "have", "here", "just", "like", "make", "model", "models", "more",
    "need", "needs", "really", "right", "should", "show", "some", "talk", "than", "that", "their",
    "them", "then", "there", "these", "they", "thing", "things", "this", "those", "through", "using",
    "video", "want", "were", "what", "when", "where", "which", "with", "would", "your",
}

TOPIC_RULES = [
    ("agent-evaluations", "Agent Evaluations", ["eval", "evaluation", "benchmark", "rubric", "judge", "score", "regression", "quality"]),
    ("agent-memory", "Agent Memory", ["memory", "context", "state", "recall", "long horizon", "knowledge graph", "cache"]),
    ("agent-security", "Agent Security", ["security", "permission", "sandbox", "auth", "secret", "attack", "supply chain", "guardrail"]),
    ("ai-sandboxes", "AI Sandboxes", ["sandbox", "environment", "isolation", "container", "runtime", "browser", "computer use"]),
    ("autoresearch", "AutoResearch", ["research", "autoresearch", "scientist", "paper", "experiment", "hypothesis"]),
    ("coding-agents", "Coding Agents", ["code", "coding", "pull request", "diff", "ide", "repo", "software engineer", "swe"]),
    ("inference-engineering", "Inference Engineering", ["inference", "gpu", "latency", "throughput", "token", "tokens", "vllm", "serving"]),
    ("mcp", "MCP", ["mcp", "model context protocol", "tool", "tools", "server", "client", "apps"]),
    ("software-factories", "Software Factories", ["software factory", "factory", "self improving", "autonomous engineering", "sdlc"]),
    ("voice-agents", "Voice Agents", ["voice", "audio", "speech", "transcription", "realtime", "conversation"]),
    ("agentic-search", "Agentic Search", ["search", "retrieval", "rag", "hybrid", "bm25", "vector", "web data"]),
]

ARTICLE_HEADINGS = [
    "Synopsis",
    "Origin And Context",
    "Why It Matters",
    "How To Use It",
    "Where It Is Useful",
    "When To Use It",
    "Active Use Cases",
    "Why It Matters Here",
]

TOPIC_ARTICLES = {
    "agent-evaluations": {
        "synopsis": "Agent evaluations are the measurement layer for systems that plan, call tools, write code, retrieve context, or take actions over time. They combine offline tests, production traces, human review, model-as-judge scoring, regression suites, and task-specific rubrics so teams can tell whether an agent is actually improving rather than merely sounding better.",
        "origin": "The practice grows out of software testing, information-retrieval benchmarks, ML evaluation, and LLM prompt evaluation. Agentic systems made the problem harder because success depends on multi-step behavior: tool choice, state handling, recovery, cost, latency, safety, and final task outcome.",
        "why": "Without evaluations, agent teams cannot safely change prompts, models, tools, routing, memory policies, or autonomy levels. Evals turn vague quality complaints into visible failure modes and make it possible to ship agents with rollback criteria, measurable acceptance thresholds, and a shared language for product and engineering decisions.",
        "how": "Start with real traces and representative tasks. Define the outcome that matters, add rubrics for intermediate behavior, keep golden examples for regressions, and separate fast pre-merge checks from slower production audits. Use model judges only when their decisions are calibrated against human review, and track cost, latency, and failure categories alongside quality.",
        "where": "Evaluations are useful in coding agents, support agents, research agents, data agents, voice agents, retrieval systems, and any workflow where the agent can take a plausible but wrong path. They are especially valuable where correctness, trust, or operational cost matters.",
        "when": "Use evals before launching, whenever prompts or models change, when adding new tools, after incidents, and when expanding an agent into a new user segment or task family. Lightweight evals should run continuously; deeper reviews should run before major releases.",
        "use_cases": [
            "Regression tests for prompt, model, and tool changes.",
            "Production trace review for agent reliability and cost drift.",
            "Benchmarking coding agents, retrieval agents, and long-horizon workflows.",
            "Reward-signal generation for continual learning and fine-tuning loops.",
        ],
    },
    "agent-memory": {
        "synopsis": "Agent memory is the set of mechanisms that lets an agent carry useful context across steps, sessions, users, repositories, documents, or decisions. It includes short-term working context, long-term stores, cached artifacts, decision traces, vector or graph retrieval, and policies that decide what should be remembered, refreshed, or forgotten.",
        "origin": "The topic comes from classic AI state management, knowledge representation, retrieval systems, personal assistants, and database-backed application design. The long-context era changed the tradeoff: teams can stuff more into prompts, but still need structured memory so agents can reason over the right facts at the right time.",
        "why": "Memory determines whether an agent can act consistently instead of restarting from scratch. It improves personalization, reduces repeated work, supports multi-step workflows, and makes decisions auditable. Poor memory creates stale assumptions, privacy risk, context bloat, and confident mistakes.",
        "how": "Separate working context from durable memory. Store source-backed facts, decisions, user preferences, and artifacts with timestamps and provenance. Retrieve by task intent, not just lexical similarity. Add policies for freshness, deletion, permissions, and summarization, and test memory behavior with scenario-based evals.",
        "where": "Memory is useful in coding agents, customer support, research assistants, enterprise knowledge agents, personal productivity tools, and any workflow that spans multiple sessions or documents.",
        "when": "Use durable memory when repeated interaction or long-horizon work matters. Avoid it for one-shot tasks, sensitive data without clear retention rules, or cases where stale state would be more harmful than asking again.",
        "use_cases": [
            "Remembering repository architecture and prior implementation decisions.",
            "Maintaining user preferences and project constraints across sessions.",
            "Decision-trace retrieval for enterprise workflows.",
            "Long-context cache and knowledge-graph backed agent workflows.",
        ],
    },
    "agent-security": {
        "synopsis": "Agent security covers the controls that keep autonomous or semi-autonomous AI systems within trusted boundaries. It includes authentication, authorization, tool permissions, sandboxing, prompt-injection resistance, secret handling, audit logs, data-boundary enforcement, and recovery paths when an agent behaves unexpectedly.",
        "origin": "It combines application security, cloud IAM, browser and plugin sandboxing, supply-chain security, and adversarial ML. Tool-using agents raise the stakes because natural-language inputs can influence systems that touch files, APIs, payments, infrastructure, or private data.",
        "why": "Agents convert text into action. That makes ordinary content, retrieved documents, web pages, or UI state part of the attack surface. Security is what lets teams give agents useful tools without handing them unlimited authority.",
        "how": "Use least-privilege tool scopes, explicit approval gates for high-risk actions, isolated execution environments, secret redaction, provenance checks, and audit trails. Treat retrieved content as untrusted input, test prompt-injection cases, and design rollback paths for destructive operations.",
        "where": "Agent security matters in coding agents, MCP servers, browser agents, enterprise assistants, finance and compliance workflows, internal operations tools, and any system connected to privileged APIs or private data.",
        "when": "Apply strong controls whenever an agent can read sensitive data, write state, call external APIs, spend money, deploy code, or influence another system. Lower-risk chat-only agents still need data handling and logging rules.",
        "use_cases": [
            "Permission-gated tool execution for enterprise agents.",
            "Sandboxed coding and browser automation.",
            "Prompt-injection and data-exfiltration testing for retrieval agents.",
            "Audit logs for regulated or high-trust agent workflows.",
        ],
    },
    "ai-sandboxes": {
        "synopsis": "AI sandboxes are controlled execution environments where agents can run code, browse, inspect files, call tools, or manipulate artifacts without putting the host system at unnecessary risk. A sandbox gives the agent enough power to do real work while limiting filesystem, network, credential, and process access.",
        "origin": "The pattern comes from operating-system isolation, browser sandboxes, CI runners, notebooks, container platforms, and secure code-execution services. Agentic coding and computer-use systems made sandboxing a default requirement rather than a specialty feature.",
        "why": "Agents need to experiment, test, and inspect state. Sandboxes let them do that while containing failures, malicious inputs, runaway processes, and accidental destructive changes.",
        "how": "Choose isolation based on risk: separate processes for low-risk tasks, containers or microVMs for untrusted code, and policy-controlled network and secret access for production work. Capture logs, diffs, artifacts, and resource usage so human operators can review what happened.",
        "where": "They are useful in coding assistants, data-analysis agents, browser agents, app builders, test runners, educational tools, and any system that executes generated code or commands.",
        "when": "Use a sandbox whenever an agent can execute code, inspect user files, download dependencies, browse unknown sites, or run untrusted scripts. Loosen limits only after the workflow and threat model are well understood.",
        "use_cases": [
            "Running generated code and tests before suggesting a patch.",
            "Browser or computer-use automation with constrained state.",
            "Temporary workspaces for data analysis and document transformation.",
            "Reproducible agent task environments for evaluations.",
        ],
    },
    "autoresearch": {
        "synopsis": "AutoResearch is the use of agents to search, read, compare, synthesize, and sometimes design experiments over a body of evidence. The goal is not just summarization; it is repeatable research workflow support with source tracking, uncertainty management, and follow-up planning.",
        "origin": "It grew from literature search, systematic review methods, research assistants, web search, RAG, and scientific-discovery tooling. LLM agents added the ability to decompose questions, inspect sources, generate hypotheses, and produce structured research artifacts.",
        "why": "Research work is expensive because it involves discovery, filtering, evidence comparison, and synthesis under uncertainty. Agents can accelerate the mechanical parts, but only if they preserve citations, distinguish claims from evidence, and expose gaps.",
        "how": "Start with a clear research question, use source-specific retrieval, keep a claim-evidence table, record search terms and inclusion criteria, and separate facts, interpretations, and open questions. Use humans for scope, judgment, and final conclusions.",
        "where": "AutoResearch is useful for technical due diligence, market maps, literature reviews, competitive analysis, policy research, product discovery, and engineering design investigations.",
        "when": "Use it when the answer depends on multiple sources or evolving evidence. Avoid relying on it as a black-box oracle for high-stakes conclusions without human review.",
        "use_cases": [
            "Evidence-grounded briefing docs and source maps.",
            "Research agents that compare papers, products, or implementation patterns.",
            "Experiment-planning support for AI and data teams.",
            "Conference or domain wiki synthesis from talks, transcripts, and slides.",
        ],
    },
    "coding-agents": {
        "synopsis": "Coding agents are AI systems that can inspect repositories, reason about requirements, edit files, run commands, test changes, and sometimes open pull requests or operate development tools. They move AI coding from autocomplete toward task execution.",
        "origin": "They evolved from code completion, IDE assistants, program synthesis, CI automation, and software bots. The recent shift is tool use: agents can read context, make coordinated edits, run tests, and respond to feedback inside real development workflows.",
        "why": "Software work is full of local context, repetitive edits, dependency checks, and validation loops. Coding agents can compress that cycle, but only when they respect repository conventions, tests, review standards, and operational safety.",
        "how": "Give the agent a narrow task, repository context, tests or acceptance criteria, and permission boundaries. Require it to read before editing, keep diffs scoped, run validation, report residual risk, and leave the workspace clean.",
        "where": "They are useful in feature slices, bug fixes, test generation, refactors, migrations, docs updates, dependency audits, and operational scripts.",
        "when": "Use coding agents when the task has clear acceptance criteria and the repo has enough structure to validate changes. Keep humans in the loop for architecture decisions, risky production operations, and ambiguous product calls.",
        "use_cases": [
            "Bug fixes with local tests and deploy verification.",
            "Repository-wide mechanical updates with reviewable diffs.",
            "CI failure diagnosis and targeted remediation.",
            "Agentic software factories that coordinate planning, coding, testing, and release steps.",
        ],
    },
    "inference-engineering": {
        "synopsis": "Inference engineering is the practice of making AI model serving reliable, fast, cost-aware, and fit for product constraints. It covers model selection, batching, caching, routing, quantization, GPU utilization, latency budgets, observability, and fallback behavior.",
        "origin": "It extends production ML serving, distributed systems, GPU infrastructure, and web-performance engineering. LLMs added new constraints: token streaming, long prompts, context caching, tool latency, and rapidly changing model/provider economics.",
        "why": "The same prompt can be unusable or profitable depending on latency, throughput, context size, and cost. Inference engineering turns model capability into a dependable product surface.",
        "how": "Measure end-to-end latency and token costs, separate prefill from generation costs, cache stable context, route tasks to the smallest adequate model, batch where possible, and monitor quality regressions when optimizing speed or cost.",
        "where": "It matters in chat products, coding agents, voice agents, search and RAG systems, enterprise assistants, on-device AI, and high-volume API products.",
        "when": "Invest in inference engineering once prototypes need predictable user experience, margins, scale, or reliability. It becomes critical when workloads are high-volume, latency-sensitive, or model-provider dependent.",
        "use_cases": [
            "Reducing token and GPU cost for agent workflows.",
            "Serving long-context or cached-context applications.",
            "Routing between frontier, small, local, and specialized models.",
            "Optimizing voice and interactive applications for low latency.",
        ],
    },
    "mcp": {
        "synopsis": "Model Context Protocol, or MCP, is a standard pattern for connecting AI applications to tools, data, and interactive capabilities through structured servers and clients. In this wiki it also includes MCP Apps and agent-facing interfaces that expose richer actions or UI surfaces to models.",
        "origin": "MCP emerged from the need to standardize how AI clients discover and call tools, access resources, and integrate with external systems. It sits in the lineage of plugin APIs, language-server style tooling, RPC, browser extensions, and developer-tool protocols.",
        "why": "Agents are only as useful as the tools and context they can safely access. MCP reduces one-off integrations, gives tool providers a common surface, and helps clients reason about capabilities, permissions, and interaction patterns.",
        "how": "Define focused MCP servers with clear tools, schemas, resources, and permission boundaries. Keep tool names concrete, return structured results, test with inspectors, and design for least privilege. For MCP Apps, treat UI and iframe boundaries as part of the security and product contract.",
        "where": "MCP is useful in IDEs, desktop assistants, enterprise data connectors, browser agents, design tools, developer platforms, and internal operations systems.",
        "when": "Use MCP when multiple AI clients need access to the same tools or when a tool provider wants a standard agent-facing integration. For a single narrow app, direct APIs may be simpler until reuse or interoperability matters.",
        "use_cases": [
            "Connecting agents to repositories, browsers, docs, databases, and SaaS tools.",
            "MCP Apps that return interactive UI from tool servers.",
            "Agent-ready web and developer-tool integrations.",
            "Local inspectors and compliance checks for tool servers.",
        ],
    },
    "software-factories": {
        "synopsis": "Software factories are coordinated systems for turning ideas, issues, designs, tests, agents, and human review into shipped software. In an AI-native version, multiple agents may handle planning, coding, testing, review, documentation, and release support under explicit workflow rules.",
        "origin": "The idea comes from assembly-line metaphors in software engineering, CI/CD, DevOps, internal developer platforms, and automated code generation. AI agents make the factory metaphor more literal because parts of the SDLC can be delegated to tool-using systems.",
        "why": "A single coding assistant is useful, but organizations need repeatability, governance, and quality gates. Software factories focus on the whole production system: intake, context, implementation, validation, review, deployment, and learning.",
        "how": "Model the workflow as stages with inputs, outputs, owners, and acceptance checks. Give agents scoped roles, shared artifacts, test gates, traceability, and rollback paths. Measure cycle time, defect rate, review burden, and production outcomes.",
        "where": "They fit engineering organizations, platform teams, internal tools groups, migration projects, and product teams with repeatable implementation patterns.",
        "when": "Use a software-factory approach when many similar tasks flow through the same path or when agent work needs governance. Avoid overbuilding it for occasional one-off tasks.",
        "use_cases": [
            "Agent-assisted feature delivery pipelines.",
            "Automated maintenance, migration, and dependency-update programs.",
            "Multi-agent planning, coding, testing, and review workflows.",
            "Internal developer platforms with AI-native task orchestration.",
        ],
    },
    "voice-agents": {
        "synopsis": "Voice agents are AI systems that understand, reason, and respond through speech, often in real time. They combine speech recognition, speaker diarization, language models, tool use, dialogue state, text-to-speech, and sometimes visual or screen output.",
        "origin": "They build on IVR systems, speech recognition, voice assistants, call-center automation, real-time media systems, and conversational AI. Modern multimodal and realtime models make them more fluid, but production voice still depends on latency, turn-taking, and trust.",
        "why": "Voice is natural for hands-free, high-attention, or emotionally sensitive workflows. It also exposes failures quickly: delays, interruptions, wrong speaker attribution, and unnatural responses break trust faster than in text.",
        "how": "Design around conversation state, latency budgets, interruption handling, speaker identity, fallback paths, and clear tool permissions. Test with realistic audio conditions, accents, overlapping speakers, and production transcripts.",
        "where": "Voice agents are useful in customer support, healthcare intake, sales calls, meeting assistants, field work, accessibility tools, tutoring, and companion interfaces.",
        "when": "Use voice when speaking is faster or more accessible than typing, or when the workflow happens away from a keyboard. Prefer text when precision, reviewability, or complex visual comparison is primary.",
        "use_cases": [
            "Realtime support and appointment workflows.",
            "Meeting and call understanding with speaker attribution.",
            "Voice-in visual-out interfaces for richer task completion.",
            "Hands-free operational assistants.",
        ],
    },
    "agentic-search": {
        "synopsis": "Agentic search is retrieval where an AI system actively plans, queries, follows leads, compares sources, and decides when it has enough evidence. It goes beyond one-shot RAG by treating search as an iterative reasoning and tool-use process.",
        "origin": "It combines web search, enterprise search, information retrieval, RAG, semantic search, BM25, vector databases, knowledge graphs, and research-agent workflows. Agents add query reformulation, source triage, multi-hop exploration, and evidence synthesis.",
        "why": "Many tasks fail because the agent either retrieves the wrong context or stops too early. Agentic search improves coverage, reduces hallucination, and helps systems expose the evidence behind an answer.",
        "how": "Define the question, retrieve broadly, rerank by task relevance, inspect primary sources, track claims and citations, and loop when evidence conflicts or gaps remain. Use hybrid retrieval and structured indexes where pure vector search misses exact terms or relationships.",
        "where": "It is useful in research, support knowledge bases, compliance review, code search, enterprise assistants, competitive intelligence, and document-heavy operations.",
        "when": "Use agentic search when answers require multiple sources, fresh evidence, exact facts, or cross-document reasoning. Simple lookup or direct database queries are better for narrow deterministic questions.",
        "use_cases": [
            "Research agents that cite and compare sources.",
            "Hybrid RAG over documents, SQL, UI telemetry, and web data.",
            "Semantic code retrieval for coding agents.",
            "Enterprise knowledge agents with source-grounded answers.",
        ],
    },
}


def slugify(value: str, *, max_len: int = 90) -> str:
    value = value.lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:max_len].strip("-") or "untitled"


def md_escape(value: str | None) -> str:
    return (value or "").replace("|", "\\|").strip()


def frontmatter(data: dict) -> str:
    lines = ["---"]
    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {json.dumps(item, ensure_ascii=False)}")
        else:
            lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines)


def read_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(errors="ignore"))


def load_new_videos() -> dict[str, dict]:
    videos: dict[str, dict] = {}
    metadata: dict[str, dict] = {}
    discovered: set[str] = set()
    for path in [RAW / "new-video-discovery-2026-07-06.json", RAW / "aidotengineer-channel-videos-latest.json", RAW / "aidotengineer-channel-streams-latest.json"]:
        data = read_json(path, {})
        entries = []
        if isinstance(data, dict):
            new_entries = []
            new_entries.extend(data.get("new_cut_videos") or [])
            new_entries.extend(data.get("new_wf26_streams") or [])
            entries.extend(new_entries)
            entries.extend(data.get("entries") or [])
            if path.name.startswith("new-video-discovery"):
                for entry in new_entries:
                    vid = entry.get("id") or entry.get("video_id")
                    if vid:
                        discovered.add(vid)
        elif isinstance(data, list):
            entries.extend(data)
        for entry in entries:
            vid = entry.get("id") or entry.get("video_id")
            if vid:
                metadata[vid] = entry

    wanted = set(discovered)
    for base in [RAW / "youtube-transcripts", RAW / "youtube-livestream-transcripts"]:
        if base.exists():
            wanted.update(path.stem for path in base.glob("*.txt") if path.stat().st_size > 200)

    for vid in sorted(wanted):
        entry = metadata.get(vid, {})
        title = entry.get("title") or entry.get("youtube_title")
        if not title:
            resource = RESOURCES / f"youtube-{vid}.md"
            if resource.exists():
                match = re.search(r"^#\s+(.+)$", resource.read_text(errors="ignore"), re.M)
                title = match.group(1).strip() if match else None
        videos[vid] = {
            "video_id": vid,
            "youtube_title": title or vid,
            "youtube_url": entry.get("url") or entry.get("webpage_url") or f"https://www.youtube.com/watch?v={vid}",
            "duration": entry.get("duration"),
            "source_kind": "channel_stream" if (RAW / "youtube-livestream-transcripts" / f"{vid}.txt").exists() else "channel_video",
        }
    return videos


def transcript_path(video_id: str) -> Path | None:
    for base in [RAW / "youtube-transcripts", RAW / "youtube-livestream-transcripts"]:
        path = base / f"{video_id}.txt"
        if path.exists() and path.stat().st_size > 200:
            return path
    return None


def title_speaker(title: str) -> tuple[str, list[str], str]:
    parts = re.split(r"\s+[—-]\s+", title, maxsplit=1)
    talk = parts[0].strip()
    speaker_blob = parts[1].strip() if len(parts) > 1 else ""
    speaker_blob = re.sub(r"\b(ft\.|with|w/)\b", "", speaker_blob, flags=re.I)
    speakers = []
    for bit in re.split(r",|&| and ", speaker_blob):
        bit = re.sub(r"\([^)]*\)", "", bit).strip()
        bit = re.sub(r"\b(Anthropic|Google|AWS|Cloudflare|Stripe|RunPod|Snorkel|GitHub|OpenClaw|OpenGov|Modal|Cline|Postman|Nvidia|Databricks|YouTube|AI|Inc|Labs?)\b.*", "", bit).strip()
        if 2 <= len(bit.split()) <= 4 and bit:
            speakers.append(bit)
    company = ""
    if "," in speaker_blob:
        company = speaker_blob.split(",")[-1].strip()
    return talk, speakers[:3], company


def session_slug(session: dict) -> str:
    registry = read_json(WIKI / "talks" / "registry.json", [])
    by_title = {item.get("title", "").lower(): item.get("id") for item in registry}
    return by_title.get(session.get("title", "").lower()) or slugify(f"{session.get('title', '')}")


def normalize(value: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", value.lower()) if len(w) > 2 and w not in STOPWORDS}


def related_sessions(video: dict, sessions: list[dict]) -> list[tuple[int, dict]]:
    title = video["youtube_title"]
    talk_title, speakers, _company = title_speaker(title)
    title_terms = normalize(talk_title)
    speaker_terms = {s.lower() for s in speakers}
    matches = []
    for session in sessions:
        score = 0
        stitle = session.get("title", "")
        overlap = len(title_terms & normalize(stitle))
        if overlap:
            score += overlap * 3
        for speaker in session.get("speakers") or []:
            low = speaker.lower()
            if low in title.lower() or any(low == ss for ss in speaker_terms):
                score += 80
        if score >= 9:
            matches.append((score, session))
    return sorted(matches, key=lambda item: item[0], reverse=True)[:5]


def transcript_summary(text: str) -> list[str]:
    words = normalize(text)
    counts = Counter(w for w in words if len(w) > 3)
    top = [w for w, _ in counts.most_common(10)]
    return top[:8]


def topic_hits(title: str, text: str) -> list[tuple[str, str, int]]:
    hay = f"{title}\n{text[:25000]}".lower()
    hits = []
    for slug, label, keys in TOPIC_RULES:
        score = 0
        for key in keys:
            score += hay.count(key.lower())
        if score:
            hits.append((slug, label, score))
    return sorted(hits, key=lambda row: row[2], reverse=True)[:4]


def split_sentences(text: str) -> list[str]:
    compact = re.sub(r"\s+", " ", text).strip()
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", compact) if s.strip()]


QUOTE_PATTERNS = [
    r"\bthe (hard|important|interesting|weird|scary|funny) part\b",
    r"\bwhat (we|you|I) learned\b",
    r"\bthe problem is\b",
    r"\bthe key is\b",
    r"\bwe need to\b",
    r"\byou need to\b",
    r"\bnot just\b",
    r"\bin production\b",
    r"\btrust\b",
    r"\bevaluation\b",
    r"\bsecurity\b",
    r"\bmemory\b",
    r"\bcontext\b",
]


def quote_candidates(video_id: str, video: dict, text: str, topics: list[tuple[str, str, int]]) -> list[dict]:
    candidates = []
    topic_slug = topics[0][0] if topics else "resources"
    topic_label = topics[0][1] if topics else "Supporting Resources"
    related_topics = [{"slug": slug, "label": label, "score": score} for slug, label, score in topics]
    for sentence in split_sentences(text):
        words = sentence.split()
        if len(words) < 12 or len(words) > 42:
            continue
        low = sentence.lower()
        score = sum(5 for pat in QUOTE_PATTERNS if re.search(pat, low))
        score += min(10, len(set(normalize(sentence)) & set(normalize(video["youtube_title"]))) * 2)
        if score >= 5:
            candidates.append({
                "quote": sentence,
                "score": score,
                "video_id": video_id,
                "video_title": video["youtube_title"],
                "topic": topic_slug,
                "topic_label": topic_label,
                "related_topics": related_topics,
            })
    dedup = []
    seen = set()
    for row in sorted(candidates, key=lambda r: r["score"], reverse=True):
        key = re.sub(r"[^a-z0-9]+", " ", row["quote"].lower())[:100]
        if key in seen:
            continue
        seen.add(key)
        dedup.append(row)
        if len(dedup) >= 3:
            break
    return dedup


def quote_importance(row: dict) -> str:
    quote = row["quote"].strip()
    low = quote.lower()
    topic_label = row.get("topic_label") or "the related topic"
    video_title = row.get("video_title") or "the source talk"
    signals = []
    if "you need to" in low or "we need to" in low:
        signals.append("states an explicit operating requirement")
    if "problem is" in low:
        signals.append("names a concrete failure mode")
    if "key is" in low or "important" in low:
        signals.append("marks a principle the speaker treats as central")
    if "not just" in low:
        signals.append("draws a useful boundary between shallow and production-ready practice")
    if "production" in low:
        signals.append("connects the idea to real deployment pressure")
    if "evaluation" in low or "measuring" in low or "measure" in low:
        signals.append("turns the discussion toward measurement and accountability")
    if "security" in low or "trust" in low:
        signals.append("connects the technical point to trust and risk")
    if "memory" in low or "context" in low:
        signals.append("surfaces context management as an engineering concern")
    if not signals:
        signals.append("captures a compact claim from the transcript that helps navigate the broader talk")
    unique_signals = list(dict.fromkeys(signals))
    if len(unique_signals) == 1:
        signal_text = unique_signals[0]
    elif len(unique_signals) == 2:
        signal_text = f"{unique_signals[0]} and {unique_signals[1]}"
    else:
        signal_text = f"{'; '.join(unique_signals[:-1])}; and {unique_signals[-1]}"
    return (
        f"This quote was chosen because it {signal_text}. In the context of "
        f"[[youtube-{row['video_id']}|{md_escape(video_title)}]], it is a useful pointer into "
        f"[[{row['topic']}|{topic_label}]] rather than just a memorable line: it captures a reusable engineering judgment readers can compare against the source transcript, slides, and related scheduled sessions."
    )


def quote_topic_links(row: dict) -> list[str]:
    seen = set()
    links = []
    related = row.get("related_topics") or [{"slug": row["topic"], "label": row["topic_label"], "score": 0}]
    for topic in related:
        slug = topic.get("slug")
        label = topic.get("label") or slug
        if not slug or slug in seen:
            continue
        seen.add(slug)
        suffix = "primary transcript signal" if slug == row.get("topic") else "secondary transcript signal"
        links.append(f"- [[{slug}|{label}]] — {suffix}")
    return links


def upsert_section(path: Path, heading: str, body: str) -> None:
    text = path.read_text(errors="ignore") if path.exists() else ""
    section = f"## {heading}\n{body.strip()}\n"
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    if pattern.search(text):
        text = pattern.sub(section, text).rstrip() + "\n"
    else:
        text = text.rstrip() + "\n\n" + section
    path.write_text(text, encoding="utf-8")


def write_resource(video_id: str, video: dict, text: str, topics: list[tuple[str, str, int]], matches: list[tuple[int, dict]]) -> None:
    RESOURCES.mkdir(parents=True, exist_ok=True)
    words = len(text.split())
    topic_links = ", ".join(f"[[{slug}|{label}]]" for slug, label, _score in topics) or "None detected"
    keywords = ", ".join(f"`{w}`" for w in transcript_summary(text))
    source_kind = "WF26 livestream" if video.get("source_kind") == "channel_stream" else "AI Engineer cut video"
    what_it_is = (
        "An official AI Engineer YouTube WF26 livestream for AI Engineer World's Fair San Francisco 2026. "
        "This is a primary event video source for what the recording, transcript, and captured slides show; official schedule pages remain canonical for schedule metadata."
        if video.get("source_kind") == "channel_stream"
        else
        "An official AI Engineer YouTube cut video for AI Engineer World's Fair San Francisco 2026. "
        "This is a primary event video source for what the published talk recording, transcript, and captured slides show; official schedule pages remain canonical for schedule metadata."
    )
    lines = [
        frontmatter({
            "title": video["youtube_title"],
            "category": "resources",
            "sourceLabels": ["Public YouTube metadata", "YouTube transcript"],
            "videoId": video_id,
            "last_enriched": datetime.now(timezone.utc).isoformat(),
        }),
        f"# {video['youtube_title']}",
        "",
        "## What It Is",
        what_it_is,
        "",
        "## Source Classification",
        "- Source role: primary event video source for AI Engineer World's Fair San Francisco 2026.",
        f"- Channel/source: official AI Engineer YouTube channel {source_kind}.",
        "- Use: primary evidence for media, transcript, and slide content; official schedule pages remain canonical for session metadata.",
        "",
        "## Transcript Status",
        f"Cached transcript text is available at `raw/sources/{'youtube-livestream-transcripts' if video.get('source_kind') == 'channel_stream' else 'youtube-transcripts'}/{video_id}.txt` ({words:,} words).",
        "",
        "## Topic Signals",
        f"- {topic_links}",
        f"- Transcript keywords: {keywords or 'none'}",
        "",
        "## Link",
        f"[YouTube]({video['youtube_url']})",
    ]
    if matches:
        lines.extend(["", "## Related Scheduled Sessions"])
        for score, session in matches:
            lines.append(f"- [[{session_slug(session)}]] — {md_escape(session.get('title'))} (match score {score})")
    page = RESOURCES / f"youtube-{video_id}.md"
    existing = page.read_text(errors="ignore") if page.exists() else ""
    preserved_sections = set()
    for section in ["Extracted Slides", "Dense Slide Evidence", "Reconstructed Slide Deck"]:
        m = re.search(rf"^## {re.escape(section)}\n.*?(?=^## |\Z)", existing, re.M | re.S)
        if m:
            lines.extend(["", m.group(0).strip()])
            preserved_sections.add(section)
    if "Extracted Slides" not in preserved_sections and (WIKI / "slides" / f"youtube-{video_id}-slides.md").exists():
        lines.extend(["", "## Extracted Slides", f"- [[youtube-{video_id}-slides]]"])
    page.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def non_article_supporting_media(video: dict) -> bool:
    title = (video.get("youtube_title") or "").lower()
    return "vibe reel" in title


def write_non_transcript_resource(video_id: str, video: dict, reason: str) -> None:
    RESOURCES.mkdir(parents=True, exist_ok=True)
    lines = [
        frontmatter({
            "title": video["youtube_title"],
            "category": "resources",
            "sourceLabels": ["Public YouTube metadata"],
            "videoId": video_id,
            "last_enriched": datetime.now(timezone.utc).isoformat(),
        }),
        f"# {video['youtube_title']}",
        "",
        "## What It Is",
        "An official AI Engineer YouTube media item connected to AI Engineer World's Fair San Francisco 2026.",
        "",
        "## Source Classification",
        "- Source role: primary event video source when the item is an official World's Fair San Francisco 2026 livestream or cut video; otherwise supporting official-channel context.",
        "- Channel/source: official AI Engineer YouTube channel.",
        "- Use: verify against the official schedule and transcript/slide availability before using it for specific session claims.",
        "",
        "## Transcript Status",
        reason,
        "",
        "## Link",
        f"[YouTube]({video['youtube_url']})",
    ]
    page = RESOURCES / f"youtube-{video_id}.md"
    existing = page.read_text(errors="ignore") if page.exists() else ""
    preserved_sections = set()
    for section in ["Extracted Slides", "Dense Slide Evidence", "Reconstructed Slide Deck"]:
        m = re.search(rf"^## {re.escape(section)}\n.*?(?=^## |\Z)", existing, re.M | re.S)
        if m:
            lines.extend(["", m.group(0).strip()])
            preserved_sections.add(section)
    if "Extracted Slides" not in preserved_sections and (WIKI / "slides" / f"youtube-{video_id}-slides.md").exists():
        lines.extend(["", "## Extracted Slides", f"- [[youtube-{video_id}-slides]]"])
    page.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_quote_pages(quotes: list[dict]) -> None:
    QUOTES.mkdir(parents=True, exist_ok=True)
    index_lines = [
        frontmatter({"title": "Quotes", "category": "quotes", "sourceLabels": ["YouTube transcript"]}),
        "# Quotes",
        "",
        "Transcript-backed pull quotes surfaced from AI Engineer World's Fair 2026 supporting videos and livestreams. These are short excerpts selected for navigation and should be checked against the linked transcript/resource context before reuse.",
        "",
        "## Index",
    ]
    by_topic: dict[str, list[dict]] = defaultdict(list)
    for row in quotes:
        by_topic[row["topic"]].append(row)
    for topic, rows in sorted(by_topic.items()):
        index_lines.extend(["", f"### [[{topic}|{rows[0]['topic_label']}]]"])
        for index, row in enumerate(sorted(rows, key=lambda r: r["score"], reverse=True)[:12], start=1):
            qslug = slugify(row["quote"], max_len=70)
            page_id = f"quote-{row['video_id']}-{index:02d}-{qslug}"
            index_lines.append(f"- [[{page_id}]] — {md_escape(row['video_title'])}")
            (QUOTES / f"{page_id}.md").write_text(
                "\n".join([
                    frontmatter({
                        "title": row["quote"][:80],
                        "category": "quotes",
                        "sourceLabels": ["YouTube transcript"],
                        "videoId": row["video_id"],
                        "topic": row["topic"],
                    }),
                    f"# {row['quote'][:80]}",
                    "",
                    f"> {row['quote']}",
                    "",
                    "## Why This Quote Matters",
                    quote_importance(row),
                    "",
                    "## Related Topics",
                    *quote_topic_links(row),
                    "",
                    "## Source",
                    f"- [[youtube-{row['video_id']}]] — {md_escape(row['video_title'])}",
                ]).rstrip() + "\n",
                encoding="utf-8",
            )
    (WIKI / "quotes.md").write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")
    registry = [
        {"id": p.stem, "title": p.stem.removeprefix("quote-"), "path": f"wiki/quotes/{p.name}"}
        for p in sorted(QUOTES.glob("*.md"))
    ]
    (QUOTES / "registry.json").write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8")


def registry_title_map(category: str) -> dict[str, str]:
    rows = read_json(WIKI / category / "registry.json", [])
    return {str(row.get("title", "")).lower(): row.get("id") for row in rows if row.get("title") and row.get("id")}


def people_company_map() -> dict[str, str]:
    companies = {}
    for page in sorted((WIKI / "people").glob("*.md")):
        text = page.read_text(errors="ignore")
        title_match = re.search(r'^title:\s*"?([^"\n]+)"?$', text, re.M)
        company_match = re.search(r'^company:\s*"?([^"\n]+)"?$', text, re.M)
        if title_match and company_match:
            companies[title_match.group(1).strip().lower()] = company_match.group(1).strip()
    return companies


def person_link(name: str, people_by_title: dict[str, str]) -> str:
    slug = people_by_title.get(name.lower()) or slugify(name)
    return f"[[{slug}|{md_escape(name)}]]"


def company_link(name: str, companies_by_title: dict[str, str]) -> str:
    slug = companies_by_title.get(name.lower()) or slugify(name)
    return f"[[{slug}|{md_escape(name)}]]"


def collect_schedule_topic_sessions(sessions: list[dict]) -> dict[str, list[dict]]:
    topic_sessions: dict[str, list[dict]] = defaultdict(list)
    for session in sessions:
        haystack = " ".join(str(session.get(key, "")) for key in ["description", "track", "type", "room"])
        title = str(session.get("title", ""))
        track = str(session.get("track", ""))
        title_low = title.lower()
        track_low = track.lower()
        for slug, _label, score in topic_hits(title, haystack):
            keys = next((keys for rule_slug, _rule_label, keys in TOPIC_RULES if rule_slug == slug), [])
            title_boost = 120 if any(key.lower() in title_low for key in keys) else 0
            track_boost = 40 if any(key.lower() in track_low for key in keys) else 0
            topic_sessions[slug].append({"session": session, "score": score * 10 + title_boost + track_boost, "source": "official schedule"})
    return topic_sessions


def section_block(text: str, heading: str) -> tuple[str, str]:
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    match = pattern.search(text)
    if not match:
        return text, ""
    return (text[: match.start()] + text[match.end() :]).rstrip() + "\n", match.group(0).strip()


def reorder_topic_graph_sections(path: Path) -> None:
    text = path.read_text(errors="ignore")
    blocks = []
    for heading in ["Related Scheduled Sessions", "Related People", "Related Companies", "Transcript And Resource Support"]:
        text, block = section_block(text, heading)
        if block:
            blocks.append(block)
    if not blocks:
        path.write_text(text.rstrip() + "\n", encoding="utf-8")
        return
    insert_match = re.search(r"^## Related Slide Decks\n.*?(?=^## |\Z)", text, flags=re.M | re.S)
    if not insert_match:
        insert_match = re.search(r"^## Active Use Cases\n.*?(?=^## |\Z)", text, flags=re.M | re.S)
    insert_at = insert_match.end() if insert_match else len(text)
    replacement = text[:insert_at].rstrip() + "\n\n" + "\n\n".join(blocks) + "\n\n" + text[insert_at:].lstrip()
    path.write_text(replacement.rstrip() + "\n", encoding="utf-8")


def upsert_topic_relationships(path: Path, session_rows: list[dict]) -> None:
    people_by_title = registry_title_map("people")
    companies_by_title = registry_title_map("companies")
    company_by_person = people_company_map()

    deduped_sessions = []
    seen_sessions = set()
    for row in sorted(session_rows, key=lambda item: item["score"], reverse=True):
        session = row["session"]
        slug = session_slug(session)
        if slug in seen_sessions:
            continue
        seen_sessions.add(slug)
        deduped_sessions.append(row)

    selected = deduped_sessions[:24]
    if selected:
        lines = []
        for row in selected:
            session = row["session"]
            speakers = session.get("speakers") or []
            speaker_text = ", ".join(person_link(name, people_by_title) for name in speakers) or "speaker TBD"
            meta = " · ".join(part for part in [session.get("day"), session.get("time"), session.get("track") or session.get("room")] if part)
            source = row.get("source", "topic match")
            via = f"; via [[youtube-{row['video_id']}]]" if row.get("video_id") else ""
            suffix = f" ({meta}; {source}{via})" if meta or source or via else ""
            lines.append(f"- [[{session_slug(session)}]] — {md_escape(session.get('title'))}; {speaker_text}{suffix}")
        upsert_section(path, "Related Scheduled Sessions", "\n".join(lines))

    people_scores: Counter[str] = Counter()
    company_scores: Counter[str] = Counter()
    for index, row in enumerate(deduped_sessions):
        weight = max(1, 1000 - index)
        for speaker in row["session"].get("speakers") or []:
            people_scores[speaker] += weight
            company = company_by_person.get(speaker.lower())
            if company:
                company_scores[company] += weight

    if people_scores:
        lines = [f"- {person_link(name, people_by_title)}" for name, _count in people_scores.most_common(24)]
        upsert_section(path, "Related People", "\n".join(lines))
    if company_scores:
        lines = [f"- {company_link(name, companies_by_title)}" for name, _count in company_scores.most_common(18)]
        upsert_section(path, "Related Companies", "\n".join(lines))


def update_topic_pages(topic_resources: dict[str, list[dict]], topic_quotes: dict[str, list[dict]], topic_sessions: dict[str, list[dict]]) -> None:
    TOPICS.mkdir(parents=True, exist_ok=True)
    existing_registry = read_json(TOPICS / "registry.json", [])
    known = {item.get("id"): item.get("title") for item in existing_registry}
    for slug, label, _keys in TOPIC_RULES:
        path = TOPICS / f"{slug}.md"
        if not path.exists():
            path.write_text(
                "\n".join([
                    frontmatter({"title": label, "category": "topics", "sourceLabels": ["Transcript-derived supporting context"]}),
                    f"# {label}",
                ]) + "\n",
                encoding="utf-8",
            )
        upsert_topic_article(path, slug, label)
        upsert_topic_relationships(path, topic_sessions.get(slug, []))
        resources = topic_resources.get(slug, [])
        quotes = topic_quotes.get(slug, [])
        support = []
        if resources:
            support.append("### Transcript-backed resources")
            for row in sorted(resources, key=lambda r: r["score"], reverse=True)[:18]:
                support.append(f"- [[youtube-{row['video_id']}]] — {md_escape(row['title'])}")
        if quotes:
            support.extend(["", "### Quote signals"])
            for row in sorted(quotes, key=lambda r: r["score"], reverse=True)[:8]:
                support.append(f"- “{md_escape(row['quote'])}” — [[youtube-{row['video_id']}]]")
        if support:
            upsert_section(path, "Transcript And Resource Support", "\n".join(support))
        reorder_topic_graph_sections(path)
        known.setdefault(slug, label)
    registry = [{"id": slug, "title": title or slug.replace("-", " ").title(), "path": f"wiki/topics/{slug}.md"} for slug, title in sorted(known.items()) if slug]
    (TOPICS / "registry.json").write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8")


def topic_article_sections(slug: str, label: str) -> list[tuple[str, str]]:
    article = TOPIC_ARTICLES.get(slug)
    if not article:
        article = {
            "synopsis": f"{label} is a recurring AI Engineer World's Fair 2026 topic connected to agent design, production use, and applied AI engineering practice.",
            "origin": "This page is synthesized from the wiki's schedule, transcripts, slide OCR, and supporting AI Engineer YouTube resources.",
            "why": "It matters because teams need a shared vocabulary for deciding when the pattern is useful, how to implement it, and how to evaluate production tradeoffs.",
            "how": "Use the supporting talks and resources below to identify common patterns, then test those patterns against real tasks, constraints, and failure modes.",
            "where": "The topic is useful where its constraints and active use cases match a real product or engineering workflow.",
            "when": "Use it when the operational benefits outweigh added complexity, and revisit the decision as model, tooling, and product constraints change.",
            "use_cases": ["Conference-derived examples and supporting resources listed below."],
        }
    use_cases = "\n".join(f"- {item}" for item in article["use_cases"])
    return [
        ("Synopsis", article["synopsis"]),
        ("Origin And Context", article["origin"]),
        ("Why It Matters", article["why"]),
        ("How To Use It", article["how"]),
        ("Where It Is Useful", article["where"]),
        ("When To Use It", article["when"]),
        ("Active Use Cases", use_cases),
    ]


def upsert_topic_article(path: Path, slug: str, label: str) -> None:
    text = path.read_text(errors="ignore") if path.exists() else ""
    if all(f"## {heading}" in text for heading in ARTICLE_HEADINGS[:7]):
        return
    for heading in ARTICLE_HEADINGS:
        text = re.sub(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", "", text, flags=re.M | re.S).rstrip() + "\n"
    article = "\n\n".join(f"## {heading}\n{body.strip()}" for heading, body in topic_article_sections(slug, label))
    match = re.search(r"^# .+$", text, flags=re.M)
    if not match:
        path.write_text(article.rstrip() + "\n", encoding="utf-8")
        return
    insert_at = match.end()
    replacement = text[:insert_at].rstrip() + "\n\n" + article + "\n\n" + text[insert_at:].lstrip()
    path.write_text(replacement.rstrip() + "\n", encoding="utf-8")


def update_resource_registry() -> None:
    rows = []
    for page in sorted(RESOURCES.glob("*.md")):
        if page.name == "registry.json":
            continue
        title = page.stem.replace("-", " ").title()
        text = page.read_text(errors="ignore")
        m = re.search(r"^title:\s*(.+)$", text, re.M)
        if m:
            title = m.group(1).strip().strip('"')
        rows.append({"id": page.stem, "title": title, "path": f"wiki/resources/{page.name}"})
    (RESOURCES / "registry.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> int:
    sessions = read_json(RAW / "official-sessions.json", {}).get("sessions", [])
    videos = load_new_videos()
    quote_rows = []
    topic_resources: dict[str, list[dict]] = defaultdict(list)
    topic_quotes: dict[str, list[dict]] = defaultdict(list)
    topic_sessions = collect_schedule_topic_sessions(sessions)
    processed = []
    missing = []
    skipped_non_article = []
    for video_id, video in sorted(videos.items(), key=lambda item: item[1]["youtube_title"].lower()):
        path = transcript_path(video_id)
        if not path:
            if non_article_supporting_media(video):
                write_non_transcript_resource(
                    video_id,
                    video,
                    "No article transcript is expected for this non-talk event reel; it is kept as supporting media rather than topic evidence.",
                )
                skipped_non_article.append({"video_id": video_id, "title": video["youtube_title"], "reason": "non-talk event reel"})
                continue
            missing.append(video_id)
            continue
        text = path.read_text(errors="ignore")
        topics = topic_hits(video["youtube_title"], text)
        matches = related_sessions(video, sessions)
        write_resource(video_id, video, text, topics, matches)
        for slug, label, score in topics:
            topic_resources[slug].append({"video_id": video_id, "title": video["youtube_title"], "score": score})
            for match_score, session in matches:
                topic_sessions[slug].append({"session": session, "score": score + match_score, "source": "related YouTube resource", "video_id": video_id})
        qrows = quote_candidates(video_id, video, text, topics)
        quote_rows.extend(qrows)
        for row in qrows:
            topic_quotes[row["topic"]].append(row)
        processed.append({"video_id": video_id, "title": video["youtube_title"], "topics": topics, "matches": [session_slug(s) for _score, s in matches], "quotes": len(qrows), "words": len(text.split())})
    write_quote_pages(quote_rows)
    update_topic_pages(topic_resources, topic_quotes, topic_sessions)
    update_resource_registry()
    report = {
        "processed": processed,
        "missing_transcripts": missing,
        "skipped_non_article": skipped_non_article,
        "quote_count": len(quote_rows),
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    (RAW / "transcript-enrichment-report-2026-07-06.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"processed": len(processed), "missing": missing, "quotes": len(quote_rows)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
