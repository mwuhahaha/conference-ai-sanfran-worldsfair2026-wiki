---
title: "Highlighted Concepts, People, And Talks"
category: "highlights"
sourceLabels: ["Highlight registry", "Wiki navigation"]
---

# Highlighted Concepts, People, And Talks

This is the operator-facing highlight map for targets that deserve more synthesis than ordinary generated pages. Concepts are included when a talk introduces a reusable method, hack, design pattern, or unusually sharp framing that should be tracked across the wiki.

## Concepts And Topics
- [[highlight-reachability-over-format|Reachability Over Format]] — critical — [[reachability-over-format|Reachability Over Format]]
  - A clever agent-readiness finding from Liad/ORA: the format of agent files matters less than whether agents can actually discover and reach them from trusted surfaces.
- [[highlight-agent-ready-accessibility|Agent-Ready Accessibility]] — high — [[agent-ready-accessibility|Agent-Ready Accessibility]]
  - The talk frames agent-readiness and accessibility as the same engineering problem: reachable, understandable, operable state for non-human and human intermediaries.
- [[highlight-agentic-web|Agentic Web]] — high — [[agentic-web|Agentic Web]]
  - Agentic Web is an organizing theme tying ORA, MCP Apps, browser automation, search, catalogs, and computer-use talks together.
- [[highlight-mcp-app-runtime|MCP Apps as Agentic App Runtime]] — high — [[mcp-app-runtime|MCP Apps as Agentic App Runtime]]
  - MCP Apps is a concrete method for returning interactive UI from tool servers so agents and humans can share richer app surfaces inside MCP hosts.
- [[highlight-nearly-headless-web|Nearly Headless Web]] — high — [[nearly-headless-web|Nearly Headless Web]]
  - A useful product/design frame from Liad's talk: the web becomes mostly machine-operable while preserving human-visible moments for judgment and handoff.

## People
- [[highlight-liad-yosef|Liad Yosef]] — critical — [[liad-yosef|Liad Yosef]]
  - Liad anchors the agentic-web and MCP Apps threads: agent readiness, nearly-headless web design, MCP UI/MCP Apps, and ORA's research on how real agents use sites.
- [[highlight-corey-gallon|Corey Gallon]] — high — [[corey-gallon|Corey Gallon]]
  - Corey anchors the browser automation thread and connects practical AI-native company operations to agentic web execution.

## Talks
- [[highlight-rebuilding-web-for-agents|Rebuilding the Web for Agents]] — critical — [[2026-06-29-liad-yosef-rebuilding-the-web-for-agents|Rebuilding the web for agents]]
  - This talk turns agentic web from a protocol checklist into an evidence-backed operating problem: discovery, understanding, authentication, action, and human handoff.
- [[highlight-dark-arts-web-automation|The Dark Arts of Web Automation]] — critical — [[2026-06-30-corey-gallon-the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans|The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans]]
  - Favorite and critical talk: it turns browser agents from expensive step-by-step browsing into repeatable, scriptable CDP-based automation.
- [[highlight-mcp-apps-extending-frontier|MCP Apps - Extending the Frontier]] — high — [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier|MCP Apps - Extending the frontier]]
  - This talk is a schedule anchor for MCP Apps as an agentic app runtime and for interactive UI inside MCP hosts.

## Companies And Resources
- [[highlight-shipping-production-ai-government|Shipping Production AI Inside Government]] — critical — [[youtube-qlHaO6laBlM|Shipping Production AI Inside Government — William Tarr, Ministry of Justice (DO NOT PUBLISH)]]
  - This recording is unusually concrete on production AI inside government: forward-deployed engineers, prisons/probation, frontline trust, offline constraints, procurement friction, and real rollout lessons.
- [[highlight-ora-agentic-web|ORA]] — high — [[ora|ORA]]
  - ORA is central to the agentic-web theme through Liad Yosef and public agent-readiness research.

## How To Add A Highlight
- Add a target to `raw/sources/highlighted-targets.json`.
- Use `targetType` to group it as a concept/topic, person, talk, company, tool, or resource.
- Run `python3 scripts/generate_highlights.py`.
- Expand the target page itself with evidence, transcript/source status, related concepts, people, companies, and an evidence boundary.
