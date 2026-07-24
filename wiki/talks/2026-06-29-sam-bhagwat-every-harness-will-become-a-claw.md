---
title: "Every Harness Will Become A Claw"
category: "talks"
date: "2026-06-29"
time: "3:20pm-3:40pm"
track: "Claws & Personal Agents"
room: "Track 1"
speakers: ["Sam Bhagwat"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Claws & Personal Agents"
scheduleRoom: "Track 1"
scheduleLabels: ["Claws & Personal Agents", "Track 1", "session", "confirmed"]
---
# Every Harness Will Become A Claw

## Conference Context
- Date/time: 2026-06-29 · 3:20pm-3:40pm
- Track/room: Claws & Personal Agents · Track 1
- Speaker(s): Sam Bhagwat
- Session type/status: session · confirmed

- Track: Claws & Personal Agents
- Room: Track 1
- Session type: session
- Status: confirmed

## Session Description
Most of the Harness discussion is just a reprise of Context Engineering from last summer. But it's not 2025 anymore. We live in a Claude Code world, and the best way to think about a harness is Context engineering + Coding Agents = Harness. Harnesses are a magical DX because of specific features like planning mode, parallel subagents, skills, background tasks etc. But it doesn't stop there. People are shoving their harnesses in a box, making them listen to external events, giving them channels (the ability to ping its users), and a heartbeat. They are making them into Claws. And actually, harnesses _want_ to become claws, so they can take up more share of mind, suit collaboration workflows, and be available afk. I propose "Steinberger's law", a spinoff of Zawinski's law: every harness will expand until it becomes a Claw

## Synthesis
### Transcript-Backed Summary
Sam Bhagwat argues that the software stack is moving from simple LLMs to agents, then to harnesses, and finally to claws: always-on systems that can take initiative, persist across sessions, and act through multiple channels. He explains the mechanism as a bundle of capabilities such as context engineering, planning mode, parallel subagents, skills, background tasks, persistence, heartbeats, and trace-driven learning. The central tradeoff is power versus control: the more access and autonomy a harness gains, the more useful it becomes, but the harder it is to bound and the more likely the market is to consolidate around a few high-value winners. His practical advice is to build for the capabilities users need now, but expect another shakeout as the category expands.

### Key Takeaways
- Planning mode, parallel subagents, skills, and background tasks are concrete reasons harnesses feel more capable than older agent setups.
  - Evidence: "There's planning mode. We all see this in cloud code. Um parallel sub aents being able to fan out multiple tasks at the same time."
- Always-on harnesses change the product surface because they can live in collaboration channels instead of only in a local editor.
  - Evidence: "What do I mean by a harness that is always on? Well, you might be talking to it in Slack. Maybe you're talking to it in Slack along with your colleagues, right?"
- Continual learning is attractive, but the right implementation is still unsettled.
  - Evidence: "Uh it often will do continual learning, right? So this concept that you know the agent the harness runs and then you know based on the traces that it generates it it sort of autoimproves itself and there's different ways of doing this."
- Builders should keep up with the faster pace of change and make sure their systems cover the capabilities users actually need.
  - Evidence: "So the the first thing is um the first thing is don't get this is the reason that like events are are are important that like staying up with like if the rate of change increases 3 to 4x that means you know we need to figure out what's going on even more frequently."

### Claims From The Talk
- He says the industry is entering a harness era after last year's focus on agents. (`explicit`)
  - Evidence: "Um and uh the thing that I'm going to say is is welcome to the harness era. What do I mean by the harness era?"
- He distinguishes harnesses from ordinary agents by durability and doggedness. (`explicit`)
  - Evidence: "put action but um you know qualities here are starting to emerge when we move from an agent to a harness durability and doggedness um a friend of mine was referring to an agent that he was using and he called it dogged which I really like and I'm taking that for this talk, right?"
- He says the field is moving from local harnesses to always-on cloud harnesses. (`explicit`)
  - Evidence: "I think this is something we've seen over the last really 3 months. Um, and I think we're all still starting to grapple with what it means, which is this movement from a local harness to a cloud harness where the harness is always on."
- He describes claws as harnesses that learn continually from the traces they produce. (`explicit`)
  - Evidence: "Uh it often will do continual learning, right? So this concept that you know the agent the harness runs and then you know based on the traces that it generates it it sort of autoimproves itself and there's different ways of doing this."
- He argues people want these systems with power and control, not just as a boxed-in claw. (`explicit`)
  - Evidence: "And so we furiously looked at the the you know the features that you know openclaw have that Hermes agent have and say and and we we've said like look you know a lot of people a lot of folks want these features but they want them with power and control."
- He predicts that products in this category must be either very valuable or very frequent to stay relevant. (`explicit`)
  - Evidence: "So there's there's sort of like it either has to be very economically valuable or has to be very frequent."

### Topics Covered
- [[software-factories|Harness era]] — The stage where the industry focus has shifted from agents to harnesses.
- [[inference-engineering|Agentic spectrum]] — The ladder of autonomy from LLMs to agents to harnesses to claws.
- [[ai-sandboxes|Always-on cloud harnesses]] — Harnesses that run continuously in cloud sandboxes and broader collaboration surfaces.
- [[coding-agents|Claws]] — Harnesses that initiate work, listen to external events, and learn over time.
- **Market shakeout** — A future consolidation in which only a few high-value systems remain salient.
- [[agent-security|Power and control tradeoff]] — The tension between giving systems more capability and keeping them under user control.

### Tools And Named Systems
- [[slack|Slack]] — Collaboration surface used for always-on harness interaction.
- [[github|GitHub]] — Destination for code changes created by the harness.
- **WhatsApp** — Channel the harness can be pinged through.
- **Telegram** — Channel the harness can be pinged through.
- **Android** — Platform cited as part of the 2010s mobile-platform shakeout example.
- **iOS** — Platform cited as part of the 2010s mobile-platform shakeout example.

### Novel Concepts And Methods
- [[context-engineering|Context engineering]] — Using prompt and state management to make an agent reliable across turns.
- **Planning mode** — Letting the harness pause and organize work before acting.
- **Parallel subagents** — Fanning out multiple tasks concurrently to increase throughput.
- **Thread persistence** — Saving and resuming conversation state after disconnects or long gaps.
- **Heartbeat activation** — Waking on a schedule or external event instead of only responding to a user turn.
- **Trace-driven continual learning** — Improving the harness from generated traces and auto-generated skills.

### Open Questions
- **What is the right way to do continual learning without losing control or making the harness too autonomous?** — The talk treats continual learning as promising but unresolved.
- **Which interaction surfaces best support an always-on harness across Slack, mobile, and local workflows?** — The talk argues that harnesses are shifting into collaboration surfaces beyond a single local editor.
- **Which claws will survive the coming shakeout, and what makes them durable enough to stay in users' minds?** — The talk predicts consolidation around a small number of high-value systems.

### Derived Links And Source Material
- [[youtube-8qWIPUia2O8-transcript]] — dedicated official recording transcript.
- [[youtube-8qWIPUia2O8]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/8qWIPUia2O8--2026-06-29-sam-bhagwat-every-harness-will-become-a-claw.json`.

### Speaker Context
- [[sam-bhagwat|Sam Bhagwat]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[sam-bhagwat]]

## Official YouTube Recording
- [[youtube-8qWIPUia2O8|Every Harness Will Become A Claw — Sam Bhagwat, Mastra]] — official AI Engineer YouTube recording published 2026-07-21.
- Evidence status: [[youtube-8qWIPUia2O8-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-8qWIPUia2O8]] - dedicated official event recording.
- [[youtube-8qWIPUia2O8-transcript]] - dedicated official recording transcript.

- Source video: `youtube-8qWIPUia2O8`
- Slide deck: [[youtube-8qWIPUia2O8-slides|Slides: Every Harness Will Become A Claw — Sam Bhagwat, Mastra]] — 13 visible slide image(s).
![[assets/slides/8qWIPUia2O8/slide-001.jpg]]
![[assets/slides/8qWIPUia2O8/slide-002.jpg]]
![[assets/slides/8qWIPUia2O8/slide-003.jpg]]
- Slide-derived themes for `youtube-8qWIPUia2O8`: engineering, future, ascending, agentic, spectrum, ells, actions, retry.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/8qWIPUia2O8.txt` (2,869 words).

## Transcript Markdown
- [[youtube-8qWIPUia2O8-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/8qWIPUia2O8.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-8qWIPUia2O8` — 2,869 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-8qWIPUia2O8`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-8qWIPUia2O8`: harness, maybe, harnesses, cloud, well, local, little, running.
- Slide-derived themes for `youtube-8qWIPUia2O8`: engineering, future, ascending, agentic, spectrum, ells, actions, retry.
- Evidence links for `youtube-8qWIPUia2O8` (primary event evidence): [[youtube-8qWIPUia2O8]], [[youtube-8qWIPUia2O8-transcript]], [[youtube-8qWIPUia2O8-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
