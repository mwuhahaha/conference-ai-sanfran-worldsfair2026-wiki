---
title: "Weight Folding, CUDA Streams, and the Bug That Made My Model Speak Backwards"
category: "talks"
date: "2026-07-01"
time: "3:45pm-4:05pm"
track: "Inference"
room: "Track 9"
speakers: ["Filip Makraduli"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Inference"
scheduleRoom: "Track 9"
scheduleLabels: ["Inference", "Track 9", "session", "confirmed"]
---
# Weight Folding, CUDA Streams, and the Bug That Made My Model Speak Backwards

## Conference Context
- Date/time: 2026-07-01 · 3:45pm-4:05pm
- Track/room: Inference · Track 9
- Speaker(s): Filip Makraduli
- Session type/status: session · confirmed

- Track: Inference
- Room: Track 9
- Session type: session
- Status: confirmed

## Session Description
A talk about contributing GPU benchmarks to an open-source research paper (FlashNorm). I'll walk through the engineering journey: folding norm weights into projections, writing Triton kernels, accidentally making attention bidirectional (oops), and ultimately proving a 33-35% speedup on the norm+project operation. Practical lessons for anyone trying to optimize transformer inference.

## Media Evidence
[The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked](https://www.youtube.com/watch?v=qdh_x-uRs9g) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

- Source video: `youtube-qdh_x-uRs9g`
- Slide deck: [[youtube-qdh_x-uRs9g-reconstructed-slides|Reconstructed Slides: The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked]] — 10 visible slide image(s); 10 HTML recreation(s).
![[assets/reconstructed-slides/qdh_x-uRs9g/slide-003.jpg]]
![[assets/reconstructed-slides/qdh_x-uRs9g/slide-004.jpg]]
![[assets/reconstructed-slides/qdh_x-uRs9g/slide-005.jpg]]
- Additional slide evidence: [[youtube-qdh_x-uRs9g-slides|Slides: The Small Model Infrastructure Nobody Built (So We Did) — Filip Makraduli, Superlinked]]
- Slide-derived themes for `youtube-qdh_x-uRs9g`: makes, embedding, learning, first, principles, models, production, best.

## Evidence Graph
This evidence graph is generated from currently linked source material: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Media Signals
- `youtube-qdh_x-uRs9g` — 5 slide-derived text signals
- Slide-derived themes for `youtube-qdh_x-uRs9g`: makes, embedding, learning, first, principles, models, production, best.
- Evidence links for `youtube-qdh_x-uRs9g`: [[youtube-qdh_x-uRs9g]], [[youtube-qdh_x-uRs9g-slides]], [[youtube-qdh_x-uRs9g-reconstructed-slides]]

### Agent Reading Notes
Use these signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## People
- [[filip-makraduli]]

## Supporting Slides
- [[youtube-qdh_x-uRs9g-slides]] — extracted from the related public AI Engineer video.
