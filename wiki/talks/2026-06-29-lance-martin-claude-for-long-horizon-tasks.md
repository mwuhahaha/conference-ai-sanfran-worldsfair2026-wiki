---
title: "Claude for long-horizon tasks"
category: "talks"
date: "2026-06-29"
time: "1:55pm-2:15pm"
track: "Claws & Personal Agents"
room: "Track 1"
speakers: ["Lance Martin"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Claws & Personal Agents"
scheduleRoom: "Track 1"
scheduleLabels: ["Claws & Personal Agents", "Track 1", "session", "confirmed"]
---
# Claude for long-horizon tasks

## Conference Context
- Date/time: 2026-06-29 · 1:55pm-2:15pm
- Track/room: Claws & Personal Agents · Track 1
- Speaker(s): Lance Martin
- Session type/status: session · confirmed

- Track: Claws & Personal Agents
- Room: Track 1
- Session type: session
- Status: confirmed

## Session Description
Claude is capable of long horizon tasks. In this talk, we'll share lessons learned about building agent harnesses for reliable and secure long-horizon work. This include decoupling the brain and hands, self-verification, self-learning, and design for evolving agent harnesses.

## Synthesis
### Transcript-Backed Summary
Martin argues that long-horizon AI work is no longer primarily a prompt-design problem; it is a harness-design problem, because models are now capable of hours of autonomous work and need infrastructure that matches that horizon. His main prescription is to separate the model's reasoning process from execution, verification, and memory: keep the harness stateless, keep session state append-only, use independent verifier contexts, and let the model write to general memory substrates that can later be consolidated offline. He also shows that these patterns matter in practice: looped verification can drive strong benchmark performance, in-band memory writing gets better as model capacity rises, and offline dreaming can repair bad memories that would otherwise cause repeated failures. The practical consequence is a shift from single-user, reactive agents to shared, proactive org-level harnesses that are more reliable, safer with credentials, and easier for teams to use.

### Key Takeaways
- Treat the harness as stateless and the session as durable if you want long-horizon work to survive failures cleanly.
  - Evidence: "They're stored in a separate vault. So, this decoupling actually makes it quite reliable and safe, particularly for long-horizon tasks."
- Do not use the same context to do work and judge it; separate verification context improves reliability.
  - Evidence: "Um and the reason is the verifier context can be tuned very specifically for the critical verification task."
- Let the model structure and maintain its own memory instead of forcing a fixed memory schema.
  - Evidence: "Let the model structure and maintain its own memory. Don't give it a prescribed memory schema."
- Use offline consolidation to inspect memory traces and correct mistakes that would otherwise persist.
  - Evidence: "Because what it does is it looks at your memory store and it looks at all your prior traces or sessions and kind of can find and correct errors."
- Build async agents that can proactively alert users based on shared organizational context, not just react to prompts.
  - Evidence: "Um and this is a very important kind of new kind of UX that I think is going to be more and more common with async agents that kind of access to organizational context."

### Claims From The Talk
- Martin argues that async agents only become practical once models can sustain much longer autonomous work than the old chat-and-local-coding regime. (`strong`)
  - Evidence: "In order to really unlock async, we needed longer task horizons. And so we're starting to see that now."
- He reports that putting the harness and the sandbox in the same container makes long-horizon agents brittle because losing the container can lose the session. (`explicit`)
  - Evidence: "We put the harness in the sandbox in the same container. Now the problem here is, what happens if the harness dies or the container dies?"
- He says sharing secrets with a long-running execution container is a security concern as models become more capable. (`explicit`)
  - Evidence: "So, for example, giving Claude access to a bunch of your secrets and letting it run for 10 hours and not watching it can be a little bit spooky and have some security concerns, especially as models get extremely capable."
- He argues that decoupling the brain from the hands, with a stateless harness, append-only session, and separate vault, improves reliability and safety. (`explicit`)
  - Evidence: "They're stored in a separate vault. So, this decoupling actually makes it quite reliable and safe, particularly for long-horizon tasks."
- He says verification should be separated into its own context window because self-grading in the same context can produce confabulation and odd artifacts. (`explicit`)
  - Evidence: "And so, what we found is it's quite effective to separate verification into a separate context window."
- He reports that looped verifier setups let frontier models self-correct by encoding the signal in the environment rather than relying on human steering. (`strong`)
  - Evidence: "What you see is the frontier capability models are extremely good with this pattern of kind of loops in software and and kind of verification because what happens is instead of encoding steering me and into like me as the human, you're encoding the signal into the environment."
- He says Claude has gotten much better at in-band memory writing across model generations. (`explicit`)
  - Evidence: "So, the key point I'm making here is that Claude has gotten much better at this in-band memory writing across model generations."
- He reports that offline dreaming can correct an incorrect memory and prevent the repeated failure it causes in the task. (`explicit`)
  - Evidence: "With the dreaming, this error is corrected, and it's able to properly localize itself and not fall fall down this trap."

### Topics Covered
- [[coding-agents|Long-horizon async agents]] — Agents that can run for hours with limited human steering and need durable orchestration.
- **Brain-hand decoupling** — Architectures that separate reasoning and coordination from execution environments.
- [[agent-evaluations|Verifier loops]] — Using an independent context to judge work rather than self-grading in the same context.
- [[agent-memory|In-band memory writing]] — Writing memory during execution through simple writable storage primitives.
- [[agent-memory|Dreaming-based memory consolidation]] — Offline passes that inspect traces and repair memory errors.
- [[agent-evaluations|Org-level harnesses]] — Shared harnesses with organizational identity, organizational context, and team-wide access.
- **Proactive agent UX** — Agents that can alert users based on shared context rather than only responding to direct prompts.

### Tools And Named Systems
- **Messages API** — The prompt-response API the speaker describes as a simple base for building harnesses.
- **Agent SDK** — The programmatic surface for calling Claude Code as a harness.
- **Managed Agents** — The packaged API surface that includes both the harness and managed deployment infrastructure.
- [[claude-code|Claude Code]] — The synchronous coding agent the speaker cites as a shift toward about an hour of work.
- [[claude-tag|Claude Tag]] — The org-level harness the speaker uses as an example of multiplayer async agents.
- [[sonnet-3-5|Sonnet 3.5]] — The earlier model used in the Pokémon memory-writing example.
- **4 6** — The newer model used in the memory-writing and continual-learning comparisons.

### Novel Concepts And Methods
- **Append-only session log** — Keep the harness stateless and move durable state into an append-only session log.
- **Separate verifier context** — Grade work in a separate verifier context instead of in the same context that produced it.
- **Build-verifier loop** — Run a build context and a verifier context in a loop until the verifier accepts the outcome.
- **General memory substrate** — Let the model manage memory through a general substrate rather than a prescriptive schema.
- **Offline memory dreaming** — Use an offline dreaming pass to inspect traces and repair bad memories.
- **Multiplayer org harness** — Share one harness across many users with organizational identity and context.

### Open Questions
- **What memory substrate best supports model-managed memory when the structure stays highly programmable instead of prescriptive?** — The talk suggests memory design matters as much as model capability, but leaves open how to choose the best general-purpose substrate.
- **How should offline dreaming be evaluated to tell whether the memory corrections are actually worth the extra compute?** — If dreaming is going to be part of an agent harness, teams need a reliable way to measure whether it improves real task performance.
- **What combination of model capability, memory, security, and architecture is required to sustain the long-horizon gap for real agents?** — The talk argues that long-horizon performance is not just a model issue, so the open question is which system components matter most.

### Derived Links And Source Material
- [[youtube-9QebvrrY3KY-transcript]] — dedicated official recording transcript.
- [[youtube-9QebvrrY3KY]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/9QebvrrY3KY--2026-06-29-lance-martin-claude-for-long-horizon-tasks.json`.

### Speaker Context
- [[lance-martin|Lance Martin]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[lance-martin]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-ib-wTAvCZqg-dense-slides]] (4 viable slide images).
- Related slide/OCR pages:
- [[youtube-ib-wTAvCZqg-dense-slides]]
- [[youtube-ib-wTAvCZqg-reconstructed-slides]]
- [[youtube-ib-wTAvCZqg-slides]]
- Slide-derived terms: `generation`, `bias`, `tokens`, `question`, `search`, `documents`, `llms`, `recent`, `awws`, `step`, `lististr`, `retrieval`, `recency`, `tasks`, `typically`, `used`, `attend`, `models`

## Official YouTube Recording
- [[youtube-9QebvrrY3KY|Claude for Long-Horizon Tasks — Lance Martin, Anthropic]] — official AI Engineer YouTube recording published 2026-07-22.
- Evidence status: [[youtube-9QebvrrY3KY-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-9QebvrrY3KY]] - dedicated official event recording.
- [[youtube-9QebvrrY3KY-transcript]] - dedicated official recording transcript.
- [[youtube-ib-wTAvCZqg]] - supporting context; not the exact session recording.

- [[youtube-9QebvrrY3KY-slides]] — extracted from the related public AI Engineer video.

- Source video: `youtube-9QebvrrY3KY`
- Slide deck: [[youtube-9QebvrrY3KY-slides|Slides: Claude for Long-Horizon Tasks — Lance Martin, Anthropic]] — 4 visible slide image(s).
![[assets/slides/9QebvrrY3KY/slide-001.jpg]]
![[assets/slides/9QebvrrY3KY/slide-002.jpg]]
![[assets/slides/9QebvrrY3KY/slide-003.jpg]]
- Slide-derived themes for `youtube-9QebvrrY3KY`: generator, lance, martin, member, technical, staff, engineering, future.
- Source video: `youtube-ib-wTAvCZqg`
- Slide deck: [[youtube-ib-wTAvCZqg-dense-slides|Dense Slides: Architecting and Testing Controllable Agents: Lance Martin]] — slide evidence page.
- Additional slide evidence: [[youtube-ib-wTAvCZqg-slides|Slides: Architecting and Testing Controllable Agents: Lance Martin]], [[youtube-ib-wTAvCZqg-reconstructed-slides|Reconstructed Slides: Architecting and Testing Controllable Agents: Lance Martin]]
- Slide-derived themes for `youtube-ib-wTAvCZqg`: step, display, search, documents, retrieval, typically, used, most.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/9QebvrrY3KY.txt` (4,450 words).

## Transcript Markdown
- [[youtube-9QebvrrY3KY-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/9QebvrrY3KY.txt`.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-9QebvrrY3KY` — 4,450 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-9QebvrrY3KY`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-9QebvrrY3KY`: memory, models, claude, model, context, interesting, harness, important.
- Slide-derived themes for `youtube-9QebvrrY3KY`: generator, lance, martin, member, technical, staff, engineering, future.
- Evidence links for `youtube-9QebvrrY3KY` (primary event evidence): [[youtube-9QebvrrY3KY]], [[youtube-9QebvrrY3KY-transcript]], [[youtube-9QebvrrY3KY-slides]]
- `youtube-ib-wTAvCZqg` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-ib-wTAvCZqg`: step, display, search, documents, retrieval, typically, used, most.
- Evidence links for `youtube-ib-wTAvCZqg` (supporting context only): [[youtube-ib-wTAvCZqg]], [[youtube-ib-wTAvCZqg-slides]], [[youtube-ib-wTAvCZqg-dense-slides]], [[youtube-ib-wTAvCZqg-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
