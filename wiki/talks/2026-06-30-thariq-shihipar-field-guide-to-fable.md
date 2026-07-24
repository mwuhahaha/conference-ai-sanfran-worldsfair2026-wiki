---
title: "Field Guide to Fable"
category: "talks"
date: "2026-06-30"
time: "9:05am-9:25am"
track: "Autoresearch"
room: "Main Stage"
speakers: ["Thariq Shihipar"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Autoresearch"
scheduleRoom: "Main Stage"
scheduleLabels: ["Autoresearch", "Main Stage", "keynote", "confirmed"]
---
# Field Guide to Fable

## Conference Context
- Date/time: 2026-06-30 · 9:05am-9:25am
- Track/room: Autoresearch · Main Stage
- Speaker(s): Thariq Shihipar
- Session type/status: keynote · confirmed

- Track: Autoresearch
- Room: Main Stage
- Session type: keynote
- Status: confirmed

## Session Description
https://x.com/trq212/status/2027463795355095314

## Synthesis
### Transcript-Backed Summary
The talk argues that Fable is not just a stronger chat model but a different operating regime: it creates capability overhang, so the main job is to learn how to work with it rather than merely ask it for answers. The speaker’s method is to unhobble both the model and the human: give Claude more effective tools and less constraining prompting, then use the model to expose unknowns through blind spot passes, interviews, references, and post-run explanations. The practical consequence is that coding work becomes faster and more exploratory, but that speed only matters if teams stay in the loop, keep testing assumptions, and push past inherited tradeoffs to generate real value.

### Key Takeaways
- Giving the model tools to search and act in its environment can be more powerful than simply increasing context size.
  - Evidence: "But it turns out that instead, if you give it arms, like you give it the bash tool and ways to work with the environment, it can build and search its own context."
- The way the model asks for help has become richer over time, moving from simple multiple-choice prompts to embedded questions in HTML reports.
  - Evidence: "Uh, another feature I really like is the ask you a question tool. This is something I worked on when I first got to Claude code."
- The useful distinction is between the map in your head and the territory of the actual codebase or problem space.
  - Evidence: "When I'm working on a coding problem, the plan and prompt and spec that I have in my mind is the map, right?"
- A blind spot pass can reveal relevant dead ends, gotchas, and missing context before work starts.
  - Evidence: "Can you do a blind spot pass to help me figure out my relevant unknown unknowns and help me prompt better, right?\" And so, this like might have Claude go through the the auth module and figure out like, \"Oh, you know, this is kind of like a hairy little uh dead end that comes up a lot.\" Maybe search in my Git diff or Slack."
- Staying in the loop with Fable is central because it reduces drift between what you want and what gets built.
  - Evidence: "And I think that's like one of the most important parts of Fable is like staying in the loop and making sure that you uh you get what you want."
- The bar for proving agents matters is to produce the best work faster than before, not just to automate busywork.
  - Evidence: "Because I think the only way to prove that agents work is to do the best work of our lives faster than ever before."

### Claims From The Talk
- The speaker argues that Fable should be understood through capability overhang: it can do qualitatively more when paired with the right tools, rather than just being a bigger chat model. (`explicit`)
  - Evidence: "And so, this is what I mean by like unhobbling Claude. We call this capability overhang, right?"
- He reports that Anthropic removed 80% of the Claude Code system prompt because newer models need less constraint and more context. (`explicit`)
  - Evidence: "But there's there's more here. So, for example, uh, we recently removed 80% of the system prompt for Claude code, right?"
- He argues that Claude can be used to surface unknown unknowns by actively probing a project, not just executing a requested task. (`explicit`)
  - Evidence: "So, I'm going to go over a few examples of how I do that with Fable. Um The first is I like to do what I call a blind spot pass."
- He argues that tradeoffs are less fixed than people assume and that Fable changes how ambitious work can be pursued. (`explicit`)
  - Evidence: "I call this being unreasonable. One of my favorite parts of Anthropic is that we believe that tradeoffs are not real."
- He states that building has become easier, but generating value is still hard, so the real challenge remains choosing and validating worthwhile work. (`explicit`)
  - Evidence: "Uh I think it's also worth calling out that building is easier, but generating value is still hard."

### Topics Covered
- [[model-capability-and-product-framing|Field guide to Fable]] — How to adapt prompting, tools, and harnesses to a new model class with more latent capability.
- [[model-capability-and-product-framing|Capability overhang]] — The idea that model usefulness can jump when paired with tools instead of only scaling parameters or context.
- **Map and territory** — The distinction between what the operator thinks they know and the real constraints in the environment.
- **Unknown unknowns** — Structured techniques for uncovering missing requirements before implementation.
- [[coding-agents|Grief and gain from AI coding]] — The emotional and professional adjustment to faster, easier coding workflows.
- [[coding-agents|Unreasonableness]] — The push to pursue more ambitious goals instead of accepting familiar constraints.

### Tools And Named Systems
- [[claude-code|Claude Code]] — The coding assistant the speaker says he works on and uses as the basis for the talk's workflow.
- [[fable|Fable]] — The model family the talk is about and the central subject of the field guide.
- [[claude-tag|Claude Tag]] — The proactive agent product the speaker says was recently rolled out to unlock multiplayer work.
- **Opus 4** — The model variant used as a reference point for the progression in question-asking ability.
- [[opus-4-8|Opus 4.8]] — A later model variant used as an example of improved ability to generate HTML reports with embedded questions.
- **HTML** — The markup format used for richer reports and prompt-facing outputs in the examples.

### Novel Concepts And Methods
- **Unhobbling the model** — Treat the model as needing growth through tools, data, feedback, and harness design rather than assuming a fixed capability ceiling.
- **Blind spot pass** — Use the model to identify what you do not know by probing blind spots before committing to implementation.
- **Model interview** — Ask the model to interview the operator so missing requirements and architecture-changing questions surface early.
- **Reference-driven prompting** — Provide a reference artifact as a map so the model can infer the target behavior from an example instead of a long spec.
- **Implementation notes** — Log deviations and unknowns during execution so the resulting plan can be audited and corrected.
- **Operator quiz** — Have the model quiz the operator on what happened to confirm understanding and keep the human in the loop.

### Open Questions
- **What exactly counts as capability overhang in Fable, and which tasks become possible only once the right tool or harness is added?** — This determines how to discover new uses for the model instead of underestimating it.
- **When should a newer model get a smaller system prompt instead of more examples and constraints?** — This affects how to prompt the model without unnecessarily limiting its behavior.
- **What prompting format best elicits architecture-changing questions without overwhelming the user?** — This shapes whether the interview approach is actually useful in real projects.
- **How can teams distinguish real tradeoffs from assumptions that only seem unavoidable?** — This affects how ambitious a team can be when adopting Fable.

### Derived Links And Source Material
- [[youtube-9fubhllmsBU-transcript]] — dedicated official recording transcript.
- [[youtube-9fubhllmsBU]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/9fubhllmsBU--2026-06-30-thariq-shihipar-field-guide-to-fable.json`.

### Speaker Context
- [[thariq-shihipar|Thariq Shihipar]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[thariq-shihipar]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-TqC1qOfiVcQ-dense-slides]] (26 viable slide images).
- Related slide/OCR pages:
- [[youtube-TqC1qOfiVcQ-dense-slides]]
- [[youtube-TqC1qOfiVcQ-reconstructed-slides]]
- [[youtube-TqC1qOfiVcQ-slides]]
- Slide-derived terms: `claude`, `code`, `bash`, `workflows`, `anthrop`, `skills`, `tool`, `file`, `tools`, `system`, `files`, `tial`, `tasks`, `models`, `context`, `query`, `call`, `example`

## Official YouTube Recording
- [[youtube-9fubhllmsBU|Field Guide to Fable — Thariq Shihipar, Anthropic]] — official AI Engineer YouTube recording published 2026-07-06.
- Evidence status: [[youtube-9fubhllmsBU-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-9fubhllmsBU]] - dedicated official event recording.
- [[youtube-9fubhllmsBU-transcript]] - dedicated official recording transcript.
- [[youtube-TqC1qOfiVcQ]] - supporting context; not the exact session recording.

- Source video: `youtube-9fubhllmsBU`
- Slide deck: [[youtube-9fubhllmsBU-slides|Slides: Field Guide to Fable — Thariq Shihipar, Anthropic]] — 13 visible slide image(s).
![[assets/slides/9fubhllmsBU/slide-001.jpg]]
![[assets/slides/9fubhllmsBU/slide-002.jpg]]
![[assets/slides/9fubhllmsBU/slide-003.jpg]]
- Slide-derived themes for `youtube-9fubhllmsBU`: land, king, guide, unknowns, fable, dealing, grief, models.
- Source video: `youtube-TqC1qOfiVcQ`
- Slide deck: [[youtube-TqC1qOfiVcQ-dense-slides|Dense Slides: Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — slide evidence page.
- Additional slide evidence: [[youtube-TqC1qOfiVcQ-slides|Slides: Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]], [[youtube-TqC1qOfiVcQ-reconstructed-slides|Reconstructed Slides: Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]]
- Slide-derived themes for `youtube-TqC1qOfiVcQ`: claude, code, file, system, tools, prompts, custom, features.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/9fubhllmsBU.txt` (3,542 words).

## Transcript Markdown
- [[youtube-9fubhllmsBU-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/9fubhllmsBU.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-9fubhllmsBU` — 3,542 transcript words; 9 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-9fubhllmsBU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-9fubhllmsBU`: claude, fable, code, give, models, prompt, model, little.
- Slide-derived themes for `youtube-9fubhllmsBU`: land, king, guide, unknowns, fable, dealing, grief, models.
- Evidence links for `youtube-9fubhllmsBU` (primary event evidence): [[youtube-9fubhllmsBU]], [[youtube-9fubhllmsBU-transcript]], [[youtube-9fubhllmsBU-slides]]
- `youtube-TqC1qOfiVcQ` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-TqC1qOfiVcQ`: claude, code, file, system, tools, prompts, custom, features.
- Evidence links for `youtube-TqC1qOfiVcQ` (supporting context only): [[youtube-TqC1qOfiVcQ]], [[youtube-TqC1qOfiVcQ-slides]], [[youtube-TqC1qOfiVcQ-dense-slides]], [[youtube-TqC1qOfiVcQ-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
