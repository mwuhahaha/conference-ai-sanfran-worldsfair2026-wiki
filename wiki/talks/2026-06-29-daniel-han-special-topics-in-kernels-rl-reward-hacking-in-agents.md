---
title: "Special topics in Kernels, RL, Reward Hacking in Agents"
category: "talks"
date: "2026-06-29"
time: "2:20pm-5:30pm"
track: "Workshops Day 1"
room: "Track 3"
speakers: ["Daniel Han"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Workshops Day 1"
scheduleRoom: "Track 3"
scheduleLabels: ["Workshops Day 1", "Track 3", "session", "confirmed"]
---
# Special topics in Kernels, RL, Reward Hacking in Agents

## Conference Context
- Date/time: 2026-06-29 · 2:20pm-5:30pm
- Track/room: Workshops Day 1 · Track 3
- Speaker(s): Daniel Han
- Session type/status: session · confirmed

- Track: Workshops Day 1
- Room: Track 3
- Session type: session
- Status: confirmed

## Session Description
An advanced seminar (good prerequisites: Daniel's 2024 and 2025 hit AIE workshops, but all are welcome!) PLS WATCH: https://www.youtube.com/@aiDotEngineer/search?query=daniel%20han

## Synthesis
### Transcript-Backed Summary
Han's central thesis is that AI progress has not stopped; it has shifted from raw scaling to reasoning, software improvements, and stricter evaluation discipline. He argues that the recent acceleration comes from methods like reasoning training, quantization, compiler optimizations, checkpointing, and better harnesses, while the main risk is that benchmarks and inference stacks can make models look better or worse than they really are. The talk repeatedly emphasizes tradeoffs: better scores can come from cheating, contaminated tests, wrong prompts, or harness changes, and the most reliable gains often require more engineering work around the model rather than simply making the model larger. The practical takeaway is to verify models in controlled environments, distrust easy-to-game benchmarks, and focus on stack-level fixes before assuming a frontier model is truly better.

### Key Takeaways
- Treat benchmark results as system tests, because prompts, harnesses, providers, and implementation details can swing measured accuracy as much as the model itself.
  - Evidence: "It's not the model anymore. Um and so like you know as we have seen if they have accidentally botched you know if they accidentally botched the harness you will get reduced accuracy."
- For local open-source deployment, he recommends downloading from Hugging Face and using stable runtimes like Llama CPP or Llama server.
  - Evidence: "I think Llama CPP and Llama server is probably the most bugfree system. So I would like suggest yes you should download from hugging face."
- Before writing custom kernels, try torch.compile first, since the talk shows it can outperform handwritten kernels on modern PyTorch.
  - Evidence: "Um so the main point is you should always firstly look at torch compile right before you write a kernel use torch compile first do not start learning how to do triton or you know cuda or whatever is your favorite coding language for kernels don't do that instead use torch compile um even worse"
- If you want trustworthy RL signals, use process supervision or anti-hacking filters, because outcome-only rewards can be gamed.
  - Evidence: "Um and process supervision what you do is you manually check every single line not you don't just assign plus 10 to the final you know the answer is correct right the answer is correct plus 10 assign every single line as plus 10 you don't do this instead what you do is you assign"
- Benchmarks should be designed to be hard to benchmax and easy to verify, such as random math tasks or constrained generation tasks.
  - Evidence: "The first condition is the benchmark must not must not be benchmaxable. Right? How do you make a benchmark that is extremely hard to benchmark, right?"

### Claims From The Talk
- Reasoning is the speaker's explanation for why AI progress moved past an apparent plateau, and he argues the effective capability doubling time fell to about 3.5 months. (`explicit`)
  - Evidence: "you know the green line is the new scaling law um and you can see previously the black line the doubling time was actually around seven months so every single seven months the capabilities of the models double um but now it has shrunk to 3.5 months."
- Open source models still lag closed source models, but the gap has narrowed to around four months and could continue shrinking if the trend holds. (`explicit`)
  - Evidence: "It's around four months now. Um so open source labs lag behind closed source labs by around four months."
- He reports that Claude Code's apparent accuracy drop was traced to harness problems, including a deleted thinking trace and a bad system prompt. (`explicit`)
  - Evidence: "know like these things do happen over time um and so like for this specific example you know cloud code the harness the harness itself was the problem not the actual model right the harness the thinking trace got deleted and they had a very not a very good system prompt."
- Software and algorithmic changes, not just hardware scaling, are the main path forward because precision tricks, checkpointing, and related stack improvements deliver large gains. (`explicit`)
  - Evidence: "So using diffusion LLMs to do faster inference and again this is a software change. And my main point is is that in general, hardware innovations are getting less and less important."
- Reward hacking is already happening in training runs, so models need process supervision or anti-hacking checks instead of only outcome-level rewards. (`explicit`)
  - Evidence: "It's not going to happen in real world. Um, well, GLM 5.2 during its training methodology, they specifically mentioned they have this new methodology for reinforcement learning called anti-hacking."

### Topics Covered
- [[inference-engineering|Reasoning Scaling]] — The idea that reasoning training and new scaling laws extended model progress after an apparent plateau.
- [[agent-evaluations|Benchmark Integrity]] — Designing benchmarks that resist gaming while remaining easy to check.
- [[agent-evaluations|Harness Fidelity]] — How prompts, harnesses, and providers affect measured model quality.
- **Software-First Optimization** — The shift from hardware-first to software-first AI performance gains.
- [[inference-engineering|Reward Hacking]] — How models exploit reward functions and how to detect or prevent that behavior.

### Tools And Named Systems
- **torch.compile** — The compiler path the speaker recommends as the first optimization attempt before custom kernel work.
- **Hugging Face** — The model hub he recommends for downloading open-source models.
- **Llama CPP** — The local runtime he recommends for serving open-source models.
- [[openrouter|OpenRouter]] — The inference platform he references when discussing benchmarked provider accuracy.
- **DeepSeek R1** — The open-source reasoning model family he cites as part of the open-source catch-up story.

### Novel Concepts And Methods
- **Dynamic Quantization** — Dynamic quantization that leaves some layers at higher precision while compressing others to preserve accuracy.
- **Process Supervision** — Process supervision that assigns rewards to intermediate reasoning steps instead of only the final answer.
- **Bisection Search** — Binary search over compiler or kernel flags to cut the search space for performance tuning.
- **Rolling Average Analysis** — Rolling-average trend analysis for noisy benchmark time series instead of reading daily points directly.

### Open Questions
- **Will the reasoning-driven scaling line continue, or will it taper into another plateau?** — This determines whether the current acceleration is durable or just another temporary phase.
- **How can we build benchmarks that are both hard to game and easy to verify?** — The talk argues that most current benchmarks fail on one or both of those requirements.
- **What benchmark or definition should determine frontier intelligence for regulation?** — The answer affects licensing, release controls, and how governments classify models.
- **How can reinforcement learning avoid reward hacking at scale without relying on expensive manual process supervision?** — This is the core obstacle to making RL reliable in real training systems.

### Derived Links And Source Material
- [[youtube-uIiA6DquRiE-transcript]] — dedicated official recording transcript.
- [[youtube-uIiA6DquRiE]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/uIiA6DquRiE--2026-06-29-daniel-han-special-topics-in-kernels-rl-reward-hacking-in-agents.json`.

### Speaker Context
- [[daniel-han|Daniel Han]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[daniel-han]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-OkEGJ5G3foU-dense-slides]] (1 viable slide images).
- Related slide/OCR pages:
- [[youtube-OkEGJ5G3foU-dense-slides]]
- [[youtube-OkEGJ5G3foU-reconstructed-slides]]
- [[youtube-OkEGJ5G3foU-slides]]
- Slide-derived terms: `microsoft`, `contributions`, `fixes`, `awss`, `graphite`, `windsurf`, `mongobr`, `mdaily`, `augment`, `code`, `workos`, `unsloth`, `daniel`, `deep-dive`, `kernels`, `quantization`, `aaeoat`, `naan`

## Official YouTube Recording
- [[youtube-uIiA6DquRiE|Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth]] — official AI Engineer YouTube recording published 2026-07-17.
- Evidence status: [[youtube-uIiA6DquRiE-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-uIiA6DquRiE]] - dedicated official event recording.
- [[youtube-uIiA6DquRiE-transcript]] - dedicated official recording transcript.
- [[youtube-OkEGJ5G3foU]] - supporting context; not the exact session recording.

- Source video: `youtube-uIiA6DquRiE`
- Slide deck: [[youtube-uIiA6DquRiE-slides|Slides: Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth]] — 11 visible slide image(s).
![[assets/slides/uIiA6DquRiE/slide-001.jpg]]
![[assets/slides/uIiA6DquRiE/slide-002.jpg]]
![[assets/slides/uIiA6DquRiE/slide-003.jpg]]
- Slide-derived themes for `youtube-uIiA6DquRiE`: smaller, model, high, extra, license, businesses, users, open.
- Source video: `youtube-OkEGJ5G3foU`
- Slide deck: [[youtube-OkEGJ5G3foU-dense-slides|Dense Slides: [Full Workshop] Reinforcement Learning, Kernels, Reasoning, Quantization & Agents — Daniel Han]] — slide evidence page.
- Additional slide evidence: [[youtube-OkEGJ5G3foU-slides|Slides: [Full Workshop] Reinforcement Learning, Kernels, Reasoning, Quantization & Agents — Daniel Han]], [[youtube-OkEGJ5G3foU-reconstructed-slides|Reconstructed Slides: [Full Workshop] Reinforcement Learning, Kernels, Reasoning, Quantization & Agents — Daniel Han]]
- Slide-derived themes for `youtube-OkEGJ5G3foU`: fixes, chat, template, multiple, llama, research, google, github.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/uIiA6DquRiE.txt` (25,283 words).

## Transcript Markdown
- [[youtube-uIiA6DquRiE-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/uIiA6DquRiE.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-uIiA6DquRiE` — 25,283 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-uIiA6DquRiE`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-uIiA6DquRiE`: model, models, source, open, benchmark, question, okay, accuracy.
- Slide-derived themes for `youtube-uIiA6DquRiE`: smaller, model, high, extra, license, businesses, users, open.
- Evidence links for `youtube-uIiA6DquRiE` (primary event evidence): [[youtube-uIiA6DquRiE]], [[youtube-uIiA6DquRiE-transcript]], [[youtube-uIiA6DquRiE-slides]]
- `youtube-OkEGJ5G3foU` — 3 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-OkEGJ5G3foU`: fixes, chat, template, multiple, llama, research, google, github.
- Evidence links for `youtube-OkEGJ5G3foU` (supporting context only): [[youtube-OkEGJ5G3foU]], [[youtube-OkEGJ5G3foU-slides]], [[youtube-OkEGJ5G3foU-dense-slides]], [[youtube-OkEGJ5G3foU-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
