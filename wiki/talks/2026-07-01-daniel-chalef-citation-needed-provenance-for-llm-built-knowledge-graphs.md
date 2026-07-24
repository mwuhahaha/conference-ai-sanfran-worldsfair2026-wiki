---
title: "Citation Needed: Provenance for LLM-Built Knowledge Graphs"
category: "talks"
date: "2026-07-01"
time: "3:20pm-3:40pm"
track: "Graphs"
room: "Track 5"
speakers: ["Daniel Chalef"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Graphs"
scheduleRoom: "Track 5"
scheduleLabels: ["Graphs", "Track 5", "sponsor", "confirmed"]
---
# Citation Needed: Provenance for LLM-Built Knowledge Graphs

## Conference Context
- Date/time: 2026-07-01 · 3:20pm-3:40pm
- Track/room: Graphs · Track 5
- Speaker(s): Daniel Chalef
- Session type/status: sponsor · confirmed

- Track: Graphs
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
An LLM doesn't copy facts into your knowledge graph. It synthesizes them: entities merge across sources, and later data invalidates earlier facts. By the time your agent retrieves "patient has a penicillin allergy," the origin — an EHR record, a lab report, or something typed into a chatbot — is gone. This talk covers engineering lineage into a lossy, generative pipeline: episode-to-fact links as structural graph properties, provenance that survives entity resolution, metadata projection (tag a source once; it follows every derived node and edge), and the query semantics of filtering facts by ancestry, including mixed-trust parentage. Deletion is the inverse problem: GDPR erasure propagates back through the same derivation edges. Compliance gets an audit trail; engineers get agents they can debug instead of black boxes.

## Synthesis
### Transcript-Backed Summary
The talk argues that LLM-built context is inherently lossy and non-deterministic, so provenance cannot be recovered reliably after the fact from a simple log or source pointer. The proposed method is to make lineage a first-class property of a graph: keep source episodes verbatim, derive entities and facts through graph relationships, and project metadata so trust tags survive entity merges, contradictions, and downstream derivations. That enables practical outcomes such as veracity checks, debugging, and selective deletion, but it also introduces real cost and latency, so the system has to balance provenance fidelity against production efficiency.

### Key Takeaways
- Build lineage into the graph itself instead of trying to reconstruct it later from logs.
  - Evidence: "So to sum it all up, deriving context is lossy and generative. Lineage needs to be built in to the data structure, engineered into the data structure, which is a graph, not logged afterwards."
- Keep source material verbatim and link every derived artifact back to its source.
  - Evidence: "And in graffiti we keep the sources verbatim and we link everything back everything derived from those sources back to the source."
- Provenance lets agents evaluate whether a fact is trustworthy based on its sources.
  - Evidence: "You can verify a fact based on its sources so you understand veracity. Should I trust this fact?"
- Provenance also makes debugging easier because you can ask why a fact exists and how it was generated.
  - Evidence: "It's easy to debug where something came from. So, why do I have this fact? How was it generated?"
- Any production design needs to account for the cost and latency of building graph artifacts.
  - Evidence: "And so we've put significant effort into reducing cost and latency of generating graph artifacts."

### Claims From The Talk
- The speaker says LLM synthesis can produce outputs that do not appear verbatim in the source inputs, which destroys the original paper trail. (`explicit`)
  - Evidence: "And this output artifact may not appear verbatim in the source inputs. Synthesis often destroys the paper trail of how these outputs were originated."
- He argues that a simple source ID on a fact breaks down in LLM context pipelines because multiple sources can feed the same output. (`explicit`)
  - Evidence: "But with context pipelines run by LLMs, this breaks in several ways. You prompt an LLM with several sources."
- He says entity resolution can merge identities, such as J. Smith and John Smith, into one entity and change how facts are attributed. (`explicit`)
  - Evidence: "Many facts are each synthesized from one or more of the sources. Somebody like J. Smith and John Smith are merged into a single entity, one identity."
- He presents provenance for context stores as a graph problem, where tracing a fact back to its source is a graph walk and merged entities must retain all source links. (`explicit`)
  - Evidence: "Tracing a fact to its source is just a graph walk. So it's pretty simple and easy to map source to fact on the first right but keeping it correct while the graph changes can be really hard when new data uh so for example when two entities merge the merged entity needs to keep all source links from both otherwise we silently drop a source and we lose lineage."
- When new data contradicts an existing fact, the graph should mark the fact invalid and record the source episodes that caused the mutation. (`explicit`)
  - Evidence: "In the rightmost card, a fact is rendered invalid by new data. And in graffiti, an invalid date is added to the mutated edge."
- A tag assigned to an ingested episode should inherit to all downstream entities and facts derived from that episode. (`explicit`)
  - Evidence: "And so on ingestion, we tag the episodes with the EHR tag. All subsequent entities and facts derived from the episode inherit the tag."
- The speaker says the underlying store can expose which parent episodes carry a tag, but the agent must apply the actual business rule for whether a fact counts as verified. (`explicit`)
  - Evidence: "And here graffiti or the underlying store exposes that choice. It exposes which of the episodes have the gra the particular tag, but your agent needs to execute or apply your business rules."
- For deletion requests, a fact should be deleted only if no remaining episodes still support it. (`explicit`)
  - Evidence: "So, the rule is pretty simple here and it's easier to apply because the link exists. A fact is only deleted if no remaining episodes support it."

### Topics Covered
- [[agentic-search|Provenance]] — The need to preserve where synthesized facts came from in LLM-built knowledge graphs.
- [[agentic-search|Lineage graph]] — Keeping source links intact as entities merge, facts mutate, and the graph changes over time.
- [[semantic-infrastructure-and-ontology|Metadata projection]] — Projecting a source classification onto all descendant nodes and edges after ingestion.
- [[agentic-search|Mixed-trust retrieval]] — Applying different trust rules when a fact has multiple parents and mixed-source ancestry.
- **Deletion propagation** — Propagating deletion from source records to derived facts when support disappears.
- [[agent-memory|File-based memory limits]] — The point that file-based memory becomes hard to reason about when lineage matters.
- [[agentic-search|Graph construction cost]] — The overhead of building provenance-aware graph artifacts at scale.
- [[agentic-search|Entity resolution]] — Splitting facts across episodes, entities, and derived artifacts while preserving lineage through entity resolution.

### Tools And Named Systems
- **Graffiti** — The open-source temporal graph framework used as the provenance layer.
- [[zep|Zep]] — The enterprise agent memory infrastructure built on Graffiti.

### Novel Concepts And Methods
- **Graph-walk provenance tracing** — Tracing a derived fact back to its origin by walking graph relationships from fact to source episode.
- **Metadata projection** — Assigning a source tag at ingestion so that all descendant entities and facts inherit the classification.
- **Ancestry-based filtering** — Filtering retrieved facts by ancestry or source tags to enforce a chosen verification policy.
- **Policy-specific parent verification** — Applying different verification rules depending on how many parents a fact has and what trust policy is in force.
- **Support-based deletion propagation** — Removing a fact only after confirming that no surviving parent episodes still justify it.
- **Structured extraction and deconfliction** — Extracting entities, relationships, and candidate facts from an episode, then deduplicating and reconciling them against existing graph state.

### Open Questions
- **How should a graph or retrieval layer represent facts that require different verification rules depending on the business context?** — The same ancestry shape can be safe in one workflow and unsafe in another, so the policy boundary needs to be explicit.
- **How can provenance stay trustworthy when part of the tracing logic lives outside the graph in a separate data structure?** — If some lineage is external, the system still needs a coherent answer for audit and debugging.
- **How can graph construction cost and latency be reduced without losing the provenance guarantees the system depends on?** — The talk makes clear that provenance is useful, but expensive enough to require engineering attention.

### Derived Links And Source Material
- [[youtube-H7puB0RwJMM-transcript]] — dedicated official recording transcript.
- [[youtube-H7puB0RwJMM]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/H7puB0RwJMM--2026-07-01-daniel-chalef-citation-needed-provenance-for-llm-built-knowledge-graphs.json`.

### Speaker Context
- [[daniel-chalef|Daniel Chalef]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[daniel-chalef]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-T5IMo5ntyhA-dense-slides]] (1 viable slide images).
- Related slide/OCR pages:
- [[youtube-T5IMo5ntyhA-dense-slides]]
- [[youtube-T5IMo5ntyhA-reconstructed-slides]]
- [[youtube-T5IMo5ntyhA-slides]]
- Slide-derived terms: `entitytype`, `entityfields.text`, `memory`, `export`, `financial`, `fields`, `debt`, `category`, `benchmark`, `none`, `reflect`, `description`, `user`, `type`, `goal`, `entityfields.float`, `amount`, `high`

## Official YouTube Recording
- [[youtube-H7puB0RwJMM|Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI]] — official AI Engineer YouTube recording published 2026-07-23.
- Evidence status: [[youtube-H7puB0RwJMM-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-H7puB0RwJMM]] - dedicated official event recording.
- [[youtube-H7puB0RwJMM-transcript]] - dedicated official recording transcript.
- [[youtube-T5IMo5ntyhA]] - supporting context; not the exact session recording.

- Source video: `youtube-H7puB0RwJMM`
- Slide deck: [[youtube-H7puB0RwJMM-slides|Slides: Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI]] — 5 visible slide image(s).
![[assets/slides/H7puB0RwJMM/slide-001.jpg]]
![[assets/slides/H7puB0RwJMM/slide-002.jpg]]
![[assets/slides/H7puB0RwJMM/slide-003.jpg]]
- Slide-derived themes for `youtube-H7puB0RwJMM`: track, graphs, provenance, engineering, future, temporal, knowledge, built.
- Source video: `youtube-T5IMo5ntyhA`
- Slide deck: [[youtube-T5IMo5ntyhA-dense-slides|Dense Slides: Stop Using RAG as Memory — Daniel Chalef, Zep]] — slide evidence page.
- Additional slide evidence: [[youtube-T5IMo5ntyhA-slides|Slides: Stop Using RAG as Memory — Daniel Chalef, Zep]], [[youtube-T5IMo5ntyhA-reconstructed-slides|Reconstructed Slides: Stop Using RAG as Memory — Daniel Chalef, Zep]]
- Slide-derived themes for `youtube-T5IMo5ntyhA`: text, memory, description, financial, goal, type, target, amount.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/H7puB0RwJMM.txt` (2,544 words).

## Transcript Markdown
- [[youtube-H7puB0RwJMM-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/H7puB0RwJMM.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-H7puB0RwJMM` — 2,544 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-H7puB0RwJMM`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-H7puB0RwJMM`: fact, graph, data, source, graffiti, facts, provenence, sources.
- Slide-derived themes for `youtube-H7puB0RwJMM`: track, graphs, provenance, engineering, future, temporal, knowledge, built.
- Evidence links for `youtube-H7puB0RwJMM` (primary event evidence): [[youtube-H7puB0RwJMM]], [[youtube-H7puB0RwJMM-transcript]], [[youtube-H7puB0RwJMM-slides]]
- `youtube-T5IMo5ntyhA` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-T5IMo5ntyhA`: text, memory, description, financial, goal, type, target, amount.
- Evidence links for `youtube-T5IMo5ntyhA` (supporting context only): [[youtube-T5IMo5ntyhA]], [[youtube-T5IMo5ntyhA-slides]], [[youtube-T5IMo5ntyhA-dense-slides]], [[youtube-T5IMo5ntyhA-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
