---
title: "AIE Wiki Generation Delta"
category: "resources"
sourceLabels:
  - "Local wiki comparison"
  - "Build logic comparison"
  - "Source-boundary review"
---

# AIE Wiki Generation Delta

This page records the factual delta between four local AI Engineer wiki generations inspected on 2026-07-10:

- AI Engineer World's Fair 2024 local fixture wiki.
- AI Engineer Miami 2026 local public wiki app.
- AI Engineer World's Fair 2025 local fixture wiki.
- This AI Engineer World's Fair 2026 public static wiki.

The main comparison is the evolution of the AI engineering conversation: what information became important, which technologies moved into focus, and what lessons the wiki logic needed to preserve. The implementation details are included only where they explain what the wiki can see.

## Executive Delta

| Stage | What the AI conversation focused on | What changed in the wiki's job |
|---|---|---|
| World's Fair 2024 | AI engineering as a broad discipline: RAG, open models, multimodality, evals, infrastructure, codegen, agents, human oversight, and enterprise adoption. | Preserve separate layers for official facts, transcript synthesis, slide/OCR evidence, claims, quotes, and questions. |
| Miami 2026 | Coding agents and agent interfaces became concrete: MCP vs skills, agent runtime, context engineering, agent-ready interfaces, code-quality gates, future IDEs, remote agents, latency debt, and agent auditability. | Move from fixture summaries to transcript-first synthesis, because the important lessons were in talk arguments and repeated phrasing across two full-day transcripts. |
| World's Fair 2025 | Production agent concerns dominated the indexed talk titles: MCP, evals, enterprise agents, memory, agent security, GraphRAG, voice agents, robotics, coding agents, inference engines, and product/organizational adoption. | Expand session/person/company coverage and evidence pages, while still keeping the fixture-style source boundary. |
| World's Fair 2026 | The current wiki treats agents as operational systems: software factories, agent evaluations, memory/context graphs, security boundaries, agentic search, sandboxes, inference engineering, MCP governance, voice agents, and autoresearch. | Preserve the official schedule as canonical, then layer confirmed event videos, transcripts, slide OCR, reconstructed slides, tools, questions, harnesses, playbooks, evaluations, policies, graph data, and agent-readable markdown. |

## Evolution Of AI Focus

### 2024: from model usage to AI engineering discipline

The 2024 topic index is broad and foundational. It contains topics for RAG/LLM frameworks, open models, multimodality, model training, GPUs/inference, AI infrastructure, codegen/dev tools, coding agents, agent reliability, agent evaluation, human oversight, leadership, workshops, and AI in the Fortune 500.

The lesson visible in the 2024 wiki is that AI engineering was already more than prompt use. The local output separated:

- official program facts;
- transcript synthesis;
- derived knowledge;
- slide/OCR evidence;
- claim pages;
- quote pages;
- question pages.

That separation matters because many 2024 themes were still broad categories. The wiki's job was to keep evidence and synthesis apart so broad themes such as agents, RAG, open models, and evals did not collapse into unsourced trend summaries.

### Miami 2026: agent work became developer workflow

Miami is smaller in page count, but sharper in focus. The local Miami overview points to exact event days, April 20 and April 21, 2026, and to two transcript files as the primary source corpus.

The Miami topic trails show a shift from "AI engineering as a category" to "how engineers actually work with agents":

- MCP vs skills;
- agent runtime;
- context engineering;
- agent-ready interfaces;
- latency debt;
- future of IDEs;
- agent auditability;
- governed agents;
- code-quality gates;
- production agents;
- remote coding agents;
- sandboxed compute;
- terminal workflows;
- typed AI interfaces;
- PR slop;
- research-plan-implement loops.

The technology focus also changed. Miami's talk list centered on coding agents, OpenCode, HumanLayer, OpenAI, Modem, OpenRouter, Qodo, Cloudflare, LangGraph/MCP, Neo4j context graphs, Cursor, Arize, and agent skills.

The lesson visible in Miami is that agent systems needed interfaces, runtime boundaries, memory/context, governance, and developer-experience judgment. A useful wiki could no longer only list sessions; it had to preserve talk-level arguments and cross-link repeated concepts across transcripts.

### World's Fair 2025: production agents, MCP, evals, and infrastructure scaled up

The inspected World's Fair 2025 output is still a fixture wiki, but the talk index shows a larger and more production-oriented AI engineering agenda.

Visible title clusters include:

- MCP and agent interfaces: "MCP is all you need", "What does enterprise-ready MCP mean?", "Real-world MCPs in GitHub Copilot Agent Mode", "Observable Tools: The State of MCP Observability", "Building Protected MCP Servers", and "Letting AI Interface with Your App with MCP".
- Evals and production quality: "2025 is the year of evals", "Evals are not unit tests", "Solving for the hardest Eval challenge", "Mastering AI Evaluation", "Human-Seeded Evals", and "CI in the Era of AI".
- Coding agents and software work: "Claude Code: The Evolution of Agentic Coding", "Agentic Coding with Windsurf", "Ship Agents that Ship", "Software Development Agents: What Works and What Doesn't", and "Code Review for the Age of AI".
- Memory and context: "Make Your AI Agents Remember What They Do", "Stop Using RAG as Memory", "The Eyes Are the Context Window to the Soul", and GraphRAG / knowledge-graph talks.
- Safety, identity, and control: "Containing Agent Chaos", "How to Build Agents Without Losing Control", "Agents, Access, and the Future of Machine Identity", "How to Secure Agents Using OAuth", and "Safety and Security for Code-Executing Agents".
- Form factors beyond chat: voice agents, realtime conversational video, humanoid robots, autonomous vehicles, generative media, and recommendation systems.
- Infrastructure: LLM serving, inference engines, GPUs, Apple Silicon, open models, and cloud-scale agents.

The lesson visible in 2025 is operationalization. Agents were no longer only interesting demos or coding assistants; the indexed talks repeatedly ask how to ship, evaluate, secure, observe, coordinate, and govern them.

### World's Fair 2026: agents became systems with evidence trails

The current 2026 wiki is built around the assumption that AI engineering is now systems engineering. Its theme map includes coding agents, software factories, agent evaluations, agent memory, agent security, agentic search, voice agents, inference engineering, MCP, AI sandboxes, and autoresearch.

The current question layer makes the same change explicit:

- How should coding agents be evaluated before production use?
- What context graph and memory architecture is practical?
- What latency and cost budget is right for agent systems?
- What makes a codebase agent-ready?
- What security boundaries should agents have?
- When do software factories outperform individual IDE agents?

The technology layer is also more concrete. The current tool inventory includes agent platforms and protocols such as MCP, MCP Apps, mcpc, Amazon Bedrock, Amazon Nova Act, Azure AI Foundry, Braintrust, Browserbase, Claude Agent SDK, Codex, Cursor, Daytona, Docker, DSPy, Exa, Gemini, GitHub Copilot, GraphRAG, LangGraph, Langfuse, LlamaIndex, Modal, Neo4j, OpenHands, OpenRouter, Pydantic, Sourcegraph Amp, Temporal, vLLM, VS Code, WebAssembly, Windsurf, x402, and Zep.

The lesson for the 2026 wiki is evidence discipline. A production-agent conference wiki needs to know which facts came from the official schedule, which statements came from actual event recordings, which text came from transcripts, which claims came from slide OCR, and which links are only supporting context.

## Evolution By Axis

| Axis | 2024 | Miami 2026 | 2025 | World's Fair 2026 |
|---|---|---|---|---|
| Main AI focus | Broad AI engineering map: RAG, open models, multimodality, evals, infra, codegen, agents. | Developer workflow with agents: MCP vs skills, runtimes, context, IDEs, governance, latency, quality gates. | Production agent scale: MCP, evals, security, memory, voice, robotics, coding agents, inference, enterprise adoption. | Operational agent systems: software factories, eval gates, memory graphs, security boundaries, sandboxes, agentic search, MCP governance. |
| Information needed | Official facts plus evidence/synthesis separation. | Full transcripts, because the lessons are in detailed talk arguments. | Large session/title evidence and fixture records. | Schedule, official event media, transcripts, OCR, reconstructed slides, tools, topics, questions, policies, and graph links. |
| Technical lesson | Do not blend broad themes with evidence. | Treat agent concepts as a linked knowledge graph, not one-off talk notes. | Production agents require evaluation, observability, security, memory, and deployment patterns. | Every derived claim needs provenance because agent systems depend on operational details. |
| Wiki lesson | Preserve source classes separately. | Use transcript-first synthesis and read-only graph navigation. | Scale coverage while retaining fixture boundaries. | Keep the public site static/read-only while publishing agent-readable indexes and evidence layers. |

## Date Anchors

| Wiki | Event date information visible in the inspected sources | Inspection note |
|---|---:|---|
| AI Engineer World's Fair 2024 | The inspected overview identifies the event year as 2024; it does not expose calendar-day event dates in the overview or source-boundary page. | Local fixture wiki served from a static HTML export. |
| AI Engineer Miami 2026 | April 20, 2026 and April 21, 2026. | The Miami overview names two transcript files, one for each conference day. |
| AI Engineer World's Fair 2025 | The inspected overview identifies the event year as 2025; it does not expose calendar-day event dates in the overview or source-boundary page. | Local fixture wiki served from a static HTML export. |
| AI Engineer World's Fair 2026 | June 28-July 2, 2026. | Current public wiki event days are New Engineer Orientation, Workshop Day and Welcome Reception, Keynotes and Breakouts, World Cup and Multi-Track Programming, and Final Day and Last Chance Expo. |

## Scale At Inspection Time

| Wiki | Talks | People | Companies | Tools | Topics | Events | Evidence / media-specific pages | Notes |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| World's Fair 2024 | 180 | 170 | 108 | 5 | 20 | Not exposed as event-day pages in the inspected output | 180 evidence pages, 89 transcript pages, 88 synthesis pages, 88 claim pages, 88 quote pages | The source-boundary page reports 471 synthesis pages and 1,413 public source citations on synthesis pages. |
| Miami 2026 | 28 | 29 | 26 | 38 | 55 | 2 | 4 resource pages | The local app reports 186 total pages and a read-only public-share project. |
| World's Fair 2025 | 271 | 287 | 157 | 0 | 21 | Not exposed as event-day pages in the inspected output | 271 evidence pages | The source-boundary page reports 736 synthesis pages and 2,208 public source citations on synthesis pages. |
| World's Fair 2026 | 560 | 555 | 344 | 62 | 16 | 5 | 226 resource pages, 104 transcript pages, 418 slide pages | Current wiki also has question, harness, playbook, evaluation, and policy layers. |

Counts are filesystem or local API counts from the inspected local wiki outputs. They are build-shape facts, not event-size claims.

## Source Boundary Delta

### World's Fair 2024

The 2024 local wiki is a `specific_event` fixture output. Its source-boundary page says it was generated from local fixture objects and did not perform live source discovery, transcript processing, browser automation, external scripts, network access, deployment, or repository creation.

Included source classes were:

- official event fixture URLs;
- official or supporting video fixture URLs;
- corrected local transcript fixture snippets copied into evidence pages.

The logic split synthesis pages from evidence pages. The overview explicitly says official program facts, transcript synthesis, derived knowledge, and slide/OCR evidence remain separately labeled in integrated views.

### Miami 2026

Miami changed the logic from fixture-first to transcript-first. Its overview says the wiki combines:

- two allowed transcript files;
- the official conference website;
- clearly labeled public-web supporting context from company, product, documentation, or GitHub-style public URLs.

The Miami source videos did not have directly available transcripts, so audio was downloaded and transcribed with Whisper. The two transcript files became the primary corpus for the April 20 and April 21 pages.

Miami also changed the serving model. It uses a static Express app that reads markdown, renders wikilinks, builds backlinks and graph data at request time, and exposes read-only API routes. Mutating authoring endpoints are intentionally blocked for the public deployment.

### World's Fair 2025

The 2025 local wiki keeps the 2024 fixture pattern but at larger scale. Its source-boundary page has the same core restriction: generated from local fixture objects only, with no live source discovery, transcript processing, browser automation, external scripts, network access, deployment, or repository creation.

Included source classes were the same class of inputs as 2024:

- official event fixture URLs;
- official or supporting video fixture URLs;
- corrected local transcript fixture snippets copied into evidence pages.

The visible category model covers talks, people, companies, tools, and topics, but the inspected output had zero tool pages. The 2025 fixture output therefore expanded session/person/company/topic coverage without adopting Miami's richer tool/topic graph behavior.

### World's Fair 2026

The 2026 wiki changes the logic again. It is schedule-first, public-static, and source-bounded:

- official AI Engineer World's Fair 2026 schedule and speaker data are canonical for dates, titles, times, tracks, rooms, speakers, and affiliations;
- official AI Engineer World's Fair San Francisco 2026 videos are primary event video sources for media, transcripts, and slide evidence;
- related non-event YouTube videos are supporting context only, not first-class event evidence;
- public profile and company-site links are supporting context unless they come from the official schedule or official speaker roster.

The 2026 build also adds source layers that are not present in the inspected 2024/2025 fixture overviews:

- talk/video/transcript mapping;
- YouTube caption and local Whisper transcript handling;
- video frame extraction;
- slide OCR and RapidOCR repair;
- reconstructed slide crops and dense slide pages;
- content-derived topics;
- tools, questions, harnesses, playbooks, evaluations, and policies;
- static graph data and an agent-readable public index.

## Logic Changes By Generation

| Change | 2024 fixture | Miami 2026 | 2025 fixture | World's Fair 2026 |
|---|---|---|---|---|
| Primary corpus | Local fixture objects. | Two Whisper transcript files plus official conference website. | Local fixture objects. | Official schedule and speaker data, then confirmed event media and derived evidence layers. |
| Event dates | Event year visible; calendar dates not visible in inspected overview/source-boundary. | Exact days visible: 2026-04-20 and 2026-04-21. | Event year visible; calendar dates not visible in inspected overview/source-boundary. | Exact span visible: 2026-06-28 through 2026-07-02. |
| Evidence separation | Explicit synthesis/evidence separation. | Transcript-derived, conference-site, and public-web source labels. | Explicit synthesis/evidence separation. | Official schedule, primary event video, supporting video, transcript, OCR, slide, and public-profile roles. |
| Video handling | Fixture URLs and copied transcript snippets only. | Downloaded YouTube audio and Whisper transcripts. | Fixture URLs and copied transcript snippets only. | Official event recordings are first-class; non-event videos are supporting context only. |
| Graph/backlinks | Agent index and rendered static pages. | Backlinks and graph data built by the read-only app at request time. | Static fixture pages; the inspected local server did not expose `/agent-index.json`. | Static graph dataset and `/graph/` page generated at build time. |
| Public contract | Local fixture validation output. | Public-share, read-only app; mutating routes blocked. | Local fixture validation output. | Standalone static public repo/site with markdown backing files and `/agent-index.md`. |

## Practical Takeaways For This Wiki

- Keep Miami's strong idea: a conference-native wiki should explain sources, dates, event-day entry points, graph navigation, and topic synthesis plainly.
- Keep the 2024/2025 fixture discipline: synthesis and evidence records must remain distinct.
- Keep the 2026 evidence boundary stricter than simple YouTube matching: only actual World's Fair San Francisco 2026 event recordings should become first-class video evidence.
- Keep the public contract static and read-only: generated graph data, markdown mirrors, and agent indexes are safer than runtime mutation for the published site.
