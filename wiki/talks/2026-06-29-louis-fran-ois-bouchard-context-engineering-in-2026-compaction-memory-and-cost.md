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

## Official Schedule Context
- Date/time: 2026-06-29 · 2:20pm-4:20pm
- Track/room: track TBD · Track 6
- Speaker(s): Louis-François Bouchard, Samridhi Vaid, Omar Solano
- Session type/status: sponsor · confirmed

## Schedule Labels
- Track: track TBD
- Room: Track 6
- Session type: sponsor
- Status: confirmed

## Official Description
Every long agent session eventually breaks: the assistant that swore it would "never push to main" does exactly that forty turns later. The model didn't get dumber — its context did. This workshop is about engineering the context window so that stops happening, shown with Towards AI's open-source AI tutor, which answers questions for students of our AI-engineering courses. Context engineering is deciding what the model sees on every single call — instructions, history, retrieved course content, memory, and tool outputs — and it's the line between a tutor that holds a coherent session and one that forgets the student's setup halfway through. We'll move in three stages, mirroring how the project actually went. The concepts: the two root problems (a finite window, a stateless model), the full compaction toolkit (truncation, trimming, tool-result clearing, summarization, and offloading to files — and when each actually helps), memory that survives across sessions, skills loaded on demand, and production-grade retrieval (chunking, metadata, course scoping, hybrid search, reranking, and evaluating). We'll cover the tutor's architecture, and the evaluation harness we used to measure every run on Gemini — tokens, cost, latency, and memory probes instead of vibe-checks. At real volume, even Gemini Flash got expensive, so we tested whether open and local models could match the quality for a fraction of the cost and match result quality. Everything is open-source and will be shared during the workshop.

## Related YouTube Video
[Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](https://www.youtube.com/watch?v=ZRM_TfEZcIo) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## People
- [[louis-fran-ois-bouchard]]
- [[samridhi-vaid]]
- [[omar-solano]]

## Supporting Slides
- [[youtube-ZRM_TfEZcIo-slides]] — extracted from the related public AI Engineer video.
## Slide Evidence
- Slide-only cropped deck: [[youtube-ZRM_TfEZcIo-dense-slides]] (12 viable slide images).
- Related slide/OCR pages:
- [[youtube-ZRM_TfEZcIo-dense-slides]]
- [[youtube-ZRM_TfEZcIo-reconstructed-slides]]
- [[youtube-ZRM_TfEZcIo-slides]]
- Slide-derived terms: `notes`, `obsidian`, `research`, `towards`, `index`, `every`, `database`, `files`, `engineer`, `handbook`, `content`, `courses`, `videos`, `starts`, `zero`, `codex`, `repos`, `course`
## Livestream Segment
- [Watch in livestream at 02:11:16](https://www.youtube.com/watch?v=I2cbIws9j10&t=7876s) — WF26: Harness Engineering & Startup Battlefield (Day 3).
- Match basis: speaker and title; timed captions matched Louis-François Bouchard, engineering.
- Confidence: high automated match; prefer a dedicated cut-video recording when one exists.

## Transcript Markdown
- [[youtube-I2cbIws9j10-transcript]] — full cached transcript markdown for the related YouTube source.

## Source-Derived Enrichment
This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Source Signals
- `youtube-I2cbIws9j10` — 91,792 transcript words; 4 slide-derived text signals
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: choosing, model, quality, dominates, agentic, capabilities, customization, support.
- Evidence links for `youtube-I2cbIws9j10`: [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
- `youtube-ZRM_TfEZcIo` — 9 slide-derived text signals
- Slide-derived themes for `youtube-ZRM_TfEZcIo`: obsidian, plus, notion, google, drive, growing, files, month.
- Evidence links for `youtube-ZRM_TfEZcIo`: [[youtube-ZRM_TfEZcIo]], [[youtube-ZRM_TfEZcIo-slides]], [[youtube-ZRM_TfEZcIo-dense-slides]], [[youtube-ZRM_TfEZcIo-reconstructed-slides]]

### Article Use
Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.
## Slides
- Source video: `youtube-I2cbIws9j10`
- Slide deck: [[youtube-I2cbIws9j10-dense-slides|Dense Slides: WF26: Harness Engineering & Startup Battlefield ft. Garry Tan, Mike Krieger, @t3dotgg , DSPy]] — 12 visible slide image(s).
![[assets/dense-slides/I2cbIws9j10/slide-001.jpg]]
![[assets/dense-slides/I2cbIws9j10/slide-002.jpg]]
![[assets/dense-slides/I2cbIws9j10/slide-003.jpg]]
- Additional slide evidence: [[youtube-I2cbIws9j10-slides|Slides: WF26: Harness Engineering & Startup Battlefield ft. Garry Tan, Mike Krieger, @t3dotgg , DSPy]]
- Slide-derived themes for `youtube-I2cbIws9j10`: choosing, model, quality, dominates, agentic, capabilities, customization, support.
- Source video: `youtube-ZRM_TfEZcIo`
- Slide deck: [[youtube-ZRM_TfEZcIo-dense-slides|Dense Slides: Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI]] — 11 visible slide image(s); 11 HTML recreation(s).
![[assets/dense-slides/ZRM_TfEZcIo/slide-001.jpg]]
![[assets/dense-slides/ZRM_TfEZcIo/slide-003.jpg]]
![[assets/dense-slides/ZRM_TfEZcIo/slide-004.jpg]]
- Additional slide evidence: [[youtube-ZRM_TfEZcIo-slides|Slides: Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI]], [[youtube-ZRM_TfEZcIo-reconstructed-slides|Reconstructed Slides: Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI]]
- Slide-derived themes for `youtube-ZRM_TfEZcIo`: obsidian, plus, notion, google, drive, growing, files, month.
## Attendance Visibility
No high-confidence attendance icon signal is shown for this talk. The sampled video evidence was either low confidence, source-proxy-only, or did not expose a clear audience view.
