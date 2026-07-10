---
title: "Context Graph Ingest"
category: "harnesses"
status: "seeded"
sourceLabels: ["Official schedule", "Question layer", "Topic synthesis"]
---

# Context Graph Ingest

## Purpose
A harness for turning documents, talks, repositories, profiles, and transcripts into a source-labeled graph that agents can retrieve without losing provenance.

## Observed At AIE
- Context graph, GraphRAG, memory, and retrieval sessions emphasize relationships rather than isolated chunks.
- The wiki already separates official schedule facts, supporting videos, transcripts, OCR, and public source-of-source context.
- Search and memory talks show that source reachability and relationship quality are part of agent performance.

## Recommended Implementation Steps
- Ingest sources by source type and preserve the original file or URL for every claim.
- Extract entities, relationships, and claim snippets into separate reviewable records.
- Score retrieval by whether it returns the right source for the question, not only similar text.
- Keep stale or weak sources reachable but labeled, so agents do not treat every edge equally.
- Promote stable graph patterns into topic pages, evaluations, or playbooks only after review.

## Source Evidence
- [[agent-memory]] - Topic synthesis
- [[agentic-search]] - Topic synthesis
- [[what-context-graph-and-memory-architecture-is-practical]] - Question layer
- [[2026-06-30-gil-feig-why-your-company-needs-a-context-graph-and-how-to-build-it]] - Official schedule
- [[2026-06-29-nyah-macklin-rag-needs-a-map-using-graphrag-to-retrieve-connected-context]] - Official schedule
- [[2026-07-01-daniel-chalef-citation-needed-provenance-for-llm-built-knowledge-graphs]] - Official schedule

## Evidence Boundary
This is a reusable workflow synthesized from the linked conference evidence. Treat it as a recommended implementation pattern, not as a direct quote from any single talk.
