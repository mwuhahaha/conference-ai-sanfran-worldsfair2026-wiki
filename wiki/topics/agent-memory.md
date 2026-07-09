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
- [[youtube-HEFSExa0xl0-slides]] — Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs (11 extracted slide frames)
- [[youtube-4kYl2_mqmnQ-slides]] — I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON (10 extracted slide frames)
- [[youtube-IQkVMvXQKLY-slides]] — Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis (14 extracted slide frames)
- [[youtube-UcYoMg-8-L8-slides]] — 500 people vibe-coded for 30 days. I was one of them. - Sanja Grbic, Automattic (11 extracted slide frames)
- [[youtube-kZsf_Sfm7RU-slides]] — The Missing Layer After Launch - Raphael Kalandadze, Wandero AI (19 extracted slide frames)
- [[youtube-2IxD9OB3XuQ-slides]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI (24 extracted slide frames)
- [[youtube-vljxQZfJ9wY-slides]] — Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs (12 extracted slide frames)

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
- [[youtube-4kYl2_mqmnQ]] — I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON
- [[youtube-EcqMYoIV57A]] — Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo
- [[youtube-B9h9ovW5H9U]] — Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j
- [[youtube-TUnPNY4E2fw]] — Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI
- [[youtube-UNzCG3lw6O0]] — Building Great Agent Skills: The Missing Manual
- [[youtube-zKk7sDMGDEQ]] — Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer
- [[youtube-XovaGv4f39A]] — When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis
- [[youtube-jVjt-2g8NMY]] — A Genius With Amnesia - Victor Savkin, Nx
- [[youtube-UPwGaM2MKHY]] — The Log Is The Agent - Ishaan Sehgal, Omnara
- [[youtube-LrGCT7G_rU8]] — Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon
- [[youtube-CLttOU7n6sI]] — Respect The Process - Andrew Dumit, Watershed Technology Inc.
- [[youtube-Jx4ZFEAq6bY]] — User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch
- [[youtube-r305-aQTaU0]] — Text Diffusion — Brendan O’Donoghue, Google DeepMind
- [[youtube-spNAUEgq_A8]] — The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents
- [[youtube-IJXjTLPzvAU]] — The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen
- [[youtube-sAOBXCDiDOs]] — MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc
- [[youtube-YYH0DMQr30A]] — Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel
- [[youtube-qlHaO6laBlM]] — Shipping Production AI Inside Government — William Tarr, Ministry of Justice (DO NOT PUBLISH)

### Quote signals
- “And today, I'm going to tell you about our research project, which is called Road to 5 million sequence length, breaking memory barriers in context parallelism.” — [[youtube-TUnPNY4E2fw]]
- “Um to do that all effectively, you need to make sure that the models are able to process that context and work with it correctly at the training time.” — [[youtube-TUnPNY4E2fw]]
- “This approach would look something like "cache augmented generation" (CAG), where we use a model with a large context window, load the documents into the context, and cache the context by storing the model's KB matrix.” — [[youtube-XovaGv4f39A]]
- “Uh as you continue scaling your context, your memory keeps growing linearly, which is not as bad, but still pretty difficult to deal with, unless you apply a range of specific techniques.” — [[youtube-TUnPNY4E2fw]]
- “I'm on a mission to solve knowledge representation when all context matters.” — [[youtube-XovaGv4f39A]]
- “And so, to kind of think actually about what a context graph is, we need to ask ourselves, "Would you agents really be accurate?" Right?” — [[youtube-B9h9ovW5H9U]]
- “And then context, policies that are um in different reasoning by AI that records memory, but um by employees and and past humans that have made decisions.” — [[youtube-B9h9ovW5H9U]]
- “Um But yeah, that's a good point and then in the create context graph, we're still working on how you would write um new decision traces.” — [[youtube-B9h9ovW5H9U]]

## Source-Derived Enrichment
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

### Talk Evidence
- [[2026-06-29-anders-swanson-from-context-to-memory-your-agents-need-a-real-memory-layer|From Context to Memory: Your Agents Need a Real Memory Layer]]
- [[2026-06-30-stefania-druga-memory-harnesses-for-long-running-research-agents|Memory Harnesses for Long-Running Research Agents]]
- [[2026-06-30-prukalpa-sankar-wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents|WTF Is the Context Layer? The Missing Infrastructure for Production Agents]]
- [[2026-06-30-elizabeth-fuentes-leone-the-infinite-context-window-is-a-myth-context-engineering-for-ai-agents|The Infinite Context Window Is a Myth: Context Engineering for AI Agents]]
- [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens|CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens]]
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one|Video Has No Memory. Here's How We Built One.]]
- [[2026-06-29-ignacio-martinez-total-recall-agent-memory-and-harness-engineering|Total Recall: Agent Memory and Harness Engineering]]
- [[2026-06-29-louis-fran-ois-bouchard-context-engineering-in-2026-compaction-memory-and-cost|Context Engineering in 2026: Compaction, Memory & Cost]]
- [[2026-06-30-anant-srivastava-prompt-memory-weights-the-architecture-decisions-most-ai-teams-make-by-accident|Prompt, Memory, Weights: The Architecture Decisions Most AI Teams Make by Accident]]
- [[2026-06-30-shlok-khemani-lessons-from-studying-every-memory-system|Lessons from Studying Every Memory System]]

### Slide And Transcript Signals
- `youtube-wNH3q9pqn0U` — 10 slide-derived text signals
  - Slide-derived themes: solution, water, growth, crystal, salt, input, sources, services.
  - Evidence links: [[youtube-wNH3q9pqn0U]], [[youtube-wNH3q9pqn0U-slides]], [[youtube-wNH3q9pqn0U-dense-slides]], [[youtube-wNH3q9pqn0U-reconstructed-slides]]
- `youtube-eW_vxrjvERk` — 10 slide-derived text signals
  - Slide-derived themes: context, slack, knowledge, enhance, relevance, domain, alternatives, considered.
  - Evidence links: [[youtube-eW_vxrjvERk]], [[youtube-eW_vxrjvERk-slides]], [[youtube-eW_vxrjvERk-dense-slides]], [[youtube-eW_vxrjvERk-reconstructed-slides]]
- `youtube-I2cbIws9j10` — 91,792 transcript words; 4 slide-derived text signals
  - Transcript signals: code, model, back, system, well, first, today, even.
  - Slide-derived themes: choosing, model, quality, dominates, agentic, capabilities, customization, support.
  - Evidence links: [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
- `youtube-ZRM_TfEZcIo` — 9 slide-derived text signals
  - Slide-derived themes: obsidian, plus, notion, google, drive, growing, files, month.
  - Evidence links: [[youtube-ZRM_TfEZcIo]], [[youtube-ZRM_TfEZcIo-slides]], [[youtube-ZRM_TfEZcIo-dense-slides]], [[youtube-ZRM_TfEZcIo-reconstructed-slides]]
