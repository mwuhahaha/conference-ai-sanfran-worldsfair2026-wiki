---
title: Autoresearch
category: topics
sourceLabels:
  - Official schedule
  - Public YouTube livestream transcript
  - Local slide OCR
last_auto_summarized: '2026-07-18T14:18:53.314Z'
sourceAssessment:
  schemaVersion: 1
  claimId: claim:7b93b18ab67ed48d64bc9e190c404a2919536098d6fe6fd2c60f3b2b8e9791df
  subjectId: concept:autoresearch
  domain: topics page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-20T01:11:38.017560Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-official-sessions
  - source:official-wf26-youtube-WkBPX-oDMnA
  - source:official-wf26-youtube-q4Tr-DknG2M
sourceAssessmentBodySha256: sha256:5da72661ea5f2813c32ffe0c51fbbe9c7752a270137d7b6bcc47c9ed6b3bb27a
---
# Autoresearch

## Overview
AutoResearch at WF2026 is framed as a closed-loop engineering discipline rather than a one-shot research assistant: keep an objective stable, gather evidence, propose a bounded change, execute a test, compare the result with a baseline, and decide what survives into the next iteration. The program grounds that loop in specific systems. Weco AI CEO Zhengyao Jiang, MTS Dixing Xu, founding engineer Dhruv Srikanth, and Vayum Arora connect automated hill climbing, self-improving agents, and recursive improvement to the Parameter Golf workshop. Elastic VP of AI Han Xiao focuses on test-time compute around frozen embedding models; Morph founder Tejas Bhakta brings the loop to generated kernels and specialized code inference; and Tim Sweeney’s Closing the Loop session names the autonomous research-agent cycle directly. Roland Gavrilescu and Julian Bright extend the discussion from controlled experiments to infrastructure for self-improving systems operating in the wild.

The connected sessions make clear that the object being optimized is often larger than a model response. Lakshya Agrawal separates context, the agent harness, and model weights into distinct reflective-optimization surfaces. Sakana.ai researcher Stefania Druga’s memory-harness session addresses the durable state required by long-running research agents, while Zubin Aysola’s ARIA session makes the recursive construction problem explicit by describing autoresearch used to build an autoresearch system. Erina Karati and Arunachalam Manikandan place research iteration inside a multi-agent AI Village, and Morgan Stanley scientist Brendan Rappazzo’s ALPHALAB session applies frontier models across multiple optimization domains. The adjacent hill-climbing-skills workshop and Lee Robinson’s Recursive Model Improvement recording sharpen the shared governance question: which component may change, which evaluation controls acceptance, and which failures must remain visible to the next attempt.

The Autoresearch track also presents a progression from research direction to operational practice. Richard Socher’s First Steps Toward Automated AI Research establishes the emerging capability; Google DeepMind VP Benoit Schillings links research to deployment reality; and Prime Intellect research engineer Elie Bakouch situates auto research alongside open pre-training work. The surrounding program exposes the dependencies that determine whether these loops are useful: perception agents for observations, memory systems for continuity, evaluations for selection, inference engineering for controlled execution, and human judgment for recognizing benchmark gaming or persuasive but unsupported results. Sessions on speech research, synthetic personas, robotics, and understanding as a bottleneck show how the same loop encounters different evidence, action, and measurement constraints outside code generation.

For this wiki, autoresearch therefore denotes an inspectable chain from question to source, hypothesis, intervention, measurement, and next decision—not merely an agent that produces polished prose. The official Autoresearch and Keynotes livestream and transcript are primary event evidence for recording- or speaker-attributed interpretation. Schedule pages establish titles, speakers, times, affiliations, and track framing; extracted, dense, and reconstructed slide pages form a separate OCR-derived layer whose text can be incomplete or noisy. Preserving those distinctions makes it possible to compare retrieval search, kernel benchmarking, Parameter Golf, memory harnesses, reflective optimization, and multi-agent research without turning schedule language or machine-read slide fragments into verified technical claims.

## Conference Context
AutoResearch grows out of literature search, systematic review, research assistants, web search, RAG, benchmarking, and scientific-discovery tooling, but adds an action-and-measurement loop. Instead of stopping after retrieval and synthesis, the system can select the next query, preserve experimental state, modify a candidate artifact, execute a test, score the outcome, and revise its policy. At WF2026, those artifacts range from embedding-model retrieval strategies and generated kernels to prompts, context, agent skills, harnesses, model weights, and multi-agent research plans.

The connected program traces a progression from capability to infrastructure and then to bounded applications. Socher’s First Steps session and Schillings’s Research to Reality keynote establish the research direction; Sweeney, Agrawal, Druga, and the Introspection team focus on feedback, memory, reflective optimization, and operation over time; and the Parameter Golf, dense-retrieval, kernel, ARIA, AI Village, and ALPHALAB sessions apply those mechanisms to measurable domains. Neighboring sessions on agent evaluations, recursive model improvement, synthetic personas, robotics, speech research, and perception expose the interfaces autoresearch depends on: reliable observations, durable state, controllable actions, and metrics that distinguish genuine progress from a persuasive-looking result.

The conference context also shows that autoresearch is not one fixed architecture. A retrieval loop may spend additional test-time compute without changing the embedding model; a kernel loop may generate code and benchmark latency or correctness; a Parameter Golf loop may hill-climb against a compact score; and a multi-agent system may divide investigation across competing hypotheses or optimization domains. What unifies them is not the model vendor or domain, but the presence of a bounded objective, an observable intervention, a comparison against prior state, and a recorded decision about what happens next.

## Significance
AutoResearch shifts the bottleneck from generating plausible ideas to governing repeated research decisions. A useful system must determine which evidence to seek, which variable to change, which metric represents progress, what state must survive between trials, and when an apparent gain is reproducible. WF2026 makes those decisions visible across documents and embeddings, generated code and kernels, context and harnesses, model weights, multi-agent coordination, and production research infrastructure. This breadth matters because it turns autoresearch from a single-agent demo pattern into a general systems problem spanning retrieval, experimentation, evaluation, memory, and operations.

The same breadth creates concrete failure modes. A retrieval agent can optimize a benchmark that does not reflect user relevance; a kernel researcher can accept a speedup that breaks correctness; a long-running agent can lose the failed trials needed to explain why a path was abandoned; and a multi-agent investigation can amplify the same unsupported assumption across several workers. In this wiki, an additional risk is evidence-layer collapse: schedule descriptions, speaker-attributed transcript statements, OCR-derived slide text, and external context do not carry the same evidentiary weight. The connected evaluation, memory, retrieval, and reflective-optimization sessions indicate that closed-loop capability must be paired with traceable inputs, stable baselines, explicit stopping rules, reproducible comparisons, and human review. Faster iteration is valuable only when the system can explain what changed, why it changed, and whether the measured improvement survives scrutiny.

## Applied Use
Begin with a bounded objective and an output that can actually be checked: a ranked retrieval result, a kernel benchmark, a reproduced paper result, a source-grounded market map, or a documented experiment plan. Define the baseline, evaluation metric, resource budget, and stopping rule before the loop begins. Record every query, selected and excluded source, hypothesis, code or configuration change, measured result, and rationale for the next step so that improvement can be separated from metric drift, data leakage, or accidental variance.

Match the loop to the substrate. Dense-retrieval work should preserve the frozen embedding model, corpus snapshot, candidate-generation settings, reranking procedure, query set, and test-time compute budget. Kernel research should retain generated code, compiler and hardware details, correctness checks, latency measurements, and failed variants. Parameter Golf or agent-skill hill climbing should record the exact scoring harness and every accepted or rejected mutation. Reflective optimization should distinguish whether a gain came from context, harness behavior, or model-weight changes rather than treating the entire system as one opaque candidate.

Maintain an evidence ledger that separates official schedule facts, recording- or transcript-backed observations, slide/OCR-derived notes, external supporting context, interpretations, and unresolved questions. For long-running investigations, use a memory harness that preserves decisions, failed trials, and provenance without blindly replaying stale context. For multi-agent work, assign explicit hypotheses or optimization domains, require each agent to return evidence and uncertainty, and reconcile conflicting results against a shared evaluation rather than accepting consensus as proof.

The WF2026 examples support several concrete applications: automated hill climbing for Parameter Golf and agent skills; test-time search over frozen embedding models; generation-and-benchmark loops for kernels; multi-agent exploration across optimization domains; reflective improvement of context, harnesses, and weights; and conference-intelligence synthesis across schedules, talks, transcripts, and slide evidence. The same structure can support technical due diligence, literature review, financial-compliance document correlation, competitive analysis, product discovery, and engineering design investigations when the work depends on repeated comparison rather than a single answer.

Use humans to set scope, approve consequential actions, inspect surprising gains, resolve ambiguous evidence, and decide when the investigation is sufficient. AutoResearch is most valuable when it produces an auditable research map or reproducible experiment trail; it should not be treated as a black-box authority for high-stakes conclusions.

## Active Use Cases
- Evidence-grounded briefing docs and source maps.
- Research agents that compare papers, products, or implementation patterns.
- Experiment-planning support for AI and data teams.
- Conference or domain wiki synthesis from talks, transcripts, and slides.

## Livestream Source
- [[youtube-4sX_He5c4sI]] — official WF2026 Autoresearch and keynote livestream.
- [[youtube-4sX_He5c4sI-slides]] — extracted slide/OCR deck for the livestream.

## Neighboring Subjects
- [[agent-evaluations]]
- [[agentic-search]]
- [[agent-memory]]
- [[inference-engineering]]

## Connections
- [[2026-06-30-tim-sweeney-closing-the-loop-an-autonomous-ai-research-agent]] — Closing the Loop: An Autonomous AI Research Agent; [[tim-sweeney|Tim Sweeney]] (Day 3 — Session Day 2 · 1:30pm-1:50pm · Autoresearch; official schedule)
- [[2026-06-29-zhengyao-jiang-hands-on-autoresearch-cracking-openai-s-parameter-golf]] — Hands-on AutoResearch: Cracking OpenAI's Parameter Golf; [[zhengyao-jiang|Zhengyao Jiang]], [[dixing-xu|Dixing Xu]], [[vayum-arora|Vayum Arora]], [[dhruv-srikanth|Dhruv Srikanth]] (Day 1 — Workshop Day · 2:20pm-4:20pm · Workshops Day 1; official schedule)
- [[2026-06-30-elie-bakouch-the-era-of-auto-research]] — « the era of (auto) research »; [[elie-bakouch|Elie Bakouch]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · Autoresearch; official schedule)
- [[2026-06-30-erina-karati-autoresearch-in-a-multi-agent-ai-village]] — Autoresearch in a Multi-Agent AI Village; [[erina-karati|Erina Karati]], [[arunachalam-manikandan|Arunachalam Manikandan]] (Day 3 — Session Day 2 · 3:45pm-4:05pm · Autoresearch; official schedule)
- [[2026-06-30-han-xiao-autoresearch-for-dense-retrieval-test-time-compute-with-frozen-embedding-models]] — Autoresearch for Dense Retrieval: Test-Time Compute with Frozen Embedding Models; [[han-xiao|Han Xiao]] (Day 3 — Session Day 2 · 11:10am-11:30am · Autoresearch; official schedule)
- [[2026-06-30-tejas-bhakta-autoresearch-for-kernels]] — Autoresearch for Kernels; [[tejas-bhakta|Tejas Bhakta]] (Day 3 — Session Day 2 · 2:50pm-3:10pm · Autoresearch; official schedule)
- [[2026-06-30-roland-gavrilescu-autoresearch-in-the-wild]] — Autoresearch in the wild; [[roland-gavrilescu|Roland Gavrilescu]], [[julian-bright|Julian Bright]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Autoresearch; official schedule)
- [[2026-07-01-brendan-rappazzo-alphalab-autonomous-multi-agent-research-across-optimization-domains-with-frontier-llms]] — ALPHALAB: Autonomous Multi-Agent Research Across Optimization Domains with Frontier LLMs; [[brendan-rappazzo|Brendan Rappazzo]] (Day 4 — Session Day 3 · 10:45am-11:05am · AI in Finance; official schedule)
- [[2026-06-30-benoit-schillings-research-to-reality-with-google-deepmind]] — Research to Reality with Google DeepMind; [[benoit-schillings|Benoit Schillings]] (Day 3 — Session Day 2 · 10:05am-10:25am · Autoresearch; official schedule)
- [[2026-06-30-richard-socher-first-steps-toward-automated-ai-research]] — First Steps Toward Automated AI Research; [[richard-socher|Richard Socher]] (Day 3 — Session Day 2 · 10:45am-11:05am · Autoresearch; official schedule)
- [[2026-06-30-stefania-druga-memory-harnesses-for-long-running-research-agents]] — Memory Harnesses for Long-Running Research Agents; [[stefania-druga|Stefania Druga]] (Day 3 — Session Day 2 · 11:40am-12:00pm · Memory & Continual Learning; official schedule)
- [[2026-07-01-zubin-aysola-aria-how-we-built-autoresearch-with-autoresearch]] — ARIA, how we built autoresearch with autoresearch; [[zubin-aysola|Zubin Aysola]] (Day 4 — Session Day 3 · 11:10am-11:30am · Expo Stage 2 NW; official schedule)
- [[2026-06-29-valeria-wu-fon-speech-to-speech-model-research-at-google-deepmind]] — Speech-to-Speech Model Research at Google DeepMind; [[valeria-wu-fon|Valeria Wu Fon]], [[tom-ouyang|Tom Ouyang]] (Day 2 — Session Day 1 · 11:10am-11:30am · Voice & Realtime AI; official schedule)
- [[2026-06-30-ishan-anand-will-ai-predict-people-like-we-predict-the-weather-alternate-title-a-field-guide-to-synthetic-personas-for-market-research]] — Will AI predict people like we predict the weather? (alternate title “A field guide to synthetic personas for market research”); [[ishan-anand|Ishan Anand]] (Day 3 — Session Day 2 · 2:50pm-3:10pm · Computer Use; official schedule)
- [[2026-06-30-deepak-pathak-frontier-robotics-research]] — Frontier Robotics Research; [[deepak-pathak|Deepak Pathak]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Robotics & World Models; official schedule)
- [[2026-06-30-zhengyao-jiang-an-ai-agent-became-the-1-contributor-in-openai-s-hiring-challenge]] — An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge; [[zhengyao-jiang|Zhengyao Jiang]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Autoresearch; official schedule)
- [[2026-06-29-lee-robinson-recursive-model-improvement]] — Recursive Model Improvement; [[lee-robinson|Lee Robinson]] (Day 2 — Session Day 1 · 5:10pm-5:30pm · Software Factories; verified event YouTube resource; via [[youtube-q4Tr-DknG2M]])
- [[2026-06-30-geoffrey-litt-understanding-is-the-new-bottleneck]] — Understanding is the new bottleneck; [[geoffrey-litt|Geoffrey Litt]] (Day 3 — Session Day 2 · 10:45am-11:05am · Design Engineering; verified event YouTube resource; via [[youtube-WkBPX-oDMnA]])
- [[2026-06-30-thariq-shihipar-field-guide-to-fable]] — Field Guide to Fable; [[thariq-shihipar|Thariq Shihipar]] (Day 3 — Session Day 2 · 9:05am-9:25am · Autoresearch; official schedule)
- [[2026-06-30-antje-barth-perception-agents]] — Perception Agents; [[antje-barth|Antje Barth]] (Day 3 — Session Day 2 · 9:45am-10:05am · Autoresearch; official schedule)
- [[2026-06-30-laurie-voss-evals-track-intro]] — Evals Track Intro; [[laurie-voss|Laurie Voss]], [[aparna-dhinakaran|Aparna Dhinakaran]] (Day 3 — Session Day 2 · 10:25am-10:30am · Autoresearch; official schedule)
- [[2026-06-30-lakshya-agrawal-self-improvement-of-context-harness-and-model-weights-through-reflective-optimization]] — Self-Improvement of Context, Harness, and Model Weights through Reflective Optimization; [[lakshya-agrawal|Lakshya Agrawal]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Autoresearch; official schedule)
- [[2026-06-30-wei-lin-chiang-closing-keynote]] — Closing Keynote; [[addy-osmani|Addy Osmani]] (Day 3 — Session Day 2 · 4:30pm-4:50pm · Autoresearch; official schedule)
- [[2026-06-30-george-cameron-trends-in-ai]] — Trends in AI; [[george-cameron|George Cameron]], [[micah-hill-smith|Micah Hill-Smith]] (Day 3 — Session Day 2 · 4:50pm-5:10pm · Autoresearch; official schedule)

- [[laurie-voss|Laurie Voss]]
- [[zhengyao-jiang|Zhengyao Jiang]]
- [[tim-sweeney|Tim Sweeney]]
- [[dixing-xu|Dixing Xu]]
- [[vayum-arora|Vayum Arora]]
- [[dhruv-srikanth|Dhruv Srikanth]]
- [[elie-bakouch|Elie Bakouch]]
- [[erina-karati|Erina Karati]]
- [[arunachalam-manikandan|Arunachalam Manikandan]]
- [[han-xiao|Han Xiao]]
- [[tejas-bhakta|Tejas Bhakta]]
- [[roland-gavrilescu|Roland Gavrilescu]]
- [[julian-bright|Julian Bright]]
- [[brendan-rappazzo|Brendan Rappazzo]]
- [[benoit-schillings|Benoit Schillings]]
- [[richard-socher|Richard Socher]]
- [[stefania-druga|Stefania Druga]]
- [[zubin-aysola|Zubin Aysola]]
- [[valeria-wu-fon|Valeria Wu Fon]]
- [[tom-ouyang|Tom Ouyang]]
- [[ishan-anand|Ishan Anand]]
- [[deepak-pathak|Deepak Pathak]]
- [[lee-robinson|Lee Robinson]]
- [[geoffrey-litt|Geoffrey Litt]]

- [[weco-ai|Weco AI]]
- [[google-deepmind|Google DeepMind]]
- [[arize-ai|Arize AI]]
- [[together-ai|Together AI]]
- [[weights-and-biases-by-coreweave|Weights & Biases by CoreWeave]]
- [[introspection|Introspection]]
- [[artificial-analysis|Artificial Analysis]]
- [[doordash|DoorDash]]
- [[browserbase|Browserbase]]
- [[superlinked|Superlinked]]
- [[atlassian|Atlassian]]
- [[friendliai|FriendliAI]]
- [[coreweave|Coreweave]]
- [[prime-intellect|Prime Intellect]]
- [[supercell|Supercell]]
- [[university-of-minnesota|University of Minnesota]]
- [[elastic|Elastic]]
- [[morph|Morph]]

- [[2026-06-29-shubhankar-srivastava-hill-climbing-skills-how-to-improve-agents-without-touching-the-model]] — Hill-climbing Skills: How to Improve Agents Without Touching the Model; [[shubhankar-srivastava|Shubhankar Srivastava]] (Day 1 — Workshop Day · 4:30pm-5:30pm · Workshops Day 1; official schedule)

- [[thariq-shihipar|Thariq Shihipar]]

- [[2026-06-29-nachiket-paranjape-ai-evals-platform-for-cross-functional-teams-at-scale]] — AI Evals Platform for Cross-Functional Teams at Scale; [[nachiket-paranjape|Nachiket Paranjape]], [[swaroop-chitlur-haridas|Swaroop Chitlur Haridas]] (Day 2 — Session Day 1 · 1:55pm-2:15pm · AI-Native Enterprises; official schedule)

- [[antje-barth|Antje Barth]]

- [[2026-06-29-sonar-expo-welcome-speech]] — Expo Welcome Speech; [[sonar|Sonar]], [[extend-ai|Extend AI]] (Day 1 — Workshop Day · 6:00pm-6:15pm · Expo Stage 3; related YouTube resource; via [[youtube-4sX_He5c4sI]])
- [[2026-06-29-charlie-guo-cooking-with-codex]] — Cooking with Codex; [[charlie-guo|Charlie Guo]], [[gabriel-chua|Gabriel Chua]] (Day 1 — Workshop Day · 9:00am-11:00am · Workshops Day 1; related YouTube resource; via [[youtube-dvft0Gp9sEE]])
- [[2026-06-29-charlie-guo-voice-agents-can-just-do-things]] — Voice Agents Can Just Do Things; [[charlie-guo|Charlie Guo]] (Day 2 — Session Day 1 · 11:40am-12:00pm · Voice & Realtime AI; related YouTube resource; via [[youtube-dvft0Gp9sEE]])
- [[2026-06-29-doug-guthrie-advanced-workshop-mastering-ai-observability]] — Advanced workshop: Mastering AI Observability; [[doug-guthrie|Doug Guthrie]] (Day 1 — Workshop Day · 9:00am-11:00am · Track 9; related YouTube resource; via [[youtube-bk0TmxoZlUY]])

- [[charlie-guo|Charlie Guo]]
- [[sonar|Sonar]]

- [[openai|OpenAI]]
- [[poolside|poolside]]

## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.

### Linked Sessions
- [[2026-06-30-tim-sweeney-closing-the-loop-an-autonomous-ai-research-agent|Closing the Loop: An Autonomous AI Research Agent]]
- [[2026-06-29-zhengyao-jiang-hands-on-autoresearch-cracking-openai-s-parameter-golf|Hands-on AutoResearch: Cracking OpenAI's Parameter Golf]]
- [[2026-06-30-elie-bakouch-the-era-of-auto-research|« the era of (auto) research »]]
- [[2026-06-30-erina-karati-autoresearch-in-a-multi-agent-ai-village|Autoresearch in a Multi-Agent AI Village]]
- [[2026-06-30-han-xiao-autoresearch-for-dense-retrieval-test-time-compute-with-frozen-embedding-models|Autoresearch for Dense Retrieval: Test-Time Compute with Frozen Embedding Models]]
- [[2026-06-30-tejas-bhakta-autoresearch-for-kernels|Autoresearch for Kernels]]
- [[2026-06-30-roland-gavrilescu-autoresearch-in-the-wild|Autoresearch in the wild]]
- [[2026-07-01-brendan-rappazzo-alphalab-autonomous-multi-agent-research-across-optimization-domains-with-frontier-llms|ALPHALAB: Autonomous Multi-Agent Research Across Optimization Domains with Frontier LLMs]]
- [[2026-06-30-benoit-schillings-research-to-reality-with-google-deepmind|Research to Reality with Google DeepMind]]
- [[2026-06-30-richard-socher-first-steps-toward-automated-ai-research|First Steps Toward Automated AI Research]]

### Media Signals
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-4sX_He5c4sI`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: lots, examples, stream, starts, july, land, king, chief.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube-q4Tr-DknG2M` — 4,039 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-q4Tr-DknG2M`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-q4Tr-DknG2M`: models, model, training, evals, pretty, loop, compute, cursor.
- Slide-derived themes for `youtube-q4Tr-DknG2M`: future, cursor, compute, better, model, anon, pease, days.
- Evidence links for `youtube-q4Tr-DknG2M` (primary event evidence): [[youtube-q4Tr-DknG2M]], [[youtube-q4Tr-DknG2M-transcript]], [[youtube-q4Tr-DknG2M-slides]]

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 61 | Related pages outside the main evidence categories. |
| resources | 5 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 4 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 30 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 2 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 2 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-30-tim-sweeney-closing-the-loop-an-autonomous-ai-research-agent]]
- [[2026-06-29-zhengyao-jiang-hands-on-autoresearch-cracking-openai-s-parameter-golf]]
- [[2026-06-30-elie-bakouch-the-era-of-auto-research]]
- [[2026-06-30-erina-karati-autoresearch-in-a-multi-agent-ai-village]]
- [[2026-06-30-han-xiao-autoresearch-for-dense-retrieval-test-time-compute-with-frozen-embedding-models]]
- [[2026-06-30-tejas-bhakta-autoresearch-for-kernels]]

### Resources
- [[youtube-4sX_He5c4sI]]
- [[youtube-q4Tr-DknG2M]]
- [[youtube-WkBPX-oDMnA]]
- [[youtube-dvft0Gp9sEE]]
- [[youtube-bk0TmxoZlUY]]

### Slides
- [[youtube-4sX_He5c4sI-slides]]
- [[youtube-4sX_He5c4sI-dense-slides]]
- [[youtube-4sX_He5c4sI-reconstructed-slides]]
- [[youtube-q4Tr-DknG2M-slides]]

### Transcripts
- [[youtube-4sX_He5c4sI-transcript]]
- [[youtube-q4Tr-DknG2M-transcript]]

### Tools
- [[browserbase]]
- [[prime-intellect]]
