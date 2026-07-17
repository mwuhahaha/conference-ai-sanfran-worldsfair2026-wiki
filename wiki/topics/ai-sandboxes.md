---
title: "AI Sandboxes"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
sourceAssessment:
  schemaVersion: 1
  claimId: claim:5b206028141586ca2746aff32d9733f1bb75c7de22b847a403790c2fec3af04b
  subjectId: concept:ai-sandboxes
  domain: topics page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-17T13:24:54.408152Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-youtube--CnA2lGfymY
  - source:official-wf26-youtube-1P1hJ36rxM0
  - source:official-wf26-youtube-OqM67QG_Ikk
  - source:official-wf26-youtube-ZSQb5fzRFPw
  - source:official-wf26-youtube-ZyIoTOAbRfs
  - source:official-wf26-youtube-pMggiOb18tc
sourceAssessmentBodySha256: sha256:339952c19a8036959203d1d8b8212c666c5ed08baa4b4f980eb62cf80817ee6d
---
# AI Sandboxes

## Overview
AI sandboxes are controlled execution environments where agents can run code, browse, inspect files, call tools, or manipulate artifacts without putting the host system at unnecessary risk. A sandbox gives the agent enough power to do real work while limiting filesystem, network, credential, and process access.

## Conference Context
The pattern comes from operating-system isolation, browser sandboxes, CI runners, notebooks, container platforms, and secure code-execution services. Agentic coding and computer-use systems made sandboxing a default requirement rather than a specialty feature.

## How This Theme Evolved
- **World's Fair 2024 (local comparison fixture):** Human oversight and infrastructure were broad safeguards around AI systems.
- **Miami 2026 (public comparison wiki):** Remote agents and sandboxed compute made runtime boundaries part of developer workflow.
- **World's Fair 2025 (local comparison fixture):** The comparison corpus foregrounded containment, identity, OAuth, access control, and code-execution safety.
- **World's Fair 2026 (current event synthesis backed by linked local evidence):** The linked conference graph treats sandboxes, tool permissions, provenance, and eval gates as one operational control surface.

**Confidence:** high.
**Boundary:** Earlier event wikis are comparison context only. They are not primary evidence for World's Fair 2026 claims, and no local fixture is represented as a public live site.
**Comparison source:** [[aie-wiki-generation-delta]].

## Significance
Agents need to experiment, test, and inspect state. Sandboxes let them do that while containing failures, malicious inputs, runaway processes, and accidental destructive changes.

## Why This Matters Now
Agents increasingly execute code and use credentials rather than only returning text, so correctness and blast-radius control must be designed together.

**WF26 evidence gate:** this section was emitted only because the page links to configured local evidence. Relevant configured evidence: [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale]], [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert]].

**Confidence:** high. Comparison history is context; linked WF26 pages remain the evidence for current-event claims.

## Applied Use
Choose isolation based on risk: separate processes for low-risk tasks, containers or microVMs for untrusted code, and policy-controlled network and secret access for production work. Capture logs, diffs, artifacts, and resource usage so human operators can review what happened.

They are useful in coding assistants, data-analysis agents, browser agents, app builders, test runners, educational tools, and any system that executes generated code or commands.

Use a sandbox whenever an agent can execute code, inspect user files, download dependencies, browse unknown sites, or run untrusted scripts. Loosen limits only after the workflow and threat model are well understood.

## Active Use Cases
- Running generated code and tests before suggesting a patch.
- Browser or computer-use automation with constrained state.
- Temporary workspaces for data analysis and document transformation.
- Reproducible agent task environments for evaluations.

## Practical Lesson
Give each run the minimum tools, credentials, network reach, filesystem scope, and lifetime it needs; capture actions and outputs so approval and incident review use the same evidence trail.

**Confidence:** high. Treat this as synthesis derived from the linked evidence graph, not as an official schedule claim.

## Slide-Derived Scheduled Session Signals
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]] — In Code They Act, In Proof We Trust
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2
- [[2026-06-30-benoit-schillings-research-to-reality-with-google-deepmind]] — Research to Reality with Google DeepMind
- [[2026-06-30-sean-cai-state-of-data]] — State of Data

## Slide-Derived Supporting Decks
- [[youtube--CnA2lGfymY-slides]] — "I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox (32 extracted slide frames)
- [[youtube-1P1hJ36rxM0-slides]] — Research to Reality with Google DeepMind — Benoit Schillings, Google DeepMind (15 extracted slide frames)
- [[youtube-OqM67QG_Ikk-slides]] — From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI (15 extracted slide frames)
- [[youtube-ZSQb5fzRFPw-slides]] —  (17 extracted slide frames)
- [[youtube-ZyIoTOAbRfs-slides]] — State of Data — Sean Cai, Independent / State of Data (10 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

## Connections
- [[2026-06-30-pierluca-d-oro-computer-use-at-the-edge-of-the-statistical-precipice]] — Computer Use at the Edge of the Statistical Precipice; [[pierluca-d-oro|Pierluca D'Oro]] (Day 3 — Session Day 2 · 11:10am-11:30am · Computer Use; official schedule)
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale]] — Sandboxes Aren't Optional: Runtime Isolation Patterns for Coding Agents at Scale; [[robert-brennan|Robert Brennan]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Sandbox & Platform Engineering; official schedule)
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert]] — Your agent needs a sandbox, not a desert; [[samuel-colvin|Samuel Colvin]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · Sandbox & Platform Engineering; official schedule)
- [[2026-06-29-tushar-jain-unlock-agent-autonomy-the-runtime-for-ai-native-systems]] — Unlock Agent Autonomy: The Runtime for AI-Native Systems; [[tushar-jain|Tushar Jain]] (Day 2 — Session Day 1 · 3:45pm-4:05pm · AI Architects: Show my Workflow; official schedule)
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1; [[abhishek-bhardwaj|Abhishek Bhardwaj]] (Day 3 — Session Day 2 · 1:30pm-1:50pm · Sandbox & Platform Engineering; official schedule)
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2; [[abhishek-bhardwaj|Abhishek Bhardwaj]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Sandbox & Platform Engineering; official schedule)
- [[2026-06-30-ivan-burazin-kubernetes-is-not-your-sandbox]] — Kubernetes Is Not Your Sandbox; [[ivan-burazin|Ivan Burazin]] (Day 3 — Session Day 2 · 11:40am-12:00pm · Sandbox & Platform Engineering; official schedule)
- [[2026-06-30-kevin-orellana-1-000-agent-tasks-in-a-sandbox-what-breaks-when-llms-write-and-run-code]] — 1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Write and Run Code; [[kevin-orellana|Kevin Orellana]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Sandbox & Platform Engineering; official schedule)
- [[2026-06-30-adam-azzam-don-t-build-agents-build-environments]] — Don’t build agents, build environments; [[adam-azzam|Adam Azzam]] (Day 3 — Session Day 2 · 10:45am-11:05am · Sandbox & Platform Engineering; official schedule)
- [[2026-06-29-matt-brockman-how-i-learned-to-stop-worrying-and-love-the-sandbox]] — How I learned to stop worrying and love the sandbox; [[matt-brockman|Matt Brockman]] (Day 1 — Workshop Day · 11:05am-12:05pm · Workshops Day 1; official schedule)
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]] — The Golden Age of AI Engineering; [[alexander-embiricos|Alexander Embiricos]], [[romain-huet|Romain Huet]] (Day 2 — Session Day 1 · 9:25am-9:45am · Software Factories; verified event YouTube resource; via [[youtube-pMggiOb18tc]])
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]] — MCP Apps - Extending the frontier; [[liad-yosef|Liad Yosef]], [[ido-salomon|Ido Salomon]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Context Engineering; verified event YouTube resource; via [[youtube-o-zkvb0iFDQ]])
- [[2026-07-01-arun-sekhar-blast-radius-zero-one-command-openclaw-sandboxes-in-the-cloud]] — Blast Radius Zero: One‑Command OpenClaw Sandboxes in the Cloud; [[arun-sekhar|Arun Sekhar]] (Day 4 — Session Day 3 · 1:55pm-2:15pm · Track M; official schedule)
- [[2026-06-29-derek-meegan-deploying-browser-agents-at-scale]] — Deploying browser agents at scale; [[derek-meegan|Derek Meegan]] (Day 2 — Session Day 1 · 1:55pm-2:15pm · Expo Stage 4 SE; official schedule)
- [[2026-06-29-ross-taylor-scaling-to-long-horizons-algorithms-environments-compute]] — Scaling to Long-Horizons: Algorithms, Environments, Compute; [[ross-taylor|Ross Taylor]], [[chengxi-taylor|Chengxi Taylor]] (Day 2 — Session Day 1 · 2:25pm-2:45pm · Data Quality; official schedule)
- [[2026-07-01-miguel-gonz-lez-fern-ndez-the-art-of-building-verifiers-for-computer-use-agents]] — The Art of Building Verifiers for Computer Use Agents; [[miguel-gonz-lez-fern-ndez|Miguel González Fernández]], [[corby-rosset|Corby Rosset]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Expo Stage 1 NE; official schedule)
- [[2026-07-01-rowan-christmas-yolo-mode-safely-microvm-sandboxes-for-any-agent]] — YOLO Mode, Safely: microVM Sandboxes for Any Agent; [[rowan-christmas|Rowan Christmas]] (Day 4 — Session Day 3 · 1:30pm-1:50pm · Expo Stage 2 NW; official schedule)
- [[2026-06-29-rayan-garg-rethinking-environments-for-long-horizon-work]] — Rethinking Environments for Long Horizon Work; [[rayan-garg|Rayan Garg]] (Day 2 — Session Day 1 · 11:40am-12:00pm · Data Quality; official schedule)
- [[2026-06-29-mahesh-sathiamoorthy-data-and-environment-curation-for-post-training-llms]] — Data and Environment Curation for Post-training LLMs; [[mahesh-sathiamoorthy|Mahesh Sathiamoorthy]] (Day 2 — Session Day 1 · 3:45pm-4:05pm · Data Quality; official schedule)
- [[2026-06-30-tina-manghnani-from-framework-to-runtime-running-agents-with-foundry-agent-service]] — From framework to runtime: running agents with Foundry Agent Service; [[tina-manghnani|Tina Manghnani]], [[keiji-kanazawa|Keiji Kanazawa]] (Day 3 — Session Day 2 · 10:45am-11:05am · Track M; official schedule)
- [[2026-06-30-viren-baraiya-harnessing-agents-the-durable-runtime-for-dynamic-workflows]] — Harnessing Agents: The Durable Runtime for Dynamic Workflows; [[viren-baraiya|Viren Baraiya]] (Day 3 — Session Day 2 · 11:10am-11:30am · Expo Stage 1 NE; official schedule)
- [[2026-07-01-yohei-nakajima-active-graph-agent-runtime-babyagi-4]] — Active Graph Agent Runtime (BabyAGI 4); [[yohei-nakajima|Yohei Nakajima]] (Day 4 — Session Day 3 · 11:10am-11:30am · Graphs; official schedule)
- [[2026-06-29-ang-li-the-autonomous-computer-full-stack-infrastructure-for-computer-use-agents]] — The Autonomous Computer: Full-stack Infrastructure for Computer Use Agents; [[ang-li|Ang Li]] (Day 1 — Workshop Day · 4:30pm-5:30pm · Workshops Day 1; official schedule)
- [[2026-06-30-philipp-schmid-why-agents-should-have-their-own-sandbox]] — Why Agents Should Have Their Own Sandbox; [[philipp-schmid|Philipp Schmid]] (Day 3 — Session Day 2 · 1:30pm-1:50pm · Expo Stage 1; official schedule)

- [[john-craft|John Craft]]
- [[abhishek-bhardwaj|Abhishek Bhardwaj]]
- [[arun-sekhar|Arun Sekhar]]
- [[will-brown|Will Brown]]
- [[tina-manghnani|Tina Manghnani]]
- [[pierluca-d-oro|Pierluca D'Oro]]
- [[robert-brennan|Robert Brennan]]
- [[samuel-colvin|Samuel Colvin]]
- [[tushar-jain|Tushar Jain]]
- [[ivan-burazin|Ivan Burazin]]
- [[kevin-orellana|Kevin Orellana]]
- [[adam-azzam|Adam Azzam]]
- [[matt-brockman|Matt Brockman]]
- [[alexander-embiricos|Alexander Embiricos]]
- [[romain-huet|Romain Huet]]
- [[liad-yosef|Liad Yosef]]
- [[ido-salomon|Ido Salomon]]
- [[derek-meegan|Derek Meegan]]
- [[ross-taylor|Ross Taylor]]
- [[chengxi-taylor|Chengxi Taylor]]
- [[miguel-gonz-lez-fern-ndez|Miguel González Fernández]]
- [[corby-rosset|Corby Rosset]]
- [[rowan-christmas|Rowan Christmas]]
- [[rayan-garg|Rayan Garg]]

- [[docker|Docker]]
- [[microsoft|Microsoft]]
- [[openai|OpenAI]]
- [[browserbase|Browserbase]]
- [[amazon-agi-lab|Amazon AGI Lab]]
- [[prime-intellect|Prime Intellect]]
- [[mcp-apps|MCP Apps]]
- [[cua|Cua]]
- [[typedef|typedef]]
- [[oxylabs|Oxylabs]]
- [[amazon-web-services|Amazon Web Services]]
- [[navan|Navan]]
- [[uber|Uber]]
- [[warp|Warp]]
- [[meta|Meta]]
- [[yugabyte|Yugabyte]]
- [[programma-labs|Programma Labs]]
- [[openhands|OpenHands]]

- [[mahesh-sathiamoorthy|Mahesh Sathiamoorthy]]

- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]] — The Golden Age of AI Engineering; [[alexander-embiricos|Alexander Embiricos]], [[romain-huet|Romain Huet]] (Day 2 — Session Day 1 · 9:25am-9:45am · Software Factories; related YouTube resource; via [[youtube-pMggiOb18tc]])
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]] — MCP Apps - Extending the frontier; [[liad-yosef|Liad Yosef]], [[ido-salomon|Ido Salomon]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Context Engineering; related YouTube resource; via [[youtube-o-zkvb0iFDQ]])

- [[youtube-4kYl2_mqmnQ-slides]] — I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON (10 extracted slide frames)
- [[youtube-qdZzND79mcg-slides]] — Beyond the Harness: A Journey Towards Adaptative Engineering - Rajiv Chandegra, Annicha Labs (16 extracted slide frames)
- [[youtube-2IxD9OB3XuQ-slides]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI (24 extracted slide frames)
- [[youtube-sAOBXCDiDOs-slides]] — MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc (18 extracted slide frames)
- [[youtube-vljxQZfJ9wY-slides]] — Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs (12 extracted slide frames)

- [[2026-06-29-du-an-lightfoot-agents-that-own-their-inference-building-production-ai-agents-on-dedicated-gpus]] — Agents That Own Their Inference: Building Production AI Agents on Dedicated GPUs; [[du-an-lightfoot|Du'an Lightfoot]] (Day 1 — Workshop Day · 9:00am-11:00am · Track 7; related YouTube resource; via [[youtube-wFTVEDYVJT0]])
- [[2026-06-30-paul-klein-iv-bringing-agents-onto-the-world-wide-web]] — Bringing agents onto the world wide web; [[paul-klein-iv|Paul Klein IV]] (Day 3 — Session Day 2 · 11:40am-12:00pm · Computer Use; official schedule)

- [[keiji-kanazawa|Keiji Kanazawa]]
- [[viren-baraiya|Viren Baraiya]]
- [[yohei-nakajima|Yohei Nakajima]]
- [[ang-li|Ang Li]]

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 45 | Related pages outside the main evidence categories. |
| resources | 7 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 13 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 29 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 5 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 2 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale]]
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert]]
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]]
- [[2026-06-30-benoit-schillings-research-to-reality-with-google-deepmind]]

### Resources
- [[aie-wiki-generation-delta]]
- [[youtube-pMggiOb18tc]]
- [[youtube-o-zkvb0iFDQ]]
- [[youtube-wFTVEDYVJT0]]
- [[youtube-OqM67QG_Ikk]]
- [[youtube-wsFd22SL1s8]]

### Slides
- [[youtube--CnA2lGfymY-slides]]
- [[youtube-1P1hJ36rxM0-slides]]
- [[youtube-OqM67QG_Ikk-slides]]
- [[youtube-ZSQb5fzRFPw-slides]]
- [[youtube-ZyIoTOAbRfs-slides]]
- [[youtube-4kYl2_mqmnQ-slides]]

### Transcripts
- [[youtube-OqM67QG_Ikk-transcript]]
- [[youtube-4kYl2_mqmnQ-transcript]]

### Tools
- [[docker]]
- [[browserbase]]
- [[prime-intellect]]
- [[mcp-apps]]
- [[openhands]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

Current media support is attributable to one official recording; it is context for the theme rather than independent corroboration of every claim.

### Linked Sessions
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale|Sandboxes Aren't Optional: Runtime Isolation Patterns for Coding Agents at Scale]]
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert|Your agent needs a sandbox, not a desert]]
- [[2026-06-30-pierluca-d-oro-computer-use-at-the-edge-of-the-statistical-precipice|Computer Use at the Edge of the Statistical Precipice]]
- [[2026-06-29-tushar-jain-unlock-agent-autonomy-the-runtime-for-ai-native-systems|Unlock Agent Autonomy: The Runtime for AI-Native Systems]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1']]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2']]
- [[2026-06-30-ivan-burazin-kubernetes-is-not-your-sandbox|Kubernetes Is Not Your Sandbox]]
- [[2026-06-30-kevin-orellana-1-000-agent-tasks-in-a-sandbox-what-breaks-when-llms-write-and-run-code|1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Write and Run Code]]
- [[2026-06-30-adam-azzam-don-t-build-agents-build-environments|Don’t build agents, build environments]]
- [[2026-06-29-matt-brockman-how-i-learned-to-stop-worrying-and-love-the-sandbox|How I learned to stop worrying and love the sandbox]]

### Media Signals
- `youtube-OqM67QG_Ikk` — 7,738 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-OqM67QG_Ikk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-OqM67QG_Ikk`: kernel, many, system, code, host, guest, block, running.
- Slide-derived themes for `youtube-OqM67QG_Ikk`: engineering, sandbox, platform, track, july, security, fork, fleet.
- Evidence links for `youtube-OqM67QG_Ikk` (primary event evidence): [[youtube-OqM67QG_Ikk]], [[youtube-OqM67QG_Ikk-transcript]], [[youtube-OqM67QG_Ikk-slides]]
- `youtube-wsFd22SL1s8` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-wsFd22SL1s8`: clone, flask, project, code, create, scratch, systems, chat.
- Evidence links for `youtube-wsFd22SL1s8` (supporting context only): [[youtube-wsFd22SL1s8]], [[youtube-wsFd22SL1s8-slides]], [[youtube-wsFd22SL1s8-dense-slides]], [[youtube-wsFd22SL1s8-reconstructed-slides]]
- `youtube-4kYl2_mqmnQ` — 4,930 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-4kYl2_mqmnQ`: machine, context, machines, linux, back, whole, point, each.
- Slide-derived themes for `youtube-4kYl2_mqmnQ`: sleeps, headless, dispatch, normal, default, coding, tasks, machines.
- Evidence links for `youtube-4kYl2_mqmnQ` (supporting context only): [[youtube-4kYl2_mqmnQ]], [[youtube-4kYl2_mqmnQ-transcript]], [[youtube-4kYl2_mqmnQ-slides]]
