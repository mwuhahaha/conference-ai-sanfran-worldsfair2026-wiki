---
title: "The Unreasonable Effectiveness of Separating the Task from the Model"
category: "talks"
date: "2026-07-01"
time: "9:40am-10:00am"
track: "Harness Engineering"
room: "Main Stage"
speakers: ["Maxime Rivest", "Isaac Miller"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Harness Engineering"
scheduleRoom: "Main Stage"
scheduleLabels: ["Harness Engineering", "Main Stage", "keynote", "confirmed"]
---
# The Unreasonable Effectiveness of Separating the Task from the Model

## Conference Context
- Date/time: 2026-07-01 · 9:40am-10:00am
- Track/room: Harness Engineering · Main Stage
- Speaker(s): Maxime Rivest, Isaac Miller
- Session type/status: keynote · confirmed

- Track: Harness Engineering
- Room: Main Stage
- Session type: keynote
- Status: confirmed

## Session Description
By declaring your task’s inputs and outputs without initially considering model capability, you create the space needed to figure out the model execution later. DSPy’s entire promise is that you should evaluate and execute your AI engineering at a level higher than a specific prompt template or a particular provider’s API shape: the Signature. However, models have evolved significantly over the last few years. How can the same input and output specifications still work in a world now filled with tools, RLMs, and Skills? By defining your task strictly through its inputs and outputs, the underlying implementation becomes completely flexible. You can experiment with different models, settings, weights, templating strategies, and output formats, all without touching your actual AI workflow. Consequently, you can leverage components built by others and focus entirely on your core AI task. In this talk we will present how dspy 3.5 makes it easier much easier. DSPy has its roots in prompt optimization, where we build efficient ways to conduct search and learning beneath the signature. In this talk we will give a preview of DSPy 4.0 where we use the fact that models have now passed a tipping point for two critical concepts we have always needed. First, we no longer need to limit the search space to a single instruction block per LLM call; models can now reliably write the code underneath a signature themselves—so they should. Second, traditional prompt optimization has always required a scalar metric, which is notoriously one of the hardest parts to get right. What if a DSPy program could learn directly from your interactions with users? Ultimately, all you care about is that the function you call respects the inputs and outputs of your signature. You can let the models figure out the rest.

## Synthesis
### Transcript-Backed Summary
The talk argues that AI engineering should start from the task contract, not from a model or prompt template. The core method is to specify what should happen with natural-language instructions, what must happen with code-enforced constraints, and what good looks like through examples and evals, then treat the implementation underneath as flexible. That separation is presented as the reason teams can swap models, add tools, and incorporate techniques like recursive language models without rewriting the workflow. The main tradeoff is that you must do the hard work of defining constraints and evaluation signals well, but the payoff is cheaper, more reliable, and more adaptable AI software.

### Key Takeaways
- Define the input and output contract first so the implementation can change without disturbing the task boundary.
  - Evidence: "If for your repeated AI task you define an input interface and an output interface, you get to play in the internals."
- Use code for constraints that must always hold, not just for guidance that a model may ignore.
  - Evidence: "They have to be enforced. The best way to do that is with code. So I want you to go to the third line, a fourth line."
- Examples are essential for capturing latent behavior that cannot be fully written as instructions or code.
  - Evidence: "And so through time with example I learned how to know that a tree is a maple. But this is not limited to things like classifying plants."
- Flexibility under a stable signature lets teams search for cheaper implementations and scale to larger data.
  - Evidence: "And you can use this to scale to data sizes that weren't possible with a more expensive implementation."

### Claims From The Talk
- The speaker argues that AI programs should inherit the same benefits as functions: reuse, composability, testability, and optimization. (`explicit`)
  - Evidence: "We believe the same should be true for AR programs. Functions are awesome. Functions are reusable, composable, testable, and optimizable."
- The speaker says a fixed interface lets the implementation change freely, including swapping in new models, without changing the surrounding workflow. (`explicit`)
  - Evidence: "I can change it however I want. A new model comes up and I can change that. It's super easy because my interface is fixed like that."
- The speaker reports that flexibility over implementation can make enterprise AI systems cheaper by letting teams search for lower-cost solutions. (`explicit`)
  - Evidence: "First is that your implementation becomes cheaper. When you're flexible to what the implementation is, you can use the bitter lesson to search over different solutions, find something that solves your problem cheaply."
- The speaker presents qualitative learning as a research direction for converting textual feedback into evals and a climbable objective. (`explicit`)
  - Evidence: "How do we decrease assistance? And it's a research question right now. But what we believe is that models are now good enough to interpret whatever textual feedback is present in the environment and convert that into evals and a hill that the model can climb."

### Topics Covered
- [[coding-agents|Task-model separation]] — The central idea that the task contract should stay stable while the implementation changes underneath it.
- [[model-capability-and-product-framing|Specs, code, and evals]] — The interface defined by natural-language instructions, code constraints, and evaluative examples.
- [[agent-evaluations|Qualitative learning]] — The use of product feedback and textual signals to improve evals without relying only on hand-built metrics.
- [[coding-agents|Implementation flexibility]] — The ability to substitute models and harnesses to reduce cost while preserving behavior.
- [[software-factories|Function-like AI programs]] — The idea that AI programs should be built and optimized like ordinary reusable functions.

### Tools And Named Systems
- [[dspy|DSPy]] — The open-source Python framework the talk uses to separate task specification from implementation details.
- **DSP.flex** — A new module described as a way to learn a harness over time while keeping the function interface constant.

### Novel Concepts And Methods
- **Function-style AI design** — Design AI programs with a function-like contract so the task can be reused and optimized independently of the implementation.
- **Specs-code-evals decomposition** — Separate instructions, code-enforced constraints, and examples/evals as three distinct parts of the task specification.
- **Stable-signature implementation** — Keep the signature fixed while changing the internal harness, model, or prompt strategy underneath it.
- **Example-driven behavior learning** — Learn from examples and latent behavioral patterns when instructions and code alone are insufficient.
- **Feedback-guided qualitative learning** — Use production feedback and textual signals to refine evaluation targets over time.

### Open Questions
- **How can a system reliably decrease human assistance by turning textual feedback into useful evals automatically?** — This is the central open research problem behind qualitative learning.
- **How should traces, user actions, and product analytics be represented so they can update the objective a model is climbing?** — The talk suggests production signals could replace hand-built proxies, but the conversion mechanism remains unresolved.

### Derived Links And Source Material
- [[youtube-GgLQ02aO-hs-transcript]] — dedicated official recording transcript.
- [[youtube-GgLQ02aO-hs]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/GgLQ02aO-hs--2026-07-01-maxime-rivest-the-unreasonable-effectiveness-of-separating-the-task-from-the-model.json`.

### Speaker Context
- [[maxime-rivest|Maxime Rivest]]
- [[isaac-miller|Isaac Miller]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[maxime-rivest]]
- [[isaac-miller]]

## Official YouTube Recording
- [[youtube-GgLQ02aO-hs|The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest & Isaac Miller]] — official AI Engineer YouTube recording published 2026-07-23.
- Evidence status: [[youtube-GgLQ02aO-hs-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-GgLQ02aO-hs]] - dedicated official event recording.
- [[youtube-GgLQ02aO-hs-transcript]] - dedicated official recording transcript.

- Source video: `youtube-GgLQ02aO-hs`
- Slide deck: [[youtube-GgLQ02aO-hs-slides|Slides: The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest, DSPy]] — 22 visible slide image(s).
![[assets/slides/GgLQ02aO-hs/slide-001.jpg]]
![[assets/slides/GgLQ02aO-hs/slide-002.jpg]]
![[assets/slides/GgLQ02aO-hs/slide-003.jpg]]
- Slide-derived themes for `youtube-GgLQ02aO-hs`: task, effectiveness, separating, unreasonable, model, programs, should, fair.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/GgLQ02aO-hs.txt` (2,751 words).

## Transcript Markdown
- [[youtube-GgLQ02aO-hs-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/GgLQ02aO-hs.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-GgLQ02aO-hs` — 2,751 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-GgLQ02aO-hs`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-GgLQ02aO-hs`: implementation, solve, dspi, model, should, problem, models, techniques.
- Slide-derived themes for `youtube-GgLQ02aO-hs`: task, effectiveness, separating, unreasonable, model, programs, should, fair.
- Evidence links for `youtube-GgLQ02aO-hs` (primary event evidence): [[youtube-GgLQ02aO-hs]], [[youtube-GgLQ02aO-hs-transcript]], [[youtube-GgLQ02aO-hs-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
