---
title: "MCP Apps as Agentic App Runtime"
category: "topics"
sourceLabels: ["Official conference schedule", "Related YouTube transcript evidence", "Synthesis"]
highlighted: "true"
highlightPriority: "high"
sourceAssessment:
  schemaVersion: 1
  claimId: claim:c2997948196500f6b7827f566a012ba492bc0b7a8b3926e4dbcc1d264e29cfd3
  subjectId: concept:mcp-app-runtime
  domain: topics page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-24T00:00:00.000000Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-youtube-1EZdpEhwmNc
sourceAssessmentBodySha256: sha256:5825fc2b2a928190704c344531d8a81f3aca804c3078846c423e7dff69310924
---
# MCP Apps as Agentic App Runtime

## Overview
MCP Apps as an agentic app runtime is the idea that MCP servers can return interactive UI, not only structured text or JSON, so agents and humans can operate richer task surfaces inside MCP hosts.

## Significance
[[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier|MCP Apps - Extending the frontier]] presents MCP Apps as a path from tool calls to interactive software experiences. This matters when a task needs both model-readable data and human-operable UI.

## Applied Use
- Keep server-returned UI scoped to the task.
- Separate model data from user interaction state.
- Design for host constraints and permissions.
- Use MCP Apps when text-only tool output would force awkward back-and-forth or when human review is part of the workflow.

## Transcript Digest Evidence
This section synthesizes 3 evidence-bound talk topic candidates across at least two talks.

### Cross-Talk Synthesis
These talks treat MCP-style tool execution as a runtime substrate where authorization, typed contracts, and connector boundaries determine what agents can safely do. The variation is between protocol-level structure and app-runtime framing, but both assume dependable action comes from explicit interfaces rather than informal prompt-only behavior.

### Constituent Talk Evidence
- [[2026-06-29-kim-maida-it-s-10pm-do-you-know-where-your-agents-are|It's 10pm. Do You Know Where Your Agents Are?]] — The chain of runtime, MCP client, MCP server, and resource where authorization can be enforced.
  - Transcript: [[youtube-I3znWC3MEXM-transcript]]
  - Evidence: "Now an MCP client takes the agent's proposed tool calls and it dispatches them to its MCP server."
- [[2026-06-29-manoj-nair-through-the-ai-fog-the-architectural-decision-the-next-24-months-of-agentic-security-depends-on|Through the AI Fog: The architectural decision the next 24 months of agentic security depends on.]] — The security risks introduced by MCP servers as connectors to enterprise data and external instructions.
  - Transcript: [[youtube-1EZdpEhwmNc-transcript]]
  - Evidence: "This is great protocol, very little security built in. It's getting better, but the foundations behind it is you know, this is the GitHub MCP server exploit that we highlighted to the year a year ago."
- [[2026-07-01-frank-coyle-why-agentic-systems-need-ontologies|Why Agentic Systems Need Ontologies]] — Typed tool arguments and structured result checking before downstream action.
  - Transcript: [[youtube-Sir59K8ZDPU-transcript]]
  - Evidence: "But the idea is to surround the input with checks. Now, I've got this something that you that you should be at least taking a look at if you're doing some of this coding is something called Pydantic."

## Connections
- [[liad-yosef]]
- [[ido-salomon]]
- [[mcp-apps]]
- [[mcp]]
- [[agentic-web]]

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 3 | Related pages outside the main evidence categories. |
| resources | 3 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 7 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 4 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 2 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 6 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]]
- [[2026-06-29-kim-maida-it-s-10pm-do-you-know-where-your-agents-are]]
- [[2026-06-29-manoj-nair-through-the-ai-fog-the-architectural-decision-the-next-24-months-of-agentic-security-depends-on]]
- [[2026-07-01-frank-coyle-why-agentic-systems-need-ontologies]]

### Resources
- [[youtube-htM02KMNZnk]]
- [[youtube-jt1Pbr_n6oU]]
- [[youtube-o-zkvb0iFDQ]]

### Slides
- [[youtube-htM02KMNZnk-slides]]
- [[youtube-htM02KMNZnk-dense-slides]]
- [[youtube-htM02KMNZnk-reconstructed-slides]]
- [[youtube-jt1Pbr_n6oU-slides]]
- [[youtube-o-zkvb0iFDQ-slides]]
- [[youtube-o-zkvb0iFDQ-dense-slides]]

### Transcripts
- [[youtube-I3znWC3MEXM-transcript]]
- [[youtube-1EZdpEhwmNc-transcript]]
- [[youtube-Sir59K8ZDPU-transcript]]
- [[youtube-htM02KMNZnk-transcript]]
- [[youtube-jt1Pbr_n6oU-transcript]]
- [[youtube-o-zkvb0iFDQ-transcript]]

### Tools
- [[mcp-apps]]
- [[mcp]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.

### Linked Sessions
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier|MCP Apps - Extending the frontier]]
- [[2026-06-29-kim-maida-it-s-10pm-do-you-know-where-your-agents-are|It's 10pm. Do You Know Where Your Agents Are?]]
- [[2026-06-29-manoj-nair-through-the-ai-fog-the-architectural-decision-the-next-24-months-of-agentic-security-depends-on|Through the AI Fog: The architectural decision the next 24 months of agentic security depends on.]]
- [[2026-07-01-frank-coyle-why-agentic-systems-need-ontologies|Why Agentic Systems Need Ontologies]]

### Media Signals
- `youtube-htM02KMNZnk` — 89,050 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-htM02KMNZnk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-htM02KMNZnk`: model, code, models, loop, well, software, first, team.
- Slide-derived themes for `youtube-htM02KMNZnk`: apps, github, copilot, welcome, engineer, fair, single, line.
- Evidence links for `youtube-htM02KMNZnk` (primary event evidence): [[youtube-htM02KMNZnk]], [[youtube-htM02KMNZnk-transcript]], [[youtube-htM02KMNZnk-slides]], [[youtube-htM02KMNZnk-dense-slides]], [[youtube-htM02KMNZnk-reconstructed-slides]]
- `youtube-jt1Pbr_n6oU` — 3,441 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-jt1Pbr_n6oU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-jt1Pbr_n6oU`: data, model, graph, across, structure, chat, part, structured.
- Slide-derived themes for `youtube-jt1Pbr_n6oU`: track, july, fair, intro, defensible, organization, presented, users.
- Evidence links for `youtube-jt1Pbr_n6oU` (primary event evidence): [[youtube-jt1Pbr_n6oU]], [[youtube-jt1Pbr_n6oU-transcript]], [[youtube-jt1Pbr_n6oU-slides]]
- `youtube-o-zkvb0iFDQ` — 3,969 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-o-zkvb0iFDQ`: apps, host, claude, back, chatgpt, look, mcpui, chat.
- Slide-derived themes for `youtube-o-zkvb0iFDQ`: apps, maintainer, labs, used, text, community, easy, adoption.
- Evidence links for `youtube-o-zkvb0iFDQ` (supporting context only): [[youtube-o-zkvb0iFDQ]], [[youtube-o-zkvb0iFDQ-transcript]], [[youtube-o-zkvb0iFDQ-slides]], [[youtube-o-zkvb0iFDQ-dense-slides]], [[youtube-o-zkvb0iFDQ-reconstructed-slides]]
## Evidence Boundary
This page is grounded in official schedule context and related MCP UI/MCP Apps transcript evidence. It should be updated as MCP Apps implementation details and SEP-1865 adoption evolve.
