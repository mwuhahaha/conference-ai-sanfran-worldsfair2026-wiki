---
title: "How Forward Deployed Engineering is done at Ramp"
category: "talks"
date: "2026-06-29"
time: "2:25pm-2:45pm"
track: "Forward Deployed Engineering"
room: "Track 8"
speakers: ["Leo Mehr"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Forward Deployed Engineering"
scheduleRoom: "Track 8"
scheduleLabels: ["Forward Deployed Engineering", "Track 8", "session", "confirmed"]
---
# How Forward Deployed Engineering is done at Ramp

## Conference Context
- Date/time: 2026-06-29 · 2:25pm-2:45pm
- Track/room: Forward Deployed Engineering · Track 8
- Speaker(s): Leo Mehr
- Session type/status: session · confirmed

- Track: Forward Deployed Engineering
- Room: Track 8
- Session type: session
- Status: confirmed

## Session Description
No official description published in the schedule data.

## Synthesis
### Transcript-Backed Summary
The talk argues that forward deployed engineering at Ramp is not about indiscriminately saying yes to enterprise customers, but about combining disciplined scoping with agent-driven scaling. The first principle is to ask enough questions to understand the real need, the viable workaround, the technical constraints, and the broader set of customers who might benefit before building anything. The second principle is to treat the FDE workflow as a pipeline that agents can increasingly handle, while humans retain taste and judgment over the final output. The practical consequence is a faster, more reliable enterprise delivery function: request intake can move from hours or days to seconds, and the team can reclaim meaningful time for higher-value work without turning the process into low-quality automation.

### Key Takeaways
- Good FDE work starts with gathering context instead of reacting to the first customer ask.
  - Evidence: "So, that's like one example. [clears throat] But, you know, as an FDE, you're asking tons of questions to gather context about what's important um and what actually is the right thing to build."
- Even apparently small assumptions, like which mobile platform is required, can make a large implementation effort useless if they are not validated early.
  - Evidence: "But like obviously it was super disappointing for us because we'd put all this effort in. And so, it was a a big lesson for us to remember the importance of scoping."
- A simple agent that asks a few clarifying questions can already remove a large amount of manual scoping work.
  - Evidence: "And so, you can see here what we what we did then was we basically um used Notion uh Notion agents to build a V1, which literally just took the request and asked a couple of questions."
- Agent automation without disciplined scoping can produce a high-volume but low-quality output stream.
  - Evidence: "But the problem isn't to tie this to the first half of the talk. If you don't do a good job of scoping out requests or or building upon the principles of scoping things well, you're going to get a token maxing slop cannon."
- The speaker's practical conclusion is that future FDE work needs both strong scoping and strong agent scaling.
  - Evidence: "that's why um in the end here, I want to close with the the the most important thing is that if you have both of these, it can set you up for success in the future."

### Claims From The Talk
- At Ramp, forward deployed engineering sits inside the engineering organization and is aimed at helping the company win upmarket. (`explicit`)
  - Evidence: "So, FDE at Ramp, uh we live within the engineering organization. And our goal is to help Ramp win upmarket."
- The team works on the core product and new agentic features, with the goal of making them work well for the largest enterprise customers. (`explicit`)
  - Evidence: "So, with that in mind, what we do is we basically work on the core product and our new agentic features and make them work really well for our largest enterprise customers."
- The speaker argues that an FDE's job is not to blindly say yes to every customer request. (`explicit`)
  - Evidence: "So, I would say there's this thing where like people many many people think that as an FDE, your job is to just say yes to the customer."
- Gathering context across the request, workarounds, technical constraints, and other prospects helps the team build the right thing. (`explicit`)
  - Evidence: "And the point is that by gaining all this context, you can do a better job of building the right thing."
- The mobile reimbursement example is used to show that even basic assumptions like platform choice must be validated up front. (`explicit`)
  - Evidence: "Even some of the most basic assumptions like which you know mobile platform you build on it's it's super important um to validate them and and thus kind of emphasizes the importance of scoping up front."
- The speaker says the whole FDE lifecycle, from context gathering through implementation, can be replaced or assisted by agents. (`explicit`)
  - Evidence: "From gathering context to scoping out a request to writing out a spec and then implementing the feature, each stage of that pipeline can be replaced with agents."
- Ramp's initial Notion-agent workflow reduced request reply latency from hours or days to seconds. (`explicit`)
  - Evidence: "That was it. And um after It was kind of astonishing. Literally, after a couple of weeks, we found that it was like saving us a lot of time because, first of all, immediate like the latency of replies went from like hours or days to like, you know, seconds."
- The newer multi-turn request triage workflow is described as saving roughly 20% of the time spent on scoping requests. (`explicit`)
  - Evidence: "And it's actually been incredible how helpful this has been for us. I I would say it's probably saved us like a large percentage, I don't know, 20% of the time that we'd spend on scoping out these requests."

### Topics Covered
- [[software-factories|Forward deployed engineering]] — Forward deployed engineers work inside engineering but focus on helping enterprise customers succeed through product adaptation and delivery.
- [[software-factories|Enterprise scoping]] — A disciplined approach to deciding what to build by validating urgency, workarounds, technical constraints, and reuse across customers.
- **Agentic workflow automation** — Using agents to automate stages of a professional workflow rather than only individual tasks.
- [[agent-memory|Context provisioning]] — The need to supply agents with the right background knowledge, product context, and state before they act.
- [[software-factories|Human judgment in automation]] — Balancing automation with human taste and judgment over the final result.
- [[platform-context-and-collaboration|Request triage]] — A workflow pattern where a vague request is turned into a structured specification through repeated questioning.

### Tools And Named Systems
- [[notion|Notion]] — The company uses this workspace system as part of its request workflow and the speaker cites it as the medium for the intake flow.
- **Notion agents** — An agent-based version of the intake workflow is used to ask clarifying questions and accelerate request handling.
- **SAP S/4HANA** — The integration named in the urgent enterprise request example that illustrates the need for scoping before implementation.

### Novel Concepts And Methods
- **Always be scoping** — Validate the real need behind a customer request before committing to implementation, instead of defaulting to a yes.
- **Scale with tokens** — Treat the FDE workflow as a pipeline that can be progressively delegated to agents, from request intake to spec creation to implementation.
- **Agentic request triage** — Use repeated back-and-forth questioning to turn a vague request into a well-shaped spec.
- **Quality gating for agent workflows** — Measure and improve agent output quality with evals, rubrics, and human feedback.
- **Human-in-the-loop final judgment** — Preserve human taste and judgment over the final output even when agents handle most of the workflow.

### Open Questions
- **How can a product team's tacit knowledge be encoded into agents more completely than docs and help articles allow?** — The talk identifies context as one of the hardest problems in scaling FDE work with agents.
- **What harness, eval, and feedback design best ensures each stage of the agent pipeline produces reliable output?** — The speaker says output quality is a major challenge when replacing manual FDE steps with agents.
- **What does a robust agent harness look like for running intake, scoping, and implementation steps smoothly at scale?** — This is presented as a core engineering problem for the next phase of FDE at Ramp.

### Derived Links And Source Material
- [[youtube-ITMXwI6QL6A-transcript]] — dedicated official recording transcript.
- [[youtube-ITMXwI6QL6A]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/ITMXwI6QL6A--2026-06-29-leo-mehr-how-forward-deployed-engineering-is-done-at-ramp.json`.

### Speaker Context
- [[leo-mehr|Leo Mehr]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[leo-mehr]]

## Official YouTube Recording
- [[youtube-ITMXwI6QL6A|How Forward Deployed Engineering is done at Ramp — Leo Mehr]] — official AI Engineer YouTube recording published 2026-07-28.
- Evidence status: [[youtube-ITMXwI6QL6A-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-ITMXwI6QL6A]] - dedicated official event recording.
- [[youtube-ITMXwI6QL6A-transcript]] - dedicated official recording transcript.

- Source video: `youtube-ITMXwI6QL6A`
- Slide deck: [[youtube-ITMXwI6QL6A-slides|Slides: How Forward Deployed Engineering is done at Ramp — Leo Mehr]] — 6 visible slide image(s).
![[assets/slides/ITMXwI6QL6A/slide-001.jpg]]
![[assets/slides/ITMXwI6QL6A/slide-002.jpg]]
![[assets/slides/ITMXwI6QL6A/slide-003.jpg]]
- Slide-derived themes for `youtube-ITMXwI6QL6A`: engineering, director, ramp, joined, future, forward, deployed, track.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/ITMXwI6QL6A.txt` (2,356 words).

## Transcript Markdown
- [[youtube-ITMXwI6QL6A-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/ITMXwI6QL6A.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-ITMXwI6QL6A` — 2,356 transcript words; 4 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-ITMXwI6QL6A`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-ITMXwI6QL6A`: scoping, customer, important, ramp, first, super, most, notion.
- Slide-derived themes for `youtube-ITMXwI6QL6A`: engineering, director, ramp, joined, future, forward, deployed, track.
- Evidence links for `youtube-ITMXwI6QL6A` (primary event evidence): [[youtube-ITMXwI6QL6A]], [[youtube-ITMXwI6QL6A-transcript]], [[youtube-ITMXwI6QL6A-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
