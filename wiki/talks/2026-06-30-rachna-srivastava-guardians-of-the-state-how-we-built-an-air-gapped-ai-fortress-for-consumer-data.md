---
title: "Guardians of the State: How We Built an Air-Gapped AI Fortress for Consumer Data"
category: "talks"
date: "2026-06-30"
time: "1:55pm-2:15pm"
track: "AI-Native Enterprises"
room: "Leadership 1"
speakers: ["Rachna Srivastava"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "AI-Native Enterprises"
scheduleRoom: "Leadership 1"
scheduleLabels: ["AI-Native Enterprises", "Leadership 1", "session", "confirmed"]
---
# Guardians of the State: How We Built an Air-Gapped AI Fortress for Consumer Data

## Conference Context
- Date/time: 2026-06-30 · 1:55pm-2:15pm
- Track/room: AI-Native Enterprises · Leadership 1
- Speaker(s): Rachna Srivastava
- Session type/status: session · confirmed

- Track: AI-Native Enterprises
- Room: Leadership 1
- Session type: session
- Status: confirmed

## Session Description
Every enterprise slide deck talks about "data privacy," but at the California Department of Financial Protection and Innovation (DFPI), a single leaked Social Security Number or bank account doesn’t just mean a bad PR day—it violates strict state consumer laws and triggers massive regulatory security breaches. When your raw data includes petabytes of unredacted fraud complaints, dark web scam networks, and banking statements, standard commercial public APIs are an absolute non-starter. This talk breaks down the exact enterprise architecture the DFPI uses to leverage frontier-level reasoning on highly sensitive data without crossing legal lines. We will walk through the code and infrastructure of our sovereign data pipeline. Attendees will learn: The Infrastructure: How we host and serve local, open-weights models (like Llama 3 or Mistral) in a strictly air-gapped, secure cloud environment. The Sanitization Stack: How we built a multi-stage PII scrubbing pipeline that uses high-speed deterministic regex combined with a small, specialized local LLM to handle messy, unstructured text. The Validation Loop: How we technically validate that zero sensitive data leaks into model context weights or logging files. No promissory corporate hoopla here—just real, hard-earned architecture patterns and code snippets from a state regulator showing how to ship secure, local AI. Key Takeaways for the Audience: Learn to build a dual-pass PII sanitization pipeline for unstructured financial data. Understand the resource and latency trade-offs of running air-gapped, open-weight models locally vs. commercial APIs. Discover how to set up automated validation frameworks to detect and stop context poisoning or logging leaks.

## Media Evidence
[Cognitive Shield Real Time Real Smart - Rachna Srivastava](https://www.youtube.com/watch?v=5_QWh4LGoxg) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

- Source video: `youtube-5_QWh4LGoxg`
- Slide deck: [[youtube-5_QWh4LGoxg-dense-slides|Dense Slides: Cognitive Shield Real Time Real Smart - Rachna Srivastava]] — 17 visible slide image(s); 17 HTML recreation(s).
![[assets/dense-slides/5_QWh4LGoxg/slide-001.jpg]]
![[assets/dense-slides/5_QWh4LGoxg/slide-002.jpg]]
![[assets/dense-slides/5_QWh4LGoxg/slide-003.jpg]]
- Additional slide evidence: [[youtube-5_QWh4LGoxg-slides|Slides: Cognitive Shield Real Time Real Smart - Rachna Srivastava]], [[youtube-5_QWh4LGoxg-reconstructed-slides|Reconstructed Slides: Cognitive Shield Real Time Real Smart - Rachna Srivastava]]
- Slide-derived themes for `youtube-5_QWh4LGoxg`: fraud, ever, working, against, happens, smartest, tools, built.

## Evidence Graph
This evidence graph is generated from currently linked source material: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Media Signals
- `youtube-5_QWh4LGoxg` — 10 slide-derived text signals
- Slide-derived themes for `youtube-5_QWh4LGoxg`: fraud, ever, working, against, happens, smartest, tools, built.
- Evidence links for `youtube-5_QWh4LGoxg`: [[youtube-5_QWh4LGoxg]], [[youtube-5_QWh4LGoxg-slides]], [[youtube-5_QWh4LGoxg-dense-slides]], [[youtube-5_QWh4LGoxg-reconstructed-slides]]

### Agent Reading Notes
Use these signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## People
- [[rachna-srivastava]]

## Supporting Slides
- [[youtube-5_QWh4LGoxg-slides]] — extracted from the related public AI Engineer video.

## Slide Evidence
- Slide-only cropped deck: [[youtube-5_QWh4LGoxg-dense-slides]] (18 viable slide images).
- Related slide/OCR pages:
- [[youtube-5_QWh4LGoxg-dense-slides]]
- [[youtube-5_QWh4LGoxg-reconstructed-slides]]
- [[youtube-5_QWh4LGoxg-slides]]
- Slide-derived terms: `fraud`, `management`, `detection`, `flow`, `payment`, `graph`, `chat`, `user`, `case`, `examination`, `profile`, `portal`, `lost`, `knowledge`, `level`, `distribution`, `processing`, `search`
