---
title: "Closing Keynote — Theo Browne"
category: "talks"
date: "2026-07-01"
time: "4:30pm-4:50pm"
track: "Main Stage"
room: "Main Stage"
speakers: ["Theo Browne"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Main Stage"
scheduleRoom: "Main Stage"
scheduleLabels: ["Main Stage", "Main Stage", "keynote", "confirmed"]
---
# Closing Keynote — Theo Browne

## Conference Context
- Date/time: 2026-07-01 · 4:30pm-4:50pm
- Track/room: Main Stage · Main Stage
- Speaker(s): Theo Browne
- Session type/status: keynote · confirmed

- Track: Main Stage
- Room: Main Stage
- Session type: keynote
- Status: confirmed

## Session Description
No official description published in the schedule data.

## Synthesis
### Transcript-Backed Summary
The talk argues that AI has changed the scale at which software should be imagined: models have moved from reliable tool use to longer-running work and then orchestration, so the old boundaries around what is too big are collapsing. The mechanism is to push models to spawn and verify subwork, then redesign products around breadth, extension, and simpler automation rather than around old assumptions like terminals, code preservation, or hand-built services. The tradeoff is that you will not match incumbents on every dimension, but you can cover enough surface area to let users finish the rest themselves. Practically, that means projects that once looked like startups, internal platforms, or bespoke services can now be feasible as side projects, markdown files on a cron, or narrower products with real leverage.

### Key Takeaways
- A model that can orchestrate and verify work changes how much of a project can be delegated to it.
  - Evidence: "And it base, but it understands itself. And it base, but it understands itself. And it knows how to spawn additional models and knows how to spawn additional models and knows how to spawn additional models and break up work in a way where it could be break up work in a way where it could be break up work in a way where it could be completed more reliably and then completed more reliably and then completed more reliably and then verified afterwards."
- A lot of developer attachment to old workflows and code habits is inertia rather than necessity.
  - Evidence: "We heads that we have to start fighting. We heads that we have to start fighting. We have to take the step back and think, have to take the step back and think, have to take the step back and think, is this how we do things cuz it's right, is this how we do things cuz it's right, is this how we do things cuz it's right, or is this how we do things cuz it's or is this how we do things cuz it's or is this how we do things cuz it's just how we've always done it?"
- Some recurring internal services can be reduced to a markdown file plus cron-driven automation.
  - Evidence: "I just literally markdown file now. I just literally markdown file now. I just literally wrote like, go to these four GitHub wrote like, go to these four GitHub wrote like, go to these four GitHub repos, look at all the open PRs, figure repos, look at all the open PRs, figure repos, look at all the open PRs, figure out what the current status of the work out what the current status of the work out what the current status of the work is, is, is, and then help me prioritize it."
- A product can win by covering enough surface area and letting users build the missing vertical features themselves.
  - Evidence: "missing themselves. missing themselves. If you architect your systems and you If you architect your systems and you If you architect your systems and you architect your products in such a way architect your products in such a way architect your products in such a way that users can do things that they you that users can do things that they you that users can do things that they you never would have guessed."
- What used to be a startup-sized effort may now be small enough to fit a side project.
  - Evidence: "The fact that what used to be a process. The fact that what used to be a process. The fact that what used to be a startup is now a side project."

### Claims From The Talk
- The speaker says Mythos is a jump to orchestration, not just a better coding model. (`explicit`)
  - Evidence: "figure it out a lot of the time. figure it out a lot of the time. Mythos is another jump Mythos is another jump Mythos is another jump to orchestration."
- The speaker says the models are getting better faster than people are. (`explicit`)
  - Evidence: "before. before. The models are getting better faster The models are getting better faster The models are getting better faster than we are."
- The speaker says software developers are in a skeuomorphic phase. (`explicit`)
  - Evidence: "we got over it. we got over it. We're currently in our skeuomorphic We're currently in our skeuomorphic We're currently in our skeuomorphic phase as software developers."
- The speaker says many projects have shifted down a tier, so work that used to be a startup can now be a side project. (`explicit`)
  - Evidence: "the tiers have shifted. the tiers have shifted. Everything is now one tier lower. Everything is now one tier lower."
- The speaker says an idea should feel a little stupid if it is big enough. (`explicit`)
  - Evidence: "real. real. If your idea doesn't feel stupid, If your idea doesn't feel stupid, If your idea doesn't feel stupid, it's cuz your idea's not big enough."

### Topics Covered
- **Capability eras** — The talk frames model progress as distinct eras of capability.
- [[coding-agents|Orchestration]] — The talk emphasizes models coordinating and verifying multi-step work.
- **Skeuomorphic habits** — The talk argues developers are overvaluing familiar interfaces and workflows.
- **Breadth and depth** — The talk contrasts software breadth with depth to explain modern product strategy.
- [[agentic-search|Extensibility]] — The talk stresses products that let users extend missing features themselves.

### Tools And Named Systems
- [[sonnet-3-5|Sonnet 3.5]] — A model used as the baseline example of the earlier tool-call era.
- **Opus 4.5** — A model used to illustrate the jump to longer-running tasks.
- **Mythos** — A model named as part of the orchestration era.
- [[fable|Fable]] — A second model named alongside Mythos in the orchestration comparison.
- [[codex|Codex]] — A tool named as something markdown can be piped into for execution.
- [[claude|Claude]] — Another tool named as something markdown can be piped into for execution.
- **Vercel** — A platform used as the example of deeper full-stack front-end leaning server features.
- **AWS** — A platform used as the incumbent example of broad feature coverage.
- [[slack|Slack]] — A platform used as the example of a weak but extensible product surface.
- [[git|Git]] — The version-control system used as the example of an old industry-shaping default.

### Novel Concepts And Methods
- **Model orchestration** — Push the model to spawn and verify subwork instead of limiting it to a single pass.
- **Stop convincing and start embracing** — Stop treating familiar tooling and workflow shapes as if they are inherently correct.
- **Delete-and-reset** — Use deletion and reset when sunk cost is blocking a better answer.
- **Markdown automation** — Collapse recurring work into a markdown file that runs on a cron.
- **Breadth-depth design** — Evaluate software by its breadth across a surface area and its depth in a chosen slice.

### Open Questions
- **What belongs in the gap between a side project and something too big?** — The talk implies the old size categories have shifted, but the new boundary is still undefined.
- **How wide can a product go before the breadth tradeoff stops making sense?** — The argument depends on breadth now being viable, but the practical limit is still unclear.
- **What architecture best lets users add missing features themselves without the vendor building everything?** — The speaker's strategy depends on extensibility, but the enabling product shape is not fully specified.

### Derived Links And Source Material
- [[youtube-xUnRQ9vLXxo-transcript]] — dedicated official recording transcript.
- [[youtube-xUnRQ9vLXxo]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/xUnRQ9vLXxo--2026-07-01-theo-browne-closing-keynote-theo-browne.json`.

### Speaker Context
- [[theo-browne|Theo Browne]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[theo-browne]]

## Official YouTube Recording
- [[youtube-xUnRQ9vLXxo|Everything we knew about software has changed — Theo Browne, @t3dotgg ​]] — official AI Engineer YouTube recording published 2026-07-08.
- Evidence status: [[youtube-xUnRQ9vLXxo-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-xUnRQ9vLXxo]] - dedicated official event recording.
- [[youtube-xUnRQ9vLXxo-transcript]] - dedicated official recording transcript.

- Source video: `youtube-xUnRQ9vLXxo`
- Slide deck: [[youtube-xUnRQ9vLXxo-slides|Slides: What do we build now? — @t3dotgg]] — 4 visible slide image(s).
![[assets/slides/xUnRQ9vLXxo/slide-001.jpg]]
![[assets/slides/xUnRQ9vLXxo/slide-002.jpg]]
![[assets/slides/xUnRQ9vLXxo/slide-003.jpg]]
- Slide-derived themes for `youtube-xUnRQ9vLXxo`: colorado, boulder, keynote, founder.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/xUnRQ9vLXxo.txt` (9,663 words).

## Transcript Markdown
- [[youtube-xUnRQ9vLXxo-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/xUnRQ9vLXxo.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-xUnRQ9vLXxo` — 9,663 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-xUnRQ9vLXxo`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-xUnRQ9vLXxo`: used, model, look, code, does, models, trying, even.
- Evidence links for `youtube-xUnRQ9vLXxo` (primary event evidence): [[youtube-xUnRQ9vLXxo]], [[youtube-xUnRQ9vLXxo-transcript]], [[youtube-xUnRQ9vLXxo-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
