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

## Conference Context
- Date/time: 2026-07-01 · 12:05pm-12:25pm
- Track/room: Harness Engineering · Main Stage
- Speaker(s): Mike Chambers
- Session type/status: session · confirmed

- Track: Harness Engineering
- Room: Main Stage
- Session type: session
- Status: confirmed

## Session Description
Every agent is a while loop. The model takes strings in and produces strings out. We've all written it, debugged it, shipped it. And yet every team building agents is still re-inventing the same session management, truncation logic, tool wiring, and memory plumbing from scratch. The hard part is the harness: session isolation, context management, memory persistence, sandboxed execution, observability. The machinery that makes a model dependable in production. Most of the failures we see in deployed agents (context rot, premature completion, tool bloat) trace back to harness problems, not model problems. This talk covers what a harness actually does, why "harness engineering" suddenly showed up in engineering posts from everyone, and what changes when you stop building harnesses by hand. In live demos, we'll build the same agent three ways: hand-rolled Python, framework-generated, and fully managed through a single API call. Each level shifts the failure modes from infrastructure plumbing to engineering judgment, where the real questions are what context to preserve, when to verify, and how to keep an agent from finishing half the job and calling it done. The harness handles the machinery. You still have to engineer the behavior.

## Synthesis
### Synthesized Breakdown
Every agent is a while loop. The model takes strings in and produces strings out. We've all written it, debugged it, shipped it. And yet every team building agents is still re-inventing the same session management, truncation logic, tool wiring, and memory plumbing from scratch.

### Speaker And Company Context
- [[mike-chambers|Mike Chambers]] — Senior Developer Advocate for Generative AI at [[amazon-web-services-aws|Amazon Web Services (AWS)]].

### Topics Covered
- [[ai-sandboxes]]

### Derived Links And Source Material
- [[youtube-HT4l0DeP69I]] — related YouTube source page.
- [[youtube-HT4l0DeP69I-slides]] — slide evidence.
- [[youtube-HT4l0DeP69I-reconstructed-slides]] — slide evidence.
- [[youtube-HT4l0DeP69I-dense-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## People
- [[mike-chambers]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-HT4l0DeP69I-dense-slides]] (2 viable slide images).
- Related slide/OCR pages:
- [[youtube-HT4l0DeP69I-dense-slides]]
- [[youtube-HT4l0DeP69I-reconstructed-slides]]
- [[youtube-HT4l0DeP69I-slides]]
- Slide-derived terms: `models`, `amazon`, `microsoft`, `bedrock`, `model`, `prompt`, `mike`, `system`, `master`, `roll`, `claude`, `chat`, `select`, `nova`, `learn`, `world`, `ate-wf-2025-demos`, `grand`

## Livestream Segment
- [Watch in livestream at 03:14:28](https://www.youtube.com/watch?v=I2cbIws9j10&t=11668s) — WF26: Harness Engineering & Startup Battlefield (Day 3).
- Evidence: transcript-aligned segment validated against the official schedule and timed captions.
- Confidence: high automated match; prefer a dedicated cut-video recording when one exists.

## Media Evidence
- [[youtube-HT4l0DeP69I]] - supporting context; not the exact session recording.

- Source video: `youtube-HT4l0DeP69I`
- Slide deck: [[youtube-HT4l0DeP69I-dense-slides|Dense Slides: Ship it! Building Production Ready Agents — Mike Chambers, AWS]] — slide evidence page.
- Additional slide evidence: [[youtube-HT4l0DeP69I-slides|Slides: Ship it! Building Production Ready Agents — Mike Chambers, AWS]], [[youtube-HT4l0DeP69I-reconstructed-slides|Reconstructed Slides: Ship it! Building Production Ready Agents — Mike Chambers, AWS]]
- Slide-derived themes for `youtube-HT4l0DeP69I`: mike, chambers, advocate, engineering, generative, real, world, applications.

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## Attendance Visibility
No high-confidence attendance icon signal is shown for this talk. The sampled video evidence was either low confidence, source-proxy-only, or did not expose a clear audience view.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-HT4l0DeP69I` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-HT4l0DeP69I`: mike, chambers, advocate, engineering, generative, real, world, applications.
- Evidence links for `youtube-HT4l0DeP69I` (supporting context only): [[youtube-HT4l0DeP69I]], [[youtube-HT4l0DeP69I-slides]], [[youtube-HT4l0DeP69I-dense-slides]], [[youtube-HT4l0DeP69I-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
