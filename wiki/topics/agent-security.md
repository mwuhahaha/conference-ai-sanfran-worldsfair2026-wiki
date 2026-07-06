---
title: "Agent Security"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---

# Agent Security

## Synopsis
Agent security covers the controls that keep autonomous or semi-autonomous AI systems within trusted boundaries. It includes authentication, authorization, tool permissions, sandboxing, prompt-injection resistance, secret handling, audit logs, data-boundary enforcement, and recovery paths when an agent behaves unexpectedly.

## Origin And Context
It combines application security, cloud IAM, browser and plugin sandboxing, supply-chain security, and adversarial ML. Tool-using agents raise the stakes because natural-language inputs can influence systems that touch files, APIs, payments, infrastructure, or private data.

## Why It Matters
Agents convert text into action. That makes ordinary content, retrieved documents, web pages, or UI state part of the attack surface. Security is what lets teams give agents useful tools without handing them unlimited authority.

## How To Use It
Use least-privilege tool scopes, explicit approval gates for high-risk actions, isolated execution environments, secret redaction, provenance checks, and audit trails. Treat retrieved content as untrusted input, test prompt-injection cases, and design rollback paths for destructive operations.

## Where It Is Useful
Agent security matters in coding agents, MCP servers, browser agents, enterprise assistants, finance and compliance workflows, internal operations tools, and any system connected to privileged APIs or private data.

## When To Use It
Apply strong controls whenever an agent can read sensitive data, write state, call external APIs, spend money, deploy code, or influence another system. Lower-risk chat-only agents still need data handling and logging rules.

## Active Use Cases
- Permission-gated tool execution for enterprise agents.
- Sandboxed coding and browser automation.
- Prompt-injection and data-exfiltration testing for retrieval agents.
- Audit logs for regulated or high-trust agent workflows.

## Related Slide Decks
- [[youtube-aHhB3sjGjkI-slides]] — Agents Building Agents - Alfonso Graziano, Nearform (24 extracted slide frames)
- [[youtube-jVjt-2g8NMY-slides]] — A Genius With Amnesia - Victor Savkin, Nx (19 extracted slide frames)

## Related Scheduled Sessions

## Transcript And Resource Support
### Transcript-backed resources
- [[youtube-SKDJo2CopRs]] — Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare
- [[youtube-c-2eEv2ou7Y]] — Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic
- [[youtube-LrGCT7G_rU8]] — Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon
- [[youtube-hCMrEfPG2Yg]] — Beyond Components: Designing Generative UI for MCP Apps — Ruben Casas, Postman
- [[youtube-_xIwFcnHqp4]] — Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub
- [[youtube-6bmM45jkMDY]] — You Can't Prompt the Room: The Last Skill AI Won't Replace - Balázs Horváth, VisualLabs
