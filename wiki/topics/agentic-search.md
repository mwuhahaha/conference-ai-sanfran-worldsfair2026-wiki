---
title: Agentic Search
category: topics
sourceLabels:
  - Slide/video-derived supporting context
last_auto_summarized: '2026-07-06T19:56:49.686Z'
---
# Agentic Search

## Synopsis
Agentic search is retrieval run as an active investigation rather than a single lookup. In the World's Fair material, it shows up as the move away from "vector search once and stuff it into context" toward systems that plan queries, combine retrieval modes, inspect source quality, follow missing evidence, and keep a decision trace of what was searched and why.

## Origin And Context
The connected sessions frame agentic search as a convergence of RAG, hybrid retrieval, semantic code search, SQL, UI telemetry, long-context caching, knowledge graphs, web data, and agent evaluation. Turbopuffer's RAG talk argues that retrieval is broader than vector search; Ogilvy's hybrid RAG session adds SQL RRF and UI telemetry; Tesco and Turbopuffer connect the pattern to local code indexes and semantic code retrieval; Neo4j emphasizes decision traces over document dumps; Bright Data focuses on whether an agent actually searched the web in a verifiable way.

## Why It Matters
The linked talks repeatedly point to the same failure mode: agents sound confident while retrieving the wrong evidence, ignoring user signals, overloading the context window, or claiming to have searched without a durable search trail. Agentic search matters here because it turns retrieval into an observable workflow: query choices, source triage, reranking, citations, gaps, conflicts, and stopping criteria can be evaluated instead of hidden inside one prompt.

## How To Use It
Treat search as a loop with state. Start from the user question and available signals, retrieve across the right surfaces, rerank by task relevance, inspect primary or authoritative sources, record claims with citations, and branch when evidence conflicts. Use BM25 or exact search for identifiers and rare terms, vector search for semantic recall, SQL for structured facts, knowledge graphs for relationships, UI telemetry for product context, and cache or long-context strategies only when they improve evidence quality rather than merely adding bulk.

## Where It Is Useful
Agentic search is useful anywhere an answer depends on evidence scattered across multiple systems: research agents comparing sources, enterprise assistants over internal knowledge bases, coding agents searching repositories, compliance workflows correlating documents, product agents turning user signals into pull requests, and support systems that need to explain which logs, tickets, docs, or web pages informed the response.

## When To Use It
Use agentic search when the question is underspecified, evidence is distributed, freshness matters, exact citations are required, or the agent must reconcile conflicting sources. A direct database query, deterministic API call, or simple keyword lookup is still better when the answer lives in one known structured source and the task does not require exploration.

## Active Use Cases
- Research agents that cite and compare sources.
- Hybrid RAG over documents, SQL, UI telemetry, and web data.
- Semantic code retrieval for coding agents.
- Enterprise knowledge agents with source-grounded answers.

## Related Slide Decks
- [[youtube-aHhB3sjGjkI-slides]] — Agents Building Agents - Alfonso Graziano, Nearform (24 extracted slide frames)
- [[youtube-jVjt-2g8NMY-slides]] — A Genius With Amnesia - Victor Savkin, Nx (19 extracted slide frames)

## Related Scheduled Sessions
- [[2026-07-01-session-vector-isn-t-enough-hybrid-search-and-retrieval-for-ai-engineers]] — Vector Isn't Enough: Hybrid Search & Retrieval for AI Engineers; [[jeff-vestal|Jeff Vestal]] (Day 1 — Workshop Day · 2:20pm-4:20pm · Track 7; official schedule)
- [[2026-06-29-jo-kristian-bergum-the-unreasonable-effectiveness-of-bm25-for-agentic-search]] — The unreasonable effectiveness of BM25 for agentic search; [[jo-kristian-bergum|Jo Kristian Bergum]] (Day 2 — Session Day 1 · 11:10am-11:30am · Search & Retrieval; official schedule)
- [[2026-06-29-will-bryk-the-search-engine-for-the-agentic-web]] — The Search Engine for the Agentic Web; [[will-bryk|Will Bryk]] (Day 2 — Session Day 1 · 11:40am-12:00pm · Search & Retrieval; official schedule)
- [[2026-06-29-maximilian-david-rumpf-where-rl-will-take-search]] — Where RL Will Take Search; [[maximilian-david-rumpf|Maximilian-David Rumpf]], [[lotte-seifert|Lotte Seifert]] (Day 2 — Session Day 1 · 2:50pm-3:10pm · Search & Retrieval; official schedule)
- [[2026-06-30-han-xiao-autoresearch-for-dense-retrieval-test-time-compute-with-frozen-embedding-models]] — Autoresearch for Dense Retrieval: Test-Time Compute with Frozen Embedding Models; [[han-xiao|Han Xiao]] (Day 3 — Session Day 2 · 11:10am-11:30am · Autoresearch; official schedule)
- [[2026-06-30-elie-bakouch-the-era-of-auto-research]] — « the era of (auto) research »; [[elie-bakouch|Elie Bakouch]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · Autoresearch; official schedule)
- [[2026-06-30-tim-sweeney-closing-the-loop-an-autonomous-ai-research-agent]] — Closing the Loop: An Autonomous AI Research Agent; [[tim-sweeney|Tim Sweeney]] (Day 3 — Session Day 2 · 1:30pm-1:50pm · Autoresearch; official schedule)
- [[2026-06-29-dhruv-nathawani-teaching-agents-to-search-building-synthetic-training-pipelines-with-nvidia-data-designer]] — Teaching Agents to Search: Building Synthetic Training Pipelines with NVIDIA Data Designer; [[dhruv-nathawani|Dhruv Nathawani]] (Day 1 — Workshop Day · 11:05am-12:05pm · Workshops Day 1; official schedule)
- [[2026-06-30-erina-karati-autoresearch-in-a-multi-agent-ai-village]] — Autoresearch in a Multi-Agent AI Village; [[erina-karati|Erina Karati]], [[arunachalam-manikandan|Arunachalam Manikandan]] (Day 3 — Session Day 2 · 3:45pm-4:05pm · Autoresearch; official schedule)
- [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens]] — CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens; [[stephen-chin|Stephen Chin]] (Day 4 — Session Day 3 · 10:45am-11:05am · Graphs; official schedule)
- [[2026-06-29-zhengyao-jiang-hands-on-autoresearch-cracking-openai-s-parameter-golf]] — Hands-on AutoResearch: Cracking OpenAI's Parameter Golf; [[zhengyao-jiang|Zhengyao Jiang]], [[dixing-xu|Dixing Xu]], [[vayum-arora|Vayum Arora]], [[dhruv-srikanth|Dhruv Srikanth]] (Day 1 — Workshop Day · 2:20pm-4:20pm · Workshops Day 1; official schedule)
- [[2026-06-30-benoit-schillings-research-to-reality-with-google-deepmind]] — Research to Reality with Google DeepMind; [[benoit-schillings|Benoit Schillings]] (Day 3 — Session Day 2 · 10:05am-10:25am · Autoresearch; official schedule)
- [[2026-06-30-richard-socher-first-steps-toward-automated-ai-research]] — First Steps Toward Automated AI Research; [[richard-socher|Richard Socher]] (Day 3 — Session Day 2 · 10:45am-11:05am · Autoresearch; official schedule)
- [[2026-06-30-tejas-bhakta-autoresearch-for-kernels]] — Autoresearch for Kernels; [[tejas-bhakta|Tejas Bhakta]] (Day 3 — Session Day 2 · 2:50pm-3:10pm · Autoresearch; official schedule)
- [[2026-06-30-roland-gavrilescu-autoresearch-in-the-wild]] — Autoresearch in the wild; [[roland-gavrilescu|Roland Gavrilescu]], [[julian-bright|Julian Bright]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Autoresearch; official schedule)
- [[2026-07-01-brendan-rappazzo-alphalab-autonomous-multi-agent-research-across-optimization-domains-with-frontier-llms]] — ALPHALAB: Autonomous Multi-Agent Research Across Optimization Domains with Frontier LLMs; [[brendan-rappazzo|Brendan Rappazzo]] (Day 4 — Session Day 3 · 10:45am-11:05am · AI in Finance; official schedule)
- [[2026-06-29-nyah-macklin-rag-needs-a-map-using-graphrag-to-retrieve-connected-context]] — RAG Needs a Map: Using GraphRAG to Retrieve Connected Context; [[nyah-macklin|Nyah Macklin]] (Day 1 — Workshop Day · 11:05am-12:05pm · Track 2; official schedule)
- [[2026-06-29-jess-wang-agentic-vs-vector-search-an-eval-driven-approach-to-coding-agent-performance]] — Agentic vs. Vector Search: An Eval-Driven Approach to Coding Agent Performance; [[jess-wang|Jess Wang]] (Day 2 — Session Day 1 · 11:40am-12:00pm · Expo Stage 2 NW; official schedule)
- [[2026-06-30-nixon-dinh-the-death-of-keyword-search-and-the-rise-of-agent-readable-catalogs]] — The Death of Keyword Search and the Rise of Agent-Readable Catalogs; [[nixon-dinh|Nixon Dinh]] (Day 3 — Session Day 2 · 11:10am-11:30am · Expo Stage 3; official schedule)
- [[2026-07-01-george-he-everyone-talks-about-document-search-but-what-about-results]] — Everyone talks about document search, but what about results?; [[george-he|George He]] (Day 4 — Session Day 3 · 1:55pm-2:15pm · Expo Stage 4 SE; official schedule)
- [[2026-06-30-stefania-druga-memory-harnesses-for-long-running-research-agents]] — Memory Harnesses for Long-Running Research Agents; [[stefania-druga|Stefania Druga]] (Day 3 — Session Day 2 · 11:40am-12:00pm · Memory & Continual Learning; official schedule)
- [[2026-07-01-zubin-aysola-aria-how-we-built-autoresearch-with-autoresearch]] — ARIA, how we built autoresearch with autoresearch; [[zubin-aysola|Zubin Aysola]] (Day 4 — Session Day 3 · 11:10am-11:30am · Expo Stage 2 NW; official schedule)
- [[2026-06-29-peter-werry-beyond-rag-build-a-relational-context-engine-from-scratch]] — Beyond RAG: Build a Relational Context Engine from Scratch; [[peter-werry|Peter Werry]] (Day 1 — Workshop Day · 12:10pm-1:10pm · Workshops Day 1; official schedule)
- [[2026-06-29-valeria-wu-fon-speech-to-speech-model-research-at-google-deepmind]] — Speech-to-Speech Model Research at Google DeepMind; [[valeria-wu-fon|Valeria Wu Fon]], [[tom-ouyang|Tom Ouyang]] (Day 2 — Session Day 1 · 11:10am-11:30am · Voice & Realtime AI; official schedule)

## Related People
- [[zhengyao-jiang|Zhengyao Jiang]]
- [[charlie-guo|Charlie Guo]]
- [[brandon-waselnuk|Brandon Waselnuk]]
- [[christopher-manning|Christopher Manning]]
- [[kent-c-dodds|Kent C. Dodds]]
- [[abhishek-bhardwaj|Abhishek Bhardwaj]]
- [[jeff-vestal|Jeff Vestal]]
- [[jo-kristian-bergum|Jo Kristian Bergum]]
- [[will-bryk|Will Bryk]]
- [[maximilian-david-rumpf|Maximilian-David Rumpf]]
- [[lotte-seifert|Lotte Seifert]]
- [[han-xiao|Han Xiao]]
- [[elie-bakouch|Elie Bakouch]]
- [[tim-sweeney|Tim Sweeney]]
- [[dhruv-nathawani|Dhruv Nathawani]]
- [[erina-karati|Erina Karati]]
- [[arunachalam-manikandan|Arunachalam Manikandan]]
- [[stephen-chin|Stephen Chin]]
- [[dixing-xu|Dixing Xu]]
- [[vayum-arora|Vayum Arora]]
- [[dhruv-srikanth|Dhruv Srikanth]]
- [[benoit-schillings|Benoit Schillings]]
- [[richard-socher|Richard Socher]]
- [[tejas-bhakta|Tejas Bhakta]]

## Related Companies
- [[nvidia|NVIDIA]]
- [[weco-ai|Weco AI]]
- [[google-deepmind|Google DeepMind]]
- [[openai|OpenAI]]
- [[neo4j|Neo4j]]
- [[bright-data|Bright Data]]
- [[unblocked|Unblocked]]
- [[oracle|Oracle]]
- [[amazon-agi-lab|Amazon AGI Lab]]
- [[elastic|Elastic]]
- [[weights-and-biases-by-coreweave|Weights & Biases by CoreWeave]]
- [[introspection|Introspection]]
- [[exa|Exa]]
- [[turbopuffer|turbopuffer]]
- [[llamaindex|LlamaIndex]]
- [[artificial-analysis|Artificial Analysis]]
- [[prime-intellect|Prime Intellect]]
- [[datologyai|DatologyAI]]

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
