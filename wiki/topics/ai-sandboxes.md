---
title: AI Sandboxes
category: topics
sourceLabels:
  - Slide/video-derived supporting context
last_auto_summarized: '2026-07-19T01:15:51.606Z'
sourceAssessment:
  schemaVersion: 1
  claimId: claim:5b206028141586ca2746aff32d9733f1bb75c7de22b847a403790c2fec3af04b
  subjectId: concept:ai-sandboxes
  domain: topics page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-24T00:00:00.000000Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-youtube--CnA2lGfymY
  - source:official-wf26-youtube-1EZdpEhwmNc
  - source:official-wf26-youtube-1P1hJ36rxM0
  - source:official-wf26-youtube-8qWIPUia2O8
  - source:official-wf26-youtube-OqM67QG_Ikk
  - source:official-wf26-youtube-X1kp-ABIIxQ
  - source:official-wf26-youtube-ZSQb5fzRFPw
  - source:official-wf26-youtube-ZyIoTOAbRfs
  - source:official-wf26-youtube-imFedndyXYQ
  - source:official-wf26-youtube-jRCpXUjz4CI
  - source:official-wf26-youtube-pMggiOb18tc
sourceAssessmentBodySha256: sha256:e08cd0f6fc9f27cd4d845e4b5bae1011c525c6cbae9b58bfce4d723c05d2cde4
---
# AI Sandboxes

## Overview
AI sandboxes are controlled execution environments in which agents can write and run code, inspect files, install dependencies, browse, and produce artifacts without inheriting unrestricted access to the host. The World’s Fair 2026 material treats a sandbox as an execution control plane, not merely a container: process isolation must be combined with scoped filesystems, explicit network and credential policy, resource limits, action logs, artifact capture, reproducible state, and reliable teardown.

The Sandbox & Platform Engineering track develops this boundary from several concrete angles. Abhishek Bhardwaj’s two-part OpenAI session traces sandbox infrastructure from `fork()`-level host and guest separation to fleet-scale operation; its official recording, 7,738-word transcript, and extracted slides provide the page’s strongest linked media evidence. Ivan Burazin’s “Kubernetes Is Not Your Sandbox” separates workload orchestration from the security boundary required for untrusted agent code. Kevin Orellana examines failures across 1,000 AWS code-writing tasks, Adam Azzam argues that better environments can matter more than additional agent-framework machinery, and Robert Brennan connects runtime isolation to operating OpenHands coding agents at scale. Samuel Colvin frames sandbox design as a product tradeoff between useful capabilities and an unusably restricted “desert,” while Matt Brockman’s E2B workshop turns those principles into hands-on implementation.

The surrounding conference graph broadens sandboxing beyond coding assistants. Tushar Jain ties agent autonomy to Docker-based runtime infrastructure; Derek Meegan applies constrained execution to browser-agent fleets; Arun Sekhar presents one-command cloud sandboxes organized around a near-zero blast radius; and Rowan Christmas focuses on microVM isolation for arbitrary agents. Pierluca D’Oro and Ang Li extend the environment problem to computer use, where agents interact with graphical systems rather than only shells. Miguel González Fernández and Corby Rosset show why those environments need task-specific verifiers, while Erik Meijer’s proof-oriented harness framing supplies the acceptance boundary: completing an action is not proof that its result is correct or safe. Sessions on long-horizon environments, durable runtimes, autonomous computers, dedicated infrastructure, post-training data curation, and browser automation further connect sandbox quality to persistence, state fidelity, reproducibility, and recovery.

Taken together, the linked material defines sandboxing as the layer that mediates autonomous software’s ability to affect the world. Orchestration decides where work runs; isolation limits what a compromised or mistaken agent can reach; filesystem, network, and credential policies constrain external effects; logs and captured artifacts establish provenance; and verifiers decide whether outputs may be accepted. The central design choice is therefore not simply process versus container versus microVM, but a risk-specific combination of boundary strength, permitted capabilities, observability, task lifetime, reproducibility, and evidence-based acceptance. The DeepMind, State of Data, multi-machine agent-fleet, and other slide-linked material remains adjacent slide, transcript, or OCR context rather than independent proof of a particular sandbox architecture.

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
- [[2026-06-29-manoj-nair-through-the-ai-fog-the-architectural-decision-the-next-24-months-of-agentic-security-depends-on]] — Through the AI Fog: The architectural decision the next 24 months of agentic security depends on.
- [[2026-06-29-zach-blumenfeld-ai-on-your-lakehouse-context-comes-in-shapes-not-queries]] — AI on Your Lakehouse: Context Comes in Shapes, Not Queries
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]] — From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2
- [[2026-06-30-alex-shaw-everything-is-a-rollout]] — Everything Is a Rollout
- [[2026-06-30-francesco-bonacci-computer-use-2-0-agents-just-got-multi-cursor]] — Computer-Use 2.0: Agents Just Got Multi-Cursor
- [[2026-06-30-sean-cai-state-of-data]] — State of Data

## Slide-Derived Supporting Decks
- [[youtube--CnA2lGfymY-slides]] — "I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox (32 extracted slide frames)
- [[youtube-1EZdpEhwmNc-slides]] — Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk (16 extracted slide frames)
- [[youtube-1P1hJ36rxM0-slides]] — Research to Reality with Google DeepMind — Benoit Schillings, Google DeepMind (15 extracted slide frames)
- [[youtube-jRCpXUjz4CI-slides]] — Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute (32 extracted slide frames)
- [[youtube-kRkcNOsRyYg-slides]] — AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j (32 extracted slide frames)
- [[youtube-OqM67QG_Ikk-slides]] — From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI (15 extracted slide frames)
- [[youtube-ZSQb5fzRFPw-slides]] —  (17 extracted slide frames)
- [[youtube-ZyIoTOAbRfs-slides]] — State of Data — Sean Cai, Independent / State of Data (10 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

## Transcript Digest Evidence
This section synthesizes 11 evidence-bound talk topic candidates across at least two talks.

### Cross-Talk Synthesis
These candidates describe isolated execution environments for agents, ranging from sandbox fleets and snapshot-aware workspaces to stronger containment around code and tool use. The variation is between persistence and isolation: some talks want durable state that survives failures, while others emphasize hard boundaries and reproducible execution above all else.

### Constituent Talk Evidence
- [[2026-06-29-eugene-yan-using-llms-to-secure-source-code|Using LLMs to Secure Source Code]] — Running exploit tests in isolated, reproducible environments to safely validate findings.
  - Transcript: [[youtube-imFedndyXYQ-transcript]]
  - Evidence: "So this isolation doing bad things could be data exfiltration or you know dropping things in production and of course uh you you want all of this to be running in a VM without egress and of of course without your cloud credentials."
- [[2026-06-29-moritz-johner-we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night|We Gave an Agent Production Code Access and Then Tried to Sleep at Night]] — Containing an agent that needs Docker access by moving it into a micro-VM rather than a normal sandbox.
  - Transcript: [[youtube-LqLoYksJ6do-transcript]]
  - Evidence: "So, let me share a design that we came up with, which is still like in its in its infancy."
- [[2026-06-29-sam-bhagwat-every-harness-will-become-a-claw|Every Harness Will Become A Claw]] — Harnesses that run continuously in cloud sandboxes and broader collaboration surfaces.
  - Transcript: [[youtube-8qWIPUia2O8-transcript]]
  - Evidence: "I think this is something we've seen over the last really 3 months. Um, and I think we're all still starting to grapple with what it means, which is this movement from a local harness to a cloud harness where the harness is always on."
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1']] — Saved sandbox state that survives failures and long tasks.
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
  - Evidence: "So, we want to give them durable storage. And so, this this part of the presentation is specifically working on disk storage, not memory persistence, but disk persistence."
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2']] — How to execute agent tool calls and untrusted code securely for product and research workloads.
  - Transcript: [[youtube-OqM67QG_Ikk-transcript]]
  - Evidence: "So, a sandbox is a play an environment in which you can run these tool calls and execute code on behalf of the model securely and it could be on your laptop or it could be on the cloud."
- [[2026-06-30-alex-shaw-everything-is-a-rollout|Everything Is a Rollout]] — Sandboxed task environments that pair instructions with execution space and verification.
  - Transcript: [[youtube-jRCpXUjz4CI-transcript]]
  - Evidence: "So we'll put it into a computer, but we'll put it into a virtual computer. So a sandbox. Um, and then we need some way of telling whether or not the agent actually did the thing that we told it to do in the sandbox within some amount of time or other stopping condition."
- [[2026-06-30-dan-farrelly-your-agent-architecture-has-a-half-life-of-6-months|Your agent architecture has a half-life of 6 months]] — Using ephemeral sandboxes for code, browsing, and file work without treating them as the source of durability.
  - Transcript: [[youtube-X1kp-ABIIxQ-transcript]]
  - Evidence: "But, a sandbox is ephemeral and stateless by design. So, using it for durability, snapshots, or something in state, I think is an anti-pattern."
- [[2026-06-30-francesco-bonacci-computer-use-2-0-agents-just-got-multi-cursor|Computer-Use 2.0: Agents Just Got Multi-Cursor]] — Keeping GPU workers busy by allocating sandboxes from a demand-sized warm pool.
  - Transcript: [[youtube-ZSQb5fzRFPw-transcript]]
  - Evidence: "So um I guess I'll just explain to you orally and what what that is is uh so we have like a a set of GPUs here which all want to use a sandbox and what we will do is that we use a demandbased autoscaler to detect um how many GPUs like currently need a sandbox and we can grow the pool to be that size uh on demand."

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
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]] — MCP Apps - Extending the frontier; [[liad-yosef|Liad Yosef]], [[ido-salomon|Ido Salomon]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Context Engineering; related YouTube resource; via [[youtube-o-zkvb0iFDQ]])
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
| resources | 8 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 17 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 36 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 5 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 8 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale]]
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert]]
- [[2026-06-29-erik-meijer-in-code-they-act-in-proof-we-trust]]
- [[2026-06-29-manoj-nair-through-the-ai-fog-the-architectural-decision-the-next-24-months-of-agentic-security-depends-on]]
- [[2026-06-29-zach-blumenfeld-ai-on-your-lakehouse-context-comes-in-shapes-not-queries]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]]

### Resources
- [[aie-wiki-generation-delta]]
- [[youtube-pMggiOb18tc]]
- [[youtube-o-zkvb0iFDQ]]
- [[youtube-wFTVEDYVJT0]]
- [[youtube-LqLoYksJ6do]]
- [[youtube-OqM67QG_Ikk]]

### Slides
- [[youtube--CnA2lGfymY-slides]]
- [[youtube-1EZdpEhwmNc-slides]]
- [[youtube-1P1hJ36rxM0-slides]]
- [[youtube-jRCpXUjz4CI-slides]]
- [[youtube-kRkcNOsRyYg-slides]]
- [[youtube-OqM67QG_Ikk-slides]]

### Transcripts
- [[youtube-imFedndyXYQ-transcript]]
- [[youtube-LqLoYksJ6do-transcript]]
- [[youtube-8qWIPUia2O8-transcript]]
- [[youtube-OqM67QG_Ikk-transcript]]
- [[youtube-jRCpXUjz4CI-transcript]]
- [[youtube-X1kp-ABIIxQ-transcript]]

### Tools
- [[docker]]
- [[browserbase]]
- [[prime-intellect]]
- [[mcp-apps]]
- [[openhands]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.

### Linked Sessions
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale|Sandboxes Aren't Optional: Runtime Isolation Patterns for Coding Agents at Scale]]
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert|Your agent needs a sandbox, not a desert]]
- [[2026-06-29-eugene-yan-using-llms-to-secure-source-code|Using LLMs to Secure Source Code]]
- [[2026-06-29-moritz-johner-we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night|We Gave an Agent Production Code Access and Then Tried to Sleep at Night]]
- [[2026-06-29-sam-bhagwat-every-harness-will-become-a-claw|Every Harness Will Become A Claw]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1']]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2']]
- [[2026-06-30-alex-shaw-everything-is-a-rollout|Everything Is a Rollout]]
- [[2026-06-30-dan-farrelly-your-agent-architecture-has-a-half-life-of-6-months|Your agent architecture has a half-life of 6 months]]
- [[2026-06-30-francesco-bonacci-computer-use-2-0-agents-just-got-multi-cursor|Computer-Use 2.0: Agents Just Got Multi-Cursor]]

### Media Signals
- `youtube-LqLoYksJ6do` — 4,014 transcript words; 5 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-LqLoYksJ6do`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-LqLoYksJ6do`: case, docker, sandbox, access, repository, order, deterministic, give.
- Slide-derived themes for `youtube-LqLoYksJ6do`: code, gave, production, access, tried, sleep, night, track.
- Evidence links for `youtube-LqLoYksJ6do` (primary event evidence): [[youtube-LqLoYksJ6do]], [[youtube-LqLoYksJ6do-transcript]], [[youtube-LqLoYksJ6do-slides]]
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
