---
title: "Through the AI Fog: The architectural decision the next 24 months of agentic security depends on."
category: "talks"
date: "2026-06-29"
time: "10:45am-11:05am"
track: "Security"
room: "Track 5"
speakers: ["Manoj Nair"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Security"
scheduleRoom: "Track 5"
scheduleLabels: ["Security", "Track 5", "sponsor", "confirmed"]
---
# Through the AI Fog: The architectural decision the next 24 months of agentic security depends on.

## Conference Context
- Date/time: 2026-06-29 · 10:45am-11:05am
- Track/room: Security · Track 5
- Speaker(s): Manoj Nair
- Session type/status: sponsor · confirmed

- Track: Security
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
No official description published in the schedule data.

## Synthesis
### Transcript-Backed Summary
Manoj Nair argues that agentic security now depends on a design choice: do not assume the same system can generate work and validate it safely. He uses customer data, benchmark results, and attack examples to show that autonomous attacks, poisoned skills, risky MCP servers, and agent behavior create a broader and more dynamic attack surface than traditional software. His practical answer is to move security into the live workflow, combine deterministic checks with model-based analysis, inspect provenance and breakability before allowing packages or skills into use, and enforce policy in real time where agents and developers actually work. He closes by framing Evo as an open, community-built system meant to give AI security engineers the same operational leverage that agentic systems give builders.

### Key Takeaways
- The speaker's core takeaway is that chasing one model or one latest capability will not solve agentic security; the system has to be designed around the problem.
  - Evidence: "It's just not widespread enough. And so, trying to like you know, chase systems and like the specific model will be the cure for all this is not the way is our point."
- Package choice should account for maintenance and future patchability, not only whether a package is currently free of CVEs.
  - Evidence: "Uh but, the first one, QR code, is healthy, meaning it's actively being maintained. Um and there's a ton of a ton of active usage downloads of this."
- A skill or tool can become unsafe even if the local file does not change, because it may depend on external instructions or data that can be altered later.
  - Evidence: "So, it's really giving it the logic to actually execute the skill from a third-party website."
- Security policy has to be enforced in the loop, because static documents cannot keep up with fast-moving code repositories and agent actions.
  - Evidence: "So, how do you real-time look at everything that is happening in a very fast moving complex code repositories and understand risk and have policies enforced in the loops that the agents and the devs are."

### Claims From The Talk
- The speaker argues that a central security question in agentic systems is whether the generator and validator can be the same, and he says his answer is no. (`explicit`)
  - Evidence: "So, one thing you're going to hear from from me quite a bit of, you know, in this like, you know, what if you take one thing, it's this notion of our learning from this real-life data and working with the biggest frontier labs in the world and the biggest companies in the world is this concept that has really been, you know, not questioned in security before, but it is being asked now, right?"
- He reports that frontier labs have already been used in automated attacks and that attackers can operate continuously when they have good context and a good harness. (`explicit`)
  - Evidence: "All the frontier labs have been used in automated attacks. You can do that even without having frontier models."
- He says his customer data shows backlog has grown by 108 percent quarter over quarter across more than 4,800 customers, which he treats as evidence that risk is increasing faster than teams are controlling it. (`strong`)
  - Evidence: "This is 4,800 plus customers in the last year. Their actual backlog quarter over quarter is like 108% more backlog."
- He argues that skills and MCP servers are part of the security problem because skills can contain malware or vulnerabilities and MCP adds another weak security layer for enterprise data access. (`explicit`)
  - Evidence: "This is you know, the amount of vulnerable code coming from the latest models. Plus the skills, there's toxic skills."
- He reports that Snyk has GA'd an agentic dev security offering that watches the environment, outputs, skills, MCP servers, and agent behavior in real time. (`explicit`)
  - Evidence: "We just GA'd our agentic dev security offering yesterday. It's looking at the environment, the output, the skills, the MCP servers, and the behavior of coding agents like Cursor Cloud, um Codex, and others."
- He presents Evo as a concept and system built to support AI security engineers through observation, orientation, decision, and action, and says it is meant to be open and community-built. (`explicit`)
  - Evidence: "And we learned, you know, this as I mentioned Evo, what is Evo? Evo is the system that we we brought to the world late last year in terms of a concept and we've constantly built these different agents."

### Topics Covered
- [[agent-security|Agentic security]] — The overarching problem of securing autonomous and semi-autonomous AI systems across code, tools, data, and behavior.
- [[agent-evaluations|Generator-validator separation]] — The claim that generation and validation should be separated because models are not reliable enough to serve as their own judges.
- [[agent-security|Skill supply-chain risk]] — The idea that skills can hide malware, vulnerabilities, or externally controlled logic and therefore need review.
- [[mcp-app-runtime|MCP server security]] — The security risks introduced by MCP servers as connectors to enterprise data and external instructions.
- [[agent-security|Breakability-aware remediation]] — Choosing remediation steps based on how likely they are to break applications rather than only on severity counts.
- [[agent-security|Real-time policy enforcement]] — Enforcing security decisions live inside the tools and workflows that agents and developers use.

### Tools And Named Systems
- **Snyk** — The security and package-health product the speaker demoed as part of the agentic dev security workflow.
- [[claude|Claude]] — The model/service used in the demo to generate a CLI tool.
- [[codex|Codex]] — A coding agent explicitly named as part of the security monitoring scope.
- [[cursor|Cursor]] — A coding agent explicitly named as part of the security monitoring scope.
- [[mcp|MCP]] — The protocol discussed as an integration point for enterprise data and agent tools.
- [[evo|Evo]] — The system the speaker says is being built to empower AI security engineers.

### Novel Concepts And Methods
- **Generator-validator separation** — Use generator-validator separation instead of assuming the same model can both create and judge agent output reliably.
- **Deterministic package gating** — Apply deterministic package-health checks and policy hooks before an agent introduces dependencies into a workflow.
- **Skill and MCP risk assessment** — Assess skills and MCP servers as first-class attack surface rather than trusting their labels or filenames.
- **Breakability-aware remediation** — Measure breakability before remediation so teams can reduce vulnerability backlog without breaking applications.
- **Real-time policy enforcement** — Keep security decisions inside the live agent loop instead of relying on static governance documents.
- **OODA operating loop** — Use observe, orient, decide, act as the operating loop for continuously improving agentic security systems.

### Open Questions
- **What is the safe path to re-enable MCP servers after a broad shutdown once their risks are understood?** — The talk shows that disabling powerful interfaces is easy, but safely restoring them is the harder operational problem.
- **How should teams combine probabilistic model checks with deterministic checks so they catch what each one misses?** — The speaker says latest models and deterministic checks each miss different issues, which leaves open the right division of labor.
- **How can breakability be measured well enough to know whether a remediation or upgrade is truly safe?** — The speaker presents breakability as necessary for zeroing backlog without causing outages, but the operational method is not fully settled.
- **How do you coordinate multiple agents, shared memory, and harnesses without losing control of the system?** — He says multi-agent coordination is still unsolved, so this is a core research and implementation gap.

### Derived Links And Source Material
- [[youtube-1EZdpEhwmNc-transcript]] — dedicated official recording transcript.
- [[youtube-1EZdpEhwmNc]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/1EZdpEhwmNc--2026-06-29-manoj-nair-through-the-ai-fog-the-architectural-decision-the-next-24-months-of-agentic-security-depends-on.json`.

### Speaker Context
- [[manoj-nair|Manoj Nair]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[manoj-nair]]

## Official YouTube Recording
- [[youtube-1EZdpEhwmNc|Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk]] — official AI Engineer YouTube recording published 2026-07-20.
- Evidence status: [[youtube-1EZdpEhwmNc-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-1EZdpEhwmNc]] - dedicated official event recording.
- [[youtube-1EZdpEhwmNc-transcript]] - dedicated official recording transcript.

- Source video: `youtube-1EZdpEhwmNc`
- Slide deck: [[youtube-1EZdpEhwmNc-slides|Slides: Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk]] — 16 visible slide image(s).
![[assets/slides/1EZdpEhwmNc/slide-001.jpg]]
![[assets/slides/1EZdpEhwmNc/slide-002.jpg]]
![[assets/slides/1EZdpEhwmNc/slide-003.jpg]]
- Slide-derived themes for `youtube-1EZdpEhwmNc`: track, june, security, malicious, engineering, future, pitch, defend.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/1EZdpEhwmNc.txt` (4,245 words).

## Transcript Markdown
- [[youtube-1EZdpEhwmNc-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/1EZdpEhwmNc.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-1EZdpEhwmNc` — 4,245 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-1EZdpEhwmNc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-1EZdpEhwmNc`: security, data, code, able, find, skill, customers, attacks.
- Slide-derived themes for `youtube-1EZdpEhwmNc`: track, june, security, malicious, engineering, future, pitch, defend.
- Evidence links for `youtube-1EZdpEhwmNc` (primary event evidence): [[youtube-1EZdpEhwmNc]], [[youtube-1EZdpEhwmNc-transcript]], [[youtube-1EZdpEhwmNc-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
