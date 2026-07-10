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

## Media Evidence
No related AI Engineer channel video found yet.

- [[youtube-I2cbIws9j10-transcript]] — full cached transcript markdown for the related YouTube source.

- Source video: `youtube-I2cbIws9j10`
- Slide deck: [[youtube-I2cbIws9j10-dense-slides|Dense Slides: WF26: Harness Engineering & Startup Battlefield ft. Garry Tan, Mike Krieger, @t3dotgg , DSPy]] — 11 visible slide image(s); 11 HTML recreation(s).
![[assets/dense-slides/I2cbIws9j10/slide-001.jpg]]
![[assets/dense-slides/I2cbIws9j10/slide-002.jpg]]
![[assets/dense-slides/I2cbIws9j10/slide-003.jpg]]
- Additional slide evidence: [[youtube-I2cbIws9j10-slides|Slides: WF26: Harness Engineering & Startup Battlefield ft. Garry Tan, Mike Krieger, @t3dotgg , DSPy]]
- Slide-derived themes for `youtube-I2cbIws9j10`: context, window, selects, response, facts, retry, coerce, rollback.

## Evidence Graph
This evidence graph is generated from currently linked source material: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Media Signals
- `youtube-I2cbIws9j10` — 91,792 transcript words; 7 slide-derived text signals
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: context, window, selects, response, facts, retry, coerce, rollback.
- Evidence links for `youtube-I2cbIws9j10`: [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]

### Agent Reading Notes
Use these signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[maxime-rivest]]
- [[isaac-miller]]

## Livestream Segment
- [Watch in livestream at 00:53:36](https://www.youtube.com/watch?v=I2cbIws9j10&t=3216s) — WF26: Harness Engineering & Startup Battlefield (Day 3).
- Match basis: speaker and title; timed captions matched Maxime Rivest, effectiveness, model, separating, task, unreasonable.
- Confidence: high automated match; prefer a dedicated cut-video recording when one exists.

## Synthesis
### Synthesized Breakdown
Mhm. Mhm. Mhm. Ladies and gentlemen, welcome to the AI Engineer World's Fair.

### Speaker And Company Context
- [[maxime-rivest|Maxime Rivest]] — Core Contributor at [[dspy|DSPy]].
- [[isaac-miller|Isaac Miller]] — Lead Maintainer of DSPy; Co-Founder at [[cmpnd|cmpnd]].

### Topics Covered
- [[agent-security]]
- [[agentic-search]]
- [[agentic-web]]
- [[ai-sandboxes]]
- [[coding-agents]]
- [[mcp]]

### Derived Links And Source Material
- [[youtube-I2cbIws9j10-transcript]] — transcript markdown; source cache `raw/sources/youtube-livestream-transcripts/I2cbIws9j10.txt` (91,792 words).
- [[youtube-I2cbIws9j10]] — related YouTube source page.
- [[youtube-I2cbIws9j10-slides]] — slide evidence.
- [[youtube-I2cbIws9j10-dense-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- [[agent-ready-accessibility|Agent-Ready Accessibility]] — Designing for agents and designing for accessibility converge around explicit structure, reachable controls, and understandable state.

### Evidence Boundary
This synthesis uses the official schedule plus cached video transcripts. Official AI Engineer World's Fair San Francisco 2026 livestreams and cut videos are primary event video sources for transcript/slide evidence; external, historical, or speaker-matched videos remain supporting context unless manually verified as exact official event recordings.
