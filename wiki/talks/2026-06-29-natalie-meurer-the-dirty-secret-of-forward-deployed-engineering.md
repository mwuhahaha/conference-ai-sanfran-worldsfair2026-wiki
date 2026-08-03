---
title: "The Dirty Secret of Forward Deployed Engineering"
category: "talks"
date: "2026-06-29"
time: "1:30pm-1:50pm"
track: "Forward Deployed Engineering"
room: "Track 8"
speakers: ["Natalie Meurer"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Forward Deployed Engineering"
scheduleRoom: "Track 8"
scheduleLabels: ["Forward Deployed Engineering", "Track 8", "session", "confirmed"]
---
# The Dirty Secret of Forward Deployed Engineering

## Conference Context
- Date/time: 2026-06-29 · 1:30pm-1:50pm
- Track/room: Forward Deployed Engineering · Track 8
- Speaker(s): Natalie Meurer
- Session type/status: session · confirmed

- Track: Forward Deployed Engineering
- Room: Track 8
- Session type: session
- Status: confirmed

## Session Description
Since its origins at Palantir, the term "Forward Deployed Engineer" has described wildly different jobs, yet today it's one of the fastest-growing roles in AI. What happened? And what does that reveal about the future of engineering? Join Nat Meurer, Head of Agent Engineering at Sierra, for a historical tour of one of tech's most misunderstood roles, and why its biggest contradiction may explain where the industry is headed next.

## Synthesis
### Transcript-Backed Summary
The speaker argues that forward deployed engineering began as a concrete, on-the-ground role at Palantir, but over time accumulated DevOps, data integration, custom solutioning, and customer enablement until the label stopped naming one job. Her core mechanism is a customer-accountability loop: engineers translate customer needs into deployment work, data models, and product changes, and AI now amplifies that loop by making code cheap and end-to-end solution building faster. She concludes that as product engineering becomes more client-facing and pricing shifts toward outcomes, forward deployed engineering is less a narrow specialty than a direction the whole engineering stack is moving toward.

### Key Takeaways
- Forward deployed engineering is best understood as a bundle of customer-facing responsibilities rather than a single stable job title.
  - Evidence: "And so if you're confused, that's sort of what this talk is about. And so the dirty secret of forward deployed engineering, I won't make you wait until the end, is it doesn't exist."
- The role expanded from deployment work into data integration and ontology-driven modeling of customer data.
  - Evidence: "And what Palantir uh did then and now still does call an ontology, which is sort of a famous Palantir um term of art."
- Once platforms matured, enabling customers to do the work themselves became part of the job.
  - Evidence: "So, this is basically where the forward deployed engineers or the deployment strategists would go in and actually teach customers to use the software."
- Outcome-based pricing makes customer outcome ownership a structural requirement, not just a nice-to-have.
  - Evidence: "So, if you have both of these things, you have forward-deployed engineers that can now contribute to the product, you have more outcome-based pricing, how do you actually guarantee the outcome?"

### Claims From The Talk
- The speaker argues that forward deployed engineering no longer names one coherent job and has become too broad to define cleanly. (`explicit`)
  - Evidence: "And so if you're confused, that's sort of what this talk is about. And so the dirty secret of forward deployed engineering, I won't make you wait until the end, is it doesn't exist."
- She reports that early forward deployed engineering at Palantir was largely about deployment and customer-side operational fixes, including late-night support. (`explicit`)
  - Evidence: "Hey, could you look into it? By the way, it's 2:00 a.m. and you need to go in. Um and so, in practice, a lot of the early forward-deployed engineering was was really focused on DevOps."
- She says the role later absorbed data integration work and ontology-based modeling of customer data. (`explicit`)
  - Evidence: "And what Palantir uh did then and now still does call an ontology, which is sort of a famous Palantir um term of art."
- She argues that the Foundry era shifted the emphasis toward making data useful and turning it into decision-making support. (`explicit`)
  - Evidence: "And the era of Foundry was effectively all about um making data useful. So, Palantir had this phrase of uh going from data to decision-making, which was was sort of the core problem."
- She argues that modern AI lets forward deployed engineers build end-to-end solutions with coding agents instead of only talking to customers or prototyping. (`explicit`)
  - Evidence: "So forward deployed engineers can now not just talk to customers, not just prototype, but actually build end-to-end solutions with coding agents."
- She concludes that agent engineering is only a subset or flavor of forward deployed engineering and that most engineering roles are trending in that direction. (`explicit`)
  - Evidence: "But these days, I'm actually of a different mind, which is that um really in some ways everything is forward deployed engineering, or at least everything is trending that way."

### Topics Covered
- [[software-factories|Forward deployed engineering]] — The evolving role that mixes deployment, integration, solutioning, and customer ownership.
- [[software-factories|Customer accountability]] — The obligation to own customer-facing results across technical work.
- [[forward-deployed-engineering|Outcome-based pricing]] — A pricing model where revenue is tied to delivered business outcomes.
- [[software-factories|Product-engineering convergence]] — The blurring line between product work and field-facing implementation work.
- [[software-factories|Agent engineering]] — A discipline focused on building and deploying AI agents with customer outcome focus.

### Tools And Named Systems
- **EC2** — The deployment target used in the early Palantir example of getting software running.
- **Slate** — The drag-and-drop builder used for mapping page components to data sources.
- [[foundry|Foundry]] — The main Palantir platform discussed as making data useful.
- **AIFTE** — The later platform the speaker says uses large language models for similar work.

### Novel Concepts And Methods
- **Ontology-based data modeling** — Using ontology-based data modeling to translate customer data into a usable structure.
- **Customer enablement bootcamp** — Running customer enablement sessions so customers can do work previously handled by deployment specialists.
- **Customer-accountable development loop** — Maintaining a customer-accountable development loop that turns field feedback into product changes.
- **Coding-agent-assisted solutioning** — Building end-to-end solutions with coding agents as part of the delivery workflow.

### Open Questions
- **Where should the boundary sit between forward deployed engineering and product engineering as the two roles become more client-facing?** — The talk claims the roles are converging, so teams need a workable division of labor.
- **How do companies guarantee customer outcomes when pricing is tied to outcomes rather than seats or usage?** — The speaker treats outcome assurance as the central challenge of the new model.
- **Which parts of the historical forward deployed engineering stack still matter once coding agents can generate substantial implementation work?** — This determines whether the role shrinks, changes shape, or becomes more strategically important.

### Derived Links And Source Material
- [[youtube-Byv311hdoHE-transcript]] — dedicated official recording transcript.
- [[youtube-Byv311hdoHE]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/Byv311hdoHE--2026-06-29-natalie-meurer-the-dirty-secret-of-forward-deployed-engineering.json`.

### Speaker Context
- [[natalie-meurer|Natalie Meurer]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[natalie-meurer]]

## Official YouTube Recording
- [[youtube-Byv311hdoHE|The Dirty Secret of Forward Deployed Engineering — Natalie Meurer, Sierra]] — official AI Engineer YouTube recording published 2026-07-28.
- Evidence status: [[youtube-Byv311hdoHE-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-Byv311hdoHE]] - dedicated official event recording.
- [[youtube-Byv311hdoHE-transcript]] - dedicated official recording transcript.

- Source video: `youtube-Byv311hdoHE`
- Slide deck: [[youtube-Byv311hdoHE-slides|Slides: The Dirty Secret of Forward Deployed Engineering — Natalie Meurer, Sierra]] — 31 visible slide image(s).
![[assets/slides/Byv311hdoHE/slide-001.jpg]]
![[assets/slides/Byv311hdoHE/slide-002.jpg]]
![[assets/slides/Byv311hdoHE/slide-003.jpg]]
- Slide-derived themes for `youtube-Byv311hdoHE`: track, june, engineering, deployed, forward, future, eras, georgetown.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/Byv311hdoHE.txt` (3,109 words).

## Transcript Markdown
- [[youtube-Byv311hdoHE-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/Byv311hdoHE.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-Byv311hdoHE` — 3,109 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Byv311hdoHE`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Byv311hdoHE`: engineering, deployed, forward, data, palantir, engineer, software, engineers.
- Slide-derived themes for `youtube-Byv311hdoHE`: track, june, engineering, deployed, forward, future, eras, georgetown.
- Evidence links for `youtube-Byv311hdoHE` (primary event evidence): [[youtube-Byv311hdoHE]], [[youtube-Byv311hdoHE-transcript]], [[youtube-Byv311hdoHE-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
