---
title: Software Factories
category: topics
sourceLabels:
  - Official schedule
  - Public YouTube livestream transcript
  - Local slide OCR
last_auto_summarized: '2026-07-18T13:19:38.026Z'
sourceAssessment:
  schemaVersion: 1
  claimId: claim:2ebffdab952df23254670a2efb37c05b7fcd63b2459f6042eee551d2c1cac804
  subjectId: concept:software-factories
  domain: topics page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-24T00:00:00.000000Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-official-sessions
  - source:official-wf26-youtube--I5W5QVAT8E
  - source:official-wf26-youtube-8qWIPUia2O8
  - source:official-wf26-youtube-VrpEyglYgeU
  - source:official-wf26-youtube-c35YoMdnI78
  - source:official-wf26-youtube-n97BCfyFIvw
sourceAssessmentBodySha256: sha256:79c13eabb44ad2ebd1cb7d48bb8c5d6c25d8d9d89845fc83a7ecd6e96bed0763
---
# Software Factories

## Overview
At World’s Fair 2026, a software factory is presented as a governed production system for agent-assisted engineering: work enters through structured intake, receives assembled context and a plan, moves through scoped implementation and sandboxed execution, and exits only after evaluation, human review, release controls, and recorded outcomes. [[2026-06-29-uday-kiran-medisetty-agentic-sdlc-at-uber-building-blocks-for-uber-s-software-factory]] places those building blocks inside an enterprise SDLC, [[2026-06-29-nnenna-ndukwe-how-to-build-quality-gates-into-agentic-coding-workflows]] makes quality gates explicit within the coding workflow, and [[2026-06-30-suraj-gupta-warp-building-self-improving-agent-software-factories]] extends the model toward factories that learn from completed work rather than repeatedly starting from an empty prompt.

The linked sessions distinguish this system from a collection of coding assistants. [[2026-06-29-shane-wolf-the-best-sdlc-is-the-one-you-build-yourself-why-orchestration-changes-everything]] argues for an organization-specific orchestration layer, while [[2026-06-29-kyle-mistele-loop-engineering-from-first-principles]] focuses on the design of the engineering loop itself. [[2026-07-01-ryan-cooke-no-that-s-not-a-software-factory]] supplies the necessary counterpoint by challenging loose use of the label. Factory’s forward-deployed engineering session, Atlassian’s SDLC workshop, Qodo AI’s quality-gate workshop, HumanLayer’s loop-engineering session, and Warp’s self-improving-factory talk show different operational slices of the same problem: assigning work, constraining agent action, validating results, and feeding evidence back into the next run.

Across that graph, the defining properties are durable stages, shared artifacts, explicit owners, bounded permissions, observable handoffs, measurable acceptance criteria, rollback paths, and feedback tied to real delivery outcomes. Coding agents are specialized participants within this system—not autonomous substitutes for the engineering organization. A chat interface that generates code is therefore an ingredient, not a factory; the factory is the repeatable mechanism that turns a request into reviewed, traceable, releasable software.

## Conference Context
The idea comes from assembly-line metaphors in software engineering, CI/CD, DevOps, internal developer platforms, and automated code generation. AI agents make the factory metaphor more literal because parts of the SDLC can be delegated to tool-using systems.

## How This Theme Evolved
- **World's Fair 2024 (local comparison fixture):** Coding agents sat inside a broader code-generation and AI-engineering discipline.
- **Miami 2026 (public comparison wiki):** The focus narrowed to developer workflow, agent-ready interfaces, runtimes, IDEs, context, and quality gates.
- **World's Fair 2025 (local comparison fixture):** The comparison corpus emphasized shipping, evaluating, securing, and reviewing production coding agents.
- **World's Fair 2026 (current event synthesis backed by linked local evidence):** The linked conference graph frames coding agents as software-factory components governed by eval gates, context systems, and execution boundaries.

**Confidence:** medium-high.
**Boundary:** Earlier event wikis are comparison context only. They are not primary evidence for World's Fair 2026 claims, and no local fixture is represented as a public live site.
**Comparison source:** [[aie-wiki-generation-delta]].

## Significance
A single coding assistant is useful, but organizations need repeatability, governance, and quality gates. Software factories focus on the whole production system: intake, context, implementation, validation, review, deployment, and learning.

## Why This Matters Now
The unit of engineering is shifting from an isolated assistant interaction to a repeatable production system that delegates, verifies, and records software work.

**WF26 evidence gate:** this section was emitted only because the page links to configured local evidence. Relevant configured evidence: [[2026-06-29-nnenna-ndukwe-how-to-build-quality-gates-into-agentic-coding-workflows]], [[2026-06-29-uday-kiran-medisetty-agentic-sdlc-at-uber-building-blocks-for-uber-s-software-factory]], [[2026-06-30-suraj-gupta-warp-building-self-improving-agent-software-factories]].

**Confidence:** medium-high. Comparison history is context; linked WF26 pages remain the evidence for current-event claims.

## Applied Use
Model the workflow as stages with inputs, outputs, owners, and acceptance checks. Give agents scoped roles, shared artifacts, test gates, traceability, and rollback paths. Measure cycle time, defect rate, review burden, and production outcomes.

They fit engineering organizations, platform teams, internal tools groups, migration projects, and product teams with repeatable implementation patterns.

Use a software-factory approach when many similar tasks flow through the same path or when agent work needs governance. Avoid overbuilding it for occasional one-off tasks.

## Active Use Cases
- Agent-assisted feature delivery pipelines.
- Automated maintenance, migration, and dependency-update programs.
- Multi-agent planning, coding, testing, and review workflows.
- Internal developer platforms with AI-native task orchestration.

## Practical Lesson
Evaluate the complete agent loop: task definition, context assembly, tool permissions, sandbox execution, verification, review, and provenance. Model capability alone is not the system boundary.

**Confidence:** medium-high. Treat this as synthesis derived from the linked evidence graph, not as an official schedule claim.

## Livestream Source
- [[youtube-htM02KMNZnk]] — official WF2026 Software Factories and keynote livestream.
- [[youtube-htM02KMNZnk-slides]] — extracted slide/OCR deck for the livestream.

## Transcript Digest Evidence
This section synthesizes 4 evidence-bound talk topic candidates across at least two talks.

### Cross-Talk Synthesis
End-to-end delivery systems that turn requests into shipped software through coordinated loops, scaffolding, and ownership boundaries. The recurring variation is whether the focus is harnesses, delivery orchestration, or long-term maintainability, with the tradeoff being throughput versus codebase health.

### Constituent Talk Evidence
- [[2026-06-29-dex-horthy-harness-engineering-is-not-enough-why-software-factories-fail|Harness Engineering is not Enough: Why Software Factories Fail]] — Breaking implementation into coordinated end-to-end chunks across a system.
  - Transcript: [[youtube-Ib5GBkD555M-transcript]]
  - Evidence: "Um which is the order of implementation, multi-reo coordination. How are we going to build this across our entire system and how are we going to check it along the way?"
- [[2026-06-29-sam-bhagwat-every-harness-will-become-a-claw|Every Harness Will Become A Claw]] — The stage where the industry focus has shifted from agents to harnesses.
  - Transcript: [[youtube-8qWIPUia2O8-transcript]]
  - Evidence: "Um and uh the thing that I'm going to say is is welcome to the harness era. What do I mean by the harness era?"
- [[2026-06-30-tariq-shaukat-in-the-land-of-ai-agents-the-verifiers-are-king|'In the Land of AI Agents, the Verifiers Are King']] — The growth of maintainability, reliability, and security debt as agents generate more code.
  - Transcript: [[youtube-VrpEyglYgeU-transcript]]
  - Evidence: "And then the last point I mentioned is technical debt does explode. Right? As you generate code, technical debt is also generated."

## Neighboring Subjects
- [[coding-agents]]
- [[agent-security]]
- [[agent-evaluations]]
- [[ai-sandboxes]]

## Connections
- [[2026-07-01-session-the-software-factory]] — The Software Factory; speaker TBD (Day 4 — Session Day 3 · 2:50pm-3:10pm · Expo Stage 4 SE; official schedule)
- [[2026-06-29-shane-wolf-the-best-sdlc-is-the-one-you-build-yourself-why-orchestration-changes-everything]] — The best SDLC is the one you build yourself: Why orchestration changes everything; [[shane-wolf|Shane Wolf]], [[andrei-bocan|Andrei Bocan]] (Day 1 — Workshop Day · 9:00am-11:00am · Workshops Day 1; official schedule)
- [[2026-06-29-uday-kiran-medisetty-agentic-sdlc-at-uber-building-blocks-for-uber-s-software-factory]] — Agentic SDLC at Uber: Building Blocks for Uber's Software Factory; [[uday-kiran-medisetty|Uday Kiran Medisetty]], [[adam-huda|Adam Huda]] (Day 2 — Session Day 1 · 11:40am-12:00pm · AI-Native Enterprises; official schedule)
- [[2026-07-01-ryan-cooke-no-that-s-not-a-software-factory]] — No, That's Not a Software Factory; [[ryan-cooke|Ryan Cooke]] (Day 4 — Session Day 3 · 10:45am-11:05am · Expo Stage 3; official schedule)
- [[2026-06-29-tereza-t-kov-rise-of-the-software-factory]] — Rise of the Software Factory; [[tereza-t-kov|Tereza Tížková]] (Day 2 — Session Day 1 · 11:10am-11:30am · Software Factories; official schedule)
- [[2026-06-29-eno-reyes-how-forward-deployed-engineering-is-done-at-factory]] — How Forward Deployed Engineering is done at Factory; [[eno-reyes|Eno Reyes]] (Day 2 — Session Day 1 · 10:45am-11:05am · Forward Deployed Engineering; official schedule)
- [[2026-06-29-kyle-mistele-loop-engineering-from-first-principles]] — Loop Engineering from first principles; [[kyle-mistele|Kyle Mistele]] (Day 2 — Session Day 1 · 3:45pm-4:05pm · Software Factories; official schedule)
- [[2026-06-30-christopher-manning-building-the-simulation-infrastructure-for-practical-world-model-use]] — Building the simulation infrastructure for practical world model use; [[christopher-manning|Christopher Manning]] (Day 3 — Session Day 2 · 10:45am-11:05am · Robotics & World Models; official schedule)
- [[2026-06-30-christopher-manning-building-the-simulation-infrastructure-for-practical-world-model-use-part-2]] — Building the simulation infrastructure for practical world model use (Part 2); [[christopher-manning|Christopher Manning]] (Day 3 — Session Day 2 · 11:10am-11:30am · Robotics & World Models; official schedule)
- [[2026-06-29-nnenna-ndukwe-how-to-build-quality-gates-into-agentic-coding-workflows]] — How to Build Quality Gates into Agentic Coding Workflows; [[nnenna-ndukwe|Nnenna Ndukwe]] (Day 1 — Workshop Day · 11:05am-12:05pm · Workshops Day 1; official schedule)
- [[2026-06-29-joel-hooks-the-art-and-science-of-loopcraft-with-pi-and-friends]] — The Art and Science of Loopcraft with Pi (and friends); [[joel-hooks|Joel Hooks]] (Day 1 — Workshop Day · 4:30pm-5:30pm · Workshops Day 1; official schedule)
- [[2026-06-30-suraj-gupta-warp-building-self-improving-agent-software-factories]] — Warp: Building Self-Improving Agent Software Factories; [[suraj-gupta|Suraj Gupta]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Expo Stage 3 SW; official schedule)

- [[christopher-manning|Christopher Manning]]
- [[shane-wolf|Shane Wolf]]
- [[andrei-bocan|Andrei Bocan]]
- [[uday-kiran-medisetty|Uday Kiran Medisetty]]
- [[adam-huda|Adam Huda]]
- [[ryan-cooke|Ryan Cooke]]
- [[tereza-t-kov|Tereza Tížková]]
- [[eno-reyes|Eno Reyes]]
- [[kyle-mistele|Kyle Mistele]]
- [[nnenna-ndukwe|Nnenna Ndukwe]]
- [[joel-hooks|Joel Hooks]]
- [[suraj-gupta|Suraj Gupta]]

- [[atlassian|Atlassian]]
- [[uber|Uber]]
- [[factory|Factory]]
- [[moonlake-ai|Moonlake AI]]
- [[workos|WorkOS]]
- [[humanlayer|HumanLayer]]
- [[qodo-ai|Qodo AI]]
- [[badass-dev-egghead-io|badass.dev / egghead.io]]
- [[warp|Warp]]

- [[2026-07-01-mike-chambers-harness-engineering-building-the-production-cage-for-powerful-domain-agents]] — Harness Engineering: Building the Production Cage for Powerful Domain Agents; [[mike-chambers|Mike Chambers]] (Day 4 — Session Day 3 · 12:05pm-12:25pm · Harness Engineering; related YouTube resource; via [[youtube-qdZzND79mcg]])
- [[2026-07-01-dru-knox-harness-engineering-the-new-core-skill-for-agentic-developers]] — Harness Engineering: The New Core Skill for Agentic Developers; [[dru-knox|Dru Knox]] (Day 4 — Session Day 3 · 2:50pm-3:10pm · Expo Stage 1 NE; related YouTube resource; via [[youtube-qdZzND79mcg]])

- [[mike-chambers|Mike Chambers]]
- [[dru-knox|Dru Knox]]

- [[amazon-web-services-aws|Amazon Web Services (AWS)]]
- [[tessl|Tessl]]

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 29 | Related pages outside the main evidence categories. |
| resources | 10 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 15 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 17 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| transcripts | 9 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-uday-kiran-medisetty-agentic-sdlc-at-uber-building-blocks-for-uber-s-software-factory]]
- [[2026-06-29-nnenna-ndukwe-how-to-build-quality-gates-into-agentic-coding-workflows]]
- [[2026-06-30-suraj-gupta-warp-building-self-improving-agent-software-factories]]
- [[2026-06-29-shane-wolf-the-best-sdlc-is-the-one-you-build-yourself-why-orchestration-changes-everything]]
- [[2026-06-29-kyle-mistele-loop-engineering-from-first-principles]]
- [[2026-07-01-ryan-cooke-no-that-s-not-a-software-factory]]

### Resources
- [[aie-wiki-generation-delta]]
- [[youtube-htM02KMNZnk]]
- [[youtube-qdZzND79mcg]]
- [[youtube-I2cbIws9j10]]
- [[youtube-Ib5GBkD555M]]
- [[youtube--I5W5QVAT8E]]

### Slides
- [[youtube-htM02KMNZnk-slides]]
- [[youtube-I2cbIws9j10-slides]]
- [[youtube-I2cbIws9j10-dense-slides]]
- [[youtube-Ib5GBkD555M-slides]]
- [[youtube--I5W5QVAT8E-slides]]
- [[youtube-c35YoMdnI78-slides]]

### Transcripts
- [[youtube-I2cbIws9j10-transcript]]
- [[youtube-Ib5GBkD555M-transcript]]
- [[youtube--I5W5QVAT8E-transcript]]
- [[youtube-c35YoMdnI78-transcript]]
- [[youtube-n97BCfyFIvw-transcript]]
- [[youtube-4sX_He5c4sI-transcript]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.

### Linked Sessions
- [[2026-06-29-uday-kiran-medisetty-agentic-sdlc-at-uber-building-blocks-for-uber-s-software-factory|Agentic SDLC at Uber: Building Blocks for Uber's Software Factory]]
- [[2026-06-29-nnenna-ndukwe-how-to-build-quality-gates-into-agentic-coding-workflows|How to Build Quality Gates into Agentic Coding Workflows]]
- [[2026-06-30-suraj-gupta-warp-building-self-improving-agent-software-factories|'Warp: Building Self-Improving Agent Software Factories']]
- [[2026-06-29-shane-wolf-the-best-sdlc-is-the-one-you-build-yourself-why-orchestration-changes-everything|>-]]
- [[2026-06-29-kyle-mistele-loop-engineering-from-first-principles|Loop Engineering from first principles]]
- [[2026-07-01-ryan-cooke-no-that-s-not-a-software-factory|No, That's Not a Software Factory]]
- [[2026-07-01-session-the-software-factory|The Software Factory]]
- [[2026-06-29-tereza-t-kov-rise-of-the-software-factory|Rise of the Software Factory]]
- [[2026-06-29-eno-reyes-how-forward-deployed-engineering-is-done-at-factory|How Forward Deployed Engineering is done at Factory]]
- [[2026-06-30-christopher-manning-building-the-simulation-infrastructure-for-practical-world-model-use|Building the simulation infrastructure for practical world model use]]

### Media Signals
- `youtube-I2cbIws9j10` — 91,792 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-I2cbIws9j10`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: choosing, model, quality, dominates, agentic, capabilities, customization, support.
- Evidence links for `youtube-I2cbIws9j10` (primary event evidence): [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
- `youtube-Ib5GBkD555M` — 4,045 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Ib5GBkD555M`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Ib5GBkD555M`: code, review, model, coding, software, stuff, test, better.
- Slide-derived themes for `youtube-Ib5GBkD555M`: software, harness, enough, team, engineering, factories, fail, pierre.
- Evidence links for `youtube-Ib5GBkD555M` (primary event evidence): [[youtube-Ib5GBkD555M]], [[youtube-Ib5GBkD555M-transcript]], [[youtube-Ib5GBkD555M-slides]]
- `youtube--I5W5QVAT8E` — 4,014 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube--I5W5QVAT8E`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube--I5W5QVAT8E`: model, notion, today, customers, product, okay, always, system.
- Slide-derived themes for `youtube--I5W5QVAT8E`: engineering, plan, future, fair, recently, purchased, each, subscription.
- Evidence links for `youtube--I5W5QVAT8E` (primary event evidence): [[youtube--I5W5QVAT8E]], [[youtube--I5W5QVAT8E-transcript]], [[youtube--I5W5QVAT8E-slides]]
- `youtube-c35YoMdnI78` — 11,538 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-c35YoMdnI78`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-c35YoMdnI78`: loops, loop, software, code, today, debate, engineering, should.
- Slide-derived themes for `youtube-c35YoMdnI78`: hands, reek, loan, take, career, karen, comets.
- Evidence links for `youtube-c35YoMdnI78` (primary event evidence): [[youtube-c35YoMdnI78]], [[youtube-c35YoMdnI78-transcript]], [[youtube-c35YoMdnI78-slides]]
- `youtube-n97BCfyFIvw` — 3,068 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-n97BCfyFIvw`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-n97BCfyFIvw`: code, still, taste, loop, engineering, evidence, system, human.
- Slide-derived themes for `youtube-n97BCfyFIvw`: roles, google, look, across, worth, doing, increasingly, automated.
- Evidence links for `youtube-n97BCfyFIvw` (primary event evidence): [[youtube-n97BCfyFIvw]], [[youtube-n97BCfyFIvw-transcript]], [[youtube-n97BCfyFIvw-slides]]
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-4sX_He5c4sI`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: lots, examples, stream, starts, july, land, king, chief.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube-htM02KMNZnk` — 89,050 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-htM02KMNZnk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-htM02KMNZnk`: model, code, models, loop, well, software, first, team.
- Slide-derived themes for `youtube-htM02KMNZnk`: apps, github, copilot, welcome, engineer, fair, single, line.
- Evidence links for `youtube-htM02KMNZnk` (primary event evidence): [[youtube-htM02KMNZnk]], [[youtube-htM02KMNZnk-transcript]], [[youtube-htM02KMNZnk-slides]], [[youtube-htM02KMNZnk-dense-slides]], [[youtube-htM02KMNZnk-reconstructed-slides]]
- `youtube-bVNNvWq6dKo` — 6 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-bVNNvWq6dKo`: always, believed, future, software, write, analyzes, content, most.
- Evidence links for `youtube-bVNNvWq6dKo` (supporting context only): [[youtube-bVNNvWq6dKo]], [[youtube-bVNNvWq6dKo-slides]], [[youtube-bVNNvWq6dKo-dense-slides]], [[youtube-bVNNvWq6dKo-reconstructed-slides]]
