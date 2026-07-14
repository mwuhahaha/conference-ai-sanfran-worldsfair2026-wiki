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
chrome-agent is Corey Gallon's open source Python CLI for letting AI agents observe and interact with Chrome through the Chrome DevTools Protocol (CDP). It connects directly to a running browser rather than presenting a separate browser abstraction layer.

## Why It Matters At World's Fair
chrome-agent is named in [[2026-06-30-corey-gallon-the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans|The Dark Arts of Web Automation]] as the tool Corey Gallon uses to make browser work programmatic. In the context of the talk, it represents a broader pattern: use CDP-level browser control to turn repeated web workflows into scripts instead of prompting an agent through every click.

## Important Capabilities
- Direct CDP commands and event subscriptions against a running Chrome or Chromium instance.
- Browser launch, status, navigation, JavaScript evaluation, screenshots, and live protocol help.
- Multiple human and agent participants with isolated event subscriptions.
- One-shot commands for scripts and persistent event streams for longer-running observation.
- Access to the running browser's available CDP domains rather than a fixed curated browser-tool subset.

## Related Scheduled Sessions
- [[2026-06-30-corey-gallon-the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans]] — The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans (Computer Use / Track 7)

## Related Pages
- [[corey-gallon]]
- [[rexmore]]
- [[agentic-web]]
- [[ai-sandboxes]]

## Public Sources
- [Corey Gallon's chrome-agent repository](https://github.com/captivus/chrome-agent)
- [chrome-agent PyPI package](https://pypi.org/project/chrome-agent/)

## Evidence Boundary
The official schedule confirms the talk and describes chrome-agent as the tool being demonstrated. The repository and PyPI package are supporting technical context for the tool's implementation and capabilities; they do not substitute for a recording of the scheduled session.
