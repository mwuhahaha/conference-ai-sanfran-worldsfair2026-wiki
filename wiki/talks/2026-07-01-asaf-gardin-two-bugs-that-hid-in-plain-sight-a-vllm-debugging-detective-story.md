---
title: "Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story"
category: "talks"
date: "2026-07-01"
time: "3:20pm-3:40pm"
track: "Inference"
room: "Track 9"
speakers: ["Asaf Gardin", "Yuval Belfer"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Inference"
scheduleRoom: "Track 9"
scheduleLabels: ["Inference", "Track 9", "session", "confirmed"]
---
# Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story

## Conference Context
- Date/time: 2026-07-01 · 3:20pm-3:40pm
- Track/room: Inference · Track 9
- Speaker(s): Asaf Gardin, Yuval Belfer
- Session type/status: session · confirmed

- Track: Inference
- Room: Track 9
- Session type: session
- Status: confirmed

## Session Description
Your model generates gibberish. Once every thousand prompts. High confidence scores. No crashes. No warnings. We hit this twice while building Jamba models. First: A request gets misclassified during scheduling, loads stale state from a previous prompt cache slot, and confidently generates nonsense. Second: Logprob spikes during RL training that looked like training instability-until we noticed they tracked with rollout count, then with cache size. In this talk, we'll walk through both debugging journeys-the false starts, how we instrumented vLLM to thread request IDs through the forward pass, the search for variables that change failure structure rather than magnitude, and the lesson both share: distributed inference systems fail silently. No stack trace. No sanitizer warning. Just wrong answers with perfect confidence. You'll learn how to build comparison scripts that expose logprob divergence, force memory pressure to surface rare bugs, and shrink a distributed RL training mystery into a reproducible single-script failure. Walk away knowing how to debug vLLM when it lies to you quietly.

## Synthesis
### Synthesized Breakdown
Your model generates gibberish. Once every thousand prompts. High confidence scores. No crashes.

### Speaker And Company Context
- [[asaf-gardin|Asaf Gardin]] — Senior Software Engineer/Inference Engineer at [[ai21|AI21]].
- [[yuval-belfer|Yuval Belfer]] — Sr. Developer Advocate at [[ai21|AI21]].

### Topics Covered
- [[agentic-search]]

### Derived Links And Source Material
- [[youtube-Ywl4LsvHKzU]] — related YouTube source page.
- [[youtube-Ywl4LsvHKzU-slides]] — slide evidence.
- [[youtube-Ywl4LsvHKzU-reconstructed-slides]] — slide evidence.
- [[youtube-Ywl4LsvHKzU-dense-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[asaf-gardin]]
- [[yuval-belfer]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-Ywl4LsvHKzU-dense-slides]] (7 viable slide images).
- Related slide/OCR pages:
- [[youtube-Ywl4LsvHKzU-dense-slides]]
- [[youtube-Ywl4LsvHKzU-reconstructed-slides]]
- [[youtube-Ywl4LsvHKzU-slides]]
- Slide-derived terms: `world`, `fifa`, `local`, `name`, `questions`, `same`, `future`, `wife`, `first`, `mother`, `schema`, `prob`, `answers`, `assuming`, `answer`, `lies`, `certain`, `chunk`

## Media Evidence
- [[youtube-Ywl4LsvHKzU]] - supporting context; not the exact session recording.

- Source video: `youtube-Ywl4LsvHKzU`
- Slide deck: [[youtube-Ywl4LsvHKzU-dense-slides|Dense Slides: RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot]] — 7 visible slide image(s); 7 HTML recreation(s).
![[assets/dense-slides/Ywl4LsvHKzU/slide-001.jpg]]
![[assets/dense-slides/Ywl4LsvHKzU/slide-002.jpg]]
![[assets/dense-slides/Ywl4LsvHKzU/slide-003.jpg]]
- Additional slide evidence: [[youtube-Ywl4LsvHKzU-slides|Slides: RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot]], [[youtube-Ywl4LsvHKzU-reconstructed-slides|Reconstructed Slides: RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot]]
- Slide-derived themes for `youtube-Ywl4LsvHKzU`: world, local, questions, name, answers, assuming, answer, lies.

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-Ywl4LsvHKzU` — 8 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-Ywl4LsvHKzU`: world, local, questions, name, answers, assuming, answer, lies.
- Evidence links for `youtube-Ywl4LsvHKzU` (supporting context only): [[youtube-Ywl4LsvHKzU]], [[youtube-Ywl4LsvHKzU-slides]], [[youtube-Ywl4LsvHKzU-dense-slides]], [[youtube-Ywl4LsvHKzU-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
