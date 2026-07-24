---
title: "From Signal to PR: Anatomy of a Self-Improving Agent"
category: "talks"
date: "2026-06-30"
time: "11:10am-11:30am"
track: "Evals"
room: "Track 5"
speakers: ["Jason Lopatecki"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Evals"
scheduleRoom: "Track 5"
scheduleLabels: ["Evals", "Track 5", "sponsor", "confirmed"]
---
# From Signal to PR: Anatomy of a Self-Improving Agent

## Conference Context
- Date/time: 2026-06-30 · 11:10am-11:30am
- Track/room: Evals · Track 5
- Speaker(s): Jason Lopatecki
- Session type/status: sponsor · confirmed

- Track: Evals
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
What if your observability platform didn't just tell you something was wrong, but told you why, and opened a PR with the fix? We'll walk through how we built Autopilot at Arize: an autonomous investigation agent that triggers on monitor alerts or schedules, pulls traces into a working filesystem, runs root-cause analysis, and produces actionable assets: a PR with prompt or code changes ready for review. We'll cover the architecture decisions (cloud agents vs. sandboxed containers, AI harness + skills), why traces-on-a-filesystem is the key unlock for agent-driven debugging, and how we dogfooded the system on our own agent, Alyx, before shipping it to customers. You'll leave with a concrete picture of what "observability that fixes itself" looks like in practice, and where and why the human stays in the loop.

## Synthesis
### Transcript-Backed Summary
The talk argues that observability is changing from a human-centered dashboard workflow into an agentic debugging loop that can investigate, propose fixes, and eventually open a PR. The mechanism is to trigger an agent on an alert or schedule, pull traces and related artifacts into a filesystem-backed working context, and use skills plus a sandbox or harness to gather evidence and shape the fix. The main tradeoff is that autonomy only works if the skills, data packaging, and execution environment are carefully designed, because the hard part is not generating a patch but deciding whether it is trustworthy enough to ship and when a human must stay in the loop.

### Key Takeaways
- More traces and logs can become useful rather than noisy when agents can use them to reconstruct the software path and run continuous repair loops.
  - Evidence: "Um by logging and tracing orders and orders of magnitude more than we do today, we can actually create these continuous loops that know what path was taking your software and and and actually have it fix itself."
- Putting the right artifacts into files inside a repo is a key unlock because harnesses are much better at working with files than with raw telemetry.
  - Evidence: "That's kind of the magic of this skills which are composable for the agent to go actually put a fix."
- The quality of the skill surface matters as much as the model itself; the agent needs the right data in the right shape, not just direct access to everything.
  - Evidence: "Um but but you've got to kind of design the skill surface area in a way that Claude can really really work well and and and it's not just like point Claude at the data."
- Evals are part of the operational loop, not a separate layer, because they can ride on production traces and preprocessed failure patterns to catch known issues again.
  - Evidence: "pre-processed information on the data that that and then as signal is running it's using data from the evals that were layered on um in addition to all the raw data that it has there Um it but it tends to be like you build an eval for a failure you've seen before a lot"

### Claims From The Talk
- The speaker argues that observability is moving from human-only UI inspection toward a combination of coding agents and skills. (`explicit`)
  - Evidence: "Um and and today it's I would argue it's a lot of 2.0 which is like this combination of coding agent."
- He says the target state is systems that autonomously fix themselves rather than only surface problems for humans. (`explicit`)
  - Evidence: "Evals add another layer to this. Um but really what we're at here is is how do I build systems that autonomously fix themselves?"
- He describes the current loop as one where the agent often prepares evidence or an issue first, and the human continues from there. (`explicit`)
  - Evidence: "It's looking at the data before a human even looks at it. Um and and what you move from there is is kind of humans grabbing tickets to to having some amount of evidence um some deep evidence relative to whatever you're looking at already sitting in front of you by the time you actually even look at it."
- He reports that Signal can create issues, evaluators, and datasets from recurring problems while attaching evidence. (`explicit`)
  - Evidence: "It can create an issue in your repo. You can create an evaluator from this. Maybe u maybe there's a a specific problem by which you want to catch again."
- He says many customers prefer VPC-hosted sandboxes because they do not want production systems connected out to Anthropic. (`explicit`)
  - Evidence: "So we install in the VPC of a lot of you know bigname companies out there um from from Uber to um to bookings to you name it and and these people don't want to send their connections out but they'll they'll use a s you know many many companies um are very comfortable installing a V into a VPC and actually connecting it up."

### Topics Covered
- **Agentic observability** — Using observability data as input for autonomous debugging and repair loops
- [[autoresearch|Self-improving systems]] — Systems that improve themselves through repeated investigation and repair
- [[coding-agents|Filesystem-backed debugging]] — Debugging workflows built around traces, logs, and repo files
- [[agent-evaluations|Observability skills]] — Composable skills that gather and shape observability context
- [[agent-evaluations|Online evals]] — Evaluations that run alongside production traces as operational checks
- **Sandboxed agent execution** — Running debugging agents in sandboxes rather than only on a laptop
- [[human-oversight-and-review-dynamics|Human-in-the-loop repair]] — Human review after the agent assembles evidence and proposes a fix

### Tools And Named Systems
- **Arize AX** — Arize's SaaS observability and agent platform used to host Signal
- **Phoenix** — Arize's open source product for starting quickly
- **Signal** — Arize's autonomous investigation agent that runs on alerts or schedules
- [[cloud-code|Cloud Code]] — Local coding environment used as the baseline experience being extended into the loop
- [[claude|Claude]] — Model used in the skill-and-data example for debugging with traces
- **Pyroscope** — Profiling tool whose skills can surface memory issues and cohort analysis
- [[daytona|Daytona]] — Sandbox option mentioned as an alternative execution environment
- [[github|GitHub]] — Repository and issue surface integrated into the workflow

### Novel Concepts And Methods
- **Event-triggered loop** — Event-or-schedule-triggered investigation loop
- **Skill-based context assembly** — Skill-driven context gathering
- **Filesystem-backed debugging** — Filesystem-backed debugging workflow
- **Sandboxed execution** — Sandboxed agent execution for debugging
- **Online eval layering** — Online evals layered on production traces

### Open Questions
- **What is the minimal skill surface area needed for an LLM to debug trace data reliably without overcomplicating the workflow?** — This determines how reusable and maintainable the agent debugging stack can be.
- **How should systems calibrate confidence so they can move faster without pushing too many wrong fixes for human review?** — This is the main gating problem in making the loop safe enough to automate.
- **How much extra tracing and logging can teams afford before the cost outweighs the benefit of a continuous repair loop?** — The approach depends on whether expanded telemetry stays practical at scale.

### Derived Links And Source Material
- [[youtube-9HbzAWnKbo4-transcript]] — dedicated official recording transcript.
- [[youtube-9HbzAWnKbo4]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/9HbzAWnKbo4--2026-06-30-jason-lopatecki-from-signal-to-pr-anatomy-of-a-self-improving-agent.json`.

### Speaker Context
- [[jason-lopatecki|Jason Lopatecki]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[jason-lopatecki]]

## Official YouTube Recording
- [[youtube-9HbzAWnKbo4|From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize]] — official AI Engineer YouTube recording published 2026-07-24.
- Evidence status: [[youtube-9HbzAWnKbo4-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-9HbzAWnKbo4]] - dedicated official event recording.
- [[youtube-9HbzAWnKbo4-transcript]] - dedicated official recording transcript.

- Source video: `youtube-9HbzAWnKbo4`
- Slide deck: [[youtube-9HbzAWnKbo4-slides|Slides: From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize]] — 17 visible slide image(s).
![[assets/slides/9HbzAWnKbo4/slide-001.jpg]]
![[assets/slides/9HbzAWnKbo4/slide-002.jpg]]
![[assets/slides/9HbzAWnKbo4/slide-003.jpg]]
- Slide-derived themes for `youtube-9HbzAWnKbo4`: track, july, macro, signal, engineering, future, consumes, telemetry.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/9HbzAWnKbo4.txt` (3,797 words).

## Transcript Markdown
- [[youtube-9HbzAWnKbo4-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/9HbzAWnKbo4.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-9HbzAWnKbo4` — 3,797 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-9HbzAWnKbo4`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-9HbzAWnKbo4`: skills, data, traces, maybe, running, well, signal, cloud.
- Slide-derived themes for `youtube-9HbzAWnKbo4`: track, july, macro, signal, engineering, future, consumes, telemetry.
- Evidence links for `youtube-9HbzAWnKbo4` (primary event evidence): [[youtube-9HbzAWnKbo4]], [[youtube-9HbzAWnKbo4-transcript]], [[youtube-9HbzAWnKbo4-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
