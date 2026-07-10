---
title: "Agent Security"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---
# Agent Security

## Overview
Agent security covers the controls that keep autonomous or semi-autonomous AI systems within trusted boundaries. It includes authentication, authorization, tool permissions, sandboxing, prompt-injection resistance, secret handling, audit logs, data-boundary enforcement, and recovery paths when an agent behaves unexpectedly.

## Conference Context
It combines application security, cloud IAM, browser and plugin sandboxing, supply-chain security, and adversarial ML. Tool-using agents raise the stakes because natural-language inputs can influence systems that touch files, APIs, payments, infrastructure, or private data.

## Significance
Agents convert text into action. That makes ordinary content, retrieved documents, web pages, or UI state part of the attack surface. Security is what lets teams give agents useful tools without handing them unlimited authority.

## Applied Use
Use least-privilege tool scopes, explicit approval gates for high-risk actions, isolated execution environments, secret redaction, provenance checks, and audit trails. Treat retrieved content as untrusted input, test prompt-injection cases, and design rollback paths for destructive operations.

Agent security matters in coding agents, MCP servers, browser agents, enterprise assistants, finance and compliance workflows, internal operations tools, and any system connected to privileged APIs or private data.

Apply strong controls whenever an agent can read sensitive data, write state, call external APIs, spend money, deploy code, or influence another system. Lower-risk chat-only agents still need data handling and logging rules.

## Connections
- [[youtube-4kYl2_mqmnQ-slides]] — I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON (10 extracted slide frames)
- [[youtube-2IxD9OB3XuQ-slides]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI (24 extracted slide frames)

- [[2026-06-29-lovina-dmello-your-llm-stack-is-a-2008-database-with-better-marketing-why-ml-security-is-dominated-by-misconfiguration-not-missing-features]] — Your LLM Stack Is a 2008 Database With Better Marketing: Why ML Security Is Dominated by Misconfiguration, Not Missing Features; [[lovina-dmello|Lovina Dmello]] (Day 2 — Session Day 1 · 11:10am-11:30am · Security; official schedule)
- [[2026-06-29-steve-yegge-agentic-security-permissions-provenance-and-the-agent-supply-chain]] — Agentic Security: Permissions, Provenance, and the Agent Supply Chain; [[steve-yegge|Steve Yegge]] (Day 2 — Session Day 1 · 2:25pm-2:45pm · Security; official schedule)
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale]] — Sandboxes Aren't Optional: Runtime Isolation Patterns for Coding Agents at Scale; [[robert-brennan|Robert Brennan]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Sandbox & Platform Engineering; official schedule)
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert]] — Your agent needs a sandbox, not a desert; [[samuel-colvin|Samuel Colvin]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · Sandbox & Platform Engineering; official schedule)
- [[2026-06-30-ivan-burazin-kubernetes-is-not-your-sandbox]] — Kubernetes Is Not Your Sandbox; [[ivan-burazin|Ivan Burazin]] (Day 3 — Session Day 2 · 11:40am-12:00pm · Sandbox & Platform Engineering; official schedule)
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1; [[abhishek-bhardwaj|Abhishek Bhardwaj]] (Day 3 — Session Day 2 · 1:30pm-1:50pm · Sandbox & Platform Engineering; official schedule)
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2; [[abhishek-bhardwaj|Abhishek Bhardwaj]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Sandbox & Platform Engineering; official schedule)
- [[2026-06-30-kevin-orellana-1-000-agent-tasks-in-a-sandbox-what-breaks-when-llms-write-and-run-code]] — 1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Write and Run Code; [[kevin-orellana|Kevin Orellana]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Sandbox & Platform Engineering; official schedule)
- [[2026-06-29-bereket-habtemeskel-agent-auth]] — Agent Auth; [[bereket-habtemeskel|Bereket Habtemeskel]], [[paola-estefania|Paola Estefania]] (Day 1 — Workshop Day · 4:30pm-5:30pm · Workshops Day 1; official schedule)
- [[2026-07-01-jay-mok-your-agent-just-authorized-what]] — Your Agent Just Authorized What?!; [[jay-mok|Jay Mok]] (Day 4 — Session Day 3 · 2:50pm-3:10pm · Agentic Commerce; official schedule)
- [[2026-06-29-manoj-nair-through-the-ai-fog-the-architectural-decision-the-next-24-months-of-agentic-security-depends-on]] — Through the AI Fog: The architectural decision the next 24 months of agentic security depends on.; [[manoj-nair|Manoj Nair]] (Day 2 — Session Day 1 · 10:45am-11:05am · Security; official schedule)
- [[2026-06-29-ezra-tanzer-agentic-development-security]] — Agentic Development Security; [[ezra-tanzer|Ezra Tanzer]] (Day 2 — Session Day 1 · 12:05pm-12:25pm · Security; official schedule)
- [[2026-07-01-michael-grinich-auth-for-agents-unblock-autonomous-ai-with-auth-md]] — Auth for Agents: Unblock Autonomous AI with auth.md; [[michael-grinich|Michael Grinich]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Agentic Engineering; official schedule)
- [[2026-06-29-matt-brockman-how-i-learned-to-stop-worrying-and-love-the-sandbox]] — How I learned to stop worrying and love the sandbox; [[matt-brockman|Matt Brockman]] (Day 1 — Workshop Day · 11:05am-12:05pm · Workshops Day 1; official schedule)
- [[2026-06-29-ryan-dahl-security-firewall-for-agents]] — Security Firewall for Agents; [[ryan-dahl|Ryan Dahl]] (Day 2 — Session Day 1 · 10:45am-11:05am · Claws & Personal Agents; official schedule)
- [[2026-06-29-tanmai-gopal-your-company-brain-will-leak-secrets-here-s-how-we-stopped-it-for-big-banks-and-ourselves]] — Your company brain will leak secrets. Here's how we stopped it for big banks and ourselves.; [[tanmai-gopal|Tanmai Gopal]] (Day 2 — Session Day 1 · 2:50pm-3:10pm · Claws & Personal Agents; official schedule)
- [[2026-07-01-rowan-christmas-yolo-mode-safely-microvm-sandboxes-for-any-agent]] — YOLO Mode, Safely: microVM Sandboxes for Any Agent; [[rowan-christmas|Rowan Christmas]] (Day 4 — Session Day 3 · 1:30pm-1:50pm · Expo Stage 2 NW; official schedule)
- [[2026-07-01-arun-sekhar-blast-radius-zero-one-command-openclaw-sandboxes-in-the-cloud]] — Blast Radius Zero: One‑Command OpenClaw Sandboxes in the Cloud; [[arun-sekhar|Arun Sekhar]] (Day 4 — Session Day 3 · 1:55pm-2:15pm · Track M; official schedule)
- [[2026-07-01-rashi-agrawal-guardrails-first-engineering-member-facing-health-ai]] — Guardrails First: Engineering Member-Facing Health AI; [[rashi-agrawal|Rashi Agrawal]] (Day 4 — Session Day 3 · 11:10am-11:30am · AI in Healthcare; official schedule)
- [[2026-06-29-micah-silverman-ai-security-engineer-foundations-certificate]] — AI Security Engineer Foundations + Certificate; [[javier-garza|Javier Garza]] (Day 1 — Workshop Day · 9:00am-11:00am · Workshops Day 1; official schedule)
- [[2026-06-29-palak-agarwal-how-reducto-parsed-the-epstein-files-for-the-viral-jmail-project-the-secret-complexities-of-document]] — How Reducto parsed the Epstein Files for the Viral JMail Project: The Secret Complexities of Document; [[palak-agarwal|Palak Agarwal]] (Day 1 — Workshop Day · 1:15pm-2:15pm · Track 7; official schedule)
- [[2026-06-29-manoj-nair-security-track-intro]] — Security Track intro; [[manoj-nair|Manoj Nair]] (Day 2 — Session Day 1 · 10:25am-10:30am · Software Factories; official schedule)
- [[2026-06-29-natalie-meurer-the-dirty-secret-of-forward-deployed-engineering]] — The Dirty Secret of Forward Deployed Engineering; [[natalie-meurer|Natalie Meurer]] (Day 2 — Session Day 1 · 1:30pm-1:50pm · Forward Deployed Engineering; official schedule)
- [[2026-06-30-philipp-schmid-why-agents-should-have-their-own-sandbox]] — Why Agents Should Have Their Own Sandbox; [[philipp-schmid|Philipp Schmid]] (Day 3 — Session Day 2 · 1:30pm-1:50pm · Expo Stage 1; official schedule)

- [[john-craft|John Craft]]
- [[abhishek-bhardwaj|Abhishek Bhardwaj]]
- [[manoj-nair|Manoj Nair]]
- [[christopher-manning|Christopher Manning]]
- [[lovina-dmello|Lovina Dmello]]
- [[steve-yegge|Steve Yegge]]
- [[robert-brennan|Robert Brennan]]
- [[samuel-colvin|Samuel Colvin]]
- [[ivan-burazin|Ivan Burazin]]
- [[kevin-orellana|Kevin Orellana]]
- [[bereket-habtemeskel|Bereket Habtemeskel]]
- [[paola-estefania|Paola Estefania]]
- [[jay-mok|Jay Mok]]
- [[ezra-tanzer|Ezra Tanzer]]
- [[michael-grinich|Michael Grinich]]
- [[matt-brockman|Matt Brockman]]
- [[ryan-dahl|Ryan Dahl]]
- [[tanmai-gopal|Tanmai Gopal]]
- [[rowan-christmas|Rowan Christmas]]
- [[arun-sekhar|Arun Sekhar]]
- [[rashi-agrawal|Rashi Agrawal]]
- [[javier-garza|Javier Garza]]
- [[palak-agarwal|Palak Agarwal]]
- [[natalie-meurer|Natalie Meurer]]

- [[docker|Docker]]
- [[snyk|Snyk]]
- [[workos|WorkOS]]
- [[openai|OpenAI]]
- [[anthropic|Anthropic]]
- [[paypal|PayPal]]
- [[microsoft|Microsoft]]
- [[better-auth|Better Auth]]
- [[navan|Navan]]
- [[stripe|Stripe]]
- [[moonlake-ai|Moonlake AI]]
- [[uber|Uber]]
- [[sondermind|SonderMind]]
- [[nvidia|NVIDIA]]
- [[gas-town|Gas Town]]
- [[openhands|OpenHands]]
- [[pydantic|Pydantic]]
- [[daytona|Daytona]]

## Evidence Graph
### Transcript-backed resources
- [[youtube-MpZzWMdmQCE]] — Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com
- [[youtube-SKDJo2CopRs]] — Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare
- [[youtube-CLttOU7n6sI]] — Respect The Process - Andrew Dumit, Watershed Technology Inc.
- [[youtube-c-2eEv2ou7Y]] — Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic
- [[youtube-LrGCT7G_rU8]] — Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon
- [[youtube-CDqzWpwkSls]] — Build AI Systems for Discernment, Not Approval - Angel Ortmann Lee, Duolingo
- [[youtube-BqZrTdgBaPw]] — Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG
- [[youtube-iRcX54EO5g8]] — Your agent is blindfolded — Johan Lajili, Poolside AI
- [[youtube-hCMrEfPG2Yg]] — Beyond Components: Designing Generative UI for MCP Apps — Ruben Casas, Postman
- [[youtube-_xIwFcnHqp4]] — Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub
- [[youtube-6bmM45jkMDY]] — You Can't Prompt the Room: The Last Skill AI Won't Replace - Balázs Horváth, VisualLabs

This evidence graph consolidates scheduled talks, linked videos, transcripts, and slide-derived material connected to this topic.

### Linked Sessions
- [[2026-06-29-lovina-dmello-your-llm-stack-is-a-2008-database-with-better-marketing-why-ml-security-is-dominated-by-misconfiguration-not-missing-features|Your LLM Stack Is a 2008 Database With Better Marketing: Why ML Security Is Dominated by Misconfiguration, Not Missing Features]]
- [[2026-06-29-steve-yegge-agentic-security-permissions-provenance-and-the-agent-supply-chain|Agentic Security: Permissions, Provenance, and the Agent Supply Chain]]
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale|Sandboxes Aren't Optional: Runtime Isolation Patterns for Coding Agents at Scale]]
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert|Your agent needs a sandbox, not a desert]]
- [[2026-06-30-ivan-burazin-kubernetes-is-not-your-sandbox|Kubernetes Is Not Your Sandbox]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1']]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2']]
- [[2026-06-30-kevin-orellana-1-000-agent-tasks-in-a-sandbox-what-breaks-when-llms-write-and-run-code|1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Write and Run Code]]
- [[2026-06-29-bereket-habtemeskel-agent-auth|Agent Auth]]
- [[2026-07-01-jay-mok-your-agent-just-authorized-what|Your Agent Just Authorized What?!]]

### Media Signals
- `youtube-7Dtu2bilcFs` — 9 slide-derived text signals
- Slide-derived themes for `youtube-7Dtu2bilcFs`: coding, agentic, final, form, coming, next, stop, models.
- Evidence links for `youtube-7Dtu2bilcFs`: [[youtube-7Dtu2bilcFs]], [[youtube-7Dtu2bilcFs-slides]], [[youtube-7Dtu2bilcFs-dense-slides]], [[youtube-7Dtu2bilcFs-reconstructed-slides]]
- `youtube-rcsliSIy_YU` — 8 slide-derived text signals
- Slide-derived themes for `youtube-rcsliSIy_YU`: coding, code, snippets, generation, single, atomic, tasks, curl.
- Evidence links for `youtube-rcsliSIy_YU`: [[youtube-rcsliSIy_YU]], [[youtube-rcsliSIy_YU-slides]], [[youtube-rcsliSIy_YU-dense-slides]], [[youtube-rcsliSIy_YU-reconstructed-slides]]
- `youtube-bmWZk9vTze0` — 10 slide-derived text signals
- Slide-derived themes for `youtube-bmWZk9vTze0`: query, client, info, table, tool, call, response, await.
- Evidence links for `youtube-bmWZk9vTze0`: [[youtube-bmWZk9vTze0]], [[youtube-bmWZk9vTze0-slides]], [[youtube-bmWZk9vTze0-dense-slides]], [[youtube-bmWZk9vTze0-reconstructed-slides]]
- `youtube-e9sLVMN76qU` — 8 slide-derived text signals
- Slide-derived themes for `youtube-e9sLVMN76qU`: most, today, tooling, breaks, moment, remove, human, loop.
- Evidence links for `youtube-e9sLVMN76qU`: [[youtube-e9sLVMN76qU]], [[youtube-e9sLVMN76qU-slides]], [[youtube-e9sLVMN76qU-reconstructed-slides]]
- `youtube-wsFd22SL1s8` — 10 slide-derived text signals
- Slide-derived themes for `youtube-wsFd22SL1s8`: systems, chrome, code, sandboxes, operating, distributed, windows, subsystem.
- Evidence links for `youtube-wsFd22SL1s8`: [[youtube-wsFd22SL1s8]], [[youtube-wsFd22SL1s8-slides]], [[youtube-wsFd22SL1s8-dense-slides]], [[youtube-wsFd22SL1s8-reconstructed-slides]]

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 39 | Related pages outside the main evidence categories. |
| resources | 16 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 16 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 24 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 4 | Derived inventory pages; use as entity context, not independent proof. |

### Talks
- [[2026-06-29-lovina-dmello-your-llm-stack-is-a-2008-database-with-better-marketing-why-ml-security-is-dominated-by-misconfiguration-not-missing-features]]
- [[2026-06-29-steve-yegge-agentic-security-permissions-provenance-and-the-agent-supply-chain]]
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale]]
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert]]
- [[2026-06-30-ivan-burazin-kubernetes-is-not-your-sandbox]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]]

### Resources
- [[youtube-MpZzWMdmQCE]]
- [[youtube-SKDJo2CopRs]]
- [[youtube-CLttOU7n6sI]]
- [[youtube-c-2eEv2ou7Y]]
- [[youtube-LrGCT7G_rU8]]
- [[youtube-CDqzWpwkSls]]

### Slides
- [[youtube-4kYl2_mqmnQ-slides]]
- [[youtube-2IxD9OB3XuQ-slides]]
- [[youtube-7Dtu2bilcFs-slides]]
- [[youtube-7Dtu2bilcFs-dense-slides]]
- [[youtube-7Dtu2bilcFs-reconstructed-slides]]
- [[youtube-rcsliSIy_YU-slides]]

### Tools
- [[docker]]
- [[openhands]]
- [[pydantic]]
- [[daytona]]

## Active Use Cases
- Permission-gated tool execution for enterprise agents.
- Sandboxed coding and browser automation.
- Prompt-injection and data-exfiltration testing for retrieval agents.
- Audit logs for regulated or high-trust agent workflows.
