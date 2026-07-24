---
title: "The Z/L Continuum: Should AI Engineers Still Read Code?"
category: "talks"
date: "2026-06-30"
time: "10:45am-11:05am"
track: "AI Architects: Tokenmaxxing"
room: "Leadership 2"
speakers: ["Alex Volkov"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "AI Architects: Tokenmaxxing"
scheduleRoom: "Leadership 2"
scheduleLabels: ["AI Architects: Tokenmaxxing", "Leadership 2", "session", "confirmed"]
---
# The Z/L Continuum: Should AI Engineers Still Read Code?

## Conference Context
- Date/time: 2026-06-30 · 10:45am-11:05am
- Track/room: AI Architects: Tokenmaxxing · Leadership 2
- Speaker(s): Alex Volkov
- Session type/status: session · confirmed

- Track: AI Architects: Tokenmaxxing
- Room: Leadership 2
- Session type: session
- Status: confirmed

## Session Description
At AI Engineer Europe, two of the best speakers gave directly opposite advice. Zechner: slow the f*** down, read every line your model writes. Lopopolo: code is a liability, you don't even open the IDE anymore. Both got applause. The room walked out confused. On the train back I sketched the Z/L Continuum on a napkin — a five-stop spectrum from "read the clanker code" to "what IDE?" — and the whole week clicked into place. In this talk I'll walk through the Continuum, introduce FOMAT (Fear of Missing Agent Time — coined backstage by Michael Richman), and make four arguments: the Continuum is real, your stop is per-task not per-person, model capability bends everything toward L, and FOMAT is a filter problem, not an agent problem. You'll leave with a vocabulary for the argument every AI engineer is having right now. Audience takeaways A shared vocabulary (Z, L, the five stops) for the debate splitting AI engineering teams FOMAT — name the fear so you can manage it A per-task framework for choosing where on the Continuum to operate Why capability drift makes "I'll never let it cook" a losing position over time Speaker: Alex Volkov · ThursdAI · @altryne

## Synthesis
### Transcript-Backed Summary
Alex Volkov argues that the real debate in 2026 is not whether AI engineers should read code at all, but how much proof a specific task needs. His core mechanism is a task-based continuum: routine or decomposable work can move toward system-level verification, while high-risk changes still require direct human inspection of the critical path. He pairs that with a practical operating model built around routing changes to the right proof, splitting large pull requests, separating generation from verification, and using traces, evals, shadow mode, observability, and rollback to make the system remember what was checked. The tradeoff is that higher model capability and looped agents reduce the need to inspect every line, but they do not remove judgment; they shift it upward and make review a design problem, not a personality trait.

### Key Takeaways
- The useful operating rule is to route each change to the proof it needs instead of applying one review policy everywhere.
  - Evidence: "This is the your Monday artifact. Routing the change where the proof needs it. Routing the change to the proof that it needs."
- Critical paths still deserve direct human attention, especially for authentication, money movement, permissions, and reversible data.
  - Evidence: "You read every line of authentication, money movement, permissions and reversible data. You inspect the critical path yourself and then obviously you keep going."
- Agents are useful for decomposing large work into smaller pull requests, which makes review more manageable.
  - Evidence: "Your eyes are starting to glaze over a a very long pull request. So splitting into atomic reviewable PRs, you know who's good at it?"
- Looped automation can help, but it does not replace judgment, and self-verifying systems can spiral if left unchecked.
  - Evidence: "I'd likely end up in a downward spiral digging myself into a deeper hole. So again, loops don't remove judgment, but they do raise the stakes on where you put it."

### Claims From The Talk
- The Z/L continuum is real, but it should be applied to tasks rather than treated as a fixed property of a person. (`explicit`)
  - Evidence: "The ZL continuum is real. But it's not about the people. It's about the tasks. The continuum is real."
- As code output scales up, human code review becomes a new bottleneck. (`explicit`)
  - Evidence: "And then they say this, we as we began to push more code around the organization, human code review has become a new bottleneck."
- Capability gains keep moving the review layer upward, so where proof belongs changes over time. (`strong`)
  - Evidence: "If yesterday we inspected the outputs and we read the code uh and today we inspect the task direction and kind of like directed to the right proof maybe tomorrow we're inspecting the loops capability drift changes where proof belongs."
- Looped automation still needs human judgment, and relying on it alone can drive quality downward. (`explicit`)
  - Evidence: "I'd likely end up in a downward spiral digging myself into a deeper hole. So again, loops don't remove judgment, but they do raise the stakes on where you put it."

### Topics Covered
- [[agent-evaluations|Task-based review]] — The idea that review depth should be chosen per task instead of per engineer identity.
- [[agent-evaluations|Proof routing]] — A change-routing approach that assigns the right proof method to each piece of work.
- [[human-oversight-and-review-dynamics|Capability drift]] — The way rising model capability moves the review layer and the location of proof over time.
- [[agent-reliability-and-durable-execution|Looped verification]] — Agents that plan, execute, and verify work on a schedule or loop.

### Tools And Named Systems
- [[cloud-code|Cloud Code]] — The talk uses Cloud Code as an example of agent-authored code becoming normal.
- [[github|GitHub]] — GitHub is used as evidence of the scale of AI-assisted code and commit volume.
- [[fable|Fable]] — Fable is cited as a capability jump that changes what people inspect.

### Novel Concepts And Methods
- **Proof routing** — Send each change to the evidence layer that can actually prove it is safe.
- **Critical-path inspection** — Manually inspect high-risk paths like authentication, money movement, permissions, and reversible data.
- **Atomic PR decomposition** — Break large changes into smaller reviewable units before asking for approval.
- **Separated verification** — Keep code generation, output inspection, and testing in distinct roles.

### Open Questions
- **How should a team decide the minimum proof a specific change needs without overreviewing everything?** — This is the operating question the talk replaces the old read-every-line versus read-nothing debate with.
- **As capability keeps improving, which parts of review stay human and which move into the system?** — The talk argues that capability drift changes the review layer rather than eliminating it.
- **Where should a looped agent stop self-correcting and hand judgment back to a human?** — The talk warns that self-verifying loops can hurt quality if they become the only guardrail.

### Derived Links And Source Material
- [[youtube-ZpK5PWX2YRM-transcript]] — dedicated official recording transcript.
- [[youtube-ZpK5PWX2YRM]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/ZpK5PWX2YRM--2026-06-30-alex-volkov-the-z-l-continuum-should-ai-engineers-still-read-code.json`.

### Speaker Context
- [[alex-volkov|Alex Volkov]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[alex-volkov]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-Lcqat4iP_lE-dense-slides]] (1 viable slide images).
- Related slide/OCR pages:
- [[youtube-Lcqat4iP_lE-dense-slides]]
- [[youtube-Lcqat4iP_lE-reconstructed-slides]]
- [[youtube-Lcqat4iP_lE-slides]]
- Slide-derived terms: `microsoft`, `observability`, `world`, `fair`, `otel`, `windsurf`, `support`, `work`, `observable`, `moment`, `graphite`, `mdaily`, `care`, `both`, `tools`, `openttelemetry`, `primitives`, `traces`

## Official YouTube Recording
- [[youtube-ZpK5PWX2YRM|Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI]] — official AI Engineer YouTube recording published 2026-07-10.
- Evidence status: [[youtube-ZpK5PWX2YRM-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-ZpK5PWX2YRM]] - dedicated official event recording.
- [[youtube-ZpK5PWX2YRM-transcript]] - dedicated official recording transcript.
- [[youtube-Lcqat4iP_lE]] - supporting context; not the exact session recording.

- Source video: `youtube-ZpK5PWX2YRM`
- Slide deck: [[youtube-ZpK5PWX2YRM-slides|Slides: Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI]] — 32 visible slide image(s).
![[assets/slides/ZpK5PWX2YRM/slide-001.jpg]]
![[assets/slides/ZpK5PWX2YRM/slide-002.jpg]]
![[assets/slides/ZpK5PWX2YRM/slide-003.jpg]]
- Slide-derived themes for `youtube-ZpK5PWX2YRM`: future, software, bigger, than, last, engineering, leadership, july.
- Source video: `youtube-Lcqat4iP_lE`
- Slide deck: [[youtube-Lcqat4iP_lE-dense-slides|Dense Slides: The State of MCP observability: Observable.tools — Alex Volkov and Benjamin Eckel, W&B and Dylibso]] — slide evidence page.
- Additional slide evidence: [[youtube-Lcqat4iP_lE-slides|Slides: The State of MCP observability: Observable.tools — Alex Volkov and Benjamin Eckel, W&B and Dylibso]], [[youtube-Lcqat4iP_lE-reconstructed-slides|Reconstructed Slides: The State of MCP observability: Observable.tools — Alex Volkov and Benjamin Eckel, W&B and Dylibso]]
- Slide-derived themes for `youtube-Lcqat4iP_lE`: tool, call, microsoft, tools, client, server, path, calculate.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/ZpK5PWX2YRM.txt` (3,931 words).

## Transcript Markdown
- [[youtube-ZpK5PWX2YRM-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/ZpK5PWX2YRM.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-ZpK5PWX2YRM` — 3,931 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-ZpK5PWX2YRM`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-ZpK5PWX2YRM`: code, okay, read, line, guys, still, loops, engineer.
- Slide-derived themes for `youtube-ZpK5PWX2YRM`: future, software, bigger, than, last, engineering, leadership, july.
- Evidence links for `youtube-ZpK5PWX2YRM` (primary event evidence): [[youtube-ZpK5PWX2YRM]], [[youtube-ZpK5PWX2YRM-transcript]], [[youtube-ZpK5PWX2YRM-slides]]
- `youtube-Lcqat4iP_lE` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-Lcqat4iP_lE`: tool, call, microsoft, tools, client, server, path, calculate.
- Evidence links for `youtube-Lcqat4iP_lE` (supporting context only): [[youtube-Lcqat4iP_lE]], [[youtube-Lcqat4iP_lE-slides]], [[youtube-Lcqat4iP_lE-dense-slides]], [[youtube-Lcqat4iP_lE-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
