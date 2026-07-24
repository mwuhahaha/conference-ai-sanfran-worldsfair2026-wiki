---
title: "Agentic Web"
category: "topics"
sourceLabels: ["Official conference schedule", "Public YouTube metadata", "YouTube transcript evidence", "Local slide OCR", "Topic synthesis"]
sourceAssessment:
  schemaVersion: 1
  claimId: claim:9f0de2efc095323effa785b6c11aac4b8819f81d12c60cdfb33cd90a869cae79
  subjectId: concept:agentic-web
  domain: topics page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-24T00:00:00.000000Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-official-sessions
  - source:official-wf26-youtube-2JX6JYyQG4Y
  - source:official-wf26-youtube-Cz4v1WHVyZc
  - source:official-wf26-youtube-ZSQb5fzRFPw
  - source:official-wf26-youtube-pMggiOb18tc
sourceAssessmentBodySha256: sha256:499cd0aa08bb25445911ccd92b6dc7c2693fa5e6cbee4a81303ec5f3f5307a95
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

## Transcript Digest Evidence
This section synthesizes 2 evidence-bound talk topic candidates across at least two talks.

### Cross-Talk Synthesis
Web workflows where agents act through web-native or non-screen inputs instead of relying on traditional manual interaction. The distinction is between media generation and workflow control, but both treat the web as an active execution substrate rather than a passive display layer.

### Constituent Talk Evidence
- [[2026-06-30-antje-barth-perception-agents|Perception Agents]] — Using non-screen inputs, such as meeting transcripts, to drive changes in the same workflow.
  - Transcript: [[youtube-2JX6JYyQG4Y-transcript]]
  - Evidence: "So we had the discussion the be did the transcript and you can see here on the right we're pulling this meeting transcript right in there is a whole detailed summary of the meeting."
- [[2026-07-01-james-russo-html-is-all-agents-need|HTML Is All Agents Need]] — Using HTML, CSS, and JavaScript as the interface for agent-generated video.
  - Transcript: [[youtube-Cz4v1WHVyZc-transcript]]
  - Evidence: "Our bet is on HTML. HTML, CSS, and JavaScript are the native languages of LLMs. Most of their training data, every webpage that gets scraped at the end of day is essentially just HTML, CSS, and JavaScript under the hood."

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

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 22 | Related pages outside the main evidence categories. |
| resources | 13 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 23 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 11 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 5 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 9 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-will-bryk-the-search-engine-for-the-agentic-web]]
- [[2026-06-29-yohan-raju-building-ai-agents-with-real-time-web-data]]
- [[2026-06-30-nixon-dinh-the-death-of-keyword-search-and-the-rise-of-agent-readable-catalogs]]
- [[2026-06-30-patricija-emaityt-how-web-data-infrastructure-powers-the-next-generation-of-ai]]
- [[2026-06-29-derek-meegan-deploying-browser-agents-at-scale]]
- [[2026-06-30-dhruv-batra-computer-use-models-will-agentify-the-web-not-apis]]

### Resources
- [[talk-video-transcript-map]]
- [[youtube-xnXqpUW_Kp8]]
- [[youtube-o-zkvb0iFDQ]]
- [[youtube-YRGjll7uu5w]]
- [[youtube-JsKTQbT58BY]]
- [[worldsfair-2026-livestreams]]

### Slides
- [[slide-library]]
- [[reconstructed-slide-library]]
- [[dense-slide-library]]
- [[youtube-JnubYCYunk8-slides]]
- [[youtube-YRGjll7uu5w-slides]]
- [[youtube-o-zkvb0iFDQ-slides]]

### Transcripts
- [[youtube-4sX_He5c4sI-transcript]]
- [[youtube-htM02KMNZnk-transcript]]
- [[youtube-2JX6JYyQG4Y-transcript]]
- [[youtube-ZSQb5fzRFPw-transcript]]
- [[youtube-pMggiOb18tc-transcript]]
- [[youtube-Ib5GBkD555M-transcript]]

### Tools
- [[mcp]]
- [[exa]]
- [[browserbase]]
- [[mcp-apps]]
- [[chrome-agent]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.

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
- `youtube-4sX_He5c4sI` — 82,600 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-4sX_He5c4sI`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-4sX_He5c4sI`: model, code, models, research, system, well, first, better.
- Slide-derived themes for `youtube-4sX_He5c4sI`: lots, examples, stream, starts, july, land, king, chief.
- Evidence links for `youtube-4sX_He5c4sI` (primary event evidence): [[youtube-4sX_He5c4sI]], [[youtube-4sX_He5c4sI-transcript]], [[youtube-4sX_He5c4sI-slides]], [[youtube-4sX_He5c4sI-dense-slides]], [[youtube-4sX_He5c4sI-reconstructed-slides]]
- `youtube-htM02KMNZnk` — 89,050 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-htM02KMNZnk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-htM02KMNZnk`: model, code, models, loop, well, software, first, team.
- Slide-derived themes for `youtube-htM02KMNZnk`: apps, github, copilot, welcome, engineer, fair, single, line.
- Evidence links for `youtube-htM02KMNZnk` (primary event evidence): [[youtube-htM02KMNZnk]], [[youtube-htM02KMNZnk-transcript]], [[youtube-htM02KMNZnk-slides]], [[youtube-htM02KMNZnk-dense-slides]], [[youtube-htM02KMNZnk-reconstructed-slides]]
- `youtube-2JX6JYyQG4Y` — 2,870 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-2JX6JYyQG4Y`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-2JX6JYyQG4Y`: screen, still, first, maybe, check, meeting, click, part.
- Slide-derived themes for `youtube-2JX6JYyQG4Y`: amazon, easy, part, clicking, tool, still, figure, ease.
- Evidence links for `youtube-2JX6JYyQG4Y` (primary event evidence): [[youtube-2JX6JYyQG4Y]], [[youtube-2JX6JYyQG4Y-transcript]], [[youtube-2JX6JYyQG4Y-slides]]
- `youtube-ZSQb5fzRFPw` — 2,617 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-ZSQb5fzRFPw`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-ZSQb5fzRFPw`: computer, take, over, driver, background, task, might, sandbox.
- Slide-derived themes for `youtube-ZSQb5fzRFPw`: track, july, fair, computer, operator, loop, wired, model.
- Evidence links for `youtube-ZSQb5fzRFPw` (primary event evidence): [[youtube-ZSQb5fzRFPw]], [[youtube-ZSQb5fzRFPw-transcript]], [[youtube-ZSQb5fzRFPw-slides]]
- `youtube-pMggiOb18tc` — 4,606 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-pMggiOb18tc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-pMggiOb18tc`: models, codex, open, model, should, engineering, well, even.
- Slide-derived themes for `youtube-pMggiOb18tc`: codex, software, engineers, computer, plugins, lifetime, career, left.
- Evidence links for `youtube-pMggiOb18tc` (primary event evidence): [[youtube-pMggiOb18tc]], [[youtube-pMggiOb18tc-transcript]], [[youtube-pMggiOb18tc-slides]]
- `youtube-Ib5GBkD555M` — 4,045 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Ib5GBkD555M`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Ib5GBkD555M`: code, review, model, coding, software, stuff, test, better.
- Slide-derived themes for `youtube-Ib5GBkD555M`: software, harness, enough, team, engineering, factories, fail, pierre.
- Evidence links for `youtube-Ib5GBkD555M` (primary event evidence): [[youtube-Ib5GBkD555M]], [[youtube-Ib5GBkD555M-transcript]], [[youtube-Ib5GBkD555M-slides]]
- `youtube-YRGjll7uu5w` — 8 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-YRGjll7uu5w`: playwright, automation, stagehand, february, date, march, april, take.
- Evidence links for `youtube-YRGjll7uu5w` (supporting context only): [[youtube-YRGjll7uu5w]], [[youtube-YRGjll7uu5w-slides]], [[youtube-YRGjll7uu5w-dense-slides]], [[youtube-YRGjll7uu5w-reconstructed-slides]]
- `youtube-o-zkvb0iFDQ` — 3,969 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-o-zkvb0iFDQ`: apps, host, claude, back, chatgpt, look, mcpui, chat.
- Slide-derived themes for `youtube-o-zkvb0iFDQ`: apps, maintainer, labs, used, text, community, easy, adoption.
- Evidence links for `youtube-o-zkvb0iFDQ` (supporting context only): [[youtube-o-zkvb0iFDQ]], [[youtube-o-zkvb0iFDQ-transcript]], [[youtube-o-zkvb0iFDQ-slides]], [[youtube-o-zkvb0iFDQ-dense-slides]], [[youtube-o-zkvb0iFDQ-reconstructed-slides]]
- `youtube-JnubYCYunk8` — 937 transcript words; 4 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-JnubYCYunk8`: browser, screenshot, give, click, website, been, took, maybe.
- Slide-derived themes for `youtube-JnubYCYunk8`: today, trying, navigate, browser, challenge.
- Evidence links for `youtube-JnubYCYunk8` (supporting context only): [[youtube-JnubYCYunk8]], [[youtube-JnubYCYunk8-transcript]], [[youtube-JnubYCYunk8-slides]]
- `youtube-xnXqpUW_Kp8` — 8 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-xnXqpUW_Kp8`: built, humans, queries, biden, information, traditional, search, engines.
- Evidence links for `youtube-xnXqpUW_Kp8` (supporting context only): [[youtube-xnXqpUW_Kp8]], [[youtube-xnXqpUW_Kp8-slides]], [[youtube-xnXqpUW_Kp8-dense-slides]], [[youtube-xnXqpUW_Kp8-reconstructed-slides]]
- `youtube-JsKTQbT58BY` — source page linked; role: supporting context only.
- Evidence links for `youtube-JsKTQbT58BY` (supporting context only): [[youtube-JsKTQbT58BY]]
## Evidence Boundary
Official schedule data is canonical for talk titles, speakers, dates, tracks, rooms, and inclusion in the schedule anchor list. YouTube videos, transcripts, local Whisper output, OCR, and reconstructed slide crops are supporting evidence. Treat transcript and OCR-derived claims as reviewable evidence, and verify important slide claims against the embedded slide image or reconstructed crop when available.
