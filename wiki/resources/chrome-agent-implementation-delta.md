---
title: "chrome-agent Implementation Delta"
category: "resources"
sourceLabels: ["Official conference schedule", "Public GitHub repositories", "PyPI package", "Supporting comparison context"]
status: "correction and comparison"
---

# chrome-agent Implementation Delta

## Purpose
Two unrelated public projects use the name `chrome-agent`. This page separates their identities after a third-party validation error matched the Rust repository to Corey Gallon's scheduled World's Fair tool. The correction keeps the event record precise while preserving the other project as optional technical comparison context.

## Corey Gallon's chrome-agent
The project connected to Corey's scheduled session is [captivus/chrome-agent](https://github.com/captivus/chrome-agent), a Python CLI distributed as [chrome-agent on PyPI](https://pypi.org/project/chrome-agent/). It exposes direct Chrome DevTools Protocol access for browser launch, status, navigation, JavaScript evaluation, screenshots, protocol help, and event subscriptions. The official schedule connects Corey and this tool to [[2026-06-30-corey-gallon-the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans|The Dark Arts of Web Automation]].

## sderosiaux/chrome-agent
[[sderosiaux-chrome-agent|sderosiaux/chrome-agent]] is a separate Rust project. Its public repository presents an agent-oriented CDP workflow built around compact accessibility snapshots, stable backend node identifiers, actions, inspection, and content extraction. Its similar name and browser-agent focus do not make it Corey Gallon's work or event evidence.

## Practical Difference
<table>
  <thead>
    <tr><th>Dimension</th><th>Corey Gallon's project</th><th>sderosiaux project</th></tr>
  </thead>
  <tbody>
    <tr><td>Repository and package</td><td><code>captivus/chrome-agent</code>; Python package on PyPI</td><td><code>sderosiaux/chrome-agent</code>; Rust crate and npm package</td></tr>
    <tr><td>Core operating model</td><td>Name a running Chrome instance, send any CDP <code>Domain.method</code>, or hold an event subscription with <code>attach</code>.</td><td>Use an agent-oriented command vocabulary such as <code>inspect</code>, <code>click</code>, <code>read</code>, and <code>extract</code> over CDP.</td></tr>
    <tr><td>Page-state representation</td><td>Raw CDP results selected by the caller: DOM, Runtime, Network, Page, Input, and other live protocol domains.</td><td>Compact accessibility snapshots with stable backend-node-derived UIDs, plus targeted visible-text and extraction commands.</td></tr>
    <tr><td>Best fit</td><td>Protocol-level debugging, event observation, exact Chrome capability access, and workflows where the operator chooses the CDP primitive.</td><td>Agent navigation and extraction loops where compact state, direct UIDs, and built-in content commands reduce prompt/context overhead.</td></tr>
    <tr><td>Interaction pattern</td><td>One-shot commands for spot work; persistent <code>attach</code> streams for event observation; optional Python API for in-process control.</td><td><code>--inspect</code> returns state with an action; <code>batch</code> and <code>pipe</code> serve multi-command flows.</td></tr>
    <tr><td>When not to choose it first</td><td>When an agent needs a small, opinionated page representation rather than direct protocol knowledge.</td><td>When debugging depends on arbitrary/new CDP methods or a custom event subscription model not covered by its higher-level commands.</td></tr>
    <tr><td>World's Fair connection</td><td>Supporting implementation context for Corey's scheduled session.</td><td>None established.</td></tr>
    <tr><td>Appropriate role in this wiki</td><td>Tool page tied to the official schedule, with repository implementation context clearly labeled.</td><td>External alternative and comparison context only.</td></tr>
  </tbody>
</table>

## Selection Guide
<table>
  <thead>
    <tr><th>Need</th><th>Prefer</th><th>Reason</th></tr>
  </thead>
  <tbody>
    <tr><td>Call a CDP method that landed after a CLI release or is absent from a curated wrapper</td><td>[[chrome-agent|Corey Gallon's chrome-agent]]</td><td>It forwards the method and parameters to the running browser, and its live <code>help</code> reads that browser's schema.</td></tr>
    <tr><td>Observe selected navigation or network events while another actor uses the same browser</td><td>[[chrome-agent|Corey Gallon's chrome-agent]]</td><td>Its persistent <code>attach</code> model provides isolated event subscriptions.</td></tr>
    <tr><td>Give an LLM a small actionable snapshot of a normal web page</td><td>[[sderosiaux-chrome-agent|sderosiaux/chrome-agent]]</td><td>Its a11y UID model and <code>--inspect</code> action loop are designed for compact agent-facing page state.</td></tr>
    <tr><td>Extract an article, a repeating feed, or a card/table collection before writing selectors</td><td>[[sderosiaux-chrome-agent|sderosiaux/chrome-agent]]</td><td>It supplies <code>read</code> and <code>extract</code> commands for those common shapes.</td></tr>
    <tr><td>Investigate a complicated browser bug with DOM, runtime, input, protocol, and network tools chosen case by case</td><td>[[chrome-agent|Corey Gallon's chrome-agent]]</td><td>The lower-level CDP-first model leaves the diagnostic method under the operator's control.</td></tr>
  </tbody>
</table>

These are implementation-level selection inferences from the two public repositories, not claims made by the World's Fair program or evidence about the scheduled talk.

## Discovery And Source Boundary
The Rust repository entered the research path because an earlier third-party validation matched a shared project name without confirming the repository owner. This page records that error explicitly so it is not repeated. The official schedule is canonical for the session, speaker, and conference association; the GitHub repositories and PyPI package support implementation comparison only. No AIE source establishes a relationship between `sderosiaux/chrome-agent`, Corey Gallon, or the event.

## Related Pages
- [[chrome-agent]]
- [[sderosiaux-chrome-agent]]
- [[source-boundary]]

## Public Sources
- [Corey Gallon's chrome-agent repository](https://github.com/captivus/chrome-agent)
- [chrome-agent PyPI package](https://pypi.org/project/chrome-agent/)
- [sderosiaux/chrome-agent repository](https://github.com/sderosiaux/chrome-agent)
