---
title: "chrome-agent"
category: "tools"
aliases: ["chrome-agent", "Chrome Agent", "Chrome DevTools Protocol", "CDP"]
sourceLabels: ["Official conference schedule", "Public GitHub project", "Highlight synthesis"]
scheduleTracks: ["Computer Use"]
scheduleRooms: ["Track 7"]
highlighted: "true"
highlightPriority: "high"
---

# chrome-agent

## What It Is
chrome-agent is an open source browser automation tool for AI agents. The GitHub project describes it as a small Rust binary that talks directly to Chrome through the Chrome DevTools Protocol and returns compact, agent-readable page state.

## Why It Matters At World's Fair
chrome-agent is named in [[2026-06-30-corey-gallon-the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans|The Dark Arts of Web Automation]] as the tool Corey Gallon uses to make browser work programmatic. In the context of the talk, it represents a broader pattern: use CDP-level browser control to turn repeated web workflows into scripts instead of prompting an agent through every click.

## Important Capabilities
- Direct CDP control of Chrome.
- Compact page representation for agents.
- Stable element identifiers based on Chrome backend node IDs.
- Action plus observation in one command when using inspect-style workflows.
- Article reading, list/table extraction, and network inspection.
- Structured errors and hints that an agent can parse.
- Session persistence so Chrome can remain alive between commands.

## Related Scheduled Sessions
- [[2026-06-30-corey-gallon-the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans]] — The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans (Computer Use / Track 7)

## Related Pages
- [[corey-gallon]]
- [[rexmore]]
- [[agentic-web]]
- [[ai-sandboxes]]

## Public Sources
- [chrome-agent GitHub repository](https://github.com/sderosiaux/chrome-agent)

## Evidence Boundary
The official schedule confirms the talk and describes chrome-agent as the tool being demonstrated. The GitHub repository is supporting technical context for what the tool does and how it frames browser automation for agents.
