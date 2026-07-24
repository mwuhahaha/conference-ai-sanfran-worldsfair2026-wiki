---
title: "Semantic Infrastructure and Ontology"
category: "topics"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
sourceAssessment:
  schemaVersion: 1
  claimId: claim:9a2b2da3c2a61943d0f85fb7a8f9d8c549192230757b7768ad21ff5697985a36
  subjectId: concept:semantic-infrastructure-and-ontology
  domain: topics page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-24T00:00:00.000000Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-youtube-8G_1-3IO4ZQ
  - source:official-wf26-youtube-RGSFUqzqErE
  - source:official-wf26-youtube-YZQsWVeN3rE
sourceAssessmentBodySha256: sha256:2394d56744123df20aa49e58d8e4ea5b63d5ba6a0a3c50a0b2358636dc227bbf
---
# Semantic Infrastructure and Ontology

## Overview
These talks focus on the semantic layer that lets an organization represent its domain, map concepts to systems of record, and project shared context into agent workflows. The shared idea is explicit structure, while the tradeoff is between expert-designed ontologies and data-driven extension, plus how much of that structure should be exposed as a runtime substrate versus a planning aid.

## Significance
These talks focus on the semantic layer that lets an organization represent its domain, map concepts to systems of record, and project shared context into agent workflows. The shared idea is explicit structure, while the tradeoff is between expert-designed ontologies and data-driven extension, plus how much of that structure should be exposed as a runtime substrate versus a planning aid.

## Applied Use
Use this topic to compare how the linked speakers frame the same problem or technique. Validate applicability in the target system before adopting a talk-derived recommendation.

## Transcript Digest Evidence
This section synthesizes 14 evidence-bound talk topic candidates across at least two talks.

### Cross-Talk Synthesis
These talks focus on the semantic layer that lets an organization represent its domain, map concepts to systems of record, and project shared context into agent workflows. The shared idea is explicit structure, while the tradeoff is between expert-designed ontologies and data-driven extension, plus how much of that structure should be exposed as a runtime substrate versus a planning aid.

### Constituent Talk Evidence
- [[2026-06-29-pablo-castro-on-ai-and-knowledge|On AI and Knowledge]] — How AI systems use organizational and public data to ground agent behavior.
  - Transcript: [[youtube-RGSFUqzqErE-transcript]]
  - Evidence: "So let's start with company grounding. Like at Microsoft, you know, spending time with customers, one of the things we saw early was that whenever you build an agent, you you always have the knowledge you care about for that agent and you'll manage that yourself, but you also need to ground the agent often on the kind of ambient data of your organization, you know, whenever the agent leaves."
- [[2026-06-29-zach-blumenfeld-ai-on-your-lakehouse-context-comes-in-shapes-not-queries|AI on Your Lakehouse: Context Comes in Shapes, Not Queries]] — A metadata graph that acts as a semantic layer over warehouse schemas.
  - Transcript: [[youtube-kRkcNOsRyYg-transcript]]
  - Evidence: "And to build that semantic layer, we're going to use something called Neoarta. Um Neoarta is a labs project."
- [[2026-06-30-prukalpa-sankar-wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents|WTF Is the Context Layer? The Missing Infrastructure for Production Agents]] — A common repository of company knowledge, skills, and retrieval paths shared across agents.
  - Transcript: [[youtube-8G_1-3IO4ZQ-transcript]]
  - Evidence: "All of this goes into this common one place which is this one company brain of sorts, right?"
- [[2026-07-01-alex-bauer-how-juries-and-librarians-can-solve-gtm-s-ai-trust-problem|How Juries and Librarians Can Solve GTM's AI Trust Problem]] — Preparing company facts, capabilities, and personas as reusable reference material before generation.
  - Transcript: [[youtube-YZQsWVeN3rE-transcript]]
  - Evidence: "So, you have to do some scaffolding. And by scaffolding, what I mean is you have to tell it what to know about your business."
- [[2026-07-01-daniel-chalef-citation-needed-provenance-for-llm-built-knowledge-graphs|Citation Needed: Provenance for LLM-Built Knowledge Graphs]] — Projecting a source classification onto all descendant nodes and edges after ingestion.
  - Transcript: [[youtube-H7puB0RwJMM-transcript]]
  - Evidence: "With metadata projection, we can also model classifications that span many different episodes."
- [[2026-07-01-emil-eifrem-thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer|Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer]] — A business-readable graph of concepts and relationships used to model how the organization talks about its domain.
  - Transcript: [[youtube-VGN22pPpb-8-transcript]]
  - Evidence: "probably thanks to Palunteer but also the rise of AI and there's a lot of people that want to make ontologies really complex but the core concepts are actually super simple what are the key concepts in your organization in our banking example customers accounts um debit cards checks transactions and how do they all"
- [[2026-07-01-frank-coyle-why-agentic-systems-need-ontologies|Why Agentic Systems Need Ontologies]] — Formal inference and constraint mechanisms such as domain, range, transitivity, and functional properties.
  - Transcript: [[youtube-Sir59K8ZDPU-transcript]]
  - Evidence: "Or you want to be able to make inference over them. So, for example, there is uh some terms in this technology called RDFS."
- [[2026-07-01-mike-phipps-your-moat-is-your-data-model|Your Moat Is Your Data Model]] — The practice of turning unstructured documents into semantically meaningful graph content at ingestion time.
  - Transcript: [[youtube-jt1Pbr_n6oU-transcript]]
  - Evidence: "So you have [sighs] for different data sets whether it's structured unstructured there's different pre-processing filtering dduplication there's an order to different documents there can be uh inconsistencies across documents those need to be uh handled up front there's extraction so structured field extraction semantic chunking for unstructured documents if you have figures you need"
- [[2026-07-01-omri-bruchim-from-systems-of-record-to-systems-of-context|From Systems of Record to Systems of Context]] — The shift from storing records to building a live layer that explains how work is connected and why decisions were made.
  - Transcript: [[youtube-Btk8wDUVs74-transcript]]
  - Evidence: "What we want to talk today is like take it step further. Uh we want software that actually understand the connection between them."

## Connections
The talk and transcript links in the evidence section are the admitted conference connections for this generated page.

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| resources | 4 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 12 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 10 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| transcripts | 10 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-pablo-castro-on-ai-and-knowledge]]
- [[2026-06-29-zach-blumenfeld-ai-on-your-lakehouse-context-comes-in-shapes-not-queries]]
- [[2026-06-30-prukalpa-sankar-wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents]]
- [[2026-07-01-alex-bauer-how-juries-and-librarians-can-solve-gtm-s-ai-trust-problem]]
- [[2026-07-01-daniel-chalef-citation-needed-provenance-for-llm-built-knowledge-graphs]]
- [[2026-07-01-emil-eifrem-thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer]]

### Resources
- [[youtube-knDDGYHnnSI]]
- [[youtube-B9h9ovW5H9U]]
- [[youtube-T5IMo5ntyhA]]
- [[youtube-xnXqpUW_Kp8]]

### Slides
- [[youtube-knDDGYHnnSI-slides]]
- [[youtube-knDDGYHnnSI-dense-slides]]
- [[youtube-knDDGYHnnSI-reconstructed-slides]]
- [[youtube-B9h9ovW5H9U-slides]]
- [[youtube-B9h9ovW5H9U-dense-slides]]
- [[youtube-B9h9ovW5H9U-reconstructed-slides]]

### Transcripts
- [[youtube-RGSFUqzqErE-transcript]]
- [[youtube-kRkcNOsRyYg-transcript]]
- [[youtube-8G_1-3IO4ZQ-transcript]]
- [[youtube-YZQsWVeN3rE-transcript]]
- [[youtube-H7puB0RwJMM-transcript]]
- [[youtube-VGN22pPpb-8-transcript]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

### Linked Sessions
- [[2026-06-29-pablo-castro-on-ai-and-knowledge|On AI and Knowledge]]
- [[2026-06-29-zach-blumenfeld-ai-on-your-lakehouse-context-comes-in-shapes-not-queries|AI on Your Lakehouse: Context Comes in Shapes, Not Queries]]
- [[2026-06-30-prukalpa-sankar-wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents|WTF Is the Context Layer? The Missing Infrastructure for Production Agents]]
- [[2026-07-01-alex-bauer-how-juries-and-librarians-can-solve-gtm-s-ai-trust-problem|How Juries and Librarians Can Solve GTM's AI Trust Problem]]
- [[2026-07-01-daniel-chalef-citation-needed-provenance-for-llm-built-knowledge-graphs|Citation Needed: Provenance for LLM-Built Knowledge Graphs]]
- [[2026-07-01-emil-eifrem-thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer|Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer]]
- [[2026-07-01-frank-coyle-why-agentic-systems-need-ontologies|Why Agentic Systems Need Ontologies]]
- [[2026-07-01-mike-phipps-your-moat-is-your-data-model|Your Moat Is Your Data Model]]
- [[2026-07-01-omri-bruchim-from-systems-of-record-to-systems-of-context|From Systems of Record to Systems of Context]]
- [[2026-06-29-tereza-t-kov-rise-of-the-software-factory|Rise of the Software Factory]]

### Media Signals
- `youtube-knDDGYHnnSI` — source page linked; role: supporting context only.
- Evidence links for `youtube-knDDGYHnnSI` (supporting context only): [[youtube-knDDGYHnnSI]], [[youtube-knDDGYHnnSI-slides]], [[youtube-knDDGYHnnSI-dense-slides]], [[youtube-knDDGYHnnSI-reconstructed-slides]]
- `youtube-B9h9ovW5H9U` — 2,859 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-B9h9ovW5H9U`: graph, context, data, create, traces, back, little, decision.
- Slide-derived themes for `youtube-B9h9ovW5H9U`: context, graphs, information, required, accurate, answer, graph, started.
- Evidence links for `youtube-B9h9ovW5H9U` (supporting context only): [[youtube-B9h9ovW5H9U]], [[youtube-B9h9ovW5H9U-transcript]], [[youtube-B9h9ovW5H9U-slides]], [[youtube-B9h9ovW5H9U-dense-slides]], [[youtube-B9h9ovW5H9U-reconstructed-slides]]
- `youtube-T5IMo5ntyhA` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-T5IMo5ntyhA`: text, memory, description, financial, goal, type, target, amount.
- Evidence links for `youtube-T5IMo5ntyhA` (supporting context only): [[youtube-T5IMo5ntyhA]], [[youtube-T5IMo5ntyhA-slides]], [[youtube-T5IMo5ntyhA-dense-slides]], [[youtube-T5IMo5ntyhA-reconstructed-slides]]
- `youtube-xnXqpUW_Kp8` — 8 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-xnXqpUW_Kp8`: built, humans, queries, biden, information, traditional, search, engines.
- Evidence links for `youtube-xnXqpUW_Kp8` (supporting context only): [[youtube-xnXqpUW_Kp8]], [[youtube-xnXqpUW_Kp8-slides]], [[youtube-xnXqpUW_Kp8-dense-slides]], [[youtube-xnXqpUW_Kp8-reconstructed-slides]]
## Evidence Boundary
This page is content-derived from official event transcripts. The linked transcript excerpts support presence and attributed framing; they do not independently verify broader claims.
