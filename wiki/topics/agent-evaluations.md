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
  - source:official-wf26-youtube-31GUkCBD-Uc
  - source:official-wf26-youtube-9QebvrrY3KY
  - source:official-wf26-youtube-Cz4v1WHVyZc
  - source:official-wf26-youtube-GgLQ02aO-hs
  - source:official-wf26-youtube-OqM67QG_Ikk
  - source:official-wf26-youtube-RGSFUqzqErE
  - source:official-wf26-youtube-V-EDrhIhHzQ
  - source:official-wf26-youtube-VrpEyglYgeU
  - source:official-wf26-youtube-WkBPX-oDMnA
  - source:official-wf26-youtube-X1kp-ABIIxQ
  - source:official-wf26-youtube-XV2oYi7kojc
  - source:official-wf26-youtube-YnNF55QV0zs
  - source:official-wf26-youtube-ZSQb5fzRFPw
  - source:official-wf26-youtube-ZpK5PWX2YRM
  - source:official-wf26-youtube-ZyIoTOAbRfs
  - source:official-wf26-youtube-iCj_ATyThvc
  - source:official-wf26-youtube-il1c1a2FufU
  - source:official-wf26-youtube-jRCpXUjz4CI
  - source:official-wf26-youtube-n97BCfyFIvw
  - source:official-wf26-youtube-q4Tr-DknG2M
  - source:official-wf26-youtube-uIiA6DquRiE
  - source:official-wf26-youtube-uU5Gv2h8-9g
  - source:official-wf26-youtube-xyL2Ltkh-SA
sourceAssessmentBodySha256: sha256:2e3b699298bc0634d87d5ecfc29efd02a888968f88ddb47bd405c11394bfa5b4
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
- [[2026-06-30-alex-shaw-everything-is-a-rollout]] — Everything Is a Rollout
- [[2026-06-30-antje-barth-perception-agents]] — Perception Agents
- [[2026-06-30-chris-souza-model-whisperers-how-evals-and-prompts-shape-agent-behavior]] — Model Whisperers: How Evals and Prompts Shape Agent Behavior
- [[2026-06-30-dan-farrelly-your-agent-architecture-has-a-half-life-of-6-months]] — Your agent architecture has a half-life of 6 months
- [[2026-06-30-francesco-bonacci-computer-use-2-0-agents-just-got-multi-cursor]] — Computer-Use 2.0: Agents Just Got Multi-Cursor
- [[2026-06-30-jason-lopatecki-from-signal-to-pr-anatomy-of-a-self-improving-agent]] — From Signal to PR: Anatomy of a Self-Improving Agent
- [[2026-06-30-sean-cai-state-of-data]] — State of Data
- [[2026-06-30-soumya-gupta-building-closed-loop-evals-for-a-multimodal-agent-at-uber-scale]] — Building Closed-Loop Evals for a Multimodal Agent at Uber Scale
- [[2026-07-01-emil-eifrem-thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer]] — Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one]] — Video Has No Memory. Here's How We Built One.
- [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens]] — CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens

## Slide-Derived Supporting Decks
- [[youtube--CnA2lGfymY-slides]] — "I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox (32 extracted slide frames)
- [[youtube-2JX6JYyQG4Y-slides]] — Perception Agents — Antje Barth, Amazon AGI Lab (31 extracted slide frames)
- [[youtube-31GUkCBD-Uc-slides]] — Building Closed-Loop Evals for a Multimodal Agent at Scale — Soumya Gupta & Jai Chopra, Uber (16 extracted slide frames)
- [[youtube-9HbzAWnKbo4-slides]] — From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize (17 extracted slide frames)
- [[youtube-9QebvrrY3KY-slides]] — Claude for Long-Horizon Tasks — Lance Martin, Anthropic (4 extracted slide frames)
- [[youtube-Ib5GBkD555M-slides]] — Harness Engineering is not Enough: Why Software Factories Fail — Dex Horthy, HumanLayer (32 extracted slide frames)
- [[youtube-il1c1a2FufU-slides]] — Setting Yourself Up for Success — Part 1 — Jason Liu, OpenAI (12 extracted slide frames)
- [[youtube-jRCpXUjz4CI-slides]] — Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute (32 extracted slide frames)
- [[youtube-mOf-PP4mVjA-slides]] — Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs (31 extracted slide frames)
- [[youtube-n97BCfyFIvw-slides]] — "The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani (32 extracted slide frames)
- [[youtube-OqM67QG_Ikk-slides]] — From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI (15 extracted slide frames)
- [[youtube-Q0VkgCyNVUg-slides]] — CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j (22 extracted slide frames)
- [[youtube-RGSFUqzqErE-slides]] — On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft (28 extracted slide frames)
- [[youtube-VGN22pPpb-8-slides]] — Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j (32 extracted slide frames)
- [[youtube-X1kp-ABIIxQ-slides]] — Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest (15 extracted slide frames)
- [[youtube-xyL2Ltkh-SA-slides]] — How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads (7 extracted slide frames)
- [[youtube-ZSQb5fzRFPw-slides]] —  (17 extracted slide frames)
- [[youtube-ZyIoTOAbRfs-slides]] — State of Data — Sean Cai, Independent / State of Data (10 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

## Transcript Digest Evidence
This section synthesizes 60 evidence-bound talk topic candidates across at least two talks.

### Cross-Talk Synthesis
These candidates center on how to measure agent behavior without letting the system game the metric, using harnesses, verifier loops, golden sets, rollout checks, and closed-loop feedback. The important variation is between offline benchmark design and live production validation, with several talks stressing that the evaluation itself must stay resilient as agents adapt to it.

### Constituent Talk Evidence
- [[2026-06-29-daniel-han-special-topics-in-kernels-rl-reward-hacking-in-agents|Special topics in Kernels, RL, Reward Hacking in Agents]] — Designing benchmarks that resist gaming while remaining easy to check.
  - Transcript: [[youtube-uIiA6DquRiE-transcript]]
  - Evidence: "The first condition is the benchmark must not must not be benchmaxable. Right? How do you make a benchmark that is extremely hard to benchmark, right?"
- [[2026-06-29-dex-horthy-harness-engineering-is-not-enough-why-software-factories-fail|Harness Engineering is not Enough: Why Software Factories Fail]] — Evaluating coding agents and code quality with benchmarks, verifiers, and reward channels.
  - Transcript: [[youtube-Ib5GBkD555M-transcript]]
  - Evidence: "So, we're going to look at these as like what is the future of evaluating code maintainability."
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust|In Code They Act, In Proof We Trust]] — Turning agent intent into a program that can be inspected and analyzed statically.
  - Transcript: [[youtube--CnA2lGfymY-transcript]]
  - Evidence: "Um, and again, it's a small step for a signature, but a giant leap for safety because now the model returns an expression, a program that represents a computation."
- [[2026-06-29-lance-martin-claude-for-long-horizon-tasks|Claude for long-horizon tasks]] — Shared harnesses with organizational identity, organizational context, and team-wide access.
  - Transcript: [[youtube-9QebvrrY3KY-transcript]]
  - Evidence: "What's interesting about Claude Tag is it is a harness that everyone in the organization has access to and can use."
- [[2026-06-29-lee-robinson-recursive-model-improvement|Recursive Model Improvement]] — Controls and benchmark design choices that prevent models from gaming evaluation results.
  - Transcript: [[youtube-q4Tr-DknG2M-transcript]]
  - Evidence: "So, first off, we would delete the Git history at the start, and we could restore it at the end, so that wouldn't affect the run."
- [[2026-06-29-manoj-nair-through-the-ai-fog-the-architectural-decision-the-next-24-months-of-agentic-security-depends-on|Through the AI Fog: The architectural decision the next 24 months of agentic security depends on.]] — The claim that generation and validation should be separated because models are not reliable enough to serve as their own judges.
  - Transcript: [[youtube-1EZdpEhwmNc-transcript]]
  - Evidence: "That's not how you can run an enterprise system if you just use the LLM without any anything else."
- [[2026-06-29-pablo-castro-on-ai-and-knowledge|On AI and Knowledge]] — Improving agents through evaluation-driven candidate generation and deployment.
  - Transcript: [[youtube-RGSFUqzqErE-transcript]]
  - Evidence: "So we built a component called the agent optimizer that effectively goes through this process and allows you to evaluate a baseline, generate candidates, and then you know, evaluate the new candidates and we have a strong result, then deploy that to production."
- [[2026-06-29-sarah-sachs-notion-s-token-town|Notion's Token Town]] — Judging providers by end-to-end task outcomes rather than by single-call metrics.
  - Transcript: [[youtube--I5W5QVAT8E-transcript]]
  - Evidence: "But if you have expertise in entire web search trajectories, you'll see how it differs. The granularity of this eval is what lets us make the best decisions for our customers because we understand all of the trade-offs on entire trajectories, not just single calls."
- [[2026-06-29-will-brown-the-prime-intellect-stack|The Prime Intellect Stack]] — Reward design that compares grouped samples to balance correctness and efficiency.
  - Transcript: [[youtube-V-EDrhIhHzQ-transcript]]
  - Evidence: "But there's a lot of things where you really want to do pairwise judging or you want to do ranking or you want to give a bonus to the uh the shortest correct answer uh in terms of tokens used."
- [[2026-06-30-addy-osmani-closing-keynote|Closing Keynote]] — The shift from a final review step to a broader system for routing, verifying, and integrating work.
  - Transcript: [[youtube-n97BCfyFIvw-transcript]]
  - Evidence: "It has to become a whole control system. The second thing to avoid is cognitive surrender."
- [[2026-06-30-alex-shaw-everything-is-a-rollout|Everything Is a Rollout]] — The idea that agent behavior should be measured empirically instead of assumed from code inspection.
  - Transcript: [[youtube-jRCpXUjz4CI-transcript]]
  - Evidence: "Uh and that brings us to our next question which is how do I actually evaluate an agent? Uh and this is when we start to get into uh what what harbor does."
- [[2026-06-30-alex-volkov-the-z-l-continuum-should-ai-engineers-still-read-code|The Z/L Continuum: Should AI Engineers Still Read Code?]] — The idea that review depth should be chosen per task instead of per engineer identity.
  - Transcript: [[youtube-ZpK5PWX2YRM-transcript]]
  - Evidence: "The ZL continuum is real. But it's not about the people. It's about the tasks. The continuum is real."
- [[2026-06-30-chris-souza-model-whisperers-how-evals-and-prompts-shape-agent-behavior|Model Whisperers: How Evals and Prompts Shape Agent Behavior]] — A curated set of representative examples used to judge agent behavior.
  - Transcript: [[youtube-xyL2Ltkh-SA-transcript]]
  - Evidence: "So we want to give a golden set that's like super expansive. It covers a broad range of use cases and it also has very high human human agreement within your team."
- [[2026-06-30-francesco-bonacci-computer-use-2-0-agents-just-got-multi-cursor|Computer-Use 2.0: Agents Just Got Multi-Cursor]] — Using recorded trajectories to probe whether a model can predict reward or internal state.
  - Transcript: [[youtube-ZSQb5fzRFPw-transcript]]
  - Evidence: "From there we can probe a model asking to predict the reward, the internal state or any other observation of the computer and compare it against the fork."
- [[2026-06-30-geoffrey-litt-understanding-is-the-new-bottleneck|Understanding is the new bottleneck]] — A learning technique that uses quizzes to verify genuine comprehension instead of passive reading.
  - Transcript: [[youtube-WkBPX-oDMnA-transcript]]
  - Evidence: "So, that So, he and his collaborator Michael Nielsen tried this thing where in an essay, there are interactive spaced repetition quizzes that test whether you actually remember what you just read."
- [[2026-06-30-ishan-anand-will-ai-predict-people-like-we-predict-the-weather-alternate-title-a-field-guide-to-synthetic-personas-for-market-research|Will AI predict people like we predict the weather? (alternate title “A field guide to synthetic personas for market research”)]] — The distinction between measuring stated attitudes and predicting actual behavior.
  - Transcript: [[youtube-YnNF55QV0zs-transcript]]
  - Evidence: "Those are behaviors, and those are things that need to be transcribed into actions. They're less likely to be in the training data, and correspondingly, the LLM doesn't do as well."
- [[2026-06-30-jason-lopatecki-from-signal-to-pr-anatomy-of-a-self-improving-agent|From Signal to PR: Anatomy of a Self-Improving Agent]] — Composable skills that gather and shape observability context
  - Transcript: [[youtube-9HbzAWnKbo4-transcript]]
  - Evidence: "Okay, handful. Okay, cool. Awesome. Um, so the magic of of of skills that that that connect to observability platforms um is it can gather the context."
- [[2026-06-30-philipp-schmid-don-t-ship-skills-without-evals|Don't Ship Skills Without Evals]] — Skills that encode durable team or company preferences and workflows.
  - Transcript: [[youtube-0vphxNt4wyk-transcript]]
  - Evidence: "Those are more durable, mostly encode some references. So, if you have a specific workflow in your team or a specific style language or other preferences which are very specific to your company, Um will have or create preference skills and those uh preference skills are then protected with e-walls where because most of like the foundation models might not uh integrate the knowledge which is very specific to your use case or your domain."
- [[2026-06-30-sean-cai-state-of-data|State of Data]] — The idea that task ease of training depends on how verifiable the task is.
  - Transcript: [[youtube-ZyIoTOAbRfs-transcript]]
  - Evidence: "It's called Verifier's Law. The ease of training a model to do a task is proportional to how verifiable the task is."
- [[2026-06-30-soumya-gupta-building-closed-loop-evals-for-a-multimodal-agent-at-uber-scale|Building Closed-Loop Evals for a Multimodal Agent at Uber Scale]] — The speakers emphasize that edits should not collapse the visual diversity of the marketplace.
  - Transcript: [[youtube-31GUkCBD-Uc-transcript]]
  - Evidence: "If we have the same prompt for every photo that we're editing, the diversity of the marketplace is going to collapse."
- [[2026-06-30-tariq-shaukat-in-the-land-of-ai-agents-the-verifiers-are-king|'In the Land of AI Agents, the Verifiers Are King']] — Combining multiple verification techniques to cover both obvious and subtle failures.
  - Transcript: [[youtube-VrpEyglYgeU-transcript]]
  - Evidence: "Software has lots of of of intricacies involved with it. And so what we believe and again have found to be quite um impactful here is that a combination of algorithmic verification looking at things like data flows, control flows, known patterns, secrets, these areas combined with what is now possible with agentic verification looking at intent, business logic, the unknown unknowns."
- [[2026-06-30-uri-rolls-training-frontier-models-to-out-think-hackers|Training Frontier Models to Out-Think Hackers]] — Verifying each action in a long exploitation chain with machine-checkable scoring.
  - Transcript: [[youtube-O-CBZ3JtRvo-transcript]]
  - Evidence: "And everything because the tasks are so difficult, everything has a deterministic greater."
- [[2026-06-30-zhengyao-jiang-an-ai-agent-became-the-1-contributor-in-openai-s-hiring-challenge|An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge]] — The role of evaluation design in determining what an autonomous research system optimizes for.
  - Transcript: [[youtube-iCj_ATyThvc-transcript]]
  - Evidence: "It sets what the agent optimizes for. Take the eval first. The eval is the signal you use to train a model."
- [[2026-07-01-frank-coyle-why-agentic-systems-need-ontologies|Why Agentic Systems Need Ontologies]] — The execution pattern where an LLM proposes a tool action, a stop reason is checked, and the tool result is validated.
  - Transcript: [[youtube-Sir59K8ZDPU-transcript]]
  - Evidence: "So, stop reason means the LLM has stopped for some reason. The The reason here is that it can't do anything, and if the reason is tool use, ah, now it's time."
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one|Video Has No Memory. Here's How We Built One.]] — A deterministic operating model for video understanding that plans tasks, retrieves evidence, and validates outputs.
  - Transcript: [[youtube-mOf-PP4mVjA-transcript]]
  - Evidence: "So what does it look like for for video on a static model right um a model co a single answer it is stateless it start fresh time start fresh each time and doesn't have any constraint so the output is largely based on what the model decide to produce a video worker on the"
- [[2026-07-01-james-russo-html-is-all-agents-need|HTML Is All Agents Need]] — Using skills and evaluation loops to shape model output quality.
  - Transcript: [[youtube-Cz4v1WHVyZc-transcript]]
  - Evidence: "And a big part of this is the skills that we couple with our framework. Our skill is focused on taste and video aspects because the LLMs and agents already know how to write HTML and CSS and JavaScript, we don't have to teach them the language, we just teach them how to create good videos."
- [[2026-07-01-maxime-rivest-the-unreasonable-effectiveness-of-separating-the-task-from-the-model|The Unreasonable Effectiveness of Separating the Task from the Model]] — The use of product feedback and textual signals to improve evals without relying only on hand-built metrics.
  - Transcript: [[youtube-GgLQ02aO-hs-transcript]]
  - Evidence: "How do we decrease assistance? And it's a research question right now. But what we believe is that models are now good enough to interpret whatever textual feedback is present in the environment and convert that into evals and a hill that the model can climb."
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
| resources | 36 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 57 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 60 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 3 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 40 | Transcript markdown; check session matching and caption quality. |

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
- [[youtube-uIiA6DquRiE]]
- [[youtube-Ib5GBkD555M]]
- [[youtube-9QebvrrY3KY]]
- [[youtube-q4Tr-DknG2M]]

### Slides
- [[youtube--CnA2lGfymY-slides]]
- [[youtube-2JX6JYyQG4Y-slides]]
- [[youtube-31GUkCBD-Uc-slides]]
- [[youtube-9HbzAWnKbo4-slides]]
- [[youtube-9QebvrrY3KY-slides]]
- [[youtube-Ib5GBkD555M-slides]]

### Transcripts
- [[youtube-uIiA6DquRiE-transcript]]
- [[youtube-Ib5GBkD555M-transcript]]
- [[youtube--CnA2lGfymY-transcript]]
- [[youtube-9QebvrrY3KY-transcript]]
- [[youtube-q4Tr-DknG2M-transcript]]
- [[youtube-1EZdpEhwmNc-transcript]]

### Tools
- [[braintrust]]
- [[prime-intellect]]
- [[arize]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.

### Linked Sessions
- [[2026-06-29-daniel-han-special-topics-in-kernels-rl-reward-hacking-in-agents|Special topics in Kernels, RL, Reward Hacking in Agents]]
- [[2026-06-29-dex-horthy-harness-engineering-is-not-enough-why-software-factories-fail|Harness Engineering is not Enough: Why Software Factories Fail]]
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust|In Code They Act, In Proof We Trust]]
- [[2026-06-29-lance-martin-claude-for-long-horizon-tasks|Claude for long-horizon tasks]]
- [[2026-06-29-lee-robinson-recursive-model-improvement|Recursive Model Improvement]]
- [[2026-06-29-manoj-nair-through-the-ai-fog-the-architectural-decision-the-next-24-months-of-agentic-security-depends-on|Through the AI Fog: The architectural decision the next 24 months of agentic security depends on.]]
- [[2026-06-29-pablo-castro-on-ai-and-knowledge|On AI and Knowledge]]
- [[2026-06-29-sarah-sachs-notion-s-token-town|Notion's Token Town]]
- [[2026-06-29-will-brown-the-prime-intellect-stack|The Prime Intellect Stack]]
- [[2026-06-30-addy-osmani-closing-keynote|Closing Keynote]]

### Media Signals
- `youtube-uIiA6DquRiE` — 25,283 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-uIiA6DquRiE`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-uIiA6DquRiE`: model, models, source, open, benchmark, question, okay, accuracy.
- Slide-derived themes for `youtube-uIiA6DquRiE`: smaller, model, high, extra, license, businesses, users, open.
- Evidence links for `youtube-uIiA6DquRiE` (primary event evidence): [[youtube-uIiA6DquRiE]], [[youtube-uIiA6DquRiE-transcript]], [[youtube-uIiA6DquRiE-slides]]
- `youtube-Ib5GBkD555M` — 4,045 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Ib5GBkD555M`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Ib5GBkD555M`: code, review, model, coding, software, stuff, test, better.
- Slide-derived themes for `youtube-Ib5GBkD555M`: software, harness, enough, team, engineering, factories, fail, pierre.
- Evidence links for `youtube-Ib5GBkD555M` (primary event evidence): [[youtube-Ib5GBkD555M]], [[youtube-Ib5GBkD555M-transcript]], [[youtube-Ib5GBkD555M-slides]]
- `youtube-9QebvrrY3KY` — 4,450 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-9QebvrrY3KY`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-9QebvrrY3KY`: memory, models, claude, model, context, interesting, harness, important.
- Slide-derived themes for `youtube-9QebvrrY3KY`: generator, lance, martin, member, technical, staff, engineering, future.
- Evidence links for `youtube-9QebvrrY3KY` (primary event evidence): [[youtube-9QebvrrY3KY]], [[youtube-9QebvrrY3KY-transcript]], [[youtube-9QebvrrY3KY-slides]]
- `youtube-q4Tr-DknG2M` — 4,039 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-q4Tr-DknG2M`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-q4Tr-DknG2M`: models, model, training, evals, pretty, loop, compute, cursor.
- Slide-derived themes for `youtube-q4Tr-DknG2M`: future, cursor, compute, better, model, anon, pease, days.
- Evidence links for `youtube-q4Tr-DknG2M` (primary event evidence): [[youtube-q4Tr-DknG2M]], [[youtube-q4Tr-DknG2M-transcript]], [[youtube-q4Tr-DknG2M-slides]]
- `youtube-1EZdpEhwmNc` — 4,245 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-1EZdpEhwmNc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-1EZdpEhwmNc`: security, data, code, able, find, skill, customers, attacks.
- Slide-derived themes for `youtube-1EZdpEhwmNc`: track, june, security, malicious, engineering, future, pitch, defend.
- Evidence links for `youtube-1EZdpEhwmNc` (primary event evidence): [[youtube-1EZdpEhwmNc]], [[youtube-1EZdpEhwmNc-transcript]], [[youtube-1EZdpEhwmNc-slides]]
- `youtube-RGSFUqzqErE` — 3,081 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-RGSFUqzqErE`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-RGSFUqzqErE`: knowledge, data, retrieval, foundry, whatnot, microsoft, models, give.
- Slide-derived themes for `youtube-RGSFUqzqErE`: fair, engineering, future, bile, microsoft, resolve, knowledge, pablo.
- Evidence links for `youtube-RGSFUqzqErE` (primary event evidence): [[youtube-RGSFUqzqErE]], [[youtube-RGSFUqzqErE-transcript]], [[youtube-RGSFUqzqErE-slides]]
- `youtube--I5W5QVAT8E` — 4,014 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube--I5W5QVAT8E`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube--I5W5QVAT8E`: model, notion, today, customers, product, okay, always, system.
- Slide-derived themes for `youtube--I5W5QVAT8E`: engineering, plan, future, fair, recently, purchased, each, subscription.
- Evidence links for `youtube--I5W5QVAT8E` (primary event evidence): [[youtube--I5W5QVAT8E]], [[youtube--I5W5QVAT8E-transcript]], [[youtube--I5W5QVAT8E-slides]]
- `youtube-V-EDrhIhHzQ` — 10,228 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-V-EDrhIhHzQ`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-V-EDrhIhHzQ`: model, harness, well, doing, environment, training, able, models.
- Slide-derived themes for `youtube-V-EDrhIhHzQ`: engineering, future, prime, intellect, stack, open.
- Evidence links for `youtube-V-EDrhIhHzQ` (primary event evidence): [[youtube-V-EDrhIhHzQ]], [[youtube-V-EDrhIhHzQ-transcript]], [[youtube-V-EDrhIhHzQ-slides]]
- `youtube-n97BCfyFIvw` — 3,068 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-n97BCfyFIvw`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-n97BCfyFIvw`: code, still, taste, loop, engineering, evidence, system, human.
- Slide-derived themes for `youtube-n97BCfyFIvw`: roles, google, look, across, worth, doing, increasingly, automated.
- Evidence links for `youtube-n97BCfyFIvw` (primary event evidence): [[youtube-n97BCfyFIvw]], [[youtube-n97BCfyFIvw-transcript]], [[youtube-n97BCfyFIvw-slides]]
- `youtube-jRCpXUjz4CI` — 3,664 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-jRCpXUjz4CI`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-jRCpXUjz4CI`: harbor, model, software, well, sandbox, probably, looks, learning.
- Slide-derived themes for `youtube-jRCpXUjz4CI`: text, number, part, extract, phone, response, engineering, future.
- Evidence links for `youtube-jRCpXUjz4CI` (primary event evidence): [[youtube-jRCpXUjz4CI]], [[youtube-jRCpXUjz4CI-transcript]], [[youtube-jRCpXUjz4CI-slides]]
- `youtube-ZpK5PWX2YRM` — 3,931 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-ZpK5PWX2YRM`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-ZpK5PWX2YRM`: code, okay, read, line, guys, still, loops, engineer.
- Slide-derived themes for `youtube-ZpK5PWX2YRM`: future, software, bigger, than, last, engineering, leadership, july.
- Evidence links for `youtube-ZpK5PWX2YRM` (primary event evidence): [[youtube-ZpK5PWX2YRM]], [[youtube-ZpK5PWX2YRM-transcript]], [[youtube-ZpK5PWX2YRM-slides]]
- `youtube-xyL2Ltkh-SA` — 3,548 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-xyL2Ltkh-SA`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-xyL2Ltkh-SA`: eval, important, doing, cases, should, having, scale, first.
- Slide-derived themes for `youtube-xyL2Ltkh-SA`: model, models, microsoft, hard, provides, foundation, critique, loop.
- Evidence links for `youtube-xyL2Ltkh-SA` (primary event evidence): [[youtube-xyL2Ltkh-SA]], [[youtube-xyL2Ltkh-SA-transcript]], [[youtube-xyL2Ltkh-SA-slides]]
- `youtube-ZSQb5fzRFPw` — 2,617 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-ZSQb5fzRFPw`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-ZSQb5fzRFPw`: computer, take, over, driver, background, task, might, sandbox.
- Slide-derived themes for `youtube-ZSQb5fzRFPw`: track, july, fair, computer, operator, loop, wired, model.
- Evidence links for `youtube-ZSQb5fzRFPw` (primary event evidence): [[youtube-ZSQb5fzRFPw]], [[youtube-ZSQb5fzRFPw-transcript]], [[youtube-ZSQb5fzRFPw-slides]]
- `youtube-9HbzAWnKbo4` — 3,797 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-9HbzAWnKbo4`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-9HbzAWnKbo4`: skills, data, traces, maybe, running, well, signal, cloud.
- Slide-derived themes for `youtube-9HbzAWnKbo4`: track, july, macro, signal, engineering, future, consumes, telemetry.
- Evidence links for `youtube-9HbzAWnKbo4` (primary event evidence): [[youtube-9HbzAWnKbo4]], [[youtube-9HbzAWnKbo4-transcript]], [[youtube-9HbzAWnKbo4-slides]]
- `youtube-0vphxNt4wyk` — 3,965 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-0vphxNt4wyk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-0vphxNt4wyk`: skill, skills, model, should, look, evals, eval, always.
- Slide-derived themes for `youtube-0vphxNt4wyk`: skills, fail, chad, vibe, checks, production, engineering, future.
- Evidence links for `youtube-0vphxNt4wyk` (primary event evidence): [[youtube-0vphxNt4wyk]], [[youtube-0vphxNt4wyk-transcript]], [[youtube-0vphxNt4wyk-slides]]
- `youtube-ZyIoTOAbRfs` — 3,355 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-ZyIoTOAbRfs`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-ZyIoTOAbRfs`: data, model, layer, three, companies, type, real, labs.
- Slide-derived themes for `youtube-ZyIoTOAbRfs`: track, july, data, bottleneck, never, intelligence, ones, human.
- Evidence links for `youtube-ZyIoTOAbRfs` (primary event evidence): [[youtube-ZyIoTOAbRfs]], [[youtube-ZyIoTOAbRfs-transcript]], [[youtube-ZyIoTOAbRfs-slides]]
- `youtube-31GUkCBD-Uc` — 3,773 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-31GUkCBD-Uc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-31GUkCBD-Uc`: image, feedback, system, production, output, pass, model, send.
- Slide-derived themes for `youtube-31GUkCBD-Uc`: track, july, problem, poor, chopra, product, manager, engineering.
- Evidence links for `youtube-31GUkCBD-Uc` (primary event evidence): [[youtube-31GUkCBD-Uc]], [[youtube-31GUkCBD-Uc-transcript]], [[youtube-31GUkCBD-Uc-slides]]
- `youtube-VrpEyglYgeU` — 3,005 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-VrpEyglYgeU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-VrpEyglYgeU`: code, verification, models, loop, still, question, sure, problem.
- Slide-derived themes for `youtube-VrpEyglYgeU`: accuracy, land, king, meters, industry, struggling, slop, coding.
- Evidence links for `youtube-VrpEyglYgeU` (primary event evidence): [[youtube-VrpEyglYgeU]], [[youtube-VrpEyglYgeU-transcript]], [[youtube-VrpEyglYgeU-slides]]
- `youtube-O-CBZ3JtRvo` — 3,557 transcript words; 9 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-O-CBZ3JtRvo`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-O-CBZ3JtRvo`: model, cyber, models, able, reason, been, benchmark, understand.
- Slide-derived themes for `youtube-O-CBZ3JtRvo`: training, models, attackers, engineering, future, track, july, arithmetic.
- Evidence links for `youtube-O-CBZ3JtRvo` (primary event evidence): [[youtube-O-CBZ3JtRvo]], [[youtube-O-CBZ3JtRvo-transcript]], [[youtube-O-CBZ3JtRvo-slides]]
- `youtube-iCj_ATyThvc` — 1,795 transcript words; 4 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-iCj_ATyThvc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-iCj_ATyThvc`: research, auto, aiden, human, training, ideas, data, competition.
- Slide-derived themes for `youtube-iCj_ATyThvc`: code, golf, neural, networks, train, best, language, model.
- Evidence links for `youtube-iCj_ATyThvc` (primary event evidence): [[youtube-iCj_ATyThvc]], [[youtube-iCj_ATyThvc-transcript]], [[youtube-iCj_ATyThvc-slides]]
- `youtube-mOf-PP4mVjA` — 3,509 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-mOf-PP4mVjA`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-mOf-PP4mVjA`: memory, scene, content, system, across, layer, application, context.
- Slide-derived themes for `youtube-mOf-PP4mVjA`: memory, built, data, incredibly, complex, scale, holistic, understanding.
- Evidence links for `youtube-mOf-PP4mVjA` (primary event evidence): [[youtube-mOf-PP4mVjA]], [[youtube-mOf-PP4mVjA-transcript]], [[youtube-mOf-PP4mVjA-slides]]
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
- `youtube-jt1Pbr_n6oU` — 3,441 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-jt1Pbr_n6oU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-jt1Pbr_n6oU`: data, model, graph, across, structure, chat, part, structured.
- Slide-derived themes for `youtube-jt1Pbr_n6oU`: track, july, fair, intro, defensible, organization, presented, users.
- Evidence links for `youtube-jt1Pbr_n6oU` (primary event evidence): [[youtube-jt1Pbr_n6oU]], [[youtube-jt1Pbr_n6oU-transcript]], [[youtube-jt1Pbr_n6oU-slides]]
- `youtube-XV2oYi7kojc` — 2,590 transcript words; 3 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-XV2oYi7kojc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-XV2oYi7kojc`: models, billion, hardware, open, model, source, parameter, months.
- Slide-derived themes for `youtube-XV2oYi7kojc`: within, roughly, months, class, intelligence, late, mode, performs.
- Evidence links for `youtube-XV2oYi7kojc` (primary event evidence): [[youtube-XV2oYi7kojc]], [[youtube-XV2oYi7kojc-transcript]], [[youtube-XV2oYi7kojc-slides]]
- `youtube-il1c1a2FufU` — 13,744 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-il1c1a2FufU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-il1c1a2FufU`: thread, computer, slack, been, pretty, skills, threads, skill.
- Slide-derived themes for `youtube-il1c1a2FufU`: workshops, track, june, product, days, jobs, context, problem.
- Evidence links for `youtube-il1c1a2FufU` (primary event evidence): [[youtube-il1c1a2FufU]], [[youtube-il1c1a2FufU-transcript]], [[youtube-il1c1a2FufU-slides]]
- `youtube-uU5Gv2h8-9g` — 10,417 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-uU5Gv2h8-9g`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-uU5Gv2h8-9g`: code, claude, prompt, been, cloud, model, mode, team.
- Evidence links for `youtube-uU5Gv2h8-9g` (primary event evidence): [[youtube-uU5Gv2h8-9g]], [[youtube-uU5Gv2h8-9g-transcript]], [[youtube-uU5Gv2h8-9g-slides]]
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-4sX_He5c4sI`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: lots, examples, stream, starts, july, land, king, chief.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube-I2cbIws9j10` — 91,792 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-I2cbIws9j10`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: choosing, model, quality, dominates, agentic, capabilities, customization, support.
- Evidence links for `youtube-I2cbIws9j10` (primary event evidence): [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
- `youtube-htM02KMNZnk` — 89,050 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-htM02KMNZnk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-htM02KMNZnk`: model, code, models, loop, well, software, first, team.
- Slide-derived themes for `youtube-htM02KMNZnk`: apps, github, copilot, welcome, engineer, fair, single, line.
- Evidence links for `youtube-htM02KMNZnk` (primary event evidence): [[youtube-htM02KMNZnk]], [[youtube-htM02KMNZnk-transcript]], [[youtube-htM02KMNZnk-slides]], [[youtube-htM02KMNZnk-dense-slides]], [[youtube-htM02KMNZnk-reconstructed-slides]]
- `youtube-Xfl50508LZM` — 22,591 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-Xfl50508LZM`: evals, eval, data, should, judge, output, whether, phoenix.
- Slide-derived themes for `youtube-Xfl50508LZM`: swiss, cheese, talking, setting, tracing, phoenix, paine, theoretical.
- Evidence links for `youtube-Xfl50508LZM` (supporting context only): [[youtube-Xfl50508LZM]], [[youtube-Xfl50508LZM-transcript]], [[youtube-Xfl50508LZM-slides]], [[youtube-Xfl50508LZM-dense-slides]], [[youtube-Xfl50508LZM-reconstructed-slides]]
- `youtube-Rx8f05JI_WA` — 4,329 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-Rx8f05JI_WA`: tasks, verifier, task, full, marathon, hours, compiler, tests.
- Slide-derived themes for `youtube-Rx8f05JI_WA`: tasks, tokens, coding, projects, trial, stay, coherent, over.
- Evidence links for `youtube-Rx8f05JI_WA` (supporting context only): [[youtube-Rx8f05JI_WA]], [[youtube-Rx8f05JI_WA-transcript]], [[youtube-Rx8f05JI_WA-slides]]
- `youtube-vljxQZfJ9wY` — 1,143 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-vljxQZfJ9wY`: evaluation, production, systems, most, model, tool, becomes, infrastructure.
- Slide-derived themes for `youtube-vljxQZfJ9wY`: accuracy, evaluation, output, behavior, workflow, tool, failure, volume.
- Evidence links for `youtube-vljxQZfJ9wY` (supporting context only): [[youtube-vljxQZfJ9wY]], [[youtube-vljxQZfJ9wY-transcript]], [[youtube-vljxQZfJ9wY-slides]]
- `youtube-bk0TmxoZlUY` — 9,125 transcript words; 9 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-bk0TmxoZlUY`: maybe, trust, brain, within, data, scores, eval, application.
- Slide-derived themes for `youtube-bk0TmxoZlUY`: support, leading, teams, netflix, nite, become, core, skill.
- Evidence links for `youtube-bk0TmxoZlUY` (supporting context only): [[youtube-bk0TmxoZlUY]], [[youtube-bk0TmxoZlUY-transcript]], [[youtube-bk0TmxoZlUY-slides]], [[youtube-bk0TmxoZlUY-dense-slides]], [[youtube-bk0TmxoZlUY-reconstructed-slides]]
- `youtube-1IdzkRVmWAA` — 6,138 transcript words; 4 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-1IdzkRVmWAA`: search, query, tools, queries, tool, retrieval, semantic, chunks.
- Slide-derived themes for `youtube-1IdzkRVmWAA`: taught, retrieval, trajectories, tool, calls, toes.
- Evidence links for `youtube-1IdzkRVmWAA` (supporting context only): [[youtube-1IdzkRVmWAA]], [[youtube-1IdzkRVmWAA-transcript]], [[youtube-1IdzkRVmWAA-slides]]
- `youtube-Lcqat4iP_lE` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-Lcqat4iP_lE`: tool, call, microsoft, tools, client, server, path, calculate.
- Evidence links for `youtube-Lcqat4iP_lE` (supporting context only): [[youtube-Lcqat4iP_lE]], [[youtube-Lcqat4iP_lE-slides]], [[youtube-Lcqat4iP_lE-dense-slides]], [[youtube-Lcqat4iP_lE-reconstructed-slides]]
