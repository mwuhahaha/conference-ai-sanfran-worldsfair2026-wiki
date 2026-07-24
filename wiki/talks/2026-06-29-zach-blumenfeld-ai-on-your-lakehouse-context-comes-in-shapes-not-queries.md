---
title: "AI on Your Lakehouse: Context Comes in Shapes, Not Queries"
category: "talks"
date: "2026-06-29"
time: "9:00am-11:00am"
track: "Track 2"
room: "Track 2"
speakers: ["Zach Blumenfeld"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Track 2"
scheduleRoom: "Track 2"
scheduleLabels: ["Track 2", "Track 2", "sponsor", "confirmed"]
---
# AI on Your Lakehouse: Context Comes in Shapes, Not Queries

## Conference Context
- Date/time: 2026-06-29 · 9:00am-11:00am
- Track/room: Track 2 · Track 2
- Speaker(s): Zach Blumenfeld
- Session type/status: sponsor · confirmed

- Track: Track 2
- Room: Track 2
- Session type: sponsor
- Status: confirmed

## Session Description
Your agent can reach your data but still can't use it reliably: vector search and Text2SQL each hand it a slice, but not the view to know what's truly relevant and how to connect the right info. Without that, answers come back confident but wrong, and agent decisions cannot be trusted. The problem isn't caused by a bad model or bad query, but rather a lack of context, and thinking in terms of shapes is what cracks it. In this hands-on session, you'll learn how to build three reusable graph shapes from your lakehouse data using Neo4j, so your agent can navigate and view the right context to answer and act accurately: - Table of Contents (Trees) — navigate what's there - Themes (Communities) — surface patterns nobody named - Connections (Paths & Cycles) — trace how entities, documents, and records relate Portable to BigQuery, Databricks, Snowflake, or anywhere. You'll leave with real, practical techniques and the code to run with your own data and agents.

## Synthesis
### Transcript-Backed Summary
Zach Blumenfeld argues that lakehouse copilots usually fail because they get the wrong context, not because the model cannot answer questions. His fix is to encode context as reusable graph shapes rather than as a single query style: a semantic-layer graph for warehouse metadata, a deterministic tree-plus-links graph for documents, and community-detection themes for corpus-wide patterns. The practical payoff is that an agent can navigate to the right slice of data, chain the shapes together, and answer both point questions and estate-level coverage questions with less hallucination and less dependence on moving all data into a graph. The main tradeoff is that this lighter-weight approach depends on good source structure and careful naming, so it is faster and more model-agnostic than LLM extraction, but sometimes less expressive and still best combined with search.

### Key Takeaways
- The workshop centers on three reusable shapes: connections, table of contents, and themes.
  - Evidence: "And so there's going to be three concrete shapes that we'll introduce you to today. Uh, so the first one um, we're going to call table of contents and it's somewhat like a tree structure uh, but with also different types of links between them."
- The connection shape gives the agent a semantic layer that helps it join warehouse tables correctly as the schema grows.
  - Evidence: "Um so that's the basics of this first shape. And you can imagine that as your data starts to grow and you start to get more and more tables, it's very useful to have this semantic layer um to then help essentially guide how everything joins together."
- The table-of-contents shape lets the agent traverse document hierarchy and links instead of relying only on similarity search.
  - Evidence: "Um, that's the general idea with this. And so what this gives the agent to do is not just search like vector search or or lexical search but actually kind of traverse through the documents in a sense."
- Theme detection is useful for estate-level questions because it reveals how documents cluster across the corpus.
  - Evidence: "And so this is very useful from sort of a whole estate wide question because you can start to understand in your data kind of how everything kind of groups and clusters together."
- The final workflow combines full-text grounding, tree traversal, and warehouse joins so the agent can answer a repair question end to end.
  - Evidence: "And you'll see what it will do here. Um it will look for the document code. It'll do a full text search."

### Claims From The Talk
- The speaker argues that lakehouse copilots usually fail because they lack the right context, not because the model or query style is inherently broken. (`explicit`)
  - Evidence: "times what can happen is you're given these tools like text to SQL and vector search and nowadays we don't really have trouble accessing that data Um, but sometimes there are still some challenges around how do you give your agent the right type of context, whether or not they can see all the data"
- He says moving all warehouse data into graph is often the wrong default because continuous sync, security posture, and custom ETL overhead can make that impractical. (`explicit`)
  - Evidence: "Why wouldn't we just push that into the graph? Well, I think in a lot of cases that's easier said than done, right?"
- He reports that the connection shape uses graph as a semantic layer for metadata, not as a data copy, so the agent can infer joins from structure instead of ingesting the full warehouse. (`explicit`)
  - Evidence: "And so if you notice the thing that we're doing here really is we're not using the graph to copy the data over."
- He says the document graph load is deterministic and idempotent, which makes it faster and more repeatable when the source documents already have strong structure. (`explicit`)
  - Evidence: "Um, and the benefits of having a deterministic load like this is number one, it's going to be item potent."
- He argues that semantic search is not a replacement for the other shapes and that hybrid retrieval, especially with full text search, still matters. (`explicit`)
  - Evidence: "I think it would be naive to call it a replacement because most of the people that I see using this will eventually incorporate some sort of hybrid vector retrieval or full text search work I do."
- He says the theme view is stable and data-derived, but its usefulness depends on the quality of document titles, links, and metadata. (`strong`)
  - Evidence: "If the data changes, it will change to reflect the data. So, it's very stable. The disadvantage to it would be if your links in your documents um, and the titles and things that are being scooped up, because this is really only looking basically at document metadata and link metadata."

### Topics Covered
- [[agent-memory|Lakehouse context]] — Using graph shapes to supply agents with the right context for lakehouse reasoning.
- **Semantic layers** — A metadata graph that acts as a semantic layer over warehouse schemas.
- [[agent-memory|Document navigation trees]] — A containment-tree view of documents with hierarchical links and drill-down navigation.
- [[agentic-search|Theme discovery]] — Community detection for surfacing corpus-wide clusters and hidden themes.
- [[agentic-search|Agentic query routing]] — An agent workflow that chains outline, search, and theme shapes to answer mixed structured and unstructured questions.

### Tools And Named Systems
- **BigQuery** — The warehouse example used throughout the session for structured repair data and join paths.
- [[neo4j|Neo4j]] — Neo4j is the graph platform at the center of the semantic layer, document graph, and theme analysis.
- **Neo Carta** — Neo Carta is the lab project used to create the metadata graph for the semantic layer.
- [[claude-code|Claude Code]] — Claude Code is the agentic coding environment used to run the workshop workflows and generate queries.
- **Lucene** — Lucene is the full-text search index used for document and section lookup inside the graph.
- **Graph Data Science** — The Graph Data Science library powers the Leiden community detection used in the themes view.
- **MCP server** — The MCP server is the interface the agent uses to read metadata and drive the semantic-layer workflow.

### Novel Concepts And Methods
- **Graph semantic layer** — Use a graph semantic layer over warehouse metadata to let an agent reason about joins without copying the underlying tables into graph.
- **Deterministic document ingestion** — Load documents deterministically into a containment tree with ordered links so the agent can traverse a table-of-contents view.
- **URI-scoped search** — Run full-text search on document and section nodes, then scope results by hierarchical URI so search stays inside the right subtree.
- **Projected community detection** — Project the graph into memory and run Leiden community detection to surface clusters and themes efficiently.
- **Spec-driven query generation** — Write a spec first and have the agent generate Cypher against that spec, rather than hand-authoring complex queries directly.

### Open Questions
- **How granular should relationship naming be before the graph becomes too hard for humans and agents to manage?** — This affects how expressive the graph can be without making query generation and maintenance unwieldy.
- **How should theme assignments and summaries be handled when the underlying data changes over time?** — Temporal data can invalidate clusters, so the answer determines whether theme outputs can support snapshots or trend analysis.
- **How should teams benchmark these shapes against ordinary vector search as the knowledge base grows?** — Without benchmarking, it is hard to know when the graph shapes justify their added modeling effort.
- **Should the structured-data graph and the unstructured-data graph eventually be linked together, and if so, how?** — Direct linking could make cross-domain reasoning more deterministic, but it adds modeling and maintenance complexity.

### Derived Links And Source Material
- [[youtube-kRkcNOsRyYg-transcript]] — dedicated official recording transcript.
- [[youtube-kRkcNOsRyYg]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/kRkcNOsRyYg--2026-06-29-zach-blumenfeld-ai-on-your-lakehouse-context-comes-in-shapes-not-queries.json`.

### Speaker Context
- [[zach-blumenfeld|Zach Blumenfeld]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[zach-blumenfeld]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-B9h9ovW5H9U-dense-slides]] (1 viable slide images).
- Related slide/OCR pages:
- [[youtube-B9h9ovW5H9U-dense-slides]]
- [[youtube-B9h9ovW5H9U-reconstructed-slides]]
- [[youtube-B9h9ovW5H9U-slides]]
- Slide-derived terms: `context`, `graph`, `engineering`, `claude`, `future`, `graphs`, `knowledge`, `base`, `engineer`, `decision`, `relationships`, `neo4j`, `alengineer`, `information`, `required`, `jessica`, `backend`, `frontend`

## Official YouTube Recording
- [[youtube-kRkcNOsRyYg|AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j]] — official AI Engineer YouTube recording published 2026-07-23.
- Evidence status: [[youtube-kRkcNOsRyYg-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-kRkcNOsRyYg]] - dedicated official event recording.
- [[youtube-kRkcNOsRyYg-transcript]] - dedicated official recording transcript.
- [[youtube-B9h9ovW5H9U]] - supporting context; not the exact session recording.

- [[youtube-kRkcNOsRyYg-slides]] — extracted from the related public AI Engineer video.

- Source video: `youtube-kRkcNOsRyYg`
- Slide deck: [[youtube-kRkcNOsRyYg-slides|Slides: AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j]] — 32 visible slide image(s).
![[assets/slides/kRkcNOsRyYg/slide-001.jpg]]
![[assets/slides/kRkcNOsRyYg/slide-002.jpg]]
![[assets/slides/kRkcNOsRyYg/slide-003.jpg]]
- Slide-derived themes for `youtube-kRkcNOsRyYg`: engineering, future, engineer, squire, ryan, knight, senior, partner.
- Source video: `youtube-B9h9ovW5H9U`
- Slide deck: [[youtube-B9h9ovW5H9U-dense-slides|Dense Slides: Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j]] — slide evidence page.
- Additional slide evidence: [[youtube-B9h9ovW5H9U-slides|Slides: Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j]], [[youtube-B9h9ovW5H9U-reconstructed-slides|Reconstructed Slides: Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j]]
- Slide-derived themes for `youtube-B9h9ovW5H9U`: context, graphs, information, required, accurate, answer, graph, started.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/kRkcNOsRyYg.txt` (18,117 words).

## Transcript Markdown
- [[youtube-kRkcNOsRyYg-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/kRkcNOsRyYg.txt`.

## Attendance Visibility
No high-confidence attendance icon signal is shown for this talk. The sampled video evidence was either low confidence, source-proxy-only, or did not expose a clear audience view.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-kRkcNOsRyYg` — 18,117 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-kRkcNOsRyYg`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-kRkcNOsRyYg`: graph, data, well, question, inside, search, over, documents.
- Slide-derived themes for `youtube-kRkcNOsRyYg`: engineering, future, engineer, squire, ryan, knight, senior, partner.
- Evidence links for `youtube-kRkcNOsRyYg` (primary event evidence): [[youtube-kRkcNOsRyYg]], [[youtube-kRkcNOsRyYg-transcript]], [[youtube-kRkcNOsRyYg-slides]]
- `youtube-B9h9ovW5H9U` — 2,859 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-B9h9ovW5H9U`: graph, context, data, create, traces, back, little, decision.
- Slide-derived themes for `youtube-B9h9ovW5H9U`: context, graphs, information, required, accurate, answer, graph, started.
- Evidence links for `youtube-B9h9ovW5H9U` (supporting context only): [[youtube-B9h9ovW5H9U]], [[youtube-B9h9ovW5H9U-transcript]], [[youtube-B9h9ovW5H9U-slides]], [[youtube-B9h9ovW5H9U-dense-slides]], [[youtube-B9h9ovW5H9U-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
