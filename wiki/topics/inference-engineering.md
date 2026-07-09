---
title: "Inference Engineering"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---
# Inference Engineering

## Synopsis
Inference engineering is the practice of making AI model serving reliable, fast, cost-aware, and fit for product constraints. It covers model selection, batching, caching, routing, quantization, GPU utilization, latency budgets, observability, and fallback behavior.

## Origin And Context
It extends production ML serving, distributed systems, GPU infrastructure, and web-performance engineering. LLMs added new constraints: token streaming, long prompts, context caching, tool latency, and rapidly changing model/provider economics.

## Why It Matters
The same prompt can be unusable or profitable depending on latency, throughput, context size, and cost. Inference engineering turns model capability into a dependable product surface.

## How To Use It
Measure end-to-end latency and token costs, separate prefill from generation costs, cache stable context, route tasks to the smallest adequate model, batch where possible, and monitor quality regressions when optimizing speed or cost.

## Where It Is Useful
It matters in chat products, coding agents, voice agents, search and RAG systems, enterprise assistants, on-device AI, and high-volume API products.

## When To Use It
Invest in inference engineering once prototypes need predictable user experience, margins, scale, or reliability. It becomes critical when workloads are high-volume, latency-sensitive, or model-provider dependent.

## Active Use Cases
- Reducing token and GPU cost for agent workflows.
- Serving long-context or cached-context applications.
- Routing between frontier, small, local, and specialized models.
- Optimizing voice and interactive applications for low latency.

## Related Slide Decks
- [[youtube-2IxD9OB3XuQ-slides]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI (24 extracted slide frames)
- [[youtube-vljxQZfJ9wY-slides]] — Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs (12 extracted slide frames)

## Related Scheduled Sessions
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
- [[2026-06-29-simran-arora-can-llms-write-fast-multi-gpu-kernels-we-built-a-benchmark-to-find-out]] — Can LLMs write fast multi-GPU kernels? We built a benchmark to find out.; [[simran-arora|Simran Arora]] (Day 2 — Session Day 1 · 12:05pm-12:25pm · Expo Stage 3 SW; official schedule)
- [[2026-06-30-mingsheng-hong-from-tokenmaxxing-to-trusted-throughput]] — From Tokenmaxxing to Trusted Throughput; [[mingsheng-hong|Mingsheng Hong]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · AI-Native Enterprises; official schedule)
- [[2026-06-30-tarun-sunkaraneni-ray-actors-vision-tokens-and-the-gil-engineering-an-sft-data-pipeline-that-keeps-gpus-busy]] — Ray Actors, Vision Tokens, and the GIL: Engineering an SFT Data Pipeline That Keeps GPUs Busy; [[tarun-sunkaraneni|Tarun Sunkaraneni]] (Day 3 — Session Day 2 · 3:45pm-4:05pm · Expo Stage 4 SE; official schedule)
- [[2026-07-01-john-ousterhout-tcp-and-rdma-are-killing-inference-throughput-homa-can-fix-it]] — TCP and RDMA are Killing Inference Throughput; Homa can Fix It; [[john-ousterhout|John Ousterhout]] (Day 4 — Session Day 3 · 9:20am-9:40am · Software Factories; official schedule)
- [[2026-06-30-david-corbitt-inference-is-the-new-training-loop-architecting-high-reliability-agents-and-continuous-ai-systems]] — Inference is the New Training Loop: Architecting High-Reliability Agents and Continuous AI Systems; [[david-corbitt|David Corbitt]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Posttraining & Midtraining; official schedule)
- [[2026-07-01-sujee-maniyam-optimizing-open-models-for-production-grade-inference]] — Optimizing Open Models for Production Grade Inference; [[sujee-maniyam|Sujee Maniyam]], [[dylan-bristot|Dylan Bristot]] (Day 4 — Session Day 3 · 2:25pm-2:45pm · Expo Stage 1 NE; official schedule)

## Related People
- [[laurie-voss|Laurie Voss]]
- [[neil-zeghidour|Neil Zeghidour]]
- [[harshul-jain|Harshul Jain]]
- [[tanmay-sah|Tanmay Sah]]
- [[swyx|swyx]]
- [[yuval-belfer|Yuval Belfer]]
- [[ahmad-osman|Ahmad Osman]]
- [[christopher-manning|Christopher Manning]]
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

## Related Companies
- [[together-ai|Together AI]]
- [[arize-ai|Arize AI]]
- [[nvidia|NVIDIA]]
- [[anthropic|Anthropic]]
- [[meta|Meta]]
- [[friendliai|FriendliAI]]
- [[microsoft|Microsoft]]
- [[ai21|AI21]]
- [[towards-ai|Towards AI]]
- [[superlinked|Superlinked]]
- [[stripe|Stripe]]
- [[gradium|Gradium]]
- [[audible|Audible]]
- [[zions-bancorporation|Zions Bancorporation]]
- [[openai|OpenAI]]
- [[coreweave|Coreweave]]
- [[stanford-university|Stanford University]]
- [[red-hat|Red Hat]]

## Transcript And Resource Support
### Transcript-backed resources
- [[youtube-r305-aQTaU0]] — Text Diffusion — Brendan O’Donoghue, Google DeepMind
- [[youtube-vh2VGuQ3zhY]] — The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica
- [[youtube-fWXJM-J0ZB8]] — Frontier results, on device - RL Nabors, Arize
- [[youtube-TUnPNY4E2fw]] — Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI
- [[youtube-_B4Pv9ttFgY]] — Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google
- [[youtube-Rx8f05JI_WA]] — SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI
- [[youtube-zDGHt0LB-dA]] — GPU Cloud Deployment Without Leaving Your IDE — Audry Hsu, RunPod
- [[youtube-SS-A8sE7hkw]] — Sovereign Escape Velocity: Ownership w Open Models — Gus Martins, & Ian Ballantyne, Google DeepMind
- [[youtube-KLSuFPj2ld0]] — Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe
- [[youtube-65X0pQ6Lmbg]] — Voice In, Visuals Out: The Agony and the Ecstasy - Allen Pike, Forestwalk Labs
- [[youtube-dRmWYHuIJxM]] — We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco
- [[youtube-I2cbIws9j10]] — WF26: Harness Engineering & Startup Battlefield ft. Garry Tan, Mike Krieger, @t3dotgg , DSPy
- [[youtube-pmoDeA3RBZY]] — Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw
- [[youtube-HvZXAOZ3iv8]] — What Lies Beneath the API — Benjamin Cowen, Modal
- [[youtube-uiP88SpCi1Q]] — Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS
- [[youtube-HsxQICTLF84]] — Building an ACP-Compatible Agent Live — Bennet Fenner, Zed
- [[youtube-spNAUEgq_A8]] — The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents
- [[youtube-ILdE7FaAjVA]] — Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod

### Quote signals
- “I'm talking today about text diffusion, which is kind of a more forward-looking research area at DeepMind.” — [[youtube-r305-aQTaU0]]
- “Most small language models uh for mobile and web are deployed with quantization, that is to say, 8-bit, 4-bit, and that can have a quarter disk and memory requirements.” — [[youtube-fWXJM-J0ZB8]]
- “Um you need to before you start doing anything, you need to know what it is that you're measuring.” — [[youtube-fWXJM-J0ZB8]]
- “So it's not just one pass, it does multiple passes, but it gets to attend to the future tokens and so on.” — [[youtube-r305-aQTaU0]]
- “All right, so So, when we're serving uh an auto regressive model, these these chips are memory bound.” — [[youtube-r305-aQTaU0]]

## Source-Derived Enrichment
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

### Talk Evidence
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

### Slide And Transcript Signals
- `youtube-APh1Vx0oLmQ` — 7 slide-derived text signals
- Slide-derived themes for `youtube-APh1Vx0oLmQ`: emerging, control, plane, autonomous, systems, deterministic, boundary, entropy.
- Evidence links for `youtube-APh1Vx0oLmQ`: [[youtube-APh1Vx0oLmQ]], [[youtube-APh1Vx0oLmQ-slides]], [[youtube-APh1Vx0oLmQ-dense-slides]], [[youtube-APh1Vx0oLmQ-reconstructed-slides]]
- `youtube-wFTVEDYVJT0` — 13,586 transcript words; 9 slide-derived text signals
- Transcript signals for `youtube-wFTVEDYVJT0`: nova, amazon, code, server, browser, able, open, click.
- Slide-derived themes for `youtube-wFTVEDYVJT0`: plan, execute, actions, achieve, specific, goals, agentic, tamera.
- Evidence links for `youtube-wFTVEDYVJT0`: [[youtube-wFTVEDYVJT0]], [[youtube-wFTVEDYVJT0-transcript]], [[youtube-wFTVEDYVJT0-slides]], [[youtube-wFTVEDYVJT0-dense-slides]], [[youtube-wFTVEDYVJT0-reconstructed-slides]]
- `youtube-tzRvcTEapzo` — 10 slide-derived text signals
- Slide-derived themes for `youtube-tzRvcTEapzo`: mixture, experts, queen, research, focus, training, cores, buffers.
- Evidence links for `youtube-tzRvcTEapzo`: [[youtube-tzRvcTEapzo]], [[youtube-tzRvcTEapzo-slides]], [[youtube-tzRvcTEapzo-dense-slides]], [[youtube-tzRvcTEapzo-reconstructed-slides]]
