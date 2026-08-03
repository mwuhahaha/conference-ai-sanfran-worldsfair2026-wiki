---
title: "Loop Engineering from first principles"
category: "talks"
date: "2026-06-29"
time: "3:45pm-4:05pm"
track: "Software Factories"
room: "Main Stage"
speakers: ["Kyle Mistele"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Software Factories"
scheduleRoom: "Main Stage"
scheduleLabels: ["Software Factories", "Main Stage", "session", "confirmed"]
---
# Loop Engineering from first principles

## Conference Context
- Date/time: 2026-06-29 · 3:45pm-4:05pm
- Track/room: Software Factories · Main Stage
- Speaker(s): Kyle Mistele
- Session type/status: session · confirmed

- Track: Software Factories
- Room: Main Stage
- Session type: session
- Status: confirmed

## Session Description
Code is free, software is infinite, and agents can do it all - that's the promise of the lights-off software factory, where humans interact only with tickets & specifications, and nobody reads the code, let alone writes it. We ran our own for six months, and we have the scars to prove it - bad code compounded, and agents created problems that agents couldn't solve - until we had to throw it all away. But this is a survivor's guide, not an obituary. In this talk, we'll share the challenges we encountered, what we liked, what we hated, what we're still doing, what we stopped doing, and what we started doing afterwards.

## Synthesis
### Transcript-Backed Summary
The talk argues that agentic software work should be built as control loops, not blind prompt-and-pray automation. The central mechanism is to define a measurable set point, detect the current state with sensors, choose an incremental change with a controller, and apply it through an agent acting inside a constrained workflow. The practical tradeoff is that the loop must stay small, deterministic, and reviewable: the speaker emphasizes baseline scans, feedback files, PR labels, and flow control so the team gets incremental progress without producing huge unreadable diffs or stacked work that humans cannot review.

### Key Takeaways
- A useful loop starts by defining the desired end state, adding a sensor for the property you care about, and letting that measurement drive incremental change.
  - Evidence: "loops and to do that we start by defining a set point which is the desired end state of our codebase with respect to some property of it and we add a sensor there's a lot of ways to build a sensor it can be strictly deterministic your eslint rules your as GP, your pack"
- A good sensor can be deterministic and language agnostic, which makes tools like asgrep useful for finding violations outside normal project configuration.
  - Evidence: "It's a great tool to have in your toolbox for building loops. It's language agnostic. It's out of band from your TypeScript config or ESLint rules, which if you're a TypeScript developer, you have watched Claude disable those with inline comments."
- The agent works better when it is given hand-built golden patterns and a response template instead of only generic internet-derived behavior.
  - Evidence: "You'll want to iterate on it over time based on what works. At human layer, we like to build out what we call golden patterns by hand before setting the agent loose."
- Tracking feedback in version control makes loop steering observable, reversible, and easier to refine over time.
  - Evidence: "Looks kind of like this. And the benefit of doing this way is that now that feedback file with instructions is tracked in your version control."
- Limiting each loop to at most one open PR at a time prevents duplicated, conflicting, or unreviewed work from piling up.
  - Evidence: "This way we have exactly one PR at most open per loop at a time. No stacking, no duplication."

### Claims From The Talk
- The speaker argues that loops are valuable in the real world, but they should be designed so humans can still read and improve the code rather than blindly generating huge changes. (`strong`)
  - Evidence: "So today I want to talk about what I think works in the real world and what we've started doing at human layer which to be clear is still building loops right I think loops are super powerful but we can design loops and still read the code in fact we can design loops that"
- He frames the core engineering model as control theory: measure the current state, compare it to a desired set point, generate a control signal, and apply incremental change. (`explicit`)
  - Evidence: "Control theory is all about how we drive a dynamic system which would be your codebase towards some desired stable or optimal end state."
- The talk presents an internal migration loop that scans for unmigrated procedures, tracks violations on main, and uses the results to guide incremental adoption of Effect. (`explicit`)
  - Evidence: "Uh for our loop, we are incrementally migrating our RPC API to effect. We adopted it for some of our raceprone code."
- He says low-friction human feedback can be built by storing loop instructions in a version-controlled markdown file and loading it into the agent each run. (`explicit`)
  - Evidence: "And the way to do this is to just create a feedback file that's tracked in version control just as a markdown file, right?"
- He also argues for flow control so each loop keeps at most one open PR at a time, preventing duplicated or stacked work that humans have not reviewed. (`explicit`)
  - Evidence: "And so now we just had all this like junk we had to deal with that wasn't important. So this is actually a really easy problem to fix uh because each loop and its workflow has a label that gets attached to PRs."

### Topics Covered
- **Control theory** — Designing software workflows as feedback systems with sensors, controllers, actuators, and incremental correction.
- [[coding-agents|Agentic code loops]] — Using agent-driven automation to make small, reviewable code changes instead of large unreadable PRs.
- [[software-factories|Loop flow control]] — Constraining automation with baseline scans, open-PR checks, labels, and versioned feedback so human review remains manageable.

### Tools And Named Systems
- **asgrep** — A language-agnostic search tool used to detect unmigrated procedures and other code patterns.
- **GitHub Actions** — A hosted CI platform suggested for running the loop because it already has repository, secret, and scheduling access.
- **GitLab** — A version-control and CI platform mentioned as an alternative place to run the same loop workflow.

### Novel Concepts And Methods
- **Incremental control loop** — A control-loop workflow that measures a codebase property, chooses an incremental change, applies it, and re-measures on the next iteration.
- **Baseline-and-diff gating** — A deterministic pre-scan that finds and sorts violations on main before allowing incremental PRs to proceed.
- **Version-controlled feedback channel** — A tracked markdown feedback file loaded into agent context on every run so humans can steer the loop without editing the workflow live.
- **Loop flow control** — A PR label plus open-PR check that pauses a loop when the previous iteration is still awaiting review.

### Open Questions
- **How should the controller be tuned so the agent makes the right-sized change instead of an overly large or wrong change?** — The talk says a poorly tuned controller can cause trouble quickly, so tuning determines whether the loop stays safe and useful.
- **What telemetry signals are most useful for choosing which code path to migrate when the goal is not just parity but better error handling and instrumentation?** — The speaker suggests feeding telemetry into the control signal, but the best selection criteria are still an open design choice.
- **How far can a loop be sped up by batching several procedures or assigning multiple PRs before review cost, context separation, or conflicts erase the gains?** — The talk proposes faster modes, but the safe upper bound is not established.

### Derived Links And Source Material
- [[youtube-xIt_mTQp6mY-transcript]] — dedicated official recording transcript.
- [[youtube-xIt_mTQp6mY]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/xIt_mTQp6mY--2026-06-29-kyle-mistele-loop-engineering-from-first-principles.json`.

### Speaker Context
- [[kyle-mistele|Kyle Mistele]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[kyle-mistele]]

## Official YouTube Recording
- [[youtube-xIt_mTQp6mY|Loop Engineering from First Principles — Kyle Mistele, HumanLayer]] — official AI Engineer YouTube recording published 2026-07-25.
- Evidence status: [[youtube-xIt_mTQp6mY-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-xIt_mTQp6mY]] - dedicated official event recording.
- [[youtube-xIt_mTQp6mY-transcript]] - dedicated official recording transcript.

- Source video: `youtube-xIt_mTQp6mY`
- Slide deck: [[youtube-xIt_mTQp6mY-slides|Slides: Loop Engineering from First Principles — Kyle Mistele, HumanLayer]] — 32 visible slide image(s).
![[assets/slides/xIt_mTQp6mY/slide-001.jpg]]
![[assets/slides/xIt_mTQp6mY/slide-002.jpg]]
![[assets/slides/xIt_mTQp6mY/slide-003.jpg]]
- Slide-derived themes for `youtube-xIt_mTQp6mY`: loop, engineering, system, first, kyle, reed, measured, controller.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/xIt_mTQp6mY.txt` (3,455 words).

## Transcript Markdown
- [[youtube-xIt_mTQp6mY-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/xIt_mTQp6mY.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-xIt_mTQp6mY` — 3,455 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-xIt_mTQp6mY`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-xIt_mTQp6mY`: loops, code, loop, control, change, controller, skill, doing.
- Slide-derived themes for `youtube-xIt_mTQp6mY`: loop, engineering, system, first, kyle, reed, measured, controller.
- Evidence links for `youtube-xIt_mTQp6mY` (primary event evidence): [[youtube-xIt_mTQp6mY]], [[youtube-xIt_mTQp6mY-transcript]], [[youtube-xIt_mTQp6mY-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
