---
title: "Harness Engineering: Building the Production Cage for Powerful Domain Agents"
category: "talks"
date: "2026-07-01"
time: "12:05pm-12:25pm"
track: "Harness Engineering"
room: "Main Stage"
speakers: ["Mike Chambers"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Harness Engineering"
scheduleRoom: "Main Stage"
scheduleLabels: ["Harness Engineering", "Main Stage", "session", "confirmed"]
---
# Harness Engineering: Building the Production Cage for Powerful Domain Agents

## Official Schedule Context
- Date/time: 2026-07-01 · 12:05pm-12:25pm
- Track/room: Harness Engineering · Main Stage
- Speaker(s): Mike Chambers
- Session type/status: session · confirmed

## Schedule Labels
- Track: Harness Engineering
- Room: Main Stage
- Session type: session
- Status: confirmed

## Official Description
Every agent is a while loop. The model takes strings in and produces strings out. We've all written

it, debugged it, shipped it. And yet every team building agents is still re-inventing the same

session management, truncation logic, tool wiring, and memory plumbing from scratch. The hard part

is the harness: session isolation, context management, memory persistence, sandboxed execution,

observability. The machinery that makes a model dependable in production. Most of the failures we

see in deployed agents (context rot, premature completion, tool bloat) trace back to harness

problems, not model problems. This talk covers what a harness actually does, why "harness

engineering" suddenly showed up in engineering posts from everyone, and what changes when you stop

building harnesses by hand. In live demos, we'll build the same agent three ways: hand-rolled

Python, framework-generated, and fully managed through a single API call. Each level shifts the

failure modes from infrastructure plumbing to engineering judgment, where the real questions are

what context to preserve, when to verify, and how to keep an agent from finishing half the job and

calling it done. The harness handles the machinery. You still have to engineer the behavior.

## Related YouTube Video
[Ship it! Building Production Ready Agents — Mike Chambers, AWS](https://www.youtube.com/watch?v=HT4l0DeP69I) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## People
- [[mike-chambers]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
## Supporting Slides
- [[youtube-HT4l0DeP69I-slides]] — extracted from the related public AI Engineer video.
## Slide Evidence
- Slide-only cropped deck: [[youtube-HT4l0DeP69I-dense-slides]] (2 viable slide images).
- Related slide/OCR pages:
- [[youtube-HT4l0DeP69I-dense-slides]]
- [[youtube-HT4l0DeP69I-reconstructed-slides]]
- [[youtube-HT4l0DeP69I-slides]]
- Slide-derived terms: `models`, `amazon`, `microsoft`, `bedrock`, `model`, `prompt`, `mike`, `system`, `master`, `roll`, `claude`, `chat`, `select`, `nova`, `learn`, `world`, `ate-wf-2025-demos`, `grand`
## Livestream Segment
- [Watch in livestream at 03:14:28](https://www.youtube.com/watch?v=I2cbIws9j10&t=11668s) — WF26: Harness Engineering & Startup Battlefield (Day 3).
- Match basis: speaker and title; timed captions matched Mike Chambers, engineering, harness.
- Confidence: high automated match; prefer a dedicated cut-video recording when one exists.
