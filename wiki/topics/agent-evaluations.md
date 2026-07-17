---
title: "Agent Evaluations"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---
# Agent Evaluations

## Overview
Agent evaluations are the measurement layer for systems that plan, call tools, write code, retrieve context, or take actions over time. They combine offline tests, production traces, human review, model-as-judge scoring, regression suites, and task-specific rubrics so teams can tell whether an agent is actually improving rather than merely sounding better.

## Conference Context
The practice grows out of software testing, information-retrieval benchmarks, ML evaluation, and LLM prompt evaluation. Agentic systems made the problem harder because success depends on multi-step behavior: tool choice, state handling, recovery, cost, latency, safety, and final task outcome.

## Significance
Without evaluations, agent teams cannot safely change prompts, models, tools, routing, memory policies, or autonomy levels. Evals turn vague quality complaints into visible failure modes and make it possible to ship agents with rollback criteria, measurable acceptance thresholds, and a shared language for product and engineering decisions.

## Applied Use
Start with real traces and representative tasks. Define the outcome that matters, add rubrics for intermediate behavior, keep golden examples for regressions, and separate fast pre-merge checks from slower production audits. Use model judges only when their decisions are calibrated against human review, and track cost, latency, and failure categories alongside quality.

Evaluations are useful in coding agents, support agents, research agents, data agents, voice agents, retrieval systems, and any workflow where the agent can take a plausible but wrong path. They are especially valuable where correctness, trust, or operational cost matters.

Use evals before launching, whenever prompts or models change, when adding new tools, after incidents, and when expanding an agent into a new user segment or task family. Lightweight evals should run continuously; deeper reviews should run before major releases.

## Active Use Cases
- Regression tests for prompt, model, and tool changes.
- Production trace review for agent reliability and cost drift.
- Benchmarking coding agents, retrieval agents, and long-horizon workflows.
- Reward-signal generation for continual learning and fine-tuning loops.

## Slide-Derived Scheduled Session Signals
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]] — In Code They Act, In Proof We Trust
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2
- [[2026-06-30-addy-osmani-closing-keynote]] — Closing Keynote
- [[2026-06-30-sean-cai-state-of-data]] — State of Data

## Slide-Derived Supporting Decks
- [[youtube--CnA2lGfymY-slides]] — "I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox (32 extracted slide frames)
- [[youtube-n97BCfyFIvw-slides]] — "The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani (32 extracted slide frames)
- [[youtube-OqM67QG_Ikk-slides]] — From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI (15 extracted slide frames)
- [[youtube-ZSQb5fzRFPw-slides]] —  (17 extracted slide frames)
- [[youtube-ZyIoTOAbRfs-slides]] — State of Data — Sean Cai, Independent / State of Data (10 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

## Connections
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
- [[2026-06-30-parth-asawa-beyond-static-intelligence-evaluating-continual-learning]] — Beyond Static Intelligence: Evaluating Continual Learning; [[parth-asawa|Parth Asawa]] (Day 3 — Session Day 2 · 10:45am-11:05am · Memory & Continual Learning; official schedule)
- [[2026-06-30-philipp-schmid-don-t-ship-skills-without-evals]] — Don't Ship Skills Without Evals; [[philipp-schmid|Philipp Schmid]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Evals; official schedule)
- [[2026-06-29-ameya-bhatawdekar-your-agent-evolved-your-evals-didn-t]] — Your Agent Evolved. Your Evals Didn't.; [[ameya-bhatawdekar|Ameya Bhatawdekar]] (Day 2 — Session Day 1 · 11:10am-11:30am · AI Architects: Show my Workflow; official schedule)
- [[2026-06-30-lukas-petersson-vending-bench-long-horizon-agent-evals-for-a-simulated-vending-business]] — Vending-Bench: Long-Horizon Agent Evals for a Simulated Vending Business; [[lukas-petersson|Lukas Petersson]] (Day 3 — Session Day 2 · 10:45am-11:05am · Evals; official schedule)
- [[2026-07-01-ashok-chandrasekar-are-llm-performance-benchmarks-reliable]] — Are LLM Performance Benchmarks Reliable?; [[ashok-chandrasekar|Ashok Chandrasekar]], [[jason-kramberger|Jason Kramberger]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Inference; official schedule)
- [[2026-07-01-session-vector-isn-t-enough-hybrid-search-and-retrieval-for-ai-engineers]] — Vector Isn't Enough: Hybrid Search & Retrieval for AI Engineers; [[jeff-vestal|Jeff Vestal]] (Day 1 — Workshop Day · 2:20pm-4:20pm · Track 7; official schedule)
- [[2026-06-29-jess-wang-agentic-vs-vector-search-an-eval-driven-approach-to-coding-agent-performance]] — Agentic vs. Vector Search: An Eval-Driven Approach to Coding Agent Performance; [[jess-wang|Jess Wang]] (Day 2 — Session Day 1 · 11:40am-12:00pm · Expo Stage 2 NW; official schedule)
- [[2026-06-29-simran-arora-can-llms-write-fast-multi-gpu-kernels-we-built-a-benchmark-to-find-out]] — Can LLMs write fast multi-GPU kernels? We built a benchmark to find out.; [[simran-arora|Simran Arora]] (Day 2 — Session Day 1 · 12:05pm-12:25pm · Expo Stage 3 SW; official schedule)
- [[2026-06-30-ali-khial-benchmarks-the-good-the-bad-and-the-ugly]] — Benchmarks: The Good, the Bad, and the Ugly; [[ali-khial|Ali Khial]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Posttraining & Midtraining; official schedule)
- [[2026-06-29-felipe-blanes-designing-evals-that-earn-user-trust]] — Designing Evals That Earn User Trust; [[felipe-blanes|Felipe Blanes]] (Day 2 — Session Day 1 · 1:30pm-1:50pm · Expo Stage 3 SW; official schedule)
- [[2026-06-29-nnenna-ndukwe-how-to-build-quality-gates-into-agentic-coding-workflows]] — How to Build Quality Gates into Agentic Coding Workflows; [[nnenna-ndukwe|Nnenna Ndukwe]] (Day 1 — Workshop Day · 11:05am-12:05pm · Workshops Day 1; official schedule)
- [[2026-06-29-will-bond-scaling-code-quality-building-ureview-uber-s-multi-agent-code-review-engine]] — Scaling Code Quality: Building uReview, Uber’s Multi-Agent Code Review Engine; [[will-bond|Will Bond]], [[ameya-ketkar|Ameya Ketkar]] (Day 2 — Session Day 1 · 12:05pm-12:25pm · AI-Native Enterprises; official schedule)
- [[2026-07-01-ross-wollman-benchmarking-vs-code-with-vsc-bench-how-to-measure-agent-performance]] — Benchmarking VS Code with VSC-Bench: How to measure agent performance; [[ross-wollman|Ross Wollman]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Track M; official schedule)

- [[laurie-voss|Laurie Voss]]
- [[pamela-fox|Pamela Fox]]
- [[will-brown|Will Brown]]
- [[fuad-ali|Fuad Ali]]
- [[ahmad-osman|Ahmad Osman]]
- [[brendan-rappazzo|Brendan Rappazzo]]
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

- [[google|Google]]
- [[arize-ai|Arize AI]]
- [[microsoft|Microsoft]]
- [[uber|Uber]]
- [[braintrust|Braintrust]]
- [[towards-ai|Towards AI]]
- [[weights-and-biases-by-coreweave|Weights & Biases by CoreWeave]]
- [[prime-intellect|Prime Intellect]]
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

- [[swaroop-chitlur-haridas|Swaroop Chitlur Haridas]]

- [[laude-institute|Laude Institute]]

- [[2026-06-30-laurie-voss-evals-track-intro]] — Evals Track Intro; [[laurie-voss|Laurie Voss]], [[aparna-dhinakaran|Aparna Dhinakaran]] (Day 3 — Session Day 2 · 10:25am-10:30am · Autoresearch; related YouTube resource; via [[youtube-Xfl50508LZM]])
- [[2026-06-30-laurie-voss-the-death-of-the-code-review]] — The Death of the Code Review; [[laurie-voss|Laurie Voss]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · AI Architects: Tokenmaxxing; related YouTube resource; via [[youtube-Xfl50508LZM]])
- [[2026-06-30-laurie-voss-how-long-can-your-skills-be-before-your-agent-forgets-what-you-told-it]] — How long can your skills be before your agent forgets what you told it?; [[laurie-voss|Laurie Voss]] (Day 3 — Session Day 2 · 1:30pm-1:50pm · Context Engineering; related YouTube resource; via [[youtube-Xfl50508LZM]])
- [[2026-06-29-doug-guthrie-advanced-workshop-mastering-ai-observability]] — Advanced workshop: Mastering AI Observability; [[doug-guthrie|Doug Guthrie]] (Day 1 — Workshop Day · 9:00am-11:00am · Track 9; related YouTube resource; via [[youtube-bk0TmxoZlUY]])

- [[meta|Meta]]

- [[youtube-4kYl2_mqmnQ-slides]] — I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON (10 extracted slide frames)
- [[youtube-IQkVMvXQKLY-slides]] — Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis (14 extracted slide frames)
- [[youtube-1IdzkRVmWAA-slides]] — How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI (5 extracted slide frames)
- [[youtube-CLttOU7n6sI-slides]] — Respect The Process - Andrew Dumit, Watershed Technology Inc. (16 extracted slide frames)
- [[youtube-Rx8f05JI_WA-slides]] — SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI (10 extracted slide frames)
- [[youtube-2IxD9OB3XuQ-slides]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI (24 extracted slide frames)
- [[youtube-vljxQZfJ9wY-slides]] — Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs (12 extracted slide frames)

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 60 | Related pages outside the main evidence categories. |
| resources | 18 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 33 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 33 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 3 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 18 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]]
- [[2026-06-30-addy-osmani-closing-keynote]]
- [[2026-06-30-sean-cai-state-of-data]]
- [[2026-06-30-maor-bril-evaling-video-slop]]

### Resources
- [[youtube-Xfl50508LZM]]
- [[youtube-bk0TmxoZlUY]]
- [[youtube-0vphxNt4wyk]]
- [[youtube-4sX_He5c4sI]]
- [[youtube-Cz4v1WHVyZc]]
- [[youtube-I2cbIws9j10]]

### Slides
- [[youtube--CnA2lGfymY-slides]]
- [[youtube-n97BCfyFIvw-slides]]
- [[youtube-OqM67QG_Ikk-slides]]
- [[youtube-ZSQb5fzRFPw-slides]]
- [[youtube-ZyIoTOAbRfs-slides]]
- [[youtube-4kYl2_mqmnQ-slides]]

### Transcripts
- [[youtube-0vphxNt4wyk-transcript]]
- [[youtube-4sX_He5c4sI-transcript]]
- [[youtube-Cz4v1WHVyZc-transcript]]
- [[youtube-I2cbIws9j10-transcript]]
- [[youtube-V-EDrhIhHzQ-transcript]]
- [[youtube-ZSQb5fzRFPw-transcript]]

### Tools
- [[braintrust]]
- [[prime-intellect]]
- [[arize]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.

### Linked Sessions
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

### Media Signals
- `youtube-0vphxNt4wyk` — 3,965 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-0vphxNt4wyk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-0vphxNt4wyk`: skill, skills, model, should, look, evals, eval, always.
- Slide-derived themes for `youtube-0vphxNt4wyk`: skills, fail, chad, vibe, checks, production, engineering, future.
- Evidence links for `youtube-0vphxNt4wyk` (primary event evidence): [[youtube-0vphxNt4wyk]], [[youtube-0vphxNt4wyk-transcript]], [[youtube-0vphxNt4wyk-slides]]
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-4sX_He5c4sI`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: system, prompt, examples, tools, lots, claude, gets, smarter.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube-Cz4v1WHVyZc` — 2,535 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Cz4v1WHVyZc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Cz4v1WHVyZc`: html, great, hyperframes, output, create, frame, coding, javascript.
- Slide-derived themes for `youtube-Cz4v1WHVyZc`: track, july, most, engineering, future, html, javascript, native.
- Evidence links for `youtube-Cz4v1WHVyZc` (primary event evidence): [[youtube-Cz4v1WHVyZc]], [[youtube-Cz4v1WHVyZc-transcript]], [[youtube-Cz4v1WHVyZc-slides]]
- `youtube-I2cbIws9j10` — 91,792 transcript words; 7 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-I2cbIws9j10`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: context, window, selects, response, facts, retry, coerce, rollback.
- Evidence links for `youtube-I2cbIws9j10` (primary event evidence): [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
- `youtube-V-EDrhIhHzQ` — 10,228 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-V-EDrhIhHzQ`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-V-EDrhIhHzQ`: model, harness, well, doing, environment, training, able, models.
- Slide-derived themes for `youtube-V-EDrhIhHzQ`: engineering, future, prime, intellect, stack, open.
- Evidence links for `youtube-V-EDrhIhHzQ` (primary event evidence): [[youtube-V-EDrhIhHzQ]], [[youtube-V-EDrhIhHzQ-transcript]], [[youtube-V-EDrhIhHzQ-slides]]
- `youtube-ZSQb5fzRFPw` — 2,617 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-ZSQb5fzRFPw`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-ZSQb5fzRFPw`: computer, take, over, driver, background, task, might, sandbox.
- Slide-derived themes for `youtube-ZSQb5fzRFPw`: track, july, fair, computer, operator, loop, wired, model.
- Evidence links for `youtube-ZSQb5fzRFPw` (primary event evidence): [[youtube-ZSQb5fzRFPw]], [[youtube-ZSQb5fzRFPw-transcript]], [[youtube-ZSQb5fzRFPw-slides]]
- `youtube-ZpK5PWX2YRM` — 3,931 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-ZpK5PWX2YRM`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-ZpK5PWX2YRM`: code, okay, read, line, guys, still, loops, engineer.
- Slide-derived themes for `youtube-ZpK5PWX2YRM`: future, software, bigger, than, last, engineering, leadership, july.
- Evidence links for `youtube-ZpK5PWX2YRM` (primary event evidence): [[youtube-ZpK5PWX2YRM]], [[youtube-ZpK5PWX2YRM-transcript]], [[youtube-ZpK5PWX2YRM-slides]]
- `youtube-ZyIoTOAbRfs` — 3,355 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-ZyIoTOAbRfs`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-ZyIoTOAbRfs`: data, model, layer, three, companies, type, real, labs.
- Slide-derived themes for `youtube-ZyIoTOAbRfs`: track, july, data, bottleneck, never, intelligence, ones, human.
- Evidence links for `youtube-ZyIoTOAbRfs` (primary event evidence): [[youtube-ZyIoTOAbRfs]], [[youtube-ZyIoTOAbRfs-transcript]], [[youtube-ZyIoTOAbRfs-slides]]
- `youtube-htM02KMNZnk` — 89,050 transcript words; 4 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-htM02KMNZnk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-htM02KMNZnk`: model, code, models, loop, well, software, first, team.
- Slide-derived themes for `youtube-htM02KMNZnk`: cycles, stacking, loops, tokens, tools, tasks, throughput, many.
- Evidence links for `youtube-htM02KMNZnk` (primary event evidence): [[youtube-htM02KMNZnk]], [[youtube-htM02KMNZnk-transcript]], [[youtube-htM02KMNZnk-slides]], [[youtube-htM02KMNZnk-dense-slides]], [[youtube-htM02KMNZnk-reconstructed-slides]]
- `youtube-iCj_ATyThvc` — 1,795 transcript words; 4 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-iCj_ATyThvc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-iCj_ATyThvc`: research, auto, aiden, human, training, ideas, data, competition.
- Slide-derived themes for `youtube-iCj_ATyThvc`: code, golf, neural, networks, train, best, language, model.
- Evidence links for `youtube-iCj_ATyThvc` (primary event evidence): [[youtube-iCj_ATyThvc]], [[youtube-iCj_ATyThvc-transcript]], [[youtube-iCj_ATyThvc-slides]]
- `youtube-n97BCfyFIvw` — 3,068 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-n97BCfyFIvw`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-n97BCfyFIvw`: code, still, taste, loop, engineering, evidence, system, human.
- Slide-derived themes for `youtube-n97BCfyFIvw`: roles, google, look, across, worth, doing, increasingly, automated.
- Evidence links for `youtube-n97BCfyFIvw` (primary event evidence): [[youtube-n97BCfyFIvw]], [[youtube-n97BCfyFIvw-transcript]], [[youtube-n97BCfyFIvw-slides]]
- `youtube-q4Tr-DknG2M` — 4,039 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-q4Tr-DknG2M`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-q4Tr-DknG2M`: models, model, training, evals, pretty, loop, compute, cursor.
- Slide-derived themes for `youtube-q4Tr-DknG2M`: future, cursor, compute, better, model, anon, pease, days.
- Evidence links for `youtube-q4Tr-DknG2M` (primary event evidence): [[youtube-q4Tr-DknG2M]], [[youtube-q4Tr-DknG2M-transcript]], [[youtube-q4Tr-DknG2M-slides]]
- `youtube-uU5Gv2h8-9g` — 10,417 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-uU5Gv2h8-9g`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-uU5Gv2h8-9g`: code, claude, prompt, been, cloud, model, mode, team.
- Evidence links for `youtube-uU5Gv2h8-9g` (primary event evidence): [[youtube-uU5Gv2h8-9g]], [[youtube-uU5Gv2h8-9g-transcript]], [[youtube-uU5Gv2h8-9g-slides]]
- `youtube-Xfl50508LZM` — 22,591 transcript words; 6 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-Xfl50508LZM`: evals, eval, data, should, judge, output, whether, phoenix.
- Slide-derived themes for `youtube-Xfl50508LZM`: phoenix, prompt, settings, general, detect, regressions, change, compare.
- Evidence links for `youtube-Xfl50508LZM` (supporting context only): [[youtube-Xfl50508LZM]], [[youtube-Xfl50508LZM-transcript]], [[youtube-Xfl50508LZM-slides]], [[youtube-Xfl50508LZM-dense-slides]], [[youtube-Xfl50508LZM-reconstructed-slides]]
- `youtube-bk0TmxoZlUY` — 9,125 transcript words; role: supporting context only.
- Transcript signals for `youtube-bk0TmxoZlUY`: maybe, trust, brain, within, data, scores, eval, application.
- Evidence links for `youtube-bk0TmxoZlUY` (supporting context only): [[youtube-bk0TmxoZlUY]], [[youtube-bk0TmxoZlUY-transcript]], [[youtube-bk0TmxoZlUY-slides]], [[youtube-bk0TmxoZlUY-dense-slides]], [[youtube-bk0TmxoZlUY-reconstructed-slides]]
- `youtube-Rx8f05JI_WA` — 4,329 transcript words; 7 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-Rx8f05JI_WA`: tasks, verifier, task, full, marathon, hours, compiler, tests.
- Slide-derived themes for `youtube-Rx8f05JI_WA`: tasks, task, coding, projects, tokens, stay, coherent, over.
- Evidence links for `youtube-Rx8f05JI_WA` (supporting context only): [[youtube-Rx8f05JI_WA]], [[youtube-Rx8f05JI_WA-transcript]], [[youtube-Rx8f05JI_WA-slides]]
- `youtube-vljxQZfJ9wY` — 1,143 transcript words; 8 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-vljxQZfJ9wY`: evaluation, production, systems, most, model, tool, becomes, infrastructure.
- Slide-derived themes for `youtube-vljxQZfJ9wY`: evaluation, reliability, accuracy, systems, behavior, measuring, beyond, autonomous.
- Evidence links for `youtube-vljxQZfJ9wY` (supporting context only): [[youtube-vljxQZfJ9wY]], [[youtube-vljxQZfJ9wY-transcript]], [[youtube-vljxQZfJ9wY-slides]]
- `youtube-1IdzkRVmWAA` — 6,138 transcript words; role: supporting context only.
- Transcript signals for `youtube-1IdzkRVmWAA`: search, query, tools, queries, tool, retrieval, semantic, chunks.
- Evidence links for `youtube-1IdzkRVmWAA` (supporting context only): [[youtube-1IdzkRVmWAA]], [[youtube-1IdzkRVmWAA-transcript]], [[youtube-1IdzkRVmWAA-slides]]
