---
title: "How Kepler Built Verifiable AI for Financial Services"
category: "talks"
date: "2026-07-01"
time: "12:05pm-12:25pm"
track: "AI in Finance"
room: "Track 3"
speakers: ["Vinoo Ganesh"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "AI in Finance"
scheduleRoom: "Track 3"
scheduleLabels: ["AI in Finance", "Track 3", "session", "confirmed"]
---
# How Kepler Built Verifiable AI for Financial Services

## Conference Context
- Date/time: 2026-07-01 · 12:05pm-12:25pm
- Track/room: AI in Finance · Track 3
- Speaker(s): Vinoo Ganesh
- Session type/status: session · confirmed

- Track: AI in Finance
- Room: Track 3
- Session type: session
- Status: confirmed

## Session Description
Financial answers have to be auditable. Vinoo Ganesh (CEO, Kepler) shows how Kepler Finance pairs Claude's reasoning with deterministic verification infrastructure to index 26M+ SEC filings across 14,000+ companies and 27 markets — and validate every number back to the exact filing, page, and line item. A look at trust, provenance, and content engineering for AI in regulated finance.

## Synthesis
### Transcript-Backed Summary
Kepler's thesis is that financial AI becomes useful only when reasoning models are wrapped in a deterministic verification substrate that can prove every number back to its source. The mechanism is to split work so the model handles planning and provenance selection while code handles extraction, arithmetic, and reconciliation, which lets the system enforce atomic provenance, scope determinism, and derivation chains without trusting the model to compute. The practical payoff is faster, cheaper analyst work products that can survive audit and regulatory scrutiny, and the speaker argues this pattern will eventually extend beyond finance to other high-stakes domains.

### Key Takeaways
- Citations help with auditability, but verification is different because it must deterministically prove the number is right.
  - Evidence: "The citation is effectively an after-the-fact audit. Now, a verification is a deterministic, repeatable, numerically verifiable mechanism that we can use to produce validity that a number is right."
- Moving computation out of the model makes the system cheaper as well as more accurate.
  - Evidence: "This also is a lot cheaper because again, I don't need the model to do a bunch of stuff it shouldn't be doing."
- The immediate customer value is not an AI portfolio manager but an AI analyst that removes repetitive desk work.
  - Evidence: "Like they want the AI analyst. And so the thing they're most excited about is a way of rapidly producing, rapidly doing kind of the repeatable painful tasks that their analysts are doing."
- The main remaining problem is not generation; it is tracking provenance and proving the output fits the firm's rules.
  - Evidence: "The reading problem is still very open. And you verifying a data point is not enough anymore."

### Claims From The Talk
- The speaker argues that AI cannot produce verifiable work product in finance unless it is augmented with a deterministic substrate. (`explicit`)
  - Evidence: "Because it's a probability machine. It is great at next token prediction. So, the second contention of this whole talk is that you cannot use AI to produce verifiable work product in finance without augmenting it with a deterministic substrate."
- Atomic provenance means the model should emit a reference to the number rather than writing or manipulating the number itself. (`explicit`)
  - Evidence: "And that's because a wrong number is still wrong if you're in that unfortunate 6%. So, with atomic provenance, what we do is the model writes effectively a reference to the number."
- Scope determinism separates model planning from computation, leaving the actual calculation to deterministic tooling. (`explicit`)
  - Evidence: "[snorts] Um and so, what the model does is the model decides what to compute. It never does the computation itself."
- Because financial ratios and multiples are defined differently across organizations, the system needs a chain of events that shows what went into each output. (`strong`)
  - Evidence: "So, not only do we have to codify that in the processes that are run, but we need some kind of a chain of events to figure out what went into producing an individual number and what went into producing an outcome."
- The platform can consolidate financial statements in seconds while keeping every number tied back to its individual source. (`strong`)
  - Evidence: "What this allows us to do is this allows us to do things like consolidate financial statements in seconds with every number tied back to its individual source."
- The next open step is building verifiable ontologies that proxy a firm's investment processes rather than just reducing token spend. (`strong`)
  - Evidence: "The last remaining mile is going to be that personalization. So, the second version of this in 2027 hopefully one of us will be on stage talking about how we're now able to build verifiable ontologies that actually proxy our investment processes instead of saying how do I not spend a trillion tokens to solve this individual problem."

### Topics Covered
- **Verifiable AI for finance** — The central problem of making AI outputs auditable in regulated finance.
- [[context-engineering-and-knowledge-architecture|Atomic provenance]] — The requirement to trace every number back to its source document or internal record.
- [[observed-work-and-traceability|Scope determinism]] — Separating reasoning from computation so the model plans but does not calculate.
- [[context-engineering-and-knowledge-architecture|Derivation chains]] — Tracking the chain of steps that produced a financial metric or ratio.
- [[agent-evaluations|Firm-specific verification]] — Using codified firm rules to decide what outputs are allowed.
- **Cross-domain verifiable work product** — The broader idea that the same verification architecture can extend to other regulated domains.

### Tools And Named Systems
- **AI** — The reasoning model used as the front end for the workflow.
- **10-K** — The source of cited financial filings that the system verifies against.
- **Bloomberg** — The source layer used for market and company information that the speaker contrasts with Kepler's approach.
- **FactSet** — The other market-data product the speaker contrasts with Kepler's approach.
- **CapIQ** — The data product the speaker cites as an example of systems that contractors support.
- [[claude|Claude]] — The model family the speaker mentions as a comparison point for search-style outputs.

### Novel Concepts And Methods
- **Deterministic verification** — Deterministic verification gate that strips out numbers that cannot be independently verified.
- **Atomic provenance** — Atomic provenance that records the exact source for each extracted number before any downstream use.
- **Scope determinism** — Scope determinism that pushes arithmetic and parsing into code instead of the model.
- **Derivation chains** — Derivation chains that preserve the sequence of steps used to produce a financial output.
- **Replayable derivation** — Replayable and rewindable event chains for rebuilding how an output was produced.
- **Allowed-output constraints** — Firm-specific verification rules that codify what the system is allowed to produce.

### Open Questions
- **How can a firm have the system track its own provenance while still enforcing its unique investment philosophy?** — The talk says verifiability has to reflect each firm's rules, not just generic source tracking.
- **How do we build verifiable ontologies that actually proxy investment processes?** — The speaker frames this as the next remaining mile after the current verification layer.
- **How far can the same verification pattern be generalized to legal work, drug discovery, and other regulated domains?** — The speaker claims the finance pattern generalizes, but the domain-specific transformations still have to be built.

### Derived Links And Source Material
- [[youtube-Tt2kX2sgQio-transcript]] — dedicated official recording transcript.
- [[youtube-Tt2kX2sgQio]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/Tt2kX2sgQio--2026-07-01-vinoo-ganesh-how-kepler-built-verifiable-ai-for-financial-services.json`.

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
- [[youtube-Tt2kX2sgQio|How Kepler Built Verifiable AI for Financial Services — Vinoo Ganesh]] — official AI Engineer YouTube recording published 2026-07-29.
- Evidence status: [[youtube-Tt2kX2sgQio-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-Tt2kX2sgQio]] - dedicated official event recording.
- [[youtube-Tt2kX2sgQio-transcript]] - dedicated official recording transcript.

- Source video: `youtube-Tt2kX2sgQio`
- Slide deck: [[youtube-Tt2kX2sgQio-slides|Slides: How Kepler Built Verifiable AI for Financial Services — Vinoo Ganesh]] — 9 visible slide image(s).
![[assets/slides/Tt2kX2sgQio/slide-001.jpg]]
![[assets/slides/Tt2kX2sgQio/slide-002.jpg]]
![[assets/slides/Tt2kX2sgQio/slide-003.jpg]]
- Slide-derived themes for `youtube-Tt2kX2sgQio`: producing, hard, part, made, nearly, number, comes, based.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/Tt2kX2sgQio.txt` (3,846 words).

## Transcript Markdown
- [[youtube-Tt2kX2sgQio-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/Tt2kX2sgQio.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-Tt2kX2sgQio` — 3,846 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Tt2kX2sgQio`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Tt2kX2sgQio`: model, number, information, produce, producing, been, data, whole.
- Slide-derived themes for `youtube-Tt2kX2sgQio`: producing, hard, part, made, nearly, number, comes, based.
- Evidence links for `youtube-Tt2kX2sgQio` (primary event evidence): [[youtube-Tt2kX2sgQio]], [[youtube-Tt2kX2sgQio-transcript]], [[youtube-Tt2kX2sgQio-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
