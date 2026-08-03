---
title: "Forward Deployed Engineering 101"
category: "talks"
date: "2026-06-29"
time: "2:50pm-3:10pm"
track: "Forward Deployed Engineering"
room: "Track 8"
speakers: ["Kevin Bai"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Forward Deployed Engineering"
scheduleRoom: "Track 8"
scheduleLabels: ["Forward Deployed Engineering", "Track 8", "session", "confirmed"]
---
# Forward Deployed Engineering 101

## Conference Context
- Date/time: 2026-06-29 · 2:50pm-3:10pm
- Track/room: Forward Deployed Engineering · Track 8
- Speaker(s): Kevin Bai
- Session type/status: session · confirmed

- Track: Forward Deployed Engineering
- Room: Track 8
- Session type: session
- Status: confirmed

## Session Description
No official description published in the schedule data.

## Synthesis
### Transcript-Backed Summary
The talk argues that forward deployed engineering is not just custom services with a new name; it is a design-partnership motion scaled into the enterprise. The core mechanism is to sell outcomes by having customer-facing engineers build on shared platform primitives, so the company can solve customer problems without recreating the software stack from scratch for every account. The main tradeoff is maintenance: if the work is not anchored in a reusable platform, the function collapses into a dev shop that is expensive, hard to staff, and impossible to sustain. The practical advice is to adopt FDE only when you truly need to sell technical capability to non-technical buyers, and to use custom projects as a way to discover which parts of the product should later be generalized.

### Key Takeaways
- If engineers build everything from scratch for each customer, the function stops being FDE and becomes a dev shop.
  - Evidence: "And you would be totally right. If you were to implement an FTE function where each FTE is building entirely from scratch, my friends, you do not have an FTE function."
- A company should only consider FDE if it is willing to invest in a platform with shared primitives.
  - Evidence: "Right? It's only in this situation where you need FTE. That's the first piece. So the second piece is do I have a platform or phrased another way am I willing to invest in building one because I assure you right no matter how tempting it is to uh have these engineers that can make you money if they are not building on top of a platform with some number of shared primitives you are in for a very bad time."
- As software becomes more agentic and customizable, many companies will face customers who do not understand the product well enough to implement it themselves.
  - Evidence: "And that means nearly every platform is customizable. And that also means nearly all of you are going to have a situation where your customers have no idea what the heck it is that you actually do."
- Early FDE work should be used to scout which bespoke needs can become future product capabilities.
  - Evidence: "Anything that can be generalizable should be generalized in the long term. Now, when you begin uh your FTEing, right, probably you're not going to have a lot of different primitives, but that's okay because FD is also a great way to scout ahead and to find what additional product services you can build upon to further enable the success of your business."

### Claims From The Talk
- Forward deployed engineering is presented as design partnerships scaled up into the enterprise. (`explicit`)
  - Evidence: "Um FDE is basically taking this concept of a design partnership and scaling it up into enterprise."
- A real FDE function depends on building on top of a shared platform rather than writing custom software from scratch for each customer. (`explicit`)
  - Evidence: "But the thing that makes an FTE program different is that they are building on top of a platform."
- The speaker argues that the first implementation question is whether a company truly needs FDE, not whether the idea is fashionable. (`explicit`)
  - Evidence: "Um, so how do you go about doing that? First and foremost, and this is the thing that I advise to everyone who's thinking through the concept of forward deployed engineering is really ask yourselves, do I need an FTE function?"
- The speaker argues that AI has made customizable software far easier to build, which makes FDE more relevant across the software industry. (`explicit`)
  - Evidence: "My personal hypothesis is that the thing which has changed is that the nature of doing business in the software industry itself is what's changed because now nearly every platform is agentic."
- The speaker defines an FTE as a customer-facing software engineer. (`explicit`)
  - Evidence: "What is the perfect profile? Oh, this is so good. What is the perfect profile of an FTE? So, the the tagline that I will leave you with is that a FTE is nothing more than a customerfacing software engineer."

### Topics Covered
- [[software-factories|Forward Deployed Engineering]] — The central operating model discussed in the talk: customer-facing engineers embedded in solution delivery.
- [[software-factories|Design Partnerships]] — A scalable enterprise approach where seller and buyer co-develop a solution closely.
- [[software-factories|Shared Primitives]] — Using reusable building blocks so custom work stays maintainable.
- [[software-factories|Platform-Led Delivery]] — Building on a product platform rather than creating one-off bespoke systems.
- [[software-factories|Technical-to-Nontechnical GTM]] — Selling technical software to buyers who are not deeply technical themselves.

### Tools And Named Systems
- [[foundry|Foundry]] — The platform the speaker uses as the main example of a reusable foundation for customer solutions.
- [[aws|AWS]] — The example of a broadly shared cloud platform with common primitives used to illustrate generalizable infrastructure.

### Novel Concepts And Methods
- **Enterprise Design Partnership** — Use design partnership practices as the operating model for enterprise deployment.
- **Platform-Bound Customization** — Build customer solutions on shared platform primitives instead of from scratch.
- **Generalize What Repeats** — Separate bespoke customer work from generalizable product capabilities.
- **Need-Driven FDE Gate** — Evaluate whether the company truly needs an FDE motion before adopting it.

### Open Questions
- **How atomic should shared primitives be for different platform and customer contexts?** — The answer determines how much of the app is prebuilt versus truly customized.
- **Which engineering changes should stay in the platform, and which should remain customer-specific in the forward deployed layer?** — That boundary controls maintainability and whether the company can turn custom work into reusable product.
- **What profile best fits a customer-facing software engineer in an FDE role?** — Hiring and team design depend on the mix of software depth and customer presence the role requires.

### Derived Links And Source Material
- [[youtube-KwhgfwOSToQ-transcript]] — dedicated official recording transcript.
- [[youtube-KwhgfwOSToQ]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/KwhgfwOSToQ--2026-06-29-kevin-bai-forward-deployed-engineering-101.json`.

### Speaker Context
- [[kevin-bai|Kevin Bai]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[kevin-bai]]

## Official YouTube Recording
- [[youtube-KwhgfwOSToQ|Forward Deployed Engineering 101 — Kevin Bai, Anthropic, ex Palantir & Rippling Founding FDE]] — official AI Engineer YouTube recording published 2026-07-28.
- Evidence status: [[youtube-KwhgfwOSToQ-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-KwhgfwOSToQ]] - dedicated official event recording.
- [[youtube-KwhgfwOSToQ-transcript]] - dedicated official recording transcript.

- Source video: `youtube-KwhgfwOSToQ`
- Slide deck: [[youtube-KwhgfwOSToQ-slides|Slides: Forward Deployed Engineering 101 — Kevin Bai, Anthropic, ex Palantir & Rippling Founding FDE]] — 9 visible slide image(s).
![[assets/slides/KwhgfwOSToQ/slide-001.jpg]]
![[assets/slides/KwhgfwOSToQ/slide-002.jpg]]
![[assets/slides/KwhgfwOSToQ/slide-003.jpg]]

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/KwhgfwOSToQ.txt` (3,202 words).

## Transcript Markdown
- [[youtube-KwhgfwOSToQ-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/KwhgfwOSToQ.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-KwhgfwOSToQ` — 3,202 transcript words; role: primary event evidence.
- Interpretation rule for `youtube-KwhgfwOSToQ`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-KwhgfwOSToQ`: platform, okay, software, customer, palunteer, does, foundry, data.
- Evidence links for `youtube-KwhgfwOSToQ` (primary event evidence): [[youtube-KwhgfwOSToQ]], [[youtube-KwhgfwOSToQ-transcript]], [[youtube-KwhgfwOSToQ-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
