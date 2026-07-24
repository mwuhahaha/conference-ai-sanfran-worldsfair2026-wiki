---
title: "Model Whisperers: How Evals and Prompts Shape Agent Behavior"
category: "talks"
date: "2026-06-30"
time: "1:30pm-1:50pm"
track: "Evals"
room: "Track 5"
speakers: ["Chris Souza", "Preetika Bhateja", "Daniel Bump"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Evals"
scheduleRoom: "Track 5"
scheduleLabels: ["Evals", "Track 5", "sponsor", "confirmed"]
---
# Model Whisperers: How Evals and Prompts Shape Agent Behavior

## Conference Context
- Date/time: 2026-06-30 · 1:30pm-1:50pm
- Track/room: Evals · Track 5
- Speaker(s): Chris Souza, Preetika Bhateja, Daniel Bump
- Session type/status: sponsor · confirmed

- Track: Evals
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
Getting an AI agent to behave the way you want isn’t just about writing better prompts. In real systems, behavior emerges from a loop: prompts->evals->iteration->feedback. Small changes in any part of that loop can completely change outcomes. We saw this while building a seed asset agent - a system that turns messy, real-world advertising creatives (low quality images, cluttered visuals, heavy text overlays) into clean, reusable assets for downstream Gen AI tools. The agent acts like an editor, simplifying visuals, removing unnecessary elements, and isolating core content so that additional context (like text or CTAs) can be added back in a more controlled, brand-safe way. But the real challenge wasn’t just building the agent - it was making it reliable. And prompting alone wasn’t enough. What actually moved the system forward was how we defined success—and how we used evals to reinforce it. Over time, evals stopped being just a way to measure quality. They became part of how the agent learned what “good” looks like. In this talk, we’ll cover: Why prompting alone doesn’t give you stable agent behavior How evals act like feedback signals, not just scorecards How we built evals sets that reflect the real-world Using agent trace logs to understand why things fail (not just that they fail) How to iterate without breaking things you already fixed By the end, you’ll have a set of patterns you can apply to any system dealing with messy/continuously changing data and how to tweak your prompt and evals to accommodate such changes.

## Synthesis
### Transcript-Backed Summary
The talk argues that stable agent behavior comes from a loop of prompts, evals, iteration, and feedback, not from prompt writing alone. In the AI Engineer World’s Fair session, the speakers frame production reliability as a function of the agent’s capabilities, its guardrails, and the quality of the eval system around it, using their YouTube ads work as the concrete example. The main tradeoff is that early intuition-driven probing is fast and revealing but not scalable, while production-grade evals must be strict, measurable, and continuously refreshed from real data so the team can catch regressions, understand failure patterns, and improve the system without breaking what already works.

### Key Takeaways
- Start with a small set of core tasks and expand the eval later.
  - Evidence: "Um you can just kind of start with a few core tasks. So you can look through your agent and define what are the primary things that you want to target, right?"
- Test negatives, not only successful task completion, because absence of a bad behavior matters too.
  - Evidence: "Um, and so here it's important to also test the negatives. Checking if the model like didn't do something as bad, uh, something bad is just as critical as checking if it did the task."
- Use trace review when aggregate metrics do not explain a policy violation or unexpected failure.
  - Evidence: "So we really had to look at the traces to see what was going on. And in this example, you can see in the initial trace, it actually detects that there is a disclaimer in what it's searching for and it says, okay, I found a disclaimer and now I'm going to go ahead and remove it, which was not what we asked it to do."
- Define launch criteria and acceptable regressions before treating a model as ready.
  - Evidence: "What's an acceptable regression versus not? Things like that. As you're doing these systems, it's important to like uh get some clarity early on on what is your gatekeeping rule like what's your launch criteria."
- Keep the eval set and test data aligned with changing production behavior.
  - Evidence: "Uh important to of course keep it evolving. That's why we talked about having your online eval having test sets that are refreshed with production data, having sampling pipelines, all sorts of things."

### Claims From The Talk
- The speakers argue that evals are not just scorecards; they are part of the feedback loop used to prove changes and drive iteration. (`explicit`)
  - Evidence: "Uh and then once your base structure is defined uh you can have you can then go to um having an eval and having a strong eval is very important as this gives you um like a way of proving the value of changes you make as well as running ablation experiments on any changes you make."
- They say agent reliability comes from the combination of agent capabilities, guardrails, and evals. (`explicit`)
  - Evidence: "Um so yeah the the reliability of your agent is basically a function of the capabilities of the agent uh the guard rails and the evals."
- They report that early intuition-based probing can be useful even though it is not scalable, because it reveals failure patterns quickly. (`explicit`)
  - Evidence: "Um so when you're first uh starting out it may be that uh you you know you could uh take a track of basically just going ahead and making the super comprehensive eval right um but we found it actually works better to first do intuition based approach where you kind of um first see"
- They argue that clear rubrics, concrete examples, and explanation capture are essential for human raters to be useful. (`explicit`)
  - Evidence: "Uh one was that providing them with a clear rubric of what they were actually rating with very clear examples."
- They show that trace inspection can uncover instruction-violating behavior that aggregate pass/fail metrics miss. (`explicit`)
  - Evidence: "So we really had to look at the traces to see what was going on. And in this example, you can see in the initial trace, it actually detects that there is a disclaimer in what it's searching for and it says, okay, I found a disclaimer and now I'm going to go ahead and remove it, which was not what we asked it to do."
- They emphasize that regression analysis should focus on recurring patterns across examples rather than isolated failures. (`explicit`)
  - Evidence: "Um so yeah this is basically just saying like it's very important to understand from these evals right what is the exact issue that you're having and figure out um the trade-offs here and then um you should also this is a very important point so you should focus on patterns rather than isolated runs"
- They say evals and test sets must keep evolving with production data and the current product stage. (`explicit`)
  - Evidence: "Uh important to of course keep it evolving. That's why we talked about having your online eval having test sets that are refreshed with production data, having sampling pipelines, all sorts of things."

### Topics Covered
- [[agent-evaluations|Eval-driven iteration]] — The idea that agent performance improves through a closed loop of prompts, evals, iteration, and feedback.
- [[agent-evaluations|Agent reliability]] — How to reason about whether an agent will behave reliably in production.
- [[agent-evaluations|Golden sets]] — A curated set of representative examples used to judge agent behavior.
- [[agent-evaluations|Trace analysis]] — Inspecting agent traces to understand why a failure occurred.
- [[agent-evaluations|LLM judging]] — Using model or automated judges alongside human raters and checking agreement.
- [[agent-evaluations|Launch readiness]] — Evaluating whether a system is ready to ship and what regressions are acceptable.

### Tools And Named Systems
- No named tool or system passed the transcript evidence gate.

### Novel Concepts And Methods
- **Prompt-eval feedback loop** — Use a prompt-eval-iteration-feedback loop to improve agent behavior without treating prompting as the whole solution.
- **Start-small eval design** — Begin with a small set of core tasks and expand later instead of waiting for a comprehensive golden set.
- **Rubric calibration** — Attach clear rating rubrics and concrete examples so raters can make consistent judgments.
- **Explanation capture** — Collect explanations for pass/fail decisions so the team can see why a rating was assigned.
- **Judge agreement monitoring** — Track how human and model judgments disagree over time to calibrate automated judging.
- **Trace-based debugging** — Inspect agent traces to diagnose failures that summary metrics conceal.

### Open Questions
- **How should a team calibrate an LLM judge against human raters without losing useful coverage across use cases?** — The talk treats judge alignment as a practical operational problem, but does not specify a complete calibration recipe.
- **How do you know when a golden set has become stale enough that it needs to be refreshed from production data?** — The speakers recommend keeping evals evolving, but the trigger for refresh is left open.
- **What launch metric should replace or complement precision and recall for a given agent task?** — They say launch criteria can differ by system, but do not define a universal metric choice.

### Derived Links And Source Material
- [[youtube-xyL2Ltkh-SA-transcript]] — dedicated official recording transcript.
- [[youtube-xyL2Ltkh-SA]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/xyL2Ltkh-SA--2026-06-30-chris-souza-model-whisperers-how-evals-and-prompts-shape-agent-behavior.json`.

### Speaker Context
- [[chris-souza|Chris Souza]]
- [[preetika-bhateja|Preetika Bhateja]]
- [[daniel-bump|Daniel Bump]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[chris-souza]]
- [[preetika-bhateja]]
- [[daniel-bump]]

## Official YouTube Recording
- [[youtube-xyL2Ltkh-SA|How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads]] — official AI Engineer YouTube recording published 2026-07-24.
- Evidence status: [[youtube-xyL2Ltkh-SA-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-xyL2Ltkh-SA]] - dedicated official event recording.
- [[youtube-xyL2Ltkh-SA-transcript]] - dedicated official recording transcript.

- Source video: `youtube-xyL2Ltkh-SA`
- Slide deck: [[youtube-xyL2Ltkh-SA-slides|Slides: How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads]] — 7 visible slide image(s).
![[assets/slides/xyL2Ltkh-SA/slide-001.jpg]]
![[assets/slides/xyL2Ltkh-SA/slide-002.jpg]]
![[assets/slides/xyL2Ltkh-SA/slide-003.jpg]]
- Slide-derived themes for `youtube-xyL2Ltkh-SA`: model, models, microsoft, hard, provides, foundation, critique, loop.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/xyL2Ltkh-SA.txt` (3,548 words).

## Transcript Markdown
- [[youtube-xyL2Ltkh-SA-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/xyL2Ltkh-SA.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-xyL2Ltkh-SA` — 3,548 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-xyL2Ltkh-SA`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-xyL2Ltkh-SA`: eval, important, doing, cases, should, having, scale, first.
- Slide-derived themes for `youtube-xyL2Ltkh-SA`: model, models, microsoft, hard, provides, foundation, critique, loop.
- Evidence links for `youtube-xyL2Ltkh-SA` (primary event evidence): [[youtube-xyL2Ltkh-SA]], [[youtube-xyL2Ltkh-SA-transcript]], [[youtube-xyL2Ltkh-SA-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
