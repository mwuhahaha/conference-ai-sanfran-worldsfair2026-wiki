---
title: "Active Graph Agent Runtime (BabyAGI 4)"
category: "talks"
date: "2026-07-01"
time: "11:10am-11:30am"
track: "Graphs"
room: "Track 5"
speakers: ["Yohei Nakajima"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Graphs"
scheduleRoom: "Track 5"
scheduleLabels: ["Graphs", "Track 5", "sponsor", "confirmed"]
---
# Active Graph Agent Runtime (BabyAGI 4)

## Conference Context
- Date/time: 2026-07-01 · 11:10am-11:30am
- Track/room: Graphs · Track 5
- Speaker(s): Yohei Nakajima
- Session type/status: sponsor · confirmed

- Track: Graphs
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
Proposing a novel event-sourced graph runtime for building long-running auditable, agentic systems. Built on top of and combining various BabyAGI iterations and graph experiments (memory, code, logs) into a single primitive.

## Synthesis
### Transcript-Backed Summary
The talk argues for a log-centered agent runtime: instead of starting from the LLM, tools, and message flow, ActiveGraph treats the immutable event log as the ground truth of the agent. Behaviors subscribe to graph changes, read a queryable slice of state, and emit new events, while policies decide which graph changes can happen automatically and which require human review or a proposed patch. The practical claim is that this gives long-running agents replay, rollback, forking, cleaner debugging, and better self-improvement loops, while also making failures recoverable without restarting everything. The speaker is candid that the system is experimental and more complex than typical agent code, but argues that the complexity is offset by the fact that AI can often write the glue code and by the benefits of auditable, persistent agent state.

### Key Takeaways
- ActiveGraph forces communication through shared state rather than direct message passing between agents or components.
  - Evidence: "You're just forcing every single communication to communicate through the shared state. [snorts] So at the highest level, right?"
- Because the event log is immutable and typed, the runtime naturally supports replay, rollback, and forks.
  - Evidence: "But yeah, in the end you get this beautiful typed event log, which gives you replays. It gives you rollbacks and it gives you forks."
- Policies are the mechanism that controls which changes an agent can make on its own and which changes need extra tests or human approval.
  - Evidence: "Again, this is how you these these policies kind of give it the control on what it's allowed to change by itself, what uh what kind of changes require certain tests, um and I'll give a few examples in a bit, um or if you want human in the loop, right?"
- Packs bundle object types and behaviors so agent capabilities can be composed and swapped as modular units.
  - Evidence: "So now you kind of get the idea of how I'm trying to build agents on top of ActiveGraph. And each of these packs have object types and behaviors."
- Self-modification is treated as a fork-and-test workflow: propose a change, gate it statically and in a sandbox, then accept it only if it improves results.
  - Evidence: "This is essentially the agent forking itself, proposing a change, doing a static gate check, a sandbox gate check, and then making sure it actually impacted the result, and only then accepted a change."
- A practical benefit of the runtime is that long runs no longer need to start over from the beginning after interruptions.
  - Evidence: "Um no more starting long runs over from the beginning and I know what didn't work, which are some of the things I shared."

### Claims From The Talk
- The speaker argues that most agent stacks are built around the LLM, but ActiveGraph reverses the center of gravity and builds around the log instead. (`explicit`)
  - Evidence: "So today most people build agents around the LLM. You start with the LLM, you add a response API, you give it tools, you add memory, and then you make sure you log everything correctly, which can give you you know all the benefits that ActiveGraph will give you, but ActiveGraph asks, what if you build around the log?"
- He says the agent’s changing state should be flattened into a single immutable event log that serves as the ground truth. (`explicit`)
  - Evidence: "And a lot of people, what the agent does and how the agent changes are tracked in two different places, but I'm saying let's flatten that down into a single immutable event log, and this is the ground truth of the agent."
- He claims this typed event log enables replay, rollback, and forking. (`explicit`)
  - Evidence: "But yeah, in the end you get this beautiful typed event log, which gives you replays. It gives you rollbacks and it gives you forks."
- He says some graph changes should require a proposed patch and approval, especially for sensitive edits like prompts or facts. (`explicit`)
  - Evidence: "Um and you know, I earlier I talked about policies, so some graph changes require a proposed patch before approval."
- He reports that the controlled self-modification loop produced modest but statistically significant improvements on long mem eval. (`explicit`)
  - Evidence: "And it actually did have, you know, modest, but like statistically significant improvement on long mem eval scores."
- He proposes that long-running agents need an experiential world model, not only a predictive one. (`explicit`)
  - Evidence: "So I'll caveat that. But I'm building this, I'm starting to really think that long-running agents need not just a world world model and like a predictive world model, but what I might call an experiential world model."

### Topics Covered
- **Event-sourced agent runtime** — The core idea that the agent should be modeled as an auditable, event-sourced graph rather than a message thread.
- [[agent-memory|Immutable agent log]] — The use of a single immutable log as the source of truth for agent state, history, and change tracking.
- [[agent-reliability-and-durable-execution|Behavior-driven state updates]] — Mechanisms for attaching reacting code to graph updates and letting it emit new events.
- [[inference-engineering|Policy-controlled mutation]] — Using policies to constrain edits, approvals, and safe self-modification.
- [[software-factories|Agent packs]] — Bundling object schemas, tools, behaviors, and policies into reusable agent units.
- [[agent-memory|Graph-backed memory]] — Treating logs and replays as the basis for memory and recovery in long-running systems.
- [[agent-evaluations|Self-improving evaluation loops]] — Controlled self-improvement loops that propose changes, test them, and keep only verified gains.
- **Experiential world model** — The idea that an agent’s identity and learning may derive from its own experiential history.

### Tools And Named Systems
- **ActiveGraph** — The speaker’s experimental runtime for building auditable agents around an event-sourced graph.
- **BabyAGI** — The earlier project that the speaker says launched his multi-year agent research thread.
- **Replit** — The coding platform he used to build a coding agent on top of ActiveGraph.
- [[claude-code|Claude Code]] — The coding assistant he says helped with some self-modification work.
- **LangSmith** — The observability product he mentions as an alternative way to get some of the same logging benefits.
- **Kafka** — The message-driven distributed system he cites as an inspiration for shared-state worker coordination.

### Novel Concepts And Methods
- **Log-centered state model** — Represent agent state as a single immutable event log that becomes the source of truth for behavior and change history.
- **Behavior-driven event loop** — Attach behaviors that react to graph changes and emit new events back into the same shared state.
- **Graph-query context management** — Use graph queries to assemble the relevant subset of state as context for a behavior.
- **Policy-gated self-modification** — Require proposed patches plus policy checks before accepting certain self-modifications.
- **Checkpointed replay recovery** — Resume interrupted evaluation runs from the logged checkpoint instead of restarting from scratch.

### Open Questions
- **If LLM-agent patterns have less training data than older shared-state architectures, how much of the runtime design should be optimized for that prior knowledge gap versus for raw model capability?** — This affects whether the runtime should primarily encode old systems patterns or lean on newer model behavior.
- **What should an experiential world model look like in a long-running agent, and how should it be trained or updated from logs and replays?** — This is the talk’s key unresolved conceptual leap from logging to durable agent identity and learning.
- **How should policies be specified so they are strict enough to prevent harmful edits but flexible enough for autonomous improvement?** — The practical usefulness of self-modifying agents depends on the right approval boundary.

### Derived Links And Source Material
- [[youtube-khVX_BUnEwU-transcript]] — dedicated official recording transcript.
- [[youtube-khVX_BUnEwU]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/khVX_BUnEwU--2026-07-01-yohei-nakajima-active-graph-agent-runtime-babyagi-4.json`.

### Speaker Context
- [[yohei-nakajima|Yohei Nakajima]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[yohei-nakajima]]

## Official YouTube Recording
- [[youtube-khVX_BUnEwU|Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital]] — official AI Engineer YouTube recording published 2026-07-22.
- Evidence status: [[youtube-khVX_BUnEwU-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-khVX_BUnEwU]] - dedicated official event recording.
- [[youtube-khVX_BUnEwU-transcript]] - dedicated official recording transcript.

- Source video: `youtube-khVX_BUnEwU`
- Slide deck: [[youtube-khVX_BUnEwU-slides|Slides: Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital]] — 31 visible slide image(s).
![[assets/slides/khVX_BUnEwU/slide-001.jpg]]
![[assets/slides/khVX_BUnEwU/slide-002.jpg]]
![[assets/slides/khVX_BUnEwU/slide-003.jpg]]
- Slide-derived themes for `youtube-khVX_BUnEwU`: track, july, engineering, future, graph, ieee, greene, behavior.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/khVX_BUnEwU.txt` (3,675 words).

## Transcript Markdown
- [[youtube-khVX_BUnEwU-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/khVX_BUnEwU.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-khVX_BUnEwU` — 3,675 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-khVX_BUnEwU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-khVX_BUnEwU`: graph, pack, activegraph, called, didn, code, event, state.
- Slide-derived themes for `youtube-khVX_BUnEwU`: track, july, engineering, future, graph, ieee, greene, behavior.
- Evidence links for `youtube-khVX_BUnEwU` (primary event evidence): [[youtube-khVX_BUnEwU]], [[youtube-khVX_BUnEwU-transcript]], [[youtube-khVX_BUnEwU-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
