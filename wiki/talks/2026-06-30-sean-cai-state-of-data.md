---
title: "State of Data"
category: "talks"
date: "2026-06-30"
time: "11:10am-11:30am"
track: "Posttraining & Midtraining"
room: "Track 9"
speakers: ["Sean Cai"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Posttraining & Midtraining"
scheduleRoom: "Track 9"
scheduleLabels: ["Posttraining & Midtraining", "Track 9", "session", "confirmed"]
---
# State of Data

## Conference Context
- Date/time: 2026-06-30 · 11:10am-11:30am
- Track/room: Posttraining & Midtraining · Track 9
- Speaker(s): Sean Cai
- Session type/status: session · confirmed

- Track: Posttraining & Midtraining
- Room: Track 9
- Session type: session
- Status: confirmed

## Session Description
No official description published in the schedule data.

## Synthesis
### Transcript-Backed Summary
Sean Cai argues that the real bottleneck in frontier AI is no longer raw data volume but trustworthy process-based data that captures how expert work actually unfolds. He says the data market is fragmenting because specialists can beat vertically integrated giants on sourcing, environment design, reward design, and evals, and that task verifiability explains why code matured first while finance, healthcare, law, cyber, biology, and taste are next. The practical consequence is that builders should treat real-world workflow pipelines, rerunning post-training, and enterprise-owned traces as the moat, because headline benchmarks and vendor-produced realism are too easy to game and too unstable across harnesses.

### Key Takeaways
- Live business workflows are the durable data asset because frontier data moves with the market, while dead codebases age out quickly.
  - Evidence: "Um a data set is only available in so far as frontier data markets as the frontier moves. So, the only durable supply of it technically is a live business you partner with, not a dead startup's code bases like so many data companies out there are buying today."
- Task maturity tracks verifiability, so domains with decomposable correctness, shared definitions, and abundant examples mature earlier than low-verifiability domains.
  - Evidence: "How often does the real world sort of hand you fresh examples of verified work? If you think about like coding as the first mature AI app layer market, that's really no accident because we were blessed to have something called GitHub from web 2.0 which solved all three of these at once."
- A single benchmark number is not trustworthy by itself because it is just one sample from a larger, mostly unmeasured distribution.
  - Evidence: "a single benchmark number under a single scaffold is like basically one sample from a distribution who's basically with nobody measured."
- For builders, the moat is the pipeline into real-world work and the infrastructure that keeps retraining as models improve.
  - Evidence: "Um, that's kind of just letting the task test writer grade the task. And if you're a builder, your moat's not the data, it's the sort of pipeline into real-world work."

### Claims From The Talk
- The speaker's core argument is that data is the underfunded leg of model improvement, and that the valuable data is the kind that turns a generalist model into a real expert rather than more legacy annotation scale. (`explicit`)
  - Evidence: "Uh data is sort of the underfunded leg here. It's the one that sort of turns a generalist model into a real expert."
- He argues that data supply chains are permanently fragmenting, with specialists outcompeting giant integrated vendors on sourcing people, building environments, designing rewards, and running evals. (`explicit`)
  - Evidence: "The fragmentation I would say, is pretty permanent. It's not transitional. And uh quality increasingly does not scale linearly with quantity, which leads to a sort of cottage industry in data land right now, where you have labs literally mandates uh vendor diversification on the scale of like 20 to 30 different vendors because they inherently distrust their ability to scale quality with quantity."
- He presents Verifier's Law as a central mechanism for predicting which application-layer markets mature first: the easier a task is to verify, the easier it is to train a model to do it. (`explicit`)
  - Evidence: "It's called Verifier's Law. The ease of training a model to do a task is proportional to how verifiable the task is."
- He claims much of the benchmark market is distorted by Goodhart-style incentive problems, where contrived benchmarks and benchmark-selling loops make many headline scores misleading. (`explicit`)
  - Evidence: "It's Goodhart's law with a profit motive. Basically, the moment your measure like becomes a target, and then the target is set by people who aren't true domain experts, it stops sort of measuring anything real."
- He says successful data companies are becoming enterprise-focused neo-labs that need an abstraction layer for owning, routing, and retraining on real-world work rather than just selling data. (`explicit`)
  - Evidence: "Enterprise in ways you wouldn't expect a data business to do. Once enterprises stop renting out labs intelligence and starts owning their own, you need an entire abstraction layer that doesn't exist yet."

### Topics Covered
- [[agent-evaluations|Process-Based Data]] — Data derived from real workflows, reasoning traces, and decision sequences rather than only final outputs.
- [[agent-evaluations|Verification-Driven Maturity]] — The idea that task ease of training depends on how verifiable the task is.
- [[agent-evaluations|Benchmark Reliability]] — Failure modes where benchmarks become noisy, gameable, or scaffold-dependent.
- **Enterprise AI Infrastructure** — Enterprise-oriented infrastructure for owning workflows, routing models, and retraining on live work.

### Tools And Named Systems
- [[github|GitHub]] — The code host cited as an example of a platform that provides objective correctness signals and abundant public traces.
- [[slack|Slack]] — Enterprise collaboration source mentioned as a valuable repository of workflow traces.
- [[jira|Jira]] — Work tracking source mentioned as a valuable repository of workflow traces.

### Novel Concepts And Methods
- **Process-Based Data Capture** — Capture trajectories, reasoning traces, and decision sequences from real work instead of only storing final-state outputs.
- **Three-Axis Verifiability Analysis** — Score tasks by asymmetry of verification, veracity of verification, and proliferation of verification to estimate how quickly a market can mature.
- **Cross-Harness Differencing** — Compare results across different harnesses or infrastructures to reveal whether benchmark numbers are stable or just scaffold-specific noise.
- **Long-Horizon Rubric Analysis** — Evaluate long-horizon tasks with deterministic verifiers paired with an LLM judge and rubric analysis instead of relying on a single aggregate score.

### Open Questions
- **How can buyers reliably distinguish type one data from type two data when the market has incentives to relabel one as the other?** — This determines whether procurement can actually buy realism instead of benchmark-shaped theater.
- **Which enterprise workflows will produce the richest fresh verification traces for the next wave of model training outside software engineering?** — The answer affects which domains become the next durable data markets.
- **How should robotics data be standardized when the modality itself is still an unresolved research question?** — If the modality is unstable, vendor strategy and dataset design may be mis-specified from the start.

### Derived Links And Source Material
- [[youtube-ZyIoTOAbRfs-transcript]] — dedicated official recording transcript.
- [[youtube-ZyIoTOAbRfs]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/ZyIoTOAbRfs--2026-06-30-sean-cai-state-of-data.json`.

### Speaker Context
- [[sean-cai|Sean Cai]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[sean-cai]]

## Official YouTube Recording
- [[youtube-ZyIoTOAbRfs|State of Data — Sean Cai, Independent / State of Data]] — official AI Engineer YouTube recording published 2026-07-11.
- Evidence status: [[youtube-ZyIoTOAbRfs-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-ZyIoTOAbRfs]] - dedicated official event recording.
- [[youtube-ZyIoTOAbRfs-transcript]] - dedicated official recording transcript.

- Source video: `youtube-ZyIoTOAbRfs`
- Slide deck: [[youtube-ZyIoTOAbRfs-slides|Slides: State of Data — Sean Cai, Independent / State of Data]] — 10 visible slide image(s).
![[assets/slides/ZyIoTOAbRfs/slide-001.jpg]]
![[assets/slides/ZyIoTOAbRfs/slide-002.jpg]]
![[assets/slides/ZyIoTOAbRfs/slide-003.jpg]]
- Slide-derived themes for `youtube-ZyIoTOAbRfs`: track, july, data, bottleneck, never, intelligence, ones, human.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/ZyIoTOAbRfs.txt` (3,355 words).

## Transcript Markdown
- [[youtube-ZyIoTOAbRfs-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/ZyIoTOAbRfs.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-ZyIoTOAbRfs` — 3,355 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-ZyIoTOAbRfs`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-ZyIoTOAbRfs`: data, model, layer, three, companies, type, real, labs.
- Slide-derived themes for `youtube-ZyIoTOAbRfs`: track, july, data, bottleneck, never, intelligence, ones, human.
- Evidence links for `youtube-ZyIoTOAbRfs` (primary event evidence): [[youtube-ZyIoTOAbRfs]], [[youtube-ZyIoTOAbRfs-transcript]], [[youtube-ZyIoTOAbRfs-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
