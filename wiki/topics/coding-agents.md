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

## Active Use Cases
- Bug fixes with local tests and deploy verification.
- Repository-wide mechanical updates with reviewable diffs.
- CI failure diagnosis and targeted remediation.
- Agentic software factories that coordinate planning, coding, testing, and release steps.

## Slide-Derived Scheduled Session Signals
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]] — The Golden Age of AI Engineering
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]] — In Code They Act, In Proof We Trust
- [[2026-06-30-addy-osmani-closing-keynote]] — Closing Keynote
- [[2026-06-30-alex-volkov-the-z-l-continuum-should-ai-engineers-still-read-code]] — The Z/L Continuum: Should AI Engineers Still Read Code?
- [[2026-06-30-benoit-schillings-research-to-reality-with-google-deepmind]] — Research to Reality with Google DeepMind
- [[2026-06-30-zhengyao-jiang-an-ai-agent-became-the-1-contributor-in-openai-s-hiring-challenge]] — An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge
- [[2026-07-01-james-russo-html-is-all-agents-need]] — HTML Is All Agents Need

## Slide-Derived Supporting Decks
- [[youtube--CnA2lGfymY-slides]] — "I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox (32 extracted slide frames)
- [[youtube-1P1hJ36rxM0-slides]] — Research to Reality with Google DeepMind — Benoit Schillings, Google DeepMind (15 extracted slide frames)
- [[youtube-Cz4v1WHVyZc-slides]] — HTML Is All Agents Need — James Russo, HeyGen (32 extracted slide frames)
- [[youtube-iCj_ATyThvc-slides]] — An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge — Zhengyao Jiang, Weco (3 extracted slide frames)
- [[youtube-n97BCfyFIvw-slides]] — "The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani (32 extracted slide frames)
- [[youtube-pMggiOb18tc-slides]] — The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI (32 extracted slide frames)
- [[youtube-WkBPX-oDMnA-slides]] —  (12 extracted slide frames)
- [[youtube-ZpK5PWX2YRM-slides]] — Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI (32 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

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

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 70 | Related pages outside the main evidence categories. |
| resources | 22 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 47 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 31 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 2 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 19 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]]
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]]
- [[2026-06-30-addy-osmani-closing-keynote]]
- [[2026-06-30-alex-volkov-the-z-l-continuum-should-ai-engineers-still-read-code]]
- [[2026-06-30-benoit-schillings-research-to-reality-with-google-deepmind]]
- [[2026-06-30-zhengyao-jiang-an-ai-agent-became-the-1-contributor-in-openai-s-hiring-challenge]]

### Resources
- [[youtube-pMggiOb18tc]]
- [[youtube-o-zkvb0iFDQ]]
- [[youtube-ZpK5PWX2YRM]]
- [[youtube-OqM67QG_Ikk]]
- [[youtube-0vphxNt4wyk]]
- [[youtube-4sX_He5c4sI]]

### Slides
- [[youtube--CnA2lGfymY-slides]]
- [[youtube-1P1hJ36rxM0-slides]]
- [[youtube-Cz4v1WHVyZc-slides]]
- [[youtube-iCj_ATyThvc-slides]]
- [[youtube-n97BCfyFIvw-slides]]
- [[youtube-pMggiOb18tc-slides]]

### Transcripts
- [[youtube-pMggiOb18tc-transcript]]
- [[youtube-o-zkvb0iFDQ-transcript]]
- [[youtube-OqM67QG_Ikk-transcript]]
- [[youtube-0vphxNt4wyk-transcript]]
- [[youtube-4sX_He5c4sI-transcript]]
- [[youtube-9fubhllmsBU-transcript]]

### Tools
- [[docker]]
- [[mcp-apps]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.

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
- `youtube-pMggiOb18tc` — 4,606 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-pMggiOb18tc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-pMggiOb18tc`: models, codex, open, model, should, engineering, well, even.
- Slide-derived themes for `youtube-pMggiOb18tc`: codex, software, engineers, computer, plugins, lifetime, career, left.
- Evidence links for `youtube-pMggiOb18tc` (primary event evidence): [[youtube-pMggiOb18tc]], [[youtube-pMggiOb18tc-transcript]], [[youtube-pMggiOb18tc-slides]]
- `youtube-o-zkvb0iFDQ` — 3,969 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-o-zkvb0iFDQ`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-o-zkvb0iFDQ`: apps, host, claude, back, chatgpt, look, mcpui, chat.
- Evidence links for `youtube-o-zkvb0iFDQ` (primary event evidence): [[youtube-o-zkvb0iFDQ]], [[youtube-o-zkvb0iFDQ-transcript]], [[youtube-o-zkvb0iFDQ-slides]], [[youtube-o-zkvb0iFDQ-dense-slides]], [[youtube-o-zkvb0iFDQ-reconstructed-slides]]
- `youtube-OqM67QG_Ikk` — 7,738 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-OqM67QG_Ikk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-OqM67QG_Ikk`: kernel, many, system, code, host, guest, block, running.
- Slide-derived themes for `youtube-OqM67QG_Ikk`: engineering, sandbox, platform, track, july, security, fork, fleet.
- Evidence links for `youtube-OqM67QG_Ikk` (primary event evidence): [[youtube-OqM67QG_Ikk]], [[youtube-OqM67QG_Ikk-transcript]], [[youtube-OqM67QG_Ikk-slides]]
- `youtube-0vphxNt4wyk` — 3,965 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-0vphxNt4wyk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-0vphxNt4wyk`: skill, skills, model, should, look, evals, eval, always.
- Slide-derived themes for `youtube-0vphxNt4wyk`: skills, fail, chad, vibe, checks, production, engineering, future.
- Evidence links for `youtube-0vphxNt4wyk` (primary event evidence): [[youtube-0vphxNt4wyk]], [[youtube-0vphxNt4wyk-transcript]], [[youtube-0vphxNt4wyk-slides]]
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-4sX_He5c4sI`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: system, prompt, examples, tools, lots, claude, gets, smarter.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube-9fubhllmsBU` — 3,542 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-9fubhllmsBU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-9fubhllmsBU`: claude, fable, code, give, models, prompt, model, little.
- Slide-derived themes for `youtube-9fubhllmsBU`: opening, land, king, models, grown, designed, fetch, write.
- Evidence links for `youtube-9fubhllmsBU` (primary event evidence): [[youtube-9fubhllmsBU]], [[youtube-9fubhllmsBU-transcript]], [[youtube-9fubhllmsBU-slides]]
- `youtube-Cz4v1WHVyZc` — 2,535 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Cz4v1WHVyZc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Cz4v1WHVyZc`: html, great, hyperframes, output, create, frame, coding, javascript.
- Slide-derived themes for `youtube-Cz4v1WHVyZc`: track, july, most, engineering, future, html, javascript, native.
- Evidence links for `youtube-Cz4v1WHVyZc` (primary event evidence): [[youtube-Cz4v1WHVyZc]], [[youtube-Cz4v1WHVyZc-transcript]], [[youtube-Cz4v1WHVyZc-slides]]
- `youtube-I2cbIws9j10` — 91,792 transcript words; 7 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-I2cbIws9j10`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: context, window, selects, response, facts, retry, coerce, rollback.
- Evidence links for `youtube-I2cbIws9j10` (primary event evidence): [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
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
- `youtube-htM02KMNZnk` — 89,050 transcript words; 4 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-htM02KMNZnk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-htM02KMNZnk`: model, code, models, loop, well, software, first, team.
- Slide-derived themes for `youtube-htM02KMNZnk`: cycles, stacking, loops, tokens, tools, tasks, throughput, many.
- Evidence links for `youtube-htM02KMNZnk` (primary event evidence): [[youtube-htM02KMNZnk]], [[youtube-htM02KMNZnk-transcript]], [[youtube-htM02KMNZnk-slides]], [[youtube-htM02KMNZnk-dense-slides]], [[youtube-htM02KMNZnk-reconstructed-slides]]
- `youtube-n97BCfyFIvw` — 3,068 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-n97BCfyFIvw`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-n97BCfyFIvw`: code, still, taste, loop, engineering, evidence, system, human.
- Slide-derived themes for `youtube-n97BCfyFIvw`: roles, google, look, across, worth, doing, increasingly, automated.
- Evidence links for `youtube-n97BCfyFIvw` (primary event evidence): [[youtube-n97BCfyFIvw]], [[youtube-n97BCfyFIvw-transcript]], [[youtube-n97BCfyFIvw-slides]]
- `youtube-uU5Gv2h8-9g` — 10,417 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-uU5Gv2h8-9g`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-uU5Gv2h8-9g`: code, claude, prompt, been, cloud, model, mode, team.
- Evidence links for `youtube-uU5Gv2h8-9g` (primary event evidence): [[youtube-uU5Gv2h8-9g]], [[youtube-uU5Gv2h8-9g-transcript]], [[youtube-uU5Gv2h8-9g-slides]]
- `youtube-xUnRQ9vLXxo` — 9,663 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-xUnRQ9vLXxo`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-xUnRQ9vLXxo`: used, model, look, code, does, models, trying, even.
- Evidence links for `youtube-xUnRQ9vLXxo` (primary event evidence): [[youtube-xUnRQ9vLXxo]], [[youtube-xUnRQ9vLXxo-transcript]], [[youtube-xUnRQ9vLXxo-slides]]
- `youtube-7Dtu2bilcFs` — 9 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-7Dtu2bilcFs`: coding, agentic, final, form, coming, next, stop, models.
- Evidence links for `youtube-7Dtu2bilcFs` (supporting context only): [[youtube-7Dtu2bilcFs]], [[youtube-7Dtu2bilcFs-slides]], [[youtube-7Dtu2bilcFs-dense-slides]], [[youtube-7Dtu2bilcFs-reconstructed-slides]]
- `youtube-MpZzWMdmQCE` — 5,590 transcript words; role: supporting context only.
- Transcript signals for `youtube-MpZzWMdmQCE`: claude, code, little, okay, give, cool, verification, well.
- Evidence links for `youtube-MpZzWMdmQCE` (supporting context only): [[youtube-MpZzWMdmQCE]], [[youtube-MpZzWMdmQCE-transcript]], [[youtube-MpZzWMdmQCE-slides]]
- `youtube-HEFSExa0xl0` — 9,009 transcript words; 6 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-HEFSExa0xl0`: repl, model, tools, spreadsheet, tool, code, many, ended.
- Slide-derived themes for `youtube-HEFSExa0xl0`: interface, coding, engines, mattered, most, replacing, discrete, tools.
- Evidence links for `youtube-HEFSExa0xl0` (supporting context only): [[youtube-HEFSExa0xl0]], [[youtube-HEFSExa0xl0-transcript]], [[youtube-HEFSExa0xl0-slides]]
- `youtube-Rx8f05JI_WA` — 4,329 transcript words; 7 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-Rx8f05JI_WA`: tasks, verifier, task, full, marathon, hours, compiler, tests.
- Slide-derived themes for `youtube-Rx8f05JI_WA`: tasks, task, coding, projects, tokens, stay, coherent, over.
- Evidence links for `youtube-Rx8f05JI_WA` (supporting context only): [[youtube-Rx8f05JI_WA]], [[youtube-Rx8f05JI_WA-transcript]], [[youtube-Rx8f05JI_WA-slides]]
- `youtube-bSG9wUYaHWU` — source page linked; role: supporting context only.
- Evidence links for `youtube-bSG9wUYaHWU` (supporting context only): [[youtube-bSG9wUYaHWU]], [[youtube-bSG9wUYaHWU-slides]], [[youtube-bSG9wUYaHWU-dense-slides]], [[youtube-bSG9wUYaHWU-reconstructed-slides]]
