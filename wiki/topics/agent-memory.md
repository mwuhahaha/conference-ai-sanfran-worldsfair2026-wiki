---
title: Agent Memory
category: topics
sourceLabels:
  - Slide/video-derived supporting context
last_auto_summarized: '2026-07-18T06:14:28.335Z'
sourceAssessment:
  schemaVersion: 1
  claimId: claim:8c6b128508f3d2b28e81cb166edc23205c391d3cde8a1be8619b309da4e4264c
  subjectId: concept:agent-memory
  domain: topics page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-24T00:00:00.000000Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-youtube-8G_1-3IO4ZQ
  - source:official-wf26-youtube-8qWIPUia2O8
  - source:official-wf26-youtube-9QebvrrY3KY
  - source:official-wf26-youtube-GgLQ02aO-hs
  - source:official-wf26-youtube-OqM67QG_Ikk
  - source:official-wf26-youtube-RGSFUqzqErE
  - source:official-wf26-youtube-VrpEyglYgeU
  - source:official-wf26-youtube-WkBPX-oDMnA
  - source:official-wf26-youtube-X1kp-ABIIxQ
  - source:official-wf26-youtube-YZQsWVeN3rE
  - source:official-wf26-youtube-eBUyTS7SzV4
  - source:official-wf26-youtube-iCj_ATyThvc
  - source:official-wf26-youtube-n97BCfyFIvw
sourceAssessmentBodySha256: sha256:244377762dfea36c030c96f0c6a83215a66139da5b0446d79ee4f742d2dff1bf
---
# Agent Memory

## Overview
Agent memory is the state and retrieval layer that lets an agent preserve useful context beyond a single prompt. The World’s Fair program treats it as a concrete systems problem spanning working context, durable stores, compaction, graph and relational retrieval, context layers, databases, harnesses, and continual learning. Connected sessions examine moving from context to a dedicated memory layer, building memory harnesses for long-running research, replacing token-heavy retrieval with graph memory, giving video persistent recall, and deciding what belongs in prompts, memory, or model weights. Together, they frame memory not as unlimited transcript storage, but as a governed process for selecting, preserving, refreshing, retrieving, and forgetting source-backed state.

## Conference Context
The topic comes from classic AI state management, knowledge representation, retrieval systems, personal assistants, and database-backed application design. The long-context era changed the tradeoff: teams can stuff more into prompts, but still need structured memory so agents can reason over the right facts at the right time.

## Significance
Memory determines whether an agent can act consistently instead of restarting from scratch. It improves personalization, reduces repeated work, supports multi-step workflows, and makes decisions auditable. Poor memory creates stale assumptions, privacy risk, context bloat, and confident mistakes.

## Applied Use
Separate working context from durable memory. Store source-backed facts, decisions, user preferences, and artifacts with timestamps and provenance. Retrieve by task intent, not just lexical similarity. Add policies for freshness, deletion, permissions, and summarization, and test memory behavior with scenario-based evals.

Memory is useful in coding agents, customer support, research assistants, enterprise knowledge agents, personal productivity tools, and any workflow that spans multiple sessions or documents.

Use durable memory when repeated interaction or long-horizon work matters. Avoid it for one-shot tasks, sensitive data without clear retention rules, or cases where stale state would be more harmful than asking again.

## Active Use Cases
- Remembering repository architecture and prior implementation decisions.
- Maintaining user preferences and project constraints across sessions.
- Decision-trace retrieval for enterprise workflows.
- Long-context cache and knowledge-graph backed agent workflows.

## Slide-Derived Scheduled Session Signals
- [[2026-06-29-pablo-castro-on-ai-and-knowledge]] — On AI and Knowledge
- [[2026-06-29-sam-bhagwat-every-harness-will-become-a-claw]] — Every Harness Will Become A Claw
- [[2026-06-29-zach-blumenfeld-ai-on-your-lakehouse-context-comes-in-shapes-not-queries]] — AI on Your Lakehouse: Context Comes in Shapes, Not Queries
- [[2026-06-30-addy-osmani-closing-keynote]] — Closing Keynote
- [[2026-06-30-dan-farrelly-your-agent-architecture-has-a-half-life-of-6-months]] — Your agent architecture has a half-life of 6 months
- [[2026-06-30-prukalpa-sankar-wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents]] — WTF Is the Context Layer? The Missing Infrastructure for Production Agents
- [[2026-06-30-tariq-shaukat-in-the-land-of-ai-agents-the-verifiers-are-king]] — In the Land of AI Agents, the Verifiers Are King
- [[2026-07-01-daniel-chalef-citation-needed-provenance-for-llm-built-knowledge-graphs]] — Citation Needed: Provenance for LLM-Built Knowledge Graphs
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one]] — Video Has No Memory. Here's How We Built One.
- [[2026-07-01-maxime-rivest-the-unreasonable-effectiveness-of-separating-the-task-from-the-model]] — The Unreasonable Effectiveness of Separating the Task from the Model
- [[2026-07-01-omri-bruchim-from-systems-of-record-to-systems-of-context]] — From Systems of Record to Systems of Context
- [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens]] — CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens
- [[2026-07-01-yohei-nakajima-active-graph-agent-runtime-babyagi-4]] — Active Graph Agent Runtime (BabyAGI 4)

## Slide-Derived Supporting Decks
- [[youtube-8G_1-3IO4ZQ-slides]] —  (10 extracted slide frames)
- [[youtube-8qWIPUia2O8-slides]] — Every Harness Will Become A Claw — Sam Bhagwat, Mastra (13 extracted slide frames)
- [[youtube-Btk8wDUVs74-slides]] — From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com (19 extracted slide frames)
- [[youtube-GgLQ02aO-hs-slides]] — The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest, DSPy (22 extracted slide frames)
- [[youtube-H7puB0RwJMM-slides]] — Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI (5 extracted slide frames)
- [[youtube-il1c1a2FufU-slides]] — Setting Yourself Up for Success — Part 1 — Jason Liu, OpenAI (12 extracted slide frames)
- [[youtube-khVX_BUnEwU-slides]] — Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital (31 extracted slide frames)
- [[youtube-kRkcNOsRyYg-slides]] — AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j (32 extracted slide frames)
- [[youtube-mOf-PP4mVjA-slides]] — Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs (31 extracted slide frames)
- [[youtube-n97BCfyFIvw-slides]] — "The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani (32 extracted slide frames)
- [[youtube-Q0VkgCyNVUg-slides]] — CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j (22 extracted slide frames)
- [[youtube-RGSFUqzqErE-slides]] — On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft (28 extracted slide frames)
- [[youtube-VrpEyglYgeU-slides]] — In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar (32 extracted slide frames)
- [[youtube-X1kp-ABIIxQ-slides]] — Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest (15 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

## Transcript Digest Evidence
This section synthesizes 42 evidence-bound talk topic candidates across at least two talks.

### Cross-Talk Synthesis
Persistent context systems that let agents retain, retrieve, and audit useful knowledge across sessions and artifacts. The variations include traces, graphs, ontologies, provenance, and writable memory, with the central tradeoff being richer recall versus higher complexity and maintenance cost.

### Constituent Talk Evidence
- [[2026-06-29-lance-martin-claude-for-long-horizon-tasks|Claude for long-horizon tasks]] — Offline passes that inspect traces and repair memory errors.
  - Transcript: [[youtube-9QebvrrY3KY-transcript]]
  - Evidence: "This is a very important nuance in this process of dreaming is is kind of an offline or out of band process that we've used to consolidate and improve memory."
- [[2026-06-29-pablo-castro-on-ai-and-knowledge|On AI and Knowledge]] — A retrieval architecture that supports both simple usage and expert control in one system.
  - Transcript: [[youtube-RGSFUqzqErE-transcript]]
  - Evidence: "So, in Foundry IQ, that was one of our core design goals. And the way we do this is we actually layer the system."
- [[2026-06-29-zach-blumenfeld-ai-on-your-lakehouse-context-comes-in-shapes-not-queries|AI on Your Lakehouse: Context Comes in Shapes, Not Queries]] — A containment-tree view of documents with hierarchical links and drill-down navigation.
  - Transcript: [[youtube-kRkcNOsRyYg-transcript]]
  - Evidence: "Um, that's the general idea with this. And so what this gives the agent to do is not just search like vector search or or lexical search but actually kind of traverse through the documents in a sense."
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1']] — Saved sandbox state that survives failures and long tasks.
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
  - Evidence: "So, we want to give them durable storage. And so, this this part of the presentation is specifically working on disk storage, not memory persistence, but disk persistence."
- [[2026-06-30-addy-osmani-closing-keynote|Closing Keynote]] — The erosion of understanding and memory that can follow heavy reliance on agents.
  - Transcript: [[youtube-n97BCfyFIvw-transcript]]
  - Evidence: "Well, the first thing to avoid really is cognitive debt. Now, cognitive debt is the erosion of your understanding and memory around how to solve problems."
- [[2026-06-30-dan-farrelly-your-agent-architecture-has-a-half-life-of-6-months|Your agent architecture has a half-life of 6 months]] — Capturing traces across the full run so long-running agents can be debugged and improved.
  - Transcript: [[youtube-X1kp-ABIIxQ-transcript]]
  - Evidence: "So, the full session trace across your entire run is essential. So, if you can't see the entirety of a trace from the trigger through the whole stack, it's really hard to debug it, let alone improve your agent and keep evolving it."
- [[2026-06-30-geoffrey-litt-understanding-is-the-new-bottleneck|Understanding is the new bottleneck]] — A collaborative environment where humans and agents can reason about work together.
  - Transcript: [[youtube-WkBPX-oDMnA-transcript]]
  - Evidence: "Let's ask a different agent.\" And that agent comes in and talks to us. What's happening here is that instead of me and my PM both talking to our own agents, we're in a shared space, we can see each other's communication."
- [[2026-06-30-prukalpa-sankar-wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents|WTF Is the Context Layer? The Missing Infrastructure for Production Agents]] — The failure mode where agents learn separately and drift away from a single source of truth.
  - Transcript: [[youtube-8G_1-3IO4ZQ-transcript]]
  - Evidence: "Um and over time we started dealing with uh context sprawl. Uh we had the the the hard part about this was agents all had their own memory systems to a certain extent."
- [[2026-06-30-zhengyao-jiang-an-ai-agent-became-the-1-contributor-in-openai-s-hiring-challenge|An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge]] — An autonomous multi-agent system that runs experiments and submits research PRs after a quality gate.
  - Transcript: [[youtube-iCj_ATyThvc-transcript]]
  - Evidence: "Aiden is the next step and a experimental prototype. It's a multi-agent self-improving system that can read public information like research papers and other PRs, run its own experiments and submit a PR once the findings pass a quality gate."
- [[2026-07-01-alex-bauer-how-juries-and-librarians-can-solve-gtm-s-ai-trust-problem|How Juries and Librarians Can Solve GTM's AI Trust Problem]] — A pre-answer knowledge layer that gives agents company definitions, documentation, and failure history.
  - Transcript: [[youtube-YZQsWVeN3rE-transcript]]
  - Evidence: "So what we actually have it do is consult the librarian first. And the librarian has access to documentation and the library of knowledge items about your company and the schema of prior failed queries."
- [[2026-07-01-daniel-chalef-citation-needed-provenance-for-llm-built-knowledge-graphs|Citation Needed: Provenance for LLM-Built Knowledge Graphs]] — The need to preserve where synthesized facts came from in LLM-built knowledge graphs.
  - Transcript: [[youtube-H7puB0RwJMM-transcript]]
  - Evidence: "And I'm going to be talking today about provenence, which is tracing how an artifact was built and why."
- [[2026-07-01-emil-eifrem-thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer|Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer]] — Using observed agent runs to score outcomes and guide future decisions.
  - Transcript: [[youtube-VGN22pPpb-8-transcript]]
  - Evidence: "And then the third pillar is the runtime signals out of your agents. When they walk this graph and they execute, they leave the traces around what have I tried?"
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one|Video Has No Memory. Here's How We Built One.]] — The importance of temporal order and multimodal signals in making video meaningful.
  - Transcript: [[youtube-mOf-PP4mVjA-transcript]]
  - Evidence: "is useful approximation for some task but it throw away the thing that makes video very unique which is continuity right so meaning in video derives from space time modalities the sequence so a better mental for video is a spatial temporal volume."
- [[2026-07-01-mike-phipps-your-moat-is-your-data-model|Your Moat Is Your Data Model]] — A graph-based semantic layer that joins multiple systems of record into one traversable model.
  - Transcript: [[youtube-jt1Pbr_n6oU-transcript]]
  - Evidence: "So we're building a knowledge graph with the idea of the agent consumer and here is an endto-end look of what this looks like."
- [[2026-07-01-omri-bruchim-from-systems-of-record-to-systems-of-context|From Systems of Record to Systems of Context]] — The shift from storing records to building a live layer that explains how work is connected and why decisions were made.
  - Transcript: [[youtube-Btk8wDUVs74-transcript]]
  - Evidence: "What we want to talk today is like take it step further. Uh we want software that actually understand the connection between them."
- [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens|CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens]] — Graph-based representation of entities and relationships for connected data.
  - Transcript: [[youtube-Q0VkgCyNVUg-transcript]]
  - Evidence: "That's that's very unfortunate. So enter graphs. Graphs are a great way of finding the relationships, finding those identities, bu mapping out the paths, getting that full chain and they're built for this sort of connected data."
- [[2026-07-01-yohei-nakajima-active-graph-agent-runtime-babyagi-4|Active Graph Agent Runtime (BabyAGI 4)]] — Mechanisms for attaching reacting code to graph updates and letting it emit new events.
  - Transcript: [[youtube-khVX_BUnEwU-transcript]]
  - Evidence: "And then they emit events, which then in turn updates the state of the agent, which might trigger new behaviors."

## Connections
- [[2026-06-29-anders-swanson-from-context-to-memory-your-agents-need-a-real-memory-layer]] — From Context to Memory: Your Agents Need a Real Memory Layer; [[anders-swanson|Anders Swanson]] (Day 2 — Session Day 1 · 3:20pm-3:40pm · Expo Stage 2 NW; official schedule)
- [[2026-06-30-stefania-druga-memory-harnesses-for-long-running-research-agents]] — Memory Harnesses for Long-Running Research Agents; [[stefania-druga|Stefania Druga]] (Day 3 — Session Day 2 · 11:40am-12:00pm · Memory & Continual Learning; official schedule)
- [[2026-06-30-prukalpa-sankar-wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents]] — WTF Is the Context Layer? The Missing Infrastructure for Production Agents; [[prukalpa-sankar|Prukalpa Sankar]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Context Engineering; official schedule)
- [[2026-06-30-elizabeth-fuentes-leone-the-infinite-context-window-is-a-myth-context-engineering-for-ai-agents]] — The Infinite Context Window Is a Myth: Context Engineering for AI Agents; [[elizabeth-fuentes-leone|Elizabeth Fuentes Leone]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Expo Stage 3 SW; official schedule)
- [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens]] — CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens; [[stephen-chin|Stephen Chin]] (Day 4 — Session Day 3 · 10:45am-11:05am · Graphs; official schedule)
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one]] — Video Has No Memory. Here's How We Built One.; [[james-le|James Le]] (Day 4 — Session Day 3 · 2:25pm-2:45pm · Graphs; official schedule)
- [[2026-06-29-ignacio-martinez-total-recall-agent-memory-and-harness-engineering]] — Total Recall: Agent Memory and Harness Engineering; [[ignacio-martinez|Ignacio Martinez]] (Day 1 — Workshop Day · 9:00am-11:00am · Workshops Day 1; official schedule)
- [[2026-06-29-louis-fran-ois-bouchard-context-engineering-in-2026-compaction-memory-and-cost]] — Context Engineering in 2026: Compaction, Memory & Cost; [[louis-fran-ois-bouchard|Louis-François Bouchard]], [[samridhi-vaid|Samridhi Vaid]], [[omar-solano|Omar Solano]] (Day 1 — Workshop Day · 2:20pm-4:20pm · Track 6; official schedule)
- [[2026-06-30-anant-srivastava-prompt-memory-weights-the-architecture-decisions-most-ai-teams-make-by-accident]] — Prompt, Memory, Weights: The Architecture Decisions Most AI Teams Make by Accident; [[anant-srivastava|Anant Srivastava]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · Context Engineering; official schedule)
- [[2026-06-30-shlok-khemani-lessons-from-studying-every-memory-system]] — Lessons from Studying Every Memory System; [[shlok-khemani|Shlok Khemani]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Memory & Continual Learning; official schedule)
- [[2026-06-29-yoni-michael-the-data-context-layer-why-data-engineering-agents-need-more-than-code-and-databases]] — The Data Context Layer: Why Data Engineering Agents Need More Than Code and Databases; [[yoni-michael|Yoni Michael]], [[brandon-callender|Brandon Callender]] (Day 1 — Workshop Day · 2:20pm-4:20pm · Track 2; official schedule)
- [[2026-06-30-jack-morris-scaling-compute-on-context]] — Scaling Compute on Context; [[jack-morris|Jack Morris]] (Day 3 — Session Day 2 · 11:40am-12:00pm · Memory & Continual Learning; official schedule)
- [[2026-06-30-brandon-waselnuk-your-agents-lack-context-here-s-how-to-fix-you-re-absolutely-right]] — Your agents lack context: Here's how to fix "You're absolutely right!"; [[brandon-waselnuk|Brandon Waselnuk]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · Context Engineering; official schedule)
- [[2026-06-30-gil-feig-why-your-company-needs-a-context-graph-and-how-to-build-it]] — Why your company needs a context graph, and how to build it; [[gil-feig|Gil Feig]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Expo Stage 3; official schedule)
- [[2026-07-01-omri-bruchim-from-systems-of-record-to-systems-of-context]] — From Systems of Record to Systems of Context; [[omri-bruchim|Omri Bruchim]] (Day 4 — Session Day 3 · 12:05pm-12:25pm · Graphs; official schedule)
- [[2026-07-01-yuchen-fama-kv-cache-aware-routing-and-p-d-disaggregation-on-kubernetes-the-parts-public-benchmarks-don-t-show]] — KV Cache-Aware Routing and P/D Disaggregation on Kubernetes: The Parts Public Benchmarks Don't Show; [[yuchen-fama|Yuchen Fama]], [[ashish-kamra|Ashish Kamra]] (Day 4 — Session Day 3 · 2:50pm-3:10pm · Inference; official schedule)
- [[2026-06-30-rishab-kumar-from-stateless-to-stateful-orchestrating-real-time-voice-and-messaging-agents-with-twilio-and-amazon-bedrock]] — From Stateless to Stateful: Orchestrating Real-Time Voice & Messaging Agents with Twilio and Amazon Bedrock; [[rishab-kumar|Rishab Kumar]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · Expo Stage 2 NW; official schedule)
- [[2026-06-30-omer-primor-the-rise-of-caas-context-as-a-service-for-agentic-ai]] — The Rise of CaaS: Context-as-a-Service for Agentic AI; [[omer-primor|Omer Primor]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Computer Use; official schedule)
- [[2026-06-30-rachna-srivastava-guardians-of-the-state-how-we-built-an-air-gapped-ai-fortress-for-consumer-data]] — Guardians of the State: How We Built an Air-Gapped AI Fortress for Consumer Data; [[rachna-srivastava|Rachna Srivastava]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · AI-Native Enterprises; official schedule)
- [[2026-07-01-brandon-waselnuk-beyond-rag-see-a-relational-context-engine-reduce-token-burn]] — Beyond RAG: See a relational context engine reduce token burn; [[brandon-waselnuk|Brandon Waselnuk]] (Day 4 — Session Day 3 · 11:10am-11:30am · Expo Stage 1 NE; official schedule)
- [[2026-07-01-kay-malcolm-no-memory-no-harness-why-the-database-is-the-last-line-of-defense]] — No Memory, No Harness: Why the Database Is the Last Line of Defense; [[kay-malcolm|Kay Malcolm]] (Day 4 — Session Day 3 · 2:50pm-3:10pm · Harness Engineering; official schedule)
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]] — MCP Apps - Extending the frontier; [[liad-yosef|Liad Yosef]], [[ido-salomon|Ido Salomon]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Context Engineering; related YouTube resource; via [[youtube-o-zkvb0iFDQ]])
- [[2026-06-30-peter-werry-how-to-generate-mergeable-code-with-a-context-engine]] — How to generate mergeable code with a context engine; [[peter-werry|Peter Werry]] (Day 3 — Session Day 2 · 11:40am-12:00pm · Expo Stage 2 NW; official schedule)
- [[2026-06-29-krishna-prasad-srinivasan-from-scratch-to-sota-training-a-3b-state-space-vision-model-for-1-4-billion-people]] — From Scratch to SOTA: Training a 3B State-Space Vision Model for 1.4 Billion People; [[krishna-prasad-srinivasan|Krishna Prasad Srinivasan]] (Day 2 — Session Day 1 · 3:20pm-3:40pm · Vision & OCR; official schedule)

- [[john-lindquist|John Lindquist]]
- [[brandon-waselnuk|Brandon Waselnuk]]
- [[peter-werry|Peter Werry]]
- [[joseph-nelson|Joseph Nelson]]
- [[ahmad-osman|Ahmad Osman]]
- [[ido-salomon|Ido Salomon]]
- [[yuval-belfer|Yuval Belfer]]
- [[philipp-schmid|Philipp Schmid]]
- [[harshul-jain|Harshul Jain]]
- [[tanmay-sah|Tanmay Sah]]
- [[christopher-manning|Christopher Manning]]
- [[merve-noyan|Merve Noyan]]
- [[anders-swanson|Anders Swanson]]
- [[stefania-druga|Stefania Druga]]
- [[prukalpa-sankar|Prukalpa Sankar]]
- [[elizabeth-fuentes-leone|Elizabeth Fuentes Leone]]
- [[stephen-chin|Stephen Chin]]
- [[james-le|James Le]]
- [[ignacio-martinez|Ignacio Martinez]]
- [[louis-fran-ois-bouchard|Louis-François Bouchard]]
- [[samridhi-vaid|Samridhi Vaid]]
- [[omar-solano|Omar Solano]]
- [[anant-srivastava|Anant Srivastava]]
- [[shlok-khemani|Shlok Khemani]]

- [[together-ai|Together AI]]
- [[microsoft|Microsoft]]
- [[unblocked|Unblocked]]
- [[neo4j|Neo4j]]
- [[google|Google]]
- [[nvidia|NVIDIA]]
- [[openai|OpenAI]]
- [[oracle|Oracle]]
- [[towards-ai|Towards AI]]
- [[mcp-apps|MCP Apps]]
- [[ai21|AI21]]
- [[egghead-io|egghead.io]]
- [[anthropic|Anthropic]]
- [[google-deepmind|Google DeepMind]]
- [[typedef|typedef]]
- [[red-hat|Red Hat]]
- [[yugabyte|Yugabyte]]
- [[roboflow|Roboflow]]

- [[yoni-michael|Yoni Michael]]

- [[llamaindex|LlamaIndex]]

- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]] — MCP Apps - Extending the frontier; [[liad-yosef|Liad Yosef]], [[ido-salomon|Ido Salomon]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Context Engineering; related YouTube resource; via [[youtube-o-zkvb0iFDQ]])

- [[liad-yosef|Liad Yosef]]

- [[meta|Meta]]

- [[youtube-HEFSExa0xl0-slides]] — Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs (11 extracted slide frames)
- [[youtube-4kYl2_mqmnQ-slides]] — I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON (10 extracted slide frames)
- [[youtube-IQkVMvXQKLY-slides]] — Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis (14 extracted slide frames)
- [[youtube-UcYoMg-8-L8-slides]] — 500 people vibe-coded for 30 days. I was one of them. - Sanja Grbic, Automattic (11 extracted slide frames)
- [[youtube-kZsf_Sfm7RU-slides]] — The Missing Layer After Launch - Raphael Kalandadze, Wandero AI (19 extracted slide frames)
- [[youtube-2IxD9OB3XuQ-slides]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI (24 extracted slide frames)
- [[youtube-vljxQZfJ9wY-slides]] — Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs (12 extracted slide frames)

- [[2026-07-01-karthik-ranganathan-agent-memory-is-a-solved-problem-agent-learning-is-not]] — Agent Memory Is a Solved Problem. Agent Learning Is Not.; [[karthik-ranganathan|Karthik Ranganathan]], [[heather-downing|Heather Downing]] (Day 4 — Session Day 3 · 3:20pm-3:40pm · Expo Stage 1 NE; official schedule)

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 56 | Related pages outside the main evidence categories. |
| resources | 11 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 38 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 41 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 3 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 21 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-pablo-castro-on-ai-and-knowledge]]
- [[2026-06-29-sam-bhagwat-every-harness-will-become-a-claw]]
- [[2026-06-29-zach-blumenfeld-ai-on-your-lakehouse-context-comes-in-shapes-not-queries]]
- [[2026-06-30-addy-osmani-closing-keynote]]
- [[2026-06-30-dan-farrelly-your-agent-architecture-has-a-half-life-of-6-months]]
- [[2026-06-30-prukalpa-sankar-wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents]]

### Resources
- [[youtube-o-zkvb0iFDQ]]
- [[youtube-mOf-PP4mVjA]]
- [[youtube-H7puB0RwJMM]]
- [[youtube-I2cbIws9j10]]
- [[youtube-eBUyTS7SzV4]]
- [[youtube-4sX_He5c4sI]]

### Slides
- [[youtube-8G_1-3IO4ZQ-slides]]
- [[youtube-8qWIPUia2O8-slides]]
- [[youtube-Btk8wDUVs74-slides]]
- [[youtube-GgLQ02aO-hs-slides]]
- [[youtube-H7puB0RwJMM-slides]]
- [[youtube-il1c1a2FufU-slides]]

### Transcripts
- [[youtube-mOf-PP4mVjA-transcript]]
- [[youtube-H7puB0RwJMM-transcript]]
- [[youtube-I2cbIws9j10-transcript]]
- [[youtube-eBUyTS7SzV4-transcript]]
- [[youtube-4sX_He5c4sI-transcript]]
- [[youtube-vljxQZfJ9wY-transcript]]

### Tools
- [[neo4j]]
- [[mcp-apps]]
- [[llamaindex]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.

### Linked Sessions
- [[2026-06-29-anders-swanson-from-context-to-memory-your-agents-need-a-real-memory-layer|From Context to Memory: Your Agents Need a Real Memory Layer]]
- [[2026-06-30-stefania-druga-memory-harnesses-for-long-running-research-agents|Memory Harnesses for Long-Running Research Agents]]
- [[2026-06-30-prukalpa-sankar-wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents|WTF Is the Context Layer? The Missing Infrastructure for Production Agents]]
- [[2026-06-30-elizabeth-fuentes-leone-the-infinite-context-window-is-a-myth-context-engineering-for-ai-agents|'The Infinite Context Window Is a Myth: Context Engineering for AI Agents']]
- [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens|CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens]]
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one|Video Has No Memory. Here's How We Built One.]]
- [[2026-06-29-ignacio-martinez-total-recall-agent-memory-and-harness-engineering|Total Recall: Agent Memory and Harness Engineering]]
- [[2026-06-29-louis-fran-ois-bouchard-context-engineering-in-2026-compaction-memory-and-cost|Context Engineering in 2026: Compaction, Memory & Cost]]
- [[2026-06-30-anant-srivastava-prompt-memory-weights-the-architecture-decisions-most-ai-teams-make-by-accident|Prompt, Memory, Weights: The Architecture Decisions Most AI Teams Make by Accident]]
- [[2026-06-30-shlok-khemani-lessons-from-studying-every-memory-system|Lessons from Studying Every Memory System]]

### Media Signals
- `youtube-mOf-PP4mVjA` — 3,509 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-mOf-PP4mVjA`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-mOf-PP4mVjA`: memory, scene, content, system, across, layer, application, context.
- Slide-derived themes for `youtube-mOf-PP4mVjA`: memory, built, data, incredibly, complex, scale, holistic, understanding.
- Evidence links for `youtube-mOf-PP4mVjA` (primary event evidence): [[youtube-mOf-PP4mVjA]], [[youtube-mOf-PP4mVjA-transcript]], [[youtube-mOf-PP4mVjA-slides]]
- `youtube-H7puB0RwJMM` — 2,544 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-H7puB0RwJMM`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-H7puB0RwJMM`: fact, graph, data, source, graffiti, facts, provenence, sources.
- Slide-derived themes for `youtube-H7puB0RwJMM`: track, graphs, provenance, engineering, future, temporal, knowledge, built.
- Evidence links for `youtube-H7puB0RwJMM` (primary event evidence): [[youtube-H7puB0RwJMM]], [[youtube-H7puB0RwJMM-transcript]], [[youtube-H7puB0RwJMM-slides]]
- `youtube-I2cbIws9j10` — 91,792 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-I2cbIws9j10`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: choosing, model, quality, dominates, agentic, capabilities, customization, support.
- Evidence links for `youtube-I2cbIws9j10` (primary event evidence): [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
- `youtube-eBUyTS7SzV4` — 3,551 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-eBUyTS7SzV4`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-eBUyTS7SzV4`: company, open, companies, brain, code, three, does, person.
- Evidence links for `youtube-eBUyTS7SzV4` (primary event evidence): [[youtube-eBUyTS7SzV4]], [[youtube-eBUyTS7SzV4-transcript]]
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-4sX_He5c4sI`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: lots, examples, stream, starts, july, land, king, chief.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube-vljxQZfJ9wY` — 1,143 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-vljxQZfJ9wY`: evaluation, production, systems, most, model, tool, becomes, infrastructure.
- Slide-derived themes for `youtube-vljxQZfJ9wY`: accuracy, evaluation, output, behavior, workflow, tool, failure, volume.
- Evidence links for `youtube-vljxQZfJ9wY` (supporting context only): [[youtube-vljxQZfJ9wY]], [[youtube-vljxQZfJ9wY-transcript]], [[youtube-vljxQZfJ9wY-slides]]
- `youtube-T5IMo5ntyhA` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-T5IMo5ntyhA`: text, memory, description, financial, goal, type, target, amount.
- Evidence links for `youtube-T5IMo5ntyhA` (supporting context only): [[youtube-T5IMo5ntyhA]], [[youtube-T5IMo5ntyhA-slides]], [[youtube-T5IMo5ntyhA-dense-slides]], [[youtube-T5IMo5ntyhA-reconstructed-slides]]
- `youtube-Jty4s9-Jb78` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-Jty4s9-Jb78`: tokens, context, output, knowledge, given, user, second, blue.
- Evidence links for `youtube-Jty4s9-Jb78` (supporting context only): [[youtube-Jty4s9-Jb78]], [[youtube-Jty4s9-Jb78-slides]], [[youtube-Jty4s9-Jb78-dense-slides]], [[youtube-Jty4s9-Jb78-reconstructed-slides]]
- `youtube-ZRM_TfEZcIo` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-ZRM_TfEZcIo`: research, total, index, plus, notion, google, drive, growing.
- Evidence links for `youtube-ZRM_TfEZcIo` (supporting context only): [[youtube-ZRM_TfEZcIo]], [[youtube-ZRM_TfEZcIo-slides]], [[youtube-ZRM_TfEZcIo-dense-slides]], [[youtube-ZRM_TfEZcIo-reconstructed-slides]]
- `youtube-5ID22ACI7IM` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-5ID22ACI7IM`: context, callers, cover, today, remember, built, original, intent.
- Evidence links for `youtube-5ID22ACI7IM` (supporting context only): [[youtube-5ID22ACI7IM]], [[youtube-5ID22ACI7IM-slides]], [[youtube-5ID22ACI7IM-dense-slides]], [[youtube-5ID22ACI7IM-reconstructed-slides]]
