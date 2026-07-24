---
title: "Your agent architecture has a half-life of 6 months"
category: "talks"
date: "2026-06-30"
time: "12:05pm-12:25pm"
track: "Expo Stage 1 NE"
room: "Expo Stage 1 NE"
speakers: ["Dan Farrelly"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: ""
scheduleRoom: "Expo Stage 1 NE"
scheduleLabels: ["Expo Stage 1 NE", "session", "confirmed"]
---
# Your agent architecture has a half-life of 6 months

## Conference Context
- Date/time: 2026-06-30 · 12:05pm-12:25pm
- Track/room: track TBD · Expo Stage 1 NE
- Speaker(s): Dan Farrelly
- Session type/status: session · confirmed

- Track: track TBD
- Room: Expo Stage 1 NE
- Session type: session
- Status: confirmed

## Session Description
A short history of the right way to build an agent: RAG, ReAct, prompt chaining, orchestrator-workers, MCP, CLI, MCP again... CLI again?? Every time you adopt a trend you rebuild your architecture. In this talk, Dan Farrelly, Inngest cofounder and CTO, is not going to tell you what comes next. He's going to show you how to build so it doesn't matter. He'll cover the core primitives that show up in every production agent, how bringing decisions closer to code provides more stack flexibility, and why the right execution layer unlocks faster iteration.

## Synthesis
### Transcript-Backed Summary
Dan Farrelly's core thesis is that agent architectures decay quickly because teams tie together layers that change at very different speeds. He argues for separating execution from context and compute so the stable execution layer can own durability, retries, orchestration, and observability while models, prompts, sandboxes, and browsers can change underneath it. The practical result is a harness that can survive new frameworks and patterns without constant rewrites, and that also becomes the right place to measure outcomes and debug long-running systems.

### Key Takeaways
- Think about agent systems as three layers, not a pile of individual components: execution, context, and compute.
  - Evidence: "This is maybe the mental model. Not specific components. So, in my opinion, there are three discrete layers."
- Durable resumability requires state to live outside the running work, not in memory or on local disk.
  - Evidence: "So, for this this to work, a 3-hour run cannot hold state in memory or in disk. The state must live outside of the work."
- Execution should provide whole-session observability, including LLM calls, tools, database errors, permissions, triggers, and performance.
  - Evidence: "And now you end up kind of a mess bad abstractions. lastly, execution needs to provide observability across your entire session."
- Sandboxes should stay ephemeral; the execution layer gives them context, sequence, and durability instead of storing state itself.
  - Evidence: "So, I think when you have the execution layer separate, the execution layer is what gives the sandbox its context, its sequence, its durability."
- Outcome-based scoring becomes easier when the execution layer can attach and interpret real events like opening a PR or saving research.
  - Evidence: "If it's a research agent, was this research saved? Was it a good report? That is these these things that are events that you should be able to attach and when you have a system that can connect all these pieces, I think it's really makes doing a lot of those things um like creating outcome-based scores a lot easier."

### Claims From The Talk
- The speaker argues that most teams couple execution, context, and compute together, so the faster-changing layer drags the rest of the architecture into rewrites. (`explicit`)
  - Evidence: "So, the problem is that I think that most teams couple everything together. And what happens then is that one layer's half-life kind of leaks and drags the other components down."
- He claims that common frameworks and harnesses often bury orchestration or merge layers in ways that make component swaps require rewriting almost everything. (`explicit`)
  - Evidence: "And what's hard is you can't re- you can't like swap any of these things out without rewriting almost everything."
- He says long-running agent work cannot keep state in memory or disk, because resumability requires state to live outside the work itself. (`explicit`)
  - Evidence: "So, for this this to work, a 3-hour run cannot hold state in memory or in disk. The state must live outside of the work."
- He argues that background agents cannot be debugged well without infrastructure that captures what happened across the entire asynchronous process. (`explicit`)
  - Evidence: "So, you can't even debug your background agent that's running asynchronously without the right infrastructure, without the observability, without everything that's going on in that process or multiple processes."
- He presents Inngest as a durable execution layer for AI agents that can accept different context, model, sandbox, and browser choices. (`explicit`)
  - Evidence: "We're durable execution for AI agents. We're the execution layer. You can plug in any context layer, bring a model, framework, tool, any compute layer."

### Topics Covered
- **Layered agent architecture** — The idea that agent systems should be organized into stable and volatile layers with different lifetimes.
- [[agent-reliability-and-durable-execution|Durable execution]] — The use of durable, resumable execution as the stable core of an agent system.
- [[coding-agents|Full-session observability]] — Capturing traces across the full run so long-running agents can be debugged and improved.
- [[ai-sandboxes|Sandbox isolation]] — Using ephemeral sandboxes for code, browsing, and file work without treating them as the source of durability.
- [[agent-reliability-and-durable-execution|Background agent loops]] — Long-running background agents and looped workflows that combine scheduling, delegation, and inspection.

### Tools And Named Systems
- **Inngest** — A durable execution platform the speaker uses as the concrete example of this architecture.

### Novel Concepts And Methods
- **Layered decoupling** — Treat the agent system as separate execution, context, and compute layers so the stable parts can outlive the volatile ones.
- **External resumability** — Keep runtime state outside the work so failed or interrupted runs can resume without restarting from zero.
- **Flexible orchestration** — Use execution primitives that support cron triggers, events, human-in-the-loop steps, subagents, synchronous calls, asynchronous calls, and delayed invocation.
- **Execution-aware review loop** — Build an execution-aware review loop that inspects logs, workflows, and outcomes to improve the system over time.

### Open Questions
- **How should teams define success for agents when the real outcome is a downstream business event rather than a simple thumbs-up or thumbs-down?** — The talk argues that outcome-based scoring is more useful than generic feedback, but the exact metric depends on the workflow.
- **What execution-layer abstractions will still fit the next wave of agent architectures as new patterns keep emerging?** — The speaker's thesis is that architectures keep changing, so the unresolved problem is which primitives can remain stable across those shifts.

### Derived Links And Source Material
- [[youtube-X1kp-ABIIxQ-transcript]] — dedicated official recording transcript.
- [[youtube-X1kp-ABIIxQ]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/X1kp-ABIIxQ--2026-06-30-dan-farrelly-your-agent-architecture-has-a-half-life-of-6-months.json`.

### Speaker Context
- [[dan-farrelly|Dan Farrelly]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[dan-farrelly]]

## Official YouTube Recording
- [[youtube-X1kp-ABIIxQ|Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest]] — official AI Engineer YouTube recording published 2026-07-21.
- Evidence status: [[youtube-X1kp-ABIIxQ-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-X1kp-ABIIxQ]] - dedicated official event recording.
- [[youtube-X1kp-ABIIxQ-transcript]] - dedicated official recording transcript.

- Source video: `youtube-X1kp-ABIIxQ`
- Slide deck: [[youtube-X1kp-ABIIxQ-slides|Slides: Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest]] — 15 visible slide image(s).
![[assets/slides/X1kp-ABIIxQ/slide-001.jpg]]
![[assets/slides/X1kp-ABIIxQ/slide-002.jpg]]
![[assets/slides/X1kp-ABIIxQ/slide-003.jpg]]
- Slide-derived themes for `youtube-X1kp-ABIIxQ`: expo, stage, under, abstractions, engineering, future, hows, jobs.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/X1kp-ABIIxQ.txt` (2,909 words).

## Transcript Markdown
- [[youtube-X1kp-ABIIxQ-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/X1kp-ABIIxQ.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-X1kp-ABIIxQ` — 2,909 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-X1kp-ABIIxQ`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-X1kp-ABIIxQ`: execution, layer, system, might, maybe, months, loop, able.
- Slide-derived themes for `youtube-X1kp-ABIIxQ`: expo, stage, under, abstractions, engineering, future, hows, jobs.
- Evidence links for `youtube-X1kp-ABIIxQ` (primary event evidence): [[youtube-X1kp-ABIIxQ]], [[youtube-X1kp-ABIIxQ-transcript]], [[youtube-X1kp-ABIIxQ-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
