---
title: "CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens"
category: "talks"
date: "2026-07-01"
time: "10:45am-11:05am"
track: "Graphs"
room: "Track 5"
speakers: ["Stephen Chin"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Graphs"
scheduleRoom: "Track 5"
scheduleLabels: ["Graphs", "Track 5", "sponsor", "confirmed"]
---
# CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens

## Conference Context
- Date/time: 2026-07-01 · 10:45am-11:05am
- Track/room: Graphs · Track 5
- Speaker(s): Stephen Chin
- Session type/status: sponsor · confirmed

- Track: Graphs
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
Autonomous assistants are easy to demo and hard to make reliable. The problem is usually not tool access. It is memory. Most assistant architectures still treat memory as a chat log plus vector retrieval. That is fine for document question answering, but it breaks down when the assistant must connect conversations, people, tools, and decisions across multiple tool iterations. For an AI engineer, a single request can depend on a Slack thread, a GitHub PR, a failed CI run, a calendar event, and prior operating preferences or constraints. These are not isolated pieces of context. They form a connected state that changes as work progresses and context grows. In this talk, I’ll show why knowledge graphs, context graphs, and GraphRAG provide a better foundation for OpenClaw-style assistants. Knowledge graphs capture durable entities and relationships. Context graphs capture the operational layer assistants usually lose, including actions, decision traces, provenance, and recency. GraphRAG turns that structure into task-time context by combining graph traversal, semantic retrieval, and tool use. Attendees will leave with practical patterns for schema design, retrieval routing, and evaluation, plus a concrete blueprint for assistants that remember more than the last prompt and retrieve more than the nearest chunk.

## Synthesis
### Transcript-Backed Summary
The talk argues that automated assistants fail less because they lack tools and more because they lack a memory model that preserves connected state. Chin contrasts markdown-file and vector-only memory with graph memory, then shows a hybrid approach where vector search seeds graph traversal so the assistant can follow multihop relationships across people, devices, decisions, and actions. The practical payoff is more precise, explainable, and auditable answers for operational tasks, which the home-lab demo illustrates by finding the right exposed software and ports where vector retrieval stayed vague. The conclusion is that at larger scales, especially when context windows are no longer enough, assistants need graph memory rather than more tokens.

### Key Takeaways
- Represent assistant memory as connected entities and relationships instead of isolated note files.
  - Evidence: "That's that's very unfortunate. So enter graphs. Graphs are a great way of finding the relationships, finding those identities, bu mapping out the paths, getting that full chain and they're built for this sort of connected data."
- Use vector retrieval to seed graph traversal, then follow the graph for the actual answer.
  - Evidence: "So it uses the vector search to get the seed nodes where it starts the traversal and then it uses a graph search pulling the the nearest neighbors and then ranking those by how related they are."
- Prefer graph memory when you need answers you can inspect, explain, and audit.
  - Evidence: "And graphs are they're accurate so they give you very precise information. Explainable because you can look at the graph which got returned and auditable because now you can actually say these are the this is the context."
- Benchmark memory systems on the same source data in a direct A/B setup before trusting their behavior.
  - Evidence: "Now, what I did for this um high stakes demo is I over the past week or two, I took my home lab as the demo environment, did a full digital twin as a graph, and I have two separate environments built off the same original markdown files."

### Claims From The Talk
- The talk says the hard part of autonomous assistants is memory: what gets put into context and what gets recalled, not the response loop itself. (`explicit`)
  - Evidence: "But the hard part is the memory. The hard part is what you put in context, what you're recalling from."
- The speaker argues that storing memory as markdown files burns a large amount of context budget and scales poorly. (`explicit`)
  - Evidence: "But if your whole memory is a bunch of markdown files, you're wasting a lot of tokens. So, um, my my average agents are are loading up at least 100k in tokens for each round."
- The talk claims vector similarity alone is not the same as actual relationships, which leads to hallucinations and missed answers in complex cases. (`explicit`)
  - Evidence: "And so you get hallucinations. You get a lot of problems when you're relying solely on vector lookup as the answer."
- The speaker argues graphs are precise, explainable, and auditable because you can inspect the returned graph context directly. (`explicit`)
  - Evidence: "And graphs are they're accurate so they give you very precise information. Explainable because you can look at the graph which got returned and auditable because now you can actually say these are the this is the context."
- In the live demo, the graph-backed approach found the correct out-of-date software details, while the vector-backed approach was not useful. (`explicit`)
  - Evidence: "And you can see the answer here. So guest name tinsterland exactly as expected. Um OS version out of date and it's flagging."
- The speaker argues that large-scale assistants need a better memory system than markdown files once the task exceeds modern context-window limits. (`explicit`)
  - Evidence: "If if you have a big enterprise which has a huge data center, if you're doing things in financial services where you have like a huge set of companies and customer records you're trying to do, if you're doing anything at at large scale where it doesn't fit into the 1 million context window of the modern models, you really need a better memory system than just throwing things in markdown files."

### Topics Covered
- [[agent-memory|Assistant memory architecture]] — The central problem of preserving useful state across assistant turns and tool iterations.
- [[agent-memory|Knowledge graphs]] — Graph-based representation of entities and relationships for connected data.
- [[agent-memory|Vector retrieval]] — Similarity-based retrieval from embeddings and vectors.
- **Multihop reasoning** — Using graphs to answer questions that require multiple relationship hops.
- [[agent-memory|Auditable context]] — Answers that can be inspected and traced back to a specific graph path.
- [[agent-memory|Large-scale assistants]] — Memory limits and operating scale beyond a prompt-sized context window.

### Tools And Named Systems
- **OpenClaw** — The assistant platform used in the examples and demos.
- **pgvector** — A vector database used for embedding-based retrieval.
- **LanceDB** — A vector database used alongside the graph store in the demo.
- [[mcp|MCP]] — The protocol layer used to expose memory as callable servers and commands.
- **Hermes agent** — An agent system the speaker praises for reflecting and updating skills after each task.
- [[claude|Claude]] — The model the speaker says can write Cypher and build entity extractors.
- **Cognite** — The graph backend used for the demo environment.

### Novel Concepts And Methods
- **Memory loop** — A prompt-thinking-tool-observe loop that repeatedly updates memory as the assistant works through a task.
- **Vector-seeded graph traversal** — Use vector search to seed candidate nodes, then traverse the graph to follow connected relationships.
- **Dual-store A/B evaluation** — Build two memory backends from the same source material and compare their answers side by side.
- **Fresh-session retrieval** — Start a fresh session and rely on traversed graph memory instead of rereading the original source material.
- **Entity extraction and deduplication** — Improve graph quality by changing extraction and reducing duplicate nodes.

### Open Questions
- **When should an assistant stop relying on similarity search and switch to graph traversal for the task?** — This determines the routing policy between fast retrieval and relationship-aware reasoning.
- **What extraction and schema choices best prevent duplicate nodes without losing important distinctions?** — Graph memory quality depends on how cleanly entities and relationships are modeled.
- **How can an assistant stay accurate when it can no longer query live systems and must answer from stored memory only?** — Operational assistants need a reliable story for stale or disconnected state.
- **How can memory stay useful without flooding every turn with markdown-sized context dumps?** — Token cost and context pressure are the practical limit that motivates the whole approach.

### Derived Links And Source Material
- [[youtube-Q0VkgCyNVUg-transcript]] — dedicated official recording transcript.
- [[youtube-Q0VkgCyNVUg]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/Q0VkgCyNVUg--2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.json`.

### Speaker Context
- [[stephen-chin|Stephen Chin]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[stephen-chin]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-eW_vxrjvERk-dense-slides]] (1 viable slide images).
- Related slide/OCR pages:
- [[youtube-eW_vxrjvERk-dense-slides]]
- [[youtube-eW_vxrjvERk-reconstructed-slides]]
- [[youtube-eW_vxrjvERk-slides]]
- Slide-derived terms: `graph`, `context`, `engineer`, `memory`, `europe`, `engineering`, `future`, `reasoning`, `entities`, `knowledge`, `relationships`, `enhance`, `relevance`, `domain`, `care`, `plans`, `associated`, `andrea`

## Official YouTube Recording
- [[youtube-Q0VkgCyNVUg|CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j]] — official AI Engineer YouTube recording published 2026-07-22.
- Evidence status: [[youtube-Q0VkgCyNVUg-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-Q0VkgCyNVUg]] - dedicated official event recording.
- [[youtube-Q0VkgCyNVUg-transcript]] - dedicated official recording transcript.
- [[youtube-eW_vxrjvERk]] - supporting context; not the exact session recording.

- [[youtube-Q0VkgCyNVUg-slides]] — extracted from the related public AI Engineer video.

- Source video: `youtube-Q0VkgCyNVUg`
- Slide deck: [[youtube-Q0VkgCyNVUg-slides|Slides: CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j]] — 22 visible slide image(s).
![[assets/slides/Q0VkgCyNVUg/slide-001.jpg]]
![[assets/slides/Q0VkgCyNVUg/slide-002.jpg]]
![[assets/slides/Q0VkgCyNVUg/slide-003.jpg]]
- Slide-derived themes for `youtube-Q0VkgCyNVUg`: shell, track, july, skills, meat, engineering, future, wakes.
- Source video: `youtube-eW_vxrjvERk`
- Slide deck: [[youtube-eW_vxrjvERk-dense-slides|Dense Slides: Connecting the Dots with Context Graphs — Stephen Chin, Neo4j]] — slide evidence page.
- Additional slide evidence: [[youtube-eW_vxrjvERk-slides|Slides: Connecting the Dots with Context Graphs — Stephen Chin, Neo4j]], [[youtube-eW_vxrjvERk-reconstructed-slides|Reconstructed Slides: Connecting the Dots with Context Graphs — Stephen Chin, Neo4j]]
- Slide-derived themes for `youtube-eW_vxrjvERk`: context, slack, knowledge, enhance, relevance, domain, alternatives, considered.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/Q0VkgCyNVUg.txt` (3,266 words).

## Transcript Markdown
- [[youtube-Q0VkgCyNVUg-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/Q0VkgCyNVUg.txt`.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-Q0VkgCyNVUg` — 3,266 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Q0VkgCyNVUg`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Q0VkgCyNVUg`: graph, memory, vector, files, demo, information, great, store.
- Slide-derived themes for `youtube-Q0VkgCyNVUg`: shell, track, july, skills, meat, engineering, future, wakes.
- Evidence links for `youtube-Q0VkgCyNVUg` (primary event evidence): [[youtube-Q0VkgCyNVUg]], [[youtube-Q0VkgCyNVUg-transcript]], [[youtube-Q0VkgCyNVUg-slides]]
- `youtube-eW_vxrjvERk` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-eW_vxrjvERk`: context, slack, knowledge, enhance, relevance, domain, alternatives, considered.
- Evidence links for `youtube-eW_vxrjvERk` (supporting context only): [[youtube-eW_vxrjvERk]], [[youtube-eW_vxrjvERk-slides]], [[youtube-eW_vxrjvERk-dense-slides]], [[youtube-eW_vxrjvERk-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
