---
title: Perception Agents
category: talks
date: '2026-06-30'
time: '9:45am-10:05am'
track: Autoresearch
room: Main Stage
speakers:
  - Antje Barth
sourceLabels:
  - Official conference schedule
  - Public YouTube metadata
scheduleTrack: Autoresearch
scheduleRoom: Main Stage
scheduleLabels:
  - Autoresearch
  - Main Stage
  - keynote
  - confirmed
last_auto_summarized: '2026-07-18T09:12:58.904Z'
---
# Perception Agents

## Conference Context
- Date/time: 2026-06-30 · 9:45am-10:05am
- Track/room: Autoresearch · Main Stage
- Speaker(s): Antje Barth
- Session type/status: keynote · confirmed

- Track: Autoresearch
- Room: Main Stage
- Session type: keynote
- Status: confirmed

## Session Description
Human-agent collaboration is changing, becoming more visual. The agents most teams ship today still wait for us to type a paragraph to explain what we're looking at. They cannot see a screen, navigate a UI that changes, or recover when an application throws an unexpected modal. That is the architectural gap between agents that demo well and agents that work alongside real teams in real software. Perception agents close it. They see and use computers the way people do, reason about what they see, and act with clicks and keystrokes.

## Synthesis
### Transcript-Backed Summary
Antje Barth argues that the blocker for useful workplace agents is no longer simple action-taking, but reliable end-to-end completion of messy work across multiple applications. Her answer is to make agents perceive the rendered interface the way humans do, share context with the user, and close the loop with annotation and self-verification so the agent can confirm what it did instead of acting blindly. She contrasts this with coding, where verifiability made trust possible, and says knowledge work still lacks that kind of easy validation. The practical consequence is a workflow where people can point at what they mean, have the agent apply changes directly from that screen-grounded input, and then run visual and user-flow checks before the work is accepted.

### Key Takeaways
- For real-world agent adoption, reliability matters more than raw capability because trust collapses when failures are costly.
  - Evidence: "Now the next hard part is really reliability and without reliability we cannot really build up trust in those systems."
- Shared context is more important than a bigger model when a human and an agent need to solve work together.
  - Evidence: "What you need is this shared context. Because if we're looking the agent and myself at the same screen, I probably have much less explanating to do."
- Directly selecting what you mean on the screen reduces lossy back-and-forth compared with paragraph-length instructions.
  - Evidence: "So there is no back and forth anymore because you captured exactly what you saw on screen and the agent can see the same thing."
- Verification should end with a human-readable report that makes pass/fail results and failures explicit.
  - Evidence: "And then once it's done, it's writing a report which you can review and it's going to call out which tests passed and it's going to tell you anything that didn't."
- The system is intended to improve through open-source use, feedback, and breaking things in the open.
  - Evidence: "give us the feedback what you would like to see where this should go next because ultimately none of us get smart alone and that's the whole point."

### Claims From The Talk
- The speaker argues that the real next hard problem for agents is reliability and trust, not basic capability. (`explicit`)
  - Evidence: "Now the next hard part is really reliability and without reliability we cannot really build up trust in those systems."
- She says coding was the first domain where agents became trustworthy because code is verifiable by running, testing, and checking it. (`explicit`)
  - Evidence: "So why is that? Why was coding first solved? It's because code is verifiable. You can run it, you can test it, you can check it and you can be for sure that it worked."
- She reports that most knowledge work lacks a unit-test-like verification mechanism, which is why reliability breaks down there. (`explicit`)
  - Evidence: "So there is no unit test that can answer those questions. So verification really hits the wall right where most of our work lives."
- She argues that perception agents must read the rendered screen and its layout and state, rather than scrape page code, to act correctly. (`explicit`)
  - Evidence: "And it starts here really with the first word which is perceive. The agent has to take in the screen the way you do, not scrape the code behind the page, but what's actually rendered, the layout, the state, what just changed the work, what we're doing, and then do it."
- She says the first two open-source parts of the harness are annotation for expressing intent and verification for checking the agent's work. (`explicit`)
  - Evidence: "There's two pieces. There is annotation which you can use to tell it what you want. And then the second piece, the verification part gives the agent the capability to check its own work."

### Topics Covered
- [[agent-evaluations|Agent Reliability]] — The gap between agents that can take actions and agents that can be trusted to finish messy work end to end.
- **Shared Context** — The role of looking at the same screen or interface as the human to reduce explanation and improve collaboration.
- **Rendered UI Perception** — The idea that an agent should read the rendered UI, layout, and state before acting.
- **Screen Annotation** — Capturing intent by marking elements directly on screen instead of writing a long instruction.
- **UI Verification** — Checking UI changes against design rules and user flows after the agent acts.
- [[agentic-web|Transcript-to-Action Collaboration]] — Using non-screen inputs, such as meeting transcripts, to drive changes in the same workflow.

### Tools And Named Systems
- [[github|GitHub]] — The open-source repos where the perception-agent harness is being shared and extended.
- **Chrome** — The browser environment used for the annotation extension demo.
- **Zoom** — The meeting platform used in the example of collaborative work across a shared screen.
- [[slack|Slack]] — One of the cross-system destinations in the onboarding workflow example.

### Novel Concepts And Methods
- **Shared Context** — Use the same on-screen context as the human so the agent needs less explanation and can collaborate on the actual work.
- **Rendered-Interface Perception** — Have the agent consume the rendered interface, layout, and state before acting, instead of relying on underlying page code.
- **Annotation Capture** — Capture intent by selecting elements directly on the screen so the instruction is precise and less lossy than a long paragraph.
- **Self-Verification** — Check results after acting by comparing them with design rules and walking relevant user flows, then produce a report.

### Open Questions
- **How can agents be made reliable enough for messy knowledge work when there is no easy way to verify the answer?** — This is the central open problem behind making perception agents trustworthy in real workflows.
- **How can an agent react while the human is still working instead of waiting for turn-based prompts and back-and-forth?** — The talk frames real-time collaboration as a missing capability, not just better task completion.
- **How should design rules be represented and maintained so verification can judge whether a change is actually on brand?** — The verification flow depends on durable specs, but the talk implies those specs may not already exist in a usable form.

### Derived Links And Source Material
- [[youtube-2JX6JYyQG4Y-transcript]] — dedicated official recording transcript.
- [[youtube-2JX6JYyQG4Y]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/2JX6JYyQG4Y--2026-06-30-antje-barth-perception-agents.json`.

### Speaker Context
- No speaker profile is attached in the official schedule data.

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[antje-barth]]

## Slide Evidence
- Slide-only cropped deck: [[youtube-WJjInLeaJjo-dense-slides]] (2 viable slide images).
- Related slide/OCR pages:
- [[youtube-WJjInLeaJjo-dense-slides]]
- [[youtube-WJjInLeaJjo-reconstructed-slides]]
- [[youtube-WJjInLeaJjo-slides]]
- Slide-derived terms: `world`, `engineering`, `server`, `future`, `amazon`, `sfair`, `fair`, `tools`, `strands`, `open`, `servers`, `barth`, `alexa`, `orld`, `services`, `code`, `developer`, `rere`

## Official YouTube Recording
- [[youtube-2JX6JYyQG4Y|Perception Agents — Antje Barth, Amazon AGI Lab]] — official AI Engineer YouTube recording published 2026-07-23.
- Evidence status: [[youtube-2JX6JYyQG4Y-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-2JX6JYyQG4Y]] - dedicated official event recording.
- [[youtube-2JX6JYyQG4Y-transcript]] - dedicated official recording transcript.
- [[youtube-WJjInLeaJjo]] - supporting context; not the exact session recording.

- Source video: `youtube-2JX6JYyQG4Y`
- Slide deck: [[youtube-2JX6JYyQG4Y-slides|Slides: Perception Agents — Antje Barth, Amazon AGI Lab]] — 31 visible slide image(s).
![[assets/slides/2JX6JYyQG4Y/slide-001.jpg]]
![[assets/slides/2JX6JYyQG4Y/slide-002.jpg]]
![[assets/slides/2JX6JYyQG4Y/slide-003.jpg]]
- Slide-derived themes for `youtube-2JX6JYyQG4Y`: amazon, easy, part, clicking, tool, still, figure, ease.
- Source video: `youtube-WJjInLeaJjo`
- Slide deck: [[youtube-WJjInLeaJjo-dense-slides|Dense Slides: Building Agents at Cloud Scale — Antje Barth, AWS]] — slide evidence page.
- Additional slide evidence: [[youtube-WJjInLeaJjo-slides|Slides: Building Agents at Cloud Scale — Antje Barth, AWS]], [[youtube-WJjInLeaJjo-reconstructed-slides|Reconstructed Slides: Building Agents at Cloud Scale — Antje Barth, AWS]]
- Slide-derived themes for `youtube-WJjInLeaJjo`: barth, developer, documentation, server, customer, experience, advocate, june.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/2JX6JYyQG4Y.txt` (2,870 words).

## Transcript Markdown
- [[youtube-2JX6JYyQG4Y-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/2JX6JYyQG4Y.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-2JX6JYyQG4Y` — 2,870 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-2JX6JYyQG4Y`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-2JX6JYyQG4Y`: screen, still, first, maybe, check, meeting, click, part.
- Slide-derived themes for `youtube-2JX6JYyQG4Y`: amazon, easy, part, clicking, tool, still, figure, ease.
- Evidence links for `youtube-2JX6JYyQG4Y` (primary event evidence): [[youtube-2JX6JYyQG4Y]], [[youtube-2JX6JYyQG4Y-transcript]], [[youtube-2JX6JYyQG4Y-slides]]
- `youtube-WJjInLeaJjo` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-WJjInLeaJjo`: barth, developer, documentation, server, customer, experience, advocate, june.
- Evidence links for `youtube-WJjInLeaJjo` (supporting context only): [[youtube-WJjInLeaJjo]], [[youtube-WJjInLeaJjo-slides]], [[youtube-WJjInLeaJjo-dense-slides]], [[youtube-WJjInLeaJjo-reconstructed-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
