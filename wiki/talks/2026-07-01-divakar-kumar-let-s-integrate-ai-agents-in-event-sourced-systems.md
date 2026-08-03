---
title: "Let's integrate AI Agents in Event-Sourced Systems"
category: "talks"
date: "2026-07-01"
time: "11:40am-12:00pm"
track: "AI in Finance"
room: "Track 3"
speakers: ["Divakar Kumar"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "AI in Finance"
scheduleRoom: "Track 3"
scheduleLabels: ["AI in Finance", "Track 3", "session", "confirmed"]
---
# Let's integrate AI Agents in Event-Sourced Systems

## Conference Context
- Date/time: 2026-07-01 · 11:40am-12:00pm
- Track/room: AI in Finance · Track 3
- Speaker(s): Divakar Kumar
- Session type/status: session · confirmed

- Track: AI in Finance
- Room: Track 3
- Session type: session
- Status: confirmed

## Session Description
Fraud detection has always been a race against time. In traditional event-sourced systems, every transaction, login, or transfer is captured as a sequence of immutable events. These events tell a clear story — but only after the fact. What if events could do more than just record history? What if they could talk back? In this talk, we’ll explore how agentic event-driven systems transform fraud detection. Imagine every PaymentInitiated, LoginAttempt, or DeviceChanged event not just being logged, but immediately consumed by an autonomous Fraud Detection Agent. This agent correlates events across accounts, reasons over historical event streams, and generates new events like SuspiciousActivityFlagged or TransactionHeldForReview. Through a real-world inspired use case in banking and digital payments, we’ll show: - How event sourcing provides the perfect memory layer for fraud detection agents - Patterns for agents to safely inject new domain events without violating invariants - How to avoid runaway feedback loops when multiple agents interact (e.g., fraud + compliance + customer service agents) - Governance, auditing, and explainability challenges when autonomous agents take part in mission-critical workflows By the end of this session, you’ll see how event-driven DDD systems evolve when agents stop being passive consumers and start actively shaping the event stream — turning fraud detection from a reactive process into a proactive, adaptive defense.

## Synthesis
### Transcript-Backed Summary
This talk argues that event-sourced systems already provide the memory fraud detection agents need, but the useful move is to add agents only where rule-based and ML systems are uncertain. The mechanism is a two-tier architecture: existing deterministic scoring handles most transactions, while projections fed from event streams build a semantic layer that specialist agents use to inspect transaction, account, device, and payment context. Those agents run in a bounded fan-out and a verdict layer emits a new event back into the saga, but the design carries real tradeoffs around latency, false positives, and loop control, so the practical consequence is a proactive fraud workflow that augments rather than replaces the existing event-driven system.

### Key Takeaways
- Keep the existing deterministic systems in place and use agents only for the ambiguous gray-zone cases.
  - Evidence: "We we are just trying to handle few of the areas like that is the gray zone areas with the help of agentic AI processing."
- Build a semantic layer from projected events so agents can reason over cross-context context instead of isolated service data.
  - Evidence: "So, the idea is like we need to gather all the data from all these different contexts and to have or build a semantic layer or you could call it as a materialized view which you could further use within your agent careful."
- Treat latency as a first-class design constraint by using short-term memory and in-memory state for agent decisions.
  - Evidence: "And you also need to have a memory layer. For this particular use case like we are using an inch um short memory because uh you you can't really um rely on the long-term memory because you need to um adhere to the uh SLA that you uh provided to the customers because for for the transaction uh to be processed like it should be sub 500 milliseconds."

### Claims From The Talk
- The speaker argues that event sourcing gives the fraud system an append-only memory of business facts, because commands are stored as events instead of mutating state. (`explicit`)
  - Evidence: "And we are following event sourcing as our methodology to store the events. So, what happens is like whenever user initiate a command, so that goes into our event store as an event as a business fact."
- The speaker argues that the agent layer should not replace the existing rule-based or ML systems, but should handle only the gray-zone cases they struggle to classify. (`explicit`)
  - Evidence: "We we are just trying to handle few of the areas like that is the gray zone areas with the help of agentic AI processing."
- The speaker argues that different bounded contexts, whether relational or NoSQL, still need a semantic layer to provide enough context for AI agents to decide well. (`explicit`)
  - Evidence: "And basically, like you could have a relational database or no SQL database. In turn, like you you need to just create the semantic layer for you to provide enough context to these AI agents."
- The speaker reports a tier-two design where a risk analyzer agent and a behavior analyzer agent both contribute to a final verdict, which is then emitted as an event. (`explicit`)
  - Evidence: "One is the risk analyzer agent, the other one is the behavior analyzer agent. And once these agents like come to a conclusion based on the different tools that it has, it will finally send the response to the verdict."
- The speaker says the agent memory must be short-term and in-memory because the transaction flow has a sub-500 millisecond SLA. (`explicit`)
  - Evidence: "And you also need to have a memory layer. For this particular use case like we are using an inch um short memory because uh you you can't really um rely on the long-term memory because you need to um adhere to the uh SLA that you uh provided to the customers because for for the transaction uh to be processed like it should be sub 500 milliseconds."

### Topics Covered
- [[autoresearch|event-sourced fraud detection]] — Fraud detection built on event-sourced business facts and historical event streams.
- [[context-engineering-and-knowledge-architecture|bounded contexts]] — Separate domain boundaries that keep transaction, account, device, and payment data isolated.
- [[agent-memory|semantic layer]] — A denormalized layer assembled from projections so agents can query cross-context state.
- **agent fan-out** — A tier-two design that routes one event to multiple specialist agents before a final decision.

### Tools And Named Systems
- **Cosmos DB** — The event store the speaker says they are using for the architecture.

### Novel Concepts And Methods
- **event sourcing** — Use event sourcing as the append-only memory layer for fraud-relevant business facts.
- **CDC-driven projection pipeline** — Feed projections into a semantic layer through CDC or change feed so agents can query denormalized context.
- **fan-out agent routing** — Fan out a single event to specialist agents, then combine their outputs in a verdict layer that emits the final outcome as an event.

### Open Questions
- **What stop condition should govern agent reasoning loops for each fraud use case?** — Without an explicit stop rule, the agent can loop too long or fail to converge on a decision.
- **How can the semantic context stay rich enough for fraud reasoning while still meeting the sub-500 millisecond processing target?** — The talk makes latency a hard constraint, so freshness and speed have to be balanced carefully.
- **How should the verdict layer combine multiple agent outputs without recreating the same false-positive problem as the older rule-based system?** — The speaker says false positives remain a real issue, so the aggregation strategy is not fully settled.

### Derived Links And Source Material
- [[youtube-o6U_2vd967Y-transcript]] — dedicated official recording transcript.
- [[youtube-o6U_2vd967Y]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/o6U_2vd967Y--2026-07-01-divakar-kumar-let-s-integrate-ai-agents-in-event-sourced-systems.json`.

### Speaker Context
- [[divakar-kumar|Divakar Kumar]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[divakar-kumar]]

## Official YouTube Recording
- [[youtube-o6U_2vd967Y|Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft]] — official AI Engineer YouTube recording published 2026-07-30.
- Evidence status: [[youtube-o6U_2vd967Y-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-o6U_2vd967Y]] - dedicated official event recording.
- [[youtube-o6U_2vd967Y-transcript]] - dedicated official recording transcript.

- Source video: `youtube-o6U_2vd967Y`
- Slide deck: [[youtube-o6U_2vd967Y-slides|Slides: Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft]] — 32 visible slide image(s).
![[assets/slides/o6U_2vd967Y/slide-001.jpg]]
![[assets/slides/o6U_2vd967Y/slide-002.jpg]]
![[assets/slides/o6U_2vd967Y/slide-003.jpg]]
- Slide-derived themes for `youtube-o6U_2vd967Y`: track, july, fair, vent, rule, engineering, future, finance.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/o6U_2vd967Y.txt` (3,518 words).

## Transcript Markdown
- [[youtube-o6U_2vd967Y-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/o6U_2vd967Y.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-o6U_2vd967Y` — 3,518 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-o6U_2vd967Y`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-o6U_2vd967Y`: layer, transaction, context, events, contexts, event, system, trying.
- Slide-derived themes for `youtube-o6U_2vd967Y`: track, july, fair, vent, rule, engineering, future, finance.
- Evidence links for `youtube-o6U_2vd967Y` (primary event evidence): [[youtube-o6U_2vd967Y]], [[youtube-o6U_2vd967Y-transcript]], [[youtube-o6U_2vd967Y-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
