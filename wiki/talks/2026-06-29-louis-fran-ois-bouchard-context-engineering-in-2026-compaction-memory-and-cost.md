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
Every long agent session eventually breaks: the assistant that swore it would "never push to main"

does exactly that forty turns later. The model didn't get dumber — its context did. This workshop is

about engineering the context window so that stops happening, shown with Towards AI's open-source AI

tutor, which answers questions for students of our AI-engineering courses. Context engineering is

deciding what the model sees on every single call — instructions, history, retrieved course content,

memory, and tool outputs — and it's the line between a tutor that holds a coherent session and one

that forgets the student's setup halfway through. We'll move in three stages, mirroring how the

project actually went. The concepts: the two root problems (a finite window, a stateless model), the

full compaction toolkit (truncation, trimming, tool-result clearing, summarization, and offloading

to files — and when each actually helps), memory that survives across sessions, skills loaded on

demand, and production-grade retrieval (chunking, metadata, course scoping, hybrid search,

reranking, and evaluating). We'll cover the tutor's architecture, and the evaluation harness we used

to measure every run on Gemini — tokens, cost, latency, and memory probes instead of vibe-checks. At

real volume, even Gemini Flash got expensive, so we tested whether open and local models could match

the quality for a fraction of the cost and match result quality. Everything is open-source and will

be shared during the workshop.

## Related YouTube Video
[Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](https://www.youtube.com/watch?v=ZRM_TfEZcIo) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## People
- [[louis-fran-ois-bouchard]]
- [[samridhi-vaid]]
- [[omar-solano]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
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
