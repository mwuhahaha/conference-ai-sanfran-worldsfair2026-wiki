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

## Synthesis
### Synthesized Breakdown
Since we're talking about generative media, I thought starting with a video might be good. That video was made completely by an agent in a single shot, all utilizing HTML. My name is James Russo. I am the co-creator and tech lead of hyperframes at HeyGen.

### Speaker And Company Context
- [[james-russo|James Russo]] — Software Engineer at [[heygen|HeyGen]].

### Topics Covered
- [[agent-security]]
- [[agentic-search]]
- [[agentic-web]]
- [[coding-agents]]

### Derived Links And Source Material
- [[youtube-Cz4v1WHVyZc-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/Cz4v1WHVyZc.txt` (2,535 words).
- [[youtube-Cz4v1WHVyZc]] — related YouTube source page.
- [[youtube-Cz4v1WHVyZc-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis uses the official schedule and only a dedicated manifest-matched recording transcript for session-level claims and topic extraction. Related official-channel, external, and broad livestream sources remain supporting context and do not stand in for the scheduled session.
## People
- [[james-russo]]

## Official YouTube Recording
- [[youtube-Cz4v1WHVyZc|HTML Is All Agents Need — James Russo, HeyGen]] — official AI Engineer YouTube recording published 2026-07-11.
- Evidence status: [[youtube-Cz4v1WHVyZc-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-Cz4v1WHVyZc]] - dedicated official event recording.
- [[youtube-Cz4v1WHVyZc-transcript]] - dedicated official recording transcript.

- Source video: `youtube-Cz4v1WHVyZc`
- Slide deck: [[youtube-Cz4v1WHVyZc-slides|Slides: HTML Is All Agents Need — James Russo, HeyGen]] — 32 visible slide image(s).
![[assets/slides/Cz4v1WHVyZc/slide-001.jpg]]
![[assets/slides/Cz4v1WHVyZc/slide-002.jpg]]
![[assets/slides/Cz4v1WHVyZc/slide-003.jpg]]
- Slide-derived themes for `youtube-Cz4v1WHVyZc`: track, july, most, engineering, future, html, javascript, native.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/Cz4v1WHVyZc.txt` (2,535 words).

## Transcript Markdown
- [[youtube-Cz4v1WHVyZc-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/Cz4v1WHVyZc.txt`.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-Cz4v1WHVyZc` — 2,535 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Cz4v1WHVyZc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Cz4v1WHVyZc`: html, great, hyperframes, output, create, frame, coding, javascript.
- Slide-derived themes for `youtube-Cz4v1WHVyZc`: track, july, most, engineering, future, html, javascript, native.
- Evidence links for `youtube-Cz4v1WHVyZc` (primary event evidence): [[youtube-Cz4v1WHVyZc]], [[youtube-Cz4v1WHVyZc-transcript]], [[youtube-Cz4v1WHVyZc-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
