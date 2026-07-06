---
title: "Agentic Search"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---

# Agentic Search

## Synopsis
Agentic search is retrieval where an AI system actively plans, queries, follows leads, compares sources, and decides when it has enough evidence. It goes beyond one-shot RAG by treating search as an iterative reasoning and tool-use process.

## Origin And Context
It combines web search, enterprise search, information retrieval, RAG, semantic search, BM25, vector databases, knowledge graphs, and research-agent workflows. Agents add query reformulation, source triage, multi-hop exploration, and evidence synthesis.

## Why It Matters
Many tasks fail because the agent either retrieves the wrong context or stops too early. Agentic search improves coverage, reduces hallucination, and helps systems expose the evidence behind an answer.

## How To Use It
Define the question, retrieve broadly, rerank by task relevance, inspect primary sources, track claims and citations, and loop when evidence conflicts or gaps remain. Use hybrid retrieval and structured indexes where pure vector search misses exact terms or relationships.

## Where It Is Useful
It is useful in research, support knowledge bases, compliance review, code search, enterprise assistants, competitive intelligence, and document-heavy operations.

## When To Use It
Use agentic search when answers require multiple sources, fresh evidence, exact facts, or cross-document reasoning. Simple lookup or direct database queries are better for narrow deterministic questions.

## Active Use Cases
- Research agents that cite and compare sources.
- Hybrid RAG over documents, SQL, UI telemetry, and web data.
- Semantic code retrieval for coding agents.
- Enterprise knowledge agents with source-grounded answers.

## Related Slide Decks
- [[youtube-aHhB3sjGjkI-slides]] — Agents Building Agents - Alfonso Graziano, Nearform (24 extracted slide frames)
- [[youtube-jVjt-2g8NMY-slides]] — A Genius With Amnesia - Victor Savkin, Nx (19 extracted slide frames)

## Related Scheduled Sessions

## Transcript And Resource Support
### Transcript-backed resources
- [[youtube-UM6sFg_jdlE]] — RAG is dead, right?? — Kuba Rogut, Turbopuffer
- [[youtube-Akm1sqvWG4A]] — Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy
- [[youtube-zKk7sDMGDEQ]] — Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer
- [[youtube-T0HhO4YtTfE]] — AI System Design: From Idea to Production - Apoorva Joshi, MongoDB
- [[youtube-OXMMN-XbxwA]] — Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc
- [[youtube-htM02KMNZnk]] — WF2026: Software Factories & Keynotes ft. Microsoft, OpenAI, OpenClaw, Z.ai (GLM), MiniMax, HF
- [[youtube-wFTVEDYVJT0]] — Building Agents with Amazon Nova Act and MCP - Du'An Lightfoot, Amazon (Full Workshop)
- [[youtube--x5GEVnkuRw]] — Structuring the Unstructured - Cedric Clyburn, Red Hat
- [[youtube-vh2VGuQ3zhY]] — The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica
- [[youtube-Jx4ZFEAq6bY]] — User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch
- [[youtube-dRmWYHuIJxM]] — We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco
- [[youtube-XovaGv4f39A]] — When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis
- [[youtube-btxGmN8RvNU]] — Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data
- [[youtube-iNkFlCiij0U]] — The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI
- [[youtube-EcqMYoIV57A]] — Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo
- [[youtube-B9h9ovW5H9U]] — Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j
- [[youtube-QuuIywMG4s8]] — Evals Are Broken, Use Them Anyway — Ara Khan, Cline
- [[youtube-zMiSRliEzv4]] — Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog

### Quote signals
- “And what I Turbo puffer what we think this actually means, you know if you break down rag into retrieval augmented generation, you know retrieval is not just vector search.” — [[youtube-UM6sFg_jdlE]]
- “Um So what we're finding now is that a lot of people are no longer doing the simple rag you know the the Twitter quote unquote rag of just doing vector search once and throwing it into the context windows.” — [[youtube-UM6sFg_jdlE]]
- “So you know not not a public benchmark but you can trust the numbers they give us.” — [[youtube-UM6sFg_jdlE]]
