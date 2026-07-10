---
title: "Agentic Web"
category: "topics"
sourceLabels: ["Official conference schedule", "Public YouTube metadata", "YouTube transcript evidence", "Local slide OCR", "Topic synthesis"]
---
# Agentic Web

Agentic Web is the conference theme around making the public web usable by AI agents as an action surface, retrieval surface, interface layer, and data substrate. In this wiki it is a topic, not a standalone section: it connects scheduled talks, people, companies, videos, transcripts, slide evidence, and adjacent concepts such as agentic search, browser agents, MCP, sandboxes, catalogs, and agent-facing HTML.

A practical definition: the Agentic Web is what exists when an agent can discover a relevant web resource, understand the page or catalog well enough to choose an action, operate safely through the available interface, verify the result, and leave enough evidence for a human or system to audit what happened.

## Conference Context
The World's Fair schedule frames this as a multi-track theme rather than a single product category. Search talks emphasize finding the right live web context. Browser and computer-use talks emphasize operating existing websites. Catalog and HTML talks emphasize making web surfaces more legible to agents. MCP and sandbox talks add tool contracts and execution boundaries around those actions.

## Significance
The web was built primarily for people reading pages and clicking controls. Agents now need to search, compare, fill forms, inspect docs, use dashboards, purchase, schedule, and operate across services that may not expose clean APIs. That turns web pages, search engines, catalogs, HTML, screenshots, DOM trees, browser sandboxes, and identity controls into infrastructure for AI engineering.

For builders, this changes the product surface. A site is no longer only a human UX; it can become an agent-readable contract. A search index is no longer just a ranked list for people; it can become a planning substrate. A browser is no longer just a rendering engine; it becomes an execution environment with credentials, permissions, safety boundaries, and observability requirements.

## Technical Model
- Search and retrieval layer: agents need current, source-grounded discovery across web pages, docs, catalogs, and product data before they can reason or act.
- Representation layer: the agent must see the web through some mix of HTML, DOM, markdown, screenshots, accessibility trees, structured feeds, or agent-readable catalogs.
- Action layer: browser automation, computer-use models, MCP tools, APIs, and form workflows turn understanding into clicks, text entry, navigation, and transactions.
- Safety and identity layer: credentials, payment authority, user intent, rate limits, sandboxing, and audit trails decide what the agent is allowed to do.
- Verification layer: transcripts, screenshots, traces, browser events, retrieved sources, and result checks are needed so actions can be reviewed and failures can be corrected.

## Applied Use
Use Agentic Web patterns when the work depends on public or semi-public web context, when the target service does not expose a sufficient API, when a human workflow must be automated through an existing UI, when agents need current facts beyond a private corpus, or when products want to be discoverable and usable by agents. Prefer direct APIs or MCP tools when the action is high-risk, repetitive, privileged, or available through a more stable machine interface.

The pattern is most useful for research agents, shopping and catalog agents, browser-based operations, competitive intelligence, lead and company research, support workflows, data extraction, web-grounded coding assistants, documentation agents, and products that want AI systems to evaluate or recommend them. It is also relevant to agentic commerce, where identity, authority, and settlement become part of the web contract rather than an afterthought.

## Design Patterns
- Agent-readable catalogs: expose structured product, documentation, pricing, capability, or availability data so agents do not have to infer everything from visual pages.
- Browser execution sandboxes: isolate web actions, credentials, screenshots, downloads, and traces so agent browsing can be observed and constrained.
- Dual human/agent pages: keep the human page usable, but include enough semantic structure, stable labels, and machine-readable metadata for agents to act reliably.
- Retrieval before action: require the agent to cite or log the page, catalog, or transcript evidence it used before taking a consequential web action.
- Representation fallback: try structured sources first, then HTML or accessibility trees, then screenshots/OCR when the page is only visually understandable.
- Post-action verification: check page state, confirmation messages, generated artifacts, or external records after the action instead of trusting the click path.

## Risks And Failure Modes
- Visual ambiguity: screenshots can miss hidden state, modals, disabled controls, or off-screen context.
- DOM overload: raw page structure can be too large or noisy for models without summarization and filtering.
- Stale retrieval: search results and cached pages may lag the current site state.
- Authority confusion: an agent may not know whether it is allowed to submit, purchase, message, or change settings.
- Prompt injection: pages and documents can include attacker-controlled instructions that target the agent rather than the human reader.
- Fragile automation: selectors, layouts, bot defenses, and login flows can break browser agents even when the human workflow still works.

## Open Questions
- Which agent-facing web contract wins: richer HTML, MCP servers, APIs, catalog feeds, browser-use conventions, or a mix of all of them?
- How should websites declare which actions are safe for an agent to perform and which require explicit human confirmation?
- What is the right default representation for an agent: DOM, accessibility tree, markdown, screenshot, structured catalog, or task-specific extraction?
- How should products measure agent experience separately from human UX?
- What evidence should a browser agent preserve so that a user, auditor, or downstream system can trust the result?

## Connections
### Search, Catalogs, And Web Data
- [[2026-06-29-will-bryk-the-search-engine-for-the-agentic-web]] - The Search Engine for the Agentic Web (2026-06-29, 11:40am-12:00pm; Search & Retrieval / Track 3; Will Bryk)
- [[2026-06-29-yohan-raju-building-ai-agents-with-real-time-web-data]] - Building AI Agents with Real-Time Web Data (2026-06-29, 12:10pm-1:10pm; Track 8 / Track 8; Yohan Raju)
- [[2026-06-30-nixon-dinh-the-death-of-keyword-search-and-the-rise-of-agent-readable-catalogs]] - The Death of Keyword Search and the Rise of Agent-Readable Catalogs (2026-06-30, 11:10am-11:30am; Expo Stage 3 / Expo Stage 3 SW; Nixon Dinh)
- [[2026-06-30-patricija-emaityt-how-web-data-infrastructure-powers-the-next-generation-of-ai]] - How Web Data Infrastructure Powers the Next Generation of AI (2026-06-30, 3:20pm-3:40pm; Computer Use / Track 7; Patricija Žemaitytė)

### Browser And Computer-Use Web
- [[2026-06-29-derek-meegan-deploying-browser-agents-at-scale]] - Deploying browser agents at scale (2026-06-29, 1:55pm-2:15pm; track TBD / Expo Stage 4 SE; Derek Meegan)
- [[2026-06-30-dhruv-batra-computer-use-models-will-agentify-the-web-not-apis]] - Computer-use models will agentify the web, not APIs (2026-06-30, 10:45am-11:05am; Computer Use / Track 7; Dhruv Batra)
- [[2026-06-30-paul-klein-iv-bringing-agents-onto-the-world-wide-web]] - Bringing agents onto the world wide web (2026-06-30, 11:40am-12:00pm; Computer Use / Track 7; Paul Klein IV)
- [[2026-06-30-corey-gallon-the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans]] - The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans (2026-06-30, 12:05pm-12:25pm; Computer Use / Track 7; Corey Gallon)

### Agent-Facing Interfaces And Web Substrates
- [[2026-06-29-liad-yosef-rebuilding-the-web-for-agents]] - Rebuilding the web for agents (2026-06-29, 12:05pm-12:25pm; Search & Retrieval / Track 3; Liad Yosef)
- [[2026-07-01-james-russo-html-is-all-agents-need]] - HTML Is All Agents Need (2026-07-01, 11:10am-11:30am; Generative Media / Track 1; James Russo)

- [[talk-video-transcript-map]] - Talk/video/transcript relation map.
- [[youtube-xnXqpUW_Kp8]] - Will Bryk related YouTube evidence.
- [[youtube-o-zkvb0iFDQ]] - Liad Yosef related YouTube evidence.
- [[youtube-YRGjll7uu5w]] - Paul Klein IV related YouTube evidence.
- [[youtube-JsKTQbT58BY]] - Corey Gallon related YouTube evidence.
- [[slide-library]] - Extracted slide library.
- [[reconstructed-slide-library]] - Reconstructed slide library.
- [[dense-slide-library]] - Dense slide library.
- [[worldsfair-2026-livestreams]] - World's Fair livestream source page.
- [[youtube-JnubYCYunk8-slides]] - slide evidence for an Agentic Web-adjacent related video.
- [[youtube-YRGjll7uu5w-slides]] - slide evidence for an Agentic Web-adjacent related video.
- [[youtube-o-zkvb0iFDQ-slides]] - slide evidence for an Agentic Web-adjacent related video.
- [[youtube-xnXqpUW_Kp8-slides]] - slide evidence for an Agentic Web-adjacent related video.
- `raw/sources/youtube-transcripts/JnubYCYunk8.txt` - transcript evidence on browser-agent representation tradeoffs, including DOM, screenshot, and markdown views.

- [[agentic-search]]
- [[ai-sandboxes]]
- [[mcp]]
- [[agent-security]]
- [[coding-agents]]
- [[agent-evaluations]]
- [[inference-engineering]]

- [[will-bryk]]
- [[liad-yosef]]
- [[yohan-raju]]
- [[derek-meegan]]
- [[dhruv-batra]]
- [[nixon-dinh]]
- [[paul-klein-iv]]
- [[corey-gallon]]
- [[patricija-emaityt]]
- [[james-russo]]
- [[ido-salomon]]
- [[shubhankar-srivastava]]

- [[exa]]
- [[ora]]
- [[browserbase]]
- [[bright-data]]
- [[mcp-apps]]
- [[chrome-agent]]

- [[highlight-dark-arts-web-automation]] - critical highlighted talk on CDP-first browser automation.
- [[highlight-ora-agentic-web]] - highlighted company/research path for ORA and agent readiness.

## Evidence Graph
This evidence graph consolidates scheduled talks, linked videos, transcripts, and slide-derived material connected to this topic.

### Linked Sessions
- [[2026-06-29-will-bryk-the-search-engine-for-the-agentic-web|The Search Engine for the Agentic Web]]
- [[2026-06-29-yohan-raju-building-ai-agents-with-real-time-web-data|Building AI Agents with Real-Time Web Data]]
- [[2026-06-30-nixon-dinh-the-death-of-keyword-search-and-the-rise-of-agent-readable-catalogs|The Death of Keyword Search and the Rise of Agent-Readable Catalogs]]
- [[2026-06-30-patricija-emaityt-how-web-data-infrastructure-powers-the-next-generation-of-ai|How Web Data Infrastructure Powers the Next Generation of AI]]
- [[2026-06-29-derek-meegan-deploying-browser-agents-at-scale|Deploying browser agents at scale]]
- [[2026-06-30-dhruv-batra-computer-use-models-will-agentify-the-web-not-apis|Computer-use models will agentify the web, not APIs]]
- [[2026-06-30-paul-klein-iv-bringing-agents-onto-the-world-wide-web|Bringing agents onto the world wide web]]
- [[2026-06-30-corey-gallon-the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans|The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans]]
- [[2026-06-29-liad-yosef-rebuilding-the-web-for-agents|Rebuilding the web for agents]]
- [[2026-07-01-james-russo-html-is-all-agents-need|HTML Is All Agents Need]]

### Media Signals
- `youtube-xnXqpUW_Kp8` — 5 slide-derived text signals
- Slide-derived themes for `youtube-xnXqpUW_Kp8`: humans, built, information, traditional, search, engines, type, simple.
- Evidence links for `youtube-xnXqpUW_Kp8`: [[youtube-xnXqpUW_Kp8]], [[youtube-xnXqpUW_Kp8-slides]], [[youtube-xnXqpUW_Kp8-dense-slides]], [[youtube-xnXqpUW_Kp8-reconstructed-slides]]
- `youtube-YRGjll7uu5w` — 3 slide-derived text signals
- Slide-derived themes for `youtube-YRGjll7uu5w`: most, benchmarks, fake, news, model, performance, tasks, vary.
- Evidence links for `youtube-YRGjll7uu5w`: [[youtube-YRGjll7uu5w]], [[youtube-YRGjll7uu5w-slides]], [[youtube-YRGjll7uu5w-dense-slides]], [[youtube-YRGjll7uu5w-reconstructed-slides]]
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

## Evidence Boundary
Official schedule data is canonical for talk titles, speakers, dates, tracks, rooms, and inclusion in the schedule anchor list. YouTube videos, transcripts, local Whisper output, OCR, and reconstructed slide crops are supporting evidence. Treat transcript and OCR-derived claims as reviewable evidence, and verify important slide claims against the embedded slide image or reconstructed crop when available.
