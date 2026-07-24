---
title: "Training Frontier Models to Out-Think Hackers"
category: "talks"
date: "2026-06-30"
time: "11:40am-12:00pm"
track: "Data Quality"
room: "Track 9"
speakers: ["Uri Rolls", "Thom Wolf"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Data Quality"
scheduleRoom: "Track 9"
scheduleLabels: ["Data Quality", "Track 9", "session", "confirmed"]
---
# Training Frontier Models to Out-Think Hackers

## Conference Context
- Date/time: 2026-06-30 · 11:40am-12:00pm
- Track/room: Data Quality · Track 9
- Speaker(s): Uri Rolls, Thom Wolf
- Session type/status: session · confirmed

- Track: Data Quality
- Room: Track 9
- Session type: session
- Status: confirmed

## Session Description
We will give a surprisingly optimistic talk about AI and cyber, and why we believe it is not the end of cybersecurity as we know it, but an opportunity to empower defenders and build a lasting edge over attackers. Cyber is a battle of skill and speed, and the rising tide of frontier models is allowing human attackers to move faster and cheaper. That combination of skilled hackers and breakthrough LLMs is a real threat, while defensive systems are still expected to operate at scale with limited human intervention, constrained by what models can do out of the box. But the answer is not fear or despair. Just as high-quality data transformed software engineering, the right cyber training data can teach models to turn from weapons being used against us into tools that protect us.

## Synthesis
### Transcript-Backed Summary
The talk argues that AI is changing cyber offense economics, but that same shift creates an opening for defenders if we train models on the right kinds of cyber data. Rather than treating cyber as a generic coding problem, the speakers focus on access control and logic-heavy exploitation chains, using real zero-days, black-box environments, and deterministic graders to test whether a model can make the specific reasoning leaps that matter in live systems. Their thesis is optimistic but conditional: attackers are getting faster, so defenders need equally fast, specialized, and broadly available open-source models trained on high-quality data and evaluated with benchmarks that measure depth of understanding, not just final pass/fail outcomes.

### Key Takeaways
- A skilled attacker using frontier models can search across many targets at once, which changes the economics of offense.
  - Evidence: "And it's it's freaky and it's getting really scary. And this is my point on the house. And part of the reason we think this is happening is if cyber is this game of skill and speed, then a very skilled attacker using something like mythos can now choose a bunch of targets all at once."
- Many important cyber failures are logic breaks across systems, so the benchmark is aimed at reasoning about system behavior rather than patching obvious code bugs.
  - Evidence: "It's about very very very big systems and somewhere between them there's these logic breaks where it's possible that one thing checks for something specific in the code another checks for something else and that sort of leads to everything breaking and so what we're trying to do is we're trying to figure out how"
- Deterministic verification at each step lets the benchmark reveal how deeply a model progressed through the exploitation chain.
  - Evidence: "And so across the entire exploitation and the discovery chain, every single step can be deterministically verified, allowing us to see how deep it got within the chain."
- Current models can often gather information during discovery but still fail to make the final exploitation leap.
  - Evidence: "The model other models sort of have been able to reason across everything. If we look at the discovery phase they do capture nearly all the different information they need and they never are able to make the leap into what is the exploitation they need to do."
- The defense strategy the speakers advocate is to train fast models and make them available to many companies instead of relying on a small number of providers.
  - Evidence: "of that for us I think the solution is just to take our future and say well it's going to be a speed challenge we're going to train our model we're going to run them fast and make them available to basically every company who wants to be protected so exciting I would say it's"

### Claims From The Talk
- The speaker argues that defensive cyber systems are being squeezed because they must operate at scale with limited human intervention, while frontier models are making offensive work faster and cheaper. (`explicit`)
  - Evidence: "Um, and part of the problem with the existing stack is that defensive systems have to operate at scale."
- The talk argues that open source models are not a side issue but part of the solution, because collaboration and deployability matter for cyber defense. (`explicit`)
  - Evidence: "We have no doubt that open source models have to be part of this solution because um they allow for many things that we'll talk about as well and there's this deep need for collaboration."
- The speaker claims that high-quality evals, high-quality data, and good benchmarks could push cyber toward the same kind of capability gains that coding saw. (`explicit`)
  - Evidence: "But what if through very high quality evals, very high quality data, good benchmarks, we could get to a place where the attackers are um simply outperformed by very very very good defenders."
- The benchmark is built from real zero-days found by human researchers and then turned into black-box environments that force reasoning across chained applications rather than code reading. (`explicit`)
  - Evidence: "So we find our own zero days in widely uh distributed open source software. We use that to create these t these real live huge environments of a bunch of different um applications chained together that then allows us to basically create this blackbox setting where the model doesn't see the code and it doesn't know about the zero date because we found it ourselves and it has to find a way uh to reason across this entire surface and understand exactly what the exploitation is."
- The speaker believes that if models become very good and very fast at these capability leaps, defenders can gain a lasting edge that attackers do not currently have. (`explicit`)
  - Evidence: "This is exactly the type of capability that we believe. If every model in the world could get really really really good at doing this and very fast, that should give a lasting defense uh and capability to the defenders that the attackers simply don't have right now."
- The talk argues that speed is a major constraint and that defenders will need specialized models and hardware rather than depending on only a few big providers. (`explicit`)
  - Evidence: "and speed will be where you know you you want to have a specialized model that's maybe running on specialized hardware and actually is is going to be very important and here I think the the danger is to say we're just going to rely on two company that everyone knows here to solve all"

### Topics Covered
- [[agent-security|Cyber economics]] — How frontier models are changing the attack and defense balance in cyber.
- [[agent-security|Access control]] — A first-foothold vulnerability class where permissions and logic matter more than obvious bugs.
- **Black-box cyber evaluation** — Evaluating models in a live but hidden system with limited information and no source access.
- [[agent-evaluations|Deterministic grading]] — Verifying each action in a long exploitation chain with machine-checkable scoring.
- [[agent-security|Open source model adaptation]] — Using collaboration and post-training to adapt open source models for defense.

### Tools And Named Systems
- [[gpt-5-5|GPT 5.5]] — A model used in the live attempts against the benchmark task.
- **Opus** — A model mentioned alongside GPT 5.5 in the attempted solve.
- **Keycloak** — An application in the benchmark chain used in the real solve example.
- **Vault** — Another application in the benchmark chain used in the real solve example.
- **Bach** — The internal orchestrator used to run the actual eval.

### Novel Concepts And Methods
- **Human-first data creation** — Create training data from real zero-day findings instead of synthetic toy tasks.
- **Black-box evaluation** — Run models in a black-box environment without internet or source access so they must reason from observed behavior and allowed tools.
- **Stepwise deterministic grading** — Use deterministic graders to verify every step in a long exploitation chain, not just final success.
- **Partial-grader depth analysis** — Measure how far the model gets through exploitation with partial graders that expose depth of progress.
- **Access-control scoping** — Focus the benchmark on access control as a representative logic-heavy entry point into real systems.

### Open Questions
- **How should this benchmark family expand beyond access control while keeping the tasks realistic and verifiable?** — The speakers explicitly want to cover more of cyber, and scope determines whether the approach generalizes.
- **What fine-tuning or post-training recipe best teaches models to defend against these attacks rather than merely recognize them?** — The talk says good data is only the first step; the training method is still open.
- **How can defenders achieve the latency and throughput needed for real-time protection at scale?** — The speakers frame speed as the core race between attacker and defender.

### Derived Links And Source Material
- [[youtube-O-CBZ3JtRvo-transcript]] — dedicated official recording transcript.
- [[youtube-O-CBZ3JtRvo]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/O-CBZ3JtRvo--2026-06-30-uri-rolls-training-frontier-models-to-out-think-hackers.json`.

### Speaker Context
- [[uri-rolls|Uri Rolls]]
- [[thom-wolf|Thom Wolf]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[uri-rolls]]
- [[thom-wolf]]

## Official YouTube Recording
- [[youtube-O-CBZ3JtRvo|Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face]] — official AI Engineer YouTube recording published 2026-07-24.
- Evidence status: [[youtube-O-CBZ3JtRvo-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-O-CBZ3JtRvo]] - dedicated official event recording.
- [[youtube-O-CBZ3JtRvo-transcript]] - dedicated official recording transcript.

- Source video: `youtube-O-CBZ3JtRvo`
- Slide deck: [[youtube-O-CBZ3JtRvo-slides|Slides: Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face]] — 21 visible slide image(s).
![[assets/slides/O-CBZ3JtRvo/slide-001.jpg]]
![[assets/slides/O-CBZ3JtRvo/slide-002.jpg]]
![[assets/slides/O-CBZ3JtRvo/slide-003.jpg]]
- Slide-derived themes for `youtube-O-CBZ3JtRvo`: training, models, attackers, engineering, future, track, july, arithmetic.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/O-CBZ3JtRvo.txt` (3,557 words).

## Transcript Markdown
- [[youtube-O-CBZ3JtRvo-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/O-CBZ3JtRvo.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-O-CBZ3JtRvo` — 3,557 transcript words; 9 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-O-CBZ3JtRvo`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-O-CBZ3JtRvo`: model, cyber, models, able, reason, been, benchmark, understand.
- Slide-derived themes for `youtube-O-CBZ3JtRvo`: training, models, attackers, engineering, future, track, july, arithmetic.
- Evidence links for `youtube-O-CBZ3JtRvo` (primary event evidence): [[youtube-O-CBZ3JtRvo]], [[youtube-O-CBZ3JtRvo-transcript]], [[youtube-O-CBZ3JtRvo-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
