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
| Dimension | Corey Gallon's project | sderosiaux project |
|---|---|---|
| Repository | `captivus/chrome-agent` | `sderosiaux/chrome-agent` |
| Implementation | Python CLI | Rust CLI |
| World's Fair connection | Supporting implementation context for Corey's scheduled session | None established |
| Appropriate role in this wiki | Tool page tied to the official schedule | External alternative and comparison context |

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
