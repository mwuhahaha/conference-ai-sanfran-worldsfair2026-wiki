---
title: "The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans"
category: "talks"
date: "2026-06-30"
time: "12:05pm-12:25pm"
track: "Computer Use"
room: "Track 7"
speakers: ["Corey Gallon"]
sourceLabels: ["Official conference schedule", "Official speaker roster", "Public company site", "Public GitHub project", "Public YouTube metadata", "Synthesis"]
scheduleTrack: "Computer Use"
scheduleRoom: "Track 7"
scheduleLabels: ["Computer Use", "Track 7", "session", "confirmed"]
highlighted: "true"
highlightPriority: "critical"
---
# The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans

## Significance
This is a critical talk for the wiki's browser-agent and agentic-web coverage. It receives extra recording-search effort, richer company and tool context, and deeper synthesis because it connects web automation technique to repeatable engineering practice.

The talk matters because it argues for browser automation as durable infrastructure rather than disposable agent clicking. Corey Gallon's core claim is practical: if a browser task will happen more than once, an AI agent should be able to turn it into a repeatable program that drives Chrome through the Chrome DevTools Protocol, not burn tokens replaying the same step-by-step browsing sequence.

This talk sits at the fault line between three approaches to the web:

- Human browsing: slow, visual, stateful, and tolerant of messy interfaces.
- Agent browsing through generic tools: flexible, but often token-expensive and brittle when every click becomes another model-mediated step.
- Programmatic browser control: repeatable, scriptable, inspectable, and able to turn a successful browser run into an operating procedure.

The important idea is not simply "use a browser." It is that browser work can become a programmable substrate for agents. Once an agent has discovered the right sequence, the workflow should graduate from improvisation to reusable automation: loops, pipes, scripts, scheduled runs, and evidence trails.

That makes the session especially relevant to agentic engineering. A production agent does not just need a model and a tool list. It needs a way to interact with the messy web, preserve state, observe what happened, and avoid paying reasoning tokens for mechanical repetition.

## Conference Context
- Date/time: 2026-06-30 · 12:05pm-12:25pm
- Track/room: Computer Use · Track 7
- Speaker(s): Corey Gallon
- Session type/status: session · confirmed
- Related person: [[corey-gallon]]
- Related company: [[rexmore]]
- Related tool: [[chrome-agent]]
- Related topic: [[agentic-web]]

- Track: Computer Use
- Room: Track 7
- Session type: session
- Status: confirmed

## Session Description
Anything you can do in a browser, your agent can do too. Not by tiptoeing through an MCP server one polite, token-burning call at a time -- properly, programmatically, the way you'd drive any other tool. I'll show you how with chrome-agent, an open source wrapper over the Chrome DevTools Protocol that has become irreplaceable in my everyday work. If you'll ever do a browser task more than once, step-by-step MCP browsing is slow, brittle, and bills you tokens for every single click. A CLI straight onto CDP makes the whole browser programmable: loop it, pipe it, script it, walk away. Write it Tuesday, run it a thousand times Wednesday, all without a second of AI agent babysitting. We'll dispel the MCP hype and myths, with successful demonstrations of cheeky things like: the power of CLI-based browsing and how its so much more capable than mere MCP; reaching through those oh-so-clever cross-origin iframes to clear the verify you're human checkboxes; showing that a JavaScript .click() is not a click, rather, just a function call in a costume that is banhammerable; ultimately, proving that a CDP browser operates just like a meatbag with a mouse and keyboard. You'll learn how to point your AI agents at real, messy, uncooperative websites and web applications and have them get things done exactly the way that you would.

## Recording Search Status
No exact AI Engineer YouTube recording for this session has been found yet.

Searches performed for this page:
- The local talk/video map currently lists this session as `None found`.
- AI Engineer channel search for `Corey Gallon` found the prior related video [[youtube-JsKTQbT58BY]] but not this exact talk.
- Public YouTube search for the exact title did not return an AI Engineer recording.
- The official schedule places the session on 2026-06-30 at 12:05pm in the Computer Use track, room Track 7. The AI Engineer channel Streams tab was checked for a same-day Track 7 or Computer Use room livestream; the only World's Fair 2026 livestreams found there are the broad main-stage/program streams [[youtube-htM02KMNZnk]], [[youtube-4sX_He5c4sI]], and [[youtube-I2cbIws9j10]].
- Channel searches for `WF2026 Computer Use`, `Track 7`, `web automation`, and `Dark Arts Web Automation` did not return a Track 7 room stream or this exact session cut.
- Cached World's Fair livestream transcripts and subtitle files were searched for `Corey`, `Gallon`, `Dark Arts`, `chrome-agent`, `chrome agent`, `verify you're human`, `meatbag`, `token-burning`, `JavaScript .click`, and related distinctive talk phrases; no match was found.

Interpretation: treat [[youtube-JsKTQbT58BY]] as supporting speaker context, not as the recording of this session. If the official cut or track recording appears later, this page should be revisited first.

## Technical Pattern
The talk centers on [[chrome-agent]], an open source wrapper over the Chrome DevTools Protocol.

The key technical pattern is CDP-first browser control:

- Use the browser as an executable environment, not just a screenshot source.
- Prefer stable browser-level identifiers and observations over brittle CSS selector guessing where possible.
- Combine action and observation so the agent sees the result of a click, fill, navigation, or extraction step.
- Treat page reading, list/table extraction, network inspection, and browser state as first-class agent operations.
- Preserve repeatability: once the workflow is known, run it as code rather than re-prompting the agent through each step.

This contrasts with generic browser-use patterns where each step can require a fresh model call, a fresh visual parse, and a fresh decision about the next click.

## Applied Pattern
Use the Dark Arts pattern when:

- The task happens more than once.
- The target system only exposes a UI or has an insufficient API.
- The agent must operate inside logged-in browser state.
- The workflow involves forms, dashboards, repeated extraction, or cross-page navigation.
- A human would otherwise perform the same browser sequence manually.

Do not treat this as permission to bypass site rules, security boundaries, or user consent. The page should be read as an engineering argument for reliable browser automation, not as a recommendation to violate terms, evade protections, or run unreviewed actions against third-party systems.

## Media Evidence
- [[youtube-JsKTQbT58BY]] - The Cure for the Vibe Coding Hangover — Corey J. Gallon, Rexmore. This is a related AI Engineer recording for the same speaker/company, not the exact Dark Arts session.

- [[youtube-4sX_He5c4sI-transcript]] — full cached transcript markdown for the related YouTube source.
- [[youtube-I2cbIws9j10-transcript]] — full cached transcript markdown for the related YouTube source.
- [[youtube-htM02KMNZnk-transcript]] — full cached transcript markdown for the related YouTube source.

These are phone-photo slide captures from the Google Photos `AIE Slides` album. They are supporting slide evidence and do not override official schedule fields.
- [[google-photos-aie-slides-9gWZzS1EpXM1C5eK6-dark-arts-web-automation-slides]] - Google Photos Slides: The Dark Arts of Web Automation (confidence: high).

- Source video: `youtube-4sX_He5c4sI`
- Slide deck: [[youtube-4sX_He5c4sI-dense-slides|Dense Slides: WF2026: Autoresearch & Keynotes ft. Anthropic, Google DeepMind, Amazon AGI, Sonar, Arena, Recursive]] — 14 visible slide image(s); 14 HTML recreation(s).
![[assets/dense-slides/4sX_He5c4sI/slide-001.jpg]]
![[assets/dense-slides/4sX_He5c4sI/slide-002.jpg]]
![[assets/dense-slides/4sX_He5c4sI/slide-003.jpg]]
- Additional slide evidence: [[youtube-4sX_He5c4sI-slides|Slides: WF2026: Autoresearch & Keynotes ft. Anthropic, Google DeepMind, Amazon AGI, Sonar, Arena, Recursive]], [[youtube-4sX_He5c4sI-reconstructed-slides|Reconstructed Slides: WF2026: Autoresearch & Keynotes ft. Anthropic, Google DeepMind, Amazon AGI, Sonar, Arena, Recursive]]
- Slide-derived themes for `youtube-4sX_He5c4sI`: system, prompt, examples, tools, lots, claude, gets, smarter.
- Source video: `youtube-I2cbIws9j10`
- Slide deck: [[youtube-I2cbIws9j10-dense-slides|Dense Slides: WF26: Harness Engineering & Startup Battlefield ft. Garry Tan, Mike Krieger, @t3dotgg , DSPy]] — 11 visible slide image(s); 11 HTML recreation(s).
![[assets/dense-slides/I2cbIws9j10/slide-001.jpg]]
![[assets/dense-slides/I2cbIws9j10/slide-002.jpg]]
![[assets/dense-slides/I2cbIws9j10/slide-003.jpg]]
- Additional slide evidence: [[youtube-I2cbIws9j10-slides|Slides: WF26: Harness Engineering & Startup Battlefield ft. Garry Tan, Mike Krieger, @t3dotgg , DSPy]]
- Slide-derived themes for `youtube-I2cbIws9j10`: context, window, selects, response, facts, retry, coerce, rollback.
- Source video: `youtube-htM02KMNZnk`
- Slide deck: [[youtube-htM02KMNZnk-dense-slides|Dense Slides: WF2026: Software Factories & Keynotes ft. Microsoft, OpenAI, OpenClaw, Z.ai (GLM), MiniMax, HF]] — 18 visible slide image(s); 18 HTML recreation(s).
![[assets/dense-slides/htM02KMNZnk/slide-001.jpg]]
![[assets/dense-slides/htM02KMNZnk/slide-002.jpg]]
![[assets/dense-slides/htM02KMNZnk/slide-003.jpg]]
- Additional slide evidence: [[youtube-htM02KMNZnk-slides|Slides: WF2026: Software Factories & Keynotes ft. Microsoft, OpenAI, OpenClaw, Z.ai (GLM), MiniMax, HF]], [[youtube-htM02KMNZnk-reconstructed-slides|Reconstructed Slides: WF2026: Software Factories & Keynotes ft. Microsoft, OpenAI, OpenClaw, Z.ai (GLM), MiniMax, HF]]
- Slide-derived themes for `youtube-htM02KMNZnk`: cycles, stacking, loops, tokens, tools, tasks, throughput, many.

## Connections
- [[corey-gallon]]
- [[rexmore]]
- [[chrome-agent]]
- [[agentic-web]]
- [[ai-sandboxes]]
- [[mcp]]
- [[2026-06-30-paul-klein-iv-bringing-agents-onto-the-world-wide-web]]
- [[2026-06-30-dhruv-batra-computer-use-models-will-agentify-the-web-not-apis]]
- [[2026-06-29-derek-meegan-deploying-browser-agents-at-scale]]

## Sources
- [Corey Gallon official speaker page](https://aie-wf.sentry.dev/speakers/spk_corey_gallon)
- [Rexmore official site](https://rexmore.ai/)
- [chrome-agent GitHub repository](https://github.com/sderosiaux/chrome-agent)
- [Corey Gallon website](https://gallon.me)
- [Corey Gallon LinkedIn](https://www.linkedin.com/in/coreygallon)

## Evidence Graph
This evidence graph is generated from currently linked source material: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Media Signals
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 8 slide-derived text signals
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: system, prompt, examples, tools, lots, claude, gets, smarter.
- Evidence links for `youtube-4sX_He5c4sI`: [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube-I2cbIws9j10` — 91,792 transcript words; 7 slide-derived text signals
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: context, window, selects, response, facts, retry, coerce, rollback.
- Evidence links for `youtube-I2cbIws9j10`: [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
- `youtube-JsKTQbT58BY` — source page linked
- Evidence links for `youtube-JsKTQbT58BY`: [[youtube-JsKTQbT58BY]]
- `youtube-htM02KMNZnk` — 89,050 transcript words; 4 slide-derived text signals
- Transcript signals for `youtube-htM02KMNZnk`: model, code, models, loop, well, software, first, team.
- Slide-derived themes for `youtube-htM02KMNZnk`: cycles, stacking, loops, tokens, tools, tasks, throughput, many.
- Evidence links for `youtube-htM02KMNZnk`: [[youtube-htM02KMNZnk]], [[youtube-htM02KMNZnk-transcript]], [[youtube-htM02KMNZnk-slides]], [[youtube-htM02KMNZnk-dense-slides]], [[youtube-htM02KMNZnk-reconstructed-slides]]

### Agent Reading Notes
Use these signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.

## Evidence Boundary
Official schedule and speaker data are canonical for the talk title, speaker, date, track, and room. The recording has not been found as of this enrichment pass. Public sources about Rexmore, Corey Gallon, and chrome-agent provide supporting context for interpreting the talk, but they are not a substitute for a session transcript.

## Synthesis
### Synthesized Breakdown
The session explains MCP Apps as a way to add interactive UI to MCP-based workflows. It treats the MCP host as the place where tool data, model reasoning, and human controls meet.

### Speaker And Company Context
- [[corey-gallon|Corey Gallon]] — Managing Director at [[rexmore|Rexmore]].

### Topics Covered
- [[agent-security]]
- [[agentic-search]]
- [[agentic-web]]
- [[ai-sandboxes]]
- [[coding-agents]]
- [[mcp]]
- [[mcp-apps]]

### Derived Links And Source Material
- [[youtube-4sX_He5c4sI-transcript]] — transcript markdown; source cache `raw/sources/youtube-livestream-transcripts/4sX_He5c4sI.txt` (82,600 words).
- [[youtube-I2cbIws9j10-transcript]] — transcript markdown; source cache `raw/sources/youtube-livestream-transcripts/I2cbIws9j10.txt` (91,792 words).
- [[youtube-htM02KMNZnk-transcript]] — transcript markdown; source cache `raw/sources/youtube-livestream-transcripts/htM02KMNZnk.txt` (89,050 words).
- [[youtube-4sX_He5c4sI]] — related YouTube source page.
- [[youtube-4sX_He5c4sI-slides]] — slide evidence.
- [[youtube-4sX_He5c4sI-reconstructed-slides]] — slide evidence.
- [[youtube-4sX_He5c4sI-dense-slides]] — slide evidence.
- [[youtube-I2cbIws9j10]] — related YouTube source page.
- [[youtube-I2cbIws9j10-slides]] — slide evidence.
- [[youtube-I2cbIws9j10-dense-slides]] — slide evidence.
- [[youtube-JsKTQbT58BY]] — related YouTube source page.
- [[youtube-htM02KMNZnk]] — related YouTube source page.
- [[youtube-htM02KMNZnk-slides]] — slide evidence.
- [[youtube-htM02KMNZnk-reconstructed-slides]] — slide evidence.
- [[youtube-htM02KMNZnk-dense-slides]] — slide evidence.

### Novel Concepts / Clever Methods
- [[agent-ready-accessibility|Agent-Ready Accessibility]] — Designing for agents and designing for accessibility converge around explicit structure, reachable controls, and understandable state.
- [[mcp-app-runtime|MCP Apps As Agentic App Runtime]] — MCP Apps treats interactive UI returned from MCP servers as a runtime layer for agent-facing software.

### Evidence Boundary
This synthesis uses the official schedule plus cached video transcripts. Official AI Engineer World's Fair San Francisco 2026 livestreams and cut videos are primary event video sources for transcript/slide evidence; external, historical, or speaker-matched videos remain supporting context unless manually verified as exact official event recordings.
