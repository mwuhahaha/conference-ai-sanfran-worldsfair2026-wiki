---
title: "Inference Engineering"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---
# Inference Engineering

## Overview
Inference engineering is the practice of making AI model serving reliable, fast, cost-aware, and fit for product constraints. It covers model selection, batching, caching, routing, quantization, GPU utilization, latency budgets, observability, and fallback behavior.

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

## Slide-Derived Supporting Decks
- [[youtube-q4Tr-DknG2M-slides]] —  (12 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

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
| resources | 10 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 23 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 25 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| transcripts | 6 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-07-01-nishant-gupta-operating-distributed-inference-systems-at-scale]]
- [[2026-06-29-bogdan-gaza-running-a-20t-token-data-pipeline-infrastructure-lessons-from-production]]
- [[2026-06-29-du-an-lightfoot-agents-that-own-their-inference-building-production-ai-agents-on-dedicated-gpus]]
- [[2026-06-29-zain-hasan-open-source-inference-engineering-for-the-agentic-era]]
- [[2026-06-30-nicholas-arcolano-tokenmaxxing-is-the-new-lines-of-code]]
- [[2026-07-01-daniel-kim-all-the-things-we-have-to-do-to-satisfy-your-insatiable-need-for-tokens]]

### Resources
- [[youtube-pMggiOb18tc]]
- [[youtube-V-EDrhIhHzQ]]
- [[youtube-I2cbIws9j10]]
- [[youtube-4sX_He5c4sI]]
- [[youtube-OqM67QG_Ikk]]
- [[youtube-htM02KMNZnk]]

### Slides
- [[youtube-q4Tr-DknG2M-slides]]
- [[youtube-2IxD9OB3XuQ-slides]]
- [[youtube-vljxQZfJ9wY-slides]]
- [[youtube-V-EDrhIhHzQ-slides]]
- [[youtube-I2cbIws9j10-slides]]
- [[youtube-I2cbIws9j10-dense-slides]]

### Transcripts
- [[youtube-V-EDrhIhHzQ-transcript]]
- [[youtube-I2cbIws9j10-transcript]]
- [[youtube-4sX_He5c4sI-transcript]]
- [[youtube-OqM67QG_Ikk-transcript]]
- [[youtube-htM02KMNZnk-transcript]]
- [[youtube-iCj_ATyThvc-transcript]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.

### Linked Sessions
- [[2026-07-01-nishant-gupta-operating-distributed-inference-systems-at-scale|Operating Distributed Inference Systems at Scale]]
- [[2026-06-29-bogdan-gaza-running-a-20t-token-data-pipeline-infrastructure-lessons-from-production|Running a 20T-Token Data Pipeline: Infrastructure Lessons from Production]]
- [[2026-06-29-du-an-lightfoot-agents-that-own-their-inference-building-production-ai-agents-on-dedicated-gpus|>-]]
- [[2026-06-29-zain-hasan-open-source-inference-engineering-for-the-agentic-era|Open-Source Inference Engineering for the Agentic Era]]
- [[2026-06-30-nicholas-arcolano-tokenmaxxing-is-the-new-lines-of-code|Tokenmaxxing is the New \"Lines of Code\]]
- [[2026-07-01-daniel-kim-all-the-things-we-have-to-do-to-satisfy-your-insatiable-need-for-tokens|All the Things We Have to Do to Satisfy Your Insatiable Need for Tokens]]
- [[2026-07-01-sheilah-kirui-seeing-the-plumbing-profiling-vllm-speculative-decoding-on-nvidia-blackwell|Seeing the Plumbing: Profiling vLLM Speculative Decoding on NVIDIA Blackwell]]
- [[2026-06-29-harshul-jain-2-hr-deep-dive-on-llm-inference-at-scale-part-1-of-2|2 hr deep dive on LLM Inference at Scale — Part 1 of 2]]
- [[2026-06-29-harshul-jain-2-hr-deep-dive-on-llm-inference-at-scale-part-2-of-2|2 hr deep dive on LLM Inference at Scale — Part 2 of 2]]
- [[2026-07-01-qianru-lao-routing-llm-inference-in-production-from-engine-signals-to-policy|Routing LLM Inference in Production: From Engine Signals to Policy]]

### Media Signals
- `youtube-V-EDrhIhHzQ` — 10,228 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-V-EDrhIhHzQ`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-V-EDrhIhHzQ`: model, harness, well, doing, environment, training, able, models.
- Slide-derived themes for `youtube-V-EDrhIhHzQ`: engineering, future, prime, intellect, stack, open.
- Evidence links for `youtube-V-EDrhIhHzQ` (primary event evidence): [[youtube-V-EDrhIhHzQ]], [[youtube-V-EDrhIhHzQ-transcript]], [[youtube-V-EDrhIhHzQ-slides]]
- `youtube-I2cbIws9j10` — 91,792 transcript words; 7 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-I2cbIws9j10`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: context, window, selects, response, facts, retry, coerce, rollback.
- Evidence links for `youtube-I2cbIws9j10` (primary event evidence): [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-4sX_He5c4sI`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: system, prompt, examples, tools, lots, claude, gets, smarter.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube-OqM67QG_Ikk` — 7,738 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-OqM67QG_Ikk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-OqM67QG_Ikk`: kernel, many, system, code, host, guest, block, running.
- Slide-derived themes for `youtube-OqM67QG_Ikk`: engineering, sandbox, platform, track, july, security, fork, fleet.
- Evidence links for `youtube-OqM67QG_Ikk` (primary event evidence): [[youtube-OqM67QG_Ikk]], [[youtube-OqM67QG_Ikk-transcript]], [[youtube-OqM67QG_Ikk-slides]]
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
- `youtube-gmTHs5T_YAE` — source page linked; role: supporting context only.
- Evidence links for `youtube-gmTHs5T_YAE` (supporting context only): [[youtube-gmTHs5T_YAE]], [[youtube-gmTHs5T_YAE-slides]], [[youtube-gmTHs5T_YAE-dense-slides]], [[youtube-gmTHs5T_YAE-reconstructed-slides]]
- `youtube-DeFF3J8T5Pk` — source page linked; role: supporting context only.
- Evidence links for `youtube-DeFF3J8T5Pk` (supporting context only): [[youtube-DeFF3J8T5Pk]], [[youtube-DeFF3J8T5Pk-slides]], [[youtube-DeFF3J8T5Pk-dense-slides]], [[youtube-DeFF3J8T5Pk-reconstructed-slides]]
- `youtube-tzRvcTEapzo` — 5 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-tzRvcTEapzo`: models, training, creator, tokens, downloads, former, google, researcher.
- Evidence links for `youtube-tzRvcTEapzo` (supporting context only): [[youtube-tzRvcTEapzo]], [[youtube-tzRvcTEapzo-slides]], [[youtube-tzRvcTEapzo-dense-slides]], [[youtube-tzRvcTEapzo-reconstructed-slides]]
