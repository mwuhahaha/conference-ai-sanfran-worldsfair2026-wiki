---
title: "WTF Is the Context Layer? The Missing Infrastructure for Production Agents"
category: "talks"
date: "2026-06-30"
time: "1:55pm-2:15pm"
track: "Context Engineering"
room: "Track 8"
speakers: ["Prukalpa Sankar"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Context Engineering"
scheduleRoom: "Track 8"
scheduleLabels: ["Context Engineering", "Track 8", "session", "confirmed"]
---
# WTF Is the Context Layer? The Missing Infrastructure for Production Agents

## Conference Context
- Date/time: 2026-06-30 · 1:55pm-2:15pm
- Track/room: Context Engineering · Track 8
- Speaker(s): Prukalpa Sankar
- Session type/status: session · confirmed

- Track: Context Engineering
- Room: Track 8
- Session type: session
- Status: confirmed

## Session Description
In the last two years, models have gotten exponentially smarter. Two years ago they couldn't pass the bar. Today, top 1% of test scorers. And yet most agents still can't answer a simple business question correctly. You ship a demo that works. You deploy it. The business abandons it in a month. The missing variable is context: the business definitions, procedural knowledge, and operational norms that make a human expert valuable. Drawing on hundreds of production deployments, Prukalpa Sankar will break down what it actually takes to give agents contextual intelligence — and get them past the demo stage. She'll walk through the architecture of a context layer: how context repos work (versioned, testable, portable), how simulation environments catch failures before deployment, how agent traces compound back into shared context, and why context engineering scales where fine-tuning and prompting don't. She'll also cover why your context needs to be open (MCP, Iceberg, deploy to any framework) — and what happens when it isn't.

## Synthesis
### Transcript-Backed Summary
Prukalpa Sankar argues that the gap between smarter models and weak production outcomes is not model capability but missing business context: the facts, playbooks, and norms that make a human expert effective. Her proposed mechanism is a context layer that behaves like a versioned, testable company brain, continuously mining business systems, organizing reusable skills and semantics, and feeding those assets through retrieval and trace-driven learning loops to general-purpose agents. The tradeoff is operational complexity, because context now needs ownership, dependency management, security, and portability across tools and frameworks, but the payoff is more accurate agents, less silo drift, and context as a durable company asset rather than hard-coded prompt glue.

### Key Takeaways
- Treat the meaning of a business question as part of the problem, not an assumption the model can infer.
  - Evidence: "Is the cutoff period Monday to Sunday? Is it Pacific time? Is it Eastern time? Uh that's knowledge."
- Expect context engineering, not agent scaffolding, to consume most of the time needed for accuracy.
  - Evidence: "uh but giving it the business context that it took to actually get it to be accurate took forever."
- If context does not propagate across teams and channels, agents will keep acting on stale versions of reality.
  - Evidence: "So our marketing team had these agents and they started making changes to that and then our SDR agent on our website was still pitching the old version."
- A reusable context layer should store data graphs, skills, semantics, and business definitions together.
  - Evidence: "So like which table should I go pull from? Uh we needed a library of skills. We also needed some other things, semantics, metrics, what is ARR, how do you measure that?"
- Use traces to feed a maintainer loop so learning compounds after deployment instead of stopping at launch.
  - Evidence: "So think of it as AI that's reading through all your traces and almost brings it back to your maintainer loop and says approve reject approve reject improve this over time."

### Claims From The Talk
- The speaker argues that real-world performance depends on both intelligence and context, not just model benchmarks. (`explicit`)
  - Evidence: "you deliver in the real world and performance is a function of two things it's a function of intelligence which is cognitive horsepower that's what the model benchmarks measure every day But it's also a function of context."
- The speaker says a simple business question can hinge on facts like cutoff periods and time zones. (`explicit`)
  - Evidence: "Is the cutoff period Monday to Sunday? Is it Pacific time? Is it Eastern time? Uh that's knowledge."
- The speaker reports that agents developed separate memory systems, which made a single version of truth difficult to maintain. (`explicit`)
  - Evidence: "Um and over time we started dealing with uh context sprawl. Uh we had the the the hard part about this was agents all had their own memory systems to a certain extent."
- The speaker says the team ended up creating about 300 skills and 40 agents. (`explicit`)
  - Evidence: "Over the last 6 months, we ended up creating about 300 skills and 40 agents in this team. Uh which has been incredible."
- The speaker argues that context should be treated as intellectual property and as part of what differentiates companies. (`strong`)
  - Evidence: "So I'll end with one last thing. I started this presentation by saying context is king. Um I'd like to end it by saying context is also IP."

### Topics Covered
- [[agent-memory|Context layer]] — The shared infrastructure that turns business knowledge into reusable context for agents.
- **Context engineering** — The work of encoding business facts, skills, and norms so agents can use them correctly.
- [[agent-memory|Context sprawl]] — The failure mode where agents learn separately and drift away from a single source of truth.
- [[semantic-infrastructure-and-ontology|Shared company brain]] — A common repository of company knowledge, skills, and retrieval paths shared across agents.
- [[agent-memory|Trace-driven learning loops]] — A loop that turns traces from AI interactions into improved shared context over time.

### Tools And Named Systems
- **Relevance** — One of the agent-building systems the speaker says the team used before moving to other approaches.
- **Google ADK** — One of the agent-building systems the speaker says the team used before moving to other approaches.
- **Glean** — One of the agent-building systems the speaker says the team used before moving to other approaches.
- [[cloud-code|Cloud Code]] — One of the systems the speaker says the team used during the transition across agent frameworks.
- **Qualified** — An external product the speaker names as part of the marketing stack connected to the context layer.

### Novel Concepts And Methods
- **Jobs-to-be-done analysis** — Break work into concrete jobs-to-be-done before deciding what an agent should handle.
- **Topic-specific agent bootstrapping** — Bootstrap agents by assigning them to specific topics or functions instead of trying to make one agent do everything.
- **Context-as-code lifecycle management** — Manage company context like code, with lifecycle management, collaboration, and versioning.
- **Trace-based reverse construction** — Use traces to reconstruct and improve shared context through approval and rejection loops.
- **Cross-system context mining** — Mine context from connected business systems and use those links to build an initial company brain.

### Open Questions
- **How should ownership, approvers, and maintainers be defined for shared context artifacts at company scale?** — The talk says context needs lifecycle management and governance, but the operating model is still unresolved.
- **How do you separate local context from global context and keep both updated?** — The speaker identifies this as part of the first step in making context manageable like code.
- **What is the best harness for turning traces into reliable improvement signals?** — The talk argues that every interaction creates more context, but the extraction loop still needs a robust mechanism.
- **How do you connect many business systems into one company brain without losing context at every hop?** — The speaker says context is hidden across systems, and the challenge is reconstructing those links accurately.

### Derived Links And Source Material
- [[youtube-8G_1-3IO4ZQ-transcript]] — dedicated official recording transcript.
- [[youtube-8G_1-3IO4ZQ]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/8G_1-3IO4ZQ--2026-06-30-prukalpa-sankar-wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.json`.

### Speaker Context
- [[prukalpa-sankar|Prukalpa Sankar]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[prukalpa-sankar]]

## Official YouTube Recording
- [[youtube-8G_1-3IO4ZQ|WTF Is the Context Layer? The Missing Infrastructure for Production Agents — Prukalpa Sankar]] — official AI Engineer YouTube recording published 2026-07-14.
- Evidence status: [[youtube-8G_1-3IO4ZQ-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-8G_1-3IO4ZQ]] - dedicated official event recording.
- [[youtube-8G_1-3IO4ZQ-transcript]] - dedicated official recording transcript.

- Source video: `youtube-8G_1-3IO4ZQ`
- Slide deck: [[youtube-8G_1-3IO4ZQ-slides|Slides: 8G_1-3IO4ZQ]] — 10 visible slide image(s).
![[assets/slides/8G_1-3IO4ZQ/slide-001.jpg]]
![[assets/slides/8G_1-3IO4ZQ/slide-002.jpg]]
![[assets/slides/8G_1-3IO4ZQ/slide-003.jpg]]
- Slide-derived themes for `youtube-8G_1-3IO4ZQ`: context, layer, keep, companies, track, july, human, specialized.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/8G_1-3IO4ZQ.txt` (3,420 words).

## Transcript Markdown
- [[youtube-8G_1-3IO4ZQ-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/8G_1-3IO4ZQ.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-8G_1-3IO4ZQ` — 3,420 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-8G_1-3IO4ZQ`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-8G_1-3IO4ZQ`: context, team, started, learn, skills, company, question, systems.
- Slide-derived themes for `youtube-8G_1-3IO4ZQ`: context, layer, keep, companies, track, july, human, specialized.
- Evidence links for `youtube-8G_1-3IO4ZQ` (primary event evidence): [[youtube-8G_1-3IO4ZQ]], [[youtube-8G_1-3IO4ZQ-transcript]], [[youtube-8G_1-3IO4ZQ-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
