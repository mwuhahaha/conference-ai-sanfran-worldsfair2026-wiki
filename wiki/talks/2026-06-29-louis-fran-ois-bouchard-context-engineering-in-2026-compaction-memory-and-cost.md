---
title: "Context Engineering in 2026: Compaction, Memory & Cost"
category: "talks"
date: "2026-06-29"
time: "2:20pm-4:20pm"
track: "Track 6"
room: "Track 6"
speakers: ["Louis-François Bouchard", "Samridhi Vaid", "Omar Solano"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: ""
scheduleRoom: "Track 6"
scheduleLabels: ["Track 6", "sponsor", "confirmed"]
---
# Context Engineering in 2026: Compaction, Memory & Cost

## Conference Context
- Date/time: 2026-06-29 · 2:20pm-4:20pm
- Track/room: track TBD · Track 6
- Speaker(s): Louis-François Bouchard, Samridhi Vaid, Omar Solano
- Session type/status: sponsor · confirmed

- Track: track TBD
- Room: Track 6
- Session type: sponsor
- Status: confirmed

## Session Description
Every long agent session eventually breaks: the assistant that swore it would "never push to main" does exactly that forty turns later. The model didn't get dumber — its context did. This workshop is about engineering the context window so that stops happening, shown with Towards AI's open-source AI tutor, which answers questions for students of our AI-engineering courses. Context engineering is deciding what the model sees on every single call — instructions, history, retrieved course content, memory, and tool outputs — and it's the line between a tutor that holds a coherent session and one that forgets the student's setup halfway through. We'll move in three stages, mirroring how the project actually went. The concepts: the two root problems (a finite window, a stateless model), the full compaction toolkit (truncation, trimming, tool-result clearing, summarization, and offloading to files — and when each actually helps), memory that survives across sessions, skills loaded on demand, and production-grade retrieval (chunking, metadata, course scoping, hybrid search, reranking, and evaluating). We'll cover the tutor's architecture, and the evaluation harness we used to measure every run on Gemini — tokens, cost, latency, and memory probes instead of vibe-checks. At real volume, even Gemini Flash got expensive, so we tested whether open and local models could match the quality for a fraction of the cost and match result quality. Everything is open-source and will be shared during the workshop.

## Synthesis
### Synthesized Breakdown
Every long agent session eventually breaks: the assistant that swore it would "never push to main" does exactly that forty turns later. The model didn't get dumber — its context did. This workshop is about engineering the context window so that stops happening, shown with Towards AI's open-source AI tutor, which answers questions for students of our AI-engineering courses. Context engineering is deciding what the model sees on every single call — instructions, history, retrieved course content, memory, and tool outputs — and it's the line between a tutor that holds a coherent session and one that forgets the student's setup halfway through.

### Speaker And Company Context
- [[louis-fran-ois-bouchard|Louis-François Bouchard]] — CTO & Co-Founder at [[towards-ai|Towards AI]].
- [[samridhi-vaid|Samridhi Vaid]] — Senior Machine Learning Engineer at [[towards-ai|Towards AI]].
- [[omar-solano|Omar Solano]] — AI Engineer at [[towards-ai|Towards AI]].

### Topics Covered
- [[agent-memory]]
- [[agentic-search]]

### Derived Links And Source Material
- [[youtube-ZRM_TfEZcIo]] — related YouTube source page.
- [[youtube-ZRM_TfEZcIo-slides]] — slide evidence.
- [[youtube-ZRM_TfEZcIo-reconstructed-slides]] — slide evidence.
- [[youtube-ZRM_TfEZcIo-dense-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[louis-fran-ois-bouchard]]
- [[samridhi-vaid]]
- [[omar-solano]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-ZRM_TfEZcIo-dense-slides]] (12 viable slide images).
- Related slide/OCR pages:
- [[youtube-ZRM_TfEZcIo-dense-slides]]
- [[youtube-ZRM_TfEZcIo-reconstructed-slides]]
- [[youtube-ZRM_TfEZcIo-slides]]
- Slide-derived terms: `notes`, `obsidian`, `research`, `towards`, `index`, `every`, `database`, `files`, `engineer`, `handbook`, `content`, `courses`, `videos`, `starts`, `zero`, `codex`, `repos`, `course`

## Media Evidence
- [[youtube-ZRM_TfEZcIo]] - supporting context; not the exact session recording.

- Source video: `youtube-ZRM_TfEZcIo`
- Slide deck: [[youtube-ZRM_TfEZcIo-dense-slides|Dense Slides: Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI]] — 10 visible slide image(s); 10 HTML recreation(s).
![[assets/dense-slides/ZRM_TfEZcIo/slide-001.jpg]]
![[assets/dense-slides/ZRM_TfEZcIo/slide-004.jpg]]
![[assets/dense-slides/ZRM_TfEZcIo/slide-005.jpg]]
- Additional slide evidence: [[youtube-ZRM_TfEZcIo-slides|Slides: Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI]], [[youtube-ZRM_TfEZcIo-reconstructed-slides|Reconstructed Slides: Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI]]
- Slide-derived themes for `youtube-ZRM_TfEZcIo`: obsidian, google, plus, notion, drive, growing, files, month.

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## Attendance Visibility
No high-confidence attendance icon signal is shown for this talk. The sampled video evidence was either low confidence, source-proxy-only, or did not expose a clear audience view.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-ZRM_TfEZcIo` — 9 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-ZRM_TfEZcIo`: obsidian, google, plus, notion, drive, growing, files, month.
- Evidence links for `youtube-ZRM_TfEZcIo` (supporting context only): [[youtube-ZRM_TfEZcIo]], [[youtube-ZRM_TfEZcIo-slides]], [[youtube-ZRM_TfEZcIo-dense-slides]], [[youtube-ZRM_TfEZcIo-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
