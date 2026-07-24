---
title: "Agent Evaluations"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
sourceAssessment:
  schemaVersion: 1
  claimId: claim:00451d7b7f32cc4834ee2f2fd92365bf9371186d268e10fbddc3eaf8dd5768d1
  subjectId: concept:agent-evaluations
  domain: topics page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-24T00:00:00.000000Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-youtube--CnA2lGfymY
  - source:official-wf26-youtube--I5W5QVAT8E
  - source:official-wf26-youtube-0vphxNt4wyk
  - source:official-wf26-youtube-1EZdpEhwmNc
  - source:official-wf26-youtube-2JX6JYyQG4Y
  - source:official-wf26-youtube-9QebvrrY3KY
  - source:official-wf26-youtube-9fubhllmsBU
  - source:official-wf26-youtube-Cz4v1WHVyZc
  - source:official-wf26-youtube-GgLQ02aO-hs
  - source:official-wf26-youtube-OqM67QG_Ikk
  - source:official-wf26-youtube-RGSFUqzqErE
  - source:official-wf26-youtube-V-EDrhIhHzQ
  - source:official-wf26-youtube-VrpEyglYgeU
  - source:official-wf26-youtube-X1kp-ABIIxQ
  - source:official-wf26-youtube-XV2oYi7kojc
  - source:official-wf26-youtube-ZSQb5fzRFPw
  - source:official-wf26-youtube-ZpK5PWX2YRM
  - source:official-wf26-youtube-ZyIoTOAbRfs
  - source:official-wf26-youtube-iCj_ATyThvc
  - source:official-wf26-youtube-n97BCfyFIvw
  - source:official-wf26-youtube-q4Tr-DknG2M
  - source:official-wf26-youtube-uIiA6DquRiE
  - source:official-wf26-youtube-uU5Gv2h8-9g
sourceAssessmentBodySha256: sha256:69627a47652423d79d93c93e75b4772c6050108bba102d30aca00e3bd549a567
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
- [[2026-06-29-dex-horthy-harness-engineering-is-not-enough-why-software-factories-fail]] — Harness Engineering is not Enough: Why Software Factories Fail
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]] — In Code They Act, In Proof We Trust
- [[2026-06-29-lance-martin-claude-for-long-horizon-tasks]] — Claude for long-horizon tasks
- [[2026-06-29-pablo-castro-on-ai-and-knowledge]] — On AI and Knowledge
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2
- [[2026-06-30-addy-osmani-closing-keynote]] — Closing Keynote
- [[2026-06-30-antje-barth-perception-agents]] — Perception Agents
- [[2026-06-30-dan-farrelly-your-agent-architecture-has-a-half-life-of-6-months]] — Your agent architecture has a half-life of 6 months
- [[2026-06-30-francesco-bonacci-computer-use-2-0-agents-just-got-multi-cursor]] — Computer-Use 2.0: Agents Just Got Multi-Cursor
- [[2026-06-30-sean-cai-state-of-data]] — State of Data
- [[2026-07-01-emil-eifrem-thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer]] — Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one]] — Video Has No Memory. Here's How We Built One.
- [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens]] — CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens

## Slide-Derived Supporting Decks
- [[youtube--CnA2lGfymY-slides]] — "I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox (32 extracted slide frames)
- [[youtube-2JX6JYyQG4Y-slides]] — Perception Agents — Antje Barth, Amazon AGI Lab (31 extracted slide frames)
- [[youtube-9QebvrrY3KY-slides]] — Claude for Long-Horizon Tasks — Lance Martin, Anthropic (4 extracted slide frames)
- [[youtube-Ib5GBkD555M-slides]] — Harness Engineering is not Enough: Why Software Factories Fail — Dex Horthy, HumanLayer (32 extracted slide frames)
- [[youtube-il1c1a2FufU-slides]] — Setting Yourself Up for Success — Part 1 — Jason Liu, OpenAI (12 extracted slide frames)
- [[youtube-mOf-PP4mVjA-slides]] — Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs (31 extracted slide frames)
- [[youtube-n97BCfyFIvw-slides]] — "The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani (32 extracted slide frames)
- [[youtube-OqM67QG_Ikk-slides]] — From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI (15 extracted slide frames)
- [[youtube-Q0VkgCyNVUg-slides]] — CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j (22 extracted slide frames)
- [[youtube-RGSFUqzqErE-slides]] — On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft (28 extracted slide frames)
- [[youtube-VGN22pPpb-8-slides]] — Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j (32 extracted slide frames)
- [[youtube-X1kp-ABIIxQ-slides]] — Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest (15 extracted slide frames)
- [[youtube-ZSQb5fzRFPw-slides]] —  (17 extracted slide frames)
- [[youtube-ZyIoTOAbRfs-slides]] — State of Data — Sean Cai, Independent / State of Data (10 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

## Transcript Digest Evidence
This section synthesizes 32 evidence-bound talk topic candidates across at least two talks.

### Cross-Talk Synthesis
Evaluation design that tries to make agent quality measurable, hard to game, and useful for shipping decisions. The talks vary between benchmark design, harness structure, verifiers, and improvement loops, with the main tradeoff being whether the eval emphasizes realism, robustness, or iteration speed.

### Constituent Talk Evidence
- [[2026-06-29-daniel-han-special-topics-in-kernels-rl-reward-hacking-in-agents|Special topics in Kernels, RL, Reward Hacking in Agents]] — Designing benchmarks that resist gaming while remaining easy to check.
  - Transcript: [[youtube-uIiA6DquRiE-transcript]]
  - Evidence: "The first condition is the benchmark must not must not be benchmaxable. Right? How do you make a benchmark that is extremely hard to benchmark, right?"
- [[2026-06-29-dex-horthy-harness-engineering-is-not-enough-why-software-factories-fail|Harness Engineering is not Enough: Why Software Factories Fail]] — Evaluating coding agents and code quality with benchmarks, verifiers, and reward channels.
  - Transcript: [[youtube-Ib5GBkD555M-transcript]]
  - Evidence: "So, we're going to look at these as like what is the future of evaluating code maintainability."
- [[2026-06-29-lance-martin-claude-for-long-horizon-tasks|Claude for long-horizon tasks]] — Shared harnesses with organizational identity, organizational context, and team-wide access.
  - Transcript: [[youtube-9QebvrrY3KY-transcript]]
  - Evidence: "What's interesting about Claude Tag is it is a harness that everyone in the organization has access to and can use."
- [[2026-06-29-lee-robinson-recursive-model-improvement|Recursive Model Improvement]] — Controls and benchmark design choices that prevent models from gaming evaluation results.
  - Transcript: [[youtube-q4Tr-DknG2M-transcript]]
  - Evidence: "So, first off, we would delete the Git history at the start, and we could restore it at the end, so that wouldn't affect the run."
- [[2026-06-29-pablo-castro-on-ai-and-knowledge|On AI and Knowledge]] — Improving agents through evaluation-driven candidate generation and deployment.
  - Transcript: [[youtube-RGSFUqzqErE-transcript]]
  - Evidence: "So we built a component called the agent optimizer that effectively goes through this process and allows you to evaluate a baseline, generate candidates, and then you know, evaluate the new candidates and we have a strong result, then deploy that to production."
- [[2026-06-29-sarah-sachs-notion-s-token-town|Notion's Token Town]] — Judging providers by end-to-end task outcomes rather than by single-call metrics.
  - Transcript: [[youtube--I5W5QVAT8E-transcript]]
  - Evidence: "But if you have expertise in entire web search trajectories, you'll see how it differs. The granularity of this eval is what lets us make the best decisions for our customers because we understand all of the trade-offs on entire trajectories, not just single calls."
- [[2026-06-30-addy-osmani-closing-keynote|Closing Keynote]] — The shift from a final review step to a broader system for routing, verifying, and integrating work.
  - Transcript: [[youtube-n97BCfyFIvw-transcript]]
  - Evidence: "It has to become a whole control system. The second thing to avoid is cognitive surrender."
- [[2026-06-30-antje-barth-perception-agents|Perception Agents]] — The gap between agents that can take actions and agents that can be trusted to finish messy work end to end.
  - Transcript: [[youtube-2JX6JYyQG4Y-transcript]]
  - Evidence: "Now the next hard part is really reliability and without reliability we cannot really build up trust in those systems."
- [[2026-06-30-francesco-bonacci-computer-use-2-0-agents-just-got-multi-cursor|Computer-Use 2.0: Agents Just Got Multi-Cursor]] — Using recorded trajectories to probe whether a model can predict reward or internal state.
  - Transcript: [[youtube-ZSQb5fzRFPw-transcript]]
  - Evidence: "From there we can probe a model asking to predict the reward, the internal state or any other observation of the computer and compare it against the fork."
- [[2026-06-30-philipp-schmid-don-t-ship-skills-without-evals|Don't Ship Skills Without Evals]] — Testing a skill with and without it loaded to measure whether it still adds value.
  - Transcript: [[youtube-0vphxNt4wyk-transcript]]
  - Evidence: "So, run always evals with your skill loaded and without your skill loaded. Only that way you will know when you can retire skill or if a skill is really helpful for your performance."
- [[2026-06-30-sean-cai-state-of-data|State of Data]] — Data derived from real workflows, reasoning traces, and decision sequences rather than only final outputs.
  - Transcript: [[youtube-ZyIoTOAbRfs-transcript]]
  - Evidence: "What is actually available nowadays is process-based data, which is the trajectory, the reasoning trade trace, the sequence of decisions."
- [[2026-06-30-tariq-shaukat-in-the-land-of-ai-agents-the-verifiers-are-king|'In the Land of AI Agents, the Verifiers Are King']] — Using repository knowledge and explicit rules to steer agents before they write code.
  - Transcript: [[youtube-VrpEyglYgeU-transcript]]
  - Evidence: "What we find is critically important is to think about guide as context and constraints and we separate out context and constraints very deliberately because context is you have your code repositories."
- [[2026-06-30-thariq-shihipar-field-guide-to-fable|Field Guide to Fable]] — How to adapt prompting, tools, and harnesses to a new model class with more latent capability.
  - Transcript: [[youtube-9fubhllmsBU-transcript]]
  - Evidence: "And so, what I wanted to do in this talk is give you guys a field guide to Fable, right? How do you work with this new class of models?"
- [[2026-06-30-uri-rolls-training-frontier-models-to-out-think-hackers|Training Frontier Models to Out-Think Hackers]] — Verifying each action in a long exploitation chain with machine-checkable scoring.
  - Transcript: [[youtube-O-CBZ3JtRvo-transcript]]
  - Evidence: "And everything because the tasks are so difficult, everything has a deterministic greater."
- [[2026-06-30-zhengyao-jiang-an-ai-agent-became-the-1-contributor-in-openai-s-hiring-challenge|An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge]] — A competition used as both a benchmark and a hiring filter for small language model training under strict resource limits.
  - Transcript: [[youtube-iCj_ATyThvc-transcript]]
  - Evidence: "This April, OBI ran a hiring challenge, a competition called Parameter Golf. The top contributor was one candidate that they couldn't hire."
- [[2026-07-01-frank-coyle-why-agentic-systems-need-ontologies|Why Agentic Systems Need Ontologies]] — The execution pattern where an LLM proposes a tool action, a stop reason is checked, and the tool result is validated.
  - Transcript: [[youtube-Sir59K8ZDPU-transcript]]
  - Evidence: "So, stop reason means the LLM has stopped for some reason. The The reason here is that it can't do anything, and if the reason is tool use, ah, now it's time."
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one|Video Has No Memory. Here's How We Built One.]] — A deterministic operating model for video understanding that plans tasks, retrieves evidence, and validates outputs.
  - Transcript: [[youtube-mOf-PP4mVjA-transcript]]
  - Evidence: "So what does it look like for for video on a static model right um a model co a single answer it is stateless it start fresh time start fresh each time and doesn't have any constraint so the output is largely based on what the model decide to produce a video worker on the"
- [[2026-07-01-james-russo-html-is-all-agents-need|HTML Is All Agents Need]] — Using skills and evaluation loops to shape model output quality.
  - Transcript: [[youtube-Cz4v1WHVyZc-transcript]]
  - Evidence: "And a big part of this is the skills that we couple with our framework. Our skill is focused on taste and video aspects because the LLMs and agents already know how to write HTML and CSS and JavaScript, we don't have to teach them the language, we just teach them how to create good videos."
- [[2026-07-01-maxime-rivest-the-unreasonable-effectiveness-of-separating-the-task-from-the-model|The Unreasonable Effectiveness of Separating the Task from the Model]] — The interface defined by natural-language instructions, code constraints, and evaluative examples.
  - Transcript: [[youtube-GgLQ02aO-hs-transcript]]
  - Evidence: "Now that you have all of these, you have express fully. You have all these three languages you can put together."
- [[2026-07-01-mike-phipps-your-moat-is-your-data-model|Your Moat Is Your Data Model]] — Using evals to identify ambiguities, missing schema detail, and mismatches with reporting conventions.
  - Transcript: [[youtube-jt1Pbr_n6oU-transcript]]
  - Evidence: "Okay, I've got a couple minutes. I'll kind of speed through this, but the the way eval relate to data modeling is that as you're doing eval, you find you find gaps."
- [[2026-07-01-yohei-nakajima-active-graph-agent-runtime-babyagi-4|Active Graph Agent Runtime (BabyAGI 4)]] — Controlled self-improvement loops that propose changes, test them, and keep only verified gains.
  - Transcript: [[youtube-khVX_BUnEwU-transcript]]
  - Evidence: "Again, I did this on long mem eval. The loop was I think doing about 20 questions, looking at the answering questions, seeing where it failed, trying to self-modify, trying that on 50 different questions, see if the accuracy actually went up, and only if it went up, it would accept it."

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
| resources | 30 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 50 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 54 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 3 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 34 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-dex-horthy-harness-engineering-is-not-enough-why-software-factories-fail]]
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]]
- [[2026-06-29-lance-martin-claude-for-long-horizon-tasks]]
- [[2026-06-29-pablo-castro-on-ai-and-knowledge]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]]

### Resources
- [[youtube-Xfl50508LZM]]
- [[youtube-bk0TmxoZlUY]]
- [[youtube-0vphxNt4wyk]]
- [[youtube-Cz4v1WHVyZc]]
- [[youtube-GgLQ02aO-hs]]
- [[youtube-RGSFUqzqErE]]

### Slides
- [[youtube--CnA2lGfymY-slides]]
- [[youtube-2JX6JYyQG4Y-slides]]
- [[youtube-9QebvrrY3KY-slides]]
- [[youtube-Ib5GBkD555M-slides]]
- [[youtube-il1c1a2FufU-slides]]
- [[youtube-mOf-PP4mVjA-slides]]

### Transcripts
- [[youtube-0vphxNt4wyk-transcript]]
- [[youtube-Cz4v1WHVyZc-transcript]]
- [[youtube-GgLQ02aO-hs-transcript]]
- [[youtube-RGSFUqzqErE-transcript]]
- [[youtube-V-EDrhIhHzQ-transcript]]
- [[youtube-XV2oYi7kojc-transcript]]

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
- `youtube-Cz4v1WHVyZc` — 2,535 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Cz4v1WHVyZc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Cz4v1WHVyZc`: html, great, hyperframes, output, create, frame, coding, javascript.
- Slide-derived themes for `youtube-Cz4v1WHVyZc`: track, july, most, engineering, future, html, javascript, native.
- Evidence links for `youtube-Cz4v1WHVyZc` (primary event evidence): [[youtube-Cz4v1WHVyZc]], [[youtube-Cz4v1WHVyZc-transcript]], [[youtube-Cz4v1WHVyZc-slides]]
- `youtube-GgLQ02aO-hs` — 2,751 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-GgLQ02aO-hs`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-GgLQ02aO-hs`: implementation, solve, dspi, model, should, problem, models, techniques.
- Slide-derived themes for `youtube-GgLQ02aO-hs`: task, effectiveness, separating, unreasonable, model, programs, should, fair.
- Evidence links for `youtube-GgLQ02aO-hs` (primary event evidence): [[youtube-GgLQ02aO-hs]], [[youtube-GgLQ02aO-hs-transcript]], [[youtube-GgLQ02aO-hs-slides]]
- `youtube-RGSFUqzqErE` — 3,081 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-RGSFUqzqErE`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-RGSFUqzqErE`: knowledge, data, retrieval, foundry, whatnot, microsoft, models, give.
- Slide-derived themes for `youtube-RGSFUqzqErE`: fair, engineering, future, bile, microsoft, resolve, knowledge, pablo.
- Evidence links for `youtube-RGSFUqzqErE` (primary event evidence): [[youtube-RGSFUqzqErE]], [[youtube-RGSFUqzqErE-transcript]], [[youtube-RGSFUqzqErE-slides]]
- `youtube-V-EDrhIhHzQ` — 10,228 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-V-EDrhIhHzQ`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-V-EDrhIhHzQ`: model, harness, well, doing, environment, training, able, models.
- Slide-derived themes for `youtube-V-EDrhIhHzQ`: engineering, future, prime, intellect, stack, open.
- Evidence links for `youtube-V-EDrhIhHzQ` (primary event evidence): [[youtube-V-EDrhIhHzQ]], [[youtube-V-EDrhIhHzQ-transcript]], [[youtube-V-EDrhIhHzQ-slides]]
- `youtube-XV2oYi7kojc` — 2,590 transcript words; 3 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-XV2oYi7kojc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-XV2oYi7kojc`: models, billion, hardware, open, model, source, parameter, months.
- Slide-derived themes for `youtube-XV2oYi7kojc`: within, roughly, months, class, intelligence, late, mode, performs.
- Evidence links for `youtube-XV2oYi7kojc` (primary event evidence): [[youtube-XV2oYi7kojc]], [[youtube-XV2oYi7kojc-transcript]], [[youtube-XV2oYi7kojc-slides]]
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
- `youtube-uIiA6DquRiE` — 25,283 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-uIiA6DquRiE`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-uIiA6DquRiE`: model, models, source, open, benchmark, question, okay, accuracy.
- Slide-derived themes for `youtube-uIiA6DquRiE`: smaller, model, high, extra, license, businesses, users, open.
- Evidence links for `youtube-uIiA6DquRiE` (primary event evidence): [[youtube-uIiA6DquRiE]], [[youtube-uIiA6DquRiE-transcript]], [[youtube-uIiA6DquRiE-slides]]
- `youtube-uU5Gv2h8-9g` — 10,417 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-uU5Gv2h8-9g`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-uU5Gv2h8-9g`: code, claude, prompt, been, cloud, model, mode, team.
- Evidence links for `youtube-uU5Gv2h8-9g` (primary event evidence): [[youtube-uU5Gv2h8-9g]], [[youtube-uU5Gv2h8-9g-transcript]], [[youtube-uU5Gv2h8-9g-slides]]
- `youtube--I5W5QVAT8E` — 4,014 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube--I5W5QVAT8E`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube--I5W5QVAT8E`: model, notion, today, customers, product, okay, always, system.
- Slide-derived themes for `youtube--I5W5QVAT8E`: engineering, plan, future, fair, recently, purchased, each, subscription.
- Evidence links for `youtube--I5W5QVAT8E` (primary event evidence): [[youtube--I5W5QVAT8E]], [[youtube--I5W5QVAT8E-transcript]], [[youtube--I5W5QVAT8E-slides]]
- `youtube-1EZdpEhwmNc` — 4,245 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-1EZdpEhwmNc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-1EZdpEhwmNc`: security, data, code, able, find, skill, customers, attacks.
- Slide-derived themes for `youtube-1EZdpEhwmNc`: track, june, security, malicious, engineering, future, pitch, defend.
- Evidence links for `youtube-1EZdpEhwmNc` (primary event evidence): [[youtube-1EZdpEhwmNc]], [[youtube-1EZdpEhwmNc-transcript]], [[youtube-1EZdpEhwmNc-slides]]
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-4sX_He5c4sI`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: lots, examples, stream, starts, july, land, king, chief.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube-9QebvrrY3KY` — 4,450 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-9QebvrrY3KY`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-9QebvrrY3KY`: memory, models, claude, model, context, interesting, harness, important.
- Slide-derived themes for `youtube-9QebvrrY3KY`: generator, lance, martin, member, technical, staff, engineering, future.
- Evidence links for `youtube-9QebvrrY3KY` (primary event evidence): [[youtube-9QebvrrY3KY]], [[youtube-9QebvrrY3KY-transcript]], [[youtube-9QebvrrY3KY-slides]]
- `youtube-I2cbIws9j10` — 91,792 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-I2cbIws9j10`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: choosing, model, quality, dominates, agentic, capabilities, customization, support.
- Evidence links for `youtube-I2cbIws9j10` (primary event evidence): [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
- `youtube-Ib5GBkD555M` — 4,045 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Ib5GBkD555M`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Ib5GBkD555M`: code, review, model, coding, software, stuff, test, better.
- Slide-derived themes for `youtube-Ib5GBkD555M`: software, harness, enough, team, engineering, factories, fail, pierre.
- Evidence links for `youtube-Ib5GBkD555M` (primary event evidence): [[youtube-Ib5GBkD555M]], [[youtube-Ib5GBkD555M-transcript]], [[youtube-Ib5GBkD555M-slides]]
- `youtube-O-CBZ3JtRvo` — 3,557 transcript words; 9 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-O-CBZ3JtRvo`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-O-CBZ3JtRvo`: model, cyber, models, able, reason, been, benchmark, understand.
- Slide-derived themes for `youtube-O-CBZ3JtRvo`: training, models, attackers, engineering, future, track, july, arithmetic.
- Evidence links for `youtube-O-CBZ3JtRvo` (primary event evidence): [[youtube-O-CBZ3JtRvo]], [[youtube-O-CBZ3JtRvo-transcript]], [[youtube-O-CBZ3JtRvo-slides]]
- `youtube-VrpEyglYgeU` — 3,005 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-VrpEyglYgeU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-VrpEyglYgeU`: code, verification, models, loop, still, question, sure, problem.
- Slide-derived themes for `youtube-VrpEyglYgeU`: accuracy, land, king, meters, industry, struggling, slop, coding.
- Evidence links for `youtube-VrpEyglYgeU` (primary event evidence): [[youtube-VrpEyglYgeU]], [[youtube-VrpEyglYgeU-transcript]], [[youtube-VrpEyglYgeU-slides]]
- `youtube-htM02KMNZnk` — 89,050 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-htM02KMNZnk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-htM02KMNZnk`: model, code, models, loop, well, software, first, team.
- Slide-derived themes for `youtube-htM02KMNZnk`: apps, github, copilot, welcome, engineer, fair, single, line.
- Evidence links for `youtube-htM02KMNZnk` (primary event evidence): [[youtube-htM02KMNZnk]], [[youtube-htM02KMNZnk-transcript]], [[youtube-htM02KMNZnk-slides]], [[youtube-htM02KMNZnk-dense-slides]], [[youtube-htM02KMNZnk-reconstructed-slides]]
- `youtube-jt1Pbr_n6oU` — 3,441 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-jt1Pbr_n6oU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-jt1Pbr_n6oU`: data, model, graph, across, structure, chat, part, structured.
- Slide-derived themes for `youtube-jt1Pbr_n6oU`: track, july, fair, intro, defensible, organization, presented, users.
- Evidence links for `youtube-jt1Pbr_n6oU` (primary event evidence): [[youtube-jt1Pbr_n6oU]], [[youtube-jt1Pbr_n6oU-transcript]], [[youtube-jt1Pbr_n6oU-slides]]
- `youtube-mOf-PP4mVjA` — 3,509 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-mOf-PP4mVjA`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-mOf-PP4mVjA`: memory, scene, content, system, across, layer, application, context.
- Slide-derived themes for `youtube-mOf-PP4mVjA`: memory, built, data, incredibly, complex, scale, holistic, understanding.
- Evidence links for `youtube-mOf-PP4mVjA` (primary event evidence): [[youtube-mOf-PP4mVjA]], [[youtube-mOf-PP4mVjA-transcript]], [[youtube-mOf-PP4mVjA-slides]]
- `youtube-Xfl50508LZM` — 22,591 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-Xfl50508LZM`: evals, eval, data, should, judge, output, whether, phoenix.
- Slide-derived themes for `youtube-Xfl50508LZM`: swiss, cheese, talking, setting, tracing, phoenix, paine, theoretical.
- Evidence links for `youtube-Xfl50508LZM` (supporting context only): [[youtube-Xfl50508LZM]], [[youtube-Xfl50508LZM-transcript]], [[youtube-Xfl50508LZM-slides]], [[youtube-Xfl50508LZM-dense-slides]], [[youtube-Xfl50508LZM-reconstructed-slides]]
- `youtube-bk0TmxoZlUY` — 9,125 transcript words; 9 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-bk0TmxoZlUY`: maybe, trust, brain, within, data, scores, eval, application.
- Slide-derived themes for `youtube-bk0TmxoZlUY`: support, leading, teams, netflix, nite, become, core, skill.
- Evidence links for `youtube-bk0TmxoZlUY` (supporting context only): [[youtube-bk0TmxoZlUY]], [[youtube-bk0TmxoZlUY-transcript]], [[youtube-bk0TmxoZlUY-slides]], [[youtube-bk0TmxoZlUY-dense-slides]], [[youtube-bk0TmxoZlUY-reconstructed-slides]]
- `youtube-Rx8f05JI_WA` — 4,329 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-Rx8f05JI_WA`: tasks, verifier, task, full, marathon, hours, compiler, tests.
- Slide-derived themes for `youtube-Rx8f05JI_WA`: tasks, tokens, coding, projects, trial, stay, coherent, over.
- Evidence links for `youtube-Rx8f05JI_WA` (supporting context only): [[youtube-Rx8f05JI_WA]], [[youtube-Rx8f05JI_WA-transcript]], [[youtube-Rx8f05JI_WA-slides]]
- `youtube-vljxQZfJ9wY` — 1,143 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-vljxQZfJ9wY`: evaluation, production, systems, most, model, tool, becomes, infrastructure.
- Slide-derived themes for `youtube-vljxQZfJ9wY`: accuracy, evaluation, output, behavior, workflow, tool, failure, volume.
- Evidence links for `youtube-vljxQZfJ9wY` (supporting context only): [[youtube-vljxQZfJ9wY]], [[youtube-vljxQZfJ9wY-transcript]], [[youtube-vljxQZfJ9wY-slides]]
- `youtube-1IdzkRVmWAA` — 6,138 transcript words; 4 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-1IdzkRVmWAA`: search, query, tools, queries, tool, retrieval, semantic, chunks.
- Slide-derived themes for `youtube-1IdzkRVmWAA`: taught, retrieval, trajectories, tool, calls, toes.
- Evidence links for `youtube-1IdzkRVmWAA` (supporting context only): [[youtube-1IdzkRVmWAA]], [[youtube-1IdzkRVmWAA-transcript]], [[youtube-1IdzkRVmWAA-slides]]
