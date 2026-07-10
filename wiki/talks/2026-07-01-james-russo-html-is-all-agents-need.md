---
title: "HTML Is All Agents Need"
category: "talks"
date: "2026-07-01"
time: "11:10am-11:30am"
track: "Generative Media"
room: "Track 1"
speakers: ["James Russo"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Generative Media"
scheduleRoom: "Track 1"
scheduleLabels: ["Generative Media", "Track 1", "session", "confirmed"]
---
# HTML Is All Agents Need

## Conference Context
- Date/time: 2026-07-01 · 11:10am-11:30am
- Track/room: Generative Media · Track 1
- Speaker(s): James Russo
- Session type/status: session · confirmed

- Track: Generative Media
- Room: Track 1
- Session type: session
- Status: confirmed

## Session Description
LLMs are great at writing code. So the question we kept asking was: can they write code that produces a video? We thought it would be easy. The reality was a year of trying. We started with massive prompts to get very mediocre output. We made it more agentic to iterate and improve its output. This worked okay but wasn't production-ready. Eventually we tried Remotion. It got us deterministic video, but the React framework kept boxing the agent in. The more guardrails we added, the safer and more boring the outputs got. When we utilized plain HTML, CSS, and JavaScript, the creativity came back to the output. So we set out to build a video rendering framework on top of HTML. But it needed to work with Gemini Flash. Why? Because one tell that a framework is fighting an agent is needing the biggest model just to get usable output. So from there we shaped the framework around what small models could reliably author. That left one real engineering question: can we keep the freedom of HTML and still render a deterministic MP4? Browsers don't want to do that. Image decoders, font loaders, and animation clocks all run async on their own schedule. Great for performance. Terrible for "render the same pixels every time." Throughout, we iterated constantly with agentic loops and self-improving evals to test out the framework, find issues in our renderer, and shape a set of skills that gave the agents Taste instead of guardrails. This talk is what it took to get there.

## Media Evidence
No related AI Engineer channel video found yet.

## Evidence Graph
This evidence graph is generated from currently linked source material: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Media Signals
No linked video, transcript, or slide source has been attached yet.

### Agent Reading Notes
Use these signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[james-russo]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Synthesis
### Synthesized Breakdown
# HTML Is All Agents Need ## Conference Context - Date/time: 2026-07-01 · 11:10am-11:30am - Track/room: Generative Media · Track 1 - Speaker(s): James Russo - Session type/status: session · confirmed - Track: Generative Media - Room: Track 1 - Session type: session - Status: confirmed ## Session Description LLMs are great at writing code. So the question we kept asking was: can they write code that produces a video? We thought it would be easy. The reality was a year of trying.

### Speaker And Company Context
- [[james-russo|James Russo]] — Software Engineer at [[heygen|HeyGen]].

### Topics Covered
- [[agent-security]]
- [[agentic-web]]
- [[ai-sandboxes]]
- [[coding-agents]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
