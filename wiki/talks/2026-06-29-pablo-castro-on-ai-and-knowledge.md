---
title: "On AI and Knowledge"
category: "talks"
date: "2026-06-29"
time: "9:05am-9:25am"
track: "Software Factories"
room: "Main Stage"
speakers: ["Pablo Castro"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Software Factories"
scheduleRoom: "Main Stage"
scheduleLabels: ["Software Factories", "Main Stage", "keynote", "confirmed"]
---
# On AI and Knowledge

## Conference Context
- Date/time: 2026-06-29 · 9:05am-9:25am
- Track/room: Software Factories · Main Stage
- Speaker(s): Pablo Castro
- Session type/status: keynote · confirmed

- Track: Software Factories
- Room: Main Stage
- Session type: keynote
- Status: confirmed

## Session Description
No official description published in the schedule data.

## Synthesis
### Transcript-Backed Summary
Pablo Castro's thesis is that AI progress should be understood as a progression from intrinsic model knowledge, to extrinsic grounding in organizational data, to learned knowledge captured through feedback loops. He argues that the first wave of coding and agent gains came from what models already knew, but that production agents need structured grounding over company data and public data, plus retrieval systems that combine multiple methods instead of relying on vector similarity alone. The practical consequence is a layered platform where users can stay at a simple high-level interface for PDFs, tables, and web grounding, or drop down into index and retrieval controls when they need precision, while the system also optimizes agents automatically from traces and evaluations.

### Key Takeaways
- The field moved from basic RAG into broader context engineering for connecting agents to the knowledge they need.
  - Evidence: "That started as a pretty low-tech technique, but quickly evolved and what we do today with context engineering and you know, it became a pretty sophisticated system for connecting agents and the knowledge they need to get their job done."
- Agents often need access to ambient organizational data such as documents, email, chat, and analytics assets, not just hand-curated data.
  - Evidence: "This includes maybe your documents, your emails, your chat threads, or the information in your data warehouse and So, we built Microsoft IQ as a way to give you a single entry point into all these kind of ambient data that agents need to get the job done in addition to the specific information that you build into the agent."
- A single stack that supports both high-level simplicity and low-level tuning lets teams adapt as needs change.
  - Evidence: "You can do all of that and you can do it in the same stack, which means you can go up and down as you as your needs change."
- Token efficiency matters because retrieval systems should return the densest useful answer with the fewest tokens.
  - Evidence: "And uh so, uh we carefully evaluate this system to make sure that we give you the most information dense answer that has the fewest tokens uh so that you you know, the the your consumption of tokens has a high value when it comes to all retrieval tasks."
- The learning loop is meant to capture differentiated capability that is specific to each company or organization.
  - Evidence: "So this is a real learning loop materialized in practice. You can go back to slides. So this was like a very quick overview about how do we think about knowledge in the context of AI and how do how we think we can enable these learning loops that will capture, you know, these differentiated capability that lives in each one of the companies and organizations we work on."

### Claims From The Talk
- The speaker argues that the recent AI coding and agent wave was powered primarily by intrinsic model knowledge and reasoning. (`strong`)
  - Evidence: "So, this is the shape of the exponential we're in. And a lot of this was powered by the by the intrinsic knowledge in models and of course their ability to reason."
- The speaker reports that retrieval works better when methods are combined rather than relying on vector similarity alone. (`strong`)
  - Evidence: "It turns out, you know, things never are are never that easy. Uh, so, you know, what evaluations show over and over again is how, you know, if you combine methods, you just get better results."
- The speaker argues that organizations can materialize a learning loop by evaluating a baseline, generating candidates, and deploying a stronger agent configuration. (`strong`)
  - Evidence: "So we built a component called the agent optimizer that effectively goes through this process and allows you to evaluate a baseline, generate candidates, and then you know, evaluate the new candidates and we have a strong result, then deploy that to production."

### Topics Covered
- [[agent-memory|knowledge taxonomy]] — The distinction between what models already know, what agents retrieve from outside sources, and what systems learn over time.
- **company grounding** — How AI systems use organizational and public data to ground agent behavior.
- [[agent-memory|layered retrieval]] — A retrieval architecture that supports both simple usage and expert control in one system.
- [[agentic-search|agentic retrieval]] — Retrieval workflows that reflect on whether the query has been satisfied before returning results.
- [[agent-evaluations|agent optimization]] — Improving agents through evaluation-driven candidate generation and deployment.

### Tools And Named Systems
- **Microsoft Foundry** — Microsoft's agent and model platform used to manage agents, models, and knowledge.
- [[microsoft-iq|Microsoft IQ]] — Microsoft's knowledge-grounding capability described as a set of capabilities for ambient organizational data.
- **Work IQ** — The work-oriented grounding capability that connects agents to SharePoint, email, calendar, chats, and people connections.
- **Fabric IQ** — The analytics grounding capability for warehouses, data lakes, and Power BI reports.
- **Foundry IQ** — The agent grounding capability for pushing custom data into Foundry for retrieval.
- **Web IQ** — The web grounding capability for public information.
- [[mcp|MCP]] — The protocol used so each knowledge base can be connected without custom glue code.
- [[azure|Azure]] — The Microsoft cloud environment where the speaker shows the underlying knowledge base service.
- [[vs-code|VS Code]] — The editor used in the optimization demo with the Foundry toolkit installed.

### Novel Concepts And Methods
- **knowledge taxonomy** — Classifying knowledge into intrinsic, extrinsic, and learned categories to reason about AI systems.
- **company grounding** — Connecting agents to organizational and public data through ambient grounding sources.
- **layered retrieval stack** — Layering retrieval capabilities so users can move from simple defaults to low-level control as needed.
- **agentic retrieval** — Using reflective retrieval to decide whether the information need has been satisfied before returning results.
- **agent optimization loop** — Evaluating a baseline, generating candidates, and applying the best-performing configuration to production.

### Open Questions
- **How can a retrieval platform combine many building blocks without exposing that complexity to users who only need a simple path?** — This is the central product-design problem behind making advanced retrieval usable at scale.
- **How should teams choose the right balance between retrieval effort, latency, and answer quality for a given knowledge base?** — The talk frames this as a real tuning decision that affects practical deployment performance.
- **When does agentic retrieval produce enough benefit to justify its added complexity over simpler single-shot retrieval?** — The speaker explicitly raises usefulness as the key open evaluation question for the approach.

### Derived Links And Source Material
- [[youtube-RGSFUqzqErE-transcript]] — dedicated official recording transcript.
- [[youtube-RGSFUqzqErE]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/RGSFUqzqErE--2026-06-29-pablo-castro-on-ai-and-knowledge.json`.

### Speaker Context
- [[pablo-castro|Pablo Castro]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[pablo-castro]]

## Official YouTube Recording
- [[youtube-RGSFUqzqErE|On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft]] — official AI Engineer YouTube recording published 2026-07-17.
- Evidence status: [[youtube-RGSFUqzqErE-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-RGSFUqzqErE]] - dedicated official event recording.
- [[youtube-RGSFUqzqErE-transcript]] - dedicated official recording transcript.

- Source video: `youtube-RGSFUqzqErE`
- Slide deck: [[youtube-RGSFUqzqErE-slides|Slides: On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft]] — 28 visible slide image(s).
![[assets/slides/RGSFUqzqErE/slide-001.jpg]]
![[assets/slides/RGSFUqzqErE/slide-002.jpg]]
![[assets/slides/RGSFUqzqErE/slide-003.jpg]]
- Slide-derived themes for `youtube-RGSFUqzqErE`: fair, engineering, future, bile, microsoft, resolve, knowledge, pablo.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/RGSFUqzqErE.txt` (3,081 words).

## Transcript Markdown
- [[youtube-RGSFUqzqErE-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/RGSFUqzqErE.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-RGSFUqzqErE` — 3,081 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-RGSFUqzqErE`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-RGSFUqzqErE`: knowledge, data, retrieval, foundry, whatnot, microsoft, models, give.
- Slide-derived themes for `youtube-RGSFUqzqErE`: fair, engineering, future, bile, microsoft, resolve, knowledge, pablo.
- Evidence links for `youtube-RGSFUqzqErE` (primary event evidence): [[youtube-RGSFUqzqErE]], [[youtube-RGSFUqzqErE-transcript]], [[youtube-RGSFUqzqErE-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
