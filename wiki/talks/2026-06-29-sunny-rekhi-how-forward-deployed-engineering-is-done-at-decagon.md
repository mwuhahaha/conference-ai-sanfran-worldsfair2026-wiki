---
title: "How Forward Deployed Engineering is done at Decagon"
category: "talks"
date: "2026-06-29"
time: "1:55pm-2:15pm"
track: "Forward Deployed Engineering"
room: "Track 8"
speakers: ["Sunny Rekhi"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Forward Deployed Engineering"
scheduleRoom: "Track 8"
scheduleLabels: ["Forward Deployed Engineering", "Track 8", "session", "confirmed"]
---
# How Forward Deployed Engineering is done at Decagon

## Conference Context
- Date/time: 2026-06-29 · 1:55pm-2:15pm
- Track/room: Forward Deployed Engineering · Track 8
- Speaker(s): Sunny Rekhi
- Session type/status: session · confirmed

- Track: Forward Deployed Engineering
- Room: Track 8
- Session type: session
- Status: confirmed

## Session Description
No official description published in the schedule data.

## Synthesis
### Transcript-Backed Summary
Sunny Rekhi argues that forward deployed engineering at Decagon is not a separate support function but a product discipline that sits at the edge of the customer and continuously feeds the platform. The mechanism is twofold: configure the AI customer service agent to fit each enterprise, then convert the repeated pain points from those deployments into reusable product features and self-serve capabilities. As Decagon scaled rapidly, the company specialized this work into agent builders and agent software engineers, emphasized early definition of success, and pushed teams to prove value quickly, act as advisors rather than pure executors, and avoid brittle one-off fixes. The practical consequence is a deployment motion that compounds: each customer should make the next customer easier to serve, while also making the product better for everyone.

### Key Takeaways
- Forward deployment should bring enterprise pain back into the product instead of treating each customer ask as a one-off.
  - Evidence: "So, there's the two kinds of forward deployment engineer that we have internally, configuring the agent and then making sure all the problems that you interact with the enterprise that that come up in that in in in in the context of conversation also get brought back into the product."
- Lock down success criteria early so the team can build toward explicit metrics and avoid later misalignment.
  - Evidence: "And really narrowing that down, ideally getting it in writing so that there is like no miscommunication along the way."
- When the same integration or workflow recurs enough times, it should be redesigned as self-serve rather than rebuilt repeatedly.
  - Evidence: "And then we thought enough is enough. After like the 25th one, we're like, \"I don't know how many more are coming up.\" Uh so, let's just like build it a self-serve way."
- A strong forward deployed engineer should advise as well as execute, using cross-customer experience to steer toward higher-ROI work.
  - Evidence: "But, I think as a forward deployed engineer or forward deployed person of any sort, you're you should treat yourself as an advisor rather than just an executor, right?"
- The long-term goal is compounding: improve the experience for the next customer every time the current customer is served.
  - Evidence: "So, if the agent interfaces with customer A, you improve that for customer B. And it's all about sort of taking knowledge from the field and bringing it Uh and so, just to wrap up here, uh sort of the a few of the few of the themes."

### Claims From The Talk
- At Decagon, forward deployed engineering is treated as identical to product engineering, with the same bar and reporting structure. (`explicit`)
  - Evidence: "Which brings me to a really important point. In fact, it's so important I wish I had a slide for it, but uh at Decagon, forward deployment engineering is identical to product engineering."
- As the company scaled, the former all-in-one agent software engineering role was split into two specialized lanes: agent builders and agent software engineers. (`explicit`)
  - Evidence: "And effectively we we we broke apart this agent software engineering role into two specialized lanes."
- The hardest skill in a strong forward deployed motion is not shipping the easiest custom fix, but exercising restraint so the work scales to future customers. (`explicit`)
  - Evidence: "Making sure that gets incorporated back into the product. And um, this is I think like a super super uh, important insight, uh, which is there is routinely this temptation of Okay, customer A made this request and they're so important to us and they want it done ASAP and maybe I'll just go prompt Codex and Cloud Code to just do it for me."
- Success should be defined very early in the deal, ideally in writing, with clear metrics and target channels before implementation begins. (`explicit`)
  - Evidence: "Uh, and in in our case, we've learned like early on when you're scoping the deal, like literally when the very first conversations, you want to figure out ahead of time what does success look like for the customer."
- Staffing customers with industry experts helps knowledge compound, improves credibility, and speeds up ramp for new deployments in the same vertical. (`explicit`)
  - Evidence: "Uh this has been a really good learning for us. So, uh we try now, given that we have like a a ton of customers across various verticals, we have found it's really helpful to have industry experts that get staffed, the same kind of deal."
- In enterprise deployments, the team should prove value quickly on a narrow slice first and expand only after that initial value is demonstrated. (`explicit`)
  - Evidence: "So, it's all about how do you scale the work that you're doing. also very relevant, depending on the kind of forward deployment work you do, is especially in the enterprise, wanting to prove value as fast as possible."

### Topics Covered
- [[software-factories|Forward deployed engineering]] — The operating model where customer-facing work is treated as a direct path into product improvement.
- [[platform-context-and-collaboration|Agent configuration]] — The practice of tuning an AI agent's instructions, tone, and action boundaries for a specific enterprise.
- [[software-factories|Productization]] — The idea that recurring customer requests should become reusable product capabilities.
- [[forward-deployed-engineering|Requirements scoping]] — The discipline of getting clear on metrics, channels, and outcomes before implementation starts.
- [[software-factories|Self-serve integration]] — The pattern of turning one-off integrations into reusable self-serve workflows.

### Tools And Named Systems
- [[decagon|Decagon]] — The AI customer service platform the speaker represents and uses as the basis for the forward deployed motion.
- [[codex|Codex]] — The coding assistant mentioned as part of the temptation to implement customer asks quickly through code.
- [[cloud-code|Cloud Code]] — The coding tool mentioned alongside Codex as another way teams might rapidly patch a customer request.
- [[whatsapp|WhatsApp]] — A supported customer communication channel used as an example of what the platform can handle.

### Novel Concepts And Methods
- **Field-to-product loop** — Treat each customer deployment as a feedback loop that converts repeated manual work into product capabilities.
- **Requirements-first scoping** — Define success criteria early, in writing, before building the deployment.
- **Custom-to-self-serve conversion** — Shift recurring custom work into self-serve workflows so customers or builders can handle it without bespoke engineering.
- **Vertical expert staffing** — Use domain specialists to accelerate ramp and improve customer credibility in a vertical.
- **Advisor-led prioritization** — Act as an advisor as well as an executor by recommending the highest-ROI automation based on cross-customer experience.

### Open Questions
- **How can a forward deployed team reliably gather and lock down requirements early enough to avoid unnecessary building while still moving quickly?** — The talk says up-front alignment matters more as AI coding reduces the cost of implementation, but it leaves open how to operationalize that rigor at enterprise speed.
- **What is the best way to staff and reuse vertical expertise across many customers without making the organization brittle or overly siloed?** — The speaker argues that industry experts compound value, but the talk does not specify how to balance specialization with flexibility.
- **How should a forward deployed team decide when to follow a customer's request versus redirecting them toward a better ROI path?** — The talk elevates the advisor role, but the exact decision rules for that advisory judgment remain unspecified.

### Derived Links And Source Material
- [[youtube-7wu2hsRfvV0-transcript]] — dedicated official recording transcript.
- [[youtube-7wu2hsRfvV0]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/7wu2hsRfvV0--2026-06-29-sunny-rekhi-how-forward-deployed-engineering-is-done-at-decagon.json`.

### Speaker Context
- [[sunny-rekhi|Sunny Rekhi]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[sunny-rekhi]]

## Official YouTube Recording
- [[youtube-7wu2hsRfvV0|How Forward Deployed Engineering is done at Decagon — Sunny Rekhi]] — official AI Engineer YouTube recording published 2026-07-28.
- Evidence status: [[youtube-7wu2hsRfvV0-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-7wu2hsRfvV0]] - dedicated official event recording.
- [[youtube-7wu2hsRfvV0-transcript]] - dedicated official recording transcript.

- Source video: `youtube-7wu2hsRfvV0`
- Slide deck: [[youtube-7wu2hsRfvV0-slides|Slides: How Forward Deployed Engineering is done at Decagon — Sunny Rekhi]] — 5 visible slide image(s).
![[assets/slides/7wu2hsRfvV0/slide-001.jpg]]
![[assets/slides/7wu2hsRfvV0/slide-002.jpg]]
![[assets/slides/7wu2hsRfvV0/slide-003.jpg]]
- Slide-derived themes for `youtube-7wu2hsRfvV0`: track, june, conversational, platform, concierge, experiences, always, black.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/7wu2hsRfvV0.txt` (3,337 words).

## Transcript Markdown
- [[youtube-7wu2hsRfvV0-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/7wu2hsRfvV0.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-7wu2hsRfvV0` — 3,337 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-7wu2hsRfvV0`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-7wu2hsRfvV0`: forward, customer, customers, sure, deployed, product, back, deployment.
- Slide-derived themes for `youtube-7wu2hsRfvV0`: track, june, conversational, platform, concierge, experiences, always, black.
- Evidence links for `youtube-7wu2hsRfvV0` (primary event evidence): [[youtube-7wu2hsRfvV0]], [[youtube-7wu2hsRfvV0-transcript]], [[youtube-7wu2hsRfvV0-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
