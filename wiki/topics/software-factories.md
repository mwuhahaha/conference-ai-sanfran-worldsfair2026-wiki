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
  - source:official-wf26-youtube-APqXGyCoGW4
  - source:official-wf26-youtube-GgLQ02aO-hs
  - source:official-wf26-youtube-c35YoMdnI78
  - source:official-wf26-youtube-iCj_ATyThvc
  - source:official-wf26-youtube-n97BCfyFIvw
  - source:official-wf26-youtube-pMggiOb18tc
  - source:official-wf26-youtube-xUnRQ9vLXxo
sourceAssessmentBodySha256: sha256:f23df858205e1f1c5d4e2cd4cb3781c7618b1234c1a7aa15040111b8f7ec2348
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
This section synthesizes 17 evidence-bound talk topic candidates across at least two talks.

### Cross-Talk Synthesis
These talks frame software delivery as a managed production system with orchestration, reusable execution units, and end-to-end vertical slices. The variation is between factory-like planning and the harness layer that actually executes work, but both treat delivery as an industrial process that can be decomposed, repeated, and scaled.

### Constituent Talk Evidence
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering|The Golden Age of AI Engineering]] — Long-lived coordination between a manager agent and worker agents.
  - Transcript: [[youtube-pMggiOb18tc-transcript]]
  - Evidence: "I was no longer pairing. I was managing 10 direct reports. Now I mostly talk to a longunning manager which delegates work to a team."
- [[2026-06-29-dex-horthy-harness-engineering-is-not-enough-why-software-factories-fail|Harness Engineering is not Enough: Why Software Factories Fail]] — Human-in-the-loop planning and review before implementation.
  - Transcript: [[youtube-Ib5GBkD555M-transcript]]
  - Evidence: "Um, so turning the lights back on, we're going to put the code review back. Uh, we're going to embrace this approach of like how do we plan up front to reduce the chance that we have a long or uh difficult review process."
- [[2026-06-29-pauline-brunet-how-forward-deployed-engineering-is-done-at-cursor|How Forward Deployed Engineering is done at Cursor]] — Turning close customer work into signals for product and roadmap decisions.
  - Transcript: [[youtube-APqXGyCoGW4-transcript]]
  - Evidence: "And then finally, you have to work very delicately between the product and engineering teams and your customers, where you want to give that feedback loop to your product team saying, \"Hey, we're hearing this over and over again.\" Uh and the FTE team is so close to the customers, embedded in their organizations, they're going to be the first ones have a really good pulse on what we should build next as a company."
- [[2026-06-29-sam-bhagwat-every-harness-will-become-a-claw|Every Harness Will Become A Claw]] — A future consolidation in which only a few high-value systems remain salient.
  - Transcript: [[youtube-8qWIPUia2O8-transcript]]
  - Evidence: "um which is that and and it's something that like I don't think we we sort of talk about as much uh but after this after this phase where where we're sort of making everything more and more powerful um there will be a shakeout um and and let me walk you through sort of uh through my reasoning here which is that in the 2010s we had these platforms we had Android, we had iOS."
- [[2026-06-29-sarah-sachs-notion-s-token-town|Notion's Token Town]] — Coordinating multiple agents and humans across a software delivery workflow.
  - Transcript: [[youtube--I5W5QVAT8E-transcript]]
  - Evidence: "Usually she does, but multi-agent orchestration is important. Maybe Claude Code isn't the best at customer voice, but Decagon is, right?"
- [[2026-06-30-addy-osmani-closing-keynote|Closing Keynote]] — The pattern where cheaper software creation expands the set of problems people want built.
  - Transcript: [[youtube-n97BCfyFIvw-transcript]]
  - Evidence: "It's going to move the bottleneck from can we build this to should this exist and can we answer for it?"
- [[2026-06-30-zhengyao-jiang-an-ai-agent-became-the-1-contributor-in-openai-s-hiring-challenge|An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge]] — The role of architecture or API boundaries in steering search and preventing bad solutions.
  - Transcript: [[youtube-iCj_ATyThvc-transcript]]
  - Evidence: "The other one I think is really underrated is codebased abstraction. The abstraction provides the framework that auto research can iterate on and uh that's also that starting point hugely bias the whole search direction."
- [[2026-07-01-maxime-rivest-the-unreasonable-effectiveness-of-separating-the-task-from-the-model|The Unreasonable Effectiveness of Separating the Task from the Model]] — The idea that AI programs should be built and optimized like ordinary reusable functions.
  - Transcript: [[youtube-GgLQ02aO-hs-transcript]]
  - Evidence: "To make a function, you give it a name. You define some inputs, some outputs, and then you have some implementation logic inside of it."
- [[2026-07-01-theo-browne-closing-keynote-theo-browne|Closing Keynote — Theo Browne]] — The talk emphasizes models coordinating and verifying multi-step work.
  - Transcript: [[youtube-xUnRQ9vLXxo-transcript]]
  - Evidence: "figure it out a lot of the time. figure it out a lot of the time. Mythos is another jump Mythos is another jump Mythos is another jump to orchestration."
- [[2026-07-01-yohei-nakajima-active-graph-agent-runtime-babyagi-4|Active Graph Agent Runtime (BabyAGI 4)]] — Bundling object schemas, tools, behaviors, and policies into reusable agent units.
  - Transcript: [[youtube-khVX_BUnEwU-transcript]]
  - Evidence: "And when you bring it all together, you got these kind of object schemas, tools, deterministic LLM behaviors can be assembled into a something called a pack, right?"

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
| talks | 24 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| transcripts | 14 | Transcript markdown; check session matching and caption quality. |

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
- [[youtube-Ib5GBkD555M]]
- [[youtube--I5W5QVAT8E]]
- [[youtube-n97BCfyFIvw]]

### Slides
- [[youtube-htM02KMNZnk-slides]]
- [[youtube-Ib5GBkD555M-slides]]
- [[youtube--I5W5QVAT8E-slides]]
- [[youtube-n97BCfyFIvw-slides]]
- [[youtube-I2cbIws9j10-slides]]
- [[youtube-I2cbIws9j10-dense-slides]]

### Transcripts
- [[youtube-pMggiOb18tc-transcript]]
- [[youtube-Ib5GBkD555M-transcript]]
- [[youtube-APqXGyCoGW4-transcript]]
- [[youtube-8qWIPUia2O8-transcript]]
- [[youtube--I5W5QVAT8E-transcript]]
- [[youtube-n97BCfyFIvw-transcript]]
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
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering|The Golden Age of AI Engineering]]
- [[2026-06-29-dex-horthy-harness-engineering-is-not-enough-why-software-factories-fail|Harness Engineering is not Enough: Why Software Factories Fail]]
- [[2026-06-29-pauline-brunet-how-forward-deployed-engineering-is-done-at-cursor|How Forward Deployed Engineering is done at Cursor]]
- [[2026-06-29-sam-bhagwat-every-harness-will-become-a-claw|Every Harness Will Become A Claw]]

### Media Signals
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
- `youtube-n97BCfyFIvw` — 3,068 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-n97BCfyFIvw`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-n97BCfyFIvw`: code, still, taste, loop, engineering, evidence, system, human.
- Slide-derived themes for `youtube-n97BCfyFIvw`: roles, google, look, across, worth, doing, increasingly, automated.
- Evidence links for `youtube-n97BCfyFIvw` (primary event evidence): [[youtube-n97BCfyFIvw]], [[youtube-n97BCfyFIvw-transcript]], [[youtube-n97BCfyFIvw-slides]]
- `youtube-I2cbIws9j10` — 91,792 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-I2cbIws9j10`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: choosing, model, quality, dominates, agentic, capabilities, customization, support.
- Evidence links for `youtube-I2cbIws9j10` (primary event evidence): [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
- `youtube-c35YoMdnI78` — 11,538 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-c35YoMdnI78`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-c35YoMdnI78`: loops, loop, software, code, today, debate, engineering, should.
- Slide-derived themes for `youtube-c35YoMdnI78`: hands, reek, loan, take, career, karen, comets.
- Evidence links for `youtube-c35YoMdnI78` (primary event evidence): [[youtube-c35YoMdnI78]], [[youtube-c35YoMdnI78-transcript]], [[youtube-c35YoMdnI78-slides]]
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
