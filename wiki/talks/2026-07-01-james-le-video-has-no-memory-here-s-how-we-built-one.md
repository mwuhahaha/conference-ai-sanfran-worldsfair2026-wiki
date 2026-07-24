---
title: "Video Has No Memory. Here's How We Built One."
category: "talks"
date: "2026-07-01"
time: "2:25pm-2:45pm"
track: "Graphs"
room: "Track 5"
speakers: ["James Le"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Graphs"
scheduleRoom: "Track 5"
scheduleLabels: ["Graphs", "Track 5", "sponsor", "confirmed"]
---
# Video Has No Memory. Here's How We Built One.

## Conference Context
- Date/time: 2026-07-01 · 2:25pm-2:45pm
- Track/room: Graphs · Track 5
- Speaker(s): James Le
- Session type/status: sponsor · confirmed

- Track: Graphs
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
Every video AI query today starts from scratch. There's no durable state, no entity continuity, no way to ask "what does this corpus know?" instead of "find me something like this." This talk is about fixing that by engineering a proper memory layer for video intelligence, grounded in what we shipped at TwelveLabs with Jockey. What this talk covers: 1 - Why video memory is categorically different from text memory: Video is temporal, multimodal, dense, ambiguous, and evidence-sensitive. Larger context windows don't solve this. The problem isn't retrieval bandwidth, it's that there's no durable representation to retrieve into. 2 - The context graph as a systems concept, not a database choice: I'll define what "context graph" actually means in practice: time-bounded moments, cross-video entity resolution, appearance tracking, and relationship mapping. This is infrastructure-level thinking, not a graph DB sales pitch. 3 - Five design principles that determine whether video intelligence is reusable infrastructure or a search wrapper with extra steps: + Ingest once, reason many times (move expensive understanding work into preparation) + Store primitives, not just answers (moments, entities, appearances, relationships) + Ground every claim to source video (a timestamp is a product requirement, not a safety footnote) + Let intent shape memory (brand safety and sports highlights need different primitives from the same footage) + Keep the memory layer composable and API-first 4 - What this unlocks for builders. Corpus digest, agentic search with grounded references, entity-centric workflows, timeline reconstruction, and compliance tooling, all built on the same durable substrate. The talk is concrete and demo-grounded. You'll leave with a specific mental model for memory architecture, actionable decisions for ingestion pipeline design and entity resolution, and a clear line between "search with extra steps" and actual video intelligence infrastructure.

## Synthesis
### Synthesized Breakdown
Thanks so much for having me and uh inviting me to to be a speaker at uh the warfare. You know I attended last year and was so impressed about the quality of presenters. So so glad to to have a chance to be here and present. Uh so the title of my talk is you know video has no memory, right?

### Speaker And Company Context
- [[james-le|James Le]] — Head of Developer Experience at [[twelvelabs|TwelveLabs]].

### Topics Covered
- [[agent-security]]
- [[agentic-search]]
- [[coding-agents]]

### Derived Links And Source Material
- [[youtube-mOf-PP4mVjA-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/mOf-PP4mVjA.txt` (3,509 words).
- [[youtube-mOf-PP4mVjA]] — related YouTube source page.
- [[youtube-mOf-PP4mVjA-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis uses the official schedule and only a dedicated manifest-matched recording transcript for session-level claims and topic extraction. Related official-channel, external, and broad livestream sources remain supporting context and do not stand in for the scheduled session.
## People
- [[james-le]]

## Official YouTube Recording
- [[youtube-mOf-PP4mVjA|Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs]] — official AI Engineer YouTube recording published 2026-07-23.
- Evidence status: [[youtube-mOf-PP4mVjA-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-mOf-PP4mVjA]] - dedicated official event recording.
- [[youtube-mOf-PP4mVjA-transcript]] - dedicated official recording transcript.

- [[youtube-mOf-PP4mVjA-slides]] — extracted from the related public AI Engineer video.

- Source video: `youtube-mOf-PP4mVjA`
- Slide deck: [[youtube-mOf-PP4mVjA-slides|Slides: Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs]] — 31 visible slide image(s).
![[assets/slides/mOf-PP4mVjA/slide-001.jpg]]
![[assets/slides/mOf-PP4mVjA/slide-002.jpg]]
![[assets/slides/mOf-PP4mVjA/slide-003.jpg]]
- Slide-derived themes for `youtube-mOf-PP4mVjA`: memory, built, data, incredibly, complex, scale, holistic, understanding.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/mOf-PP4mVjA.txt` (3,509 words).

## Transcript Markdown
- [[youtube-mOf-PP4mVjA-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/mOf-PP4mVjA.txt`.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-mOf-PP4mVjA` — 3,509 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-mOf-PP4mVjA`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-mOf-PP4mVjA`: memory, scene, content, system, across, layer, application, context.
- Slide-derived themes for `youtube-mOf-PP4mVjA`: memory, built, data, incredibly, complex, scale, holistic, understanding.
- Evidence links for `youtube-mOf-PP4mVjA` (primary event evidence): [[youtube-mOf-PP4mVjA]], [[youtube-mOf-PP4mVjA-transcript]], [[youtube-mOf-PP4mVjA-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
