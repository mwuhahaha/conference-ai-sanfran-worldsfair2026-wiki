---
title: "Model Context Protocol"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---

# Model Context Protocol

## Synopsis
Model Context Protocol, or MCP, is a standard pattern for connecting AI applications to tools, data, and interactive capabilities through structured servers and clients. In this wiki it also includes MCP Apps and agent-facing interfaces that expose richer actions or UI surfaces to models.

## Origin And Context
MCP emerged from the need to standardize how AI clients discover and call tools, access resources, and integrate with external systems. It sits in the lineage of plugin APIs, language-server style tooling, RPC, browser extensions, and developer-tool protocols.

## Why It Matters
Agents are only as useful as the tools and context they can safely access. MCP reduces one-off integrations, gives tool providers a common surface, and helps clients reason about capabilities, permissions, and interaction patterns.

## How To Use It
Define focused MCP servers with clear tools, schemas, resources, and permission boundaries. Keep tool names concrete, return structured results, test with inspectors, and design for least privilege. For MCP Apps, treat UI and iframe boundaries as part of the security and product contract.

## Where It Is Useful
MCP is useful in IDEs, desktop assistants, enterprise data connectors, browser agents, design tools, developer platforms, and internal operations systems.

## When To Use It
Use MCP when multiple AI clients need access to the same tools or when a tool provider wants a standard agent-facing integration. For a single narrow app, direct APIs may be simpler until reuse or interoperability matters.

## Active Use Cases
- Connecting agents to repositories, browsers, docs, databases, and SaaS tools.
- MCP Apps that return interactive UI from tool servers.
- Agent-ready web and developer-tool integrations.
- Local inspectors and compliance checks for tool servers.

## Related Slide Decks
- [[youtube-gcseUQJ6Gbg-slides]] — Using OSS models to build AI apps with millions of users — Hassan El Mghari (4 extracted slide frames)
- [[youtube-aHhB3sjGjkI-slides]] — Agents Building Agents - Alfonso Graziano, Nearform (24 extracted slide frames)
- [[youtube-jVjt-2g8NMY-slides]] — A Genius With Amnesia - Victor Savkin, Nx (19 extracted slide frames)

## Related Scheduled Sessions
- [[2026-06-30-hassan-el-mghari-the-missing-layer-design-taste-in-ai-agents-stop-letting-your-agents-ship-ugly-uis]] — The Missing Layer: Design Taste in AI Agents // Stop Letting Your Agents Ship Ugly UIs

## Transcript And Resource Support
### Transcript-backed resources
- [[youtube-sAOBXCDiDOs]] — MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc
- [[youtube-vh2VGuQ3zhY]] — The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica
- [[youtube-_xIwFcnHqp4]] — Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub
- [[youtube-ghJmWQCIHRM]] — The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google
- [[youtube-_B4Pv9ttFgY]] — Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google
- [[youtube-c-2eEv2ou7Y]] — Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic
- [[youtube-spNAUEgq_A8]] — The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents
- [[youtube-hCMrEfPG2Yg]] — Beyond Components: Designing Generative UI for MCP Apps — Ruben Casas, Postman
- [[youtube-4uFVSLgD2Q4]] — Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov
- [[youtube-btxGmN8RvNU]] — Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data
- [[youtube-wFTVEDYVJT0]] — Building Agents with Amazon Nova Act and MCP - Du'An Lightfoot, Amazon (Full Workshop)
- [[youtube--x5GEVnkuRw]] — Structuring the Unstructured - Cedric Clyburn, Red Hat
- [[youtube-SKDJo2CopRs]] — Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare
- [[youtube-aHhB3sjGjkI]] — Agents Building Agents - Alfonso Graziano, Nearform
- [[youtube-2IxD9OB3XuQ]] — Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI
- [[youtube-dRmWYHuIJxM]] — We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco
- [[youtube-uiP88SpCi1Q]] — Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS
- [[youtube-bk0TmxoZlUY]] — Evals 101 — Doug Guthrie, Braintrust

### Quote signals
- “I'm an engineer here at OpenGov and today we're going to be talking about agents in production, specifically how OpenGov built and scaled OG Assist.” — [[youtube-4uFVSLgD2Q4]]
- “So, that's kind of how we handled long context and memory, and it's worked pretty well for us.” — [[youtube-4uFVSLgD2Q4]]
- “Uh it's an open source inspector, again, uh something comparable to the official inspector from the model context protocol maintainers that allows you to test these MCP servers and apps specifically uh on your local machine.” — [[youtube-sAOBXCDiDOs]]
- “MCP apps is now the official extension of the Model Context Protocol that allows to return UI elements within MCP servers.” — [[youtube-sAOBXCDiDOs]]
- “[clears throat] And also Cursor allows you to submit their MCP server set uh The way you submit is different for all three, but basically what happens is that you need to make sure that your MCP app is compliant.” — [[youtube-sAOBXCDiDOs]]
- “The let's say past few decades, we have been building the web for human actions and human eyes, and we've been trying to optimize for that, but these days, it's not just humans that are using the web.” — [[youtube-ghJmWQCIHRM]]
- “Well, today I'm going to share four engineering lessons from the Chrome uh DevTools team on how we build Chrome DevTools for agents and how we deployed it for effect.” — [[youtube-_B4Pv9ttFgY]]
- “In a world where you are delegating away work to agents and automating away agents, you need to think about trust boundaries.” — [[youtube-_B4Pv9ttFgY]]
