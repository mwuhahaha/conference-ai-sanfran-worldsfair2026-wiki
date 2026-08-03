---
title: "How Forward Deployed Engineering is done at Cognition"
category: "talks"
date: "2026-06-29"
time: "12:05pm-12:25pm"
track: "Forward Deployed Engineering"
room: "Track 8"
speakers: ["Jia Wu"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Forward Deployed Engineering"
scheduleRoom: "Track 8"
scheduleLabels: ["Forward Deployed Engineering", "Track 8", "session", "confirmed"]
---
# How Forward Deployed Engineering is done at Cognition

## Conference Context
- Date/time: 2026-06-29 · 12:05pm-12:25pm
- Track/room: Forward Deployed Engineering · Track 8
- Speaker(s): Jia Wu
- Session type/status: session · confirmed

- Track: Forward Deployed Engineering
- Room: Track 8
- Session type: session
- Status: confirmed

## Session Description
No official description published in the schedule data.

## Synthesis
### Transcript-Backed Summary
The talk argues that forward-deployed engineering is how Cognition turns Devin from a generic agent into enterprise leverage: engineers embed with customers, learn the real problem space, and map those problems back into product capabilities. The mechanism is not token-maxing or loose agent deployment; it is tight coupling between customer calls, hands-on implementation, field feedback, and measurable outcomes such as productive sessions, PR throughput, and delivery speed. The main tradeoff is that this motion demands both broad customer and business judgment plus deep technical expertise, but the payoff is a stronger product feedback loop, faster delivery, and larger organizational impact than single-point developer tools can achieve.

### Key Takeaways
- Deploy agents where they maximize overlap between product capability and customer pain, not as generic automation.
  - Evidence: "So, the forward-deployed motion at Cognition essentially aims to maximize the overlap between the products that we typically build and the problems that we're experiencing across the enterprise."
- The hardest enterprise software work is usually testing, review, deployment, and maintenance, not code generation itself.
  - Evidence: "But the problem isn't like writing code faster, that's usually only 20% of the problem. The problem really just becomes like how do you test this code?"
- The field-to-product feedback loop is part of the product itself, because it de-risks the roadmap and improves future deployments.
  - Evidence: "We are the bridge between products. We are the bridge between problems and the feedback is actually like half of the loop that makes the next deployment better than the previous deployment."
- Outcome-based deployment matters more than token usage; the motion has to show real business value, not just more agent activity.
  - Evidence: "A lot of organizations that we work with, some of the largest and most regulated enterprises in the world, they really care about, \"Are we getting true value out of this solution, or are we just burning tokens for no reason, right?\" And that is one core differentiator that I need to call out between us and some of the other platforms."

### Claims From The Talk
- Cognition reports that, over the last six months, using its own agent let the company ship almost an order of magnitude more good-quality, robust PRs internally. (`explicit`)
  - Evidence: "What do I mean by that? We can take a pause and take a look at this figure. So, internally at Cognition, over the last 6 months, for better or worse, we might have been behind on hiring, but using our agent, we were able to ship almost an order of magnitude more good quality robust PRs across the organization."
- The speaker says enterprise adoption of the agent is growing parabolically across different use cases and scenarios. (`explicit`)
  - Evidence: "You don't have to take our word for it. If we take a look If we can take a look at the specifics of how we're actually being consumed, how we're being utilized across the enterprise, it's a parabolic growth of how companies are adopting our agent, deploying our agent, and using it in multiple different use cases and multiple different scenarios."
- The talk argues that writing code faster is only a minority of the problem; testing, review, deployment, and maintenance are the real bottlenecks. (`explicit`)
  - Evidence: "But the problem isn't like writing code faster, that's usually only 20% of the problem. The problem really just becomes like how do you test this code?"
- One customer engagement is described as effectively adding about 150% headcount over a three-month period. (`explicit`)
  - Evidence: "We brought them on board. And functionally, over the course of those 3 months, we delivered about 150% like plus headcount."
- The speaker reports about an 82% reduction in delivery timelines after bringing Devin into a customer environment. (`explicit`)
  - Evidence: "So, about like 82% reduction across like delivery. So, if you subscribe to the agile deliver agile development methodology, obviously like you have tickets, you have sprints, like you have things that need to be built."
- The talk claims that, compared with single-point tools and before an agent harness like Devin, the organization delivers almost double the PRs. (`explicit`)
  - Evidence: "Like, is this meaningful? Does this actually make sense? So, if you think about dissecting the numbers a little like one dimension further, and you want to just look at like the raw PRs that people are ripping across the enterprise, we deliver almost double the amount of PRs that engineers were able to do with single-point tools and before you brought in an agent harness like Devin."

### Topics Covered
- [[forward-deployed-engineering|Product-market fit overlap]] — The overlap between a product's capabilities and the customer's actual problems, used here as the core deployment lens.
- [[software-factories|Enterprise software delivery lifecycle]] — The broader software delivery lifecycle that includes building, testing, reviewing, deploying, and maintaining code.
- [[software-factories|Outcome-based deployment]] — A deployment model judged by customer outcomes rather than raw tool usage or token spend.
- **Field-to-roadmap feedback loop** — The process of bringing field observations back into product planning and roadmap decisions.

### Tools And Named Systems
- **Devin** — The agent product the speaker uses as the core deployment surface for forward-deployed engineering.
- [[windsurf|Windsurf]] — A related interface surface mentioned alongside CLI and IDE-style access.
- **Devin Cloud** — The specific cloud agent surface called out as what Cognition is known for.

### Novel Concepts And Methods
- **Forward-deployed engineering** — Forward-deployed engineering: embedding engineers with customer problems so agent deployment is shaped by real enterprise needs.
- **Customer-embedded delivery** — Customer-embedded delivery: working inside customer ecosystems to identify backlog items, remediations, delayed code, missing tests, and alert triage opportunities.
- **Problem-to-capability mapping** — Problem-to-capability mapping: translating observed customer pain points back into product capabilities and roadmap priorities.
- **Session-based measurement** — Session-based measurement: treating agent runs as sessions and measuring productive engineering hours from those sessions.

### Open Questions
- **How can a deployed engineering team measure return on investment in a way that is credible across different customer environments?** — The talk says ROI is ambiguous, so this is central to deciding whether the motion is economically real or just expensive experimentation.
- **Which field workarounds, hacks, or bugs should become product features, and which should stay local to one customer?** — The speaker frames this as a recurring product judgment that affects both customer success and roadmap quality.

### Derived Links And Source Material
- [[youtube-RVxym6mmIns-transcript]] — dedicated official recording transcript.
- [[youtube-RVxym6mmIns]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/RVxym6mmIns--2026-06-29-jia-wu-how-forward-deployed-engineering-is-done-at-cognition.json`.

### Speaker Context
- [[jia-wu|Jia Wu]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[jia-wu]]

## Official YouTube Recording
- [[youtube-RVxym6mmIns|How Forward Deployed Engineering is done at Cognition — Jia Wu]] — official AI Engineer YouTube recording published 2026-07-28.
- Evidence status: [[youtube-RVxym6mmIns-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-RVxym6mmIns]] - dedicated official event recording.
- [[youtube-RVxym6mmIns-transcript]] - dedicated official recording transcript.

- Source video: `youtube-RVxym6mmIns`
- Slide deck: [[youtube-RVxym6mmIns-slides|Slides: How Forward Deployed Engineering is done at Cognition — Jia Wu]] — 32 visible slide image(s).
![[assets/slides/RVxym6mmIns/slide-001.jpg]]
![[assets/slides/RVxym6mmIns/slide-002.jpg]]
![[assets/slides/RVxym6mmIns/slide-003.jpg]]
- Slide-derived themes for `youtube-RVxym6mmIns`: engineering, deployed, forward, software, track, june, cognition, understanding.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/RVxym6mmIns.txt` (3,530 words).

## Transcript Markdown
- [[youtube-RVxym6mmIns-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/RVxym6mmIns.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-RVxym6mmIns` — 3,530 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-RVxym6mmIns`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-RVxym6mmIns`: engineering, engineers, deployed, problem, take, across, customer, cognition.
- Slide-derived themes for `youtube-RVxym6mmIns`: engineering, deployed, forward, software, track, june, cognition, understanding.
- Evidence links for `youtube-RVxym6mmIns` (primary event evidence): [[youtube-RVxym6mmIns]], [[youtube-RVxym6mmIns-transcript]], [[youtube-RVxym6mmIns-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
