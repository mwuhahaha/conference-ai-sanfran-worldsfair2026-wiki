---
title: "sderosiaux/chrome-agent"
category: "tools"
aliases: ["sderosiaux chrome-agent", "Rust chrome-agent"]
sourceLabels: ["Public GitHub project", "Supporting comparison context"]
status: "external comparison"
accidentalResources: ["https://github.com/sderosiaux/chrome-agent"]
sourceAssessment:
  schemaVersion: 1
  claimId: claim:19aefa10b1e965376169cacef953e33e2490c3c564887c1fda32b7c856843659
  subjectId: tool:sderosiaux-chrome-agent
  domain: tools page evidence coverage
  intendedUse: comparison_context
  asOf: '2026-07-17T15:12:45.081803Z'
  state: limited
  basis: source_attributed
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:github_rest-github.com
sourceAssessmentBodySha256: sha256:c104f5bdd40ed9699778c824b2050213a3fc0ee14f9f1d62ecb056b1fe977ca6
---

# sderosiaux/chrome-agent

## Overview
`sderosiaux/chrome-agent` is an independent Rust command-line project for agent-oriented browser automation through Chrome DevTools Protocol (CDP). Its public repository describes compact accessibility-tree snapshots, stable backend node identifiers, browser actions, inspection, and content extraction as parts of its interface.

## Conference Context
This project was found accidentally during third-party validation of the similarly named [[chrome-agent]] associated with Corey Gallon's scheduled World's Fair session. The initial repository match was wrong: this Rust project is not Corey Gallon's work. It is retained as a clearly labeled alternative because the name collision and technical overlap are useful comparison context.

## Applied Use
The project's documented quick path is `npx chrome-agent --help` for a no-install run, or `npm install -g chrome-agent` for the prebuilt CLI. Its default loop is inspect, act, inspect: navigate with `--inspect`, use the returned UID, then request another inspection after an action.

```bash
# Start from the built-in CLI guide, then navigate and receive an a11y snapshot.
npx chrome-agent --help
chrome-agent goto https://example.com --inspect

# Act on a returned UID and immediately inspect the next state.
chrome-agent click n12 --inspect

# Extract content without writing a selector.
chrome-agent read
chrome-agent extract

# Obtain structured output when another program or agent consumes it.
chrome-agent --json inspect --urls --filter link
```

For a real application, use `inspect` to get current UIDs, fill or select by UID, wait for an observable condition instead of sleeping, then inspect again. UIDs remain useful while their underlying DOM node exists, but a navigation or re-render can invalidate them.

## Effective Use Cases
<table>
  <thead>
    <tr><th>Situation</th><th>Useful approach</th><th>Why this tool fits</th></tr>
  </thead>
  <tbody>
    <tr><td>LLM-driven browsing where context size matters</td><td>Use <code>goto ... --inspect</code>, then operate on compact a11y UIDs.</td><td>The project is designed to reduce page-state tokens and avoid hand-authored selectors for ordinary interactions.</td></tr>
    <tr><td>Repeated list, feed, card, or table extraction</td><td>Start with <code>extract</code>; for React-style pages, use <code>extract --a11y --scroll --limit N</code>.</td><td>The CLI provides built-in repeated-content extraction before requiring site-specific scripts.</td></tr>
    <tr><td>Readable article capture</td><td>Use <code>read</code>, then scope or cap output with <code>text</code> when needed.</td><td>Its Readability-based command is a concise alternative to inspecting an entire application DOM.</td></tr>
    <tr><td>Fast interaction loops</td><td>Add <code>--inspect</code> to actions; use <code>batch</code> or <code>pipe</code> for a sequence of commands.</td><td>It combines state observation with actions and can avoid repeated process startup.</td></tr>
    <tr><td>UI and API debugging</td><td>Use <code>console --level error</code>, <code>network --filter</code>, and <code>wait network-idle</code>.</td><td>The CLI exposes browser-visible errors, requests, and an observable readiness condition.</td></tr>
  </tbody>
</table>

## Operating Tricks And Guardrails
- Start with `inspect --urls --filter link` when choosing among links: visible labels alone may not identify their destination.
- Use `diff` after an action when a full snapshot would be noisy; use `--max-chars`, `--offset`, and `--truncate` to bound context returned to an agent.
- Prefer `wait network-idle` or a targeted `wait` condition to a fixed delay on SPA and XHR-heavy applications.
- Scope screenshots to a UID or selector and use JPEG quality/width controls when visual evidence is needed without filling the agent context with a large image.
- Use named `--browser` and `--page` values to separate concurrent tasks; do not assume the default browser/session is appropriate for unrelated work.
- Keep logged-in and personal data workflows authorized and minimal. This project documents cookie-copy and anti-detection features, but their availability does not authorize access, bypass controls, or bulk collection.

## Comparison Context
The scheduled [[chrome-agent]] is Corey's Python CDP CLI at `captivus/chrome-agent`. This project is a separate Rust implementation at `sderosiaux/chrome-agent`; neither repository establishes facts about the other's author, release line, or World's Fair session. [[chrome-agent-implementation-delta|The implementation delta]] records the distinction.

## Connections
- [[chrome-agent]]
- [[chrome-agent-implementation-delta]]
## Sources
- [sderosiaux/chrome-agent repository](https://github.com/sderosiaux/chrome-agent)

## Evidence Boundary
No official World's Fair schedule, speaker record, event recording, transcript, slide, or official AI Engineer source connects this repository to Corey Gallon or to the 2026 event. This page is supporting external comparison context from the project's public GitHub repository only, not first-class AIE evidence.
