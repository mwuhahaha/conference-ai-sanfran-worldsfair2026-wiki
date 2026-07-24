---
title: "From Systems of Record to Systems of Context"
category: "talks"
date: "2026-07-01"
time: "12:05pm-12:25pm"
track: "Graphs"
room: "Track 5"
speakers: ["Omri Bruchim"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Graphs"
scheduleRoom: "Track 5"
scheduleLabels: ["Graphs", "Track 5", "sponsor", "confirmed"]
---
# From Systems of Record to Systems of Context

## Conference Context
- Date/time: 2026-07-01 · 12:05pm-12:25pm
- Track/room: Graphs · Track 5
- Speaker(s): Omri Bruchim
- Session type/status: sponsor · confirmed

- Track: Graphs
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
Enterprise AI agents are moving fast, but most of them still hit the same wall in production: they have access to tools, documents, APIs, and databases, but they do not understand the real context of how work gets done. At monday.com, we are building agents that operate across real customer workflows, internal product surfaces, knowledge, permissions, memory, and actions. The hard part is not just calling the right tool or retrieving the right document. The hard part is building a reliable context layer that helps agents understand users, work objects, organizational knowledge, prior decisions, business rules, and the relationships between them. This talk will explore the emerging idea of the context graph: a living, queryable layer that connects entities, history, permissions, decisions, and meaning across an organization. Foundation Capital describes context graphs as the next major enterprise AI opportunity because agents need more than rules. They need decision traces: how rules were applied, where exceptions were made, who approved what, and what precedent actually governs reality. I will share how we think about this opportunity at monday.com, how we are implementing parts of it in practice, and what we have learned from building AI agents inside a real AI work platform. The talk will include concrete examples, including how context is collected, represented, retrieved, governed, and evaluated. The audience will leave with a practical framework for moving beyond one-off RAG pipelines and prompt stuffing toward a reusable context layer that compounds over time, improves agent quality, and becomes a strategic moat for companies building AI-native products.

## Synthesis
### Transcript-Backed Summary
This talk argues that production enterprise agents fail less because they cannot fetch information and more because they lack understanding of how work is actually connected. The proposed fix is a reusable context layer, called the monday world model, that is built ahead of time from work activity, relationships, priorities, and decisions so the assistant can answer questions like what to focus on right now. The implementation uses a slow engine for durable patterns and a fast engine for live signals, which makes the system more resilient and better at urgency, but also means it must constantly balance freshness against bias, noise, and lagging reality.

### Key Takeaways
- The talk’s core distinction is that understanding matters more than context, memory, or retrieval by themselves.
  - Evidence: "uh those are two totally different things and almost everyone mix between them. Understanding is the word that we're going to focus the entire the entire talk."
- The monday world model is meant to help the assistant understand who the user is, why the work matters, and what not to do.
  - Evidence: "This is what we called the Monday world model. Help you um understand why this matter um how to help you, who you are, when and and what's not to do."
- The context layer compounds over time as more data is captured and the profile becomes sharper.
  - Evidence: "And the crucial part is that it compounds. Every day the data is captured, the layers fill in and the profile sharpens."
- As the system understands more, users can rely on it more, which is the intended practical payoff of the design.
  - Evidence: "The more it sees, the more it understands. And the more it understands, the more you can lean on it."

### Claims From The Talk
- The speaker argues that the core production problem for enterprise agents is not missing data or retrieval, but missing understanding. (`explicit`)
  - Evidence: "The problem was never the missing of data, the retrieval. The problem is like the missing understanding."
- The speaker reports that context understanding must be built ahead of time, before a user asks a question, rather than assembled only at runtime. (`explicit`)
  - Evidence: "So understanding understanding of the context has to be ahead of time. Um you need to build it much before someone asks the question."
- The speaker describes their implementation as two engines operating on different time windows and schedules: a slow engine for long-term patterns and a fast engine for current state. (`explicit`)
  - Evidence: "So how do we build that data model? Um we use two engines running on different time windows and schedules."
- The speaker claims this design makes the system resilient because sources are isolated and serve-time logic can fall back to the last verified context instead of failing outright. (`explicit`)
  - Evidence: "The data model, it's resilient. Sources are isolated so a bad feed can't break the rest. And the thin layer of logic that runs at serve time verifies part of the context against live data while the rest falls back to the last verified context."
- The speaker says the resulting model is unique to how a person works and does not solve everything, especially because it trails the live world and inherits bias from its signals. (`explicit`)
  - Evidence: "And the data model is unique. It's unique to how you work. We're not pretending this solves everything."

### Topics Covered
- [[agent-memory|Systems of context]] — The shift from storing records to building a live layer that explains how work is connected and why decisions were made.
- [[agent-memory|Work understanding]] — The idea that enterprise assistants need durable understanding of a user and their work, not just retrieved documents or messages.
- [[agent-memory|Context graph]] — A queryable organizational layer that links entities, history, permissions, and decisions into reusable context.
- [[agent-memory|Dual-timescale architecture]] — A two-speed architecture that combines long-term pattern learning with short-term state tracking.

### Tools And Named Systems
- **monday.com** — The enterprise work platform the speakers use as the source of work records and context.
- [[slack|Slack]] — The team communication system used as one of the work-context sources.
- [[github|GitHub]] — The code-hosting and change-history system used in the analogy for tracing why work items exist.
- [[gemini|Gemini]] — The large language model product explicitly mentioned as an example of an assistant that still misses connected understanding.
- **GPT** — The large language model product explicitly mentioned as an example of an assistant that still misses connected understanding.

### Novel Concepts And Methods
- **Dual-timescale context modeling** — Maintain two context-processing engines, one slow and historical and one fast and recent, to combine durable user patterns with live work state.
- **Offline context precomputation** — Precompute work context offline so the assistant can reason over a served model instead of assembling meaning only when a question arrives.
- **Breadcrumb aggregation** — Aggregate breadcrumbs from boards, emails, meetings, calendar, and messages into a structured work model rather than relying on ad hoc retrieval.

### Open Questions
- **How can the system reliably separate important signals from noise as the context model grows?** — That is the central quality problem the speaker says remains hardest to solve.
- **How should the model handle new users who have no reliable historical data yet?** — The speaker notes that the approach is weakest when there is not yet enough history to reason from.

### Derived Links And Source Material
- [[youtube-Btk8wDUVs74-transcript]] — dedicated official recording transcript.
- [[youtube-Btk8wDUVs74]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/Btk8wDUVs74--2026-07-01-omri-bruchim-from-systems-of-record-to-systems-of-context.json`.

### Speaker Context
- [[omri-bruchim|Omri Bruchim]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[omri-bruchim]]

## Official YouTube Recording
- [[youtube-Btk8wDUVs74|From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com]] — official AI Engineer YouTube recording published 2026-07-22.
- Evidence status: [[youtube-Btk8wDUVs74-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-Btk8wDUVs74]] - dedicated official event recording.
- [[youtube-Btk8wDUVs74-transcript]] - dedicated official recording transcript.

- [[youtube-Btk8wDUVs74-slides]] — extracted from the related public AI Engineer video.

- Source video: `youtube-Btk8wDUVs74`
- Slide deck: [[youtube-Btk8wDUVs74-slides|Slides: From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com]] — 19 visible slide image(s).
![[assets/slides/Btk8wDUVs74/slide-001.jpg]]
![[assets/slides/Btk8wDUVs74/slide-002.jpg]]
![[assets/slides/Btk8wDUVs74/slide-003.jpg]]
- Slide-derived themes for `youtube-Btk8wDUVs74`: data, track, july, missing, stack, records, systems, context.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/Btk8wDUVs74.txt` (2,510 words).

## Transcript Markdown
- [[youtube-Btk8wDUVs74-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/Btk8wDUVs74.txt`.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-Btk8wDUVs74` — 2,510 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Btk8wDUVs74`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Btk8wDUVs74`: data, understand, monday, context, help, model, user, over.
- Slide-derived themes for `youtube-Btk8wDUVs74`: data, track, july, missing, stack, records, systems, context.
- Evidence links for `youtube-Btk8wDUVs74` (primary event evidence): [[youtube-Btk8wDUVs74]], [[youtube-Btk8wDUVs74-transcript]], [[youtube-Btk8wDUVs74-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
