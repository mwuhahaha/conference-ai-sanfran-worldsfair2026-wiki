---
title: "HTML Is All Agents Need"
category: "talks"
date: "2026-07-01"
time: "11:10am-11:30am"
track: "Generative Media"
room: "Track 1"
speakers: ["James Russo"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Generative Media"
scheduleRoom: "Track 1"
scheduleLabels: ["Generative Media", "Track 1", "session", "confirmed"]
---
# HTML Is All Agents Need

## Conference Context
- Date/time: 2026-07-01 · 11:10am-11:30am
- Track/room: Generative Media · Track 1
- Speaker(s): James Russo
- Session type/status: session · confirmed

- Track: Generative Media
- Room: Track 1
- Session type: session
- Status: confirmed

## Session Description
LLMs are great at writing code. So the question we kept asking was: can they write code that produces a video? We thought it would be easy. The reality was a year of trying. We started with massive prompts to get very mediocre output. We made it more agentic to iterate and improve its output. This worked okay but wasn't production-ready. Eventually we tried Remotion. It got us deterministic video, but the React framework kept boxing the agent in. The more guardrails we added, the safer and more boring the outputs got. When we utilized plain HTML, CSS, and JavaScript, the creativity came back to the output. So we set out to build a video rendering framework on top of HTML. But it needed to work with Gemini Flash. Why? Because one tell that a framework is fighting an agent is needing the biggest model just to get usable output. So from there we shaped the framework around what small models could reliably author. That left one real engineering question: can we keep the freedom of HTML and still render a deterministic MP4? Browsers don't want to do that. Image decoders, font loaders, and animation clocks all run async on their own schedule. Great for performance. Terrible for "render the same pixels every time." Throughout, we iterated constantly with agentic loops and self-improving evals to test out the framework, find issues in our renderer, and shape a set of skills that gave the agents Taste instead of guardrails. This talk is what it took to get there.

## Synthesis
### Transcript-Backed Summary
Russo's thesis is that HTML, CSS, and JavaScript are the right interface for agentic video generation because they match what models already know, while custom DSLs and heavier framework layers tend to suppress creativity. The operational method behind Hyperframes is to let agents author browser-native compositions and then turn them into deterministic video by freezing the browser clock, stepping frame by frame, waiting for assets to settle, and capturing screenshots for MP4 encoding. The central tradeoff is freedom versus control: the more guardrails they added, the safer and more boring the output became, so the team minimized the wrapper, added skills and eval loops to shape taste, and kept humans in the loop for last-mile editing. The practical consequence is a video framework that can turn ordinary web content into video at scale, but the speaker says the creative ceiling still depends on better models and better code-to-video benchmarks.

### Key Takeaways
- Keep the authoring surface close to HTML so agents can produce video without learning a new language.
  - Evidence: "Our bet is on HTML. HTML, CSS, and JavaScript are the native languages of LLMs. Most of their training data, every webpage that gets scraped at the end of day is essentially just HTML, CSS, and JavaScript under the hood."
- Start from the thinnest workable wrapper and prove it with smaller models before scaling up.
  - Evidence: "Um but to our surprise, the thinnest wrapper ultimately won, which is essentially just HTML at the end of the day with a few data attributes as metadata to let the agent know, and to let us know uh about timing and things like that."
- Deterministic video generation from browsers requires controlling time and rendering one frame at a time.
  - Evidence: "We freeze the clock in the browser and then we seek deterministically to every single moment in time or every single frame, uh wait for everything to load on the page, ensure that it's loaded and ready to go, and then we take a screenshot and move on to the next frame, and do that over and over again uh until we get all of the necessary frames to encode that into a video."
- Use skills and evals to shape taste and video quality instead of adding more guardrails.
  - Evidence: "Um this allows us to focus on the important parts of what makes a great video and a big part of this is constantly evaling and using agents to improve them."
- Keep humans in the loop for storyboard, motion, and last-mile editing when production quality matters.
  - Evidence: "Ensuring that humans are always in the loop and have access to do anything that they would do in their normal video editor within the open-source framework's editor so that you can manually drag, tweak, uh etc."

### Claims From The Talk
- The speaker argues that HTML, CSS, and JavaScript are the native interface agents should use for video generation because they match the web data models are already trained on. (`explicit`)
  - Evidence: "Our bet is on HTML. HTML, CSS, and JavaScript are the native languages of LLMs. Most of their training data, every webpage that gets scraped at the end of day is essentially just HTML, CSS, and JavaScript under the hood."
- HeyGen found that heavier wrappers, prompts, and framework-specific abstractions reduced creativity, while a thinner HTML-based wrapper performed better. (`explicit`)
  - Evidence: "Um but to our surprise, the thinnest wrapper ultimately won, which is essentially just HTML at the end of the day with a few data attributes as metadata to let the agent know, and to let us know uh about timing and things like that."
- Hyperframes renders video by freezing the browser clock, advancing frame by frame, waiting for the page to settle, and capturing deterministic screenshots for MP4 encoding. (`explicit`)
  - Evidence: "We freeze the clock in the browser and then we seek deterministically to every single moment in time or every single frame, uh wait for everything to load on the page, ensure that it's loaded and ready to go, and then we take a screenshot and move on to the next frame, and do that over and over again uh until we get all of the necessary frames to encode that into a video."
- The team uses skills and repeated evaluation loops to push output toward taste and video craft rather than framework syntax. (`explicit`)
  - Evidence: "And a big part of this is the skills that we couple with our framework. Our skill is focused on taste and video aspects because the LLMs and agents already know how to write HTML and CSS and JavaScript, we don't have to teach them the language, we just teach them how to create good videos."
- Russo says current models are still weak at creative work, which is why the team is building a code-to-video benchmark with labs and creators. (`explicit`)
  - Evidence: "But we think there's something at a higher level that needs to change here, which is why we started to work on a code to video benchmark where we are trying to work with the LLM labs, any creators who are working on video agents to ensure that we can raise the floor of videos for everyone."

### Topics Covered
- [[agentic-web|Agent-native video authoring]] — Using HTML, CSS, and JavaScript as the interface for agent-generated video.
- **Deterministic browser rendering** — Producing repeatable video output from browser rendering.
- **Creativity versus guardrails** — The tension between creative freedom and framework guardrails.
- [[agent-evaluations|Taste-focused skill design]] — Using skills and evaluation loops to shape model output quality.
- **Code-to-video benchmarking** — Measuring and improving code-to-video systems with benchmarks.

### Tools And Named Systems
- **Hyperframes** — The open-source framework that turns agent-authored HTML into video.
- **Gemini 3 Flash** — The small model used as the design partner for the framework.
- **Remotion** — A coding-based video framework the team tested before settling on HTML.
- **After Effects** — A creative production tool used as a quality benchmark for video workflows.
- **Premiere Pro** — A creative production tool used as a quality benchmark for video workflows.

### Novel Concepts And Methods
- **Thin HTML wrapper** — Use a thin HTML wrapper with a small amount of metadata instead of a heavy framework layer.
- **Freeze-clock frame rendering** — Render browser content deterministically by freezing time and capturing one frame at a time.
- **Taste-focused skills** — Shape outputs with skills that teach taste and video craft instead of framework syntax.
- **Iterative eval loops** — Improve outputs through repeated agent-based evaluation cycles.
- **Storyboard-first assembly** — Build a video by storyboarding first, then adding motion and finishing with human editing.

### Open Questions
- **How can the freedom of HTML be preserved while still rendering deterministic MP4 output?** — This is the core engineering problem behind making browser-native authoring reliable for production video.
- **What benchmark and evaluation design would raise creative video quality enough that smaller models can author strong output reliably?** — The talk treats model creativity as the remaining bottleneck, so this determines whether the approach scales beyond a single team.

### Derived Links And Source Material
- [[youtube-Cz4v1WHVyZc-transcript]] — dedicated official recording transcript.
- [[youtube-Cz4v1WHVyZc]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/Cz4v1WHVyZc--2026-07-01-james-russo-html-is-all-agents-need.json`.

### Speaker Context
- [[james-russo|James Russo]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[james-russo]]

## Official YouTube Recording
- [[youtube-Cz4v1WHVyZc|HTML Is All Agents Need — James Russo, HeyGen]] — official AI Engineer YouTube recording published 2026-07-21.
- Evidence status: [[youtube-Cz4v1WHVyZc-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-Cz4v1WHVyZc]] - dedicated official event recording.
- [[youtube-Cz4v1WHVyZc-transcript]] - dedicated official recording transcript.

- Source video: `youtube-Cz4v1WHVyZc`
- Slide deck: [[youtube-Cz4v1WHVyZc-slides|Slides: HTML Is All Agents Need — James Russo, HeyGen]] — 32 visible slide image(s).
![[assets/slides/Cz4v1WHVyZc/slide-001.jpg]]
![[assets/slides/Cz4v1WHVyZc/slide-002.jpg]]
![[assets/slides/Cz4v1WHVyZc/slide-003.jpg]]
- Slide-derived themes for `youtube-Cz4v1WHVyZc`: track, july, most, engineering, future, html, javascript, native.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/Cz4v1WHVyZc.txt` (2,535 words).

## Transcript Markdown
- [[youtube-Cz4v1WHVyZc-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/Cz4v1WHVyZc.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-Cz4v1WHVyZc` — 2,535 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Cz4v1WHVyZc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Cz4v1WHVyZc`: html, great, hyperframes, output, create, frame, coding, javascript.
- Slide-derived themes for `youtube-Cz4v1WHVyZc`: track, july, most, engineering, future, html, javascript, native.
- Evidence links for `youtube-Cz4v1WHVyZc` (primary event evidence): [[youtube-Cz4v1WHVyZc]], [[youtube-Cz4v1WHVyZc-transcript]], [[youtube-Cz4v1WHVyZc-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
