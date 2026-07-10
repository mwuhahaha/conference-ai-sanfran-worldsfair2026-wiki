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

## Official Schedule Context
- Date/time: 2026-07-01 · 3:20pm-3:40pm
- Track/room: Inference · Track 9
- Speaker(s): Asaf Gardin, Yuval Belfer
- Session type/status: session · confirmed

## Schedule Labels
- Track: Inference
- Room: Track 9
- Session type: session
- Status: confirmed

## Official Description
Your model generates gibberish. Once every thousand prompts. High confidence scores. No crashes. No warnings. We hit this twice while building Jamba models. First: A request gets misclassified during scheduling, loads stale state from a previous prompt cache slot, and confidently generates nonsense. Second: Logprob spikes during RL training that looked like training instability-until we noticed they tracked with rollout count, then with cache size. In this talk, we'll walk through both debugging journeys-the false starts, how we instrumented vLLM to thread request IDs through the forward pass, the search for variables that change failure structure rather than magnitude, and the lesson both share: distributed inference systems fail silently. No stack trace. No sanitizer warning. Just wrong answers with perfect confidence. You'll learn how to build comparison scripts that expose logprob divergence, force memory pressure to surface rare bugs, and shrink a distributed RL training mystery into a reproducible single-script failure. Walk away knowing how to debug vLLM when it lies to you quietly.

## Related YouTube Video
[RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot](https://www.youtube.com/watch?v=Ywl4LsvHKzU) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## People
- [[asaf-gardin]]
- [[yuval-belfer]]

## Supporting Slides
- [[youtube-Ywl4LsvHKzU-slides]] — extracted from the related public AI Engineer video.
## Slide Evidence
- Slide-only cropped deck: [[youtube-Ywl4LsvHKzU-dense-slides]] (7 viable slide images).
- Related slide/OCR pages:
- [[youtube-Ywl4LsvHKzU-dense-slides]]
- [[youtube-Ywl4LsvHKzU-reconstructed-slides]]
- [[youtube-Ywl4LsvHKzU-slides]]
- Slide-derived terms: `world`, `fifa`, `local`, `name`, `questions`, `same`, `future`, `wife`, `first`, `mother`, `schema`, `prob`, `answers`, `assuming`, `answer`, `lies`, `certain`, `chunk`

## Source-Derived Enrichment
This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Source Signals
- `youtube-Ywl4LsvHKzU` — 8 slide-derived text signals
- Slide-derived themes for `youtube-Ywl4LsvHKzU`: world, local, questions, name, answers, assuming, answer, lies.
- Evidence links for `youtube-Ywl4LsvHKzU`: [[youtube-Ywl4LsvHKzU]], [[youtube-Ywl4LsvHKzU-slides]], [[youtube-Ywl4LsvHKzU-dense-slides]], [[youtube-Ywl4LsvHKzU-reconstructed-slides]]

### Article Use
Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.
## Slides
- Source video: `youtube-Ywl4LsvHKzU`
- Slide deck: [[youtube-Ywl4LsvHKzU-dense-slides|Dense Slides: RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot]] — 7 visible slide image(s); 7 HTML recreation(s).
![[assets/dense-slides/Ywl4LsvHKzU/slide-001.jpg]]
![[assets/dense-slides/Ywl4LsvHKzU/slide-002.jpg]]
![[assets/dense-slides/Ywl4LsvHKzU/slide-003.jpg]]
- Additional slide evidence: [[youtube-Ywl4LsvHKzU-slides|Slides: RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot]], [[youtube-Ywl4LsvHKzU-reconstructed-slides|Reconstructed Slides: RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot]]
- Slide-derived themes for `youtube-Ywl4LsvHKzU`: world, local, questions, name, answers, assuming, answer, lies.
