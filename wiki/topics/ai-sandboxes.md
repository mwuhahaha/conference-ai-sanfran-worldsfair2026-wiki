---
title: "AI Sandboxes"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---
# AI Sandboxes

## Overview
AI sandboxes are controlled execution environments where agents can run code, browse, inspect files, call tools, or manipulate artifacts without putting the host system at unnecessary risk. A sandbox gives the agent enough power to do real work while limiting filesystem, network, credential, and process access.

## Conference Context
The pattern comes from operating-system isolation, browser sandboxes, CI runners, notebooks, container platforms, and secure code-execution services. Agentic coding and computer-use systems made sandboxing a default requirement rather than a specialty feature.

## Significance
Agents need to experiment, test, and inspect state. Sandboxes let them do that while containing failures, malicious inputs, runaway processes, and accidental destructive changes.

## Applied Use
Choose isolation based on risk: separate processes for low-risk tasks, containers or microVMs for untrusted code, and policy-controlled network and secret access for production work. Capture logs, diffs, artifacts, and resource usage so human operators can review what happened.

They are useful in coding assistants, data-analysis agents, browser agents, app builders, test runners, educational tools, and any system that executes generated code or commands.

Use a sandbox whenever an agent can execute code, inspect user files, download dependencies, browse unknown sites, or run untrusted scripts. Loosen limits only after the workflow and threat model are well understood.

Choose isolation based on risk: separate processes for low-risk tasks, containers or microVMs for untrusted code, and policy-controlled network and secret access for production work. Capture logs, diffs, artifacts, and resource usage so human operators can review what happened.

They are useful in coding assistants, data-analysis agents, browser agents, app builders, test runners, educational tools, and any system that executes generated code or commands.

Use a sandbox whenever an agent can execute code, inspect user files, download dependencies, browse unknown sites, or run untrusted scripts. Loosen limits only after the workflow and threat model are well understood.

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
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]] — The Golden Age of AI Engineering; [[alexander-embiricos|Alexander Embiricos]], [[romain-huet|Romain Huet]] (Day 2 — Session Day 1 · 9:25am-9:45am · Software Factories; related YouTube resource; via [[youtube-pMggiOb18tc]])
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
- [[liad-yosef|Liad Yosef]]
- [[ido-salomon|Ido Salomon]]
- [[arun-sekhar|Arun Sekhar]]
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
- [[derek-meegan|Derek Meegan]]
- [[ross-taylor|Ross Taylor]]
- [[chengxi-taylor|Chengxi Taylor]]
- [[miguel-gonz-lez-fern-ndez|Miguel González Fernández]]
- [[corby-rosset|Corby Rosset]]
- [[rowan-christmas|Rowan Christmas]]
- [[rayan-garg|Rayan Garg]]
- [[mahesh-sathiamoorthy|Mahesh Sathiamoorthy]]

- [[docker|Docker]]
- [[microsoft|Microsoft]]
- [[openai|OpenAI]]
- [[mcp-apps|MCP Apps]]
- [[browserbase|Browserbase]]
- [[amazon-agi-lab|Amazon AGI Lab]]
- [[cua|Cua]]
- [[typedef|typedef]]
- [[oxylabs|Oxylabs]]
- [[amazon-web-services|Amazon Web Services]]
- [[navan|Navan]]
- [[warp|Warp]]
- [[uber|Uber]]
- [[prime-intellect|Prime Intellect]]
- [[meta|Meta]]
- [[yugabyte|Yugabyte]]
- [[programma-labs|Programma Labs]]
- [[openhands|OpenHands]]

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

## Evidence Graph
### Transcript-backed resources
- [[youtube-Rx8f05JI_WA]] — SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI
- [[youtube-2IxD9OB3XuQ]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI
- [[youtube-SKDJo2CopRs]] — Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare
- [[youtube-JnubYCYunk8]] — Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, ARK
- [[youtube-wFTVEDYVJT0]] — Building Agents with Amazon Nova Act and MCP - Du'An Lightfoot, Amazon (Full Workshop)
- [[youtube-c-2eEv2ou7Y]] — Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic
- [[youtube-TNwJ1LMiENk]] — Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel
- [[youtube-grdoOC1BT1s]] — Think You Can Build a Game with AI? Think Again! - Danielle An & David Hoe, Meta
- [[youtube-4uFVSLgD2Q4]] — Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov
- [[youtube-YYH0DMQr30A]] — Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel
- [[youtube-UPwGaM2MKHY]] — The Log Is The Agent - Ishaan Sehgal, Omnara
- [[youtube-bRnoEpoK5m4]] — The Pipeline Is Dead - Iris ten Teije, Sky Valley Ambient Computing
- [[youtube-ILdE7FaAjVA]] — Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod
- [[youtube-_B4Pv9ttFgY]] — Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google
- [[youtube-4kYl2_mqmnQ]] — I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON
- [[youtube-qlHaO6laBlM]] — Shipping Production AI Inside Government — William Tarr, Ministry of Justice
- [[youtube-ghJmWQCIHRM]] — The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google
- [[youtube-HvZXAOZ3iv8]] — What Lies Beneath the API — Benjamin Cowen, Modal

### Transcript-backed resources

This evidence graph consolidates scheduled talks, linked videos, transcripts, and slide-derived material connected to this topic.

### Linked Sessions
- [[2026-06-30-pierluca-d-oro-computer-use-at-the-edge-of-the-statistical-precipice|Computer Use at the Edge of the Statistical Precipice]]
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale|Sandboxes Aren't Optional: Runtime Isolation Patterns for Coding Agents at Scale]]
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert|Your agent needs a sandbox, not a desert]]
- [[2026-06-29-tushar-jain-unlock-agent-autonomy-the-runtime-for-ai-native-systems|Unlock Agent Autonomy: The Runtime for AI-Native Systems]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1']]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2|'From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2']]
- [[2026-06-30-ivan-burazin-kubernetes-is-not-your-sandbox|Kubernetes Is Not Your Sandbox]]
- [[2026-06-30-kevin-orellana-1-000-agent-tasks-in-a-sandbox-what-breaks-when-llms-write-and-run-code|1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Write and Run Code]]
- [[2026-06-30-adam-azzam-don-t-build-agents-build-environments|Don’t build agents, build environments]]
- [[2026-06-29-matt-brockman-how-i-learned-to-stop-worrying-and-love-the-sandbox|How I learned to stop worrying and love the sandbox]]

### Media Signals
- `youtube-rcsliSIy_YU` — 8 slide-derived text signals
- Slide-derived themes for `youtube-rcsliSIy_YU`: coding, code, snippets, generation, single, atomic, tasks, curl.
- Evidence links for `youtube-rcsliSIy_YU`: [[youtube-rcsliSIy_YU]], [[youtube-rcsliSIy_YU-slides]], [[youtube-rcsliSIy_YU-dense-slides]], [[youtube-rcsliSIy_YU-reconstructed-slides]]
- `youtube-bmWZk9vTze0` — 10 slide-derived text signals
- Slide-derived themes for `youtube-bmWZk9vTze0`: query, client, info, table, tool, call, response, await.
- Evidence links for `youtube-bmWZk9vTze0`: [[youtube-bmWZk9vTze0]], [[youtube-bmWZk9vTze0-slides]], [[youtube-bmWZk9vTze0-dense-slides]], [[youtube-bmWZk9vTze0-reconstructed-slides]]
- `youtube-wsFd22SL1s8` — 10 slide-derived text signals
- Slide-derived themes for `youtube-wsFd22SL1s8`: systems, chrome, code, sandboxes, operating, distributed, windows, subsystem.
- Evidence links for `youtube-wsFd22SL1s8`: [[youtube-wsFd22SL1s8]], [[youtube-wsFd22SL1s8-slides]], [[youtube-wsFd22SL1s8-dense-slides]], [[youtube-wsFd22SL1s8-reconstructed-slides]]
- `youtube-e9sLVMN76qU` — 8 slide-derived text signals
- Slide-derived themes for `youtube-e9sLVMN76qU`: most, today, tooling, breaks, moment, remove, human, loop.
- Evidence links for `youtube-e9sLVMN76qU`: [[youtube-e9sLVMN76qU]], [[youtube-e9sLVMN76qU-slides]], [[youtube-e9sLVMN76qU-reconstructed-slides]]

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 40 | Related pages outside the main evidence categories. |
| resources | 22 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 16 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 24 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 5 | Derived inventory pages; use as entity context, not independent proof. |

### Talks
- [[2026-06-30-pierluca-d-oro-computer-use-at-the-edge-of-the-statistical-precipice]]
- [[2026-06-30-robert-brennan-sandboxes-aren-t-optional-runtime-isolation-patterns-for-coding-agents-at-scale]]
- [[2026-06-30-samuel-colvin-your-agent-needs-a-sandbox-not-a-desert]]
- [[2026-06-29-tushar-jain-unlock-agent-autonomy-the-runtime-for-ai-native-systems]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt-1]]
- [[2026-06-30-abhishek-bhardwaj-from-fork-to-fleet-designing-an-agent-sandbox-cloud-pt2]]

### Resources
- [[youtube-wFTVEDYVJT0]]
- [[youtube-Rx8f05JI_WA]]
- [[youtube-2IxD9OB3XuQ]]
- [[youtube-SKDJo2CopRs]]
- [[youtube-JnubYCYunk8]]
- [[youtube-c-2eEv2ou7Y]]

### Slides
- [[youtube-4kYl2_mqmnQ-slides]]
- [[youtube-qdZzND79mcg-slides]]
- [[youtube-2IxD9OB3XuQ-slides]]
- [[youtube-sAOBXCDiDOs-slides]]
- [[youtube-vljxQZfJ9wY-slides]]
- [[youtube-rcsliSIy_YU-slides]]

### Tools
- [[docker]]
- [[browserbase]]
- [[mcp-apps]]
- [[prime-intellect]]
- [[openhands]]

This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| other | 44 | Related pages outside the main evidence categories. |
| resources | 24 | Video/resource pages; check source status before treating as primary event evidence. |
| talks | 26 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |

### Talks

### Resources
- [[youtube-pMggiOb18tc]]
- [[youtube-o-zkvb0iFDQ]]

### Slides

### Tools

## Active Use Cases
- Running generated code and tests before suggesting a patch.
- Browser or computer-use automation with constrained state.
- Temporary workspaces for data analysis and document transformation.
- Reproducible agent task environments for evaluations.
