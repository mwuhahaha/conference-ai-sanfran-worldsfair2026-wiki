---
title: "Evals in AI: A Deep Dive"
category: "talks"
date: "2026-06-29"
time: "12:10pm-1:10pm"
track: "Workshops Day 1"
room: "Track 1"
speakers: ["Tejas Kumar"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Workshops Day 1"
scheduleRoom: "Track 1"
scheduleLabels: ["Workshops Day 1", "Track 1", "workshop", "confirmed"]
---
# Evals in AI: A Deep Dive

## Conference Context
- Date/time: 2026-06-29 · 12:10pm-1:10pm
- Track/room: Workshops Day 1 · Track 1
- Speaker(s): Tejas Kumar
- Session type/status: workshop · confirmed

- Track: Workshops Day 1
- Room: Track 1
- Session type: workshop
- Status: confirmed

## Session Description
“Our evals pass and our velocity is up, so it works.” It’s the most reassuring sentence in AI engineering and also the most dangerous. Teams are shipping more code than ever while incidents per PR and change-failure rates climb, and the instruments meant to catch this are quietly broken. This talk takes apart both halves of that false comfort. First, why velocity lies: the same AI-driven throughput that lights up your dashboard is what’s eroding quality underneath it. Then we explore four ways offline evals deceive you: LLM-as-judge bias (your grader rewards confident, wordy, wrong answers over terse correct ones), staleness, distribution shift between your golden set and real traffic, and single-score evals that hide which step of an agent actually failed. The centerpiece is a live demo. We’ll wire up an LLM judge on stage and watch it crown a confident, friendly, factually wrong answer. Then we’ll fix it live on stage with a three-line rubric change. Same model, different instrument. From there we’ll build up what to measure instead: traces and spans, production observability, probe-based evaluation, error budgets, and quality leading indicators that sit beside every velocity number. Attendees will leave with a five-line checklist they can apply Monday. No prior eval tooling required. If you’ve ever shipped something agentic and had a nagging feeling the dashboards were too kind, this is for you.

## Synthesis
### Synthesized Breakdown
“Our evals pass and our velocity is up, so it works.” It’s the most reassuring sentence in AI engineering and also the most dangerous. Teams are shipping more code than ever while incidents per PR and change-failure rates climb, and the instruments meant to catch this are quietly broken. This talk takes apart both halves of that false comfort. First, why velocity lies: the same AI-driven throughput that lights up your dashboard is what’s eroding quality underneath it.

### Speaker And Company Context
- [[tejas-kumar|Tejas Kumar]] — AI Engineer at [[ibm|IBM]].

### Topics Covered
- [[coding-agents]]

### Derived Links And Source Material
- [[youtube-C_GG5g38vLU]] — related YouTube source page.
- [[youtube-C_GG5g38vLU-slides]] — slide evidence.
- [[youtube-C_GG5g38vLU-reconstructed-slides]] — slide evidence.
- [[youtube-C_GG5g38vLU-dense-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[tejas-kumar]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-C_GG5g38vLU-dense-slides]] (1 viable slide images).
- Related slide/OCR pages:
- [[youtube-C_GG5g38vLU-dense-slides]]
- [[youtube-C_GG5g38vLU-reconstructed-slides]]
- [[youtube-C_GG5g38vLU-slides]]
- Slide-derived terms: `model`, `const`, `news`, `engineering`, `future`, `harness`, `task`, `hacker`, `upvote`, `import`, `story`, `session`, `europe`, `lght`, `https`, `news.ycombinator.com`, `stories`, `highest-ranked`

## Media Evidence
- [[youtube-C_GG5g38vLU]] - supporting context; not the exact session recording.

- Source video: `youtube-C_GG5g38vLU`
- Slide deck: [[youtube-C_GG5g38vLU-dense-slides|Dense Slides: Harnesses in AI: A Deep Dive — Tejas Kumar, IBM]] — slide evidence page.
- Additional slide evidence: [[youtube-C_GG5g38vLU-slides|Slides: Harnesses in AI: A Deep Dive — Tejas Kumar, IBM]], [[youtube-C_GG5g38vLU-reconstructed-slides|Reconstructed Slides: Harnesses in AI: A Deep Dive — Tejas Kumar, IBM]]
- Slide-derived themes for `youtube-C_GG5g38vLU`: model, engineering, future, console, stories, tool, registry, story.

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-C_GG5g38vLU` — 8 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-C_GG5g38vLU`: model, engineering, future, console, stories, tool, registry, story.
- Evidence links for `youtube-C_GG5g38vLU` (supporting context only): [[youtube-C_GG5g38vLU]], [[youtube-C_GG5g38vLU-slides]], [[youtube-C_GG5g38vLU-dense-slides]], [[youtube-C_GG5g38vLU-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
