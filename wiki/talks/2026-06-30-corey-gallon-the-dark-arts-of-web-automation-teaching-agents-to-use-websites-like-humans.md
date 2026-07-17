---
title: "The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans"
category: "talks"
date: "2026-06-30"
time: "12:05pm-12:25pm"
track: "Computer Use"
room: "Track 7"
speakers: ["Corey Gallon"]
sourceLabels: ["Official conference schedule", "Official speaker roster", "Public company site", "Public GitHub project", "Public package registry", "Public YouTube metadata", "Synthesis"]
scheduleTrack: "Computer Use"
scheduleRoom: "Track 7"
scheduleLabels: ["Computer Use", "Track 7", "session", "confirmed"]
highlighted: "true"
highlightPriority: "critical"
---
# The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans

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

## Synthesis
### Synthesized Breakdown
Anything you can do in a browser, your agent can do too. Not by tiptoeing through an MCP server one polite, token-burning call at a time -- properly, programmatically, the way you'd drive any other tool. I'll show you how with chrome-agent, an open source wrapper over the Chrome DevTools Protocol that has become irreplaceable in my everyday work. If you'll ever do a browser task more than once, step-by-step MCP browsing is slow, brittle, and bills you tokens for every single click.

### Speaker And Company Context
- [[corey-gallon|Corey Gallon]] — Managing Director at [[rexmore|Rexmore]].

### Topics Covered
- [[agentic-web]]
- [[mcp]]

### Derived Links And Source Material
- [[youtube-JsKTQbT58BY]] — related YouTube source page.

### Novel Concepts / Clever Methods
- No highlighted novel concept has been detected yet.

### Evidence Boundary
This synthesis is based on the official schedule and linked source pages. It should be revisited when exact session recordings or transcript-backed secondary sources are available.
## Significance
This is a critical talk for the wiki's browser-agent and agentic-web coverage. It receives extra recording-search effort, richer company and tool context, and deeper synthesis because it connects web automation technique to repeatable engineering practice.

The talk matters because it argues for browser automation as durable infrastructure rather than disposable agent clicking. Corey Gallon's core claim is practical: if a browser task will happen more than once, an AI agent should be able to turn it into a repeatable program that drives Chrome through the Chrome DevTools Protocol, not burn tokens replaying the same step-by-step browsing sequence.

This talk sits at the fault line between three approaches to the web:

- Human browsing: slow, visual, stateful, and tolerant of messy interfaces.
- Agent browsing through generic tools: flexible, but often token-expensive and brittle when every click becomes another model-mediated step.
- Programmatic browser control: repeatable, scriptable, inspectable, and able to turn a successful browser run into an operating procedure.

The important idea is not simply "use a browser." It is that browser work can become a programmable substrate for agents. Once an agent has discovered the right sequence, the workflow should graduate from improvisation to reusable automation: loops, pipes, scripts, scheduled runs, and evidence trails.

That makes the session especially relevant to agentic engineering. A production agent does not just need a model and a tool list. It needs a way to interact with the messy web, preserve state, observe what happened, and avoid paying reasoning tokens for mechanical repetition.

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
- [[youtube-JsKTQbT58BY]] - supporting context; not the exact session recording.
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
- [Corey Gallon's chrome-agent GitHub repository](https://github.com/captivus/chrome-agent)
- [chrome-agent package on PyPI](https://pypi.org/project/chrome-agent/)
- [Corey Gallon website](https://gallon.me)
- [Corey Gallon LinkedIn](https://www.linkedin.com/in/coreygallon)

## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-JsKTQbT58BY` — source page linked; role: supporting context only.
- Evidence links for `youtube-JsKTQbT58BY` (supporting context only): [[youtube-JsKTQbT58BY]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
## Evidence Boundary
Official schedule and speaker data are canonical for the talk title, speaker, date, track, and room. The recording has not been found as of this enrichment pass. Public sources about Rexmore, Corey Gallon, and chrome-agent provide supporting context for interpreting the talk, but they are not a substitute for a session transcript.
