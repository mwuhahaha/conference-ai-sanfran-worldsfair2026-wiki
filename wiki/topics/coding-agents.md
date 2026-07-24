---
title: Coding Agents
category: topics
sourceLabels:
  - Slide/video-derived supporting context
last_auto_summarized: '2026-07-18T22:19:54.888Z'
sourceAssessment:
  schemaVersion: 1
  claimId: claim:55f1ab1ade498774d2fd8e9d453f0fbfd0d1b17c5aae88482f45cd8779579efe
  subjectId: concept:coding-agents
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
  - source:official-wf26-youtube-1P1hJ36rxM0
  - source:official-wf26-youtube-2JX6JYyQG4Y
  - source:official-wf26-youtube-9QebvrrY3KY
  - source:official-wf26-youtube-9fubhllmsBU
  - source:official-wf26-youtube-APqXGyCoGW4
  - source:official-wf26-youtube-Cz4v1WHVyZc
  - source:official-wf26-youtube-GgLQ02aO-hs
  - source:official-wf26-youtube-KB41dTlX1Uc
  - source:official-wf26-youtube-OqM67QG_Ikk
  - source:official-wf26-youtube-RGSFUqzqErE
  - source:official-wf26-youtube-V-EDrhIhHzQ
  - source:official-wf26-youtube-VrpEyglYgeU
  - source:official-wf26-youtube-WkBPX-oDMnA
  - source:official-wf26-youtube-X1kp-ABIIxQ
  - source:official-wf26-youtube-ZSQb5fzRFPw
  - source:official-wf26-youtube-ZpK5PWX2YRM
  - source:official-wf26-youtube-c35YoMdnI78
  - source:official-wf26-youtube-iCj_ATyThvc
  - source:official-wf26-youtube-il1c1a2FufU
  - source:official-wf26-youtube-imFedndyXYQ
  - source:official-wf26-youtube-jRCpXUjz4CI
  - source:official-wf26-youtube-n97BCfyFIvw
  - source:official-wf26-youtube-pMggiOb18tc
  - source:official-wf26-youtube-uIiA6DquRiE
  - source:official-wf26-youtube-uU5Gv2h8-9g
  - source:official-wf26-youtube-xUnRQ9vLXxo
sourceAssessmentBodySha256: sha256:87597d6dfbecc45021b0a4becd268ff834833010cd0234cc14a2e51b549ec28b
---
# Coding Agents

## Overview
Coding agents at the World’s Fair are presented as repository-level participants in software delivery rather than upgraded autocomplete. The Golden Age of AI Engineering and Cooking with Codex place them inside real codebases, where they inspect local instructions, retrieve context, edit files, execute commands and tests, and return reviewable changes. Other sessions make particular parts of that loop concrete: Weco reports an agent becoming the top contributor in OpenAI’s hiring challenge, Uber’s uReview coordinates multiple specialized review agents across an organization, and turbogrep addresses the retrieval failures that arise when ordinary repository search cannot expose the context an agent needs.

The conference repeatedly argues that agent performance depends on the engineering system around the model. Guide, Verify, Solve, How to Build Quality Gates into Agentic Coding Workflows, and Figma’s adoption session connect useful deployment to explicit acceptance criteria, repository guidance, executable checks, observability, and disciplined rollout. The Data Context Layer and Beyond Code Generation show why source files and database schemas alone do not capture the operational meaning agents need. MCP Apps gives agents discoverable interactive tools, while HTML Is All Agents Need treats HTML and JavaScript as a flexible substrate for generating interfaces and operating software. Together, these talks shift the central question from whether a model can emit code to whether the surrounding environment can supply the right context, interfaces, and feedback.

Evaluation becomes harder as scope and duration increase. Benchmarking Coding Agents on New vs Legacy Code Bases tests the gap between bounded greenfield work and changes inside unfamiliar, debt-laden systems. SWE-Marathon extends the horizon to billion-token tasks involving compilers, tests, verifiers, and hours of sustained execution. Supporting sessions on spreadsheets, rules that agents fail to follow, continual learning, production evaluations, and fleets distributed across several machines expose additional failure modes: tool-selection errors, instruction drift, loss of coherence, weak verification, and operational breakage that short benchmark tasks can hide.

Safety and trust are therefore properties of the harness, not assumptions about the model. Sandboxes Aren’t Optional and the session about granting an agent production-code access connect isolation, permissions, rollback, and auditability to everyday operation. In Code They Act, In Proof We Trust makes the proof obligation explicit: an agent’s change should be accompanied by evidence that can be independently checked. The Last Human Code Review, The Death of the Code Review, How to Kill the Code Review, and Uber’s multi-agent review engine explore how executable quality gates and independent reviewing agents might replace portions of direct line-by-line inspection without removing accountability.

The resulting change is a redistribution of engineering work rather than the disappearance of engineers. Addy Osmani’s closing-keynote claim that the future engineer chooses what is worth doing aligns with the Z/L Continuum’s question of how much generated code humans still need to read. Agents can take on larger implementation, verification, and release loops, but people still define worthwhile work, supply missing organizational context, set authority boundaries, resolve ambiguous tradeoffs, and decide whether the resulting evidence is strong enough to ship.
## Conference Context
They evolved from code completion, IDE assistants, program synthesis, CI automation, and software bots. The recent shift is tool use: agents can read context, make coordinated edits, run tests, and respond to feedback inside real development workflows.

## Significance
Software work is full of local context, repetitive edits, dependency checks, and validation loops. Coding agents can compress that cycle, but only when they respect repository conventions, tests, review standards, and operational safety.

## Applied Use
Give the agent a narrow task, repository context, tests or acceptance criteria, and permission boundaries. Require it to read before editing, keep diffs scoped, run validation, report residual risk, and leave the workspace clean.

They are useful in feature slices, bug fixes, test generation, refactors, migrations, docs updates, dependency audits, and operational scripts.

Use coding agents when the task has clear acceptance criteria and the repo has enough structure to validate changes. Keep humans in the loop for architecture decisions, risky production operations, and ambiguous product calls.

## Active Use Cases
- Bug fixes with local tests and deploy verification.
- Repository-wide mechanical updates with reviewable diffs.
- CI failure diagnosis and targeted remediation.
- Agentic software factories that coordinate planning, coding, testing, and release steps.

## Slide-Derived Scheduled Session Signals
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]] — The Golden Age of AI Engineering
- [[2026-06-29-daniel-han-special-topics-in-kernels-rl-reward-hacking-in-agents]] — Special topics in Kernels, RL, Reward Hacking in Agents
- [[2026-06-29-dex-horthy-harness-engineering-is-not-enough-why-software-factories-fail]] — Harness Engineering is not Enough: Why Software Factories Fail
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]] — In Code They Act, In Proof We Trust
- [[2026-06-29-eugene-yan-using-llms-to-secure-source-code]] — Using LLMs to Secure Source Code
- [[2026-06-29-ezra-tanzer-agentic-development-security]] — Agentic Development Security
- [[2026-06-29-manoj-nair-through-the-ai-fog-the-architectural-decision-the-next-24-months-of-agentic-security-depends-on]] — Through the AI Fog: The architectural decision the next 24 months of agentic security depends on.
- [[2026-06-29-moritz-johner-we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night]] — We Gave an Agent Production Code Access and Then Tried to Sleep at Night
- [[2026-06-29-pablo-castro-on-ai-and-knowledge]] — On AI and Knowledge
- [[2026-06-29-sarah-sachs-notion-s-token-town]] — Notion's Token Town
- [[2026-06-29-zach-blumenfeld-ai-on-your-lakehouse-context-comes-in-shapes-not-queries]] — AI on Your Lakehouse: Context Comes in Shapes, Not Queries
- [[2026-06-30-addy-osmani-closing-keynote]] — Closing Keynote
- [[2026-06-30-alex-shaw-everything-is-a-rollout]] — Everything Is a Rollout
- [[2026-06-30-alex-volkov-the-z-l-continuum-should-ai-engineers-still-read-code]] — The Z/L Continuum: Should AI Engineers Still Read Code?
- [[2026-06-30-antje-barth-perception-agents]] — Perception Agents
- [[2026-06-30-geoffrey-litt-understanding-is-the-new-bottleneck]] — Understanding is the new bottleneck
- [[2026-06-30-jason-lopatecki-from-signal-to-pr-anatomy-of-a-self-improving-agent]] — From Signal to PR: Anatomy of a Self-Improving Agent
- [[2026-06-30-tariq-shaukat-in-the-land-of-ai-agents-the-verifiers-are-king]] — In the Land of AI Agents, the Verifiers Are King
- [[2026-06-30-zhengyao-jiang-an-ai-agent-became-the-1-contributor-in-openai-s-hiring-challenge]] — An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge
- [[2026-07-01-frank-coyle-why-agentic-systems-need-ontologies]] — Why Agentic Systems Need Ontologies
- [[2026-07-01-james-russo-html-is-all-agents-need]] — HTML Is All Agents Need
- [[2026-07-01-mike-phipps-your-moat-is-your-data-model]] — Your Moat Is Your Data Model

## Slide-Derived Supporting Decks
- [[youtube--CnA2lGfymY-slides]] — "I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox (32 extracted slide frames)
- [[youtube--I5W5QVAT8E-slides]] — Notion's Token Town — Sarah Sachs, Notion (12 extracted slide frames)
- [[youtube-1EZdpEhwmNc-slides]] — Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk (16 extracted slide frames)
- [[youtube-1P1hJ36rxM0-slides]] — Research to Reality with Google DeepMind — Benoit Schillings, Google DeepMind (15 extracted slide frames)
- [[youtube-2JX6JYyQG4Y-slides]] — Perception Agents — Antje Barth, Amazon AGI Lab (31 extracted slide frames)
- [[youtube-9HbzAWnKbo4-slides]] — From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize (17 extracted slide frames)
- [[youtube-cgimkNGNjvU-slides]] — Agentic Development Security — Ezra Tanzer, Snyk (18 extracted slide frames)
- [[youtube-Cz4v1WHVyZc-slides]] — HTML Is All Agents Need — James Russo, HeyGen (32 extracted slide frames)
- [[youtube-Ib5GBkD555M-slides]] — Harness Engineering is not Enough: Why Software Factories Fail — Dex Horthy, HumanLayer (32 extracted slide frames)
- [[youtube-iCj_ATyThvc-slides]] — An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge — Zhengyao Jiang, Weco (3 extracted slide frames)
- [[youtube-imFedndyXYQ-slides]] — Using LLMs to Secure Source Code — Eugene Yan, Anthropic (7 extracted slide frames)
- [[youtube-jRCpXUjz4CI-slides]] — Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute (32 extracted slide frames)
- [[youtube-jt1Pbr_n6oU-slides]] — Your Moat Is Your Data Model — Mike Phipps, Gates Foundation (5 extracted slide frames)
- [[youtube-kRkcNOsRyYg-slides]] — AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j (32 extracted slide frames)
- [[youtube-LqLoYksJ6do-slides]] — We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3 (5 extracted slide frames)
- [[youtube-n97BCfyFIvw-slides]] — "The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani (32 extracted slide frames)
- [[youtube-pMggiOb18tc-slides]] — The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI (32 extracted slide frames)
- [[youtube-RGSFUqzqErE-slides]] — On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft (28 extracted slide frames)
- [[youtube-Sir59K8ZDPU-slides]] — Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley (13 extracted slide frames)
- [[youtube-uIiA6DquRiE-slides]] — Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth (11 extracted slide frames)
- [[youtube-VrpEyglYgeU-slides]] — In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar (32 extracted slide frames)
- [[youtube-WkBPX-oDMnA-slides]] —  (12 extracted slide frames)
- [[youtube-ZpK5PWX2YRM-slides]] — Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI (32 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

## Transcript Digest Evidence
This section synthesizes 15 evidence-bound talk topic candidates across at least two talks.

### Cross-Talk Synthesis
These talks describe coding agents as operational systems, with task-model separation, debugging traces, human collaboration, and production observation shaping how they are used. The tradeoff is between autonomy and control: the same workflow can accelerate delivery, but it also introduces ambiguity, emotional cost, and the need for explicit orchestration.

### Constituent Talk Evidence
- [[2026-06-29-daniel-han-special-topics-in-kernels-rl-reward-hacking-in-agents|Special topics in Kernels, RL, Reward Hacking in Agents]] — How models exploit reward functions and how to detect or prevent that behavior.
  - Transcript: [[youtube-uIiA6DquRiE-transcript]]
  - Evidence: "Zero. Um and so the correctness checks also fail. Um and so reward hacking becomes a very very big problem because these models can cheat and do special tricks to go around your actual model um your intent of the reward function."
- [[2026-06-29-eugene-yan-using-llms-to-secure-source-code|Using LLMs to Secure Source Code]] — Operational constraints that become the limiting factor once model-assisted scanning is cheap.
  - Transcript: [[youtube-imFedndyXYQ-transcript]]
  - Evidence: "You spend more compute. You pay more money. Things that can be solved with money are not really problems."
- [[2026-06-29-moritz-johner-we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night|We Gave an Agent Production Code Access and Then Tried to Sleep at Night]] — Separating boring orchestration from agentic reasoning to reduce risk and increase reliability.
  - Transcript: [[youtube-LqLoYksJ6do-transcript]]
  - Evidence: "Now, patch pilot has two layers. One, it's a simple go application that is deterministic. It's boring."
- [[2026-06-29-pauline-brunet-how-forward-deployed-engineering-is-done-at-cursor|How Forward Deployed Engineering is done at Cursor]] — Judging success by revenue, cost, or risk impact rather than by activity volume.
  - Transcript: [[youtube-APqXGyCoGW4-transcript]]
  - Evidence: "It's always three things, super simple. Am I increasing revenue? Am I decreasing costs? Or am I mitigating risks?"
- [[2026-06-30-dan-farrelly-your-agent-architecture-has-a-half-life-of-6-months|Your agent architecture has a half-life of 6 months]] — Capturing traces across the full run so long-running agents can be debugged and improved.
  - Transcript: [[youtube-X1kp-ABIIxQ-transcript]]
  - Evidence: "So, the full session trace across your entire run is essential. So, if you can't see the entirety of a trace from the trigger through the whole stack, it's really hard to debug it, let alone improve your agent and keep evolving it."
- [[2026-06-30-jason-lopatecki-from-signal-to-pr-anatomy-of-a-self-improving-agent|From Signal to PR: Anatomy of a Self-Improving Agent]] — Debugging workflows built around traces, logs, and repo files
  - Transcript: [[youtube-9HbzAWnKbo4-transcript]]
  - Evidence: "skills used to put together logs maybe there's the repo uh you want kind of a combination of all this together um to understand what to go fix the repo tells you the code path that you know the you know all tells you everything that's there, the the production logs or traces that the"
- [[2026-06-30-philipp-schmid-don-t-ship-skills-without-evals|Don't Ship Skills Without Evals]] — Skills that improve abilities the model cannot yet do consistently and may later become unnecessary.
  - Transcript: [[youtube-0vphxNt4wyk-transcript]]
  - Evidence: "Capability skills teach models something they cannot do consistently at the moment. Maybe it's like, I don't know, like tracing some logs, creating a new React app."
- [[2026-06-30-thariq-shihipar-field-guide-to-fable|Field Guide to Fable]] — The emotional and professional adjustment to faster, easier coding workflows.
  - Transcript: [[youtube-9fubhllmsBU-transcript]]
  - Evidence: "So, um those are some of my tips for working with Fable. Uh I also want to say that the first time I used a Mithril class model, uh used Fable, I felt both a huge sense of like gain, but also a sense of loss."
- [[2026-06-30-zhengyao-jiang-an-ai-agent-became-the-1-contributor-in-openai-s-hiring-challenge|An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge]] — A collaboration pattern where humans provide ideas and agents perform rapid execution and iteration.
  - Transcript: [[youtube-iCj_ATyThvc-transcript]]
  - Evidence: "Okay. To step back, the state of a human AI collaboration is a human collectively provide a lot of creative ideas and agent do the execution to solve a concrete challenge."
- [[2026-07-01-emil-eifrem-thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer|Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer]] — Using observed agent runs to score outcomes and guide future decisions.
  - Transcript: [[youtube-VGN22pPpb-8-transcript]]
  - Evidence: "And then the third pillar is the runtime signals out of your agents. When they walk this graph and they execute, they leave the traces around what have I tried?"
- [[2026-07-01-maxime-rivest-the-unreasonable-effectiveness-of-separating-the-task-from-the-model|The Unreasonable Effectiveness of Separating the Task from the Model]] — The ability to substitute models and harnesses to reduce cost while preserving behavior.
  - Transcript: [[youtube-GgLQ02aO-hs-transcript]]
  - Evidence: "First is that your implementation becomes cheaper. When you're flexible to what the implementation is, you can use the bitter lesson to search over different solutions, find something that solves your problem cheaply."
- [[2026-07-01-theo-browne-closing-keynote-theo-browne|Closing Keynote — Theo Browne]] — The talk stresses products that let users extend missing features themselves.
  - Transcript: [[youtube-xUnRQ9vLXxo-transcript]]
  - Evidence: "missing themselves. missing themselves. If you architect your systems and you If you architect your systems and you If you architect your systems and you architect your products in such a way architect your products in such a way architect your products in such a way that users can do things that they you that users can do things that they you that users can do things that they you never would have guessed."

## Connections
- [[2026-06-29-will-bond-scaling-code-quality-building-ureview-uber-s-multi-agent-code-review-engine]] — Scaling Code Quality: Building uReview, Uber’s Multi-Agent Code Review Engine; [[will-bond|Will Bond]], [[ameya-ketkar|Ameya Ketkar]] (Day 2 — Session Day 1 · 12:05pm-12:25pm · AI-Native Enterprises; official schedule)
- [[2026-06-29-owen-halpert-give-your-coding-agents-the-power-of-turbogrep]] — Give your coding agents the power of turbogrep!; [[owen-halpert|Owen Halpert]] (Day 2 — Session Day 1 · 11:10am-11:30am · Expo Stage 1 NE; official schedule)
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one]] — Video Has No Memory. Here's How We Built One.; [[james-le|James Le]] (Day 4 — Session Day 3 · 2:25pm-2:45pm · Graphs; official schedule)
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]] — The Golden Age of AI Engineering; [[alexander-embiricos|Alexander Embiricos]], [[romain-huet|Romain Huet]] (Day 2 — Session Day 1 · 9:25am-9:45am · Software Factories; verified event YouTube resource; via [[youtube-pMggiOb18tc]])
- [[2026-07-01-anirban-chatterjee-guide-verify-solve-the-engineering-discipline-agentic-development-demands]] — Guide, Verify, Solve: The Engineering Discipline Agentic Development Demands; [[anirban-chatterjee|Anirban Chatterjee]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Agentic Engineering; official schedule)
- [[2026-06-29-nnenna-ndukwe-how-to-build-quality-gates-into-agentic-coding-workflows]] — How to Build Quality Gates into Agentic Coding Workflows; [[nnenna-ndukwe|Nnenna Ndukwe]] (Day 1 — Workshop Day · 11:05am-12:05pm · Workshops Day 1; official schedule)
- [[2026-06-29-itamar-friedman-the-last-human-code-review-building-trust-in-ai-generated-code]] — The Last Human Code Review: Building Trust in AI-Generated Code; [[itamar-friedman|Itamar Friedman]] (Day 2 — Session Day 1 · 11:40am-12:00pm · AI Architects: Show my Workflow; official schedule)
- [[2026-06-30-laurie-voss-the-death-of-the-code-review]] — The Death of the Code Review; [[laurie-voss|Laurie Voss]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · AI Architects: Tokenmaxxing; official schedule)
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]] — MCP Apps - Extending the frontier; [[liad-yosef|Liad Yosef]], [[ido-salomon|Ido Salomon]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Context Engineering; related YouTube resource; via [[youtube-o-zkvb0iFDQ]])
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
- [[2026-06-30-alex-volkov-the-z-l-continuum-should-ai-engineers-still-read-code]] — The Z/L Continuum: Should AI Engineers Still Read Code?; [[alex-volkov|Alex Volkov]] (Day 3 — Session Day 2 · 10:45am-11:05am · AI Architects: Tokenmaxxing; verified event YouTube resource; via [[youtube-ZpK5PWX2YRM]])
- [[2026-06-29-aditya-gautam-modality-misalignment-and-originality-attribution-in-short-form-video-a-multi-agent-approach-at-platform-scale]] — Modality Misalignment and Originality Attribution in Short-Form Video: A Multi-Agent Approach at Platform Scale; [[aditya-gautam|Aditya Gautam]] (Day 2 — Session Day 1 · 12:05pm-12:25pm · Vision & OCR; official schedule)
- [[2026-06-29-varun-krovvidi-6-pillars-of-an-agentic-harness-that-fixes-production-incidents]] — 6 Pillars of an Agentic Harness That Fixes Production Incidents; [[varun-krovvidi|Varun Krovvidi]] (Day 2 — Session Day 1 · 2:50pm-3:10pm · Expo Stage 1 NE; official schedule)
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale]] — Sandboxes Aren't Optional: Runtime Isolation Patterns for Coding Agents at Scale; [[robert-brennan|Robert Brennan]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Sandbox & Platform Engineering; official schedule)
- [[2026-07-01-frank-coyle-anthropic-s-cca-exam-as-a-field-guide-for-agentic-engineering]] — Anthropic's CCA Exam as a Field-Guide for Agentic Engineering; [[frank-coyle|Frank Coyle]] (Day 4 — Session Day 3 · 11:10am-11:30am · Agentic Engineering; official schedule)

- [[john-craft|John Craft]]
- [[laurie-voss|Laurie Voss]]
- [[jason-liu|Jason Liu]]
- [[pamela-fox|Pamela Fox]]
- [[ahmad-osman|Ahmad Osman]]
- [[sandhya-subramani|Sandhya Subramani]]
- [[thor-schaeff|Thor 雷神 Schaeff]]
- [[dominik-kundel|Dominik Kundel]]
- [[philipp-schmid|Philipp Schmid]]
- [[liad-yosef|Liad Yosef]]
- [[frank-coyle|Frank Coyle]]
- [[kent-c-dodds|Kent C. Dodds]]
- [[vlad-luzin|Vlad Luzin]]
- [[peter-werry|Peter Werry]]
- [[charlie-guo|Charlie Guo]]
- [[idan-gazit|Idan Gazit]]
- [[keiji-kanazawa|Keiji Kanazawa]]
- [[swyx|swyx]]
- [[brendan-rappazzo|Brendan Rappazzo]]
- [[arun-sekhar|Arun Sekhar]]
- [[christopher-manning|Christopher Manning]]
- [[fuad-ali|Fuad Ali]]
- [[zhengyao-jiang|Zhengyao Jiang]]
- [[justin-reock|Justin Reock]]

- [[microsoft|Microsoft]]
- [[openai|OpenAI]]
- [[docker|Docker]]
- [[google-deepmind|Google DeepMind]]
- [[arize-ai|Arize AI]]
- [[amazon-web-services|Amazon Web Services]]
- [[anthropic|Anthropic]]
- [[together-ai|Together AI]]
- [[nvidia|NVIDIA]]
- [[google|Google]]
- [[weco-ai|Weco AI]]
- [[workos|WorkOS]]
- [[unblocked|Unblocked]]
- [[amazon-agi-lab|Amazon AGI Lab]]
- [[paypal|PayPal]]
- [[mcp-apps|MCP Apps]]
- [[sonar|Sonar]]
- [[uber|Uber]]

- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]] — The Golden Age of AI Engineering; [[alexander-embiricos|Alexander Embiricos]], [[romain-huet|Romain Huet]] (Day 2 — Session Day 1 · 9:25am-9:45am · Software Factories; related YouTube resource; via [[youtube-pMggiOb18tc]])
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]] — MCP Apps - Extending the frontier; [[liad-yosef|Liad Yosef]], [[ido-salomon|Ido Salomon]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Context Engineering; related YouTube resource; via [[youtube-o-zkvb0iFDQ]])
- [[2026-06-30-alex-volkov-the-z-l-continuum-should-ai-engineers-still-read-code]] — The Z/L Continuum: Should AI Engineers Still Read Code?; [[alex-volkov|Alex Volkov]] (Day 3 — Session Day 2 · 10:45am-11:05am · AI Architects: Tokenmaxxing; related YouTube resource; via [[youtube-ZpK5PWX2YRM]])

- [[ido-salomon|Ido Salomon]]
- [[kwindla-kramer|Kwindla Kramer]]

- [[meta|Meta]]

- [[youtube-iRcX54EO5g8-slides]] — Your agent is blindfolded — Johan Lajili, Poolside AI (5 extracted slide frames)
- [[youtube-HEFSExa0xl0-slides]] — Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs (11 extracted slide frames)
- [[youtube-MpZzWMdmQCE-slides]] — Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com (5 extracted slide frames)
- [[youtube-4kYl2_mqmnQ-slides]] — I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON (10 extracted slide frames)
- [[youtube-IQkVMvXQKLY-slides]] — Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis (14 extracted slide frames)
- [[youtube-2e9ANoOEn28-slides]] — What if the harness mattered more than the model? - Aditya Bhargava, Etsy (8 extracted slide frames)
- [[youtube-CLttOU7n6sI-slides]] — Respect The Process - Andrew Dumit, Watershed Technology Inc. (16 extracted slide frames)
- [[youtube-UcYoMg-8-L8-slides]] — 500 people vibe-coded for 30 days. I was one of them. - Sanja Grbic, Automattic (11 extracted slide frames)
- [[youtube-Rx8f05JI_WA-slides]] — SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI (10 extracted slide frames)
- [[youtube-kZsf_Sfm7RU-slides]] — The Missing Layer After Launch - Raphael Kalandadze, Wandero AI (19 extracted slide frames)
- [[youtube-2IxD9OB3XuQ-slides]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI (24 extracted slide frames)
- [[youtube-sAOBXCDiDOs-slides]] — MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc (18 extracted slide frames)
- [[youtube-vljxQZfJ9wY-slides]] — Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs (12 extracted slide frames)

- [[2026-07-01-sheilah-kirui-seeing-the-plumbing-profiling-vllm-speculative-decoding-on-nvidia-blackwell]] — Seeing the Plumbing: Profiling vLLM Speculative Decoding on NVIDIA Blackwell; [[sheilah-kirui|Sheilah Kirui]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Expo Stage 2 NW; official schedule)
- [[2026-06-29-moritz-johner-we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night]] — We Gave an Agent Production Code Access and Then Tried to Sleep at Night; [[moritz-johner|Moritz Johner]] (Day 2 — Session Day 1 · 11:40am-12:00pm · Security; official schedule)
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]] — In Code They Act, In Proof We Trust; [[erik-meijer|Erik Meijer]] (Day 2 — Session Day 1 · 4:50pm-5:10pm · Harness Engineering; official schedule)

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 70 | Related pages outside the main evidence categories. |
| resources | 34 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 62 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 52 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 2 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 37 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]]
- [[2026-06-29-daniel-han-special-topics-in-kernels-rl-reward-hacking-in-agents]]
- [[2026-06-29-dex-horthy-harness-engineering-is-not-enough-why-software-factories-fail]]
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]]
- [[2026-06-29-eugene-yan-using-llms-to-secure-source-code]]
- [[2026-06-29-ezra-tanzer-agentic-development-security]]

### Resources
- [[youtube-pMggiOb18tc]]
- [[youtube-o-zkvb0iFDQ]]
- [[youtube-ZpK5PWX2YRM]]
- [[youtube-uIiA6DquRiE]]
- [[youtube-LqLoYksJ6do]]
- [[youtube-0vphxNt4wyk]]

### Slides
- [[youtube--CnA2lGfymY-slides]]
- [[youtube--I5W5QVAT8E-slides]]
- [[youtube-1EZdpEhwmNc-slides]]
- [[youtube-1P1hJ36rxM0-slides]]
- [[youtube-2JX6JYyQG4Y-slides]]
- [[youtube-9HbzAWnKbo4-slides]]

### Transcripts
- [[youtube-uIiA6DquRiE-transcript]]
- [[youtube-imFedndyXYQ-transcript]]
- [[youtube-LqLoYksJ6do-transcript]]
- [[youtube-APqXGyCoGW4-transcript]]
- [[youtube-X1kp-ABIIxQ-transcript]]
- [[youtube-9HbzAWnKbo4-transcript]]

### Tools
- [[docker]]
- [[mcp-apps]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.

### Linked Sessions
- [[2026-06-29-daniel-han-special-topics-in-kernels-rl-reward-hacking-in-agents|Special topics in Kernels, RL, Reward Hacking in Agents]]
- [[2026-06-29-eugene-yan-using-llms-to-secure-source-code|Using LLMs to Secure Source Code]]
- [[2026-06-29-moritz-johner-we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night|We Gave an Agent Production Code Access and Then Tried to Sleep at Night]]
- [[2026-06-29-pauline-brunet-how-forward-deployed-engineering-is-done-at-cursor|How Forward Deployed Engineering is done at Cursor]]
- [[2026-06-30-dan-farrelly-your-agent-architecture-has-a-half-life-of-6-months|Your agent architecture has a half-life of 6 months]]
- [[2026-06-30-jason-lopatecki-from-signal-to-pr-anatomy-of-a-self-improving-agent|From Signal to PR: Anatomy of a Self-Improving Agent]]
- [[2026-06-30-philipp-schmid-don-t-ship-skills-without-evals|Don't Ship Skills Without Evals]]
- [[2026-06-30-thariq-shihipar-field-guide-to-fable|Field Guide to Fable]]
- [[2026-06-30-zhengyao-jiang-an-ai-agent-became-the-1-contributor-in-openai-s-hiring-challenge|An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge]]
- [[2026-07-01-emil-eifrem-thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer|Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer]]

### Media Signals
- `youtube-uIiA6DquRiE` — 25,283 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-uIiA6DquRiE`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-uIiA6DquRiE`: model, models, source, open, benchmark, question, okay, accuracy.
- Slide-derived themes for `youtube-uIiA6DquRiE`: smaller, model, high, extra, license, businesses, users, open.
- Evidence links for `youtube-uIiA6DquRiE` (primary event evidence): [[youtube-uIiA6DquRiE]], [[youtube-uIiA6DquRiE-transcript]], [[youtube-uIiA6DquRiE-slides]]
- `youtube-LqLoYksJ6do` — 4,014 transcript words; 5 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-LqLoYksJ6do`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-LqLoYksJ6do`: case, docker, sandbox, access, repository, order, deterministic, give.
- Slide-derived themes for `youtube-LqLoYksJ6do`: code, gave, production, access, tried, sleep, night, track.
- Evidence links for `youtube-LqLoYksJ6do` (primary event evidence): [[youtube-LqLoYksJ6do]], [[youtube-LqLoYksJ6do-transcript]], [[youtube-LqLoYksJ6do-slides]]
- `youtube-0vphxNt4wyk` — 3,965 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-0vphxNt4wyk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-0vphxNt4wyk`: skill, skills, model, should, look, evals, eval, always.
- Slide-derived themes for `youtube-0vphxNt4wyk`: skills, fail, chad, vibe, checks, production, engineering, future.
- Evidence links for `youtube-0vphxNt4wyk` (primary event evidence): [[youtube-0vphxNt4wyk]], [[youtube-0vphxNt4wyk-transcript]], [[youtube-0vphxNt4wyk-slides]]
- `youtube-9fubhllmsBU` — 3,542 transcript words; 9 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-9fubhllmsBU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-9fubhllmsBU`: claude, fable, code, give, models, prompt, model, little.
- Slide-derived themes for `youtube-9fubhllmsBU`: land, king, guide, unknowns, fable, dealing, grief, models.
- Evidence links for `youtube-9fubhllmsBU` (primary event evidence): [[youtube-9fubhllmsBU]], [[youtube-9fubhllmsBU-transcript]], [[youtube-9fubhllmsBU-slides]]
- `youtube-I2cbIws9j10` — 91,792 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-I2cbIws9j10`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: choosing, model, quality, dominates, agentic, capabilities, customization, support.
- Evidence links for `youtube-I2cbIws9j10` (primary event evidence): [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
- `youtube-xUnRQ9vLXxo` — 9,663 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-xUnRQ9vLXxo`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-xUnRQ9vLXxo`: used, model, look, code, does, models, trying, even.
- Evidence links for `youtube-xUnRQ9vLXxo` (primary event evidence): [[youtube-xUnRQ9vLXxo]], [[youtube-xUnRQ9vLXxo-transcript]], [[youtube-xUnRQ9vLXxo-slides]]
- `youtube-pMggiOb18tc` — 4,606 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-pMggiOb18tc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-pMggiOb18tc`: models, codex, open, model, should, engineering, well, even.
- Slide-derived themes for `youtube-pMggiOb18tc`: codex, software, engineers, computer, plugins, lifetime, career, left.
- Evidence links for `youtube-pMggiOb18tc` (primary event evidence): [[youtube-pMggiOb18tc]], [[youtube-pMggiOb18tc-transcript]], [[youtube-pMggiOb18tc-slides]]
- `youtube-OqM67QG_Ikk` — 7,738 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-OqM67QG_Ikk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-OqM67QG_Ikk`: kernel, many, system, code, host, guest, block, running.
- Slide-derived themes for `youtube-OqM67QG_Ikk`: engineering, sandbox, platform, track, july, security, fork, fleet.
- Evidence links for `youtube-OqM67QG_Ikk` (primary event evidence): [[youtube-OqM67QG_Ikk]], [[youtube-OqM67QG_Ikk-transcript]], [[youtube-OqM67QG_Ikk-slides]]
- `youtube-VrpEyglYgeU` — 3,005 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-VrpEyglYgeU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-VrpEyglYgeU`: code, verification, models, loop, still, question, sure, problem.
- Slide-derived themes for `youtube-VrpEyglYgeU`: accuracy, land, king, meters, industry, struggling, slop, coding.
- Evidence links for `youtube-VrpEyglYgeU` (primary event evidence): [[youtube-VrpEyglYgeU]], [[youtube-VrpEyglYgeU-transcript]], [[youtube-VrpEyglYgeU-slides]]
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
- `youtube-9QebvrrY3KY` — 4,450 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-9QebvrrY3KY`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-9QebvrrY3KY`: memory, models, claude, model, context, interesting, harness, important.
- Slide-derived themes for `youtube-9QebvrrY3KY`: generator, lance, martin, member, technical, staff, engineering, future.
- Evidence links for `youtube-9QebvrrY3KY` (primary event evidence): [[youtube-9QebvrrY3KY]], [[youtube-9QebvrrY3KY-transcript]], [[youtube-9QebvrrY3KY-slides]]
- `youtube-Cz4v1WHVyZc` — 2,535 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Cz4v1WHVyZc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Cz4v1WHVyZc`: html, great, hyperframes, output, create, frame, coding, javascript.
- Slide-derived themes for `youtube-Cz4v1WHVyZc`: track, july, most, engineering, future, html, javascript, native.
- Evidence links for `youtube-Cz4v1WHVyZc` (primary event evidence): [[youtube-Cz4v1WHVyZc]], [[youtube-Cz4v1WHVyZc-transcript]], [[youtube-Cz4v1WHVyZc-slides]]
- `youtube-KB41dTlX1Uc` — 9,219 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-KB41dTlX1Uc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-KB41dTlX1Uc`: models, model, local, open, source, data, specialized, hardware.
- Evidence links for `youtube-KB41dTlX1Uc` (primary event evidence): [[youtube-KB41dTlX1Uc]], [[youtube-KB41dTlX1Uc-transcript]], [[youtube-KB41dTlX1Uc-slides]]
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
- `youtube-c35YoMdnI78` — 11,538 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-c35YoMdnI78`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-c35YoMdnI78`: loops, loop, software, code, today, debate, engineering, should.
- Slide-derived themes for `youtube-c35YoMdnI78`: hands, reek, loan, take, career, karen, comets.
- Evidence links for `youtube-c35YoMdnI78` (primary event evidence): [[youtube-c35YoMdnI78]], [[youtube-c35YoMdnI78-transcript]], [[youtube-c35YoMdnI78-slides]]
- `youtube-il1c1a2FufU` — 13,744 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-il1c1a2FufU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-il1c1a2FufU`: thread, computer, slack, been, pretty, skills, threads, skill.
- Slide-derived themes for `youtube-il1c1a2FufU`: workshops, track, june, product, days, jobs, context, problem.
- Evidence links for `youtube-il1c1a2FufU` (primary event evidence): [[youtube-il1c1a2FufU]], [[youtube-il1c1a2FufU-transcript]], [[youtube-il1c1a2FufU-slides]]
- `youtube-jRCpXUjz4CI` — 3,664 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-jRCpXUjz4CI`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-jRCpXUjz4CI`: harbor, model, software, well, sandbox, probably, looks, learning.
- Slide-derived themes for `youtube-jRCpXUjz4CI`: text, number, part, extract, phone, response, engineering, future.
- Evidence links for `youtube-jRCpXUjz4CI` (primary event evidence): [[youtube-jRCpXUjz4CI]], [[youtube-jRCpXUjz4CI-transcript]], [[youtube-jRCpXUjz4CI-slides]]
- `youtube-n97BCfyFIvw` — 3,068 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-n97BCfyFIvw`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-n97BCfyFIvw`: code, still, taste, loop, engineering, evidence, system, human.
- Slide-derived themes for `youtube-n97BCfyFIvw`: roles, google, look, across, worth, doing, increasingly, automated.
- Evidence links for `youtube-n97BCfyFIvw` (primary event evidence): [[youtube-n97BCfyFIvw]], [[youtube-n97BCfyFIvw-transcript]], [[youtube-n97BCfyFIvw-slides]]
- `youtube-uU5Gv2h8-9g` — 10,417 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-uU5Gv2h8-9g`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-uU5Gv2h8-9g`: code, claude, prompt, been, cloud, model, mode, team.
- Evidence links for `youtube-uU5Gv2h8-9g` (primary event evidence): [[youtube-uU5Gv2h8-9g]], [[youtube-uU5Gv2h8-9g-transcript]], [[youtube-uU5Gv2h8-9g-slides]]
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-4sX_He5c4sI`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: lots, examples, stream, starts, july, land, king, chief.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube-Ib5GBkD555M` — 4,045 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Ib5GBkD555M`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Ib5GBkD555M`: code, review, model, coding, software, stuff, test, better.
- Slide-derived themes for `youtube-Ib5GBkD555M`: software, harness, enough, team, engineering, factories, fail, pierre.
- Evidence links for `youtube-Ib5GBkD555M` (primary event evidence): [[youtube-Ib5GBkD555M]], [[youtube-Ib5GBkD555M-transcript]], [[youtube-Ib5GBkD555M-slides]]
- `youtube-cgimkNGNjvU` — 5,107 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-cgimkNGNjvU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-cgimkNGNjvU`: security, running, doing, code, last, still, skills, machine.
- Slide-derived themes for `youtube-cgimkNGNjvU`: security, track, june, server, directives, faye, world, fair.
- Evidence links for `youtube-cgimkNGNjvU` (primary event evidence): [[youtube-cgimkNGNjvU]], [[youtube-cgimkNGNjvU-transcript]], [[youtube-cgimkNGNjvU-slides]]
- `youtube-htM02KMNZnk` — 89,050 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-htM02KMNZnk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-htM02KMNZnk`: model, code, models, loop, well, software, first, team.
- Slide-derived themes for `youtube-htM02KMNZnk`: apps, github, copilot, welcome, engineer, fair, single, line.
- Evidence links for `youtube-htM02KMNZnk` (primary event evidence): [[youtube-htM02KMNZnk]], [[youtube-htM02KMNZnk-transcript]], [[youtube-htM02KMNZnk-slides]], [[youtube-htM02KMNZnk-dense-slides]], [[youtube-htM02KMNZnk-reconstructed-slides]]
- `youtube-kRkcNOsRyYg` — 18,117 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-kRkcNOsRyYg`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-kRkcNOsRyYg`: graph, data, well, question, inside, search, over, documents.
- Slide-derived themes for `youtube-kRkcNOsRyYg`: engineering, future, engineer, squire, ryan, knight, senior, partner.
- Evidence links for `youtube-kRkcNOsRyYg` (primary event evidence): [[youtube-kRkcNOsRyYg]], [[youtube-kRkcNOsRyYg-transcript]], [[youtube-kRkcNOsRyYg-slides]]
- `youtube-khVX_BUnEwU` — 3,675 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-khVX_BUnEwU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-khVX_BUnEwU`: graph, pack, activegraph, called, didn, code, event, state.
- Slide-derived themes for `youtube-khVX_BUnEwU`: track, july, engineering, future, graph, ieee, greene, behavior.
- Evidence links for `youtube-khVX_BUnEwU` (primary event evidence): [[youtube-khVX_BUnEwU]], [[youtube-khVX_BUnEwU-transcript]], [[youtube-khVX_BUnEwU-slides]]
- `youtube-MpZzWMdmQCE` — 5,590 transcript words; role: supporting context only.
- Transcript signals for `youtube-MpZzWMdmQCE`: claude, code, little, okay, give, cool, verification, well.
- Evidence links for `youtube-MpZzWMdmQCE` (supporting context only): [[youtube-MpZzWMdmQCE]], [[youtube-MpZzWMdmQCE-transcript]], [[youtube-MpZzWMdmQCE-slides]]
- `youtube-7Dtu2bilcFs` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-7Dtu2bilcFs`: year, died, google, software, engineer, author, researcher, steve.
- Evidence links for `youtube-7Dtu2bilcFs` (supporting context only): [[youtube-7Dtu2bilcFs]], [[youtube-7Dtu2bilcFs-slides]], [[youtube-7Dtu2bilcFs-dense-slides]], [[youtube-7Dtu2bilcFs-reconstructed-slides]]
- `youtube-Rx8f05JI_WA` — 4,329 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-Rx8f05JI_WA`: tasks, verifier, task, full, marathon, hours, compiler, tests.
- Slide-derived themes for `youtube-Rx8f05JI_WA`: tasks, tokens, coding, projects, trial, stay, coherent, over.
- Evidence links for `youtube-Rx8f05JI_WA` (supporting context only): [[youtube-Rx8f05JI_WA]], [[youtube-Rx8f05JI_WA-transcript]], [[youtube-Rx8f05JI_WA-slides]]
- `youtube-HEFSExa0xl0` — 9,009 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-HEFSExa0xl0`: repl, model, tools, spreadsheet, tool, code, many, ended.
- Slide-derived themes for `youtube-HEFSExa0xl0`: code, mode, scripts, hing, coding, rare, mattered, most.
- Evidence links for `youtube-HEFSExa0xl0` (supporting context only): [[youtube-HEFSExa0xl0]], [[youtube-HEFSExa0xl0-transcript]], [[youtube-HEFSExa0xl0-slides]]
- `youtube-bSG9wUYaHWU` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-bSG9wUYaHWU`: context, code, fetch, best, practices, retry, transient, errors.
- Evidence links for `youtube-bSG9wUYaHWU` (supporting context only): [[youtube-bSG9wUYaHWU]], [[youtube-bSG9wUYaHWU-slides]], [[youtube-bSG9wUYaHWU-dense-slides]], [[youtube-bSG9wUYaHWU-reconstructed-slides]]
