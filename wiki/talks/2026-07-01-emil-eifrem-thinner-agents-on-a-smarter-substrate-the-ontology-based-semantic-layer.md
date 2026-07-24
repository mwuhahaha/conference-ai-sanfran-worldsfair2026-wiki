---
title: "Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer"
category: "talks"
date: "2026-07-01"
time: "10:20am-10:30am"
track: "Graphs"
room: "Main Stage"
speakers: ["Emil Eifrem"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Graphs"
scheduleRoom: "Main Stage"
scheduleLabels: ["Graphs", "Main Stage", "keynote", "confirmed"]
---
# Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer

## Conference Context
- Date/time: 2026-07-01 · 10:20am-10:30am
- Track/room: Graphs · Main Stage
- Speaker(s): Emil Eifrem
- Session type/status: keynote · confirmed

- Track: Graphs
- Room: Main Stage
- Session type: keynote
- Status: confirmed

## Session Description
No official description published in the schedule data.

## Synthesis
### Transcript-Backed Summary
The talk argues that enterprise agents should not be built as thick, one-off systems with every team manually wiring data sources from scratch. Instead, the speaker proposes thin agents sitting on a shared ontology-based semantic layer that separates business intent, technical data inventory, and runtime learning. In that model, a business ontology describes the organization in human terms, a technical ontology catalogs the actual systems and schemas, and execution traces feed back what worked so future agent runs can choose better sources and improve over time. The practical result is less duplicated integration work, better trust and governance over data access, and cross-agent learning that becomes more valuable as the number of agents and data sources grows.

### Key Takeaways
- Enterprise agents become costly when every team must rediscover data sources from scratch for each new workflow.
  - Evidence: "So, that's great. It's fantastic. It works. But it has a few problems. So first of all, every single time a team has to build an agent, they have to figure out from scratch where the data that they require for that agent to operate, where it sits, which if you work at a startup and you have one application, it sits on top of one Postgress database."
- The manual wiring approach duplicates effort and conflicts with the DRY principle when enterprise data changes.
  - Evidence: "Am I allowed to access it? So on and so forth. It also violates one of the core principles of software engineering, the dry principle."
- A shared substrate is the proposed architectural answer for scaling agents across large organizations.
  - Evidence: "And the pattern that is emerging is that in order to do agents at scale, we need thin agents on a smarter shared substrate."
- The three pillars are presented as the complete mechanism for addressing discovery, trust, governance, and learning.
  - Evidence: "Three pillars of the ontology based semantic layer, a business ontology, a technical ontology, the execution traces taken together, they solve all four of the problems."
- The desired end state is a system where knowledge accumulates across agents instead of remaining trapped in code and prompts.
  - Evidence: "And not just self-learning on an individual agent, but across agents as well. So we're moving from this world, a world of thick agents with manually wired data sources into this world where we have thin agents on a smarter shared ontology based semantic layer."

### Claims From The Talk
- The speaker argues that scaling agents in enterprises requires thin agents running on a smarter shared substrate, rather than thick agents with manually wired data sources. (`explicit`)
  - Evidence: "And the pattern that is emerging is that in order to do agents at scale, we need thin agents on a smarter shared substrate."
- He claims the three pillars of a business ontology, technical ontology, and execution traces together solve the four problems he identified. (`explicit`)
  - Evidence: "Three pillars of the ontology based semantic layer, a business ontology, a technical ontology, the execution traces taken together, they solve all four of the problems."
- He reports that this approach makes data-source discovery easier and provides a way to assess whether sources are trustworthy. (`explicit`)
  - Evidence: "We now have a very easy way to discover the data sources. We know if they're trustworthy or not."
- He says the shared mapping layer gives a single governed place to connect business intent to data sources, which prevents repeated agent-specific wiring. (`explicit`)
  - Evidence: "We have a single governed place that maps business intent and the concepts to those data sources so we don't repeat ourselves."
- He claims the runtime-trace loop enables self-learning so an agent becomes slightly smarter over time and knowledge can transfer across agents. (`explicit`)
  - Evidence: "If something changes that cascades across all my agents, right? And we have self-arning. So my agent that wakes up tomorrow is slightly smarter than it was today."

### Topics Covered
- [[semantic-infrastructure-and-ontology|Thin agents on a shared substrate]] — The architectural idea of building simpler agents that rely on a shared enterprise knowledge substrate.
- [[semantic-infrastructure-and-ontology|Business ontology]] — A business-readable graph of concepts and relationships used to model how the organization talks about its domain.
- **Technical ontology** — A graph of enterprise data systems, schemas, and assets used to represent the actual technical landscape.
- [[semantic-infrastructure-and-ontology|Ontology mapping]] — The link between domain concepts and underlying systems of record.
- [[coding-agents|Execution traces]] — Using observed agent runs to score outcomes and guide future decisions.
- [[semantic-infrastructure-and-ontology|Process-guided agent]] — An agent that is intended to follow a predefined enterprise workflow.

### Tools And Named Systems
- [[neo4j|Neo4j]] — Enterprise graph database platform used as the substrate for the ontology-based semantic layer.
- **Postgres** — Relational database mentioned as a common enterprise system of record.
- [[snowflake|Snowflake]] — Cloud data warehouse mentioned as part of the enterprise data landscape.
- **Databricks** — Analytics and data processing platform mentioned as part of the enterprise data landscape.
- [[s3|S3]] — Cloud object storage service mentioned as part of the enterprise data landscape.
- **DMV registry** — Government motor vehicle registry cited as a possible identity-verification source.
- **Passport verification service** — Identity-verification service cited as another possible source for account opening.

### Novel Concepts And Methods
- **Business ontology** — Use a business-facing ontology to represent domain concepts and processes in terms people in the organization actually use.
- **Technical ontology** — Build a technical ontology that catalogs the enterprise's databases, buckets, schemas, and other data assets.
- **Ontology mapping** — Map business concepts to systems of record so the semantic layer can resolve the right data source for a given need.
- **Trace-driven learning** — Capture execution traces from agent runs and feed outcomes back into future selection decisions.

### Open Questions
- **What are the three concrete ways to construct the technical ontology at enterprise scale?** — That is the missing implementation detail for turning the blueprint into an operational system.
- **How should trace signals be scored and combined so future agent runs choose better data sources in the right context?** — The talk depends on trace-driven improvement, but the scoring policy determines whether the loop actually learns useful behavior.
- **How is trust in a data source reconciled when human-curated knowledge and runtime evidence disagree?** — The approach uses both top-down governance and bottom-up traces, so conflict resolution is central to safe adoption.

### Derived Links And Source Material
- [[youtube-VGN22pPpb-8-transcript]] — dedicated official recording transcript.
- [[youtube-VGN22pPpb-8]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/VGN22pPpb-8--2026-07-01-emil-eifrem-thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.json`.

### Speaker Context
- [[emil-eifrem|Emil Eifrem]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[emil-eifrem]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-knDDGYHnnSI-dense-slides]] (10 viable slide images).
- Related slide/OCR pages:
- [[youtube-knDDGYHnnSI-dense-slides]]
- [[youtube-knDDGYHnnSI-reconstructed-slides]]
- [[youtube-knDDGYHnnSI-slides]]
- Slide-derived terms: `e-03`, `microsoft`, `smol`, `graphrag`, `search`, `google`, `graph`, `moscone`, `erved2024`, `knowledge`, `accuracy`, `e-04`, `lycos`, `text`, `world`, `users`, `center`, `initial`

## Official YouTube Recording
- [[youtube-VGN22pPpb-8|Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j]] — official AI Engineer YouTube recording published 2026-07-22.
- Evidence status: [[youtube-VGN22pPpb-8-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Livestream Segment
- [Watch in livestream at 01:39:01](https://www.youtube.com/watch?v=I2cbIws9j10&t=5941s) — WF26: Harness Engineering & Startup Battlefield.
- Evidence: transcript-aligned segment validated against the official schedule and timed captions.
- Confidence: high automated match; prefer a dedicated cut-video recording when one exists.
## Media Evidence
- [[youtube-VGN22pPpb-8]] - dedicated official event recording.
- [[youtube-VGN22pPpb-8-transcript]] - dedicated official recording transcript.
- [[youtube-knDDGYHnnSI]] - supporting context; not the exact session recording.

- Source video: `youtube-VGN22pPpb-8`
- Slide deck: [[youtube-VGN22pPpb-8-slides|Slides: Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j]] — 32 visible slide image(s).
![[assets/slides/VGN22pPpb-8/slide-001.jpg]]
![[assets/slides/VGN22pPpb-8/slide-002.jpg]]
![[assets/slides/VGN22pPpb-8/slide-003.jpg]]
- Slide-derived themes for `youtube-VGN22pPpb-8`: semantic, layer, thinner, smarter, substrate, world, opening, plan.
- Source video: `youtube-knDDGYHnnSI`
- Slide deck: [[youtube-knDDGYHnnSI-dense-slides|Dense Slides: GraphRAG: The Marriage of Knowledge Graphs and RAG: Emil Eifrem]] — slide evidence page.
- Additional slide evidence: [[youtube-knDDGYHnnSI-slides|Slides: GraphRAG: The Marriage of Knowledge Graphs and RAG: Emil Eifrem]], [[youtube-knDDGYHnnSI-reconstructed-slides|Reconstructed Slides: GraphRAG: The Marriage of Knowledge Graphs and RAG: Emil Eifrem]]
- Slide-derived themes for `youtube-knDDGYHnnSI`: full, text, george, mooc.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/VGN22pPpb-8.txt` (1,879 words).

## Transcript Markdown
- [[youtube-VGN22pPpb-8-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/VGN22pPpb-8.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-VGN22pPpb-8` — 1,879 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-VGN22pPpb-8`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-VGN22pPpb-8`: data, sources, ontology, first, business, smarter, name, forj.
- Slide-derived themes for `youtube-VGN22pPpb-8`: semantic, layer, thinner, smarter, substrate, world, opening, plan.
- Evidence links for `youtube-VGN22pPpb-8` (primary event evidence): [[youtube-VGN22pPpb-8]], [[youtube-VGN22pPpb-8-transcript]], [[youtube-VGN22pPpb-8-slides]]
- `youtube-knDDGYHnnSI` — source page linked; role: supporting context only.
- Evidence links for `youtube-knDDGYHnnSI` (supporting context only): [[youtube-knDDGYHnnSI]], [[youtube-knDDGYHnnSI-slides]], [[youtube-knDDGYHnnSI-dense-slides]], [[youtube-knDDGYHnnSI-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
