---
title: "Agentic Development Security"
category: "talks"
date: "2026-06-29"
time: "12:05pm-12:25pm"
track: "Security"
room: "Track 5"
speakers: ["Ezra Tanzer"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Security"
scheduleRoom: "Track 5"
scheduleLabels: ["Security", "Track 5", "sponsor", "confirmed"]
---
# Agentic Development Security

## Conference Context
- Date/time: 2026-06-29 · 12:05pm-12:25pm
- Track/room: Security · Track 5
- Speaker(s): Ezra Tanzer
- Session type/status: sponsor · confirmed

- Track: Security
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
No official description published in the schedule data.

## Synthesis
### Transcript-Backed Summary
The talk argues that agentic development security has to cover three layers at once: the code agents generate, the external components they use, and the actions they take. The proposed mechanism is to move from synchronous, rule-file-based checks to hook-driven asynchronous enforcement, component discovery, and policy controls that can either steer an agent or stop and ask for help. The speaker emphasizes tradeoffs between security and developer experience, especially latency, context bloat, and false positives, and the practical consequence is a system that is deterministic, auditable, and strong enough to support more autonomous background agents.

### Key Takeaways
- Agentic security should be treated as a three-part problem: generated output, connected components, and runtime behavior.
  - Evidence: "Uh it's really critical to secure what agents generate, what they use, and what they do. Um and I'll spend a couple minutes talking about our journey in each of these pillars over the last year, what we've learned and uh and our current perspective."
- Asynchronous hooks are a better fit than synchronous scans when the goal is deterministic enforcement without adding latency or context bloat.
  - Evidence: "Only then will it kick off a fix and validate loop. So now the workflow is deterministic. Latency is removed because all that testing happens asynchronously."
- Skills need their own security review because they can carry elevated privilege and even persist malicious behavior after removal.
  - Evidence: "That risk can still persist after the fact. Um, and in an audit that we did of nearly 4,000 skills on Claw Hub, uh, over one in eight had a critical severity issue and we actually found 76 malicious payloads, uh, in in that subset."
- Background and cloud agents make human approval prompts less viable, so finer-grained policies become more important.
  - Evidence: "But I think as we move towards more background agents and cloud agents being ran where you're trying to trying to step away and trying to not be sitting at your desk babysitting the agent entirely um asks are much much less viable option."
- Visibility, auditability, and traceability are central to trusting agents in everyday development workflows.
  - Evidence: "Give me that visibility. Give me that audibility. Give me that traceability. Uh, really important aspects in learning how to how to how to trust the agents and making sure that they're not going off the rail."

### Claims From The Talk
- The speaker argues that confidently using agents at scale requires securing what they generate, what they use, and what they do. (`explicit`)
  - Evidence: "Uh it's really critical to secure what agents generate, what they use, and what they do. Um and I'll spend a couple minutes talking about our journey in each of these pillars over the last year, what we've learned and uh and our current perspective."
- The original MCP-plus-rules approach had real limits because agents sometimes ignored rule files, scans added latency, and scans consumed tokens. (`explicit`)
  - Evidence: "Uh, but the approach did have real limitations. Agents sometimes ignored the rule files. Uh, scan execution did add latency at the end of its run."
- An audit of nearly 4,000 skills on Claw Hub found that over one in eight had a critical severity issue and 76 had malicious payloads. (`explicit`)
  - Evidence: "That risk can still persist after the fact. Um, and in an audit that we did of nearly 4,000 skills on Claw Hub, uh, over one in eight had a critical severity issue and we actually found 76 malicious payloads, uh, in in that subset."
- Behavior governance is aimed at intercepting exfiltrative, destructive, or otherwise risky agent actions. (`explicit`)
  - Evidence: "This is currently in open preview and it's really focused on how we ensure that an agent is not taking excfiltrative, destructive or otherwise malicious or risky actions."
- In the demo, Snappy blocked Claude from reading a secret file. (`explicit`)
  - Evidence: "Uh, Snappy actually blocked the access of of reading this file. Um, so yes, the agents are getting better."
- The speaker says false positives are not zero today and expects they may never reach absolute zero. (`explicit`)
  - Evidence: "But I'd be shocked if we ever lived in a world where it was like absolute zero false positive rate for for for any of the companies out there."

### Topics Covered
- [[agent-security|Agentic development security]] — The core problem of securing agentic software development across outputs, inputs, and actions.
- [[agent-security|Agent supply chain]] — The connected ecosystem of MCP servers and skills that expands the agent attack surface.
- [[agent-security|Behavior governance]] — Policies and controls for intercepting risky agent behavior before it executes.
- **Agent observability** — Seeing commands, files, sessions, costs, and tool use as part of trust in local agent workflows.
- [[agent-security|False positives]] — Managing the tension between strict enforcement and developer workflow noise.

### Tools And Named Systems
- [[mcp|MCP]] — The protocol used to connect agents to external tools and services.
- **Snappy** — The local enforcement tool shown blocking secret-file access in the demo.
- [[evo|EVO]] — The platform referenced for seeing agent guard behavior and connected components.
- [[claude|Claude]] — The agent interface used as an example of where ask-based prompting might appear.

### Novel Concepts And Methods
- **Async scan-and-fix** — Hook-driven asynchronous scan-and-fix flow that triggers scans on file changes, stores findings in a temporary file, and only runs a fix loop at session end.
- **Component autodiscovery** — Autodiscovery of MCP servers and skill files to analyze the connected agent components and identify related threats.
- **Steer or ask** — Steer-or-ask policy design that either rewrites an action safely or escalates to a human when the action is ambiguous or potentially destructive.
- **Workspace policies** — Workspace-specific guardrails that let the developer apply different policies depending on the project being worked on.
- **Local auditability** — Local enforcement and audit logging that records commands, files, sessions, and agent behavior for later review.

### Open Questions
- **How can the system drive false positives closer to zero without weakening the guardrails enough to matter?** — Adoption depends on whether developers can trust the controls without constant interruption.
- **How should agent-behavior controls work when the input is sensor data or other structured non-text data instead of natural language?** — The current model may need to generalize beyond chat and code workflows.
- **Can policy systems learn from prior user decisions so that agents need fewer asks as they become more autonomous?** — That would make background and cloud agents more practical without constant babysitting.

### Derived Links And Source Material
- [[youtube-cgimkNGNjvU-transcript]] — dedicated official recording transcript.
- [[youtube-cgimkNGNjvU]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/cgimkNGNjvU--2026-06-29-ezra-tanzer-agentic-development-security.json`.

### Speaker Context
- [[ezra-tanzer|Ezra Tanzer]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[ezra-tanzer]]

## Official YouTube Recording
- [[youtube-cgimkNGNjvU|Agentic Development Security — Ezra Tanzer, Snyk]] — official AI Engineer YouTube recording published 2026-07-20.
- Evidence status: [[youtube-cgimkNGNjvU-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-cgimkNGNjvU]] - dedicated official event recording.
- [[youtube-cgimkNGNjvU-transcript]] - dedicated official recording transcript.

- Source video: `youtube-cgimkNGNjvU`
- Slide deck: [[youtube-cgimkNGNjvU-slides|Slides: Agentic Development Security — Ezra Tanzer, Snyk]] — 18 visible slide image(s).
![[assets/slides/cgimkNGNjvU/slide-001.jpg]]
![[assets/slides/cgimkNGNjvU/slide-002.jpg]]
![[assets/slides/cgimkNGNjvU/slide-003.jpg]]
- Slide-derived themes for `youtube-cgimkNGNjvU`: security, track, june, server, directives, faye, world, fair.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/cgimkNGNjvU.txt` (5,107 words).

## Transcript Markdown
- [[youtube-cgimkNGNjvU-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/cgimkNGNjvU.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-cgimkNGNjvU` — 5,107 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-cgimkNGNjvU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-cgimkNGNjvU`: security, running, doing, code, last, still, skills, machine.
- Slide-derived themes for `youtube-cgimkNGNjvU`: security, track, june, server, directives, faye, world, fair.
- Evidence links for `youtube-cgimkNGNjvU` (primary event evidence): [[youtube-cgimkNGNjvU]], [[youtube-cgimkNGNjvU-transcript]], [[youtube-cgimkNGNjvU-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
