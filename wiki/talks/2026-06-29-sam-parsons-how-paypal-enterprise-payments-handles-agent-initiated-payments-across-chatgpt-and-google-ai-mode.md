---
title: "How PayPal Enterprise Payments handles agent-initiated payments across ChatGPT and Google AI Mode"
category: "talks"
date: "2026-06-29"
time: "10:45am-11:05am"
track: "Expo Stage 3 SW"
room: "Expo Stage 3 SW"
speakers: ["Sam Parsons"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: ""
scheduleRoom: "Expo Stage 3 SW"
scheduleLabels: ["Expo Stage 3 SW", "session", "confirmed"]
---
# How PayPal Enterprise Payments handles agent-initiated payments across ChatGPT and Google AI Mode

## Conference Context
- Date/time: 2026-06-29 · 10:45am-11:05am
- Track/room: track TBD · Expo Stage 3 SW
- Speaker(s): Sam Parsons
- Session type/status: session · confirmed

- Track: track TBD
- Room: Expo Stage 3 SW
- Session type: session
- Status: confirmed

## Session Description
PayPal Enterprise Payments has shipped integrations across the major agentic surfaces in the last six months each with human-in-the-loop confirmation and full transaction attribution back to the originating AI platform. We'll tour all three paths: ACP for ChatGPT apps (delegated payment tokens via complete_checkout, allowance validation, facilitator_details attribution), UCP with Google Pay for Google AI Mode (server-side tokenizationSpecification, parsing androidPayCards for the single-use token), and a preview of MCP Apps inline checkout, where the payment surface renders in-chat and card data never enters the LLM context. For each path we'll cover where PayPal Enterprise Payments fits, what the shopper and merchant each see, and the tradeoffs between them. You leave with working code and the docs to evaluate which path fits your stack.

## Media Evidence
No related AI Engineer channel video found yet.

## Evidence Graph
This evidence graph is generated from currently linked source material: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Media Signals
No linked video, transcript, or slide source has been attached yet.

### Agent Reading Notes
Use these signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[sam-parsons]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Synthesis
### Synthesized Breakdown
The session explains MCP Apps as a way to add interactive UI to MCP-based workflows. It treats the MCP host as the place where tool data, model reasoning, and human controls meet.

### Speaker And Company Context
- [[sam-parsons|Sam Parsons]] — Senior Staff Software Engineer and Tech Lead at [[paypal-braintree|PayPal Braintree]].

### Topics Covered
- [[agentic-search]]
- [[agentic-web]]
- [[coding-agents]]
- [[mcp]]
- [[mcp-apps]]

### Derived Links And Source Material

### Novel Concepts / Clever Methods
- [[mcp-app-runtime|MCP Apps As Agentic App Runtime]] — MCP Apps treats interactive UI returned from MCP servers as a runtime layer for agent-facing software.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
