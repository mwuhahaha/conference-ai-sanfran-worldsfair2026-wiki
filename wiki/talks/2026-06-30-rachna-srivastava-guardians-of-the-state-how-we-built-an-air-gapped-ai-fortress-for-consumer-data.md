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

## Synthesis
### Synthesized Breakdown
Every enterprise slide deck talks about "data privacy," but at the California Department of Financial Protection and Innovation (DFPI), a single leaked Social Security Number or bank account doesn’t just mean a bad PR day—it violates strict state consumer laws and triggers massive regulatory security breaches. When your raw data includes petabytes of unredacted fraud complaints, dark web scam networks, and banking statements, standard commercial public APIs are an absolute non-starter. This talk breaks down the exact enterprise architecture the DFPI uses to leverage frontier-level reasoning on highly sensitive data without crossing legal lines. We will walk through the code and infrastructure of our sovereign data pipeline.

### Speaker And Company Context
- [[rachna-srivastava|Rachna Srivastava]] — Enterprise Architect at [[dfpi|DFPI]].

### Topics Covered
- [[agentic-search]]
- [[coding-agents]]

### Derived Links And Source Material
- [[youtube-5_QWh4LGoxg]] — related YouTube source page.
- [[youtube-5_QWh4LGoxg-slides]] — slide evidence.
- [[youtube-5_QWh4LGoxg-reconstructed-slides]] — slide evidence.
- [[youtube-5_QWh4LGoxg-dense-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[rachna-srivastava]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-5_QWh4LGoxg-dense-slides]] (18 viable slide images).
- Related slide/OCR pages:
- [[youtube-5_QWh4LGoxg-dense-slides]]
- [[youtube-5_QWh4LGoxg-reconstructed-slides]]
- [[youtube-5_QWh4LGoxg-slides]]
- Slide-derived terms: `fraud`, `management`, `detection`, `flow`, `payment`, `graph`, `chat`, `user`, `case`, `examination`, `profile`, `portal`, `lost`, `knowledge`, `level`, `distribution`, `processing`, `search`

## Media Evidence
- [[youtube-5_QWh4LGoxg]] - supporting context; not the exact session recording.

- Source video: `youtube-5_QWh4LGoxg`
- Slide deck: [[youtube-5_QWh4LGoxg-dense-slides|Dense Slides: Cognitive Shield Real Time Real Smart - Rachna Srivastava]] — slide evidence page.
- Additional slide evidence: [[youtube-5_QWh4LGoxg-slides|Slides: Cognitive Shield Real Time Real Smart - Rachna Srivastava]], [[youtube-5_QWh4LGoxg-reconstructed-slides|Reconstructed Slides: Cognitive Shield Real Time Real Smart - Rachna Srivastava]]
- Slide-derived themes for `youtube-5_QWh4LGoxg`: layer, graph, phishing, emails, working, legitimate, ones, mars.

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-5_QWh4LGoxg` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-5_QWh4LGoxg`: layer, graph, phishing, emails, working, legitimate, ones, mars.
- Evidence links for `youtube-5_QWh4LGoxg` (supporting context only): [[youtube-5_QWh4LGoxg]], [[youtube-5_QWh4LGoxg-slides]], [[youtube-5_QWh4LGoxg-dense-slides]], [[youtube-5_QWh4LGoxg-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
