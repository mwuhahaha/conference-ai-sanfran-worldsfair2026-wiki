---
title: "Coding Agents"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---
# Coding Agents

## Overview
Coding agents are AI systems that can inspect repositories, reason about requirements, edit files, run commands, test changes, and sometimes open pull requests or operate development tools. They move AI coding from autocomplete toward task execution.

## Conference Context
They evolved from code completion, IDE assistants, program synthesis, CI automation, and software bots. The recent shift is tool use: agents can read context, make coordinated edits, run tests, and respond to feedback inside real development workflows.

## Significance
Software work is full of local context, repetitive edits, dependency checks, and validation loops. Coding agents can compress that cycle, but only when they respect repository conventions, tests, review standards, and operational safety.

## Applied Use
Give the agent a narrow task, repository context, tests or acceptance criteria, and permission boundaries. Require it to read before editing, keep diffs scoped, run validation, report residual risk, and leave the workspace clean.

They are useful in feature slices, bug fixes, test generation, refactors, migrations, docs updates, dependency audits, and operational scripts.

Use coding agents when the task has clear acceptance criteria and the repo has enough structure to validate changes. Keep humans in the loop for architecture decisions, risky production operations, and ambiguous product calls.

## Connections
- [[2026-06-29-will-bond-scaling-code-quality-building-ureview-uber-s-multi-agent-code-review-engine]] — Scaling Code Quality: Building uReview, Uber’s Multi-Agent Code Review Engine; [[will-bond|Will Bond]], [[ameya-ketkar|Ameya Ketkar]] (Day 2 — Session Day 1 · 12:05pm-12:25pm · AI-Native Enterprises; official schedule)
- [[2026-06-29-owen-halpert-give-your-coding-agents-the-power-of-turbogrep]] — Give your coding agents the power of turbogrep!; [[owen-halpert|Owen Halpert]] (Day 2 — Session Day 1 · 11:10am-11:30am · Expo Stage 1 NE; official schedule)
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one]] — Video Has No Memory. Here's How We Built One.; [[james-le|James Le]] (Day 4 — Session Day 3 · 2:25pm-2:45pm · Graphs; official schedule)
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]] — The Golden Age of AI Engineering; [[alexander-embiricos|Alexander Embiricos]], [[romain-huet|Romain Huet]] (Day 2 — Session Day 1 · 9:25am-9:45am · Software Factories; verified event YouTube resource; via [[youtube-pMggiOb18tc]])
- [[2026-07-01-anirban-chatterjee-guide-verify-solve-the-engineering-discipline-agentic-development-demands]] — Guide, Verify, Solve: The Engineering Discipline Agentic Development Demands; [[anirban-chatterjee|Anirban Chatterjee]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Agentic Engineering; official schedule)
- [[2026-06-29-nnenna-ndukwe-how-to-build-quality-gates-into-agentic-coding-workflows]] — How to Build Quality Gates into Agentic Coding Workflows; [[nnenna-ndukwe|Nnenna Ndukwe]] (Day 1 — Workshop Day · 11:05am-12:05pm · Workshops Day 1; official schedule)
- [[2026-06-29-itamar-friedman-the-last-human-code-review-building-trust-in-ai-generated-code]] — The Last Human Code Review: Building Trust in AI-Generated Code; [[itamar-friedman|Itamar Friedman]] (Day 2 — Session Day 1 · 11:40am-12:00pm · AI Architects: Show my Workflow; official schedule)
- [[2026-06-30-laurie-voss-the-death-of-the-code-review]] — The Death of the Code Review; [[laurie-voss|Laurie Voss]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · AI Architects: Tokenmaxxing; official schedule)
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]] — MCP Apps - Extending the frontier; [[liad-yosef|Liad Yosef]], [[ido-salomon|Ido Salomon]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Context Engineering; verified event YouTube resource; via [[youtube-o-zkvb0iFDQ]])
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

## Evidence Graph
This evidence graph consolidates scheduled talks, linked videos, transcripts, and slide-derived material connected to this topic.

### Linked Sessions
- [[2026-06-29-will-bond-scaling-code-quality-building-ureview-uber-s-multi-agent-code-review-engine|Scaling Code Quality: Building uReview, Uber’s Multi-Agent Code Review Engine]]
- [[2026-06-29-owen-halpert-give-your-coding-agents-the-power-of-turbogrep|Give your coding agents the power of turbogrep!]]
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one|Video Has No Memory. Here's How We Built One.]]
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering|The Golden Age of AI Engineering]]
- [[2026-07-01-anirban-chatterjee-guide-verify-solve-the-engineering-discipline-agentic-development-demands|Guide, Verify, Solve: The Engineering Discipline Agentic Development Demands]]
- [[2026-06-29-nnenna-ndukwe-how-to-build-quality-gates-into-agentic-coding-workflows|How to Build Quality Gates into Agentic Coding Workflows]]
- [[2026-06-29-itamar-friedman-the-last-human-code-review-building-trust-in-ai-generated-code|The Last Human Code Review: Building Trust in AI-Generated Code]]
- [[2026-06-30-laurie-voss-the-death-of-the-code-review|The Death of the Code Review]]
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier|MCP Apps - Extending the frontier]]
- [[2026-06-29-eyal-blum-how-to-get-your-org-to-adopt-coding-agents-without-shipping-garbage|How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage)]]

### Media Signals
- `youtube-pMggiOb18tc` — 4,606 transcript words; role: primary event evidence.
- Transcript signals for `youtube-pMggiOb18tc`: models, codex, open, model, should, engineering, well, even.
- Evidence links for `youtube-pMggiOb18tc` (primary event evidence): [[youtube-pMggiOb18tc]], [[youtube-pMggiOb18tc-transcript]]
- `youtube-o-zkvb0iFDQ` — 3,969 transcript words; role: primary event evidence.
- Transcript signals for `youtube-o-zkvb0iFDQ`: apps, host, claude, back, chatgpt, look, mcpui, chat.
- Evidence links for `youtube-o-zkvb0iFDQ` (primary event evidence): [[youtube-o-zkvb0iFDQ]], [[youtube-o-zkvb0iFDQ-transcript]], [[youtube-o-zkvb0iFDQ-slides]], [[youtube-o-zkvb0iFDQ-dense-slides]], [[youtube-o-zkvb0iFDQ-reconstructed-slides]]
- `youtube-ZpK5PWX2YRM` — 3,931 transcript words; role: primary event evidence.
- Transcript signals for `youtube-ZpK5PWX2YRM`: code, okay, read, line, guys, still, loops, engineer.
- Evidence links for `youtube-ZpK5PWX2YRM` (primary event evidence): [[youtube-ZpK5PWX2YRM]], [[youtube-ZpK5PWX2YRM-transcript]]
- `youtube--CnA2lGfymY` — 3,148 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube--CnA2lGfymY`: answer, lean, safe, model, type, look, llms, question.
- Slide-derived themes for `youtube--CnA2lGfymY`: someone, credible, fair, conviction, sara, made, serious, error.
- Evidence links for `youtube--CnA2lGfymY` (primary event evidence): [[youtube--CnA2lGfymY]], [[youtube--CnA2lGfymY-transcript]], [[youtube--CnA2lGfymY-slides]]
- `youtube-n97BCfyFIvw` — 3,068 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-n97BCfyFIvw`: code, still, taste, loop, engineering, evidence, system, human.
- Slide-derived themes for `youtube-n97BCfyFIvw`: roles, google, look, across, worth, doing, increasingly, automated.
- Evidence links for `youtube-n97BCfyFIvw` (primary event evidence): [[youtube-n97BCfyFIvw]], [[youtube-n97BCfyFIvw-transcript]], [[youtube-n97BCfyFIvw-slides]]
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
- `youtube-OqM67QG_Ikk` — source page linked; role: primary event evidence.
- Evidence links for `youtube-OqM67QG_Ikk` (primary event evidence): [[youtube-OqM67QG_Ikk]]
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: system, prompt, examples, tools, lots, claude, gets, smarter.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube-ZSQb5fzRFPw` — 2,617 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-ZSQb5fzRFPw`: computer, take, over, driver, background, task, might, sandbox.
- Slide-derived themes for `youtube-ZSQb5fzRFPw`: track, july, fair, computer, operator, loop, wired, model.
- Evidence links for `youtube-ZSQb5fzRFPw` (primary event evidence): [[youtube-ZSQb5fzRFPw]], [[youtube-ZSQb5fzRFPw-transcript]], [[youtube-ZSQb5fzRFPw-slides]]
- `youtube-WkBPX-oDMnA` — 3,765 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Transcript signals for `youtube-WkBPX-oDMnA`: code, understand, understanding, point, notion, okay, take, question.
- Slide-derived themes for `youtube-WkBPX-oDMnA`: track, july, understand, important, humans, tools, better, than.
- Evidence links for `youtube-WkBPX-oDMnA` (primary event evidence): [[youtube-WkBPX-oDMnA]], [[youtube-WkBPX-oDMnA-transcript]], [[youtube-WkBPX-oDMnA-slides]]
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
- `youtube-7Dtu2bilcFs` — 9 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-7Dtu2bilcFs`: coding, agentic, final, form, coming, next, stop, models.
- Evidence links for `youtube-7Dtu2bilcFs` (supporting context only): [[youtube-7Dtu2bilcFs]], [[youtube-7Dtu2bilcFs-slides]], [[youtube-7Dtu2bilcFs-dense-slides]], [[youtube-7Dtu2bilcFs-reconstructed-slides]]
- `youtube-bVNNvWq6dKo` — 4 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-bVNNvWq6dKo`: agentic, diff, review, first, company, replace, chat, deep.
- Evidence links for `youtube-bVNNvWq6dKo` (supporting context only): [[youtube-bVNNvWq6dKo]], [[youtube-bVNNvWq6dKo-slides]], [[youtube-bVNNvWq6dKo-dense-slides]], [[youtube-bVNNvWq6dKo-reconstructed-slides]]
- `youtube-MpZzWMdmQCE` — 5,590 transcript words; role: supporting context only.
- Transcript signals for `youtube-MpZzWMdmQCE`: claude, code, little, okay, give, cool, verification, well.
- Evidence links for `youtube-MpZzWMdmQCE` (supporting context only): [[youtube-MpZzWMdmQCE]], [[youtube-MpZzWMdmQCE-transcript]], [[youtube-MpZzWMdmQCE-slides]]
- `youtube-F_RyElT_gJk` — 9 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-F_RyElT_gJk`: coding, cursor, outcomes, claude, slop, incorrectly, replacement, google.
- Evidence links for `youtube-F_RyElT_gJk` (supporting context only): [[youtube-F_RyElT_gJk]], [[youtube-F_RyElT_gJk-slides]], [[youtube-F_RyElT_gJk-reconstructed-slides]]
- `youtube-HEFSExa0xl0` — 9,009 transcript words; 6 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-HEFSExa0xl0`: repl, model, tools, spreadsheet, tool, code, many, ended.
- Slide-derived themes for `youtube-HEFSExa0xl0`: interface, coding, engines, mattered, most, replacing, discrete, tools.
- Evidence links for `youtube-HEFSExa0xl0` (supporting context only): [[youtube-HEFSExa0xl0]], [[youtube-HEFSExa0xl0-transcript]], [[youtube-HEFSExa0xl0-slides]]
- `youtube-Rx8f05JI_WA` — 4,329 transcript words; 7 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-Rx8f05JI_WA`: tasks, verifier, task, full, marathon, hours, compiler, tests.
- Slide-derived themes for `youtube-Rx8f05JI_WA`: tasks, task, coding, projects, tokens, stay, coherent, over.
- Evidence links for `youtube-Rx8f05JI_WA` (supporting context only): [[youtube-Rx8f05JI_WA]], [[youtube-Rx8f05JI_WA-transcript]], [[youtube-Rx8f05JI_WA-slides]]
- `youtube-3hXJI2q0Jz8` — 3,697 transcript words; 9 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-3hXJI2q0Jz8`: coding, code, recursive, rlms, reasoning, prose, open, models.
- Slide-derived themes for `youtube-3hXJI2q0Jz8`: outcomes, behalf, reliable, while, hike, bottleneck, intelligence, reliability.
- Evidence links for `youtube-3hXJI2q0Jz8` (supporting context only): [[youtube-3hXJI2q0Jz8]], [[youtube-3hXJI2q0Jz8-transcript]], [[youtube-3hXJI2q0Jz8-slides]]
- `youtube-eOxOzcw70f0` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-eOxOzcw70f0`: code, vibes, learning, clone, even, exists, fully, give.
- Evidence links for `youtube-eOxOzcw70f0` (supporting context only): [[youtube-eOxOzcw70f0]], [[youtube-eOxOzcw70f0-slides]], [[youtube-eOxOzcw70f0-dense-slides]], [[youtube-eOxOzcw70f0-reconstructed-slides]]

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 70 | Related pages outside the main evidence categories. |
| resources | 29 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 48 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 28 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 2 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 22 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-will-bond-scaling-code-quality-building-ureview-uber-s-multi-agent-code-review-engine]]
- [[2026-06-29-owen-halpert-give-your-coding-agents-the-power-of-turbogrep]]
- [[2026-07-01-james-le-video-has-no-memory-here-s-how-we-built-one]]
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]]
- [[2026-07-01-anirban-chatterjee-guide-verify-solve-the-engineering-discipline-agentic-development-demands]]
- [[2026-06-29-nnenna-ndukwe-how-to-build-quality-gates-into-agentic-coding-workflows]]

### Resources
- [[youtube-pMggiOb18tc]]
- [[youtube-o-zkvb0iFDQ]]
- [[youtube-ZpK5PWX2YRM]]
- [[youtube--CnA2lGfymY]]
- [[youtube-n97BCfyFIvw]]
- [[youtube-uIiA6DquRiE]]

### Slides
- [[youtube-iRcX54EO5g8-slides]]
- [[youtube-HEFSExa0xl0-slides]]
- [[youtube-MpZzWMdmQCE-slides]]
- [[youtube-4kYl2_mqmnQ-slides]]
- [[youtube-IQkVMvXQKLY-slides]]
- [[youtube-2e9ANoOEn28-slides]]

### Transcripts
- [[youtube-pMggiOb18tc-transcript]]
- [[youtube-o-zkvb0iFDQ-transcript]]
- [[youtube-ZpK5PWX2YRM-transcript]]
- [[youtube--CnA2lGfymY-transcript]]
- [[youtube-n97BCfyFIvw-transcript]]
- [[youtube-htM02KMNZnk-transcript]]

### Tools
- [[docker]]
- [[mcp-apps]]

## Active Use Cases
- Bug fixes with local tests and deploy verification.
- Repository-wide mechanical updates with reviewable diffs.
- CI failure diagnosis and targeted remediation.
- Agentic software factories that coordinate planning, coding, testing, and release steps.

## Slide-Derived Supporting Decks
- [[youtube--CnA2lGfymY-slides]] — "I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox (32 extracted slide frames)
- [[youtube-n97BCfyFIvw-slides]] — "The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani (32 extracted slide frames)
- [[youtube-WkBPX-oDMnA-slides]] —  (12 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

## Slide-Derived Scheduled Session Signals
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]] — In Code They Act, In Proof We Trust
- [[2026-06-30-addy-osmani-closing-keynote]] — Closing Keynote
