---
title: "Coding Agents"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---

# Coding Agents

## Synopsis
Coding agents are AI systems that can inspect repositories, reason about requirements, edit files, run commands, test changes, and sometimes open pull requests or operate development tools. They move AI coding from autocomplete toward task execution.

## Origin And Context
They evolved from code completion, IDE assistants, program synthesis, CI automation, and software bots. The recent shift is tool use: agents can read context, make coordinated edits, run tests, and respond to feedback inside real development workflows.

## Why It Matters
Software work is full of local context, repetitive edits, dependency checks, and validation loops. Coding agents can compress that cycle, but only when they respect repository conventions, tests, review standards, and operational safety.

## How To Use It
Give the agent a narrow task, repository context, tests or acceptance criteria, and permission boundaries. Require it to read before editing, keep diffs scoped, run validation, report residual risk, and leave the workspace clean.

## Where It Is Useful
They are useful in feature slices, bug fixes, test generation, refactors, migrations, docs updates, dependency audits, and operational scripts.

## When To Use It
Use coding agents when the task has clear acceptance criteria and the repo has enough structure to validate changes. Keep humans in the loop for architecture decisions, risky production operations, and ambiguous product calls.

## Active Use Cases
- Bug fixes with local tests and deploy verification.
- Repository-wide mechanical updates with reviewable diffs.
- CI failure diagnosis and targeted remediation.
- Agentic software factories that coordinate planning, coding, testing, and release steps.

## Related Slide Decks
- [[youtube-I2cbIws9j10-slides]] — WF26: Harness Engineering & Startup Battlefield ft. Garry Tan, Mike Krieger, @t3dotgg , DSPy (80 extracted slide frames)

## Related Scheduled Sessions
- [[2026-06-29-will-bond-scaling-code-quality-building-ureview-uber-s-multi-agent-code-review-engine]] — Scaling Code Quality: Building uReview, Uber’s Multi-Agent Code Review Engine; [[will-bond|Will Bond]], [[ameya-ketkar|Ameya Ketkar]] (Day 2 — Session Day 1 · 12:05pm-12:25pm · AI-Native Enterprises; official schedule)
- [[2026-06-29-owen-halpert-give-your-coding-agents-the-power-of-turbogrep]] — Give your coding agents the power of turbogrep!; [[owen-halpert|Owen Halpert]] (Day 2 — Session Day 1 · 11:10am-11:30am · Expo Stage 1 NE; official schedule)
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one]] — Video Has No Memory. Here's How We Built One.; [[james-le|James Le]] (Day 4 — Session Day 3 · 2:25pm-2:45pm · Graphs; official schedule)
- [[2026-07-01-anirban-chatterjee-guide-verify-solve-the-engineering-discipline-agentic-development-demands]] — Guide, Verify, Solve: The Engineering Discipline Agentic Development Demands; [[anirban-chatterjee|Anirban Chatterjee]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Agentic Engineering; official schedule)
- [[2026-06-29-nnenna-ndukwe-how-to-build-quality-gates-into-agentic-coding-workflows]] — How to Build Quality Gates into Agentic Coding Workflows; [[nnenna-ndukwe|Nnenna Ndukwe]] (Day 1 — Workshop Day · 11:05am-12:05pm · Workshops Day 1; official schedule)
- [[2026-06-29-itamar-friedman-the-last-human-code-review-building-trust-in-ai-generated-code]] — The Last Human Code Review: Building Trust in AI-Generated Code; [[itamar-friedman|Itamar Friedman]] (Day 2 — Session Day 1 · 11:40am-12:00pm · AI Architects: Show my Workflow; official schedule)
- [[2026-06-30-laurie-voss-the-death-of-the-code-review]] — The Death of the Code Review; [[laurie-voss|Laurie Voss]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · AI Architects: Tokenmaxxing; official schedule)
- [[2026-06-29-eyal-blum-how-to-get-your-org-to-adopt-coding-agents-without-shipping-garbage]] — How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage); [[eyal-blum|Eyal Blum]] (Day 2 — Session Day 1 · 3:20pm-3:40pm · AI-Native Enterprises; official schedule)
- [[2026-06-30-adi-singh-the-next-trillion-users-of-the-internet-still-don-t-have-an-identity]] — The Next Trillion Users of the Internet Still Don't Have an Identity; [[adi-singh|Adi Singh]] (Day 3 — Session Day 2 · 2:50pm-3:10pm · Sandbox & Platform Engineering; official schedule)
- [[2026-07-01-ekaterina-deyneka-building-an-agentic-video-editor-for-mass-consumer]] — Building an Agentic Video Editor for Mass Consumer; [[ekaterina-deyneka|Ekaterina Deyneka]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Generative Media; official schedule)
- [[2026-07-01-denys-linkov-benchmarking-coding-agents-on-new-vs-legacy-code-bases]] — Benchmarking Coding Agents on New vs Legacy Code bases; [[denys-linkov|Denys Linkov]] (Day 4 — Session Day 3 · 12:05pm-12:25pm · Agentic Engineering; official schedule)
- [[2026-06-29-charlie-guo-cooking-with-codex]] — Cooking with Codex; [[charlie-guo|Charlie Guo]], [[gabriel-chua|Gabriel Chua]] (Day 1 — Workshop Day · 9:00am-11:00am · Workshops Day 1; official schedule)
- [[2026-06-29-yoni-michael-the-data-context-layer-why-data-engineering-agents-need-more-than-code-and-databases]] — The Data Context Layer: Why Data Engineering Agents Need More Than Code and Databases; [[yoni-michael|Yoni Michael]], [[brandon-callender|Brandon Callender]] (Day 1 — Workshop Day · 2:20pm-4:20pm · Track 2; official schedule)
- [[2026-06-30-ankit-jain-how-to-kill-the-code-review]] — How to Kill the Code Review; [[ankit-jain|Ankit Jain]] (Day 3 — Session Day 2 · 11:40am-12:00pm · AI Architects: Tokenmaxxing; official schedule)
- [[2026-06-30-kamalakannan-nandagopal-beyond-code-generation-api-context-for-agentic-engineering]] — Beyond Code Generation: API Context for Agentic Engineering; [[kamalakannan-nandagopal|Kamalakannan Nandagopal]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Expo Stage 2 NW; official schedule)
- [[2026-06-30-ben-holmes-llm-knowledge-bases-a-practical-guide]] — LLM Knowledge Bases: a practical guide; [[ben-holmes|Ben Holmes]] (Day 3 — Session Day 2 · 3:45pm-4:05pm · Memory & Continual Learning; official schedule)
- [[2026-07-01-vasant-kearney-healthcare-s-agent-bytecode-x12-as-the-harness-for-ai-agents]] — Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents; [[vasant-kearney|Vasant Kearney]] (Day 4 — Session Day 3 · 1:55pm-2:15pm · AI in Healthcare; official schedule)
- [[2026-06-29-aditya-gautam-modality-misalignment-and-originality-attribution-in-short-form-video-a-multi-agent-approach-at-platform-scale]] — Modality Misalignment and Originality Attribution in Short-Form Video: A Multi-Agent Approach at Platform Scale; [[aditya-gautam|Aditya Gautam]] (Day 2 — Session Day 1 · 12:05pm-12:25pm · Vision & OCR; official schedule)
- [[2026-06-29-varun-krovvidi-6-pillars-of-an-agentic-harness-that-fixes-production-incidents]] — 6 Pillars of an Agentic Harness That Fixes Production Incidents; [[varun-krovvidi|Varun Krovvidi]] (Day 2 — Session Day 1 · 2:50pm-3:10pm · Expo Stage 1 NE; official schedule)
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale]] — Sandboxes Aren't Optional: Runtime Isolation Patterns for Coding Agents at Scale; [[robert-brennan|Robert Brennan]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Sandbox & Platform Engineering; official schedule)
- [[2026-07-01-frank-coyle-anthropic-s-cca-exam-as-a-field-guide-for-agentic-engineering]] — Anthropic's CCA Exam as a Field-Guide for Agentic Engineering; [[frank-coyle|Frank Coyle]] (Day 4 — Session Day 3 · 11:10am-11:30am · Agentic Engineering; official schedule)
- [[2026-07-01-sheilah-kirui-seeing-the-plumbing-profiling-vllm-speculative-decoding-on-nvidia-blackwell]] — Seeing the Plumbing: Profiling vLLM Speculative Decoding on NVIDIA Blackwell; [[sheilah-kirui|Sheilah Kirui]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Expo Stage 2 NW; official schedule)
- [[2026-06-29-moritz-johner-we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night]] — We Gave an Agent Production Code Access and Then Tried to Sleep at Night; [[moritz-johner|Moritz Johner]] (Day 2 — Session Day 1 · 11:40am-12:00pm · Security; official schedule)
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]] — In Code They Act, In Proof We Trust; [[erik-meijer|Erik Meijer]] (Day 2 — Session Day 1 · 4:50pm-5:10pm · Harness Engineering; official schedule)

## Related People
- [[john-craft|John Craft]]
- [[laurie-voss|Laurie Voss]]
- [[jason-liu|Jason Liu]]
- [[swyx|swyx]]
- [[pamela-fox|Pamela Fox]]
- [[ahmad-osman|Ahmad Osman]]
- [[sandhya-subramani|Sandhya Subramani]]
- [[thor-schaeff|Thor 雷神 Schaeff]]
- [[charlie-guo|Charlie Guo]]
- [[dominik-kundel|Dominik Kundel]]
- [[frank-coyle|Frank Coyle]]
- [[kent-c-dodds|Kent C. Dodds]]
- [[vlad-luzin|Vlad Luzin]]
- [[peter-werry|Peter Werry]]
- [[liad-yosef|Liad Yosef]]
- [[idan-gazit|Idan Gazit]]
- [[christopher-manning|Christopher Manning]]
- [[keiji-kanazawa|Keiji Kanazawa]]
- [[brendan-rappazzo|Brendan Rappazzo]]
- [[philipp-schmid|Philipp Schmid]]
- [[kwindla-kramer|Kwindla Kramer]]
- [[arun-sekhar|Arun Sekhar]]
- [[fuad-ali|Fuad Ali]]
- [[zhengyao-jiang|Zhengyao Jiang]]

## Related Companies
- [[microsoft|Microsoft]]
- [[openai|OpenAI]]
- [[docker|Docker]]
- [[arize-ai|Arize AI]]
- [[google-deepmind|Google DeepMind]]
- [[anthropic|Anthropic]]
- [[amazon-web-services|Amazon Web Services]]
- [[together-ai|Together AI]]
- [[nvidia|NVIDIA]]
- [[google|Google]]
- [[weco-ai|Weco AI]]
- [[workos|WorkOS]]
- [[unblocked|Unblocked]]
- [[amazon-agi-lab|Amazon AGI Lab]]
- [[paypal|PayPal]]
- [[meta|Meta]]
- [[sonar|Sonar]]
- [[uber|Uber]]

## Transcript And Resource Support
### Transcript-backed resources
- [[youtube-jVjt-2g8NMY]] — A Genius With Amnesia - Victor Savkin, Nx
- [[youtube-3hXJI2q0Jz8]] — Recursive Coding Agents - Raymond Weitekamp, OpenProse
- [[youtube-zKk7sDMGDEQ]] — Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer
- [[youtube-EcqMYoIV57A]] — Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo
- [[youtube-aHhB3sjGjkI]] — Agents Building Agents - Alfonso Graziano, Nearform
- [[youtube-c-2eEv2ou7Y]] — Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic
- [[youtube-ij-AU9dpJjc]] — Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co
- [[youtube-Akm1sqvWG4A]] — Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy
- [[youtube-wcUJWP6WpGM]] — SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius
- [[youtube-u-rJwPPU3QA]] — How to talk to statues — Joe Reeve, ElevenLabs
- [[youtube-r305-aQTaU0]] — Text Diffusion — Brendan O’Donoghue, Google DeepMind
- [[youtube-whue9_YquGA]] — Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation
- [[youtube-IddXPepIAS4]] — Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS
- [[youtube-ObTPqBGsEbA]] — The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks
- [[youtube-T0HhO4YtTfE]] — AI System Design: From Idea to Production - Apoorva Joshi, MongoDB
- [[youtube-4sX_He5c4sI]] — WF2026: Autoresearch & Keynotes ft. Anthropic, Google DeepMind, Amazon AGI, Sonar, Arena, Recursive
- [[youtube-wFTVEDYVJT0]] — Building Agents with Amazon Nova Act and MCP - Du'An Lightfoot, Amazon (Full Workshop)
- [[youtube-bk0TmxoZlUY]] — Evals 101 — Doug Guthrie, Braintrust

### Quote signals
- “And then we have access to additional tools, memory, or we may need to talk to additional agents or LLMs like Amazon Nova ACT through something like MCP.” — [[youtube-wFTVEDYVJT0]]
- “When you're building agents, not just using them to write code, you start getting into architecting agentic systems.” — [[youtube-ZD9-4fW2HhM]]
- “So if you want to build this marketplace of app and have third-party UI rendered inside ChatGPT, why not use straight away source doc as the attribute for as the attribute for uh for injecting context into.” — [[youtube-c-2eEv2ou7Y]]
- “And finally, how do you optimize for cost, not just for accuracy, but also for cost, latency, and reliability before you ship and or as you find gaps in production.” — [[youtube-T0HhO4YtTfE]]
- “That context pointer literally just says if you need the template or if you need to update the context.md file, go to this file.” — [[youtube-UNzCG3lw6O0]]
- “We need to think about the branches in our skill moving material out behind context pointers.” — [[youtube-UNzCG3lw6O0]]
- “And this is this is pretty uh important because sometimes the problem is uh, uh so critical so we need to fix them as soon as possible and yeah, it works pretty well.” — [[youtube-kZsf_Sfm7RU]]
- “Model providers you will put evaluation benchmarks on three uh benchmark uh boards, but those are not really useful when you put them in your context, in your enterprise.” — [[youtube-ObTPqBGsEbA]]
