---
title: "chrome-agent"
category: "tools"
aliases: ["chrome-agent", "Chrome Agent", "Chrome DevTools Protocol", "CDP"]
sourceLabels: ["Official conference schedule", "Public GitHub project", "Highlight synthesis"]
scheduleTracks: ["Computer Use"]
scheduleRooms: ["Track 7"]
highlighted: "true"
highlightPriority: "high"
sourceAssessment:
  schemaVersion: 1
  claimId: claim:90852e85c17079e15bc107daf1afc92ca765f0f670dbc422828676ee785ab6f5
  subjectId: tool:chrome-agent
  domain: tools page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-17T15:12:45.081803Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:github_rest-github.com
  - source:official-wf26-official-sessions
sourceAssessmentBodySha256: sha256:77f39b9ac85366a03bb8d674ad41f617f40b812c1e63452fca23f1445a585167
---

# chrome-agent

## Overview
chrome-agent is Corey Gallon's open source Python CLI for letting AI agents observe and interact with Chrome through the Chrome DevTools Protocol (CDP). It connects directly to a running browser rather than presenting a separate browser abstraction layer.

## Conference Context
chrome-agent is named in [[2026-06-30-corey-gallon-the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans|The Dark Arts of Web Automation]] as the tool Corey Gallon uses to make browser work programmatic. In the context of the talk, it represents a broader pattern: use CDP-level browser control to turn repeated web workflows into scripts instead of prompting an agent through every click.

## Capabilities
- Direct CDP commands and event subscriptions against a running Chrome or Chromium instance.
- Browser launch, status, navigation, JavaScript evaluation, screenshots, and live protocol help.
- Multiple human and agent participants with isolated event subscriptions.
- One-shot commands for scripts and persistent event streams for longer-running observation.
- Access to the running browser's available CDP domains rather than a fixed curated browser-tool subset.

## Applied Use
Install the Python CLI with `uv tool install chrome-agent`, then launch an isolated Chrome instance. The instance name is the address used for all later CDP commands.

```bash
# Start an isolated, CDP-enabled browser.
chrome-agent launch

# Inspect available instances and page targets.
chrome-agent status

# Navigate and read an exact value from the page.
chrome-agent myproject-01 Page.navigate '{"url":"https://example.com"}'
chrome-agent myproject-01 Runtime.evaluate '{"expression":"document.title","returnByValue":true}'

# Discover the protocol supported by this running Chrome.
chrome-agent help myproject-01 Page.navigate

# Shut down the isolated instance when the work is complete.
chrome-agent stop myproject-01
```

For event-driven debugging, keep an `attach` process running while another process drives the page. The observer receives JSON lines only for the events it subscribed to.

```bash
chrome-agent attach myproject-01 +Page.loadEventFired +Network.requestWillBeSent > /tmp/chrome-agent-events.jsonl &
chrome-agent myproject-01 Page.navigate '{"url":"https://example.com"}'
```

## Effective Use Cases
<table>
  <thead>
    <tr><th>Situation</th><th>Useful approach</th><th>Why this tool fits</th></tr>
  </thead>
  <tbody>
    <tr><td>Debug a web app against a real Chrome</td><td>Use <code>Runtime.evaluate</code>, <code>Network</code>, and <code>Log</code> commands against one named instance.</td><td>The CLI forwards arbitrary CDP methods instead of limiting work to a small browser-tool surface.</td></tr>
    <tr><td>Observe a workflow while a human or another agent drives it</td><td>Run <code>attach</code> with narrow Page or Network subscriptions.</td><td>Each participant has an isolated event subscription, avoiding a shared noisy stream.</td></tr>
    <tr><td>Turn a repeated browser check into a script</td><td>Use one-shot commands for navigation, evaluation, screenshots, and direct protocol calls.</td><td>The command interface is stable while the exact supported CDP surface comes from the running browser.</td></tr>
    <tr><td>Operate a UI that ignores a synthetic DOM click</td><td>Locate coordinates, dispatch paired <code>Input.dispatchMouseEvent</code> press and release events, then observe the result.</td><td>Input-domain events go through Chrome's native input pipeline.</td></tr>
    <tr><td>Investigate a SPA or network-backed page</td><td>Wait on a Page event or observable page condition, then observe the actual request rather than guessing endpoints.</td><td>Persistent event streaming exposes browser-observed navigation and network consequences.</td></tr>
  </tbody>
</table>

## Operating Tricks And Guardrails
- Ask the live browser for the command signature with `chrome-agent help <instance> Domain.method` before using a less familiar or newly added CDP capability; its protocol schema is more current than a static command list.
- Use a sense-act-sense loop: inspect DOM, accessibility, runtime, or network state; act; then confirm an observable effect. A successful command response alone is not proof the UI changed.
- Prefer `--url` or a target-id prefix when more than one tab is open. Numeric target positions can change as tabs are added or removed.
- Avoid fixed sleeps after navigation. Wait for `Page.loadEventFired`, `document.readyState`, or the element/state that establishes page readiness.
- Keep credentialed work within accounts and systems you are authorized to access. Use an isolated browser profile by default; do not treat CDP access as permission to extract credentials or bypass site controls.
- Use `cleanup` after interrupted headless runs to remove stale instance records.

## Alternative Implementation
[[sderosiaux-chrome-agent|sderosiaux/chrome-agent]] is an independent Rust browser-agent CLI that also works through Chrome DevTools Protocol. It is not Corey Gallon's work and is not evidence for his scheduled session. See [[chrome-agent-implementation-delta|the implementation delta]] for the project identities, technical differences, and source boundary.

## Related Scheduled Sessions
- [[2026-06-30-corey-gallon-the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans]] — The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans (Computer Use / Track 7)

## Connections
- [[corey-gallon]]
- [[rexmore]]
- [[agentic-web]]
- [[ai-sandboxes]]
- [[sderosiaux-chrome-agent]]
- [[chrome-agent-implementation-delta]]

## Sources
- [Corey Gallon's chrome-agent repository](https://github.com/captivus/chrome-agent)
- [chrome-agent PyPI package](https://pypi.org/project/chrome-agent/)

## Evidence Boundary
The official schedule confirms the talk and describes chrome-agent as the tool being demonstrated. The repository and PyPI package are supporting technical context for the tool's implementation and capabilities; they do not substitute for a recording of the scheduled session.
