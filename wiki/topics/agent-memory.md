---
title: Agent Memory
category: topics
sourceLabels:
  - Slide/video-derived supporting context
last_auto_summarized: '2026-07-06T19:56:11.553Z'
---
# Agent Memory

## Synopsis
Agent memory is the layer that lets an agent carry the right state across a task instead of treating every prompt as a fresh start. In the World's Fair material, it shows up as several related patterns: long-context training and cache-augmented generation for keeping more source material available, semantic code retrieval for finding the right repository facts, context graphs and decision traces for remembering why choices were made, logs as durable agent state, and skill systems that package reusable procedures for future runs.

## Origin And Context
This topic sits at the intersection of classic AI state management, knowledge representation, retrieval systems, observability, and database-backed application design. The connected sessions sharpen the tradeoff: Max Ryabinin frames long context as a training and systems problem, Luis Romero-Sevilla argues for knowledge representation when all context matters, Zach Blumenfeld pushes beyond documents toward decision traces and context graphs, and Victor Savkin's "A Genius With Amnesia" treats forgotten project context as a practical failure mode for software agents.

## Why It Matters
Memory determines whether an agent can act consistently across multi-step work, codebases, users, and decisions. More context alone is not enough: Nupur Sharma's "Why More Context Makes Your Agent Dumber" and the Orbis cache-augmented generation talk both point to degradation when context is stuffed without structure. The stronger pattern is selective, source-grounded memory: retrieve the right facts, preserve provenance, keep decision history inspectable, and refresh or discard state when it becomes stale.

## How To Use It
Separate working context from durable memory, then decide what each layer is allowed to retain. Store source-backed facts, repository architecture, user preferences, decision traces, logs, artifacts, and evaluation outcomes with timestamps and provenance. Use retrieval keyed to task intent, not just lexical similarity, and combine retrieval with graph or log structures when the agent needs relationships, chronology, or accountability. Add explicit policies for freshness, deletion, permissions, summarization, and OCR/transcript confidence, then test memory behavior with scenarios where stale or overbroad context would cause a wrong action.

## Where It Is Useful
Memory is useful anywhere an agent has to continue work over time: coding agents that need repository history, customer-support agents that need prior case context, enterprise assistants that need decision records, research agents that need source trails, ETL remediation agents that need operational history, and personal productivity systems that must respect user preferences without relearning them every session.

## When To Use It
Use durable memory when repeated interaction, long-horizon work, auditability, or cross-document reasoning matters. Prefer lighter working context for one-shot tasks. Avoid durable memory for sensitive data unless retention and deletion rules are clear, and avoid confident reuse of old state when the cost of asking again is lower than the risk of acting on stale context.

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
- [[2026-06-29-anders-swanson-from-context-to-memory-your-agents-need-a-real-memory-layer]] — From Context to Memory: Your Agents Need a Real Memory Layer; [[anders-swanson|Anders Swanson]] (Day 2 — Session Day 1 · 3:20pm-3:40pm · Expo Stage 2 NW; official schedule)
- [[2026-06-30-stefania-druga-memory-harnesses-for-long-running-research-agents]] — Memory Harnesses for Long-Running Research Agents; [[stefania-druga|Stefania Druga]] (Day 3 — Session Day 2 · 11:40am-12:00pm · Memory & Continual Learning; official schedule)
- [[2026-06-30-prukalpa-sankar-wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents]] — WTF Is the Context Layer? The Missing Infrastructure for Production Agents; [[prukalpa-sankar|Prukalpa Sankar]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Context Engineering; official schedule)
- [[2026-06-30-elizabeth-fuentes-leone-the-infinite-context-window-is-a-myth-context-engineering-for-ai-agents]] — The Infinite Context Window Is a Myth: Context Engineering for AI Agents; [[elizabeth-fuentes-leone|Elizabeth Fuentes Leone]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Expo Stage 3 SW; official schedule)
- [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens]] — CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens; [[stephen-chin|Stephen Chin]] (Day 4 — Session Day 3 · 10:45am-11:05am · Graphs; official schedule)
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one]] — Video Has No Memory. Here's How We Built One.; [[james-le|James Le]] (Day 4 — Session Day 3 · 2:25pm-2:45pm · Graphs; official schedule)
- [[2026-06-29-ignacio-martinez-total-recall-agent-memory-and-harness-engineering]] — Total Recall: Agent Memory and Harness Engineering; [[ignacio-martinez|Ignacio Martinez]] (Day 1 — Workshop Day · 9:00am-11:00am · Workshops Day 1; official schedule)
- [[2026-06-29-louis-fran-ois-bouchard-context-engineering-in-2026-compaction-memory-and-cost]] — Context Engineering in 2026: Compaction, Memory & Cost; [[louis-fran-ois-bouchard|Louis-François Bouchard]], [[samridhi-vaid|Samridhi Vaid]], [[omar-solano|Omar Solano]] (Day 1 — Workshop Day · 2:20pm-4:20pm · Track 6; official schedule)
- [[2026-06-30-anant-srivastava-prompt-memory-weights-the-architecture-decisions-most-ai-teams-make-by-accident]] — Prompt, Memory, Weights: The Architecture Decisions Most AI Teams Make by Accident; [[anant-srivastava|Anant Srivastava]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · Context Engineering; official schedule)
- [[2026-06-30-shlok-khemani-lessons-from-studying-every-memory-system]] — Lessons from Studying Every Memory System; [[shlok-khemani|Shlok Khemani]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Memory & Continual Learning; official schedule)
- [[2026-06-29-yoni-michael-the-data-context-layer-why-data-engineering-agents-need-more-than-code-and-databases]] — The Data Context Layer: Why Data Engineering Agents Need More Than Code and Databases; [[yoni-michael|Yoni Michael]], [[brandon-callender|Brandon Callender]] (Day 1 — Workshop Day · 2:20pm-4:20pm · Track 2; official schedule)
- [[2026-06-30-jack-morris-scaling-compute-on-context]] — Scaling Compute on Context; [[jack-morris|Jack Morris]] (Day 3 — Session Day 2 · 11:40am-12:00pm · Memory & Continual Learning; official schedule)
- [[2026-06-30-brandon-waselnuk-your-agents-lack-context-here-s-how-to-fix-you-re-absolutely-right]] — Your agents lack context: Here's how to fix "You're absolutely right!"; [[brandon-waselnuk|Brandon Waselnuk]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · Context Engineering; official schedule)
- [[2026-06-30-gil-feig-why-your-company-needs-a-context-graph-and-how-to-build-it]] — Why your company needs a context graph, and how to build it; [[gil-feig|Gil Feig]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Expo Stage 3; official schedule)
- [[2026-07-01-omri-bruchim-from-systems-of-record-to-systems-of-context]] — From Systems of Record to Systems of Context; [[omri-bruchim|Omri Bruchim]] (Day 4 — Session Day 3 · 12:05pm-12:25pm · Graphs; official schedule)
- [[2026-07-01-yuchen-fama-kv-cache-aware-routing-and-p-d-disaggregation-on-kubernetes-the-parts-public-benchmarks-don-t-show]] — KV Cache-Aware Routing and P/D Disaggregation on Kubernetes: The Parts Public Benchmarks Don't Show; [[yuchen-fama|Yuchen Fama]], [[ashish-kamra|Ashish Kamra]] (Day 4 — Session Day 3 · 2:50pm-3:10pm · Inference; official schedule)
- [[2026-06-30-rishab-kumar-from-stateless-to-stateful-orchestrating-real-time-voice-and-messaging-agents-with-twilio-and-amazon-bedrock]] — From Stateless to Stateful: Orchestrating Real-Time Voice & Messaging Agents with Twilio and Amazon Bedrock; [[rishab-kumar|Rishab Kumar]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · Expo Stage 2 NW; official schedule)
- [[2026-06-30-omer-primor-the-rise-of-caas-context-as-a-service-for-agentic-ai]] — The Rise of CaaS: Context-as-a-Service for Agentic AI; [[omer-primor|Omer Primor]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Computer Use; official schedule)
- [[2026-06-30-rachna-srivastava-guardians-of-the-state-how-we-built-an-air-gapped-ai-fortress-for-consumer-data]] — Guardians of the State: How We Built an Air-Gapped AI Fortress for Consumer Data; [[rachna-srivastava|Rachna Srivastava]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · AI-Native Enterprises; official schedule)
- [[2026-07-01-brandon-waselnuk-beyond-rag-see-a-relational-context-engine-reduce-token-burn]] — Beyond RAG: See a relational context engine reduce token burn; [[brandon-waselnuk|Brandon Waselnuk]] (Day 4 — Session Day 3 · 11:10am-11:30am · Expo Stage 1 NE; official schedule)
- [[2026-07-01-kay-malcolm-no-memory-no-harness-why-the-database-is-the-last-line-of-defense]] — No Memory, No Harness: Why the Database Is the Last Line of Defense; [[kay-malcolm|Kay Malcolm]] (Day 4 — Session Day 3 · 2:50pm-3:10pm · Harness Engineering; official schedule)
- [[2026-06-30-peter-werry-how-to-generate-mergeable-code-with-a-context-engine]] — How to generate mergeable code with a context engine; [[peter-werry|Peter Werry]] (Day 3 — Session Day 2 · 11:40am-12:00pm · Expo Stage 2 NW; official schedule)
- [[2026-06-29-krishna-prasad-srinivasan-from-scratch-to-sota-training-a-3b-state-space-vision-model-for-1-4-billion-people]] — From Scratch to SOTA: Training a 3B State-Space Vision Model for 1.4 Billion People; [[krishna-prasad-srinivasan|Krishna Prasad Srinivasan]] (Day 2 — Session Day 1 · 3:20pm-3:40pm · Vision & OCR; official schedule)
- [[2026-07-01-karthik-ranganathan-agent-memory-is-a-solved-problem-agent-learning-is-not]] — Agent Memory Is a Solved Problem. Agent Learning Is Not.; [[karthik-ranganathan|Karthik Ranganathan]], [[heather-downing|Heather Downing]] (Day 4 — Session Day 3 · 3:20pm-3:40pm · Expo Stage 1 NE; official schedule)

## Related People
- [[john-lindquist|John Lindquist]]
- [[brandon-waselnuk|Brandon Waselnuk]]
- [[peter-werry|Peter Werry]]
- [[joseph-nelson|Joseph Nelson]]
- [[ahmad-osman|Ahmad Osman]]
- [[ido-salomon|Ido Salomon]]
- [[yuval-belfer|Yuval Belfer]]
- [[harshul-jain|Harshul Jain]]
- [[tanmay-sah|Tanmay Sah]]
- [[christopher-manning|Christopher Manning]]
- [[merve-noyan|Merve Noyan]]
- [[anders-swanson|Anders Swanson]]
- [[stefania-druga|Stefania Druga]]
- [[prukalpa-sankar|Prukalpa Sankar]]
- [[elizabeth-fuentes-leone|Elizabeth Fuentes Leone]]
- [[stephen-chin|Stephen Chin]]
- [[james-le|James Le]]
- [[ignacio-martinez|Ignacio Martinez]]
- [[louis-fran-ois-bouchard|Louis-François Bouchard]]
- [[samridhi-vaid|Samridhi Vaid]]
- [[omar-solano|Omar Solano]]
- [[anant-srivastava|Anant Srivastava]]
- [[shlok-khemani|Shlok Khemani]]
- [[yoni-michael|Yoni Michael]]

## Related Companies
- [[together-ai|Together AI]]
- [[microsoft|Microsoft]]
- [[unblocked|Unblocked]]
- [[neo4j|Neo4j]]
- [[google|Google]]
- [[nvidia|NVIDIA]]
- [[openai|OpenAI]]
- [[oracle|Oracle]]
- [[anthropic|Anthropic]]
- [[towards-ai|Towards AI]]
- [[mcp-apps|MCP Apps]]
- [[ai21|AI21]]
- [[egghead-io|egghead.io]]
- [[typedef|typedef]]
- [[red-hat|Red Hat]]
- [[yugabyte|Yugabyte]]
- [[roboflow|Roboflow]]
- [[meta|Meta]]

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
