---
title: AI Sandboxes
category: topics
sourceLabels:
  - Slide/video-derived supporting context
last_auto_summarized: '2026-07-06T22:02:50.744Z'
---
# AI Sandboxes

## Synopsis
AI sandboxes are the controlled execution environments that let agents operate on real files, browsers, repositories, websites, dependencies, and cloud resources without inheriting unrestricted access to the user’s machine or production account. In the World’s Fair material, sandboxing is not just a security feature for coding agents; it is the runtime substrate for agent autonomy. The connected sessions span OpenHands-style software agents, Docker and Daytona runtime boundaries, E2B sandbox operations, OpenAI fork-to-fleet infrastructure, Browserbase browser-agent deployment, Microsoft Foundry and OpenClaw hosting, Modal environment design, AWS code execution, Cua microVMs, and verifier systems for computer-use agents. Together they define a sandbox as a bounded computer plus an evidence system: it gives the agent enough state to do useful work, constrains process, filesystem, browser, network, credential, and persistence access, and leaves behind inspectable commands, diffs, logs, traces, screenshots, downloads, resource usage, verifier results, and rollback points.

## Origin And Context
The pattern inherits from operating-system isolation, browser sandboxes, CI runners, notebooks, containers, remote development workspaces, secure code-execution services, cloud GPU runtimes, and managed browser automation. The World’s Fair connections make the pattern specifically agent-shaped. The Sandbox & Platform Engineering track treats agent workspaces as stateful computers rather than empty containers: Samuel Colvin’s session frames the problem as giving agents a real environment instead of a desert, Adam Azzam’s Modal talk argues for building environments before building agents, Ivan Burazin warns that Kubernetes alone is not an agent sandbox, and Robert Brennan and Kevin Orellana focus on what happens when coding agents run large numbers of real tasks. Abhishek Bhardwaj’s two-part OpenAI session pushes the topic down to sandbox-cloud architecture, from process creation to fleet scheduling. Browserbase, Microsoft Research, Programma Labs, and Cua extend the same idea to browser and computer-use agents, where page state, screenshots, trajectories, downloads, and verifier hooks become part of the environment contract. Long-horizon and post-training sessions from General Reasoning, Theta Software, and Bespoke Labs add a training and evaluation angle: environments are also where agents learn, fail, and get measured over extended tasks.

## Why It Matters
The repeated failure mode across the connected pages is that agents become valuable when they can act, but dangerous or untrustworthy when that action is unbounded, under-specified, or invisible after the fact. Coding-agent sessions ask what breaks when LLMs write code, install packages, run tests, edit repositories, and execute generated scripts thousands of times. Browser-agent sessions show that a model’s claim to have searched, clicked, uploaded, or completed a web task is only meaningful if the environment captures page state, visual evidence, trajectories, downloads, and verifier checks. Runtime and platform talks argue that agents need real state, dependencies, and tools, but with explicit blast-radius limits around credentials, network access, persistence, and host resources. Production sessions from Microsoft, Databricks, OpenGov, Cloudflare, Modal, RunPod, and durable-workflow builders connect sandboxing to operational discipline: per-task identity, quotas, repeatable evals, audit logs, human review, incident reconstruction, and durable learning from failures. A sandbox is therefore containment, instrumentation, and accountability in one layer.

## How To Use It
Choose the sandbox boundary from the powers the agent actually has. A code assistant that only drafts text needs less isolation than one that can clone repositories, install dependencies, run test suites, open subprocesses, or modify files. A coding agent at OpenHands, AWS, E2B, Docker, Daytona, or OpenAI scale needs disposable workspaces, dependency policy, resource limits, network controls, credential scoping, diff capture, and a way to preserve the task record after the VM, container, or workspace is discarded. A browser or computer-use agent needs constrained browser profiles, controlled uploads and downloads, screenshot and DOM capture, trajectory logging, and verifier hooks that test whether the task was actually completed. MCP, ChatGPT app, and generated-interface surfaces need tool-boundary and iframe controls so rendered UI, model instructions, and tool execution do not collapse into the same trust zone. Cloud and enterprise agents need fleet-level scheduling, quotas, per-task identity, observability, durable workflow state, and review checkpoints. The useful deliverable is not only the final patch, answer, or completed web form; it is the evidence package that explains what the agent touched and why the result should be trusted.

## Where It Is Useful
Sandboxes are useful anywhere an agent does work instead of merely describing work. The connected pages place them in OpenHands-style coding agents, Docker and Daytona developer environments, E2B sandbox fleets, OpenAI RL and agent infrastructure, AWS code execution and browser automation, Browserbase browser-agent deployment, Microsoft Foundry hosted agents, OpenClaw cloud sandboxes, Cua microVM-based computer-use agents, Modal AI-native runtime platforms, Cloudflare eval infrastructure, RunPod endpoint deployment, durable workflow runtimes, MCP app surfaces, Chrome DevTools-style agent interfaces, long-horizon RL environments, post-training data curation, verifier systems, data-analysis workspaces, document transformation tools, and software-factory pipelines. The common requirement is a bounded place where the agent can use real tools while the operator can inspect the work afterwards.

## When To Use It
Use a sandbox whenever the agent can execute code, read or write user files, browse unknown sites, install dependencies, call tools, transform documents, operate a browser, deploy endpoints, use credentials, or run model-generated scripts. Tighten the boundary when the task involves production data, customer workflows, cloud accounts, persistent state, downloads, uploads, external network calls, or a browser session that could leak identity or authority. Loosen it only when the task model, threat model, allowed resources, logging requirements, rollback path, and review workflow are explicit. The practical rule from the World’s Fair evidence is simple: if the agent’s action would be hard to reconstruct, explain, or undo after the fact, the environment is not sandboxed enough.

## Active Use Cases
- Running generated code and tests before suggesting a patch.
- Browser or computer-use automation with constrained state.
- Temporary workspaces for data analysis and document transformation.
- Reproducible agent task environments for evaluations.

## Related Slide Decks
- [[youtube-aHhB3sjGjkI-slides]] — Agents Building Agents - Alfonso Graziano, Nearform (24 extracted slide frames)

## Related Scheduled Sessions
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
- [[2026-06-29-du-an-lightfoot-agents-that-own-their-inference-building-production-ai-agents-on-dedicated-gpus]] — Agents That Own Their Inference: Building Production AI Agents on Dedicated GPUs; [[du-an-lightfoot|Du'an Lightfoot]] (Day 1 — Workshop Day · 9:00am-11:00am · Track 7; related YouTube resource; via [[youtube-wFTVEDYVJT0]])
- [[2026-06-30-paul-klein-iv-bringing-agents-onto-the-world-wide-web]] — Bringing agents onto the world wide web; [[paul-klein-iv|Paul Klein IV]] (Day 3 — Session Day 2 · 11:40am-12:00pm · Computer Use; official schedule)

## Related People
- [[john-craft|John Craft]]
- [[abhishek-bhardwaj|Abhishek Bhardwaj]]
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
- [[derek-meegan|Derek Meegan]]
- [[ross-taylor|Ross Taylor]]
- [[chengxi-taylor|Chengxi Taylor]]
- [[miguel-gonz-lez-fern-ndez|Miguel González Fernández]]
- [[corby-rosset|Corby Rosset]]
- [[rowan-christmas|Rowan Christmas]]
- [[rayan-garg|Rayan Garg]]
- [[mahesh-sathiamoorthy|Mahesh Sathiamoorthy]]
- [[keiji-kanazawa|Keiji Kanazawa]]
- [[viren-baraiya|Viren Baraiya]]
- [[yohei-nakajima|Yohei Nakajima]]
- [[ang-li|Ang Li]]

## Related Companies
- [[docker|Docker]]
- [[microsoft|Microsoft]]
- [[browserbase|Browserbase]]
- [[openai|OpenAI]]
- [[amazon-agi-lab|Amazon AGI Lab]]
- [[cua|Cua]]
- [[typedef|typedef]]
- [[oxylabs|Oxylabs]]
- [[amazon-web-services|Amazon Web Services]]
- [[mcp-apps|MCP Apps]]
- [[navan|Navan]]
- [[uber|Uber]]
- [[warp|Warp]]
- [[prime-intellect|Prime Intellect]]
- [[meta|Meta]]
- [[yugabyte|Yugabyte]]
- [[programma-labs|Programma Labs]]
- [[openhands|OpenHands]]

## Transcript And Resource Support
### Transcript-backed resources
- [[youtube-2IxD9OB3XuQ]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI
- [[youtube-SKDJo2CopRs]] — Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare
- [[youtube-JnubYCYunk8]] — Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, ARK
- [[youtube-wFTVEDYVJT0]] — Building Agents with Amazon Nova Act and MCP - Du'An Lightfoot, Amazon (Full Workshop)
- [[youtube-c-2eEv2ou7Y]] — Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic
- [[youtube-TNwJ1LMiENk]] — Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel
- [[youtube-4uFVSLgD2Q4]] — Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov
- [[youtube-YYH0DMQr30A]] — Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel
- [[youtube-UPwGaM2MKHY]] — The Log Is The Agent - Ishaan Sehgal, Omnara
- [[youtube-ILdE7FaAjVA]] — Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod
- [[youtube-_B4Pv9ttFgY]] — Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google
- [[youtube-ghJmWQCIHRM]] — The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google
- [[youtube-HvZXAOZ3iv8]] — What Lies Beneath the API — Benjamin Cowen, Modal
- [[youtube-btxGmN8RvNU]] — Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data
- [[youtube-zDGHt0LB-dA]] — GPU Cloud Deployment Without Leaving Your IDE — Audry Hsu, RunPod
- [[youtube-hCMrEfPG2Yg]] — Beyond Components: Designing Generative UI for MCP Apps — Ruben Casas, Postman
- [[youtube-ObTPqBGsEbA]] — The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks
- [[youtube-DqtmZE6Hl0g]] — The Prompt is the Platform - Dominik Tornow, Resonate HQ

## Livestream Slide Support
Livestream slide OCR provides supporting evidence for this topic. These notes are source-linked summaries; inspect the dense slide pages before treating OCR text as exact wording.
- [[youtube-I2cbIws9j10]] / [[youtube-I2cbIws9j10-dense-slides]]: The agent-architecture slide separates the agent from any single model: the production agent also includes runtime or sandbox, tools, loop, and framework.
