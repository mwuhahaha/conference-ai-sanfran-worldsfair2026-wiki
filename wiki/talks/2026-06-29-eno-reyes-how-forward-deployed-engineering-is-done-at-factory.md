---
title: "How Forward Deployed Engineering is done at Factory"
category: "talks"
date: "2026-06-29"
time: "10:45am-11:05am"
track: "Forward Deployed Engineering"
room: "Track 8"
speakers: ["Eno Reyes"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Forward Deployed Engineering"
scheduleRoom: "Track 8"
scheduleLabels: ["Forward Deployed Engineering", "Track 8", "session", "confirmed"]
---
# How Forward Deployed Engineering is done at Factory

## Conference Context
- Date/time: 2026-06-29 · 10:45am-11:05am
- Track/room: Forward Deployed Engineering · Track 8
- Speaker(s): Eno Reyes
- Session type/status: session · confirmed

- Track: Forward Deployed Engineering
- Room: Track 8
- Session type: session
- Status: confirmed

## Session Description
No official description published in the schedule data.

## Synthesis
### Transcript-Backed Summary
Reyes argues that forward deployed engineering at Factory is not consulting, but a product function that embeds engineers with customers to learn how software work actually happens and feed that knowledge back into the platform. The mechanism is a software-factory loop: customer signals become prioritized plans, code changes, validation, and deployment, with deployed engineers helping make that loop increasingly autonomous through deterministic checks, better harnesses, and agent-ready workflows. The main tradeoff is that autonomy is not something you can simply buy or switch on; it requires model independence, trace ownership, governance, and careful redesign of the environment so verification is possible without disrupting human developers. The practical consequence is a role shift from directly manipulating code to designing and operating the system that builds code, with the clearest wins in bounded, verifiable workflows that can scale across large enterprise codebases.

### Key Takeaways
- More validation capacity means more room for autonomous agent work, so validation density is a direct lever for autonomy.
  - Evidence: "And so, if you introduce the ability to validate at scale, then you introduce increasing autonomy to the org."
- The hard part is often preparing the environment for verification, not solving the underlying task itself.
  - Evidence: "Less so solving the problem, more so preparing the environment for verification of the problem.\" And by the way, if you're familiar with how these models are actually trained, like this makes total sense, right?"
- Tasks that can be framed as verifiable completion problems are the best candidates for long-running agent execution.
  - Evidence: "So if you can frame any problem as the set of verification uh systems that need to validate it, then you can solve that problem with AI today."
- A convincing example of autonomy has to feel achievable enough to copy, not so extreme that the rest of the organization dismisses it as a theme park.
  - Evidence: "I just can't see how that would apply to the way that we currently work today, right?\" So it's kind of a delicate balance that you have to walk of building something that demonstrates the future is achievable enough, but ultimately does not scare away uh an org who is thinking, \"Man, what is going"

### Claims From The Talk
- Reyes says deployed engineers should act as the product feedback channel from major customers back into Factory's engineering leadership, not as a customer-services layer. (`strong`)
  - Evidence: "And I'm going to do this and then go back. But but really when we say the tip of the spear, what we mean is that deployed engineers are basically the stream of information from our largest and most critical customers of the engineering leadership in that org."
- He argues that Factory does not want deployed engineers doing consulting-style migrations or other professional services work on behalf of customers. (`explicit`)
  - Evidence: "Uh and I think that the the at least at Factory, we definitely do not want to be doing professional services work on behalf of a customer."
- He describes a software factory as a loop where signals are prioritized, turned into code changes, validated, deployed, and then turned back into new signals. (`explicit`)
  - Evidence: "And if you're able to take AI and actually transform each of these stages of the pipeline and build an understanding of what the workflow looks like at your org from each stage to each stage, then you actually can get to the point where you have a a flow through from signal to deploy that has no human intervention."
- He says enterprise use requires model independence, access to the data and traces that flow through the system, and centralized governance with control over where information goes. (`explicit`)
  - Evidence: "And so with Droid, the hardness that we build, you not only have model independence, but you also have access to every piece of data that flows in in and out of Droid, alongside centralized governance and control at the enterprise layer to be able to dictate where what information flows where."
- He argues that agent readiness is mainly a matter of having enough deterministic validation loops, because that lets agents work longer and more autonomously on harder tasks. (`explicit`)
  - Evidence: "Uh, when you have a huge volume of these feedback loops, uh, agents are able to operate for greater periods of time on more complex tasks without human intervention."
- He reports that some workflows, such as legal droid, are already effectively fully autonomous, while visual terminal problems remain hard to verify. (`explicit`)
  - Evidence: "Like we have something we call like legal droid, which is our legal workflow. That is effectively 100% autonomously maintained, but our like core harness, uh we do not yet have validators that can validate some of the hard visual problems of a like terminal based harness."

### Topics Covered
- [[software-factories|forward deployed engineering]] — The practice of embedding engineers with customers to shape the product from real operational context.
- [[software-factories|software factory]] — An end-to-end organizational loop that converts signals into validated software changes and deployment.
- **agent readiness** — The degree to which a codebase and workflow can support longer autonomous agent execution.
- [[agent-evaluations|deterministic validation loops]] — The presence of clear pass-fail checks, scans, and tests that make automation verifiable.
- [[software-factories|autonomy maturity model]] — The idea that organizations need a roadmap for moving toward autonomous software operation.
- [[inference-engineering|model independence]] — The need to own the model layer rather than depend on a single vendor or opaque runtime.

### Tools And Named Systems
- **Droid** — Factory's deployed-engineer platform and enterprise harness layer for building autonomous software engineering workflows.
- **missions** — Factory's long-running harness for difficult, validatable knowledge-work tasks.
- **legal droid** — An autonomous legal workflow that Reyes says is already effectively fully maintained by the system.

### Novel Concepts And Methods
- **customer feedback loop** — Use deployed engineers as a customer-to-product feedback loop that captures how work happens in real organizations and feeds that back into the platform.
- **software factory pipeline** — Model the organization as a software factory that moves from signals to plans to code to validation to deploy and then back into new signals.
- **agent readiness profiling** — Increase autonomy by measuring and expanding deterministic validation coverage before expecting agents to handle longer tasks.
- **verifiable long-running harness** — Run long-lived harnesses where planning is explicit, execution continues until verification says the task is done, and human intervention stays minimal.
- **environment-first adoption** — Prepare the environment for verification instead of trying to solve the task directly, so automation can close the loop safely.

### Open Questions
- **How can teams introduce stronger automated validation without disrupting the human developers' existing flow?** — The talk makes clear that validation can raise autonomy, but only if it fits the way people actually work.
- **What validators can reliably catch hard visual terminal failures like flickering so the loop can truly close?** — The speaker identifies visual failure modes as a current blocker to more complete autonomy.
- **What autonomy maturity model should an organization use to decide how to move from direct coding to managing a software-building system?** — Reyes says most organizations do not yet have a roadmap for that transition.

### Derived Links And Source Material
- [[youtube-wpOA-UXynoM-transcript]] — dedicated official recording transcript.
- [[youtube-wpOA-UXynoM]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/wpOA-UXynoM--2026-06-29-eno-reyes-how-forward-deployed-engineering-is-done-at-factory.json`.

### Speaker Context
- [[eno-reyes|Eno Reyes]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[eno-reyes]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-ShuJ_CN6zr4-dense-slides]] (2 viable slide images).
- Related slide/OCR pages:
- [[youtube-ShuJ_CN6zr4-dense-slides]]
- [[youtube-ShuJ_CN6zr4-reconstructed-slides]]
- [[youtube-ShuJ_CN6zr4-slides]]
- Slide-derived terms: `factory`, `codebases`, `summit`, `autonomous`, `engineering`, `systems`, `make`, `ready`, `cocle`, `pastas`, `code`, `making`, `agent-ready`, `creme`, `enoreves`, `ctoeco-rouncer`

## Official YouTube Recording
- [[youtube-wpOA-UXynoM|How Forward Deployed Engineering is done at Factory — Eno Reyes]] — official AI Engineer YouTube recording published 2026-07-28.
- Evidence status: [[youtube-wpOA-UXynoM-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-wpOA-UXynoM]] - dedicated official event recording.
- [[youtube-wpOA-UXynoM-transcript]] - dedicated official recording transcript.
- [[youtube-ShuJ_CN6zr4]] - supporting context; not the exact session recording.

- Source video: `youtube-wpOA-UXynoM`
- Slide deck: [[youtube-wpOA-UXynoM-slides|Slides: How Forward Deployed Engineering is done at Factory — Eno Reyes]] — 6 visible slide image(s).
![[assets/slides/wpOA-UXynoM/slide-001.jpg]]
![[assets/slides/wpOA-UXynoM/slide-002.jpg]]
![[assets/slides/wpOA-UXynoM/slide-003.jpg]]
- Slide-derived themes for `youtube-wpOA-UXynoM`: missions, microsoft, works, fact, hand, model, rosa, forward.
- Source video: `youtube-ShuJ_CN6zr4`
- Slide deck: [[youtube-ShuJ_CN6zr4-dense-slides|Dense Slides: Making Codebases Agent Ready – Eno Reyes, Factory AI]] — slide evidence page.
- Additional slide evidence: [[youtube-ShuJ_CN6zr4-slides|Slides: Making Codebases Agent Ready – Eno Reyes, Factory AI]], [[youtube-ShuJ_CN6zr4-reconstructed-slides|Reconstructed Slides: Making Codebases Agent Ready – Eno Reyes, Factory AI]]
- Slide-derived themes for `youtube-ShuJ_CN6zr4`: autonomous, engineering, systems, ready, making.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/wpOA-UXynoM.txt` (3,822 words).

## Transcript Markdown
- [[youtube-wpOA-UXynoM-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/wpOA-UXynoM.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-wpOA-UXynoM` — 3,822 transcript words; 5 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-wpOA-UXynoM`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-wpOA-UXynoM`: software, factory, code, deployed, product, engineering, engineers, model.
- Slide-derived themes for `youtube-wpOA-UXynoM`: missions, microsoft, works, fact, hand, model, rosa, forward.
- Evidence links for `youtube-wpOA-UXynoM` (primary event evidence): [[youtube-wpOA-UXynoM]], [[youtube-wpOA-UXynoM-transcript]], [[youtube-wpOA-UXynoM-slides]]
- `youtube-ShuJ_CN6zr4` — 3 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-ShuJ_CN6zr4`: autonomous, engineering, systems, ready, making.
- Evidence links for `youtube-ShuJ_CN6zr4` (supporting context only): [[youtube-ShuJ_CN6zr4]], [[youtube-ShuJ_CN6zr4-slides]], [[youtube-ShuJ_CN6zr4-dense-slides]], [[youtube-ShuJ_CN6zr4-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
