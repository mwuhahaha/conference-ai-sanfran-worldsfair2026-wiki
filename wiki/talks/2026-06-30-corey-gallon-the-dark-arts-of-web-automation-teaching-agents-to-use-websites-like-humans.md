---
title: "The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans"
category: "talks"
date: "2026-06-30"
time: "12:05pm-12:25pm"
track: "Computer Use"
room: "Track 7"
speakers: ["Corey Gallon"]
sourceLabels: ["Official conference schedule", "Official speaker roster", "Public company site", "Public GitHub project", "Public YouTube metadata", "Highlight synthesis"]
scheduleTrack: "Computer Use"
scheduleRoom: "Track 7"
scheduleLabels: ["Computer Use", "Track 7", "session", "confirmed"]
highlighted: "true"
highlightPriority: "critical"
---
# The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans

## Highlight Status
This is a highlighted critical talk in the wiki. It should receive extra recording-search effort, richer company and tool context, and more synthesis than an ordinary schedule page.

The talk matters because it argues for browser automation as durable infrastructure rather than disposable agent clicking. Corey Gallon's core claim is practical: if a browser task will happen more than once, an AI agent should be able to turn it into a repeatable program that drives Chrome through the Chrome DevTools Protocol, not burn tokens replaying the same step-by-step browsing sequence.

## Official Schedule Context
- Date/time: 2026-06-30 · 12:05pm-12:25pm
- Track/room: Computer Use · Track 7
- Speaker(s): Corey Gallon
- Session type/status: session · confirmed
- Related person: [[corey-gallon]]
- Related company: [[rexmore]]
- Related tool: [[chrome-agent]]
- Related topic: [[agentic-web]]

## Schedule Labels
- Track: Computer Use
- Room: Track 7
- Session type: session
- Status: confirmed

## Recording Search Status
No exact AI Engineer YouTube recording for this session has been found yet.

Searches performed for this page:
- The local talk/video map currently lists this session as `None found`.
- AI Engineer channel search for `Corey Gallon` found the prior related video [[youtube-JsKTQbT58BY]] but not this exact talk.
- Public YouTube search for the exact title did not return an AI Engineer recording.
- Cached World's Fair livestream transcripts and subtitle files were searched for `Corey`, `Gallon`, `Dark Arts`, `chrome-agent`, `CDP`, and distinctive talk phrases; no match was found.

Interpretation: treat [[youtube-JsKTQbT58BY]] as supporting speaker context, not as the recording of this session. If the official cut or track recording appears later, this page should be revisited first.

## Official Description
Anything you can do in a browser, your agent can do too. Not by tiptoeing through an MCP server one polite, token-burning call at a time -- properly, programmatically, the way you'd drive any other tool. I'll show you how with chrome-agent, an open source wrapper over the Chrome DevTools Protocol that has become irreplaceable in my everyday work. If you'll ever do a browser task more than once, step-by-step MCP browsing is slow, brittle, and bills you tokens for every single click. A CLI straight onto CDP makes the whole browser programmable: loop it, pipe it, script it, walk away. Write it Tuesday, run it a thousand times Wednesday, all without a second of AI agent babysitting.

We'll dispel the MCP hype and myths, with successful demonstrations of cheeky things like: the power of CLI-based browsing and how its so much more capable than mere MCP; reaching through those oh-so-clever cross-origin iframes to clear the verify you're human checkboxes; showing that a JavaScript `.click()` is not a click, rather, just a function call in a costume that is banhammerable; ultimately, proving that a CDP browser operates just like a human with a mouse and keyboard. You'll learn how to point your AI agents at real, messy, uncooperative websites and web applications and have them get things done exactly the way that you would.

## Why This Talk Is Important
This talk sits at the fault line between three approaches to the web:

- Human browsing: slow, visual, stateful, and tolerant of messy interfaces.
- Agent browsing through generic tools: flexible, but often token-expensive and brittle when every click becomes another model-mediated step.
- Programmatic browser control: repeatable, scriptable, inspectable, and able to turn a successful browser run into an operating procedure.

The important idea is not simply "use a browser." It is that browser work can become a programmable substrate for agents. Once an agent has discovered the right sequence, the workflow should graduate from improvisation to reusable automation: loops, pipes, scripts, scheduled runs, and evidence trails.

That makes the session especially relevant to agentic engineering. A production agent does not just need a model and a tool list. It needs a way to interact with the messy web, preserve state, observe what happened, and avoid paying reasoning tokens for mechanical repetition.

## Technical Throughline
The talk centers on [[chrome-agent]], an open source wrapper over the Chrome DevTools Protocol.

The key technical pattern is CDP-first browser control:

- Use the browser as an executable environment, not just a screenshot source.
- Prefer stable browser-level identifiers and observations over brittle CSS selector guessing where possible.
- Combine action and observation so the agent sees the result of a click, fill, navigation, or extraction step.
- Treat page reading, list/table extraction, network inspection, and browser state as first-class agent operations.
- Preserve repeatability: once the workflow is known, run it as code rather than re-prompting the agent through each step.

This contrasts with generic browser-use patterns where each step can require a fresh model call, a fresh visual parse, and a fresh decision about the next click.

## Practical Pattern
Use the Dark Arts pattern when:

- The task happens more than once.
- The target system only exposes a UI or has an insufficient API.
- The agent must operate inside logged-in browser state.
- The workflow involves forms, dashboards, repeated extraction, or cross-page navigation.
- A human would otherwise perform the same browser sequence manually.

Do not treat this as permission to bypass site rules, security boundaries, or user consent. The page should be read as an engineering argument for reliable browser automation, not as a recommendation to violate terms, evade protections, or run unreviewed actions against third-party systems.

## Related YouTube Video
- [[youtube-JsKTQbT58BY]] - The Cure for the Vibe Coding Hangover — Corey J. Gallon, Rexmore. This is a related AI Engineer recording for the same speaker/company, not the exact Dark Arts session.

## Related Public Sources
- [Corey Gallon official speaker page](https://aie-wf.sentry.dev/speakers/spk_corey_gallon)
- [Rexmore official site](https://rexmore.ai/)
- [chrome-agent GitHub repository](https://github.com/sderosiaux/chrome-agent)
- [Corey Gallon website](https://gallon.me)
- [Corey Gallon LinkedIn](https://www.linkedin.com/in/coreygallon)

## Related Pages
- [[corey-gallon]]
- [[rexmore]]
- [[chrome-agent]]
- [[agentic-web]]
- [[ai-sandboxes]]
- [[mcp]]
- [[2026-06-30-paul-klein-iv-bringing-agents-onto-the-world-wide-web]]
- [[2026-06-30-dhruv-batra-computer-use-models-will-agentify-the-web-not-apis]]
- [[2026-06-30-derek-meegan-deploying-browser-agents-at-scale]]

## Evidence Boundary
Official schedule and speaker data are canonical for the talk title, speaker, date, track, and room. The recording has not been found as of this enrichment pass. Public sources about Rexmore, Corey Gallon, and chrome-agent provide supporting context for interpreting the talk, but they are not a substitute for a session transcript.
