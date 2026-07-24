---
title: "Computer-Use 2.0: Agents Just Got Multi-Cursor"
category: "talks"
date: "2026-06-30"
time: "2:25pm-2:45pm"
track: "Computer Use"
room: "Track 7"
speakers: ["Francesco Bonacci", "Dillon DuPont"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Computer Use"
scheduleRoom: "Track 7"
scheduleLabels: ["Computer Use", "Track 7", "session", "confirmed"]
---
# Computer-Use 2.0: Agents Just Got Multi-Cursor

## Conference Context
- Date/time: 2026-06-30 · 2:25pm-2:45pm
- Track/room: Computer Use · Track 7
- Speaker(s): Francesco Bonacci, Dillon DuPont
- Session type/status: session · confirmed

- Track: Computer Use
- Room: Track 7
- Session type: session
- Status: confirmed

## Session Description
Computer-use agents still inherit a basic desktop limitation: one machine has one foreground app, one hardware cursor, and one active actor. Once you try to run more than one agent per desktop, they start stealing focus from the user and from each other. We built cua-driver around a different model: multiple agents operating real desktop applications in parallel, each with its own synthetic pointer, while the user's cursor and keyboard stay undisturbed. The key move is to stop treating hardware mouse and keyboard events as the primary automation layer. cua-driver goes one layer lower, into the OS plumbing behind accessibility: UI Automation on Windows, AT-SPI on Linux, and AX on macOS. Those APIs address applications and elements directly, so the OS does not require the target window to be frontmost. A click can land on a background window. A keystroke can reach a hidden one. Multiple agents can act at once because none of them is competing for the singleton hardware mouse. I'll walk through the architecture, the API shape, and the platform-specific traps we hit while making it work across Windows, macOS, and Linux. The live demo is three agents operating on one desktop while the user keeps typing uninterrupted. The goal is to make Computer-Use 2.0 feel concrete: what changes in the stack, what becomes possible, and where the approach still leaks, including Wayland, Chromium DOM surfaces, native canvas apps, and fallback input paths.

## Synthesis
### Synthesized Breakdown
Thank you for taking the time for coming over here. Um I'm Franchesco. I'm the CEO of the company. Uh alongside me, a couple of other folks.

### Speaker And Company Context
- [[francesco-bonacci|Francesco Bonacci]] — Co-founder & CEO at [[cua|Cua]].
- [[dillon-dupont|Dillon DuPont]] — CTO at [[cua|Cua]].

### Topics Covered
- [[agent-security]]
- [[agentic-search]]
- [[ai-sandboxes]]
- [[coding-agents]]

### Derived Links And Source Material
- [[youtube-ZSQb5fzRFPw-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/ZSQb5fzRFPw.txt` (2,617 words).
- [[youtube-ZSQb5fzRFPw]] — related YouTube source page.
- [[youtube-ZSQb5fzRFPw-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis uses the official schedule and only a dedicated manifest-matched recording transcript for session-level claims and topic extraction. Related official-channel, external, and broad livestream sources remain supporting context and do not stand in for the scheduled session.
## People
- [[francesco-bonacci]]
- [[dillon-dupont]]

## Official YouTube Recording
- [[youtube-ZSQb5fzRFPw|Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua]] — official AI Engineer YouTube recording published 2026-07-15.
- Evidence status: [[youtube-ZSQb5fzRFPw-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-ZSQb5fzRFPw]] - dedicated official event recording.
- [[youtube-ZSQb5fzRFPw-transcript]] - dedicated official recording transcript.

- Source video: `youtube-ZSQb5fzRFPw`
- Slide deck: [[youtube-ZSQb5fzRFPw-slides|Slides: ZSQb5fzRFPw]] — 17 visible slide image(s).
![[assets/slides/ZSQb5fzRFPw/slide-001.jpg]]
![[assets/slides/ZSQb5fzRFPw/slide-002.jpg]]
![[assets/slides/ZSQb5fzRFPw/slide-003.jpg]]
- Slide-derived themes for `youtube-ZSQb5fzRFPw`: track, july, fair, computer, operator, loop, wired, model.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/ZSQb5fzRFPw.txt` (2,617 words).

## Transcript Markdown
- [[youtube-ZSQb5fzRFPw-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/ZSQb5fzRFPw.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-ZSQb5fzRFPw` — 2,617 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-ZSQb5fzRFPw`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-ZSQb5fzRFPw`: computer, take, over, driver, background, task, might, sandbox.
- Slide-derived themes for `youtube-ZSQb5fzRFPw`: track, july, fair, computer, operator, loop, wired, model.
- Evidence links for `youtube-ZSQb5fzRFPw` (primary event evidence): [[youtube-ZSQb5fzRFPw]], [[youtube-ZSQb5fzRFPw-transcript]], [[youtube-ZSQb5fzRFPw-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
