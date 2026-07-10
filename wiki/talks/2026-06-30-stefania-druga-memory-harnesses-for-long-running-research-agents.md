---
title: Memory Harnesses for Long-Running Research Agents
category: talks
date: '2026-06-30'
time: '11:40am-12:00pm'
track: Memory & Continual Learning
room: Main Stage
speakers:
  - Stefania Druga
sourceLabels:
  - Official conference schedule
  - Public YouTube metadata
last_auto_summarized: '2026-07-04T08:21:47.410Z'
scheduleTrack: "Memory & Continual Learning"
scheduleRoom: "Main Stage"
scheduleLabels: ["Memory & Continual Learning", "Main Stage", "session", "confirmed"]
---
# Memory Harnesses for Long-Running Research Agents

## Official Schedule Context
- Date/time: 2026-06-30 · 11:40am-12:00pm
- Track/room: Memory & Continual Learning · Main Stage
- Speaker(s): Stefania Druga
- Session type/status: session · confirmed

## Summary
Stefania Druga's World's Fair session centers on the reliability layer that lets research agents keep working coherently over hundreds of turns. The official abstract argues that the model itself is often not the first thing to fail; the surrounding harness is. In long-running literature review, experiment-running, and paper-drafting workflows, the agent can contradict a decision it made dozens of turns earlier, redo completed work, lose track of the original research question, or treat state-management failures as if they were prompt-writing problems. The talk frames memory as a measurable engineering system: three-tier memory, progressive disclosure, recall-first compaction, sub-agent isolation, architectural memory beyond a vector database, and trajectory-level evaluation of whether the harness is actually improving behavior.

The connected material makes the scientific setting more concrete. Druga's related AI Engineer video, "Real-time Experiments with an AI Co-Scientist," includes slide evidence around crystal growth, supersaturation, salt and water solutions, yeast fermentation, temperature, nucleation, open-source tools, and Jacdac-style instrumentation. Those slides are supporting context rather than a confirmed recording of this exact World's Fair session, but they show the kind of research-agent environment where memory failures become operationally expensive: an AI co-scientist must remember prior hypotheses, experiment conditions, observed outcomes, and tool constraints while iterating through physical or simulated experiments. The dense and reconstructed slide pages reinforce that this is not just abstract agent orchestration; it is about agents embedded in experimental loops where continuity matters.

Druga's profile adds the institutional frame. She is a Research Scientist at Sakana AI in Tokyo working on novel architectures beyond the transformer, after prior work associated with Google DeepMind. That background makes this session sit at the intersection of agent infrastructure, scientific discovery workflows, and post-transformer research systems. For this wiki, the page should be read as a memory-and-harness counterpart to the co-scientist material: if AI systems are going to read papers, run experiments, and draft scientific outputs over long horizons, they need durable memory structures that preserve decisions, prevent duplicated effort, and keep the system anchored to the research objective.

## Schedule Labels
- Track: Memory & Continual Learning
- Room: Main Stage
- Session type: session
- Status: confirmed

## Official Description
At Sakana AI we build agents that run for hundreds of turns to read literature, run experiments, and draft papers. The model rarely breaks. The harness around it is the weak point: the agent contradicts a decision it made 80 turns ago, redoes finished work, or drifts from the question it started on. This is the binding-constraint thesis. For long-horizon tasks, reliability is set as much by the harness as by the model as clearly instantiated in autoresearch recent efforts. This is a field guide to the harness's memory layer. I'll trace a real research agent through its lifecycle, show exactly where context rot and drift set in, and cover the patterns that hold over 100+ turns: three-tier memory, progressive disclosure, recall-first compaction, sub-agent isolation, and architectural memory beyond the vector database. I will show how to measure whether your memory harness actually helps, at the trajectory level, so you stop tuning prompts to fix what's really a state-management bug.

## Related YouTube Video
[Real-time Experiments with an AI Co-Scientist - Stefania Druga, fmr. Google Deepmind](https://www.youtube.com/watch?v=wNH3q9pqn0U) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## People
- [[stefania-druga]]

## Supporting Slides
- [[youtube-wNH3q9pqn0U-slides]] — extracted from the related public AI Engineer video.
## Slide Evidence
- Slide-only cropped deck: [[youtube-wNH3q9pqn0U-dense-slides]] (14 viable slide images).
- Related slide/OCR pages:
- [[youtube-wNH3q9pqn0U-dense-slides]]
- [[youtube-wNH3q9pqn0U-reconstructed-slides]]
- [[youtube-wNH3q9pqn0U-slides]]
- Slide-derived terms: `microsoft`, `crystal`, `growth`, `water`, `solution`, `demo`, `salt`, `yeast`, `fermentation`, `open-source`, `open`, `jacdac`, `nucleation`, `science`, `supersaturation`, `dissolves`, `than`, `temperature`

## Source-Derived Enrichment
This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Source Signals
- `youtube-wNH3q9pqn0U` — 2 slide-derived text signals
- Slide-derived themes for `youtube-wNH3q9pqn0U`: sound, request, beaker, crystals.
- Evidence links for `youtube-wNH3q9pqn0U`: [[youtube-wNH3q9pqn0U]], [[youtube-wNH3q9pqn0U-slides]], [[youtube-wNH3q9pqn0U-dense-slides]], [[youtube-wNH3q9pqn0U-reconstructed-slides]]

### Article Use
Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.
## Slides
- Source video: `youtube-wNH3q9pqn0U`
- Slide deck: [[youtube-wNH3q9pqn0U-dense-slides|Dense Slides: Real-time Experiments with an AI Co-Scientist - Stefania Druga, fmr. Google Deepmind]] — 14 visible slide image(s); 14 HTML recreation(s).
![[assets/dense-slides/wNH3q9pqn0U/slide-001.jpg]]
![[assets/dense-slides/wNH3q9pqn0U/slide-002.jpg]]
![[assets/dense-slides/wNH3q9pqn0U/slide-003.jpg]]
- Additional slide evidence: [[youtube-wNH3q9pqn0U-slides|Slides: Real-time Experiments with an AI Co-Scientist - Stefania Druga, fmr. Google Deepmind]], [[youtube-wNH3q9pqn0U-reconstructed-slides|Reconstructed Slides: Real-time Experiments with an AI Co-Scientist - Stefania Druga, fmr. Google Deepmind]]
- Slide-derived themes for `youtube-wNH3q9pqn0U`: sound, request, beaker, crystals.
