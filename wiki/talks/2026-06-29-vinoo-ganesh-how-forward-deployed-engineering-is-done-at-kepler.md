---
title: "How Forward Deployed Engineering is done at Kepler"
category: "talks"
date: "2026-06-29"
time: "3:20pm-3:40pm"
track: "Forward Deployed Engineering"
room: "Track 8"
speakers: ["Vinoo Ganesh"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Forward Deployed Engineering"
scheduleRoom: "Track 8"
scheduleLabels: ["Forward Deployed Engineering", "Track 8", "session", "confirmed"]
---
# How Forward Deployed Engineering is done at Kepler

## Conference Context
- Date/time: 2026-06-29 · 3:20pm-3:40pm
- Track/room: Forward Deployed Engineering · Track 8
- Speaker(s): Vinoo Ganesh
- Session type/status: session · confirmed

- Track: Forward Deployed Engineering
- Room: Track 8
- Session type: session
- Status: confirmed

## Session Description
No official description published in the schedule data.

## Synthesis
### Transcript-Backed Summary
Vinoo Ganesh argues that forward deployed engineering is fundamentally a product strategy, not a sales support function. The core mechanism is to embed engineers with customers, observe real workflows, translate observed pain into canonical nouns and verbs, and ship the smallest fix that solves the actual problem. The talk emphasizes a key tradeoff: quick field fixes can create permanent production obligations, so FDEs have to decide carefully what becomes part of the core product and what should stay local. The practical result is product leverage: if the team gets the problem right and generalizes the solution, field work becomes a source of sticky platform capability rather than ad hoc customer service.

### Key Takeaways
- Treat customer requests as solution sketches and reframe them into the underlying problem before building.
  - Evidence: "What do we build? So I think of this in terms of an XY situation. Customers describe solutions not problems."
- Repeated, awkward, or frustrated user actions are strong signals that there is a product opportunity.
  - Evidence: "Anytime a user copies and pastes between tools, meaning if they're moving from one tool to another, anytime they're reacting this way, if the first thing you say is, \"Hey, how do you feel about this problem?\" And their reaction is, \"Well, I have to.\" And this visceral exasperation, you know, you have an opportunity there."
- Go on site and get the truth from the environment where the work actually happens.
  - Evidence: "Everything lives in that environment. And you can't survey your way to this. You have to be physically present."
- Define the nouns and verbs of the domain so the product can become the customer's shared language.
  - Evidence: "And so when I say define the language, every organization is made up of two things, nouns and verbs."
- Assume any useful workaround may live for a long time, so ship with production consequences in mind.
  - Evidence: "If it solves a problem, it's not temporary. It will live forever. So, as you're thinking from an FTE perspective, ship everything like it's going to run for 18 months because it probably will."

### Claims From The Talk
- Forward deployed engineering is presented as a product strategy, not a go-to-market role. (`explicit`)
  - Evidence: "Um this is a quote from the guy who named uh forward deploy engineering at Palanteer. It's from a couple days ago and um Sham is the CTO of Palunteer right now and I think this captures the entire essence of where my difficulty came from in the last talk which is the first fundamental truth of FTE is that this is not a role this is a product strategy how we discover the things to build are through the lens of forward deploy engineering."
- The Phoenix example is used to argue that building in isolation can fail when a system meets real customer data and workflows. (`explicit`)
  - Evidence: "What we did is we designed a system in perfect isolation that worked perfectly under certain circumstances and crashed and burned when we hit actual real data."
- The speaker argues that the right response to a field problem is to identify the real workflow and ship the smallest useful fix quickly. (`explicit`)
  - Evidence: "In 4 hours, we were able to solve this problem cradle to grave. The first move that we learned from forward deployed perspective is detect the real problem and ship the real thing."
- The parquet viewer story is used to show that on-site observation can reveal the real blocker behind a customer objection and unlock adoption. (`explicit`)
  - Evidence: "That night we built a parquet viewer. She approved the migration in the next 2 days massively reducing data costs."
- The talk claims that defining an enterprise's language and ontology creates durable product leverage because users adopt the platform's terms. (`explicit`)
  - Evidence: "And so when you are able to define the vocabulary that users use and codify that in your platform, you become the foundation under which every solution and tool is built on top of foundry enabled that ontology to be constructed and built."
- The speaker argues that temporary hacks usually become long-lived production obligations, so every fix should be designed as if it will run for a long time. (`explicit`)
  - Evidence: "If it solves a problem, it's not temporary. It will live forever. So, as you're thinking from an FTE perspective, ship everything like it's going to run for 18 months because it probably will."
- Kepler is positioned as using FDE as an extension of the product function to build sticky products that solve real problems. (`explicit`)
  - Evidence: "your job as an FTE and what we learned and what Kepler is doing is using FTEE as an extension of the product function to enable us to build products that are actually sticky and that solve problems."

### Topics Covered
- [[software-factories|Forward Deployed Engineering]] — Using field deployment as a way to discover, shape, and generalize product requirements.
- [[software-factories|Enterprise Ontology]] — The enterprise-level naming layer that defines shared entities, actions, and boundaries.
- [[software-factories|On-Site Workflow Observation]] — Learning from customers by watching the work where it actually happens.
- [[software-factories|Product Leverage]] — Turning one-off field fixes into reusable product capability across customers.
- [[forward-deployed-engineering|Productionizing Hacks]] — The risk that temporary hacks become permanent support burdens once they reach production.

### Tools And Named Systems
- [[foundry|Foundry]] — The product platform the speaker says was shaped by forward deployed engineering as a product strategy.
- [[slack|Slack]] — The alerting workflow built as the minimal fix for the shipping dispatcher problem.
- **Cassandra** — The storage system whose file-handle and memory behavior made the initial Phoenix design fail at scale.

### Novel Concepts And Methods
- **Problem Reframing** — Detect the real problem and ship the real thing instead of implementing the customer's first requested solution.
- **On-Site Observation** — Observe users on site to learn the actual workflow rather than relying on docs, surveys, or requirements documents.
- **Ontology Design** — Canonicalize enterprise terminology into an ontology of nouns and verbs that the platform can own.
- **Production Calibration** — Calibrate each shipped fix against product-wide tradeoffs before deciding whether it belongs in the core product.
- **Field-to-Product Generalization** — Convert field fixes into reusable product leverage by generalizing them across customers.

### Open Questions
- **How should an FDE decide when a field workaround belongs in the core product versus the local customer stack?** — This determines whether the team builds durable product leverage or accumulates support debt.
- **Which nouns and verbs should become the canonical ontology when different teams use the same term differently?** — The answer affects integration reliability, product clarity, and whether the platform becomes the shared language.
- **How can an early-stage company keep FDE tied to product discovery instead of sliding into go-to-market support?** — The speaker argues that this boundary changes what the company learns and what it can scale.

### Derived Links And Source Material
- [[youtube-1OMHGsUZiqA-transcript]] — dedicated official recording transcript.
- [[youtube-1OMHGsUZiqA]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/1OMHGsUZiqA--2026-06-29-vinoo-ganesh-how-forward-deployed-engineering-is-done-at-kepler.json`.

### Speaker Context
- [[vinoo-ganesh|Vinoo Ganesh]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[vinoo-ganesh]]

## Official YouTube Recording
- [[youtube-1OMHGsUZiqA|How Forward Deployed Engineering is done at Kepler — Vinoo Ganesh]] — official AI Engineer YouTube recording published 2026-07-28.
- Evidence status: [[youtube-1OMHGsUZiqA-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-1OMHGsUZiqA]] - dedicated official event recording.
- [[youtube-1OMHGsUZiqA-transcript]] - dedicated official recording transcript.

- Source video: `youtube-1OMHGsUZiqA`
- Slide deck: [[youtube-1OMHGsUZiqA-slides|Slides: How Forward Deployed Engineering is done at Kepler — Vinoo Ganesh]] — 9 visible slide image(s).
![[assets/slides/1OMHGsUZiqA/slide-001.jpg]]
![[assets/slides/1OMHGsUZiqA/slide-002.jpg]]
![[assets/slides/1OMHGsUZiqA/slide-003.jpg]]
- Slide-derived themes for `youtube-1OMHGsUZiqA`: fair, track, june, learned, tale, engineering, future, whoever.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/1OMHGsUZiqA.txt` (4,041 words).

## Transcript Markdown
- [[youtube-1OMHGsUZiqA-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/1OMHGsUZiqA.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-1OMHGsUZiqA` — 4,041 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-1OMHGsUZiqA`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-1OMHGsUZiqA`: product, problem, customer, data, define, forward, software, first.
- Slide-derived themes for `youtube-1OMHGsUZiqA`: fair, track, june, learned, tale, engineering, future, whoever.
- Evidence links for `youtube-1OMHGsUZiqA` (primary event evidence): [[youtube-1OMHGsUZiqA]], [[youtube-1OMHGsUZiqA-transcript]], [[youtube-1OMHGsUZiqA-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
