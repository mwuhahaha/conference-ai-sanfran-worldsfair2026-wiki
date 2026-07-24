---
title: Inference Engineering
category: topics
sourceLabels:
  - Slide/video-derived supporting context
last_auto_summarized: '2026-07-18T04:30:32.575Z'
sourceAssessment:
  schemaVersion: 1
  claimId: claim:4850462b84362bed601efedd32d2462a4cd5c02401c4d80bf1d975ea9b153271
  subjectId: concept:inference-engineering
  domain: topics page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-24T00:00:00.000000Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-youtube--I5W5QVAT8E
  - source:official-wf26-youtube-KB41dTlX1Uc
  - source:official-wf26-youtube-OqM67QG_Ikk
  - source:official-wf26-youtube-V-EDrhIhHzQ
  - source:official-wf26-youtube-XV2oYi7kojc
  - source:official-wf26-youtube-YnNF55QV0zs
  - source:official-wf26-youtube-Z2Erdirpudo
  - source:official-wf26-youtube-iCj_ATyThvc
  - source:official-wf26-youtube-pMggiOb18tc
  - source:official-wf26-youtube-q4Tr-DknG2M
  - source:official-wf26-youtube-uIiA6DquRiE
sourceAssessmentBodySha256: sha256:2e9619e9755197e353fc823153ce20a7b3a719cdd2793111a79f352dcd4179f7
---
# Inference Engineering

## Overview
Inference engineering is the systems discipline that turns model capability into a dependable product by controlling the complete serving path: inference-engine and model selection, prefill and generation, batching, KV and context caching, quantization, routing policy, GPU utilization, token streaming, observability, fallback behavior, and unit economics.

At World’s Fair 2026, the topic spans distributed serving at Meta scale, engine-signal-driven routing at OpenAI, open-source inference stacks from Together AI, dedicated GPUs for production agents, multi-silicon clouds, and platforms that grow from MVPs to trillion-parameter workloads. Sessions also examine vLLM speculative decoding on NVIDIA Blackwell, hidden engine bugs, token-level FinOps, network protocols that constrain throughput, and the data pipelines required to keep accelerators productive. Together, these connections frame inference engineering as a control problem across hardware, engines, models, policies, and product-level latency and reliability targets—not merely as low-level kernel optimization.

## Conference Context
It extends production ML serving, distributed systems, GPU infrastructure, and web-performance engineering. LLMs added new constraints: token streaming, long prompts, context caching, tool latency, and rapidly changing model/provider economics.

## Significance
The same prompt can be unusable or profitable depending on latency, throughput, context size, and cost. Inference engineering turns model capability into a dependable product surface.

## Applied Use
Measure end-to-end latency and token costs, separate prefill from generation costs, cache stable context, route tasks to the smallest adequate model, batch where possible, and monitor quality regressions when optimizing speed or cost.

It matters in chat products, coding agents, voice agents, search and RAG systems, enterprise assistants, on-device AI, and high-volume API products.

Invest in inference engineering once prototypes need predictable user experience, margins, scale, or reliability. It becomes critical when workloads are high-volume, latency-sensitive, or model-provider dependent.

## Active Use Cases
- Reducing token and GPU cost for agent workflows.
- Serving long-context or cached-context applications.
- Routing between frontier, small, local, and specialized models.
- Optimizing voice and interactive applications for low latency.

## Slide-Derived Scheduled Session Signals
- [[2026-06-29-daniel-han-special-topics-in-kernels-rl-reward-hacking-in-agents]] — Special topics in Kernels, RL, Reward Hacking in Agents
- [[2026-06-29-lee-robinson-recursive-model-improvement]] — Recursive Model Improvement
- [[2026-06-29-sarah-sachs-notion-s-token-town]] — Notion's Token Town
- [[2026-07-01-frank-coyle-why-agentic-systems-need-ontologies]] — Why Agentic Systems Need Ontologies
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one]] — Video Has No Memory. Here's How We Built One.

## Slide-Derived Supporting Decks
- [[youtube--I5W5QVAT8E-slides]] — Notion's Token Town — Sarah Sachs, Notion (12 extracted slide frames)
- [[youtube-mOf-PP4mVjA-slides]] — Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs (31 extracted slide frames)
- [[youtube-q4Tr-DknG2M-slides]] —  (12 extracted slide frames)
- [[youtube-Sir59K8ZDPU-slides]] — Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley (13 extracted slide frames)
- [[youtube-uIiA6DquRiE-slides]] — Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth (11 extracted slide frames)
- [[youtube-XV2oYi7kojc-slides]] — Demo: GLM 5.2 on DGX Station — Frontier Intelligence Under Your Desk — Ahmad Osman, Osmantic (6 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

## Transcript Digest Evidence
This section synthesizes 23 evidence-bound talk topic candidates across at least two talks.

### Cross-Talk Synthesis
These candidates focus on how runtime choices, local optimization, persistence, and rollout structure shape model behavior more than raw model size alone. The key variation is between compute-heavy scaling and system-level efficiency, with several talks arguing that useful capability often appears when harnesses, routing, and deployment constraints are improved together.

### Constituent Talk Evidence
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering|The Golden Age of AI Engineering]] — Choosing the right host or environment for each agent task.
  - Transcript: [[youtube-pMggiOb18tc-transcript]]
  - Evidence: "My agent should be able to connect to any of my machines. They should know which work can be done in the cloud or which work requires my local machine."
- [[2026-06-29-lee-robinson-recursive-model-improvement|Recursive Model Improvement]] — The compute, data-center, and chip expansion needed to support larger parallel training efforts.
  - Transcript: [[youtube-q4Tr-DknG2M-transcript]]
  - Evidence: "Now, how we scale these loops, both the inner and outer loops, also comes down to scaling the amount of compute we have."
- [[2026-06-29-sarah-sachs-notion-s-token-town|Notion's Token Town]] — Moving deterministic or low-complexity work off LLMs and onto CPUs or lightweight services.
  - Transcript: [[youtube--I5W5QVAT8E-transcript]]
  - Evidence: "So, be prepared now. And the last thing is CPUs over GPUs. Um, we've we've recently launched something at notion called workers."
- [[2026-06-29-will-brown-the-prime-intellect-stack|The Prime Intellect Stack]] — Training and rollout management that overlaps slow episodes by keeping inference and training separate.
  - Transcript: [[youtube-V-EDrhIhHzQ-transcript]]
  - Evidence: "And so Primer RL has been async from the ground up. Uh so I think async RL is one of those things that I think people were kind of one foot in and one foot out and a lot of training frameworks you see them uh will still kind of support synchronous training."
- [[2026-06-29-zach-blumenfeld-ai-on-your-lakehouse-context-comes-in-shapes-not-queries|AI on Your Lakehouse: Context Comes in Shapes, Not Queries]] — Using graph shapes to supply agents with the right context for lakehouse reasoning.
  - Transcript: [[youtube-kRkcNOsRyYg-transcript]]
  - Evidence: "times what can happen is you're given these tools like text to SQL and vector search and nowadays we don't really have trouble accessing that data Um, but sometimes there are still some challenges around how do you give your agent the right type of context, whether or not they can see all the data"
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1']] — The choice of isolation primitive for a single sandboxed workload.
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
  - Evidence: "There are many many parts of a sandbox cloud, but we'll specifically focus on runtime. So, how can we run uh sandbox on one node securely?"
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2']] — Saving sandbox state so long-running tasks can resume after failure or backtrack across branches.
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
  - Evidence: "And let's go into like three big use cases on what persistence can unlock, right? So, counterintuitively, persistence actually helps reliability and scale."
- [[2026-06-30-eve-bouffard-imagination-engineering|Imagination Engineering]] — Publishing one's reasoning and stream of consciousness for others to inspect.
  - Transcript: [[youtube-Z2Erdirpudo-transcript]]
  - Evidence: "But what about thinking in public? And it's basically what PG is doing, thinking in public."
- [[2026-06-30-ishan-anand-will-ai-predict-people-like-we-predict-the-weather-alternate-title-a-field-guide-to-synthetic-personas-for-market-research|Will AI predict people like we predict the weather? (alternate title “A field guide to synthetic personas for market research”)]] — The need to provide enough world context in the prompt so the model does not infer hidden variables.
  - Transcript: [[youtube-YnNF55QV0zs-transcript]]
  - Evidence: "And maybe this is a rich person, so they're more likely to purchase. And so the lesson is, we need to richly ground our personas in the personality, the context, and bizarrely, even the study's own construction."
- [[2026-07-01-nader-khalil-state-of-the-union-why-local-why-now|State of the Union: Why Local, Why Now]] — Performance work on smaller devices through tuning, quantization, and configuration.
  - Transcript: [[youtube-KB41dTlX1Uc-transcript]]
  - Evidence: "Uh doing a lot of work with the like tuning the models like quantizing the models uh to you know be fit for local."
- [[2026-07-01-nader-khalil-state-of-the-union-why-local-why-now-11-10am-11-30am-track-4-420|State of the Union: Why Local, Why Now]] — The talk's main claim that local AI has crossed an inflection point because models and harnesses improved together.
  - Transcript: [[youtube-KB41dTlX1Uc-transcript]]
  - Evidence: "And the reason why is we hit an inflection point this year. Not only did the models get really good, but the harnesses got really good."
- [[2026-07-01-yohei-nakajima-active-graph-agent-runtime-babyagi-4|Active Graph Agent Runtime (BabyAGI 4)]] — Using policies to constrain edits, approvals, and safe self-modification.
  - Transcript: [[youtube-khVX_BUnEwU-transcript]]
  - Evidence: "I'll come back to it, but for example, things like a source article that you found in research, you might be fine with adding, but if you're changing a prompt, maybe you want human in the loop."

## Connections
- [[2026-07-01-nishant-gupta-operating-distributed-inference-systems-at-scale]] — Operating Distributed Inference Systems at Scale; [[nishant-gupta|Nishant Gupta]], [[naman-ahuja|Naman Ahuja]] (Day 4 — Session Day 3 · 10:45am-11:05am · Inference; official schedule)
- [[2026-06-29-bogdan-gaza-running-a-20t-token-data-pipeline-infrastructure-lessons-from-production]] — Running a 20T-Token Data Pipeline: Infrastructure Lessons from Production; [[bogdan-gaza|Bogdan Gaza]] (Day 2 — Session Day 1 · 3:20pm-3:40pm · Expo Stage 3 SW; official schedule)
- [[2026-06-29-du-an-lightfoot-agents-that-own-their-inference-building-production-ai-agents-on-dedicated-gpus]] — Agents That Own Their Inference: Building Production AI Agents on Dedicated GPUs; [[du-an-lightfoot|Du'an Lightfoot]] (Day 1 — Workshop Day · 9:00am-11:00am · Track 7; official schedule)
- [[2026-06-29-zain-hasan-open-source-inference-engineering-for-the-agentic-era]] — Open-Source Inference Engineering for the Agentic Era; [[zain-hasan|Zain Hasan]], [[yubo-wang|Yubo Wang]], [[qingyang-wu|Qingyang Wu]], [[jue-wang|Jue Wang]] (Day 1 — Workshop Day · 9:00am-11:00am · Workshops Day 1; official schedule)
- [[2026-06-30-nicholas-arcolano-tokenmaxxing-is-the-new-lines-of-code]] — Tokenmaxxing is the New "Lines of Code"; [[nicholas-arcolano|Nicholas Arcolano]] (Day 3 — Session Day 2 · 1:30pm-1:50pm · AI Architects: Tokenmaxxing; official schedule)
- [[2026-07-01-daniel-kim-all-the-things-we-have-to-do-to-satisfy-your-insatiable-need-for-tokens]] — All the Things We Have to Do to Satisfy Your Insatiable Need for Tokens; [[daniel-kim|Daniel Kim]], [[michelle-nguyen|Michelle Nguyen]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Inference; official schedule)
- [[2026-07-01-sheilah-kirui-seeing-the-plumbing-profiling-vllm-speculative-decoding-on-nvidia-blackwell]] — Seeing the Plumbing: Profiling vLLM Speculative Decoding on NVIDIA Blackwell; [[sheilah-kirui|Sheilah Kirui]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Expo Stage 2 NW; official schedule)
- [[2026-06-29-harshul-jain-2-hr-deep-dive-on-llm-inference-at-scale-part-1-of-2]] — 2 hr deep dive on LLM Inference at Scale — Part 1 of 2; [[harshul-jain|Harshul Jain]], [[tanmay-sah|Tanmay Sah]] (Day 1 — Workshop Day · 12:10pm-1:10pm · Workshops Day 1; official schedule)
- [[2026-06-29-harshul-jain-2-hr-deep-dive-on-llm-inference-at-scale-part-2-of-2]] — 2 hr deep dive on LLM Inference at Scale — Part 2 of 2; [[harshul-jain|Harshul Jain]], [[tanmay-sah|Tanmay Sah]] (Day 1 — Workshop Day · 1:15pm-2:15pm · Workshops Day 1; official schedule)
- [[2026-07-01-qianru-lao-routing-llm-inference-in-production-from-engine-signals-to-policy]] — Routing LLM Inference in Production: From Engine Signals to Policy; [[qianru-lao|Qianru Lao]], [[lu-zhang|Lu Zhang]] (Day 4 — Session Day 3 · 11:10am-11:30am · Inference; official schedule)
- [[2026-07-01-byung-gon-gon-chun-the-frontier-ai-inference-cloud-for-agents]] — The Frontier AI Inference Cloud for Agents; [[byung-gon-gon-chun|Byung-Gon (Gon) Chun]] (Day 4 — Session Day 3 · 2:25pm-2:45pm · Inference; official schedule)
- [[2026-06-29-charles-frye-what-is-an-inference-engine-anyway]] — What is an Inference Engine, Anyway?; [[charles-frye|Charles Frye]] (Day 1 — Workshop Day · 11:05am-12:05pm · Workshops Day 1; official schedule)
- [[2026-07-01-tisha-chawla-finops-for-ai-agents-who-spent-all-the-tokens]] — FinOps for AI Agents: Who Spent All the Tokens?; [[tisha-chawla|Tisha Chawla]], [[susheem-koul|Susheem Koul]] (Day 4 — Session Day 3 · 11:10am-11:30am · AI Architects: AI Factories; official schedule)
- [[2026-07-01-rita-zhang-vertical-mobility-building-an-ai-inference-platform-that-scales-from-mvp-to-trillion-parameter-workloads]] — Vertical Mobility: Building an AI Inference Platform That Scales from MVP to Trillion-Parameter Workloads; [[rita-zhang|Rita Zhang]], [[sitanshu-gupta|Sitanshu Gupta]] (Day 4 — Session Day 3 · 12:05pm-12:25pm · Inference; official schedule)
- [[2026-07-01-philip-kiely-what-s-new-in-inference-engineering]] — What's New in Inference Engineering; [[philip-kiely|Philip Kiely]] (Day 4 — Session Day 3 · 1:30pm-1:50pm · Inference; official schedule)
- [[2026-07-01-asaf-gardin-two-bugs-that-hid-in-plain-sight-a-vllm-debugging-detective-story]] — Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story; [[asaf-gardin|Asaf Gardin]], [[yuval-belfer|Yuval Belfer]] (Day 4 — Session Day 3 · 3:20pm-3:40pm · Inference; official schedule)
- [[2026-06-30-session-your-stack-has-a-latency-problem-you-can-t-see]] — Your Stack Has a Latency Problem You Can’t See; speaker TBD (Day 3 — Session Day 2 · 2:25pm-2:45pm · Expo Stage 4 SE; official schedule)
- [[2026-06-30-alex-campos-inference-performance-as-a-competitive-advantage]] — Inference performance as a competitive advantage; [[alex-campos|Alex Campos]], [[yunmo-koo|Yunmo Koo]] (Day 3 — Session Day 2 · 2:50pm-3:10pm · Expo Stage 1 NE; official schedule)
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]] — The Golden Age of AI Engineering; [[alexander-embiricos|Alexander Embiricos]], [[romain-huet|Romain Huet]] (Day 2 — Session Day 1 · 9:25am-9:45am · Software Factories; verified event YouTube resource; via [[youtube-pMggiOb18tc]])
- [[2026-06-29-simran-arora-can-llms-write-fast-multi-gpu-kernels-we-built-a-benchmark-to-find-out]] — Can LLMs write fast multi-GPU kernels? We built a benchmark to find out.; [[simran-arora|Simran Arora]] (Day 2 — Session Day 1 · 12:05pm-12:25pm · Expo Stage 3 SW; official schedule)
- [[2026-06-30-mingsheng-hong-from-tokenmaxxing-to-trusted-throughput]] — From Tokenmaxxing to Trusted Throughput; [[mingsheng-hong|Mingsheng Hong]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · AI-Native Enterprises; official schedule)
- [[2026-06-30-tarun-sunkaraneni-ray-actors-vision-tokens-and-the-gil-engineering-an-sft-data-pipeline-that-keeps-gpus-busy]] — Ray Actors, Vision Tokens, and the GIL: Engineering an SFT Data Pipeline That Keeps GPUs Busy; [[tarun-sunkaraneni|Tarun Sunkaraneni]] (Day 3 — Session Day 2 · 3:45pm-4:05pm · Expo Stage 4 SE; official schedule)
- [[2026-07-01-john-ousterhout-tcp-and-rdma-are-killing-inference-throughput-homa-can-fix-it]] — TCP and RDMA are Killing Inference Throughput; Homa can Fix It; [[john-ousterhout|John Ousterhout]] (Day 4 — Session Day 3 · 9:20am-9:40am · Software Factories; official schedule)
- [[2026-06-30-david-corbitt-inference-is-the-new-training-loop-architecting-high-reliability-agents-and-continuous-ai-systems]] — Inference is the New Training Loop: Architecting High-Reliability Agents and Continuous AI Systems; [[david-corbitt|David Corbitt]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Posttraining & Midtraining; official schedule)

- [[neil-zeghidour|Neil Zeghidour]]
- [[harshul-jain|Harshul Jain]]
- [[tanmay-sah|Tanmay Sah]]
- [[yuval-belfer|Yuval Belfer]]
- [[ahmad-osman|Ahmad Osman]]
- [[filip-makraduli|Filip Makraduli]]
- [[nishant-gupta|Nishant Gupta]]
- [[naman-ahuja|Naman Ahuja]]
- [[bogdan-gaza|Bogdan Gaza]]
- [[du-an-lightfoot|Du'an Lightfoot]]
- [[zain-hasan|Zain Hasan]]
- [[yubo-wang|Yubo Wang]]
- [[qingyang-wu|Qingyang Wu]]
- [[jue-wang|Jue Wang]]
- [[nicholas-arcolano|Nicholas Arcolano]]
- [[daniel-kim|Daniel Kim]]
- [[michelle-nguyen|Michelle Nguyen]]
- [[sheilah-kirui|Sheilah Kirui]]
- [[qianru-lao|Qianru Lao]]
- [[lu-zhang|Lu Zhang]]
- [[byung-gon-gon-chun|Byung-Gon (Gon) Chun]]
- [[charles-frye|Charles Frye]]
- [[tisha-chawla|Tisha Chawla]]
- [[susheem-koul|Susheem Koul]]

- [[together-ai|Together AI]]
- [[nvidia|NVIDIA]]
- [[openai|OpenAI]]
- [[meta|Meta]]
- [[friendliai|FriendliAI]]
- [[microsoft|Microsoft]]
- [[anthropic|Anthropic]]
- [[ai21|AI21]]
- [[towards-ai|Towards AI]]
- [[superlinked|Superlinked]]
- [[google-deepmind|Google DeepMind]]
- [[gradium|Gradium]]
- [[audible|Audible]]
- [[zions-bancorporation|Zions Bancorporation]]
- [[coreweave|Coreweave]]
- [[stanford-university|Stanford University]]
- [[red-hat|Red Hat]]
- [[mckinsey-and-company|McKinsey & Company]]

- [[google|Google]]

- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]] — The Golden Age of AI Engineering; [[alexander-embiricos|Alexander Embiricos]], [[romain-huet|Romain Huet]] (Day 2 — Session Day 1 · 9:25am-9:45am · Software Factories; related YouTube resource; via [[youtube-pMggiOb18tc]])

- [[laurie-voss|Laurie Voss]]
- [[swyx|swyx]]
- [[christopher-manning|Christopher Manning]]

- [[arize-ai|Arize AI]]
- [[stripe|Stripe]]

- [[youtube-2IxD9OB3XuQ-slides]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI (24 extracted slide frames)
- [[youtube-vljxQZfJ9wY-slides]] — Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs (12 extracted slide frames)

- [[2026-07-01-sujee-maniyam-optimizing-open-models-for-production-grade-inference]] — Optimizing Open Models for Production Grade Inference; [[sujee-maniyam|Sujee Maniyam]], [[dylan-bristot|Dylan Bristot]] (Day 4 — Session Day 3 · 2:25pm-2:45pm · Expo Stage 1 NE; official schedule)

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 63 | Related pages outside the main evidence categories. |
| resources | 11 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 28 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 39 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| transcripts | 15 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-daniel-han-special-topics-in-kernels-rl-reward-hacking-in-agents]]
- [[2026-06-29-lee-robinson-recursive-model-improvement]]
- [[2026-06-29-sarah-sachs-notion-s-token-town]]
- [[2026-07-01-frank-coyle-why-agentic-systems-need-ontologies]]
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one]]
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]]

### Resources
- [[youtube-pMggiOb18tc]]
- [[youtube-V-EDrhIhHzQ]]
- [[youtube-OqM67QG_Ikk]]
- [[youtube-I2cbIws9j10]]
- [[youtube-iCj_ATyThvc]]
- [[youtube-uIiA6DquRiE]]

### Slides
- [[youtube--I5W5QVAT8E-slides]]
- [[youtube-mOf-PP4mVjA-slides]]
- [[youtube-q4Tr-DknG2M-slides]]
- [[youtube-Sir59K8ZDPU-slides]]
- [[youtube-uIiA6DquRiE-slides]]
- [[youtube-XV2oYi7kojc-slides]]

### Transcripts
- [[youtube-pMggiOb18tc-transcript]]
- [[youtube-q4Tr-DknG2M-transcript]]
- [[youtube--I5W5QVAT8E-transcript]]
- [[youtube-V-EDrhIhHzQ-transcript]]
- [[youtube-kRkcNOsRyYg-transcript]]
- [[youtube-OqM67QG_Ikk-transcript]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.

### Linked Sessions
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering|The Golden Age of AI Engineering]]
- [[2026-06-29-lee-robinson-recursive-model-improvement|Recursive Model Improvement]]
- [[2026-06-29-sarah-sachs-notion-s-token-town|Notion's Token Town]]
- [[2026-06-29-will-brown-the-prime-intellect-stack|The Prime Intellect Stack]]
- [[2026-06-29-zach-blumenfeld-ai-on-your-lakehouse-context-comes-in-shapes-not-queries|AI on Your Lakehouse: Context Comes in Shapes, Not Queries]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1']]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2']]
- [[2026-06-30-eve-bouffard-imagination-engineering|Imagination Engineering]]
- [[2026-06-30-ishan-anand-will-ai-predict-people-like-we-predict-the-weather-alternate-title-a-field-guide-to-synthetic-personas-for-market-research|Will AI predict people like we predict the weather? (alternate title “A field guide to synthetic personas for market research”)]]
- [[2026-07-01-nader-khalil-state-of-the-union-why-local-why-now|State of the Union: Why Local, Why Now]]

### Media Signals
- `youtube-V-EDrhIhHzQ` — 10,228 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-V-EDrhIhHzQ`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-V-EDrhIhHzQ`: model, harness, well, doing, environment, training, able, models.
- Slide-derived themes for `youtube-V-EDrhIhHzQ`: engineering, future, prime, intellect, stack, open.
- Evidence links for `youtube-V-EDrhIhHzQ` (primary event evidence): [[youtube-V-EDrhIhHzQ]], [[youtube-V-EDrhIhHzQ-transcript]], [[youtube-V-EDrhIhHzQ-slides]]
- `youtube-OqM67QG_Ikk` — 7,738 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-OqM67QG_Ikk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-OqM67QG_Ikk`: kernel, many, system, code, host, guest, block, running.
- Slide-derived themes for `youtube-OqM67QG_Ikk`: engineering, sandbox, platform, track, july, security, fork, fleet.
- Evidence links for `youtube-OqM67QG_Ikk` (primary event evidence): [[youtube-OqM67QG_Ikk]], [[youtube-OqM67QG_Ikk-transcript]], [[youtube-OqM67QG_Ikk-slides]]
- `youtube-I2cbIws9j10` — 91,792 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-I2cbIws9j10`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: choosing, model, quality, dominates, agentic, capabilities, customization, support.
- Evidence links for `youtube-I2cbIws9j10` (primary event evidence): [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
- `youtube-iCj_ATyThvc` — 1,795 transcript words; 4 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-iCj_ATyThvc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-iCj_ATyThvc`: research, auto, aiden, human, training, ideas, data, competition.
- Slide-derived themes for `youtube-iCj_ATyThvc`: code, golf, neural, networks, train, best, language, model.
- Evidence links for `youtube-iCj_ATyThvc` (primary event evidence): [[youtube-iCj_ATyThvc]], [[youtube-iCj_ATyThvc-transcript]], [[youtube-iCj_ATyThvc-slides]]
- `youtube-uIiA6DquRiE` — 25,283 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-uIiA6DquRiE`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-uIiA6DquRiE`: model, models, source, open, benchmark, question, okay, accuracy.
- Slide-derived themes for `youtube-uIiA6DquRiE`: smaller, model, high, extra, license, businesses, users, open.
- Evidence links for `youtube-uIiA6DquRiE` (primary event evidence): [[youtube-uIiA6DquRiE]], [[youtube-uIiA6DquRiE-transcript]], [[youtube-uIiA6DquRiE-slides]]
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-4sX_He5c4sI`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: lots, examples, stream, starts, july, land, king, chief.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube-htM02KMNZnk` — 89,050 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-htM02KMNZnk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-htM02KMNZnk`: model, code, models, loop, well, software, first, team.
- Slide-derived themes for `youtube-htM02KMNZnk`: apps, github, copilot, welcome, engineer, fair, single, line.
- Evidence links for `youtube-htM02KMNZnk` (primary event evidence): [[youtube-htM02KMNZnk]], [[youtube-htM02KMNZnk-transcript]], [[youtube-htM02KMNZnk-slides]], [[youtube-htM02KMNZnk-dense-slides]], [[youtube-htM02KMNZnk-reconstructed-slides]]
- `youtube-gmTHs5T_YAE` — source page linked; role: supporting context only.
- Evidence links for `youtube-gmTHs5T_YAE` (supporting context only): [[youtube-gmTHs5T_YAE]], [[youtube-gmTHs5T_YAE-slides]], [[youtube-gmTHs5T_YAE-dense-slides]], [[youtube-gmTHs5T_YAE-reconstructed-slides]]
- `youtube-DeFF3J8T5Pk` — 9 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-DeFF3J8T5Pk`: open, source, engines, getting, better, quickly, finally, makes.
- Evidence links for `youtube-DeFF3J8T5Pk` (supporting context only): [[youtube-DeFF3J8T5Pk]], [[youtube-DeFF3J8T5Pk-slides]], [[youtube-DeFF3J8T5Pk-dense-slides]], [[youtube-DeFF3J8T5Pk-reconstructed-slides]]
- `youtube-tzRvcTEapzo` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-tzRvcTEapzo`: mixture, experts, queen, research, focus, training, cores, buffers.
- Evidence links for `youtube-tzRvcTEapzo` (supporting context only): [[youtube-tzRvcTEapzo]], [[youtube-tzRvcTEapzo-slides]], [[youtube-tzRvcTEapzo-dense-slides]], [[youtube-tzRvcTEapzo-reconstructed-slides]]
