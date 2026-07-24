---
title: Agentic Search
category: topics
sourceLabels:
  - Slide/video-derived supporting context
last_auto_summarized: '2026-07-18T14:16:27.899Z'
sourceAssessment:
  schemaVersion: 1
  claimId: claim:58b65f04598a04ca30a080efc8c6b33e7e991083d42e78d2017b3d017f56b803
  subjectId: concept:agentic-search
  domain: topics page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-24T00:00:00.000000Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-youtube--CnA2lGfymY
  - source:official-wf26-youtube-1P1hJ36rxM0
  - source:official-wf26-youtube-8G_1-3IO4ZQ
  - source:official-wf26-youtube-8qWIPUia2O8
  - source:official-wf26-youtube-Cz4v1WHVyZc
  - source:official-wf26-youtube-GgLQ02aO-hs
  - source:official-wf26-youtube-OqM67QG_Ikk
  - source:official-wf26-youtube-RGSFUqzqErE
  - source:official-wf26-youtube-YZQsWVeN3rE
  - source:official-wf26-youtube-YnNF55QV0zs
  - source:official-wf26-youtube-ZyIoTOAbRfs
  - source:official-wf26-youtube-c35YoMdnI78
  - source:official-wf26-youtube-eBUyTS7SzV4
  - source:official-wf26-youtube-iCj_ATyThvc
  - source:official-wf26-youtube-jRCpXUjz4CI
  - source:official-wf26-youtube-n97BCfyFIvw
  - source:official-wf26-youtube-uU5Gv2h8-9g
  - source:official-wf26-youtube-xUnRQ9vLXxo
sourceAssessmentBodySha256: sha256:5c02b539bdf582d95a36210b0f7368108fcdb5157f44b8e61cf472545ead99fc
---
# Agentic Search

## Overview
Agentic search turns retrieval into an explicit control loop: choose an index or source, select a retrieval mode, inspect the evidence, reformulate weak queries, follow promising relationships, and stop only when the result is adequate for the task. The conference’s Search & Retrieval program supplies concrete components for that loop. [[2026-06-29-jo-kristian-bergum-the-unreasonable-effectiveness-of-bm25-for-agentic-search|Jo Kristian Bergum’s BM25 session]] argues for retaining exact lexical matching inside agent workflows, while [[2026-07-01-session-vector-isn-t-enough-hybrid-search-and-retrieval-for-ai-engineers|Jeff Vestal’s hybrid-search session]] combines lexical and vector retrieval instead of treating embeddings as a universal replacement. [[2026-06-29-will-bryk-the-search-engine-for-the-agentic-web|Will Bryk’s Exa session]] moves the same problem onto the open web, framing search infrastructure around agent consumption. [[2026-06-30-nixon-dinh-the-death-of-keyword-search-and-the-rise-of-agent-readable-catalogs|Nixon Dinh]] focuses on catalogs whose structure agents can navigate directly, and [[2026-07-01-george-he-everyone-talks-about-document-search-but-what-about-results|George He]] sharpens the output requirement by distinguishing document retrieval from delivering usable results.

The retrieval policy is itself something to train, optimize, and evaluate. [[2026-06-29-maximilian-david-rumpf-where-rl-will-take-search|Maximilian-David Rumpf and Lotte Seifert]] connect search behavior to reinforcement learning, while [[2026-06-29-dhruv-nathawani-teaching-agents-to-search-building-synthetic-training-pipelines-with-nvidia-data-designer|Dhruv Nathawani’s NVIDIA Data Designer workshop]] addresses synthetic pipelines for teaching agents how to search. [[2026-06-30-han-xiao-autoresearch-for-dense-retrieval-test-time-compute-with-frozen-embedding-models|Han Xiao]] explores spending test-time compute around a frozen dense embedding model, making the inference procedure—not only the underlying retriever—a performance lever. [[2026-06-29-jess-wang-agentic-vs-vector-search-an-eval-driven-approach-to-coding-agent-performance|Jess Wang’s coding-agent comparison]] establishes the necessary baseline discipline: additional searches, reformulations, and tool calls should earn their cost through better task completion and evidence quality rather than being presumed superior to direct vector retrieval. Hanna Lichtenberg’s linked supporting material adds retrieval trajectories, generated queries, and supervised tool calls as a complementary training view, but it remains supporting context rather than official event evidence.

The graph and memory sessions show why the searchable unit cannot always be an isolated chunk. [[2026-06-29-nyah-macklin-rag-needs-a-map-using-graphrag-to-retrieve-connected-context|Nyah Macklin’s GraphRAG workshop]], [[2026-06-29-peter-werry-beyond-rag-build-a-relational-context-engine-from-scratch|Peter Werry’s relational context engine]], and [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens|Stephen Chin’s CrabRAG session]] foreground entities, dependencies, and persistent relationships that flat semantic search can obscure. [[2026-06-30-stefania-druga-memory-harnesses-for-long-running-research-agents|Stefania Druga’s memory-harness session]] extends that context across long-running work. Together, these sessions imply a layered retrieval architecture: lexical indexes recover identifiers and exact terms, vector indexes find semantic neighbors, relational or graph indexes expose connected evidence, and durable memory records what the agent has already examined, rejected, or learned.

Autoresearch places the search loop inside a larger experimental feedback system. Sessions from [[2026-06-30-elie-bakouch-the-era-of-auto-research|Elie Bakouch]], [[2026-06-30-tim-sweeney-closing-the-loop-an-autonomous-ai-research-agent|Tim Sweeney]], [[2026-06-30-erina-karati-autoresearch-in-a-multi-agent-ai-village|Erina Karati and Arunachalam Manikandan]], and [[2026-06-29-zhengyao-jiang-hands-on-autoresearch-cracking-openai-s-parameter-golf|Zhengyao Jiang and the Weco AI team]] connect information gathering to experiment selection, execution, evaluation, and revision. In such systems, retrieval does more than initialize a prompt: it helps select the next experiment, locates inputs and prior results, surfaces contradictory evidence, and feeds outcomes back into subsequent queries. Poor stopping criteria or repeated retrieval of already-invalidated context can therefore waste an entire autonomous compute loop.

The surrounding conference material defines the interfaces and safety controls needed to deploy this pattern. [[2026-07-01-james-russo-html-is-all-agents-need|James Russo’s “HTML Is All Agents Need”]] points toward web surfaces that agents can inspect and navigate directly. Erik Meijer’s proof-oriented keynote and [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1|Abhishek Bhardwaj’s two-part sandbox-cloud sessions]] emphasize that retrieved information may trigger consequential tool calls or code execution. A production agentic-search system therefore needs source-layer provenance, claim-to-evidence links, hybrid and relationship-aware indexes, explicit retry and stopping policies, deduplication of previously inspected evidence, bounded execution environments, and evaluations that distinguish a plausible response from one supported by sufficient evidence.

## Conference Context
It combines web search, enterprise search, information retrieval, RAG, semantic search, BM25, vector databases, knowledge graphs, and research-agent workflows. Agents add query reformulation, source triage, multi-hop exploration, and evidence synthesis.

## Significance
Many tasks fail because the agent either retrieves the wrong context or stops too early. Agentic search improves coverage, reduces hallucination, and helps systems expose the evidence behind an answer.

## Applied Use
Define the question, retrieve broadly, rerank by task relevance, inspect primary sources, track claims and citations, and loop when evidence conflicts or gaps remain. Use hybrid retrieval and structured indexes where pure vector search misses exact terms or relationships.

It is useful in research, support knowledge bases, compliance review, code search, enterprise assistants, competitive intelligence, and document-heavy operations.

Use agentic search when answers require multiple sources, fresh evidence, exact facts, or cross-document reasoning. Simple lookup or direct database queries are better for narrow deterministic questions.

## Active Use Cases
- Research agents that cite and compare sources.
- Hybrid RAG over documents, SQL, UI telemetry, and web data.
- Semantic code retrieval for coding agents.
- Enterprise knowledge agents with source-grounded answers.

## Slide-Derived Scheduled Session Signals
- [[2026-06-29-aaron-stanley-ai-s-jurassic-park-period]] — AI’s Jurassic Park Period
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]] — In Code They Act, In Proof We Trust
- [[2026-06-29-pablo-castro-on-ai-and-knowledge]] — On AI and Knowledge
- [[2026-06-29-sam-bhagwat-every-harness-will-become-a-claw]] — Every Harness Will Become A Claw
- [[2026-06-29-zach-blumenfeld-ai-on-your-lakehouse-context-comes-in-shapes-not-queries]] — AI on Your Lakehouse: Context Comes in Shapes, Not Queries
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2
- [[2026-06-30-addy-osmani-closing-keynote]] — Closing Keynote
- [[2026-06-30-alex-shaw-everything-is-a-rollout]] — Everything Is a Rollout
- [[2026-06-30-ishan-anand-will-ai-predict-people-like-we-predict-the-weather-alternate-title-a-field-guide-to-synthetic-personas-for-market-research]] — Will AI predict people like we predict the weather? (alternate title “A field guide to synthetic personas for market research”)
- [[2026-06-30-sean-cai-state-of-data]] — State of Data
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one]] — Video Has No Memory. Here's How We Built One.
- [[2026-07-01-james-russo-html-is-all-agents-need]] — HTML Is All Agents Need
- [[2026-07-01-maxime-rivest-the-unreasonable-effectiveness-of-separating-the-task-from-the-model]] — The Unreasonable Effectiveness of Separating the Task from the Model
- [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens]] — CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens
- [[2026-07-01-yohei-nakajima-active-graph-agent-runtime-babyagi-4]] — Active Graph Agent Runtime (BabyAGI 4)

## Slide-Derived Supporting Decks
- [[youtube--CnA2lGfymY-slides]] — "I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox (32 extracted slide frames)
- [[youtube-1lgFGaHoGq8-slides]] — AI’s Jurassic Park Period — Aaron Stanley, dbt Labs (12 extracted slide frames)
- [[youtube-1P1hJ36rxM0-slides]] — Research to Reality with Google DeepMind — Benoit Schillings, Google DeepMind (15 extracted slide frames)
- [[youtube-8qWIPUia2O8-slides]] — Every Harness Will Become A Claw — Sam Bhagwat, Mastra (13 extracted slide frames)
- [[youtube-c35YoMdnI78-slides]] — The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents (32 extracted slide frames)
- [[youtube-Cz4v1WHVyZc-slides]] — HTML Is All Agents Need — James Russo, HeyGen (32 extracted slide frames)
- [[youtube-GgLQ02aO-hs-slides]] — The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest, DSPy (22 extracted slide frames)
- [[youtube-jRCpXUjz4CI-slides]] — Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute (32 extracted slide frames)
- [[youtube-khVX_BUnEwU-slides]] — Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital (31 extracted slide frames)
- [[youtube-kRkcNOsRyYg-slides]] — AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j (32 extracted slide frames)
- [[youtube-mOf-PP4mVjA-slides]] — Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs (31 extracted slide frames)
- [[youtube-n97BCfyFIvw-slides]] — "The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani (32 extracted slide frames)
- [[youtube-OqM67QG_Ikk-slides]] — From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI (15 extracted slide frames)
- [[youtube-Q0VkgCyNVUg-slides]] — CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j (22 extracted slide frames)
- [[youtube-RGSFUqzqErE-slides]] — On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft (28 extracted slide frames)
- [[youtube-YnNF55QV0zs-slides]] — Persona Engineering: A Field Guide to AI Synthetic Personas — Ishan Anand, InsightSciences.ai (4 extracted slide frames)
- [[youtube-ZyIoTOAbRfs-slides]] — State of Data — Sean Cai, Independent / State of Data (10 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

## Transcript Digest Evidence
This section synthesizes 13 evidence-bound talk topic candidates across at least two talks.

### Cross-Talk Synthesis
These candidates frame retrieval as a structured reasoning layer rather than a passive lookup step, with provenance, satisfaction checking, and navigable knowledge structures built into the search flow. The variation is between query routing, graph-centered recall, and entity-grounded synthesis, but all of them prioritize traceable paths through information over flat result lists.

### Constituent Talk Evidence
- [[2026-06-29-pablo-castro-on-ai-and-knowledge|On AI and Knowledge]] — A retrieval architecture that supports both simple usage and expert control in one system.
  - Transcript: [[youtube-RGSFUqzqErE-transcript]]
  - Evidence: "So, in Foundry IQ, that was one of our core design goals. And the way we do this is we actually layer the system."
- [[2026-06-29-zach-blumenfeld-ai-on-your-lakehouse-context-comes-in-shapes-not-queries|AI on Your Lakehouse: Context Comes in Shapes, Not Queries]] — A containment-tree view of documents with hierarchical links and drill-down navigation.
  - Transcript: [[youtube-kRkcNOsRyYg-transcript]]
  - Evidence: "Um, that's the general idea with this. And so what this gives the agent to do is not just search like vector search or or lexical search but actually kind of traverse through the documents in a sense."
- [[2026-07-01-daniel-chalef-citation-needed-provenance-for-llm-built-knowledge-graphs|Citation Needed: Provenance for LLM-Built Knowledge Graphs]] — Applying different trust rules when a fact has multiple parents and mixed-source ancestry.
  - Transcript: [[youtube-H7puB0RwJMM-transcript]]
  - Evidence: "So one tagging action at ingestion supports evaluating the veracity of a fact. But what if the fact is three parents or more?"
- [[2026-07-01-omri-bruchim-from-systems-of-record-to-systems-of-context|From Systems of Record to Systems of Context]] — A queryable organizational layer that links entities, history, permissions, and decisions into reusable context.
  - Transcript: [[youtube-Btk8wDUVs74-transcript]]
  - Evidence: "Um and this is why we have built what we are building. We are building uh the Monday world model."
- [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens|CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens]] — Answers that can be inspected and traced back to a specific graph path.
  - Transcript: [[youtube-Q0VkgCyNVUg-transcript]]
  - Evidence: "And graphs are they're accurate so they give you very precise information. Explainable because you can look at the graph which got returned and auditable because now you can actually say these are the this is the context."
- [[2026-07-01-theo-browne-closing-keynote-theo-browne|Closing Keynote — Theo Browne]] — The talk argues developers are overvaluing familiar interfaces and workflows.
  - Transcript: [[youtube-xUnRQ9vLXxo-transcript]]
  - Evidence: "we got over it. we got over it. We're currently in our skeuomorphic We're currently in our skeuomorphic We're currently in our skeuomorphic phase as software developers."

## Connections
- [[2026-07-01-session-vector-isn-t-enough-hybrid-search-and-retrieval-for-ai-engineers]] — Vector Isn't Enough: Hybrid Search & Retrieval for AI Engineers; [[jeff-vestal|Jeff Vestal]] (Day 1 — Workshop Day · 2:20pm-4:20pm · Track 7; official schedule)
- [[2026-06-29-jo-kristian-bergum-the-unreasonable-effectiveness-of-bm25-for-agentic-search]] — The unreasonable effectiveness of BM25 for agentic search; [[jo-kristian-bergum|Jo Kristian Bergum]] (Day 2 — Session Day 1 · 11:10am-11:30am · Search & Retrieval; official schedule)
- [[2026-06-29-will-bryk-the-search-engine-for-the-agentic-web]] — The Search Engine for the Agentic Web; [[will-bryk|Will Bryk]] (Day 2 — Session Day 1 · 11:40am-12:00pm · Search & Retrieval; official schedule)
- [[2026-06-29-maximilian-david-rumpf-where-rl-will-take-search]] — Where RL Will Take Search; [[maximilian-david-rumpf|Maximilian-David Rumpf]], [[lotte-seifert|Lotte Seifert]] (Day 2 — Session Day 1 · 2:50pm-3:10pm · Search & Retrieval; official schedule)
- [[2026-06-30-han-xiao-autoresearch-for-dense-retrieval-test-time-compute-with-frozen-embedding-models]] — Autoresearch for Dense Retrieval: Test-Time Compute with Frozen Embedding Models; [[han-xiao|Han Xiao]] (Day 3 — Session Day 2 · 11:10am-11:30am · Autoresearch; official schedule)
- [[2026-06-30-elie-bakouch-the-era-of-auto-research]] — « the era of (auto) research »; [[elie-bakouch|Elie Bakouch]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · Autoresearch; official schedule)
- [[2026-06-30-tim-sweeney-closing-the-loop-an-autonomous-ai-research-agent]] — Closing the Loop: An Autonomous AI Research Agent; [[tim-sweeney|Tim Sweeney]] (Day 3 — Session Day 2 · 1:30pm-1:50pm · Autoresearch; official schedule)
- [[2026-06-29-dhruv-nathawani-teaching-agents-to-search-building-synthetic-training-pipelines-with-nvidia-data-designer]] — Teaching Agents to Search: Building Synthetic Training Pipelines with NVIDIA Data Designer; [[dhruv-nathawani|Dhruv Nathawani]] (Day 1 — Workshop Day · 11:05am-12:05pm · Workshops Day 1; official schedule)
- [[2026-06-30-erina-karati-autoresearch-in-a-multi-agent-ai-village]] — Autoresearch in a Multi-Agent AI Village; [[erina-karati|Erina Karati]], [[arunachalam-manikandan|Arunachalam Manikandan]] (Day 3 — Session Day 2 · 3:45pm-4:05pm · Autoresearch; official schedule)
- [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens]] — CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens; [[stephen-chin|Stephen Chin]] (Day 4 — Session Day 3 · 10:45am-11:05am · Graphs; official schedule)
- [[2026-06-29-zhengyao-jiang-hands-on-autoresearch-cracking-openai-s-parameter-golf]] — Hands-on AutoResearch: Cracking OpenAI's Parameter Golf; [[zhengyao-jiang|Zhengyao Jiang]], [[dixing-xu|Dixing Xu]], [[vayum-arora|Vayum Arora]], [[dhruv-srikanth|Dhruv Srikanth]] (Day 1 — Workshop Day · 2:20pm-4:20pm · Workshops Day 1; official schedule)
- [[2026-06-30-benoit-schillings-research-to-reality-with-google-deepmind]] — Research to Reality with Google DeepMind; [[benoit-schillings|Benoit Schillings]] (Day 3 — Session Day 2 · 10:05am-10:25am · Autoresearch; official schedule)
- [[2026-06-30-richard-socher-first-steps-toward-automated-ai-research]] — First Steps Toward Automated AI Research; [[richard-socher|Richard Socher]] (Day 3 — Session Day 2 · 10:45am-11:05am · Autoresearch; official schedule)
- [[2026-06-30-tejas-bhakta-autoresearch-for-kernels]] — Autoresearch for Kernels; [[tejas-bhakta|Tejas Bhakta]] (Day 3 — Session Day 2 · 2:50pm-3:10pm · Autoresearch; official schedule)
- [[2026-06-30-roland-gavrilescu-autoresearch-in-the-wild]] — Autoresearch in the wild; [[roland-gavrilescu|Roland Gavrilescu]], [[julian-bright|Julian Bright]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Autoresearch; official schedule)
- [[2026-07-01-brendan-rappazzo-alphalab-autonomous-multi-agent-research-across-optimization-domains-with-frontier-llms]] — ALPHALAB: Autonomous Multi-Agent Research Across Optimization Domains with Frontier LLMs; [[brendan-rappazzo|Brendan Rappazzo]] (Day 4 — Session Day 3 · 10:45am-11:05am · AI in Finance; official schedule)
- [[2026-06-29-nyah-macklin-rag-needs-a-map-using-graphrag-to-retrieve-connected-context]] — RAG Needs a Map: Using GraphRAG to Retrieve Connected Context; [[nyah-macklin|Nyah Macklin]] (Day 1 — Workshop Day · 11:05am-12:05pm · Track 2; official schedule)
- [[2026-06-29-jess-wang-agentic-vs-vector-search-an-eval-driven-approach-to-coding-agent-performance]] — Agentic vs. Vector Search: An Eval-Driven Approach to Coding Agent Performance; [[jess-wang|Jess Wang]] (Day 2 — Session Day 1 · 11:40am-12:00pm · Expo Stage 2 NW; official schedule)
- [[2026-06-30-nixon-dinh-the-death-of-keyword-search-and-the-rise-of-agent-readable-catalogs]] — The Death of Keyword Search and the Rise of Agent-Readable Catalogs; [[nixon-dinh|Nixon Dinh]] (Day 3 — Session Day 2 · 11:10am-11:30am · Expo Stage 3; official schedule)
- [[2026-07-01-george-he-everyone-talks-about-document-search-but-what-about-results]] — Everyone talks about document search, but what about results?; [[george-he|George He]] (Day 4 — Session Day 3 · 1:55pm-2:15pm · Expo Stage 4 SE; official schedule)
- [[2026-06-30-stefania-druga-memory-harnesses-for-long-running-research-agents]] — Memory Harnesses for Long-Running Research Agents; [[stefania-druga|Stefania Druga]] (Day 3 — Session Day 2 · 11:40am-12:00pm · Memory & Continual Learning; official schedule)
- [[2026-07-01-zubin-aysola-aria-how-we-built-autoresearch-with-autoresearch]] — ARIA, how we built autoresearch with autoresearch; [[zubin-aysola|Zubin Aysola]] (Day 4 — Session Day 3 · 11:10am-11:30am · Expo Stage 2 NW; official schedule)
- [[2026-06-29-peter-werry-beyond-rag-build-a-relational-context-engine-from-scratch]] — Beyond RAG: Build a Relational Context Engine from Scratch; [[peter-werry|Peter Werry]] (Day 1 — Workshop Day · 12:10pm-1:10pm · Workshops Day 1; official schedule)
- [[2026-06-29-valeria-wu-fon-speech-to-speech-model-research-at-google-deepmind]] — Speech-to-Speech Model Research at Google DeepMind; [[valeria-wu-fon|Valeria Wu Fon]], [[tom-ouyang|Tom Ouyang]] (Day 2 — Session Day 1 · 11:10am-11:30am · Voice & Realtime AI; official schedule)

- [[zhengyao-jiang|Zhengyao Jiang]]
- [[brandon-waselnuk|Brandon Waselnuk]]
- [[kent-c-dodds|Kent C. Dodds]]
- [[abhishek-bhardwaj|Abhishek Bhardwaj]]
- [[jeff-vestal|Jeff Vestal]]
- [[jo-kristian-bergum|Jo Kristian Bergum]]
- [[will-bryk|Will Bryk]]
- [[maximilian-david-rumpf|Maximilian-David Rumpf]]
- [[lotte-seifert|Lotte Seifert]]
- [[han-xiao|Han Xiao]]
- [[elie-bakouch|Elie Bakouch]]
- [[tim-sweeney|Tim Sweeney]]
- [[dhruv-nathawani|Dhruv Nathawani]]
- [[erina-karati|Erina Karati]]
- [[arunachalam-manikandan|Arunachalam Manikandan]]
- [[stephen-chin|Stephen Chin]]
- [[dixing-xu|Dixing Xu]]
- [[vayum-arora|Vayum Arora]]
- [[dhruv-srikanth|Dhruv Srikanth]]
- [[benoit-schillings|Benoit Schillings]]
- [[richard-socher|Richard Socher]]
- [[tejas-bhakta|Tejas Bhakta]]
- [[roland-gavrilescu|Roland Gavrilescu]]
- [[julian-bright|Julian Bright]]

- [[nvidia|NVIDIA]]
- [[weco-ai|Weco AI]]
- [[google-deepmind|Google DeepMind]]
- [[neo4j|Neo4j]]
- [[unblocked|Unblocked]]
- [[bright-data|Bright Data]]
- [[oracle|Oracle]]
- [[amazon-agi-lab|Amazon AGI Lab]]
- [[elastic|Elastic]]
- [[weights-and-biases-by-coreweave|Weights & Biases by CoreWeave]]
- [[introspection|Introspection]]
- [[exa|Exa]]
- [[turbopuffer|turbopuffer]]
- [[llamaindex|LlamaIndex]]
- [[artificial-analysis|Artificial Analysis]]
- [[prime-intellect|Prime Intellect]]
- [[datologyai|DatologyAI]]
- [[browserbase|Browserbase]]

- [[charlie-guo|Charlie Guo]]
- [[christopher-manning|Christopher Manning]]

- [[openai|OpenAI]]

- [[youtube-HsxQICTLF84-slides]] — Building an ACP-Compatible Agent Live — Bennet Fenner, Zed (5 extracted slide frames)
- [[youtube-IQkVMvXQKLY-slides]] — Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis (14 extracted slide frames)
- [[youtube-1IdzkRVmWAA-slides]] — How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI (5 extracted slide frames)
- [[youtube-2e9ANoOEn28-slides]] — What if the harness mattered more than the model? - Aditya Bhargava, Etsy (8 extracted slide frames)
- [[youtube-CLttOU7n6sI-slides]] — Respect The Process - Andrew Dumit, Watershed Technology Inc. (16 extracted slide frames)
- [[youtube-UcYoMg-8-L8-slides]] — 500 people vibe-coded for 30 days. I was one of them. - Sanja Grbic, Automattic (11 extracted slide frames)
- [[youtube-2IxD9OB3XuQ-slides]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI (24 extracted slide frames)

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 50 | Related pages outside the main evidence categories. |
| resources | 18 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 45 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 42 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 5 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 18 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-jo-kristian-bergum-the-unreasonable-effectiveness-of-bm25-for-agentic-search]]
- [[2026-07-01-session-vector-isn-t-enough-hybrid-search-and-retrieval-for-ai-engineers]]
- [[2026-06-29-will-bryk-the-search-engine-for-the-agentic-web]]
- [[2026-06-30-nixon-dinh-the-death-of-keyword-search-and-the-rise-of-agent-readable-catalogs]]
- [[2026-07-01-george-he-everyone-talks-about-document-search-but-what-about-results]]
- [[2026-06-29-maximilian-david-rumpf-where-rl-will-take-search]]

### Resources
- [[youtube-4sX_He5c4sI]]
- [[youtube-RGSFUqzqErE]]
- [[youtube-kRkcNOsRyYg]]
- [[youtube-H7puB0RwJMM]]
- [[youtube-Btk8wDUVs74]]
- [[youtube-I2cbIws9j10]]

### Slides
- [[youtube--CnA2lGfymY-slides]]
- [[youtube-1lgFGaHoGq8-slides]]
- [[youtube-1P1hJ36rxM0-slides]]
- [[youtube-8qWIPUia2O8-slides]]
- [[youtube-c35YoMdnI78-slides]]
- [[youtube-Cz4v1WHVyZc-slides]]

### Transcripts
- [[youtube-RGSFUqzqErE-transcript]]
- [[youtube-kRkcNOsRyYg-transcript]]
- [[youtube-H7puB0RwJMM-transcript]]
- [[youtube-Btk8wDUVs74-transcript]]
- [[youtube-Q0VkgCyNVUg-transcript]]
- [[youtube-xUnRQ9vLXxo-transcript]]

### Tools
- [[neo4j]]
- [[exa]]
- [[llamaindex]]
- [[prime-intellect]]
- [[browserbase]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.

### Linked Sessions
- [[2026-06-29-jo-kristian-bergum-the-unreasonable-effectiveness-of-bm25-for-agentic-search|The unreasonable effectiveness of BM25 for agentic search]]
- [[2026-07-01-session-vector-isn-t-enough-hybrid-search-and-retrieval-for-ai-engineers|Vector Isn't Enough: Hybrid Search & Retrieval for AI Engineers]]
- [[2026-06-29-will-bryk-the-search-engine-for-the-agentic-web|The Search Engine for the Agentic Web]]
- [[2026-06-30-nixon-dinh-the-death-of-keyword-search-and-the-rise-of-agent-readable-catalogs|The Death of Keyword Search and the Rise of Agent-Readable Catalogs]]
- [[2026-07-01-george-he-everyone-talks-about-document-search-but-what-about-results|Everyone talks about document search, but what about results?]]
- [[2026-06-29-maximilian-david-rumpf-where-rl-will-take-search|Where RL Will Take Search]]
- [[2026-06-29-dhruv-nathawani-teaching-agents-to-search-building-synthetic-training-pipelines-with-nvidia-data-designer|Teaching Agents to Search: Building Synthetic Training Pipelines with NVIDIA Data Designer]]
- [[2026-06-30-han-xiao-autoresearch-for-dense-retrieval-test-time-compute-with-frozen-embedding-models|Autoresearch for Dense Retrieval: Test-Time Compute with Frozen Embedding Models]]
- [[2026-06-29-jess-wang-agentic-vs-vector-search-an-eval-driven-approach-to-coding-agent-performance|Agentic vs. Vector Search: An Eval-Driven Approach to Coding Agent Performance]]
- [[2026-06-29-nyah-macklin-rag-needs-a-map-using-graphrag-to-retrieve-connected-context|RAG Needs a Map: Using GraphRAG to Retrieve Connected Context]]

### Media Signals
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-4sX_He5c4sI`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: lots, examples, stream, starts, july, land, king, chief.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube-RGSFUqzqErE` — 3,081 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-RGSFUqzqErE`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-RGSFUqzqErE`: knowledge, data, retrieval, foundry, whatnot, microsoft, models, give.
- Slide-derived themes for `youtube-RGSFUqzqErE`: fair, engineering, future, bile, microsoft, resolve, knowledge, pablo.
- Evidence links for `youtube-RGSFUqzqErE` (primary event evidence): [[youtube-RGSFUqzqErE]], [[youtube-RGSFUqzqErE-transcript]], [[youtube-RGSFUqzqErE-slides]]
- `youtube-kRkcNOsRyYg` — 18,117 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-kRkcNOsRyYg`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-kRkcNOsRyYg`: graph, data, well, question, inside, search, over, documents.
- Slide-derived themes for `youtube-kRkcNOsRyYg`: engineering, future, engineer, squire, ryan, knight, senior, partner.
- Evidence links for `youtube-kRkcNOsRyYg` (primary event evidence): [[youtube-kRkcNOsRyYg]], [[youtube-kRkcNOsRyYg-transcript]], [[youtube-kRkcNOsRyYg-slides]]
- `youtube-H7puB0RwJMM` — 2,544 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-H7puB0RwJMM`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-H7puB0RwJMM`: fact, graph, data, source, graffiti, facts, provenence, sources.
- Slide-derived themes for `youtube-H7puB0RwJMM`: track, graphs, provenance, engineering, future, temporal, knowledge, built.
- Evidence links for `youtube-H7puB0RwJMM` (primary event evidence): [[youtube-H7puB0RwJMM]], [[youtube-H7puB0RwJMM-transcript]], [[youtube-H7puB0RwJMM-slides]]
- `youtube-Btk8wDUVs74` — 2,510 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Btk8wDUVs74`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Btk8wDUVs74`: data, understand, monday, context, help, model, user, over.
- Slide-derived themes for `youtube-Btk8wDUVs74`: data, track, july, missing, stack, records, systems, context.
- Evidence links for `youtube-Btk8wDUVs74` (primary event evidence): [[youtube-Btk8wDUVs74]], [[youtube-Btk8wDUVs74-transcript]], [[youtube-Btk8wDUVs74-slides]]
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
- `youtube-mOf-PP4mVjA` — 3,509 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-mOf-PP4mVjA`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-mOf-PP4mVjA`: memory, scene, content, system, across, layer, application, context.
- Slide-derived themes for `youtube-mOf-PP4mVjA`: memory, built, data, incredibly, complex, scale, holistic, understanding.
- Evidence links for `youtube-mOf-PP4mVjA` (primary event evidence): [[youtube-mOf-PP4mVjA]], [[youtube-mOf-PP4mVjA-transcript]], [[youtube-mOf-PP4mVjA-slides]]
- `youtube-8G_1-3IO4ZQ` — 3,420 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-8G_1-3IO4ZQ`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-8G_1-3IO4ZQ`: context, team, started, learn, skills, company, question, systems.
- Slide-derived themes for `youtube-8G_1-3IO4ZQ`: context, layer, keep, companies, track, july, human, specialized.
- Evidence links for `youtube-8G_1-3IO4ZQ` (primary event evidence): [[youtube-8G_1-3IO4ZQ]], [[youtube-8G_1-3IO4ZQ-transcript]], [[youtube-8G_1-3IO4ZQ-slides]]
- `youtube-YZQsWVeN3rE` — 2,901 transcript words; 3 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-YZQsWVeN3rE`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-YZQsWVeN3rE`: product, first, data, important, back, team, go-to-market, give.
- Slide-derived themes for `youtube-YZQsWVeN3rE`: juries, librarians, solve, trust, problem, alex, bauer, upside.
- Evidence links for `youtube-YZQsWVeN3rE` (primary event evidence): [[youtube-YZQsWVeN3rE]], [[youtube-YZQsWVeN3rE-transcript]], [[youtube-YZQsWVeN3rE-slides]]
- `youtube-eBUyTS7SzV4` — 3,551 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-eBUyTS7SzV4`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-eBUyTS7SzV4`: company, open, companies, brain, code, three, does, person.
- Evidence links for `youtube-eBUyTS7SzV4` (primary event evidence): [[youtube-eBUyTS7SzV4]], [[youtube-eBUyTS7SzV4-transcript]]
- `youtube-iCj_ATyThvc` — 1,795 transcript words; 4 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-iCj_ATyThvc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-iCj_ATyThvc`: research, auto, aiden, human, training, ideas, data, competition.
- Slide-derived themes for `youtube-iCj_ATyThvc`: code, golf, neural, networks, train, best, language, model.
- Evidence links for `youtube-iCj_ATyThvc` (primary event evidence): [[youtube-iCj_ATyThvc]], [[youtube-iCj_ATyThvc-transcript]], [[youtube-iCj_ATyThvc-slides]]
- `youtube-uU5Gv2h8-9g` — 10,417 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-uU5Gv2h8-9g`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-uU5Gv2h8-9g`: code, claude, prompt, been, cloud, model, mode, team.
- Evidence links for `youtube-uU5Gv2h8-9g` (primary event evidence): [[youtube-uU5Gv2h8-9g]], [[youtube-uU5Gv2h8-9g-transcript]], [[youtube-uU5Gv2h8-9g-slides]]
- `youtube-jt1Pbr_n6oU` — 3,441 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-jt1Pbr_n6oU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-jt1Pbr_n6oU`: data, model, graph, across, structure, chat, part, structured.
- Slide-derived themes for `youtube-jt1Pbr_n6oU`: track, july, fair, intro, defensible, organization, presented, users.
- Evidence links for `youtube-jt1Pbr_n6oU` (primary event evidence): [[youtube-jt1Pbr_n6oU]], [[youtube-jt1Pbr_n6oU-transcript]], [[youtube-jt1Pbr_n6oU-slides]]
- `youtube-khVX_BUnEwU` — 3,675 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-khVX_BUnEwU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-khVX_BUnEwU`: graph, pack, activegraph, called, didn, code, event, state.
- Slide-derived themes for `youtube-khVX_BUnEwU`: track, july, engineering, future, graph, ieee, greene, behavior.
- Evidence links for `youtube-khVX_BUnEwU` (primary event evidence): [[youtube-khVX_BUnEwU]], [[youtube-khVX_BUnEwU-transcript]], [[youtube-khVX_BUnEwU-slides]]
- `youtube-T5IMo5ntyhA` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-T5IMo5ntyhA`: text, memory, description, financial, goal, type, target, amount.
- Evidence links for `youtube-T5IMo5ntyhA` (supporting context only): [[youtube-T5IMo5ntyhA]], [[youtube-T5IMo5ntyhA-slides]], [[youtube-T5IMo5ntyhA-dense-slides]], [[youtube-T5IMo5ntyhA-reconstructed-slides]]
- `youtube-1IdzkRVmWAA` — 6,138 transcript words; 4 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-1IdzkRVmWAA`: search, query, tools, queries, tool, retrieval, semantic, chunks.
- Slide-derived themes for `youtube-1IdzkRVmWAA`: taught, retrieval, trajectories, tool, calls, toes.
- Evidence links for `youtube-1IdzkRVmWAA` (supporting context only): [[youtube-1IdzkRVmWAA]], [[youtube-1IdzkRVmWAA-transcript]], [[youtube-1IdzkRVmWAA-slides]]
- `youtube-xnXqpUW_Kp8` — 8 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-xnXqpUW_Kp8`: built, humans, queries, biden, information, traditional, search, engines.
- Evidence links for `youtube-xnXqpUW_Kp8` (supporting context only): [[youtube-xnXqpUW_Kp8]], [[youtube-xnXqpUW_Kp8-slides]], [[youtube-xnXqpUW_Kp8-dense-slides]], [[youtube-xnXqpUW_Kp8-reconstructed-slides]]
