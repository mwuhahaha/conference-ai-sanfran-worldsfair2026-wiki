---
title: "Agentic Search"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---
# Agentic Search

## Overview
Agentic search is retrieval where an AI system actively plans, queries, follows leads, compares sources, and decides when it has enough evidence. It goes beyond one-shot RAG by treating search as an iterative reasoning and tool-use process.

## Conference Context
It combines web search, enterprise search, information retrieval, RAG, semantic search, BM25, vector databases, knowledge graphs, and research-agent workflows. Agents add query reformulation, source triage, multi-hop exploration, and evidence synthesis.

## Significance
Many tasks fail because the agent either retrieves the wrong context or stops too early. Agentic search improves coverage, reduces hallucination, and helps systems expose the evidence behind an answer.

## Applied Use
Define the question, retrieve broadly, rerank by task relevance, inspect primary sources, track claims and citations, and loop when evidence conflicts or gaps remain. Use hybrid retrieval and structured indexes where pure vector search misses exact terms or relationships.

It is useful in research, support knowledge bases, compliance review, code search, enterprise assistants, competitive intelligence, and document-heavy operations.

Use agentic search when answers require multiple sources, fresh evidence, exact facts, or cross-document reasoning. Simple lookup or direct database queries are better for narrow deterministic questions.

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

## Evidence Graph
This evidence graph consolidates scheduled talks, linked videos, transcripts, and slide-derived material connected to this topic.

### Linked Sessions
- [[2026-07-01-session-vector-isn-t-enough-hybrid-search-and-retrieval-for-ai-engineers|Vector Isn't Enough: Hybrid Search & Retrieval for AI Engineers]]
- [[2026-06-29-jo-kristian-bergum-the-unreasonable-effectiveness-of-bm25-for-agentic-search|The unreasonable effectiveness of BM25 for agentic search]]
- [[2026-06-29-will-bryk-the-search-engine-for-the-agentic-web|The Search Engine for the Agentic Web]]
- [[2026-06-29-maximilian-david-rumpf-where-rl-will-take-search|Where RL Will Take Search]]
- [[2026-06-30-han-xiao-autoresearch-for-dense-retrieval-test-time-compute-with-frozen-embedding-models|Autoresearch for Dense Retrieval: Test-Time Compute with Frozen Embedding Models]]
- [[2026-06-30-elie-bakouch-the-era-of-auto-research|« the era of (auto) research »]]
- [[2026-06-30-tim-sweeney-closing-the-loop-an-autonomous-ai-research-agent|Closing the Loop: An Autonomous AI Research Agent]]
- [[2026-06-29-dhruv-nathawani-teaching-agents-to-search-building-synthetic-training-pipelines-with-nvidia-data-designer|Teaching Agents to Search: Building Synthetic Training Pipelines with NVIDIA Data Designer]]
- [[2026-06-30-erina-karati-autoresearch-in-a-multi-agent-ai-village|Autoresearch in a Multi-Agent AI Village]]
- [[2026-07-01-stephen-chin-crabrag-why-automated-assistants-need-graph-memory-not-more-tokens|CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens]]

### Media Signals
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: system, prompt, examples, tools, lots, claude, gets, smarter.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube--CnA2lGfymY` — 3,148 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube--CnA2lGfymY`: answer, lean, safe, model, type, look, llms, question.
- Slide-derived themes for `youtube--CnA2lGfymY`: someone, credible, fair, conviction, sara, made, serious, error.
- Evidence links for `youtube--CnA2lGfymY` (primary event evidence): [[youtube--CnA2lGfymY]], [[youtube--CnA2lGfymY-transcript]], [[youtube--CnA2lGfymY-slides]]
- `youtube-n97BCfyFIvw` — 3,068 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-n97BCfyFIvw`: code, still, taste, loop, engineering, evidence, system, human.
- Slide-derived themes for `youtube-n97BCfyFIvw`: roles, google, look, across, worth, doing, increasingly, automated.
- Evidence links for `youtube-n97BCfyFIvw` (primary event evidence): [[youtube-n97BCfyFIvw]], [[youtube-n97BCfyFIvw-transcript]], [[youtube-n97BCfyFIvw-slides]]
- `youtube-pMggiOb18tc` — 4,606 transcript words; role: primary event evidence.
- Transcript signals for `youtube-pMggiOb18tc`: models, codex, open, model, should, engineering, well, even.
- Evidence links for `youtube-pMggiOb18tc` (primary event evidence): [[youtube-pMggiOb18tc]], [[youtube-pMggiOb18tc-transcript]]
- `youtube-uIiA6DquRiE` — source page linked; role: primary event evidence.
- Evidence links for `youtube-uIiA6DquRiE` (primary event evidence): [[youtube-uIiA6DquRiE]]
- `youtube-htM02KMNZnk` — 89,050 transcript words; 4 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-htM02KMNZnk`: model, code, models, loop, well, software, first, team.
- Slide-derived themes for `youtube-htM02KMNZnk`: cycles, stacking, loops, tokens, tools, tasks, throughput, many.
- Evidence links for `youtube-htM02KMNZnk` (primary event evidence): [[youtube-htM02KMNZnk]], [[youtube-htM02KMNZnk-transcript]], [[youtube-htM02KMNZnk-slides]], [[youtube-htM02KMNZnk-dense-slides]], [[youtube-htM02KMNZnk-reconstructed-slides]]
- `youtube-q4Tr-DknG2M` — 4,039 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-q4Tr-DknG2M`: models, model, training, evals, pretty, loop, compute, cursor.
- Slide-derived themes for `youtube-q4Tr-DknG2M`: future, cursor, compute, better, model, anon, pease, days.
- Evidence links for `youtube-q4Tr-DknG2M` (primary event evidence): [[youtube-q4Tr-DknG2M]], [[youtube-q4Tr-DknG2M-transcript]], [[youtube-q4Tr-DknG2M-slides]]
- `youtube-o-zkvb0iFDQ` — 3,969 transcript words; role: primary event evidence.
- Transcript signals for `youtube-o-zkvb0iFDQ`: apps, host, claude, back, chatgpt, look, mcpui, chat.
- Evidence links for `youtube-o-zkvb0iFDQ` (primary event evidence): [[youtube-o-zkvb0iFDQ]], [[youtube-o-zkvb0iFDQ-transcript]], [[youtube-o-zkvb0iFDQ-slides]], [[youtube-o-zkvb0iFDQ-dense-slides]], [[youtube-o-zkvb0iFDQ-reconstructed-slides]]
- `youtube-I2cbIws9j10` — 91,792 transcript words; 7 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: context, window, selects, response, facts, retry, coerce, rollback.
- Evidence links for `youtube-I2cbIws9j10` (primary event evidence): [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
- `youtube-RGSFUqzqErE` — source page linked; role: primary event evidence.
- Evidence links for `youtube-RGSFUqzqErE` (primary event evidence): [[youtube-RGSFUqzqErE]]
- `youtube-APqXGyCoGW4` — 3,956 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-APqXGyCoGW4`: team, customers, doing, hire, cursor, product, folks, help.
- Slide-derived themes for `youtube-APqXGyCoGW4`: engineering, team, forward, deployed, microsoft, future, does, mean.
- Evidence links for `youtube-APqXGyCoGW4` (primary event evidence): [[youtube-APqXGyCoGW4]], [[youtube-APqXGyCoGW4-transcript]], [[youtube-APqXGyCoGW4-slides]]
- `youtube-V-EDrhIhHzQ` — 10,228 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-V-EDrhIhHzQ`: model, harness, well, doing, environment, training, able, models.
- Slide-derived themes for `youtube-V-EDrhIhHzQ`: engineering, future, prime, intellect, stack, open.
- Evidence links for `youtube-V-EDrhIhHzQ` (primary event evidence): [[youtube-V-EDrhIhHzQ]], [[youtube-V-EDrhIhHzQ-transcript]], [[youtube-V-EDrhIhHzQ-slides]]
- `youtube-ZpK5PWX2YRM` — 3,931 transcript words; role: primary event evidence.
- Transcript signals for `youtube-ZpK5PWX2YRM`: code, okay, read, line, guys, still, loops, engineer.
- Evidence links for `youtube-ZpK5PWX2YRM` (primary event evidence): [[youtube-ZpK5PWX2YRM]], [[youtube-ZpK5PWX2YRM-transcript]]
- `youtube-ZSQb5fzRFPw` — 2,617 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-ZSQb5fzRFPw`: computer, take, over, driver, background, task, might, sandbox.
- Slide-derived themes for `youtube-ZSQb5fzRFPw`: track, july, fair, computer, operator, loop, wired, model.
- Evidence links for `youtube-ZSQb5fzRFPw` (primary event evidence): [[youtube-ZSQb5fzRFPw]], [[youtube-ZSQb5fzRFPw-transcript]], [[youtube-ZSQb5fzRFPw-slides]]
- `youtube-WkBPX-oDMnA` — 3,765 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-WkBPX-oDMnA`: code, understand, understanding, point, notion, okay, take, question.
- Slide-derived themes for `youtube-WkBPX-oDMnA`: track, july, understand, important, humans, tools, better, than.
- Evidence links for `youtube-WkBPX-oDMnA` (primary event evidence): [[youtube-WkBPX-oDMnA]], [[youtube-WkBPX-oDMnA-transcript]], [[youtube-WkBPX-oDMnA-slides]]
- `youtube-sRpqPgKeXNk` — 7 slide-derived text signals; role: primary event evidence.
- Slide-derived themes for `youtube-sRpqPgKeXNk`: reasoning, tokens, models, analysis, index, model, output, intelligence.
- Evidence links for `youtube-sRpqPgKeXNk` (primary event evidence): [[youtube-sRpqPgKeXNk]], [[youtube-sRpqPgKeXNk-slides]], [[youtube-sRpqPgKeXNk-dense-slides]], [[youtube-sRpqPgKeXNk-reconstructed-slides]]
- `youtube-0vphxNt4wyk` — 3,965 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-0vphxNt4wyk`: skill, skills, model, should, look, evals, eval, always.
- Slide-derived themes for `youtube-0vphxNt4wyk`: skills, fail, chad, vibe, checks, production, engineering, future.
- Evidence links for `youtube-0vphxNt4wyk` (primary event evidence): [[youtube-0vphxNt4wyk]], [[youtube-0vphxNt4wyk-transcript]], [[youtube-0vphxNt4wyk-slides]]
- `youtube-8G_1-3IO4ZQ` — 3,420 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-8G_1-3IO4ZQ`: context, team, started, learn, skills, company, question, systems.
- Slide-derived themes for `youtube-8G_1-3IO4ZQ`: context, layer, keep, companies, track, july, human, specialized.
- Evidence links for `youtube-8G_1-3IO4ZQ` (primary event evidence): [[youtube-8G_1-3IO4ZQ]], [[youtube-8G_1-3IO4ZQ-transcript]], [[youtube-8G_1-3IO4ZQ-slides]]
- `youtube-YZQsWVeN3rE` — 2,901 transcript words; 3 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-YZQsWVeN3rE`: product, first, data, important, back, team, go-to-market, give.
- Slide-derived themes for `youtube-YZQsWVeN3rE`: juries, librarians, solve, trust, problem, alex, bauer, upside.
- Evidence links for `youtube-YZQsWVeN3rE` (primary event evidence): [[youtube-YZQsWVeN3rE]], [[youtube-YZQsWVeN3rE-transcript]], [[youtube-YZQsWVeN3rE-slides]]
- `youtube-KB41dTlX1Uc` — 9,219 transcript words; role: primary event evidence.
- Transcript signals for `youtube-KB41dTlX1Uc`: models, model, local, open, source, data, specialized, hardware.
- Evidence links for `youtube-KB41dTlX1Uc` (primary event evidence): [[youtube-KB41dTlX1Uc]], [[youtube-KB41dTlX1Uc-transcript]], [[youtube-KB41dTlX1Uc-slides]]
- `youtube-9fubhllmsBU` — 3,542 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-9fubhllmsBU`: claude, fable, code, give, models, prompt, model, little.
- Slide-derived themes for `youtube-9fubhllmsBU`: opening, land, king, models, grown, designed, fetch, write.
- Evidence links for `youtube-9fubhllmsBU` (primary event evidence): [[youtube-9fubhllmsBU]], [[youtube-9fubhllmsBU-transcript]], [[youtube-9fubhllmsBU-slides]]
- `youtube-knDDGYHnnSI` — 3 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-knDDGYHnnSI`: evolution, search, floor, plans, north, directions, bart, offers.
- Evidence links for `youtube-knDDGYHnnSI` (supporting context only): [[youtube-knDDGYHnnSI]], [[youtube-knDDGYHnnSI-slides]], [[youtube-knDDGYHnnSI-dense-slides]], [[youtube-knDDGYHnnSI-reconstructed-slides]]
- `youtube-zKk7sDMGDEQ` — 3,298 transcript words; 8 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-zKk7sDMGDEQ`: code, search, semantic, grep, file, files, cloud, puffer.
- Slide-derived themes for `youtube-zKk7sDMGDEQ`: claude, search, code, quickly, semantic, does, anyone, codex.
- Evidence links for `youtube-zKk7sDMGDEQ` (supporting context only): [[youtube-zKk7sDMGDEQ]], [[youtube-zKk7sDMGDEQ-transcript]], [[youtube-zKk7sDMGDEQ-slides]]
- `youtube-btxGmN8RvNU` — 2,716 transcript words; role: supporting context only.
- Transcript signals for `youtube-btxGmN8RvNU`: data, literally, search, doesn, product, access, without, tools.
- Evidence links for `youtube-btxGmN8RvNU` (supporting context only): [[youtube-btxGmN8RvNU]], [[youtube-btxGmN8RvNU-transcript]], [[youtube-btxGmN8RvNU-slides]]
- `youtube-2vlCqD6igVA` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-2vlCqD6igVA`: search, query, latte, enriching, exploratory, queries, extract, catalog.
- Evidence links for `youtube-2vlCqD6igVA` (supporting context only): [[youtube-2vlCqD6igVA]], [[youtube-2vlCqD6igVA-slides]], [[youtube-2vlCqD6igVA-reconstructed-slides]]
- `youtube-Akm1sqvWG4A` — 6,285 transcript words; 4 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-Akm1sqvWG4A`: information, upload, chunk, based, another, documents, chatbot, well.
- Slide-derived themes for `youtube-Akm1sqvWG4A`: hybrid, live, telemetry, senior, developer, ogilvy, problems, document.
- Evidence links for `youtube-Akm1sqvWG4A` (supporting context only): [[youtube-Akm1sqvWG4A]], [[youtube-Akm1sqvWG4A-transcript]], [[youtube-Akm1sqvWG4A-slides]]
- `youtube-1IdzkRVmWAA` — 6,138 transcript words; role: supporting context only.
- Transcript signals for `youtube-1IdzkRVmWAA`: search, query, tools, queries, tool, retrieval, semantic, chunks.
- Evidence links for `youtube-1IdzkRVmWAA` (supporting context only): [[youtube-1IdzkRVmWAA]], [[youtube-1IdzkRVmWAA-transcript]], [[youtube-1IdzkRVmWAA-slides]]
- `youtube-UM6sFg_jdlE` — 2,187 transcript words; 6 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-UM6sFg_jdlE`: search, code, turbo, puffer, cloud, vector, agentic, essentially.
- Slide-derived themes for `youtube-UM6sFg_jdlE`: retrieval, hybrid, becoming, default, serious, agentic, search, april.
- Evidence links for `youtube-UM6sFg_jdlE` (supporting context only): [[youtube-UM6sFg_jdlE]], [[youtube-UM6sFg_jdlE-transcript]], [[youtube-UM6sFg_jdlE-slides]]
- `youtube-Jx4ZFEAq6bY` — 1,867 transcript words; 7 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-Jx4ZFEAq6bY`: memory, retrieval, system, product, task, does, most, mouse.
- Slide-derived themes for `youtube-Jx4ZFEAq6bY`: user, signal, dies, memory, missing, layer, runs, system.
- Evidence links for `youtube-Jx4ZFEAq6bY` (supporting context only): [[youtube-Jx4ZFEAq6bY]], [[youtube-Jx4ZFEAq6bY-transcript]], [[youtube-Jx4ZFEAq6bY-slides]]

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 50 | Related pages outside the main evidence categories. |
| resources | 29 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 43 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 26 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 5 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 24 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-07-01-session-vector-isn-t-enough-hybrid-search-and-retrieval-for-ai-engineers]]
- [[2026-06-29-jo-kristian-bergum-the-unreasonable-effectiveness-of-bm25-for-agentic-search]]
- [[2026-06-29-will-bryk-the-search-engine-for-the-agentic-web]]
- [[2026-06-29-maximilian-david-rumpf-where-rl-will-take-search]]
- [[2026-06-30-han-xiao-autoresearch-for-dense-retrieval-test-time-compute-with-frozen-embedding-models]]
- [[2026-06-30-elie-bakouch-the-era-of-auto-research]]

### Resources
- [[youtube-4sX_He5c4sI]]
- [[youtube--CnA2lGfymY]]
- [[youtube-n97BCfyFIvw]]
- [[youtube-pMggiOb18tc]]
- [[youtube-uIiA6DquRiE]]
- [[youtube-htM02KMNZnk]]

### Slides
- [[youtube-HsxQICTLF84-slides]]
- [[youtube-IQkVMvXQKLY-slides]]
- [[youtube-1IdzkRVmWAA-slides]]
- [[youtube-2e9ANoOEn28-slides]]
- [[youtube-CLttOU7n6sI-slides]]
- [[youtube-UcYoMg-8-L8-slides]]

### Transcripts
- [[youtube-4sX_He5c4sI-transcript]]
- [[youtube--CnA2lGfymY-transcript]]
- [[youtube-n97BCfyFIvw-transcript]]
- [[youtube-pMggiOb18tc-transcript]]
- [[youtube-htM02KMNZnk-transcript]]
- [[youtube-q4Tr-DknG2M-transcript]]

### Tools
- [[neo4j]]
- [[exa]]
- [[llamaindex]]
- [[prime-intellect]]
- [[browserbase]]

## Active Use Cases
- Research agents that cite and compare sources.
- Hybrid RAG over documents, SQL, UI telemetry, and web data.
- Semantic code retrieval for coding agents.
- Enterprise knowledge agents with source-grounded answers.

## Slide-Derived Supporting Decks
- [[youtube--CnA2lGfymY-slides]] — "I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox (32 extracted slide frames)
- [[youtube-n97BCfyFIvw-slides]] — "The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani (32 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

## Slide-Derived Scheduled Session Signals
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]] — In Code They Act, In Proof We Trust
- [[2026-06-30-addy-osmani-closing-keynote]] — Closing Keynote
