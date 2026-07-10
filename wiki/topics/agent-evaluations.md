---
title: "Agent Evaluations"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---
# Agent Evaluations

## Synopsis
Agent evaluations are the measurement layer for systems that plan, call tools, write code, retrieve context, or take actions over time. They combine offline tests, production traces, human review, model-as-judge scoring, regression suites, and task-specific rubrics so teams can tell whether an agent is actually improving rather than merely sounding better.

## Origin And Context
The practice grows out of software testing, information-retrieval benchmarks, ML evaluation, and LLM prompt evaluation. Agentic systems made the problem harder because success depends on multi-step behavior: tool choice, state handling, recovery, cost, latency, safety, and final task outcome.

## Why It Matters
Without evaluations, agent teams cannot safely change prompts, models, tools, routing, memory policies, or autonomy levels. Evals turn vague quality complaints into visible failure modes and make it possible to ship agents with rollback criteria, measurable acceptance thresholds, and a shared language for product and engineering decisions.

## How To Use It
Start with real traces and representative tasks. Define the outcome that matters, add rubrics for intermediate behavior, keep golden examples for regressions, and separate fast pre-merge checks from slower production audits. Use model judges only when their decisions are calibrated against human review, and track cost, latency, and failure categories alongside quality.

## Where It Is Useful
Evaluations are useful in coding agents, support agents, research agents, data agents, voice agents, retrieval systems, and any workflow where the agent can take a plausible but wrong path. They are especially valuable where correctness, trust, or operational cost matters.

## When To Use It
Use evals before launching, whenever prompts or models change, when adding new tools, after incidents, and when expanding an agent into a new user segment or task family. Lightweight evals should run continuously; deeper reviews should run before major releases.

## Active Use Cases
- Regression tests for prompt, model, and tool changes.
- Production trace review for agent reliability and cost drift.
- Benchmarking coding agents, retrieval agents, and long-horizon workflows.
- Reward-signal generation for continual learning and fine-tuning loops.

## Related Slide Decks
- [[youtube-4kYl2_mqmnQ-slides]] — I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON (10 extracted slide frames)
- [[youtube-IQkVMvXQKLY-slides]] — Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis (14 extracted slide frames)
- [[youtube-1IdzkRVmWAA-slides]] — How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI (5 extracted slide frames)
- [[youtube-CLttOU7n6sI-slides]] — Respect The Process - Andrew Dumit, Watershed Technology Inc. (16 extracted slide frames)
- [[youtube-Rx8f05JI_WA-slides]] — SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI (10 extracted slide frames)
- [[youtube-2IxD9OB3XuQ-slides]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI (24 extracted slide frames)
- [[youtube-vljxQZfJ9wY-slides]] — Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs (12 extracted slide frames)

## Related Scheduled Sessions
- [[2026-06-30-maor-bril-evaling-video-slop]] — Evaling Video Slop; [[maor-bril|Maor Bril]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Evals; official schedule)
- [[2026-06-29-laurie-voss-from-vibes-to-production-evaluating-and-shipping-ai-agents-that-work-101]] — From Vibes to Production: Evaluating and Shipping AI Agents That Work 101; [[laurie-voss|Laurie Voss]] (Day 1 — Workshop Day · 9:00am-11:00am · Track 1; official schedule)
- [[2026-06-29-laurie-voss-from-vibes-to-production-evaluating-and-shipping-ai-agents-that-work-201]] — From Vibes to Production: Evaluating and Shipping AI Agents That Work 201; [[laurie-voss|Laurie Voss]] (Day 1 — Workshop Day · 2:20pm-4:20pm · Track 1; official schedule)
- [[2026-06-30-chris-souza-model-whisperers-how-evals-and-prompts-shape-agent-behavior]] — Model Whisperers: How Evals and Prompts Shape Agent Behavior; [[chris-souza|Chris Souza]], [[preetika-bhateja|Preetika Bhateja]], [[daniel-bump|Daniel Bump]] (Day 3 — Session Day 2 · 1:30pm-1:50pm · Evals; official schedule)
- [[2026-06-29-tejas-kumar-evals-in-ai-a-deep-dive]] — Evals in AI: A Deep Dive; [[tejas-kumar|Tejas Kumar]] (Day 1 — Workshop Day · 12:10pm-1:10pm · Workshops Day 1; official schedule)
- [[2026-06-29-wolfram-ravenwolf-from-zero-to-leaderboard-building-an-end-to-end-ai-agent-evaluation-pipeline]] — From Zero to Leaderboard: Building an End-to-End AI Agent Evaluation Pipeline; [[wolfram-ravenwolf|Wolfram Ravenwolf]] (Day 1 — Workshop Day · 12:10pm-1:10pm · Workshops Day 1; official schedule)
- [[2026-06-30-soumya-gupta-building-closed-loop-evals-for-a-multimodal-agent-at-uber-scale]] — Building Closed-Loop Evals for a Multimodal Agent at Uber Scale; [[soumya-gupta|Soumya Gupta]], [[jai-chopra|Jai Chopra]] (Day 3 — Session Day 2 · 11:40am-12:00pm · Evals; official schedule)
- [[2026-06-30-rustem-feyzkhanov-from-agent-traces-to-agent-simulations-the-next-era-of-agent-evaluation]] — From Agent Traces to Agent Simulations: The next era of agent evaluation; [[rustem-feyzkhanov|Rustem Feyzkhanov]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · Evals; official schedule)
- [[2026-06-30-akele-reed-evals-driven-development-engineering-a-mental-health-ai-coach-ethically-and-safely]] — Evals Driven-Development: Engineering a Mental Health AI Coach Ethically & Safely; [[akele-reed|Akele Reed]], [[dave-revere|Dave Revere]], [[doug-keller|Doug Keller]] (Day 3 — Session Day 2 · 2:50pm-3:10pm · Evals; official schedule)
- [[2026-06-29-nachiket-paranjape-ai-evals-platform-for-cross-functional-teams-at-scale]] — AI Evals Platform for Cross-Functional Teams at Scale; [[nachiket-paranjape|Nachiket Paranjape]], [[swaroop-chitlur-haridas|Swaroop Chitlur Haridas]] (Day 2 — Session Day 1 · 1:55pm-2:15pm · AI-Native Enterprises; official schedule)
- [[2026-06-29-ari-morcos-data-quality-is-the-compute-multiplier]] — Data Quality is the Compute Multiplier; [[ari-morcos|Ari Morcos]] (Day 2 — Session Day 1 · 10:45am-11:05am · Data Quality; official schedule)
- [[2026-06-30-laurie-voss-evals-track-intro]] — Evals Track Intro; [[laurie-voss|Laurie Voss]], [[aparna-dhinakaran|Aparna Dhinakaran]] (Day 3 — Session Day 2 · 10:25am-10:30am · Autoresearch; related YouTube resource; via [[youtube-Xfl50508LZM]])
- [[2026-06-30-parth-asawa-beyond-static-intelligence-evaluating-continual-learning]] — Beyond Static Intelligence: Evaluating Continual Learning; [[parth-asawa|Parth Asawa]] (Day 3 — Session Day 2 · 10:45am-11:05am · Memory & Continual Learning; official schedule)
- [[2026-06-30-philipp-schmid-don-t-ship-skills-without-evals]] — Don't Ship Skills Without Evals; [[philipp-schmid|Philipp Schmid]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Evals; official schedule)
- [[2026-06-30-laurie-voss-the-death-of-the-code-review]] — The Death of the Code Review; [[laurie-voss|Laurie Voss]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · AI Architects: Tokenmaxxing; related YouTube resource; via [[youtube-Xfl50508LZM]])
- [[2026-06-30-laurie-voss-how-long-can-your-skills-be-before-your-agent-forgets-what-you-told-it]] — How long can your skills be before your agent forgets what you told it?; [[laurie-voss|Laurie Voss]] (Day 3 — Session Day 2 · 1:30pm-1:50pm · Context Engineering; related YouTube resource; via [[youtube-Xfl50508LZM]])
- [[2026-06-29-ameya-bhatawdekar-your-agent-evolved-your-evals-didn-t]] — Your Agent Evolved. Your Evals Didn't.; [[ameya-bhatawdekar|Ameya Bhatawdekar]] (Day 2 — Session Day 1 · 11:10am-11:30am · AI Architects: Show my Workflow; official schedule)
- [[2026-06-30-lukas-petersson-vending-bench-long-horizon-agent-evals-for-a-simulated-vending-business]] — Vending-Bench: Long-Horizon Agent Evals for a Simulated Vending Business; [[lukas-petersson|Lukas Petersson]] (Day 3 — Session Day 2 · 10:45am-11:05am · Evals; official schedule)
- [[2026-07-01-ashok-chandrasekar-are-llm-performance-benchmarks-reliable]] — Are LLM Performance Benchmarks Reliable?; [[ashok-chandrasekar|Ashok Chandrasekar]], [[jason-kramberger|Jason Kramberger]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Inference; official schedule)
- [[2026-07-01-session-vector-isn-t-enough-hybrid-search-and-retrieval-for-ai-engineers]] — Vector Isn't Enough: Hybrid Search & Retrieval for AI Engineers; [[jeff-vestal|Jeff Vestal]] (Day 1 — Workshop Day · 2:20pm-4:20pm · Track 7; official schedule)
- [[2026-06-29-jess-wang-agentic-vs-vector-search-an-eval-driven-approach-to-coding-agent-performance]] — Agentic vs. Vector Search: An Eval-Driven Approach to Coding Agent Performance; [[jess-wang|Jess Wang]] (Day 2 — Session Day 1 · 11:40am-12:00pm · Expo Stage 2 NW; official schedule)
- [[2026-06-29-simran-arora-can-llms-write-fast-multi-gpu-kernels-we-built-a-benchmark-to-find-out]] — Can LLMs write fast multi-GPU kernels? We built a benchmark to find out.; [[simran-arora|Simran Arora]] (Day 2 — Session Day 1 · 12:05pm-12:25pm · Expo Stage 3 SW; official schedule)
- [[2026-06-30-ali-khial-benchmarks-the-good-the-bad-and-the-ugly]] — Benchmarks: The Good, the Bad, and the Ugly; [[ali-khial|Ali Khial]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Posttraining & Midtraining; official schedule)
- [[2026-06-29-doug-guthrie-advanced-workshop-mastering-ai-observability]] — Advanced workshop: Mastering AI Observability; [[doug-guthrie|Doug Guthrie]] (Day 1 — Workshop Day · 9:00am-11:00am · Track 9; related YouTube resource; via [[youtube-bk0TmxoZlUY]])

## Related People
- [[laurie-voss|Laurie Voss]]
- [[pamela-fox|Pamela Fox]]
- [[fuad-ali|Fuad Ali]]
- [[brendan-rappazzo|Brendan Rappazzo]]
- [[ahmad-osman|Ahmad Osman]]
- [[yuval-belfer|Yuval Belfer]]
- [[harshul-jain|Harshul Jain]]
- [[tanmay-sah|Tanmay Sah]]
- [[filip-makraduli|Filip Makraduli]]
- [[frank-coyle|Frank Coyle]]
- [[maor-bril|Maor Bril]]
- [[chris-souza|Chris Souza]]
- [[preetika-bhateja|Preetika Bhateja]]
- [[daniel-bump|Daniel Bump]]
- [[tejas-kumar|Tejas Kumar]]
- [[wolfram-ravenwolf|Wolfram Ravenwolf]]
- [[soumya-gupta|Soumya Gupta]]
- [[jai-chopra|Jai Chopra]]
- [[rustem-feyzkhanov|Rustem Feyzkhanov]]
- [[akele-reed|Akele Reed]]
- [[dave-revere|Dave Revere]]
- [[doug-keller|Doug Keller]]
- [[nachiket-paranjape|Nachiket Paranjape]]
- [[swaroop-chitlur-haridas|Swaroop Chitlur Haridas]]

## Related Companies
- [[arize-ai|Arize AI]]
- [[google|Google]]
- [[microsoft|Microsoft]]
- [[uber|Uber]]
- [[braintrust|Braintrust]]
- [[meta|Meta]]
- [[towards-ai|Towards AI]]
- [[weights-and-biases-by-coreweave|Weights & Biases by CoreWeave]]
- [[nvidia|NVIDIA]]
- [[ai21|AI21]]
- [[sondermind|SonderMind]]
- [[doordash|DoorDash]]
- [[elastic|Elastic]]
- [[digital-ocean|Digital Ocean]]
- [[arize|Arize]]
- [[turbopuffer|turbopuffer]]
- [[poolside|poolside]]
- [[g2i|G2i]]

## Transcript And Resource Support
### Transcript-backed resources
- [[youtube-Xfl50508LZM]] — Ship Real Agents: Hands-On Evals for Agentic Applications — Laurie Voss, Arize
- [[youtube-bk0TmxoZlUY]] — Evals 101 — Doug Guthrie, Braintrust
- [[youtube-iNkFlCiij0U]] — The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI
- [[youtube-vljxQZfJ9wY]] — Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs
- [[youtube-pSto5YaNGUo]] — The Agentic AI Engineer - Benedikt Sanftl, Mutagent
- [[youtube-hqHC6Z_lXyo]] — 20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna
- [[youtube-YYH0DMQr30A]] — Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel
- [[youtube-aHhB3sjGjkI]] — Agents Building Agents - Alfonso Graziano, Nearform
- [[youtube-2IxD9OB3XuQ]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI
- [[youtube-QuuIywMG4s8]] — Evals Are Broken, Use Them Anyway — Ara Khan, Cline
- [[youtube-ObTPqBGsEbA]] — £85K Burned on a Failed PoC: What Actually Gets Agents to Production — Sandipan Bhaumik, Databricks
- [[youtube-IQkVMvXQKLY]] — Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis
- [[youtube-Rx8f05JI_WA]] — SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI
- [[youtube-T0HhO4YtTfE]] — AI System Design: From Idea to Production - Apoorva Joshi, MongoDB
- [[youtube-htM02KMNZnk]] — WF2026: Software Factories & Keynotes ft. Microsoft, OpenAI, OpenClaw, Z.ai (GLM), MiniMax, HF
- [[youtube-Jx4ZFEAq6bY]] — User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch
- [[youtube-1IdzkRVmWAA]] — How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI
- [[youtube-wcUJWP6WpGM]] — SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius

### Quote signals
- “Uh I had a question on um on how how much evaluation you need to write for uh feature cuz especially when you run against live traces, sometimes the the evaluation can cost more than the actual feature.” — [[youtube-Xfl50508LZM]]
- “One of the key things is it treat memory as reasoning, not as facts, statistics, fact with no context and no history, but reasoning.” — [[youtube-Jx4ZFEAq6bY]]
- “But the problem is that state of the art is a bit a confusing concept and people maybe have different vision on this.” — [[youtube-hqHC6Z_lXyo]]
- “The event outcome becomes a first-class signal in the retrieval re-ranking and not just for retrieval.” — [[youtube-Jx4ZFEAq6bY]]
- “Uh the other thing to call out here is like we already have a lot of companies using brain trust in production today.” — [[youtube-bk0TmxoZlUY]]
- “Um so anyway, so the the title of my talk today is evals are broken and you should use them anyway.” — [[youtube-QuuIywMG4s8]]
- “And lastly, this axis is all about producing more complex work, more representative work, and also nuanced signals that can be used for not just evaluation, but reward signals during training.” — [[youtube-iNkFlCiij0U]]
- “And for the same amount of evaluation, it takes only 7 hours.” — [[youtube-hqHC6Z_lXyo]]

## Source-Derived Enrichment
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

### Talk Evidence
- [[2026-06-30-maor-bril-evaling-video-slop|Evaling Video Slop]]
- [[2026-06-29-laurie-voss-from-vibes-to-production-evaluating-and-shipping-ai-agents-that-work-101|From Vibes to Production: Evaluating and Shipping AI Agents That Work 101]]
- [[2026-06-29-laurie-voss-from-vibes-to-production-evaluating-and-shipping-ai-agents-that-work-201|From Vibes to Production: Evaluating and Shipping AI Agents That Work 201]]
- [[2026-06-30-chris-souza-model-whisperers-how-evals-and-prompts-shape-agent-behavior|Model Whisperers: How Evals and Prompts Shape Agent Behavior]]
- [[2026-06-29-tejas-kumar-evals-in-ai-a-deep-dive|Evals in AI: A Deep Dive]]
- [[2026-06-29-wolfram-ravenwolf-from-zero-to-leaderboard-building-an-end-to-end-ai-agent-evaluation-pipeline|From Zero to Leaderboard: Building an End-to-End AI Agent Evaluation Pipeline]]
- [[2026-06-30-soumya-gupta-building-closed-loop-evals-for-a-multimodal-agent-at-uber-scale|Building Closed-Loop Evals for a Multimodal Agent at Uber Scale]]
- [[2026-06-30-rustem-feyzkhanov-from-agent-traces-to-agent-simulations-the-next-era-of-agent-evaluation|From Agent Traces to Agent Simulations: The next era of agent evaluation]]
- [[2026-06-30-akele-reed-evals-driven-development-engineering-a-mental-health-ai-coach-ethically-and-safely|Evals Driven-Development: Engineering a Mental Health AI Coach Ethically & Safely]]
- [[2026-06-29-nachiket-paranjape-ai-evals-platform-for-cross-functional-teams-at-scale|AI Evals Platform for Cross-Functional Teams at Scale]]

### Slide And Transcript Signals
- `youtube-Xfl50508LZM` — 22,591 transcript words; 6 slide-derived text signals
- Transcript signals for `youtube-Xfl50508LZM`: evals, eval, data, should, judge, output, whether, phoenix.
- Slide-derived themes for `youtube-Xfl50508LZM`: phoenix, prompt, settings, general, detect, regressions, change, compare.
- Evidence links for `youtube-Xfl50508LZM`: [[youtube-Xfl50508LZM]], [[youtube-Xfl50508LZM-transcript]], [[youtube-Xfl50508LZM-slides]], [[youtube-Xfl50508LZM-dense-slides]], [[youtube-Xfl50508LZM-reconstructed-slides]]
- `youtube-C_GG5g38vLU` — 8 slide-derived text signals
- Slide-derived themes for `youtube-C_GG5g38vLU`: model, engineering, future, console, stories, tool, registry, story.
- Evidence links for `youtube-C_GG5g38vLU`: [[youtube-C_GG5g38vLU]], [[youtube-C_GG5g38vLU-slides]], [[youtube-C_GG5g38vLU-dense-slides]], [[youtube-C_GG5g38vLU-reconstructed-slides]]
## Evidence Table
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 53 | Related pages outside the main evidence categories. |
| resources | 19 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 13 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 24 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 2 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 1 | Transcript markdown; check session matching and caption quality. |

## Representative Evidence Links
### Talks
- [[2026-06-30-maor-bril-evaling-video-slop]]
- [[2026-06-29-laurie-voss-from-vibes-to-production-evaluating-and-shipping-ai-agents-that-work-101]]
- [[2026-06-29-laurie-voss-from-vibes-to-production-evaluating-and-shipping-ai-agents-that-work-201]]
- [[2026-06-30-chris-souza-model-whisperers-how-evals-and-prompts-shape-agent-behavior]]
- [[2026-06-29-tejas-kumar-evals-in-ai-a-deep-dive]]
- [[2026-06-29-wolfram-ravenwolf-from-zero-to-leaderboard-building-an-end-to-end-ai-agent-evaluation-pipeline]]

### Resources
- [[youtube-Xfl50508LZM]]
- [[youtube-bk0TmxoZlUY]]
- [[youtube-iNkFlCiij0U]]
- [[youtube-vljxQZfJ9wY]]
- [[youtube-pSto5YaNGUo]]
- [[youtube-hqHC6Z_lXyo]]

### Slides
- [[youtube-4kYl2_mqmnQ-slides]]
- [[youtube-IQkVMvXQKLY-slides]]
- [[youtube-1IdzkRVmWAA-slides]]
- [[youtube-CLttOU7n6sI-slides]]
- [[youtube-Rx8f05JI_WA-slides]]
- [[youtube-2IxD9OB3XuQ-slides]]

### Transcripts
- [[youtube-Xfl50508LZM-transcript]]

### Tools
- [[braintrust]]
- [[arize]]

## Representative Evidence Links
### Talks
- [[2026-06-30-maor-bril-evaling-video-slop]]
- [[2026-06-29-laurie-voss-from-vibes-to-production-evaluating-and-shipping-ai-agents-that-work-101]]
- [[2026-06-29-laurie-voss-from-vibes-to-production-evaluating-and-shipping-ai-agents-that-work-201]]
- [[2026-06-30-chris-souza-model-whisperers-how-evals-and-prompts-shape-agent-behavior]]
- [[2026-06-29-tejas-kumar-evals-in-ai-a-deep-dive]]
- [[2026-06-29-wolfram-ravenwolf-from-zero-to-leaderboard-building-an-end-to-end-ai-agent-evaluation-pipeline]]

### Resources
- [[youtube-Xfl50508LZM]]
- [[youtube-bk0TmxoZlUY]]
- [[youtube-iNkFlCiij0U]]
- [[youtube-vljxQZfJ9wY]]
- [[youtube-pSto5YaNGUo]]
- [[youtube-hqHC6Z_lXyo]]

### Slides
- [[youtube-4kYl2_mqmnQ-slides]]
- [[youtube-IQkVMvXQKLY-slides]]
- [[youtube-1IdzkRVmWAA-slides]]
- [[youtube-CLttOU7n6sI-slides]]
- [[youtube-Rx8f05JI_WA-slides]]
- [[youtube-2IxD9OB3XuQ-slides]]

### Transcripts
- [[youtube-Xfl50508LZM-transcript]]

### Tools
- [[braintrust]]
- [[arize]]

## Representative Evidence Links
### Talks
- [[2026-06-30-maor-bril-evaling-video-slop]]
- [[2026-06-29-laurie-voss-from-vibes-to-production-evaluating-and-shipping-ai-agents-that-work-101]]
- [[2026-06-29-laurie-voss-from-vibes-to-production-evaluating-and-shipping-ai-agents-that-work-201]]
- [[2026-06-30-chris-souza-model-whisperers-how-evals-and-prompts-shape-agent-behavior]]
- [[2026-06-29-tejas-kumar-evals-in-ai-a-deep-dive]]
- [[2026-06-29-wolfram-ravenwolf-from-zero-to-leaderboard-building-an-end-to-end-ai-agent-evaluation-pipeline]]

### Resources
- [[youtube-Xfl50508LZM]]
- [[youtube-bk0TmxoZlUY]]
- [[youtube-iNkFlCiij0U]]
- [[youtube-vljxQZfJ9wY]]
- [[youtube-pSto5YaNGUo]]
- [[youtube-hqHC6Z_lXyo]]

### Slides
- [[youtube-4kYl2_mqmnQ-slides]]
- [[youtube-IQkVMvXQKLY-slides]]
- [[youtube-1IdzkRVmWAA-slides]]
- [[youtube-CLttOU7n6sI-slides]]
- [[youtube-Rx8f05JI_WA-slides]]
- [[youtube-2IxD9OB3XuQ-slides]]

### Transcripts
- [[youtube-Xfl50508LZM-transcript]]

### Tools
- [[braintrust]]
- [[arize]]
