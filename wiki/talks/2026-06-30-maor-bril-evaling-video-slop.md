---
title: "Evaling Video Slop"
category: "talks"
date: "2026-06-30"
time: "1:55pm-2:15pm"
track: "Evals"
room: "Track 5"
speakers: ["Maor Bril"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Evals"
scheduleRoom: "Track 5"
scheduleLabels: ["Evals", "Track 5", "sponsor", "confirmed"]
---
# Evaling Video Slop

## Conference Context
- Date/time: 2026-06-30 · 1:55pm-2:15pm
- Track/room: Evals · Track 5
- Speaker(s): Maor Bril
- Session type/status: sponsor · confirmed

- Track: Evals
- Room: Track 5
- Session type: sponsor
- Status: confirmed

## Session Description
Everyone is shipping video models. Almost no one is evaling them honestly. CLIP score doesn't catch temporal incoherence. Vibes-based human review doesn't scale. And every "AI judge" you wire up will quietly drift away from human preference unless you measure the drift. This is a tactical talk on building real multimodal eval, using JudgeJudy (open-sourced at Character.ai) as the working example. You'll leave with: Why video is different from text. Temporal consistency, shot continuity, narrative coherence, and the metrics that actually capture each (clip_temporal, temporal_consistency, and friends). AI judges, the real version. Custom rubrics, when they work, when they hallucinate, when they collapse to a single dimension and pretend they didn't. The calibration loop. Pearson/Spearman correlation against human scores, automated rubric improvement, detecting systematic judge bias before it costs you a release. Pairwise preference models for video. Training a Qwen3-VL backbone with Bradley-Terry loss to score "is this slop?" before it ships. Regression gates in CI. How every AgentX release at Character.ai passes through an eval wall before it reaches users. Closing the loop with JudgeJudy. Correlating eval scores against real telemetry (Amplitude, Statsig) and feeding validated gates back into the runtime. If you're shipping any multimodal output and your eval strategy is still "the team watches some clips on Friday," this is the upgrade. github.com/character-ai/judgejudy

## Synthesis
### Transcript-Backed Summary
Maor Bril argues that video generation has improved much faster than video evaluation, so the real bottleneck is deciding whether a clip is coherent rather than producing one. His approach combines frame-level signals, a fast vision-language judge, and human calibration into a repeatable benchmark, then moves that evaluation as close to generation as possible so drift, physics mistakes, and audio mismatches are caught earlier and cheaper. A major design choice is to prefer pairwise comparisons and carefully constructed training data over absolute scoring, because the first judge version learned visual gloss and AI-versus-real artifacts instead of true quality. The practical consequence is a production-friendly eval wall that can explain why a clip is bad, not just whether it is bad.

### Key Takeaways
- Treat video as a storytelling problem, not just a frame-by-frame similarity problem.
  - Evidence: "If you think about what is video, video is a storytelling medium. Video is just another form on how we tell a story, right?"
- Catch failures as early in the generation process as possible, because fixing drift before composition is much cheaper.
  - Evidence: "So, if you can correct catch the drift at this point and correct it, then then it's much cheaper to generate the video as a whole because we we can correct it at a much cheaper cost."
- Prefer pairwise comparisons over absolute ratings when the target is subjective quality.
  - Evidence: "Right? But if I show you two videos and I'll ask you which one of them is telling a better story, the grand majority will probably agree that B is telling a better story than A, right?"
- Keep human review in the loop so automated judges stay calibrated over time.
  - Evidence: "Fair. Um so, how would you construct and align sort of like any human judges? Yeah. So, So, So, So, this is actually solved at first at the the the Judge Judy part, where every report it will generate a human can go and annotate it."

### Claims From The Talk
- The speaker argues that video generation has improved much faster than video evaluation, leaving quality judgment behind the state of the models. (`explicit`)
  - Evidence: "We still remember Sora. But but but the part that got left behind is how we evaluate the quality of the video that was generated, right?"
- He says frame-level metrics and generic LLM judges can inspect individual frames or prompt match, but they do not reliably tell whether the video tells the intended story. (`explicit`)
  - Evidence: "We're using things like clip score, which is is great to to to judge a single frame. Things like LP IPS will help us kind of detect the drift between frames, but we don't have I mean but the problem is when you kind of combine all these together, all these tools are good at watching the individual frames."
- He reports that the team built a repeatable benchmark that combines metrics, an LLM judge, and human annotation to calibrate judge behavior. (`explicit`)
  - Evidence: "Where we also use human annotation to to calibrate the the LLM as a judge. So, for every report that we generate with that harness, we're able to have humans annotate it and basically feed that feedback back in into the the the LLM as a judge prompt to make sure that it's it's aligned with what I think or what the annotator thought is good."
- He says the first judge version failed because it learned video gloss and AI-versus-real artifacts instead of true video quality. (`explicit`)
  - Evidence: "It It um it scored the vibe as opposed to the the the axes. So, it it learned how to how to detect um cohe- coherent videos and it learned how to detect the the the the the the artificial artifacts."
- He reports that the team chose a smaller vision-language model over a larger one because the larger model was slower and the extra quality did not justify the latency. (`explicit`)
  - Evidence: "Now, the we we also tested a bigger model and the results were better, but it was significantly slower."
- He argues that pairwise comparisons are more reliable than absolute 1-to-10 scoring for subjective video quality judgments. (`explicit`)
  - Evidence: "Right? But if I show you two videos and I'll ask you which one of them is telling a better story, the grand majority will probably agree that B is telling a better story than A, right?"
- He says the system moved from a complex pipeline to an agentic workflow so the generator can validate and repair its own outputs. (`explicit`)
  - Evidence: "To an agentic workflow. The reason behind this is, a, the pipelines work great if you have a very very unique use case."

### Topics Covered
- [[agent-evaluations|Video evaluation]] — The gap between better video generation and weaker evaluation methods.
- [[agent-evaluations|Story coherence]] — The idea that a video must preserve an intended narrative, not only visual resemblance.
- [[observed-work-and-traceability|Temporal consistency]] — Whether content stays consistent across frames and shots over time.
- [[context-engineering-and-knowledge-architecture|Audio-video synchronization]] — Aligning audio events with the matching visual moment.
- [[agent-evaluations|Pairwise preference modeling]] — Modeling quality as relative preference between two clips rather than an absolute score.
- [[agent-evaluations|Judge calibration]] — Using periodic human review to keep an automated judge aligned with human taste.
- [[autoresearch|Agentic workflow]] — Letting a generation system check and fix its own outputs through tools.

### Tools And Named Systems
- **JudgeJudy** — The open-sourced evaluation harness used as the working example for the talk.
- **Atmos** — The audio analysis component used to check whether sound quality is understandable.

### Novel Concepts And Methods
- **Repeatable benchmark** — Build a repeatable multimodal benchmark that can be rerun over time.
- **Human-calibrated judge** — Use human annotations to calibrate an automated judge.
- **Pairwise preference training** — Train on pairwise preferences instead of absolute scores.
- **Fast VLM scoring** — Use a fast vision-language model to score video quality quickly enough for production use.
- **Matched real-versus-AI pairs** — Construct training data by pairing real footage with AI footage while keeping encoding and annotation consistent.
- **In-loop evaluation** — Move evaluation into the generation loop so failures are caught earlier and corrected more cheaply.

### Open Questions
- **How should lip syncing be evaluated when mouth motion does not reliably correspond to speech or animation timing?** — The talk treats lip syncing as still unsolved, so it remains a key missing piece of the evaluation stack.

### Derived Links And Source Material
- [[youtube-b_PmGocP4rc-transcript]] — dedicated official recording transcript.
- [[youtube-b_PmGocP4rc]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/b_PmGocP4rc--2026-06-30-maor-bril-evaling-video-slop.json`.

### Speaker Context
- [[maor-bril|Maor Bril]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[maor-bril]]

## Official YouTube Recording
- [[youtube-b_PmGocP4rc|Evaling Video Slop — Maor Bril, Character.ai]] — official AI Engineer YouTube recording published 2026-07-25.
- Evidence status: [[youtube-b_PmGocP4rc-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-b_PmGocP4rc]] - dedicated official event recording.
- [[youtube-b_PmGocP4rc-transcript]] - dedicated official recording transcript.

- Source video: `youtube-b_PmGocP4rc`
- Slide deck: [[youtube-b_PmGocP4rc-slides|Slides: Evaling Video Slop — Maor Bril, Character.ai]] — 16 visible slide image(s).
![[assets/slides/b_PmGocP4rc/slide-001.jpg]]
![[assets/slides/b_PmGocP4rc/slide-002.jpg]]
![[assets/slides/b_PmGocP4rc/slide-003.jpg]]
- Slide-derived themes for `youtube-b_PmGocP4rc`: track, july, generating, judge, judy, amazing, engineering, future.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/b_PmGocP4rc.txt` (3,746 words).

## Transcript Markdown
- [[youtube-b_PmGocP4rc-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/b_PmGocP4rc.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-b_PmGocP4rc` — 3,746 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-b_PmGocP4rc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-b_PmGocP4rc`: model, does, sound, story, question, problem, look, better.
- Slide-derived themes for `youtube-b_PmGocP4rc`: track, july, generating, judge, judy, amazing, engineering, future.
- Evidence links for `youtube-b_PmGocP4rc` (primary event evidence): [[youtube-b_PmGocP4rc]], [[youtube-b_PmGocP4rc-transcript]], [[youtube-b_PmGocP4rc-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
