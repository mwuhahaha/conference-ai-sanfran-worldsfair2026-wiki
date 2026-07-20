---
title: "The Unreasonable Effectiveness of Separating the Task from the Model"
category: "talks"
date: "2026-07-01"
time: "9:40am-10:00am"
track: "Harness Engineering"
room: "Main Stage"
speakers: ["Maxime Rivest", "Isaac Miller"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Harness Engineering"
scheduleRoom: "Main Stage"
scheduleLabels: ["Harness Engineering", "Main Stage", "keynote", "confirmed"]
---
# The Unreasonable Effectiveness of Separating the Task from the Model

## Conference Context
- Date/time: 2026-07-01 · 9:40am-10:00am
- Track/room: Harness Engineering · Main Stage
- Speaker(s): Maxime Rivest, Isaac Miller
- Session type/status: keynote · confirmed

- Track: Harness Engineering
- Room: Main Stage
- Session type: keynote
- Status: confirmed

## Session Description
By declaring your task’s inputs and outputs without initially considering model capability, you create the space needed to figure out the model execution later. DSPy’s entire promise is that you should evaluate and execute your AI engineering at a level higher than a specific prompt template or a particular provider’s API shape: the Signature. However, models have evolved significantly over the last few years. How can the same input and output specifications still work in a world now filled with tools, RLMs, and Skills? By defining your task strictly through its inputs and outputs, the underlying implementation becomes completely flexible. You can experiment with different models, settings, weights, templating strategies, and output formats, all without touching your actual AI workflow. Consequently, you can leverage components built by others and focus entirely on your core AI task. In this talk we will present how dspy 3.5 makes it easier much easier. DSPy has its roots in prompt optimization, where we build efficient ways to conduct search and learning beneath the signature. In this talk we will give a preview of DSPy 4.0 where we use the fact that models have now passed a tipping point for two critical concepts we have always needed. First, we no longer need to limit the search space to a single instruction block per LLM call; models can now reliably write the code underneath a signature themselves—so they should. Second, traditional prompt optimization has always required a scalar metric, which is notoriously one of the hardest parts to get right. What if a DSPy program could learn directly from your interactions with users? Ultimately, all you care about is that the function you call respects the inputs and outputs of your signature. You can let the models figure out the rest.

## Synthesis
### Synthesized Breakdown
Please welcome to the stage Maxim Rest and Isaac Miller. Wow. Isaac, myself, all of the DSPI community are so grateful to be here today to get to talk to you about AI programming DSPI and the unreasonable effectiveness of separating the task from the model, its harness, and all of the implementation details. When you think about it, in programming, if we want to repeat the tasks often, we make it a function.

### Speaker And Company Context
- [[maxime-rivest|Maxime Rivest]] — Core Contributor at [[dspy|DSPy]].
- [[isaac-miller|Isaac Miller]] — Lead Maintainer of DSPy; Co-Founder at [[cmpnd|cmpnd]].

### Topics Covered
- [[agentic-search]]
- [[coding-agents]]

### Derived Links And Source Material
- [[youtube-GgLQ02aO-hs-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/GgLQ02aO-hs.txt` (2,751 words).
- [[youtube-GgLQ02aO-hs]] — related YouTube source page.
- [[youtube-GgLQ02aO-hs-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis uses the official schedule and only a dedicated manifest-matched recording transcript for session-level claims and topic extraction. Related official-channel, external, and broad livestream sources remain supporting context and do not stand in for the scheduled session.
## People
- [[maxime-rivest]]
- [[isaac-miller]]

## Official YouTube Recording
- [[youtube-GgLQ02aO-hs|The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest, DSPy]] — official AI Engineer YouTube recording published 2026-07-19.
- Evidence status: [[youtube-GgLQ02aO-hs-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-GgLQ02aO-hs]] - dedicated official event recording.
- [[youtube-GgLQ02aO-hs-transcript]] - dedicated official recording transcript.

- Source video: `youtube-GgLQ02aO-hs`
- Slide deck: [[youtube-GgLQ02aO-hs-slides|Slides: The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest, DSPy]] — 22 visible slide image(s).
![[assets/slides/GgLQ02aO-hs/slide-001.jpg]]
![[assets/slides/GgLQ02aO-hs/slide-002.jpg]]
![[assets/slides/GgLQ02aO-hs/slide-003.jpg]]
- Slide-derived themes for `youtube-GgLQ02aO-hs`: task, effectiveness, separating, unreasonable, model, programs, should, fair.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/GgLQ02aO-hs.txt` (2,751 words).

## Transcript Markdown
- [[youtube-GgLQ02aO-hs-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/GgLQ02aO-hs.txt`.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-GgLQ02aO-hs` — 2,751 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-GgLQ02aO-hs`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-GgLQ02aO-hs`: implementation, solve, dspi, model, should, problem, models, techniques.
- Slide-derived themes for `youtube-GgLQ02aO-hs`: task, effectiveness, separating, unreasonable, model, programs, should, fair.
- Evidence links for `youtube-GgLQ02aO-hs` (primary event evidence): [[youtube-GgLQ02aO-hs]], [[youtube-GgLQ02aO-hs-transcript]], [[youtube-GgLQ02aO-hs-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
