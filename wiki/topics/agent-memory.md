---
title: "Agent Memory"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---
# Agent Memory

## Overview
Agent memory is the set of mechanisms that lets an agent carry useful context across steps, sessions, users, repositories, documents, or decisions. It includes short-term working context, long-term stores, cached artifacts, decision traces, vector or graph retrieval, and policies that decide what should be remembered, refreshed, or forgotten.

## Conference Context
The topic comes from classic AI state management, knowledge representation, retrieval systems, personal assistants, and database-backed application design. The long-context era changed the tradeoff: teams can stuff more into prompts, but still need structured memory so agents can reason over the right facts at the right time.

## Significance
Memory determines whether an agent can act consistently instead of restarting from scratch. It improves personalization, reduces repeated work, supports multi-step workflows, and makes decisions auditable. Poor memory creates stale assumptions, privacy risk, context bloat, and confident mistakes.

## Applied Use
Separate working context from durable memory. Store source-backed facts, decisions, user preferences, and artifacts with timestamps and provenance. Retrieve by task intent, not just lexical similarity. Add policies for freshness, deletion, permissions, and summarization, and test memory behavior with scenario-based evals.

Memory is useful in coding agents, customer support, research assistants, enterprise knowledge agents, personal productivity tools, and any workflow that spans multiple sessions or documents.

Use durable memory when repeated interaction or long-horizon work matters. Avoid it for one-shot tasks, sensitive data without clear retention rules, or cases where stale state would be more harmful than asking again.

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
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]] — MCP Apps - Extending the frontier; [[liad-yosef|Liad Yosef]], [[ido-salomon|Ido Salomon]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Context Engineering; verified event YouTube resource; via [[youtube-o-zkvb0iFDQ]])
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

## Evidence Graph
This evidence graph consolidates scheduled talks, linked videos, transcripts, and slide-derived material connected to this topic.

### Linked Sessions
- [[2026-06-29-anders-swanson-from-context-to-memory-your-agents-need-a-real-memory-layer|From Context to Memory: Your Agents Need a Real Memory Layer]]
- [[2026-06-30-stefania-druga-memory-harnesses-for-long-running-research-agents|Memory Harnesses for Long-Running Research Agents]]
- [[2026-06-30-prukalpa-sankar-wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents|WTF Is the Context Layer? The Missing Infrastructure for Production Agents]]
- [[2026-06-30-elizabeth-fuentes-leone-the-infinite-context-window-is-a-myth-context-engineering-for-ai-agents|The Infinite Context Window Is a Myth: Context Engineering for AI Agents]]
- [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens|CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens]]
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one|Video Has No Memory. Here's How We Built One.]]
- [[2026-06-29-ignacio-martinez-total-recall-agent-memory-and-harness-engineering|Total Recall: Agent Memory and Harness Engineering]]
- [[2026-06-29-louis-fran-ois-bouchard-context-engineering-in-2026-compaction-memory-and-cost|Context Engineering in 2026: Compaction, Memory & Cost]]
- [[2026-06-30-anant-srivastava-prompt-memory-weights-the-architecture-decisions-most-ai-teams-make-by-accident|Prompt, Memory, Weights: The Architecture Decisions Most AI Teams Make by Accident]]
- [[2026-06-30-shlok-khemani-lessons-from-studying-every-memory-system|Lessons from Studying Every Memory System]]

### Media Signals
- `youtube-8G_1-3IO4ZQ` — 3,420 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-8G_1-3IO4ZQ`: context, team, started, learn, skills, company, question, systems.
- Slide-derived themes for `youtube-8G_1-3IO4ZQ`: context, layer, keep, companies, track, july, human, specialized.
- Evidence links for `youtube-8G_1-3IO4ZQ` (primary event evidence): [[youtube-8G_1-3IO4ZQ]], [[youtube-8G_1-3IO4ZQ-transcript]], [[youtube-8G_1-3IO4ZQ-slides]]
- `youtube-I2cbIws9j10` — 91,792 transcript words; 7 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: context, window, selects, response, facts, retry, coerce, rollback.
- Evidence links for `youtube-I2cbIws9j10` (primary event evidence): [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
- `youtube-o-zkvb0iFDQ` — 3,969 transcript words; role: primary event evidence.
- Transcript signals for `youtube-o-zkvb0iFDQ`: apps, host, claude, back, chatgpt, look, mcpui, chat.
- Evidence links for `youtube-o-zkvb0iFDQ` (primary event evidence): [[youtube-o-zkvb0iFDQ]], [[youtube-o-zkvb0iFDQ-transcript]], [[youtube-o-zkvb0iFDQ-slides]], [[youtube-o-zkvb0iFDQ-dense-slides]], [[youtube-o-zkvb0iFDQ-reconstructed-slides]]
- `youtube-n97BCfyFIvw` — 3,068 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-n97BCfyFIvw`: code, still, taste, loop, engineering, evidence, system, human.
- Slide-derived themes for `youtube-n97BCfyFIvw`: roles, google, look, across, worth, doing, increasingly, automated.
- Evidence links for `youtube-n97BCfyFIvw` (primary event evidence): [[youtube-n97BCfyFIvw]], [[youtube-n97BCfyFIvw-transcript]], [[youtube-n97BCfyFIvw-slides]]
- `youtube-0vphxNt4wyk` — 3,965 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-0vphxNt4wyk`: skill, skills, model, should, look, evals, eval, always.
- Slide-derived themes for `youtube-0vphxNt4wyk`: skills, fail, chad, vibe, checks, production, engineering, future.
- Evidence links for `youtube-0vphxNt4wyk` (primary event evidence): [[youtube-0vphxNt4wyk]], [[youtube-0vphxNt4wyk-transcript]], [[youtube-0vphxNt4wyk-slides]]
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: system, prompt, examples, tools, lots, claude, gets, smarter.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube-9fubhllmsBU` — 3,542 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-9fubhllmsBU`: claude, fable, code, give, models, prompt, model, little.
- Slide-derived themes for `youtube-9fubhllmsBU`: opening, land, king, models, grown, designed, fetch, write.
- Evidence links for `youtube-9fubhllmsBU` (primary event evidence): [[youtube-9fubhllmsBU]], [[youtube-9fubhllmsBU-transcript]], [[youtube-9fubhllmsBU-slides]]
- `youtube-htM02KMNZnk` — 89,050 transcript words; 4 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-htM02KMNZnk`: model, code, models, loop, well, software, first, team.
- Slide-derived themes for `youtube-htM02KMNZnk`: cycles, stacking, loops, tokens, tools, tasks, throughput, many.
- Evidence links for `youtube-htM02KMNZnk` (primary event evidence): [[youtube-htM02KMNZnk]], [[youtube-htM02KMNZnk-transcript]], [[youtube-htM02KMNZnk-slides]], [[youtube-htM02KMNZnk-dense-slides]], [[youtube-htM02KMNZnk-reconstructed-slides]]
- `youtube-vljxQZfJ9wY` — 1,143 transcript words; 8 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-vljxQZfJ9wY`: evaluation, production, systems, most, model, tool, becomes, infrastructure.
- Slide-derived themes for `youtube-vljxQZfJ9wY`: evaluation, reliability, accuracy, systems, behavior, measuring, beyond, autonomous.
- Evidence links for `youtube-vljxQZfJ9wY` (supporting context only): [[youtube-vljxQZfJ9wY]], [[youtube-vljxQZfJ9wY-transcript]], [[youtube-vljxQZfJ9wY-slides]]
- `youtube-T5IMo5ntyhA` — 9 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-T5IMo5ntyhA`: daniel, media, assistant, remembers, everything, except, listening, habits.
- Evidence links for `youtube-T5IMo5ntyhA` (supporting context only): [[youtube-T5IMo5ntyhA]], [[youtube-T5IMo5ntyhA-slides]], [[youtube-T5IMo5ntyhA-dense-slides]], [[youtube-T5IMo5ntyhA-reconstructed-slides]]
- `youtube-ZRM_TfEZcIo` — 9 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-ZRM_TfEZcIo`: obsidian, google, plus, notion, drive, growing, files, month.
- Evidence links for `youtube-ZRM_TfEZcIo` (supporting context only): [[youtube-ZRM_TfEZcIo]], [[youtube-ZRM_TfEZcIo-slides]], [[youtube-ZRM_TfEZcIo-dense-slides]], [[youtube-ZRM_TfEZcIo-reconstructed-slides]]
- `youtube-Jty4s9-Jb78` — source page linked; role: supporting context only.
- Evidence links for `youtube-Jty4s9-Jb78` (supporting context only): [[youtube-Jty4s9-Jb78]], [[youtube-Jty4s9-Jb78-slides]], [[youtube-Jty4s9-Jb78-dense-slides]], [[youtube-Jty4s9-Jb78-reconstructed-slides]]
- `youtube-TUnPNY4E2fw` — 2,091 transcript words; 5 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-TUnPNY4E2fw`: context, memory, model, training, million, quite, attention, sequence.
- Slide-derived themes for `youtube-TUnPNY4E2fw`: engineering, future, training, memory, usage.
- Evidence links for `youtube-TUnPNY4E2fw` (supporting context only): [[youtube-TUnPNY4E2fw]], [[youtube-TUnPNY4E2fw-transcript]], [[youtube-TUnPNY4E2fw-slides]]
- `youtube-5ID22ACI7IM` — 4 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-5ID22ACI7IM`: connect, code, logs, docs, tickets, gives, plausible, output.
- Evidence links for `youtube-5ID22ACI7IM` (supporting context only): [[youtube-5ID22ACI7IM]], [[youtube-5ID22ACI7IM-slides]], [[youtube-5ID22ACI7IM-dense-slides]], [[youtube-5ID22ACI7IM-reconstructed-slides]]

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 56 | Related pages outside the main evidence categories. |
| resources | 14 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 35 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 26 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 3 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 10 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-anders-swanson-from-context-to-memory-your-agents-need-a-real-memory-layer]]
- [[2026-06-30-stefania-druga-memory-harnesses-for-long-running-research-agents]]
- [[2026-06-30-prukalpa-sankar-wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents]]
- [[2026-06-30-elizabeth-fuentes-leone-the-infinite-context-window-is-a-myth-context-engineering-for-ai-agents]]
- [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens]]
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one]]

### Resources
- [[youtube-o-zkvb0iFDQ]]
- [[youtube-8G_1-3IO4ZQ]]
- [[youtube-I2cbIws9j10]]
- [[youtube-n97BCfyFIvw]]
- [[youtube-0vphxNt4wyk]]
- [[youtube-4sX_He5c4sI]]

### Slides
- [[youtube-HEFSExa0xl0-slides]]
- [[youtube-4kYl2_mqmnQ-slides]]
- [[youtube-IQkVMvXQKLY-slides]]
- [[youtube-UcYoMg-8-L8-slides]]
- [[youtube-kZsf_Sfm7RU-slides]]
- [[youtube-2IxD9OB3XuQ-slides]]

### Transcripts
- [[youtube-8G_1-3IO4ZQ-transcript]]
- [[youtube-I2cbIws9j10-transcript]]
- [[youtube-o-zkvb0iFDQ-transcript]]
- [[youtube-n97BCfyFIvw-transcript]]
- [[youtube-0vphxNt4wyk-transcript]]
- [[youtube-4sX_He5c4sI-transcript]]

### Tools
- [[neo4j]]
- [[mcp-apps]]
- [[llamaindex]]

## Active Use Cases
- Remembering repository architecture and prior implementation decisions.
- Maintaining user preferences and project constraints across sessions.
- Decision-trace retrieval for enterprise workflows.
- Long-context cache and knowledge-graph backed agent workflows.

## Slide-Derived Supporting Decks
- [[youtube-8G_1-3IO4ZQ-slides]] —  (10 extracted slide frames)
- [[youtube-n97BCfyFIvw-slides]] — "The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani (32 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

## Slide-Derived Scheduled Session Signals
- [[2026-06-30-addy-osmani-closing-keynote]] — Closing Keynote
