---
title: "Don't Ship Skills Without Evals"
category: "talks"
date: "2026-06-30"
time: "3:20pm-3:40pm"
track: "Evals"
room: "Track 5"
speakers: ["Philipp Schmid"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Evals"
scheduleRoom: "Track 5"
scheduleLabels: ["Evals", "Track 5", "sponsor", "confirmed"]
---
# Don't Ship Skills Without Evals

## Conference Context
- Date/time: 2026-06-30 · 3:20pm-3:40pm
- Track/room: Evals · Track 5
- Speaker(s): Philipp Schmid
- Session type/status: sponsor · confirmed

- Track: Evals
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
There are thousands agent skills. Almost none of them are tested. They get vibe-checked with two manual runs, maybe a thumbs-up from a colleague, then shipped. You wouldn't merge code without tests — so why are we shipping skills without evals? This talk covers the full lifecycle of building reliable agent skills: what a skill actually is (and isn't), how to write one that triggers correctly, and how to build a lightweight eval harness that catches failures before your users do.

## Synthesis
### Transcript-Backed Summary
The talk argues that agent skills should not be shipped on intuition alone: because agents are non-deterministic and trigger failures are common, every important skill needs evals. The core method is to treat a skill as a layered artifact, keep the description lean and directive, push detail into reference files, and then verify behavior with small but targeted eval suites that include both should-use and should-not-use cases. The practical payoff is that you can catch over-triggering, wrong-tool selection, brittle prompts, and silent regressions before users see them, while also knowing when a skill has become unnecessary and can be retired to save cost and maintenance.

### Key Takeaways
- Write skill descriptions around both why and how the model should use the skill.
  - Evidence: "So, very important is the the why and the how for the model. So, why it should use that skill and then how it should use that skill."
- If the workflow is always the same, use a script instead of a skill.
  - Evidence: "You maybe you should write a script because if the the process or the workflow is always the same, you don't need to waste models and tokens for that exercise."
- Keep running evals with and without the skill so you can tell when the skill is no longer needed.
  - Evidence: "So, um always try to run evals with and without the skill enabled. And if the model achieves the performance without even like triggering the skill, you know you can retire that skill, save the cost uh for your tokens, and then also um don't keep like it redundant."
- Many failures come from the skill not being triggered correctly, especially when users do not describe their task in a way that matches the skill description.
  - Evidence: "The the skill skill description is very important. Uh we have seen 50% of the failures uh because the skill was not triggered correctly because the prompt of the user was not uh detailed enough for the model to understand, \"Hey, I need to use that skill to solve that task.\" And especially if you build agents for others, they are not aware of the skill descriptions you have for your model and for your skill."
- Run more than one trial per case because agent behavior is non-deterministic.
  - Evidence: "Then definitely run more than one trial when running evals. Like agents, our models are non-deterministic."

### Claims From The Talk
- The speaker reports that skills improve performance on average by roughly 15% in the Skill Bench update. (`explicit`)
  - Evidence: "So, do skills work? Yes, they do work and I going back to a skills bench which has an update of 1.1 which has evaluated all kinds of open and closed models in different harnesses showing that skills on average improve the performance by roughly 15%."
- The speaker argues that human-written skills are better than AI-generated skills, which can hurt performance. (`explicit`)
  - Evidence: "And what I found out is that human-written skills are the best we can provide. Uh AI-generated skills can uh impact performance negatively."
- The speaker recommends using real production traces when possible because they are more valuable than synthetic examples. (`explicit`)
  - Evidence: "And then if you have already some customer or production traces, try to include those as well because nothing is better than than real-world data."
- The speaker says skill changes should not merge unless the eval improves, so regression tests gate skill updates. (`explicit`)
  - Evidence: "And we run them on every change to the skill. So, if a change happens to or like a diff to the skill file, the eval will be run, and there will also be a result, and the change will not be merged if it is not improving the test cases."
- The speaker argues that evals should be kept even after a skill is retired so the team can detect degradation and reintroduce the skill if needed. (`explicit`)
  - Evidence: "You don't need to throw that eval away because you throw the skill away. You can keep that eval to make sure that the model or the agent keeps the performance and as soon as you start seeing some degradation, you can reintroduce the skill."

### Topics Covered
- **Capability skills** — Skills that improve abilities the model cannot yet do consistently and may later become unnecessary.
- [[coding-agents|Preference skills]] — Skills that encode durable team or company preferences and workflows.
- [[agent-evaluations|Progressive disclosure]] — The layered structure of a skill: description, skill body, then deep references.
- [[agent-evaluations|Trigger evaluation]] — Small tests that check whether a skill fires in the right situations and stays quiet in the wrong ones.
- [[agent-evaluations|Ablation testing]] — Testing a skill with and without it loaded to measure whether it still adds value.
- [[agent-evaluations|Skill eval harness]] — Using prompts, regex, asserts, and judge models to score skill behavior before shipping.
- **Regression gating** — Keeping skill changes from merging unless the evaluation improves.
- [[coding-agents|No-ops]] — Short, non-behavior-changing instructions that should be removed because they add cost without value.

### Tools And Named Systems
- **Gemini Interactions API** — The API the speaker says the team needed a skill for, because the model lacked context about it.
- **Gemini CLI** — The command-line environment the speaker used to run the skill eval flow in the example.
- **SkillBench** — The benchmark the speaker cites for skill performance analysis across tasks and models.

### Novel Concepts And Methods
- **Progressive disclosure** — Progressive disclosure skill design: keep the description short, put operational guidance in the skill body, and push deep context into reference files.
- **Trigger testing** — Trigger-focused skill evaluation: build positive and negative prompts to verify when the skill should and should not activate.
- **Ablation testing** — Ablation testing: run evals with the skill enabled and disabled to measure whether the skill still adds value.
- **Regression gating** — Regression-gated skill changes: require eval improvement before merging a skill change.
- **Rule-based assertions** — Cheap automated checks: use regex and simple asserts for easy correctness checks before moving to more expensive judgments.
- **LLM judging** — LLM-as-judge rubric scoring: use a rubric when outputs are too complex for fixed rules.

### Open Questions
- **How much variance remains across different harnesses and models for the same skill, and which harness-specific behaviors should be normalized versus accepted?** — The speaker says harnesses and models behave differently, so cross-harness reliability is still an open evaluation problem.
- **What isolation strategy is sufficient to stop coding agents from leaking context or cheating through prior workspace state?** — The speaker warns that non-isolated runs can inflate scores by letting the agent exploit outside context instead of the skill.
- **What signals should decide the exact point at which a skill should be retired and later reintroduced?** — The speaker argues that model updates can make skills obsolete, but the retirement threshold is still something teams need to define.

### Derived Links And Source Material
- [[youtube-0vphxNt4wyk-transcript]] — dedicated official recording transcript.
- [[youtube-0vphxNt4wyk]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/0vphxNt4wyk--2026-06-30-philipp-schmid-don-t-ship-skills-without-evals.json`.

### Speaker Context
- [[philipp-schmid|Philipp Schmid]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[philipp-schmid]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-3_gYbhABcAE-dense-slides]] (2 viable slide images).
- Related slide/OCR pages:
- [[youtube-3_gYbhABcAE-dense-slides]]
- [[youtube-3_gYbhABcAE-reconstructed-slides]]
- [[youtube-3_gYbhABcAE-slides]]
- Slide-derived terms: `braintrust`, `workos`, `openal`, `teas`, `senior`, `engineers`, `struggle`, `tsacconss`, `mental`, `model`, `collisions`, `traditional`, `engineering`, `reatty`, `alengineer`, `colds`, `erate`, `septs`

## Official YouTube Recording
- [[youtube-0vphxNt4wyk|Don't Ship Skills Without Evals — Philipp Schmid, Google DeepMind]] — official AI Engineer YouTube recording published 2026-07-14.
- Evidence status: [[youtube-0vphxNt4wyk-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-0vphxNt4wyk]] - dedicated official event recording.
- [[youtube-0vphxNt4wyk-transcript]] - dedicated official recording transcript.
- [[youtube-3_gYbhABcAE]] - supporting context; not the exact session recording.

- Source video: `youtube-0vphxNt4wyk`
- Slide deck: [[youtube-0vphxNt4wyk-slides|Slides: 0vphxNt4wyk]] — 11 visible slide image(s).
![[assets/slides/0vphxNt4wyk/slide-001.jpg]]
![[assets/slides/0vphxNt4wyk/slide-002.jpg]]
![[assets/slides/0vphxNt4wyk/slide-003.jpg]]
- Slide-derived themes for `youtube-0vphxNt4wyk`: skills, fail, chad, vibe, checks, production, engineering, future.
- Source video: `youtube-3_gYbhABcAE`
- Slide deck: [[youtube-3_gYbhABcAE-dense-slides|Dense Slides: Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind]] — slide evidence page.
- Additional slide evidence: [[youtube-3_gYbhABcAE-slides|Slides: Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind]], [[youtube-3_gYbhABcAE-reconstructed-slides|Reconstructed Slides: Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind]]
- Slide-derived themes for `youtube-3_gYbhABcAE`: senior, engineers, engineering, text, state, trap, treating, world.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/0vphxNt4wyk.txt` (3,965 words).

## Transcript Markdown
- [[youtube-0vphxNt4wyk-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/0vphxNt4wyk.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-0vphxNt4wyk` — 3,965 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-0vphxNt4wyk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-0vphxNt4wyk`: skill, skills, model, should, look, evals, eval, always.
- Slide-derived themes for `youtube-0vphxNt4wyk`: skills, fail, chad, vibe, checks, production, engineering, future.
- Evidence links for `youtube-0vphxNt4wyk` (primary event evidence): [[youtube-0vphxNt4wyk]], [[youtube-0vphxNt4wyk-transcript]], [[youtube-0vphxNt4wyk-slides]]
- `youtube-3_gYbhABcAE` — 7 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-3_gYbhABcAE`: senior, engineers, engineering, text, state, trap, treating, world.
- Evidence links for `youtube-3_gYbhABcAE` (supporting context only): [[youtube-3_gYbhABcAE]], [[youtube-3_gYbhABcAE-slides]], [[youtube-3_gYbhABcAE-dense-slides]], [[youtube-3_gYbhABcAE-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
