---
title: "AI Sandboxes"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---

# AI Sandboxes

## Synopsis
AI sandboxes are controlled execution environments where agents can run code, browse, inspect files, call tools, or manipulate artifacts without putting the host system at unnecessary risk. A sandbox gives the agent enough power to do real work while limiting filesystem, network, credential, and process access.

## Origin And Context
The pattern comes from operating-system isolation, browser sandboxes, CI runners, notebooks, container platforms, and secure code-execution services. Agentic coding and computer-use systems made sandboxing a default requirement rather than a specialty feature.

## Why It Matters
Agents need to experiment, test, and inspect state. Sandboxes let them do that while containing failures, malicious inputs, runaway processes, and accidental destructive changes.

## How To Use It
Choose isolation based on risk: separate processes for low-risk tasks, containers or microVMs for untrusted code, and policy-controlled network and secret access for production work. Capture logs, diffs, artifacts, and resource usage so human operators can review what happened.

## Where It Is Useful
They are useful in coding assistants, data-analysis agents, browser agents, app builders, test runners, educational tools, and any system that executes generated code or commands.

## When To Use It
Use a sandbox whenever an agent can execute code, inspect user files, download dependencies, browse unknown sites, or run untrusted scripts. Loosen limits only after the workflow and threat model are well understood.

## Active Use Cases
- Running generated code and tests before suggesting a patch.
- Browser or computer-use automation with constrained state.
- Temporary workspaces for data analysis and document transformation.
- Reproducible agent task environments for evaluations.

## Related Slide Decks
- [[youtube-aHhB3sjGjkI-slides]] — Agents Building Agents - Alfonso Graziano, Nearform (24 extracted slide frames)

## Related Scheduled Sessions

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
