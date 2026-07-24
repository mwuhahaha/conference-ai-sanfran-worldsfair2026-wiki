---
title: "We Gave an Agent Production Code Access and Then Tried to Sleep at Night"
category: "talks"
date: "2026-06-29"
time: "11:40am-12:00pm"
track: "Security"
room: "Track 5"
speakers: ["Moritz Johner"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Security"
scheduleRoom: "Track 5"
scheduleLabels: ["Security", "Track 5", "sponsor", "confirmed"]
---
# We Gave an Agent Production Code Access and Then Tried to Sleep at Night

## Conference Context
- Date/time: 2026-06-29 · 11:40am-12:00pm
- Track/room: Security · Track 5
- Speaker(s): Moritz Johner
- Session type/status: sponsor · confirmed

- Track: Security
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
We let an agent touch production code to fix CVEs. That is either automation or a supply chain incident, depending on how honest your architecture is. PatchPilot started simple: find vulnerable dependencies, patch them, open a PR, let CI prove the fix, move on. Then reality showed up. The agent needed repository access, CI logs, credentials, and a Docker socket. Without that, it was useless. With it, every security reviewer in the room had a point. This is the production case study: what we gave the agent, what we refused, what infosec pushed back on, and where they were right. We will cover scoped permissions, constrained PRs, audit trails, approval gates, CI evidence, credential boundaries, and the gap between "it generated a patch" and "we can defend this change." Agentic remediation is not just developer productivity. It is a new participant in your software supply chain.

## Synthesis
### Transcript-Backed Summary
This talk argues that once an agent can touch production credentials, it is no longer just a coding assistant but a supply chain participant, so the real question is how to bound its authority. Patch Pilot answers that by splitting the system into a deterministic controller and a reasoning agent: the controller discovers vulnerable images, manages repository and PR actions, and enforces checks, while the agent is limited to making the smallest viable code changes and diagnosing failures. The main tradeoff is usefulness versus blast radius: the more freedom the agent gets, the more dangerous prompt injection, Docker socket access, and broad network privileges become, so the architecture pushes privileged actions out of the agent and into code that is easier to reason about. The practical consequence is a production remediation workflow that can fix CVEs, verify the result in CI, and still leave a human approval gate, while also exposing where current sandboxing and observability tooling remain immature.

### Key Takeaways
- After the agent edits files, the deterministic layer vets the changes, commits them, pushes a PR, and watches CI so the higher-risk actions stay outside the agent.
  - Evidence: "So we got to take care of that. And then we commit it, we push it, we create a PR, um and then we watch CI."
- The system had to be given GitHub access, registry credentials, runtime tools, and network access, showing that useful remediation requires substantial repository and environment visibility.
  - Evidence: "So, to make that work, um we gave Patch Pilot a couple of things. We gave it GitHub access, um read and write access to clone the repository, to commit, and to push changes, to open up PR, to download the CI logs, and trigger CI."
- Keeping GitHub push and CI-triggering abilities out of the agent reduces blast radius if prompt injection occurs.
  - Evidence: "Instead, we pushed um that functionality out to the deterministic part cuz that's the thing that we can reason about and we can rely on that um you know, it just does these kind of kind of actions and we do not give um the agent these kinds of credentials cuz that then fundamentally fundamentally limits the blast radius of when in case the agent gets um prompt injected prompt injected."
- Running with a Docker socket in production felt unsafe enough that the team moved away from that design.
  - Evidence: "We run it like that in production at some point. Um, it didn't feel good. We moved off of that, um, and we evaluated all the other obvious options in like the Linux sphere Linux bubble when it comes to like sandboxing."
- The speaker treats the choice of what is deterministic versus agentic as the security model itself.
  - Evidence: "Um that kind of really limits the blast radius of an agent. So, that choice, what's that what's deterministic and what's agentic, that really is, you know, your security model in this case."

### Claims From The Talk
- The speaker's central thesis is that a useful coding agent becomes a supply chain actor as soon as it gets production credentials, so the right comparison is to treat it with the same guardrails as an engineer rather than framing it as simply dangerous or safe. (`explicit`)
  - Evidence: "A useful coding agent is a supply chain actor, whether you plan for that or not. That's the thesis of this talk, basically."
- Patch Pilot separates deterministic orchestration from agentic reasoning so the agent handles the hard judgment calls while the controller handles the boring, predictable workflow. (`explicit`)
  - Evidence: "It's very simple. And inside that, we spawn agents. Now, these agents are there for the for the reasoning."
- The architecture deliberately withholds dangerous actions like pushing to GitHub or triggering CI from the agent itself and keeps them in the deterministic layer to reduce blast radius if the agent is prompt injected. (`explicit`)
  - Evidence: "The dangerous ones, the get up right access, um and trigger UCI is something that we did not give the agent."
- Giving an agent direct Docker socket access is presented as an unacceptable escalation point because it can escape the container and access host resources, so the talk treats that boundary as a major security failure mode. (`explicit`)
  - Evidence: "So, naturally you give it that Docker socket. At that point, it's more or less game over for you, um, because the agent can then simply just spawn a privileged container, escape out of it and then, you know, read environment variables of other processes, read the memory of other processes, can plant SSH keys, it's game over for you essentially at this point."
- The speaker concludes that an agent's blast radius is fundamentally an architecture decision, not just a tooling choice, because the split between deterministic and agentic behavior defines the security model. (`explicit`)
  - Evidence: "All right. If you take one thing from this, um the blast radius of an agent is an architecture decision."

### Topics Covered
- [[agent-security|Dependency patching at scale]] — How to remediate vulnerable dependencies across many repositories while keeping PRs reviewable and safe.
- [[agent-security|Agent supply-chain role]] — The idea that an agent with production credentials becomes part of the software supply chain.
- [[coding-agents|Two-layer agent architecture]] — Separating boring orchestration from agentic reasoning to reduce risk and increase reliability.
- [[agent-security|Prompt injection defense]] — Using tests and crafted repositories to check whether an agent can be manipulated by untrusted repository content.
- [[ai-sandboxes|Agent sandboxing]] — Containing an agent that needs Docker access by moving it into a micro-VM rather than a normal sandbox.
- [[agent-security|Blast radius control]] — Limiting the consequences of an agent mistake by keeping powerful actions outside the agent boundary.

### Tools And Named Systems
- **Patch Pilot** — The remediation system the speaker and team built to scan artifacts, fix CVEs, and produce PRs.
- **Dependabot** — A baseline dependency update tool that the speaker says only handles simpler manifest-bump cases.
- **Renovate** — A baseline dependency update tool mentioned alongside Dependabot for automated version bumps.
- [[docker|Docker]] — The containerization technology that creates the Docker socket exposure discussed in the talk.
- [[firecracker|Firecracker]] — The micro-VM technology proposed for stronger isolation around the agent and Docker socket.
- **Kaniko** — The package mentioned as one of the sandboxing or build options the speaker evaluated.

### Novel Concepts And Methods
- **Deterministic-controller split** — Use a two-layer architecture where deterministic code performs orchestration and privileged actions while the agent handles reasoning and small-file edits.
- **Minimal effective change set** — Constrain the agent to the smallest effective change set so it fixes only the CVE-linked issue instead of broadly upgrading dependencies.
- **Self-verification loop** — Have the agent verify its own work by rebuilding, rescanning, and then returning control to the controller for validation and cleanup.
- **Per-run retrospective** — Collect a short retrospective after each invocation so the system can aggregate what went wrong, what tools were missing, and what context would help next time.
- **Prompt-injection evaluation** — Use focused end-to-end tests against crafted repositories to probe for prompt injection and other known failure modes.
- **Micro-VM isolation** — Move the agent into a micro-VM with its own kernel when Docker socket access is required, so container escapes stay contained.

### Open Questions
- **How can teams discover and defend against unknown prompt-injection vectors that are not covered by existing crafted tests?** — The speaker says known vectors can be tested, but unknown ones still remain, so this is a core unresolved security problem.
- **Which sandbox or sandbox-as-a-service option can provide enterprise-grade containment for Docker socket access plus network policy control without excessive orchestration work?** — The talk says current options are uneven and often lack the exact controls needed for production deployment.
- **What is the right observability stack for agent behavior at scale so teams can aggregate failures and missing context across many PRs?** — The speaker describes observability for agent-in-the-loop systems as still open and being built by the community.

### Derived Links And Source Material
- [[youtube-LqLoYksJ6do-transcript]] — dedicated official recording transcript.
- [[youtube-LqLoYksJ6do]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/LqLoYksJ6do--2026-06-29-moritz-johner-we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.json`.

### Speaker Context
- [[moritz-johner|Moritz Johner]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[moritz-johner]]

## Official YouTube Recording
- [[youtube-LqLoYksJ6do|We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3]] — official AI Engineer YouTube recording published 2026-07-20.
- Evidence status: [[youtube-LqLoYksJ6do-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-LqLoYksJ6do]] - dedicated official event recording.
- [[youtube-LqLoYksJ6do-transcript]] - dedicated official recording transcript.

- [[youtube-LqLoYksJ6do-slides]] — extracted from the related public AI Engineer video.

- Source video: `youtube-LqLoYksJ6do`
- Slide deck: [[youtube-LqLoYksJ6do-slides|Slides: We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3]] — 5 visible slide image(s).
![[assets/slides/LqLoYksJ6do/slide-001.jpg]]
![[assets/slides/LqLoYksJ6do/slide-002.jpg]]
![[assets/slides/LqLoYksJ6do/slide-003.jpg]]
- Slide-derived themes for `youtube-LqLoYksJ6do`: code, gave, production, access, tried, sleep, night, track.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/LqLoYksJ6do.txt` (4,014 words).

## Transcript Markdown
- [[youtube-LqLoYksJ6do-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/LqLoYksJ6do.txt`.

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-LqLoYksJ6do` — 4,014 transcript words; 5 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-LqLoYksJ6do`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-LqLoYksJ6do`: case, docker, sandbox, access, repository, order, deterministic, give.
- Slide-derived themes for `youtube-LqLoYksJ6do`: code, gave, production, access, tried, sleep, night, track.
- Evidence links for `youtube-LqLoYksJ6do` (primary event evidence): [[youtube-LqLoYksJ6do]], [[youtube-LqLoYksJ6do-transcript]], [[youtube-LqLoYksJ6do-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
