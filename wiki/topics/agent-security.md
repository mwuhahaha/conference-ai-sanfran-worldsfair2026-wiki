---
title: "Agent Security"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
sourceAssessment:
  schemaVersion: 1
  claimId: claim:66a4c6055bfb543ba381c5d5a45b59a54312f07eca3453a6ac2711efe4d4e164
  subjectId: concept:agent-security
  domain: topics page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-17T13:24:54.408152Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-youtube--CnA2lGfymY
  - source:official-wf26-youtube-OqM67QG_Ikk
  - source:official-wf26-youtube-uU5Gv2h8-9g
sourceAssessmentBodySha256: sha256:9f427a81320d54fe314af5958193a6bb23e393e644d7dae2f7a0ee8887962594
---
# Agent Security

## Overview
Agent security covers the controls that keep autonomous or semi-autonomous AI systems within trusted boundaries. It includes authentication, authorization, tool permissions, sandboxing, prompt-injection resistance, secret handling, audit logs, data-boundary enforcement, and recovery paths when an agent behaves unexpectedly.

## Conference Context
It combines application security, cloud IAM, browser and plugin sandboxing, supply-chain security, and adversarial ML. Tool-using agents raise the stakes because natural-language inputs can influence systems that touch files, APIs, payments, infrastructure, or private data.

## How This Theme Evolved
- **World's Fair 2024 (local comparison fixture):** Human oversight and infrastructure were broad safeguards around AI systems.
- **Miami 2026 (public comparison wiki):** Remote agents and sandboxed compute made runtime boundaries part of developer workflow.
- **World's Fair 2025 (local comparison fixture):** The comparison corpus foregrounded containment, identity, OAuth, access control, and code-execution safety.
- **World's Fair 2026 (current event synthesis backed by linked local evidence):** The linked conference graph treats sandboxes, tool permissions, provenance, and eval gates as one operational control surface.

**Confidence:** high.
**Boundary:** Earlier event wikis are comparison context only. They are not primary evidence for World's Fair 2026 claims, and no local fixture is represented as a public live site.
**Comparison source:** [[aie-wiki-generation-delta]].

## Significance
Agents convert text into action. That makes ordinary content, retrieved documents, web pages, or UI state part of the attack surface. Security is what lets teams give agents useful tools without handing them unlimited authority.

## Why This Matters Now
Agents increasingly execute code and use credentials rather than only returning text, so correctness and blast-radius control must be designed together.

**WF26 evidence gate:** this section was emitted only because the page links to configured local evidence. Relevant configured evidence: [[2026-06-29-steve-yegge-agentic-security-permissions-provenance-and-the-agent-supply-chain]], [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale]], [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert]].

**Confidence:** high. Comparison history is context; linked WF26 pages remain the evidence for current-event claims.

## Applied Use
Use least-privilege tool scopes, explicit approval gates for high-risk actions, isolated execution environments, secret redaction, provenance checks, and audit trails. Treat retrieved content as untrusted input, test prompt-injection cases, and design rollback paths for destructive operations.

Agent security matters in coding agents, MCP servers, browser agents, enterprise assistants, finance and compliance workflows, internal operations tools, and any system connected to privileged APIs or private data.

Apply strong controls whenever an agent can read sensitive data, write state, call external APIs, spend money, deploy code, or influence another system. Lower-risk chat-only agents still need data handling and logging rules.

## Active Use Cases
- Permission-gated tool execution for enterprise agents.
- Sandboxed coding and browser automation.
- Prompt-injection and data-exfiltration testing for retrieval agents.
- Audit logs for regulated or high-trust agent workflows.
## Practical Lesson
Give each run the minimum tools, credentials, network reach, filesystem scope, and lifetime it needs; capture actions and outputs so approval and incident review use the same evidence trail.

**Confidence:** high. Treat this as synthesis derived from the linked evidence graph, not as an official schedule claim.

## Slide-Derived Scheduled Session Signals
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2

## Slide-Derived Supporting Decks
- [[youtube-OqM67QG_Ikk-slides]] — From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI (15 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.
## Connections
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
- [[cua|Cua]]
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

- [[youtube-4kYl2_mqmnQ-slides]] — I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON (10 extracted slide frames)
- [[youtube-2IxD9OB3XuQ-slides]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI (24 extracted slide frames)

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 40 | Related pages outside the main evidence categories. |
| resources | 7 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 13 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 24 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 4 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 6 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-steve-yegge-agentic-security-permissions-provenance-and-the-agent-supply-chain]]
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale]]
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]]
- [[2026-06-29-lovina-dmello-your-llm-stack-is-a-2008-database-with-better-marketing-why-ml-security-is-dominated-by-misconfiguration-not-missing-features]]

### Resources
- [[aie-wiki-generation-delta]]
- [[youtube-OqM67QG_Ikk]]
- [[youtube-4sX_He5c4sI]]
- [[youtube-I2cbIws9j10]]
- [[youtube-htM02KMNZnk]]
- [[youtube--CnA2lGfymY]]

### Slides
- [[youtube-OqM67QG_Ikk-slides]]
- [[youtube-4kYl2_mqmnQ-slides]]
- [[youtube-2IxD9OB3XuQ-slides]]
- [[youtube-4sX_He5c4sI-slides]]
- [[youtube-4sX_He5c4sI-dense-slides]]
- [[youtube-4sX_He5c4sI-reconstructed-slides]]

### Transcripts
- [[youtube-OqM67QG_Ikk-transcript]]
- [[youtube-4sX_He5c4sI-transcript]]
- [[youtube-I2cbIws9j10-transcript]]
- [[youtube-htM02KMNZnk-transcript]]
- [[youtube--CnA2lGfymY-transcript]]
- [[youtube-uU5Gv2h8-9g-transcript]]

### Tools
- [[docker]]
- [[openhands]]
- [[pydantic]]
- [[daytona]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.

### Linked Sessions
- [[2026-06-29-steve-yegge-agentic-security-permissions-provenance-and-the-agent-supply-chain|Agentic Security: Permissions, Provenance, and the Agent Supply Chain]]
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale|Sandboxes Aren't Optional: Runtime Isolation Patterns for Coding Agents at Scale]]
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert|Your agent needs a sandbox, not a desert]]
- [[2026-06-29-lovina-dmello-your-llm-stack-is-a-2008-database-with-better-marketing-why-ml-security-is-dominated-by-misconfiguration-not-missing-features|Your LLM Stack Is a 2008 Database With Better Marketing: Why ML Security Is Dominated by Misconfiguration, Not Missing Features]]
- [[2026-06-30-ivan-burazin-kubernetes-is-not-your-sandbox|Kubernetes Is Not Your Sandbox]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1']]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2']]
- [[2026-06-30-kevin-orellana-1-000-agent-tasks-in-a-sandbox-what-breaks-when-llms-write-and-run-code|1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Write and Run Code]]
- [[2026-06-29-bereket-habtemeskel-agent-auth|Agent Auth]]
- [[2026-07-01-jay-mok-your-agent-just-authorized-what|Your Agent Just Authorized What?!]]

### Media Signals
- `youtube-OqM67QG_Ikk` — 7,738 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-OqM67QG_Ikk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-OqM67QG_Ikk`: kernel, many, system, code, host, guest, block, running.
- Slide-derived themes for `youtube-OqM67QG_Ikk`: engineering, sandbox, platform, track, july, security, fork, fleet.
- Evidence links for `youtube-OqM67QG_Ikk` (primary event evidence): [[youtube-OqM67QG_Ikk]], [[youtube-OqM67QG_Ikk-transcript]], [[youtube-OqM67QG_Ikk-slides]]
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-4sX_He5c4sI`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: lots, examples, stream, starts, july, land, king, chief.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
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
- `youtube--CnA2lGfymY` — 3,148 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube--CnA2lGfymY`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube--CnA2lGfymY`: answer, lean, safe, model, type, look, llms, question.
- Slide-derived themes for `youtube--CnA2lGfymY`: someone, credible, fair, conviction, sara, made, serious, error.
- Evidence links for `youtube--CnA2lGfymY` (primary event evidence): [[youtube--CnA2lGfymY]], [[youtube--CnA2lGfymY-transcript]], [[youtube--CnA2lGfymY-slides]]
- `youtube-uU5Gv2h8-9g` — 10,417 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-uU5Gv2h8-9g`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-uU5Gv2h8-9g`: code, claude, prompt, been, cloud, model, mode, team.
- Evidence links for `youtube-uU5Gv2h8-9g` (primary event evidence): [[youtube-uU5Gv2h8-9g]], [[youtube-uU5Gv2h8-9g-transcript]], [[youtube-uU5Gv2h8-9g-slides]]
