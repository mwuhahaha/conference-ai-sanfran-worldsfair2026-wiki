---
title: "Computer-Use 2.0: Agents Just Got Multi-Cursor"
category: "talks"
date: "2026-06-30"
time: "2:25pm-2:45pm"
track: "Computer Use"
room: "Track 7"
speakers: ["Francesco Bonacci", "Dillon DuPont"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Computer Use"
scheduleRoom: "Track 7"
scheduleLabels: ["Computer Use", "Track 7", "session", "confirmed"]
---
# Computer-Use 2.0: Agents Just Got Multi-Cursor

## Conference Context
- Date/time: 2026-06-30 · 2:25pm-2:45pm
- Track/room: Computer Use · Track 7
- Speaker(s): Francesco Bonacci, Dillon DuPont
- Session type/status: session · confirmed

- Track: Computer Use
- Room: Track 7
- Session type: session
- Status: confirmed

## Session Description
Computer-use agents still inherit a basic desktop limitation: one machine has one foreground app, one hardware cursor, and one active actor. Once you try to run more than one agent per desktop, they start stealing focus from the user and from each other. We built cua-driver around a different model: multiple agents operating real desktop applications in parallel, each with its own synthetic pointer, while the user's cursor and keyboard stay undisturbed. The key move is to stop treating hardware mouse and keyboard events as the primary automation layer. cua-driver goes one layer lower, into the OS plumbing behind accessibility: UI Automation on Windows, AT-SPI on Linux, and AX on macOS. Those APIs address applications and elements directly, so the OS does not require the target window to be frontmost. A click can land on a background window. A keystroke can reach a hidden one. Multiple agents can act at once because none of them is competing for the singleton hardware mouse. I'll walk through the architecture, the API shape, and the platform-specific traps we hit while making it work across Windows, macOS, and Linux. The live demo is three agents operating on one desktop while the user keeps typing uninterrupted. The goal is to make Computer-Use 2.0 feel concrete: what changes in the stack, what becomes possible, and where the approach still leaks, including Wayland, Chromium DOM surfaces, native canvas apps, and fallback input paths.

## Synthesis
### Transcript-Backed Summary
The talk argues that computer-use agents become much more useful once they stop fighting the user's foreground cursor and instead operate through OS-level accessibility pathways. The core mechanism is to read window state, address elements directly through accessibility trees, and fall back to pixel-level clicks only when necessary, which enables background execution and even parallel agents on the same desktop, but also introduces platform-specific brittleness and partial coverage. The second half extends the idea into evaluation: the team builds benchmark tasks from setup, oracle, and evaluator pieces, red-teams them for reward hacking before publication, and then uses trajectory forks to probe whether a model can predict reward and internal state rather than just click correctly. The practical consequence is a tighter loop between capability and infrastructure: harder evaluations reveal how weak current models still are, while a warm sandbox pool moves startup cost off expensive GPUs so training can keep hardware busy.

### Key Takeaways
- A background-first desktop control path can act on windows without stealing focus, and it only falls back to pixel clicks when accessibility-based execution fails.
  - Evidence: "So you really um have um to observe the space in this case just by calling like get window state you get a an accessibility tree representation plus a screenshot and then you will go and uh um try a background execution using accessibility tree and if that doesn't work we go all the way and uh make the heavy lifting for you and just try a pixel background click."
- The Kua bench SDK is meant to make cross-platform GUI task authoring practical by collapsing desktop differences into a single Python file.
  - Evidence: "So using the Kubaben SDK you can write a guey that works across every desktop platform in a single Python file and use the same SDK to probe that GUI to get usable agent data."
- Switching from the built-in computer tool to Kua driver improved pass rate from 62% to 80% while using 34% fewer tokens.
  - Evidence: "If we take a look at the Kua bench basic data set scaled up to 4K resolution uh testing an agent they typically get around 62% pass rate but when you switch the agent computer tool from the built-in one to KU driver the pass rate jumps from 62% to 80% using 34% less tokens"
- Benchmark quality depends on adversarially trying to break tasks before admitting them to the dataset.
  - Evidence: "We have a matrix of agents attempt to do reward hacking and attempting to break the environment and we take all that data and we compile it into a nice code rabbit style code review and only tasks that survive our pipeline can enter the data set."
- A warm pool can shift sandbox startup overhead off GPUs, which improves utilization and lowers the effective cost of RL training.
  - Evidence: "Um so yeah so now when you have like this like uh redundancy in your pool you're paying the cost of that startup time on the infrastructure side not on the GPU side so your GPU workers have full utilization um yeah and then because we use this we can give you instant sandboxes for"

### Claims From The Talk
- The speaker says the background version of the driver keeps computer use agents from taking over the user's screen. (`explicit`)
  - Evidence: "That means that your computer user will will not take over your uh screen as like the computer use 1.0 um kind of like agent loop was doing back in the days."
- The speaker reports that the system works across Mac OS, Windows, and Linux. (`explicit`)
  - Evidence: "Um we made it working not only for Mac OS but also spanning like across Windows and Linux."
- The benchmark tasks are built from three parts: setup, oracle, and evaluator. (`explicit`)
  - Evidence: "The oracle function which provides a golden trajectory for the task and the evaluator which probes the environment to check if the agent successfully completed the task."
- The electrical engineering benchmark produced a weak result, with the top agent fully passing only six of twenty-five tasks. (`explicit`)
  - Evidence: "But the results are humbling. The top agent that we tested only got a full pass on six out of 25 of these tasks."
- The speaker reports that tasks starting from a blank schematic dropped to 0% success. (`explicit`)
  - Evidence: "Of those six, 100% of them involved editing an existing schematic. And when we start the task from a blank schematic, the success rate drops to 0%."
- Across the tested models, the leaderboard stayed flat and no model exceeded 30% reward. (`explicit`)
  - Evidence: "And across all the models that we tested, the leaderboard is flat. No model has achieved more than 30% reward."
- The infrastructure design shifts sandbox startup cost away from GPUs by using redundancy so GPU workers stay fully utilized. (`explicit`)
  - Evidence: "Um so yeah so now when you have like this like uh redundancy in your pool you're paying the cost of that startup time on the infrastructure side not on the GPU side so your GPU workers have full utilization um yeah and then because we use this we can give you instant sandboxes for"

### Topics Covered
- [[agent-reliability-and-durable-execution|Background computer use]] — Operating desktop agents without foreground takeover by running them in the background.
- [[agentic-web|Accessibility-driven control]] — Directly addressing desktop UI elements through accessibility trees instead of hardware mouse and keyboard events.
- **GUI benchmark design** — Representing GUI benchmarks as setup, oracle, and evaluator components.
- [[agent-evaluations|Electrical engineering evaluation]] — Testing computer-use agents on electrical engineering software tasks with real evaluator functions.
- [[agent-evaluations|World-model measurement]] — Using recorded trajectories to probe whether a model can predict reward or internal state.
- [[ai-sandboxes|GPU sandbox pooling]] — Keeping GPU workers busy by allocating sandboxes from a demand-sized warm pool.

### Tools And Named Systems
- **quad driver** — The open-source driver used to keep computer-use agents running in the background across desktop platforms.
- **Kua bench SDK** — The SDK for authoring and probing cross-platform GUI tasks in one Python file.
- **KUBench Kyad** — The electrical-engineering benchmark dataset used to test computer-use agents on professional software tasks.
- **Snorkel AI** — The collaborator used to build the electrical-engineering benchmark dataset.

### Novel Concepts And Methods
- **Background accessibility execution** — Run desktop agents through background execution paths instead of foreground hardware input.
- **Task triad evaluation** — Define GUI benchmarks with separate setup, oracle, and evaluator functions.
- **Reward-hacking red team** — Try to break the environment before admitting a task into the dataset.
- **Trajectory fork probing** — Measure an agent by forking any recorded run at an arbitrary moment and probing predictions against the saved state.
- **Warm-pool autoscaling** — Use a demand-based warm pool so sandbox startup happens on cheaper infrastructure rather than on GPUs.

### Open Questions
- **How can the background-control path be made consistently reliable when Mac OS, Windows, and Linux behave differently?** — The talk says the platforms do not behave the same way, so reliability across desktops is still an open engineering problem.
- **What probing targets best capture an agent's world model beyond reward prediction alone?** — The speaker treats world-model measurement as the next step after action success, but the exact best signals remain open.
- **Where is the boundary on Android between background GUI control and simpler background tool use?** — The Android discussion suggests the platform may support only partial background control, so the practical limit matters.

### Derived Links And Source Material
- [[youtube-ZSQb5fzRFPw-transcript]] — dedicated official recording transcript.
- [[youtube-ZSQb5fzRFPw]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/ZSQb5fzRFPw--2026-06-30-francesco-bonacci-computer-use-2-0-agents-just-got-multi-cursor.json`.

### Speaker Context
- [[francesco-bonacci|Francesco Bonacci]]
- [[dillon-dupont|Dillon DuPont]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[francesco-bonacci]]
- [[dillon-dupont]]

## Official YouTube Recording
- [[youtube-ZSQb5fzRFPw|Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua]] — official AI Engineer YouTube recording published 2026-07-15.
- Evidence status: [[youtube-ZSQb5fzRFPw-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-ZSQb5fzRFPw]] - dedicated official event recording.
- [[youtube-ZSQb5fzRFPw-transcript]] - dedicated official recording transcript.

- Source video: `youtube-ZSQb5fzRFPw`
- Slide deck: [[youtube-ZSQb5fzRFPw-slides|Slides: ZSQb5fzRFPw]] — 17 visible slide image(s).
![[assets/slides/ZSQb5fzRFPw/slide-001.jpg]]
![[assets/slides/ZSQb5fzRFPw/slide-002.jpg]]
![[assets/slides/ZSQb5fzRFPw/slide-003.jpg]]
- Slide-derived themes for `youtube-ZSQb5fzRFPw`: track, july, fair, computer, operator, loop, wired, model.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/ZSQb5fzRFPw.txt` (2,617 words).

## Transcript Markdown
- [[youtube-ZSQb5fzRFPw-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/ZSQb5fzRFPw.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-ZSQb5fzRFPw` — 2,617 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-ZSQb5fzRFPw`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-ZSQb5fzRFPw`: computer, take, over, driver, background, task, might, sandbox.
- Slide-derived themes for `youtube-ZSQb5fzRFPw`: track, july, fair, computer, operator, loop, wired, model.
- Evidence links for `youtube-ZSQb5fzRFPw` (primary event evidence): [[youtube-ZSQb5fzRFPw]], [[youtube-ZSQb5fzRFPw-transcript]], [[youtube-ZSQb5fzRFPw-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
