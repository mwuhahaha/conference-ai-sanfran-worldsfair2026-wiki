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

## Synthesis
### Synthesized Breakdown
PayPal Enterprise Payments has shipped integrations across the major agentic surfaces in the last six months each with human-in-the-loop confirmation and full transaction attribution back to the originating AI platform. We'll tour all three paths: ACP for ChatGPT apps (delegated payment tokens via complete_checkout, allowance validation, facilitator_details attribution), UCP with Google Pay for Google AI Mode (server-side tokenizationSpecification, parsing androidPayCards for the single-use token), and a preview of MCP Apps inline checkout, where the payment surface renders in-chat and card data never enters the LLM context. For each path we'll cover where PayPal Enterprise Payments fits, what the shopper and merchant each see, and the tradeoffs between them. You leave with working code and the docs to evaluate which path fits your stack.

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
## People
- [[sam-parsons]]

## Media Evidence
No exact recording or transcript evidence is attached yet; the official schedule remains the source for this session.
## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
No linked video, transcript, or slide source has been attached yet.

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
