---
title: "Your Moat Is Your Data Model"
category: "talks"
date: "2026-07-01"
time: "11:40am-12:00pm"
track: "Graphs"
room: "Track 5"
speakers: ["Mike Phipps"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
---

# Your Moat Is Your Data Model

## Official Schedule Context
- Date/time: 2026-07-01 · 11:40am-12:00pm
- Track/room: Graphs · Track 5
- Speaker(s): Mike Phipps
- Session type/status: sponsor · confirmed

## Official Description
Every enterprise AI team faces the same strategic question: where in the stack should a small team

focus its effort? Models, frontends, and agent frameworks evolve rapidly and are increasingly

commoditized. But regardless of how these layers mature, AI in enterprise settings remains

bottlenecked by the same underlying problem: structured data is siloed across systems of record with

domain-specific schemas, and the unstructured data needed to contextualize it sits in entirely

separate systems, with its own systematic complexities. The durable work is cleaning, curating, and

semantically modeling this data in an AI-first manner so that any client — chat, workflow, or

otherwise — can query across it. That's the moat. At the Gates Foundation, my team built and

deployed our foundation-wide knowledge graph on Neo4j that unifies structured and unstructured data

behind a single MCP server. The graph itself is modeled for agentic consumption: natural hierarchies

are projected as traversable paths rather than flattened tables, and unstructured documents are

semantically chunked, tagged, and mapped to structured entities at ingestion time using AI-driven

ETL. The result is a semantic layer where an agent can express a complex cross-system question as a

concise graph query and receive an accurate answer. This talk is an architectural walkthrough

covering the end-to-end pipeline: AI-based extraction and semantic chunking of unstructured

documents, the agent-first data modeling decisions, design considerations for our MCP server, and

how we handle graph-based retrieval evals. We'll walk through real query sessions showing Claude

interacting with the graph through both chat and workflow integrations. The intended takeaway is a

practical framework for where a small enterprise team's investment compounds — and why that

investment is the data model, not the layers above it.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[mike-phipps]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
