---
title: "Agent Memory"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---

# Agent Memory

## Synopsis
Agent memory is the set of mechanisms that lets an agent carry useful context across steps, sessions, users, repositories, documents, or decisions. It includes short-term working context, long-term stores, cached artifacts, decision traces, vector or graph retrieval, and policies that decide what should be remembered, refreshed, or forgotten.

## Origin And Context
The topic comes from classic AI state management, knowledge representation, retrieval systems, personal assistants, and database-backed application design. The long-context era changed the tradeoff: teams can stuff more into prompts, but still need structured memory so agents can reason over the right facts at the right time.

## Why It Matters
Memory determines whether an agent can act consistently instead of restarting from scratch. It improves personalization, reduces repeated work, supports multi-step workflows, and makes decisions auditable. Poor memory creates stale assumptions, privacy risk, context bloat, and confident mistakes.

## How To Use It
Separate working context from durable memory. Store source-backed facts, decisions, user preferences, and artifacts with timestamps and provenance. Retrieve by task intent, not just lexical similarity. Add policies for freshness, deletion, permissions, and summarization, and test memory behavior with scenario-based evals.

## Where It Is Useful
Memory is useful in coding agents, customer support, research assistants, enterprise knowledge agents, personal productivity tools, and any workflow that spans multiple sessions or documents.

## When To Use It
Use durable memory when repeated interaction or long-horizon work matters. Avoid it for one-shot tasks, sensitive data without clear retention rules, or cases where stale state would be more harmful than asking again.

## Active Use Cases
- Remembering repository architecture and prior implementation decisions.
- Maintaining user preferences and project constraints across sessions.
- Decision-trace retrieval for enterprise workflows.
- Long-context cache and knowledge-graph backed agent workflows.

## Related Slide Decks
- [[youtube-gcseUQJ6Gbg-slides]] — Using OSS models to build AI apps with millions of users — Hassan El Mghari (4 extracted slide frames)
- [[youtube-aHhB3sjGjkI-slides]] — Agents Building Agents - Alfonso Graziano, Nearform (24 extracted slide frames)
- [[youtube-jVjt-2g8NMY-slides]] — A Genius With Amnesia - Victor Savkin, Nx (19 extracted slide frames)
- [[youtube-EcqMYoIV57A-slides]] — Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo (4 extracted slide frames)

## Related Scheduled Sessions
- [[2026-06-30-hassan-el-mghari-the-missing-layer-design-taste-in-ai-agents-stop-letting-your-agents-ship-ugly-uis]] — The Missing Layer: Design Taste in AI Agents // Stop Letting Your Agents Ship Ugly UIs

## Transcript And Resource Support
### Transcript-backed resources
- [[youtube-EcqMYoIV57A]] — Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo
- [[youtube-B9h9ovW5H9U]] — Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j
- [[youtube-TUnPNY4E2fw]] — Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI
- [[youtube-UNzCG3lw6O0]] — Building Great Agent Skills: The Missing Manual
- [[youtube-zKk7sDMGDEQ]] — Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer
- [[youtube-XovaGv4f39A]] — When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis
- [[youtube-jVjt-2g8NMY]] — A Genius With Amnesia - Victor Savkin, Nx
- [[youtube-UPwGaM2MKHY]] — The Log Is The Agent - Ishaan Sehgal, Omnara
- [[youtube-LrGCT7G_rU8]] — Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon
- [[youtube-Jx4ZFEAq6bY]] — User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch
- [[youtube-r305-aQTaU0]] — Text Diffusion — Brendan O’Donoghue, Google DeepMind
- [[youtube-spNAUEgq_A8]] — The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents
- [[youtube-IJXjTLPzvAU]] — The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen
- [[youtube-sAOBXCDiDOs]] — MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc
- [[youtube-YYH0DMQr30A]] — Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel
- [[youtube-htM02KMNZnk]] — WF2026: Software Factories & Keynotes ft. Microsoft, OpenAI, OpenClaw, Z.ai (GLM), MiniMax, HF
- [[youtube-ZD9-4fW2HhM]] — Build Systems, Not Code - Angie Jones, Agentic AI Foundation
- [[youtube-3hXJI2q0Jz8]] — Recursive Coding Agents - Raymond Weitekamp, OpenProse

### Quote signals
- “And today, I'm going to tell you about our research project, which is called Road to 5 million sequence length, breaking memory barriers in context parallelism.” — [[youtube-TUnPNY4E2fw]]
- “Um to do that all effectively, you need to make sure that the models are able to process that context and work with it correctly at the training time.” — [[youtube-TUnPNY4E2fw]]
- “This approach would look something like "cache augmented generation" (CAG), where we use a model with a large context window, load the documents into the context, and cache the context by storing the model's KB matrix.” — [[youtube-XovaGv4f39A]]
- “Uh as you continue scaling your context, your memory keeps growing linearly, which is not as bad, but still pretty difficult to deal with, unless you apply a range of specific techniques.” — [[youtube-TUnPNY4E2fw]]
- “I'm on a mission to solve knowledge representation when all context matters.” — [[youtube-XovaGv4f39A]]
- “And so, to kind of think actually about what a context graph is, we need to ask ourselves, "Would you agents really be accurate?" Right?” — [[youtube-B9h9ovW5H9U]]
- “And then context, policies that are um in different reasoning by AI that records memory, but um by employees and and past humans that have made decisions.” — [[youtube-B9h9ovW5H9U]]
- “Um But yeah, that's a good point and then in the create context graph, we're still working on how you would write um new decision traces.” — [[youtube-B9h9ovW5H9U]]
