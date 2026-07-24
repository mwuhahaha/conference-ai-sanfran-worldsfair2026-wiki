---
title: "We Gave an Agent Production Code Access and Then Tried to Sleep at Night"
category: "talks"
date: "2026-06-29"
time: "11:40am-12:00pm"
track: "Security"
room: "Track 5"
speakers: ["Moritz Johner"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Security"
scheduleRoom: "Track 5"
scheduleLabels: ["Security", "Track 5", "sponsor", "confirmed"]
---
# We Gave an Agent Production Code Access and Then Tried to Sleep at Night

## Conference Context
- Date/time: 2026-06-29 · 11:40am-12:00pm
- Track/room: Security · Track 5
- Speaker(s): Moritz Johner
- Session type/status: sponsor · confirmed

- Track: Security
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
We let an agent touch production code to fix CVEs. That is either automation or a supply chain incident, depending on how honest your architecture is. PatchPilot started simple: find vulnerable dependencies, patch them, open a PR, let CI prove the fix, move on. Then reality showed up. The agent needed repository access, CI logs, credentials, and a Docker socket. Without that, it was useless. With it, every security reviewer in the room had a point. This is the production case study: what we gave the agent, what we refused, what infosec pushed back on, and where they were right. We will cover scoped permissions, constrained PRs, audit trails, approval gates, CI evidence, credential boundaries, and the gap between "it generated a patch" and "we can defend this change." Agentic remediation is not just developer productivity. It is a new participant in your software supply chain.

## Synthesis
### Synthesized Breakdown
Thanks everyone for joining in. Um thanks for the great intro, by the way. Um So, yeah. My talk today is about um so titles we give in Asia production code access and then try to sleep at night.

### Speaker And Company Context
- [[moritz-johner|Moritz Johner]] — Staff Engineer at [[form3|Form3]].

### Topics Covered
- [[agent-security]]
- [[agentic-search]]
- [[ai-sandboxes]]
- [[coding-agents]]

### Derived Links And Source Material
- [[youtube-LqLoYksJ6do-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/LqLoYksJ6do.txt` (4,014 words).
- [[youtube-LqLoYksJ6do]] — related YouTube source page.
- [[youtube-LqLoYksJ6do-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis uses the official schedule and only a dedicated manifest-matched recording transcript for session-level claims and topic extraction. Related official-channel, external, and broad livestream sources remain supporting context and do not stand in for the scheduled session.
## People
- [[moritz-johner]]

## Official YouTube Recording
- [[youtube-LqLoYksJ6do|We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3]] — official AI Engineer YouTube recording published 2026-07-20.
- Evidence status: [[youtube-LqLoYksJ6do-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-LqLoYksJ6do]] - dedicated official event recording.
- [[youtube-LqLoYksJ6do-transcript]] - dedicated official recording transcript.

- [[youtube-LqLoYksJ6do-slides]] — extracted from the related public AI Engineer video.

- Source video: `youtube-LqLoYksJ6do`
- Slide deck: [[youtube-LqLoYksJ6do-slides|Slides: We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3]] — 5 visible slide image(s).
![[assets/slides/LqLoYksJ6do/slide-001.jpg]]
![[assets/slides/LqLoYksJ6do/slide-002.jpg]]
![[assets/slides/LqLoYksJ6do/slide-003.jpg]]
- Slide-derived themes for `youtube-LqLoYksJ6do`: code, gave, production, access, tried, sleep, night, track.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/LqLoYksJ6do.txt` (4,014 words).

## Transcript Markdown
- [[youtube-LqLoYksJ6do-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/LqLoYksJ6do.txt`.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-LqLoYksJ6do` — 4,014 transcript words; 5 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-LqLoYksJ6do`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-LqLoYksJ6do`: case, docker, sandbox, access, repository, order, deterministic, give.
- Slide-derived themes for `youtube-LqLoYksJ6do`: code, gave, production, access, tried, sleep, night, track.
- Evidence links for `youtube-LqLoYksJ6do` (primary event evidence): [[youtube-LqLoYksJ6do]], [[youtube-LqLoYksJ6do-transcript]], [[youtube-LqLoYksJ6do-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
