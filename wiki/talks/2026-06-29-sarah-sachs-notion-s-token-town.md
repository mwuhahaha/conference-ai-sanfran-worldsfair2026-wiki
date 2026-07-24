---
title: "Notion's Token Town"
category: "talks"
date: "2026-06-29"
time: "2:50pm-3:10pm"
track: "Software Factories"
room: "Main Stage"
speakers: ["Sarah Sachs"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Software Factories"
scheduleRoom: "Main Stage"
scheduleLabels: ["Software Factories", "Main Stage", "session", "confirmed"]
---
# Notion's Token Town

## Conference Context
- Date/time: 2026-06-29 · 2:50pm-3:10pm
- Track/room: Software Factories · Main Stage
- Speaker(s): Sarah Sachs
- Session type/status: session · confirmed

- Track: Software Factories
- Room: Main Stage
- Session type: session
- Status: confirmed

## Session Description
No official description published in the schedule data.

## Synthesis
### Transcript-Backed Summary
Sarah Sachs argues that the real problem in building AI-native products is not just capability but sustainable economics. Her central thesis is that teams need leverage: they should stay model-agnostic, route traffic by task, evaluate providers on whole trajectories, and use open-weight models or CPUs whenever frontier models are unnecessary. The talk then extends that logic into software factories, where active documents and multi-agent orchestration can automate real work, but only if teams also account for security, governance, and the risks created by private data, untrusted content, and external communication.

### Key Takeaways
- Keep optionality so you can walk away from a provider when pricing or terms become untenable.
  - Evidence: "not actually having a Frontier product and remember that that optionality is your leverage if you don't have the capability to walk at any point you are stuck."
- Do not send every request to the most expensive frontier model when simpler tasks are being overcharged.
  - Evidence: "When you triage an email inbox, if we're charging you to do that on Opus, we're ripping you off and ourselves."
- Trade eval-program value and expertise for better terms when that preserves flexibility better than a large commitment.
  - Evidence: "We find that our eval program partnerships actually help us a lot with Frontier Labs and is something that we can exchange instead of extraordinarily large commits and I don't think the discount is ever worth the loss in optionality."
- Use deterministic code paths for jobs like CSV-to-PDF conversion or SQL queries instead of paying for an LLM.
  - Evidence: "Like you don't need an LLM to turn a CSV into a PDF. You don't need an LLM to talk to notion tool calls if we have a CLI."
- A software factory cannot work without both model optionality and clear judgment about which model fits which task.
  - Evidence: "We cannot do this without optionality and we cannot do this without conviction that we understand what models are required for which tasks."

### Claims From The Talk
- The speaker argues that a supplier that also builds competing products is structurally a bad token-economics partner and leaves customers with weak exit options. (`explicit`)
  - Evidence: "Um, your supplier is your competitor. I know very few people who have convinced me that that's not true."
- The speaker says the winning strategy is not token economics alone but product advantage built from data flywheels, customer understanding, and the right capability-cost tradeoffs. (`explicit`)
  - Evidence: "I don't think that that's winning on the token economics. I think it's about product. It's about building data flywheels and understanding your customers better than anyone else."
- The speaker reports that Notion runs a model-agnostic setup, with an auto model handling about 75 percent of traffic and model switching available to avoid vendor lock-in. (`explicit`)
  - Evidence: "Notion's auto model does this really well. We have state-of-the-art models available always."
- The speaker argues that open-weight models are now strong enough for many tasks and create downward pricing pressure as well as negotiation leverage. (`explicit`)
  - Evidence: "um openweight models are really strong enough to handle these tasks and the possibility to RL on top of them has also kind of expanded the upmarket growth that they can cover."
- The speaker reports that many jobs do not need GPUs or an LLM at all, and that deterministic work can be handled by CPUs and Workers instead. (`explicit`)
  - Evidence: "So, be prepared now. And the last thing is CPUs over GPUs. Um, we've we've recently launched something at notion called workers."
- The speaker warns that combining private data, untrusted content, and external communication creates the lethal trifecta of security risk, especially as systems become more autonomous. (`explicit`)
  - Evidence: "Let's start there. There's this concept called the lethal trifecta. Simon Wilson, I think, crafted this."
- The speaker shows Notion's current workflow where tasks in active documents can be scoped, iterated, and handed to agents and coding tools to produce a spec or a PR. (`explicit`)
  - Evidence: "We already have the ability to inspect tasks. And you can imagine any task that you look at um in a notion document."

### Topics Covered
- **Token economics** — The economics of buying and reselling model tokens, including margin pressure and vendor leverage.
- [[model-capability-and-product-framing|Model optionality]] — A product strategy that keeps multiple models available and avoids locking the business to one provider.
- [[agent-evaluations|Trajectory evaluation]] — Judging providers by end-to-end task outcomes rather than by single-call metrics.
- [[model-capability-and-product-framing|Open-weight models]] — Using open-weight models as a practical alternative for many production tasks.
- [[inference-engineering|CPU offload]] — Moving deterministic or low-complexity work off LLMs and onto CPUs or lightweight services.
- [[agent-security|Lethal trifecta]] — The security risk created when private data, untrusted content, and external communication coexist in autonomous systems.
- [[active-documents-and-live-work-surfaces|Active documents]] — Collaborative documents that act as live work surfaces for humans and agents.
- [[software-factories|Multi-agent orchestration]] — Coordinating multiple agents and humans across a software delivery workflow.

### Tools And Named Systems
- [[notion|Notion]] — The company platform the speaker describes as the durable system of record and collaboration layer for humans and agents.
- [[claude|Claude]] — The AI agent used inside Notion to scope tasks and help drive collaborative workflows.
- [[claude-code|Claude Code]] — The coding agent the speaker says can spin up a PR during the workflow demo.
- **Parallel** — The web search provider mentioned in the partnership example used for trajectory-based evaluation.
- **Decagon** — The AI tool the speaker says can collect the right data needed for the workflow.
- **Workers** — The product the speaker says Notion recently launched to handle discrete pieces of code on CPUs.

### Novel Concepts And Methods
- **Capability-cost routing** — Route work by capability, latency, and cost instead of defaulting to the most capable model for every request.
- **Model-agnostic routing** — Keep multiple models available so the product can switch when pricing, quality, or availability changes.
- **Trajectory evaluation** — Evaluate vendors on entire task trajectories rather than on single-call latency or cost alone.
- **Open-weight fallback** — Use open-weight models as a credible fallback and bargaining tool when frontier models are expensive or overkill.
- **CPU offload** — Move deterministic workflows to CPUs or Workers instead of spending tokens on jobs that do not need an LLM.
- **Active-document orchestration** — Treat tasks as active documents that multiple agents and humans can update collaboratively, including scoping, feedback, and PR creation.

### Open Questions
- **How can teams design evals that capture full task trajectories instead of only measuring single-call cost or latency?** — That determines whether provider comparisons reflect real product outcomes or just narrow benchmarks.
- **How should autonomous systems safely combine private data, untrusted content, and external communication without exposing the lethal trifecta?** — This is the core safety boundary for agentic products that operate on enterprise workflows.
- **Which workloads should stay on frontier models versus move to open weights or CPUs as capability gaps continue to close?** — That choice controls both margins and long-term vendor leverage.

### Derived Links And Source Material
- [[youtube--I5W5QVAT8E-transcript]] — dedicated official recording transcript.
- [[youtube--I5W5QVAT8E]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/-I5W5QVAT8E--2026-06-29-sarah-sachs-notion-s-token-town.json`.

### Speaker Context
- [[sarah-sachs|Sarah Sachs]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[sarah-sachs]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-6YdPI9YbjbI-dense-slides]] (2 viable slide images).
- Related slide/OCR pages:
- [[youtube-6YdPI9YbjbI-dense-slides]]
- [[youtube-6YdPI9YbjbI-reconstructed-slides]]
- [[youtube-6YdPI9YbjbI-slides]]
- Slide-derived terms: `evals`, `microsoft`, `evaluation`, `datasets`, `scorer`, `prompt`, `human`, `improve`, `scorers`, `world`, `across`, `scoring`, `evaluate`, `deploy`, `help`, `braintrust.dev`, `logs`, `review`

## Official YouTube Recording
- [[youtube--I5W5QVAT8E|Notion's Token Town — Sarah Sachs, Notion]] — official AI Engineer YouTube recording published 2026-07-23.
- Evidence status: [[youtube--I5W5QVAT8E-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube--I5W5QVAT8E]] - dedicated official event recording.
- [[youtube--I5W5QVAT8E-transcript]] - dedicated official recording transcript.
- [[youtube-6YdPI9YbjbI]] - supporting context; not the exact session recording.

- Source video: `youtube--I5W5QVAT8E`
- Slide deck: [[youtube--I5W5QVAT8E-slides|Slides: Notion's Token Town — Sarah Sachs, Notion]] — 12 visible slide image(s).
![[assets/slides/-I5W5QVAT8E/slide-001.jpg]]
![[assets/slides/-I5W5QVAT8E/slide-002.jpg]]
![[assets/slides/-I5W5QVAT8E/slide-003.jpg]]
- Slide-derived themes for `youtube--I5W5QVAT8E`: engineering, plan, future, fair, recently, purchased, each, subscription.
- Source video: `youtube-6YdPI9YbjbI`
- Slide deck: [[youtube-6YdPI9YbjbI-dense-slides|Dense Slides: How to build world-class AI products — Sarah Sachs (AI lead @ Notion) &  Carlos Esteban (Braintrust)]] — slide evidence page.
- Additional slide evidence: [[youtube-6YdPI9YbjbI-slides|Slides: How to build world-class AI products — Sarah Sachs (AI lead @ Notion) &  Carlos Esteban (Braintrust)]], [[youtube-6YdPI9YbjbI-reconstructed-slides|Reconstructed Slides: How to build world-class AI products — Sarah Sachs (AI lead @ Notion) &  Carlos Esteban (Braintrust)]]
- Slide-derived themes for `youtube-6YdPI9YbjbI`: across, sign, access, join, ease, acme, uses, stripe.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/-I5W5QVAT8E.txt` (4,014 words).

## Transcript Markdown
- [[youtube--I5W5QVAT8E-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/-I5W5QVAT8E.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube--I5W5QVAT8E` — 4,014 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube--I5W5QVAT8E`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube--I5W5QVAT8E`: model, notion, today, customers, product, okay, always, system.
- Slide-derived themes for `youtube--I5W5QVAT8E`: engineering, plan, future, fair, recently, purchased, each, subscription.
- Evidence links for `youtube--I5W5QVAT8E` (primary event evidence): [[youtube--I5W5QVAT8E]], [[youtube--I5W5QVAT8E-transcript]], [[youtube--I5W5QVAT8E-slides]]
- `youtube-6YdPI9YbjbI` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-6YdPI9YbjbI`: across, sign, access, join, ease, acme, uses, stripe.
- Evidence links for `youtube-6YdPI9YbjbI` (supporting context only): [[youtube-6YdPI9YbjbI]], [[youtube-6YdPI9YbjbI-slides]], [[youtube-6YdPI9YbjbI-dense-slides]], [[youtube-6YdPI9YbjbI-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
