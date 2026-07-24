---
title: Agent Security
category: topics
sourceLabels:
  - Slide/video-derived supporting context
last_auto_summarized: '2026-07-18T22:16:32.316Z'
sourceAssessment:
  schemaVersion: 1
  claimId: claim:66a4c6055bfb543ba381c5d5a45b59a54312f07eca3453a6ac2711efe4d4e164
  subjectId: concept:agent-security
  domain: topics page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-24T00:00:00.000000Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-youtube--CnA2lGfymY
  - source:official-wf26-youtube--I5W5QVAT8E
  - source:official-wf26-youtube-1EZdpEhwmNc
  - source:official-wf26-youtube-8qWIPUia2O8
  - source:official-wf26-youtube-JvKO40CFq-s
  - source:official-wf26-youtube-OqM67QG_Ikk
  - source:official-wf26-youtube-X1kp-ABIIxQ
  - source:official-wf26-youtube-imFedndyXYQ
  - source:official-wf26-youtube-n97BCfyFIvw
  - source:official-wf26-youtube-uU5Gv2h8-9g
sourceAssessmentBodySha256: sha256:c4be063df8bf9687b4be0b0c3eed2200cffcb76ad3ad925792498ee72488473b
---
# Agent Security

## Overview
At World’s Fair 2026, agent security is treated as an end-to-end systems problem rather than a model-level feature. The connected sessions span the full path from establishing an agent’s identity to limiting what it may authorize, verifying what it consumes, containing what it executes, and retaining evidence of what occurred. Steve Yegge links permissions with provenance and the agent software supply chain, while Lovina Dmello argues that many practical ML-security failures arise from configuration errors in otherwise capable infrastructure. Bereket Habtemeskel and Paola Estefania introduce the Agent Auth protocol as an identity layer for agents; Michael Grinich’s `auth.md` work applies enterprise authorization patterns to autonomous software; and Jay Mok shows why delegation must encode transaction scope when an agent can commit money. Manoj Nair and Ezra Tanzer connect these controls to the architecture and development lifecycle of agent-built applications, while Ryan Dahl’s agent firewall and Tanmai Gopal’s company-knowledge session address hostile inputs and the leakage of sensitive enterprise context.

Runtime containment is the page’s other major evidence cluster. Robert Brennan and Samuel Colvin frame purpose-built sandboxes as necessary infrastructure for coding agents, and Ivan Burazin distinguishes orchestration with Kubernetes from an actual security boundary. Abhishek Bhardwaj’s two-part “From fork() to Fleet” session follows that boundary from process creation and kernel controls to fleet-scale sandbox management, with an official recording, transcript, and extracted slides providing additional evidence. Kevin Orellana examines failures across 1,000 code-writing tasks, while Matt Brockman, Rowan Christmas, Arun Sekhar, and Philipp Schmid cover developer sandboxes, microVMs, cloud-hosted OpenClaw isolation, and agent-specific execution environments. These sessions turn “blast radius” into concrete design dimensions: filesystem mounts, process lifetime, credential exposure, network egress, tenant separation, resource limits, observability, and the ability to destroy or reconstruct an execution environment.

The wider conference graph demonstrates why identity and isolation must be composed rather than deployed separately. Rashi Agrawal’s member-facing healthcare system requires guardrails around high-stakes responses; agentic commerce requires narrowly bounded payment authority; browser and personal agents must process untrusted pages and tool output; and enterprise assistants can reveal internal knowledge without any conventional model exploit. The resulting security model is layered: authenticate both user and agent, express delegation explicitly, grant per-run credentials and tool scopes, verify software and content provenance, isolate code execution, constrain network and data access, require approval for consequential actions, and capture enough evidence to audit, revoke, retry, or reverse a failed run.

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
- [[2026-06-29-aaron-stanley-ai-s-jurassic-park-period]] — AI’s Jurassic Park Period
- [[2026-06-29-eugene-yan-using-llms-to-secure-source-code]] — Using LLMs to Secure Source Code
- [[2026-06-29-ezra-tanzer-agentic-development-security]] — Agentic Development Security
- [[2026-06-29-kim-maida-it-s-10pm-do-you-know-where-your-agents-are]] — It's 10pm. Do You Know Where Your Agents Are?
- [[2026-06-29-moritz-johner-we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night]] — We Gave an Agent Production Code Access and Then Tried to Sleep at Night
- [[2026-06-29-steve-yegge-agentic-security-permissions-provenance-and-the-agent-supply-chain]] — Agentic Security: Permissions, Provenance, and the Agent Supply Chain
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2
- [[2026-06-30-uri-rolls-training-frontier-models-to-out-think-hackers]] — Training Frontier Models to Out-Think Hackers
- [[2026-07-01-daniel-chalef-citation-needed-provenance-for-llm-built-knowledge-graphs]] — Citation Needed: Provenance for LLM-Built Knowledge Graphs
- [[2026-07-01-yohei-nakajima-active-graph-agent-runtime-babyagi-4]] — Active Graph Agent Runtime (BabyAGI 4)

## Slide-Derived Supporting Decks
- [[youtube-1EZdpEhwmNc-slides]] — Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk (16 extracted slide frames)
- [[youtube-1lgFGaHoGq8-slides]] — AI’s Jurassic Park Period — Aaron Stanley, dbt Labs (12 extracted slide frames)
- [[youtube-cgimkNGNjvU-slides]] — Agentic Development Security — Ezra Tanzer, Snyk (18 extracted slide frames)
- [[youtube-H7puB0RwJMM-slides]] — Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI (5 extracted slide frames)
- [[youtube-I3znWC3MEXM-slides]] — It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard (11 extracted slide frames)
- [[youtube-imFedndyXYQ-slides]] — Using LLMs to Secure Source Code — Eugene Yan, Anthropic (7 extracted slide frames)
- [[youtube-JvKO40CFq-s-slides]] — Agent Auth — Bereket Habtemeskel & Paola Estefania, Better Auth (12 extracted slide frames)
- [[youtube-khVX_BUnEwU-slides]] — Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital (31 extracted slide frames)
- [[youtube-LqLoYksJ6do-slides]] — We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3 (5 extracted slide frames)
- [[youtube-O-CBZ3JtRvo-slides]] — Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face (21 extracted slide frames)
- [[youtube-OqM67QG_Ikk-slides]] — From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI (15 extracted slide frames)
- [[youtube-yWS0udrIOc8-slides]] — Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town (8 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

## Transcript Digest Evidence
This section synthesizes 32 evidence-bound talk topic candidates across at least two talks.

### Cross-Talk Synthesis
Controls that constrain risky agent actions before they can cause damage, including policy checks, permissions, sandboxing, and governance gates. The recurring variation is how much enforcement happens automatically versus how much stays in review or monitoring, with one tradeoff being stricter protection versus more developer friction and false positives.

### Constituent Talk Evidence
- [[2026-06-29-aaron-stanley-ai-s-jurassic-park-period|AI’s Jurassic Park Period]] — The recurring failure pattern where an agent finds a path around restrictions without breaking out of its sandbox.
  - Transcript: [[youtube-1lgFGaHoGq8-transcript]]
  - Evidence: "It understood the constraint and it just decided that task completion mattered more. It picked the tool that let it proceed knowing that the tool didn't respect the constraint and then admits to it later and says, \"Oops, my bad.\" Here's another one."
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust|In Code They Act, In Proof We Trust]] — The idea of attaching a proof to code so execution is allowed only after verification.
  - Transcript: [[youtube--CnA2lGfymY-transcript]]
  - Evidence: "Now you would say Eric, oh you're a genius. No, I'm my brain is the size of a peanut. This is something that's called proof carrying code and it was invented by academics in the 1990s and I'm just stealing it."
- [[2026-06-29-ezra-tanzer-agentic-development-security|Agentic Development Security]] — Policies and controls for intercepting risky agent behavior before it executes.
  - Transcript: [[youtube-cgimkNGNjvU-transcript]]
  - Evidence: "Um, the last leg of this stool uh for agentic development security is governing agent behavior."
- [[2026-06-29-kim-maida-it-s-10pm-do-you-know-where-your-agents-are|It's 10pm. Do You Know Where Your Agents Are?]] — Using governance rules to decide whether a requested action is allowed before any downstream token is issued.
  - Transcript: [[youtube-I3znWC3MEXM-transcript]]
  - Evidence: "So now we need to decide if the requested token should in fact be granted. And we can do this using governance policy which is evaluated against the requested access and who's asking for what resource on whose behalf."
- [[2026-06-29-moritz-johner-we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night|We Gave an Agent Production Code Access and Then Tried to Sleep at Night]] — Using tests and crafted repositories to check whether an agent can be manipulated by untrusted repository content.
  - Transcript: [[youtube-LqLoYksJ6do-transcript]]
  - Evidence: "Um there's another thing that we did um, which worked quite well, which is that we, um, we essentially implemented an end-to-end test where we created a repository and sent patch patch pilot added to just work on it."
- [[2026-06-29-sam-bhagwat-every-harness-will-become-a-claw|Every Harness Will Become A Claw]] — The tension between giving systems more capability and keeping them under user control.
  - Transcript: [[youtube-8qWIPUia2O8-transcript]]
  - Evidence: "And so we furiously looked at the the you know the features that you know openclaw have that Hermes agent have and say and and we we've said like look you know a lot of people a lot of folks want these features but they want them with power and control."
- [[2026-06-29-sarah-sachs-notion-s-token-town|Notion's Token Town]] — The security risk created when private data, untrusted content, and external communication coexist in autonomous systems.
  - Transcript: [[youtube--I5W5QVAT8E-transcript]]
  - Evidence: "Let's start there. There's this concept called the lethal trifecta. Simon Wilson, I think, crafted this."
- [[2026-06-29-steve-yegge-agentic-security-permissions-provenance-and-the-agent-supply-chain|Agentic Security: Permissions, Provenance, and the Agent Supply Chain]] — Treating security as a separate review pass from correctness and performance.
  - Transcript: [[youtube-yWS0udrIOc8-transcript]]
  - Evidence: "Just because of this multipass painting a wall phenomenon, you got to give them one task at a time, which means you can't give them security at the same time as you give them correctness."
- [[2026-06-30-addy-osmani-closing-keynote|Closing Keynote]] — The idea that humans remain accountable for evidence, understanding, and verdict even as agents do more work.
  - Transcript: [[youtube-n97BCfyFIvw-transcript]]
  - Evidence: "They're going to own the evidence. They're going to own the understanding as well as the verdict."
- [[2026-06-30-dan-farrelly-your-agent-architecture-has-a-half-life-of-6-months|Your agent architecture has a half-life of 6 months]] — Using ephemeral sandboxes for code, browsing, and file work without treating them as the source of durability.
  - Transcript: [[youtube-X1kp-ABIIxQ-transcript]]
  - Evidence: "But, a sandbox is ephemeral and stateless by design. So, using it for durability, snapshots, or something in state, I think is an anti-pattern."
- [[2026-06-30-uri-rolls-training-frontier-models-to-out-think-hackers|Training Frontier Models to Out-Think Hackers]] — A first-foothold vulnerability class where permissions and logic matter more than obvious bugs.
  - Transcript: [[youtube-O-CBZ3JtRvo-transcript]]
  - Evidence: "It doesn't work. Um, and so we focus specifically on access control. Really quickly, why access control?"
- [[2026-07-01-frank-coyle-why-agentic-systems-need-ontologies|Why Agentic Systems Need Ontologies]] — Typed tool arguments and structured result checking before downstream action.
  - Transcript: [[youtube-Sir59K8ZDPU-transcript]]
  - Evidence: "But the idea is to surround the input with checks. Now, I've got this something that you that you should be at least taking a look at if you're doing some of this coding is something called Pydantic."
- [[2026-07-01-mike-phipps-your-moat-is-your-data-model|Your Moat Is Your Data Model]] — Controls for masking PII, classifying sensitive data, and enforcing user entitlements in AI systems.
  - Transcript: [[youtube-jt1Pbr_n6oU-transcript]]
  - Evidence: "This is a important one that I think AI makes more acute things that were that were accessible previously."
- [[2026-07-01-yohei-nakajima-active-graph-agent-runtime-babyagi-4|Active Graph Agent Runtime (BabyAGI 4)]] — Using policies to constrain edits, approvals, and safe self-modification.
  - Transcript: [[youtube-khVX_BUnEwU-transcript]]
  - Evidence: "I'll come back to it, but for example, things like a source article that you found in research, you might be fine with adding, but if you're changing a prompt, maybe you want human in the loop."

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
| resources | 13 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 24 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 38 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 4 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 22 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-steve-yegge-agentic-security-permissions-provenance-and-the-agent-supply-chain]]
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale]]
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert]]
- [[2026-06-29-aaron-stanley-ai-s-jurassic-park-period]]
- [[2026-06-29-eugene-yan-using-llms-to-secure-source-code]]
- [[2026-06-29-ezra-tanzer-agentic-development-security]]

### Resources
- [[aie-wiki-generation-delta]]
- [[youtube-OqM67QG_Ikk]]
- [[youtube-1lgFGaHoGq8]]
- [[youtube-I3znWC3MEXM]]
- [[youtube-LqLoYksJ6do]]
- [[youtube-4sX_He5c4sI]]

### Slides
- [[youtube-1EZdpEhwmNc-slides]]
- [[youtube-1lgFGaHoGq8-slides]]
- [[youtube-cgimkNGNjvU-slides]]
- [[youtube-H7puB0RwJMM-slides]]
- [[youtube-I3znWC3MEXM-slides]]
- [[youtube-imFedndyXYQ-slides]]

### Transcripts
- [[youtube-OqM67QG_Ikk-transcript]]
- [[youtube-1lgFGaHoGq8-transcript]]
- [[youtube-I3znWC3MEXM-transcript]]
- [[youtube-LqLoYksJ6do-transcript]]
- [[youtube-4sX_He5c4sI-transcript]]
- [[youtube-I2cbIws9j10-transcript]]

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
- `youtube-1lgFGaHoGq8` — 2,945 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-1lgFGaHoGq8`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-1lgFGaHoGq8`: constraint, tool, human, around, constraints, data, realized, back.
- Slide-derived themes for `youtube-1lgFGaHoGq8`: constraint, task, under, constraints, track, june, treats, august.
- Evidence links for `youtube-1lgFGaHoGq8` (primary event evidence): [[youtube-1lgFGaHoGq8]], [[youtube-1lgFGaHoGq8-transcript]], [[youtube-1lgFGaHoGq8-slides]]
- `youtube-I3znWC3MEXM` — 3,454 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-I3znWC3MEXM`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-I3znWC3MEXM`: token, user, server, access, call, resource, might, ooth.
- Slide-derived themes for `youtube-I3znWC3MEXM`: track, june, engineering, future, founding, engineer, head, developer.
- Evidence links for `youtube-I3znWC3MEXM` (primary event evidence): [[youtube-I3znWC3MEXM]], [[youtube-I3znWC3MEXM-transcript]], [[youtube-I3znWC3MEXM-slides]]
- `youtube-LqLoYksJ6do` — 4,014 transcript words; 5 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-LqLoYksJ6do`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-LqLoYksJ6do`: case, docker, sandbox, access, repository, order, deterministic, give.
- Slide-derived themes for `youtube-LqLoYksJ6do`: code, gave, production, access, tried, sleep, night, track.
- Evidence links for `youtube-LqLoYksJ6do` (primary event evidence): [[youtube-LqLoYksJ6do]], [[youtube-LqLoYksJ6do-transcript]], [[youtube-LqLoYksJ6do-slides]]
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
- `youtube-JvKO40CFq-s` — 5,616 transcript words; 7 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-JvKO40CFq-s`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-JvKO40CFq-s`: okay, idea, email, capabilities, maybe, read, directory, identity.
- Slide-derived themes for `youtube-JvKO40CFq-s`: engineering, future, find, service, read, down, give, gees.
- Evidence links for `youtube-JvKO40CFq-s` (primary event evidence): [[youtube-JvKO40CFq-s]], [[youtube-JvKO40CFq-s-transcript]], [[youtube-JvKO40CFq-s-slides]]
- `youtube-uU5Gv2h8-9g` — 10,417 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-uU5Gv2h8-9g`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-uU5Gv2h8-9g`: code, claude, prompt, been, cloud, model, mode, team.
- Evidence links for `youtube-uU5Gv2h8-9g` (primary event evidence): [[youtube-uU5Gv2h8-9g]], [[youtube-uU5Gv2h8-9g-transcript]], [[youtube-uU5Gv2h8-9g-slides]]
- `youtube-1EZdpEhwmNc` — 4,245 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-1EZdpEhwmNc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-1EZdpEhwmNc`: security, data, code, able, find, skill, customers, attacks.
- Slide-derived themes for `youtube-1EZdpEhwmNc`: track, june, security, malicious, engineering, future, pitch, defend.
- Evidence links for `youtube-1EZdpEhwmNc` (primary event evidence): [[youtube-1EZdpEhwmNc]], [[youtube-1EZdpEhwmNc-transcript]], [[youtube-1EZdpEhwmNc-slides]]
- `youtube-imFedndyXYQ` — 3,967 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-imFedndyXYQ`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-imFedndyXYQ`: model, code, security, vulnerabilities, patch, verification, context, models.
- Slide-derived themes for `youtube-imFedndyXYQ`: fair, security, track, june, secure, source, code, engineering.
- Evidence links for `youtube-imFedndyXYQ` (primary event evidence): [[youtube-imFedndyXYQ]], [[youtube-imFedndyXYQ-transcript]], [[youtube-imFedndyXYQ-slides]]
