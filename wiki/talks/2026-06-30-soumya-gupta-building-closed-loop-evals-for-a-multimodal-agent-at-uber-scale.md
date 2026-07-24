---
title: "Building Closed-Loop Evals for a Multimodal Agent at Uber Scale"
category: "talks"
date: "2026-06-30"
time: "11:40am-12:00pm"
track: "Evals"
room: "Track 5"
speakers: ["Soumya Gupta", "Jai Chopra"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Evals"
scheduleRoom: "Track 5"
scheduleLabels: ["Evals", "Track 5", "sponsor", "confirmed"]
---
# Building Closed-Loop Evals for a Multimodal Agent at Uber Scale

## Conference Context
- Date/time: 2026-06-30 · 11:40am-12:00pm
- Track/room: Evals · Track 5
- Speaker(s): Soumya Gupta, Jai Chopra
- Session type/status: sponsor · confirmed

- Track: Evals
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
This talk covers how we designed evals for Uber's food enhancement agent—which edits food photography to better present dishes for smaller, independent Uber Eats merchants—along with the pitfalls and lessons learned along the way. The problem is uniquely hard: we must stay faithful to the original dish, preserve each merchant's brand and packaging, and avoid homogenizing the marketplace—all without an existing playbook for multimodal evals in a narrow domain. We'll dig into what we learned navigating reward hacking, where the agent figured out how to game the eval loop, and how we built a closed feedback loop incorporating offline and online signals for continuous improvement—all while balancing creativity against rigid safety guardrails at scale. If you're an ML or applied AI practitioner working on multimodal systems, agentic pipelines, or eval design—especially building generative features under tight safety or quality constraints—you'll walk away with practical strategies for designing multimodal evals in a narrow domain, recognizing and countering reward hacking, and building offline/online feedback loops that keep a generative agent improving in production.

## Synthesis
### Transcript-Backed Summary
The talk’s central thesis is that a multimodal food-photo enhancement agent can only work at Uber scale if evals are built as a closed loop, not as a one-shot benchmark. The speakers lay out a staged mechanism: a router decides whether to enhance, an editing loop iterates against QA feedback, and a final publish gate enforces policy and quality while every step is logged for diagnosis. The practical tradeoff is that the system has to improve lower-quality merchant photos without flattening brand identity or marketplace diversity, so it balances creativity against recall-heavy guardrails, compute cost, and reward-hacking risk. They also show that offline tuning has to be coupled to production signals, because drift and real-world feedback determine whether the system actually keeps improving.

### Key Takeaways
- Start with logging before trying to optimize anything, because logs are what make diagnosis and self-learning possible.
  - Evidence: "You want to start with your logging cuz if you don't start with it, you have nothing to optimize for, let alone set up a self-learning loop."
- Use objective human-labeling guidelines to reduce subjective noise when building the first target dataset.
  - Evidence: "Send it to our human labelers and give them a very objective guideline to label on. This is to remove any subjective biases or any noise coming in from human labelers."
- Treat routing as a precision-and-recall problem so the guardrail matches the cost of letting bad images slip through.
  - Evidence: "Essentially, what we're doing is we're measuring the precision recall. In practice, your routers might actually be much more sophisticated."
- Measure iterative image editing with pass-at-K so you can see whether more rounds actually improve the chance of success.
  - Evidence: "So, the metric we are measuring here is pass at K. Pass at K is essentially the pass rate at Kth iteration."
- Check production impact by slicing metrics by geo, device type, and dish type instead of relying only on aggregate results.
  - Evidence: "So, in this area as opposed to the others, what we can do is sort of slice by geos, by device type, by dish type, etc."

### Claims From The Talk
- The speakers say visual content is often the first signal shoppers see, and it can determine whether they click through and add an item to cart. (`explicit`)
  - Evidence: "Visual content actually plays a really important role for the user experience. So a photo is quite often the first signal that a customer gets that gives them that initial impression about a merchant."
- They report that smaller merchants often lack the time, know-how, and money to produce high-quality photos. (`explicit`)
  - Evidence: "And when we speak to our merchants, there are three themes that kind of emerge. Lack of time, lack of know-how, and costs cuz these professional um photo shoots actually cost a lot of money."
- They argue the system has to stay faithful to the original image, preserve merchant branding, and avoid making the marketplace look uniform. (`explicit`)
  - Evidence: "So, we're threading the needle here. We need to be able to stay faithful to the original image, preserve the brand of the merchant, and avoid everything looking the same."
- They say logging is foundational because without it there is nothing to optimize or feed into a self-learning loop. (`explicit`)
  - Evidence: "You want to start with your logging cuz if you don't start with it, you have nothing to optimize for, let alone set up a self-learning loop."
- They report that static offline models will not hold up under drift, so the system has to keep evolving over time. (`explicit`)
  - Evidence: "So the meta point I'm trying to get here is you've trained your offline model, but there will be long cases where your model is going to continue to fail and the static model will not work in the real system."
- They describe reward hacking as edits that change pixels in a way that is not actually meaningful or influential. (`explicit`)
  - Evidence: "So, this is an example of a reward hacking actually. And and this is a nugatory change, but something that we don't think is a meaningful or influential change despite the actual raw pixels of the input and output being pretty different."

### Topics Covered
- **Multimodal routing** — The talk centers on routing, editing, and QA for a multimodal image agent.
- **Merchant authenticity** — The system is designed to preserve merchant identity and user trust while improving photos.
- [[agent-evaluations|Marketplace diversity]] — The speakers emphasize that edits should not collapse the visual diversity of the marketplace.
- [[agent-evaluations|Reward hacking]] — The talk gives a concrete example of reward hacking in image-edit evaluation.
- [[agent-evaluations|Closed-loop feedback]] — The system combines offline labeling, production sampling, and feedback-driven retraining.
- [[agent-evaluations|Segment-level evaluation]] — Production evaluation is broken down by slices such as geo, device type, and dish type.

### Tools And Named Systems
- **Uber Eats** — The Uber Eats delivery marketplace is the production platform the speakers use as the setting for the agent and its evaluation loop.

### Novel Concepts And Methods
- **Structured routing** — Structured-output image-understanding routing: the system asks for a description of the photo, turns it into structured output, and uses that to decide whether to enhance or skip.
- **Routing confusion matrix** — Confusion-matrix routing evaluation: routing is evaluated like a classifier with precision and recall over branch decisions.
- **Golden-label calibration** — Human-golden-dataset alignment: representative samples are labeled by humans with objective guidelines and used to tune the model before shipping.
- **Diagnoser auto-tuning** — Diagnoser-driven auto-tuning: a diagnoser localizes mismatches from production feedback and triggers the tuning pipeline.
- **Prompt optimizer loop** — Reflection-and-synthesis prompt optimization: one sub-agent reflects on mismatches and another updates the agent config from that feedback.
- **Iterative QA gating** — Iterative enhancement with a multi-dimensional QA gate: the editor keeps retrying until the output passes checks on attributes like plating, faithfulness, and color.

### Open Questions
- **How can the team define a better-image rubric that stays aligned across product, design, policy, and legal without erasing merchant-specific variety?** — That definition sets the boundary between useful enhancement and unsafe homogenization.
- **How can the system reliably detect edits that are technically different but not meaningfully better?** — This is the core defense against reward hacking in the image-editing loop.
- **How can one diagnoser generalize across multiple agents and feedback sources without reintroducing manual review bottlenecks?** — The answer determines whether the feedback system scales as the orchestration surface grows.

### Derived Links And Source Material
- [[youtube-31GUkCBD-Uc-transcript]] — dedicated official recording transcript.
- [[youtube-31GUkCBD-Uc]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/31GUkCBD-Uc--2026-06-30-soumya-gupta-building-closed-loop-evals-for-a-multimodal-agent-at-uber-scale.json`.

### Speaker Context
- [[soumya-gupta|Soumya Gupta]]
- [[jai-chopra|Jai Chopra]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[soumya-gupta]]
- [[jai-chopra]]

## Official YouTube Recording
- [[youtube-31GUkCBD-Uc|Building Closed-Loop Evals for a Multimodal Agent at Scale — Soumya Gupta & Jai Chopra, Uber]] — official AI Engineer YouTube recording published 2026-07-24.
- Evidence status: [[youtube-31GUkCBD-Uc-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-31GUkCBD-Uc]] - dedicated official event recording.
- [[youtube-31GUkCBD-Uc-transcript]] - dedicated official recording transcript.

- Source video: `youtube-31GUkCBD-Uc`
- Slide deck: [[youtube-31GUkCBD-Uc-slides|Slides: Building Closed-Loop Evals for a Multimodal Agent at Scale — Soumya Gupta & Jai Chopra, Uber]] — 16 visible slide image(s).
![[assets/slides/31GUkCBD-Uc/slide-001.jpg]]
![[assets/slides/31GUkCBD-Uc/slide-002.jpg]]
![[assets/slides/31GUkCBD-Uc/slide-003.jpg]]
- Slide-derived themes for `youtube-31GUkCBD-Uc`: track, july, problem, poor, chopra, product, manager, engineering.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/31GUkCBD-Uc.txt` (3,773 words).

## Transcript Markdown
- [[youtube-31GUkCBD-Uc-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/31GUkCBD-Uc.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-31GUkCBD-Uc` — 3,773 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-31GUkCBD-Uc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-31GUkCBD-Uc`: image, feedback, system, production, output, pass, model, send.
- Slide-derived themes for `youtube-31GUkCBD-Uc`: track, july, problem, poor, chopra, product, manager, engineering.
- Evidence links for `youtube-31GUkCBD-Uc` (primary event evidence): [[youtube-31GUkCBD-Uc]], [[youtube-31GUkCBD-Uc-transcript]], [[youtube-31GUkCBD-Uc-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
