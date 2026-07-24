---
title: "Your Moat Is Your Data Model"
category: "talks"
date: "2026-07-01"
time: "11:40am-12:00pm"
track: "Graphs"
room: "Track 5"
speakers: ["Mike Phipps"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Graphs"
scheduleRoom: "Track 5"
scheduleLabels: ["Graphs", "Track 5", "sponsor", "confirmed"]
---
# Your Moat Is Your Data Model

## Conference Context
- Date/time: 2026-07-01 · 11:40am-12:00pm
- Track/room: Graphs · Track 5
- Speaker(s): Mike Phipps
- Session type/status: sponsor · confirmed

- Track: Graphs
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
Every enterprise AI team faces the same strategic question: where in the stack should a small team focus its effort? Models, frontends, and agent frameworks evolve rapidly and are increasingly commoditized. But regardless of how these layers mature, AI in enterprise settings remains bottlenecked by the same underlying problem: structured data is siloed across systems of record with domain-specific schemas, and the unstructured data needed to contextualize it sits in entirely separate systems, with its own systematic complexities. The durable work is cleaning, curating, and semantically modeling this data in an AI-first manner so that any client — chat, workflow, or otherwise — can query across it. That's the moat. At the Gates Foundation, my team built and deployed our foundation-wide knowledge graph on Neo4j that unifies structured and unstructured data behind a single MCP server. The graph itself is modeled for agentic consumption: natural hierarchies are projected as traversable paths rather than flattened tables, and unstructured documents are semantically chunked, tagged, and mapped to structured entities at ingestion time using AI-driven ETL. The result is a semantic layer where an agent can express a complex cross-system question as a concise graph query and receive an accurate answer. This talk is an architectural walkthrough covering the end-to-end pipeline: AI-based extraction and semantic chunking of unstructured documents, the agent-first data modeling decisions, design considerations for our MCP server, and how we handle graph-based retrieval evals. We'll walk through real query sessions showing Claude interacting with the graph through both chat and workflow integrations. The intended takeaway is a practical framework for where a small enterprise team's investment compounds — and why that investment is the data model, not the layers above it.

## Synthesis
### Synthesized Breakdown
Yes. So my talk today is about the title your data models remote. We have a enterprisewide platform that we had just rolled out here this past month. And so I'll go into details on this.

### Speaker And Company Context
- [[mike-phipps|Mike Phipps]] — Lead AI Engineer at [[gates-foundation|Gates Foundation]].

### Topics Covered
- [[agent-security]]
- [[agentic-search]]
- [[ai-sandboxes]]
- [[coding-agents]]
- [[mcp]]
- [[mcp-apps]]

### Derived Links And Source Material
- [[youtube-jt1Pbr_n6oU-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/jt1Pbr_n6oU.txt` (3,441 words).
- [[youtube-jt1Pbr_n6oU]] — related YouTube source page.
- [[youtube-jt1Pbr_n6oU-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- [[agent-ready-accessibility|Agent-Ready Accessibility]] — Designing for agents and designing for accessibility converge around explicit structure, reachable controls, and understandable state.
- [[mcp-app-runtime|MCP Apps As Agentic App Runtime]] — MCP Apps treats interactive UI returned from MCP servers as a runtime layer for agent-facing software.

### Evidence Boundary
This synthesis uses the official schedule and only a dedicated manifest-matched recording transcript for session-level claims and topic extraction. Related official-channel, external, and broad livestream sources remain supporting context and do not stand in for the scheduled session.
## People
- [[mike-phipps]]

## Official YouTube Recording
- [[youtube-jt1Pbr_n6oU|Your Moat Is Your Data Model — Mike Phipps, Gates Foundation]] — official AI Engineer YouTube recording published 2026-07-22.
- Evidence status: [[youtube-jt1Pbr_n6oU-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-jt1Pbr_n6oU]] - dedicated official event recording.
- [[youtube-jt1Pbr_n6oU-transcript]] - dedicated official recording transcript.

- [[youtube-jt1Pbr_n6oU-slides]] — extracted from the related public AI Engineer video.

- Source video: `youtube-jt1Pbr_n6oU`
- Slide deck: [[youtube-jt1Pbr_n6oU-slides|Slides: Your Moat Is Your Data Model — Mike Phipps, Gates Foundation]] — 5 visible slide image(s).
![[assets/slides/jt1Pbr_n6oU/slide-001.jpg]]
![[assets/slides/jt1Pbr_n6oU/slide-002.jpg]]
![[assets/slides/jt1Pbr_n6oU/slide-003.jpg]]
- Slide-derived themes for `youtube-jt1Pbr_n6oU`: track, july, fair, intro, defensible, organization, presented, users.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/jt1Pbr_n6oU.txt` (3,441 words).

## Transcript Markdown
- [[youtube-jt1Pbr_n6oU-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/jt1Pbr_n6oU.txt`.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-jt1Pbr_n6oU` — 3,441 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-jt1Pbr_n6oU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-jt1Pbr_n6oU`: data, model, graph, across, structure, chat, part, structured.
- Slide-derived themes for `youtube-jt1Pbr_n6oU`: track, july, fair, intro, defensible, organization, presented, users.
- Evidence links for `youtube-jt1Pbr_n6oU` (primary event evidence): [[youtube-jt1Pbr_n6oU]], [[youtube-jt1Pbr_n6oU-transcript]], [[youtube-jt1Pbr_n6oU-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
