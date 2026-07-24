---
title: "Why Agentic Systems Need Ontologies"
category: "talks"
date: "2026-07-01"
time: "1:55pm-2:15pm"
track: "Graphs"
room: "Track 5"
speakers: ["Frank Coyle"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Graphs"
scheduleRoom: "Track 5"
scheduleLabels: ["Graphs", "Track 5", "sponsor", "confirmed"]
---
# Why Agentic Systems Need Ontologies

## Conference Context
- Date/time: 2026-07-01 · 1:55pm-2:15pm
- Track/room: Graphs · Track 5
- Speaker(s): Frank Coyle
- Session type/status: sponsor · confirmed

- Track: Graphs
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
Agentic systems fail in predictable ways: context degradation, brittle tool descriptions, fragile multi-agent handoffs, stop-reason confusion, and the ever-present temptation to fix reliability problems with more natural-language instructions. These anti-patterns aren't bugs to be patched turn by turn — they're symptoms of a missing architectural layer. LLMs reason probabilistically over domains they only partially understand, and no amount of prompt engineering fully closes that gap. This talk argues that the missing layer is an explicit ontology: a formal, shared map of the domain's concepts, relationships, and constraints. The pattern is not new — ontologies have driven commercial success in defense and intelligence systems for over a decade, where probabilistic models must operate over high-stakes enterprise data without drifting into nonsense. Graph databases like Neo4j and Amazon Neptune have made the underlying primitives widely accessible. We'll show how lightweight ontology constructs can surround an agentic system with enforceable logical constraints: typed entities and relationships that tools must respect, cardinality and domain restrictions that catch malformed tool calls before they execute, and a shared vocabulary that keeps coordinators and subagents talking about the same things. The session walks through several agentic applications — a multi-agent research workflow, a tool-heavy customer support agent, a coordinator-subagent delegation pattern — and shows in each case how an ontology layer addresses the kinds of anti-patterns catalogued in Anthropic's Claude Certified Architect exam. The result is a hybrid neurosymbolic architecture: probabilistic reasoning inside, logical guardrails outside. Who should attend: engineers building production agentic systems, architects evaluating reliability strategies beyond prompt engineering, and technical leads who suspect their agents need more structure than another system prompt can provide.

## Synthesis
### Synthesized Breakdown
Um, okay, we're going to launch here. So, my name is Frank Coyle. Um, I'm I'm an educator and teaching at Berkeley now. I've been doing this computer science stuff for oh, 30, 35 years.

### Speaker And Company Context
- [[frank-coyle|Frank Coyle]] — Lecturer, UCALBerkeley / Founder AI/Edge at [[ucal-berkeley|UCAL Berkeley]].

### Topics Covered
- [[agent-security]]
- [[agentic-search]]
- [[coding-agents]]

### Derived Links And Source Material
- [[youtube-Sir59K8ZDPU-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/Sir59K8ZDPU.txt` (3,096 words).
- [[youtube-Sir59K8ZDPU]] — related YouTube source page.
- [[youtube-Sir59K8ZDPU-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- [[agent-ready-accessibility|Agent-Ready Accessibility]] — Designing for agents and designing for accessibility converge around explicit structure, reachable controls, and understandable state.

### Evidence Boundary
This synthesis uses the official schedule and only a dedicated manifest-matched recording transcript for session-level claims and topic extraction. Related official-channel, external, and broad livestream sources remain supporting context and do not stand in for the scheduled session.
## People
- [[frank-coyle]]

## Official YouTube Recording
- [[youtube-Sir59K8ZDPU|Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley]] — official AI Engineer YouTube recording published 2026-07-23.
- Evidence status: [[youtube-Sir59K8ZDPU-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-Sir59K8ZDPU]] - dedicated official event recording.
- [[youtube-Sir59K8ZDPU-transcript]] - dedicated official recording transcript.

- [[youtube-Sir59K8ZDPU-slides]] — extracted from the related public AI Engineer video.

- Source video: `youtube-Sir59K8ZDPU`
- Slide deck: [[youtube-Sir59K8ZDPU-slides|Slides: Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley]] — 13 visible slide image(s).
![[assets/slides/Sir59K8ZDPU/slide-001.jpg]]
![[assets/slides/Sir59K8ZDPU/slide-002.jpg]]
![[assets/slides/Sir59K8ZDPU/slide-003.jpg]]
- Slide-derived themes for `youtube-Sir59K8ZDPU`: without, fear, probabilistic, track, july, nothing, mistake, sister.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/Sir59K8ZDPU.txt` (3,096 words).

## Transcript Markdown
- [[youtube-Sir59K8ZDPU-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/Sir59K8ZDPU.txt`.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-Sir59K8ZDPU` — 3,096 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Sir59K8ZDPU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Sir59K8ZDPU`: okay, tool, ontologies, loops, called, ontology, graph, give.
- Slide-derived themes for `youtube-Sir59K8ZDPU`: without, fear, probabilistic, track, july, nothing, mistake, sister.
- Evidence links for `youtube-Sir59K8ZDPU` (primary event evidence): [[youtube-Sir59K8ZDPU]], [[youtube-Sir59K8ZDPU-transcript]], [[youtube-Sir59K8ZDPU-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
