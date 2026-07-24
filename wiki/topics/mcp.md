---
title: Model Context Protocol
category: topics
sourceLabels:
  - Slide/video-derived supporting context
last_auto_summarized: '2026-07-18T13:16:05.013Z'
sourceAssessment:
  schemaVersion: 1
  claimId: claim:e279dee65ddf7dcb7ca408f31e224119075825168aea46cff0cdbd116cd45b17
  subjectId: concept:mcp
  domain: topics page evidence coverage
  intendedUse: attributed_context
  asOf: '2026-07-24T00:00:00.000000Z'
  state: limited
  basis: official_primary_canonical
  message: This page is limited to source-attributed facts; independent support for broader claims may be limited.
  publicSourceIds:
  - source:official-wf26-youtube--I5W5QVAT8E
  - source:official-wf26-youtube-1EZdpEhwmNc
  - source:official-wf26-youtube-9fubhllmsBU
  - source:official-wf26-youtube-JvKO40CFq-s
  - source:official-wf26-youtube-RGSFUqzqErE
  - source:official-wf26-youtube-V-EDrhIhHzQ
  - source:official-wf26-youtube-WkBPX-oDMnA
  - source:official-wf26-youtube-YZQsWVeN3rE
  - source:official-wf26-youtube-c35YoMdnI78
  - source:official-wf26-youtube-pMggiOb18tc
  - source:official-wf26-youtube-q4Tr-DknG2M
sourceAssessmentBodySha256: sha256:7a54116f612e8a13216b60385a9b272d6e7ba020e8a44d687056357e38b42965
---
# Model Context Protocol

## Overview
At AI Engineer World’s Fair 2026, Model Context Protocol (MCP) appears as the operating boundary between agents and the systems they act on, not merely a common tool-call schema. The program follows that boundary from implementation through production governance: Jesse Lumarie covers launching Figma’s MCP server while the product was still evolving; Pedro Lopez explains why Airbyte exposed both an MCP server and a CLI; Mark Lummus and Navinkumar Patil examine interactive CLI design for agents; and Nikita Kothari compares MCPs, CLIs, and skills as distinct tooling layers. Thorsten Hans takes MCP servers to Spin-based edge infrastructure, Cornelia Davis focuses on long-running asynchronous tasks, Jim Clark asks who approves third-party servers, and Sandhya Subramani extends the problem to agents that create their own tools. Jan Curn’s Apify-centered session states the core quality constraint most directly: protocol support does not make an agent effective unless it can discover, select, and correctly use the available capabilities.

MCP Apps are the clearest product-level extension of this architecture. Liad Yosef and Ido Salomon’s verified event recording supplies primary evidence for a dual output contract in which models receive structured tool results while users receive interactive UI. Dustin Mihalik’s adjacent session makes the same division explicit in its title, while Ethan Cha’s dual-surface architecture, Liad Yosef’s agent-ready web session, and Corey Gallon’s web-automation session connect it to a broader effort to serve humans and agents from the same underlying systems. In this model, host behavior, component discovery, inline rendering, iframe isolation, permission handling, and human oversight are part of the integration contract rather than presentation details. Pietro Zullo’s linked MCP Apps recording and slides add supporting context about primitives, hosts, servers, widgets, and software discovery, but remain separate from the verified conference recording and official schedule record.

The connected sessions also show why MCP must be evaluated as part of a complete agent system. Averi Kitsch and Prerna Kakkar distinguish build-time success from runtime reliability; Dan Adler places the tool layer inside enterprise codebases containing millions of lines; OpenAI’s Golden Age of AI Engineering keynote situates tools within evolving software-engineering platforms; and sessions on legacy applications, M365 deployment, dedicated inference, browser operation, and x402 commerce demonstrate how widely the same capability boundary can be deployed. Across those settings, schema validity is only the beginning. A production MCP integration needs concrete capability descriptions, explicit authorization and approval, structured and attributable results, controlled UI isolation, durable handling of asynchronous work, and enough observability for operators to determine which client, server, tool, or agent action produced an outcome.

## Conference Context
MCP emerged from the need to standardize how AI clients discover and call tools, access resources, and integrate with external systems. It sits in the lineage of plugin APIs, language-server style tooling, RPC, browser extensions, and developer-tool protocols.

## Significance
Agents are only as useful as the tools and context they can safely access. MCP reduces one-off integrations, gives tool providers a common surface, and helps clients reason about capabilities, permissions, and interaction patterns.

## Applied Use
Define focused MCP servers with clear tools, schemas, resources, and permission boundaries. Keep tool names concrete, return structured results, test with inspectors, and design for least privilege. For MCP Apps, treat UI and iframe boundaries as part of the security and product contract.

MCP is useful in IDEs, desktop assistants, enterprise data connectors, browser agents, design tools, developer platforms, and internal operations systems.

Use MCP when multiple AI clients need access to the same tools or when a tool provider wants a standard agent-facing integration. For a single narrow app, direct APIs may be simpler until reuse or interoperability matters.

## Active Use Cases
- Connecting agents to repositories, browsers, docs, databases, and SaaS tools.
- MCP Apps that return interactive UI from tool servers.
- Agent-ready web and developer-tool integrations.
- Local inspectors and compliance checks for tool servers.

## Slide-Derived Scheduled Session Signals
- [[2026-06-29-ezra-tanzer-agentic-development-security]] — Agentic Development Security
- [[2026-06-29-sarah-sachs-notion-s-token-town]] — Notion's Token Town

## Slide-Derived Supporting Decks
- [[youtube--I5W5QVAT8E-slides]] — Notion's Token Town — Sarah Sachs, Notion (12 extracted slide frames)
- [[youtube-1EZdpEhwmNc-slides]] — Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk (16 extracted slide frames)
- [[youtube-cgimkNGNjvU-slides]] — Agentic Development Security — Ezra Tanzer, Snyk (18 extracted slide frames)

These decks are slide/OCR support only; keep the article synopsis, origin, use cases, and schedule sections as the primary topic narrative.

## Connections
- [[2026-07-01-jan-curn-mcp-doesn-t-suck-your-agent-does]] — MCP doesn’t suck — your agent does; [[jan-curn|Jan Curn]] (Day 4 — Session Day 3 · 1:55pm-2:15pm · Expo Stage 2 NW; official schedule)
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]] — MCP Apps - Extending the frontier; [[liad-yosef|Liad Yosef]], [[ido-salomon|Ido Salomon]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Context Engineering; related YouTube resource; via [[youtube-o-zkvb0iFDQ]])
- [[2026-06-30-dustin-mihalik-mcp-apps-give-the-model-data-give-the-user-a-ui]] — MCP Apps: Give the Model Data, Give the User a UI; [[dustin-mihalik|Dustin Mihalik]] (Day 3 — Session Day 2 · 2:50pm-3:10pm · Context Engineering; official schedule)
- [[2026-06-30-averi-kitsch-build-time-vs-run-time-why-your-dev-tools-will-fail-in-production]] — Build-Time vs. Run-Time: Why Your Dev Tools Will Fail in Production; [[averi-kitsch|Averi Kitsch]], [[prerna-kakkar|Prerna Kakkar]] (Day 3 — Session Day 2 · 10:45am-11:05am · Context Engineering; official schedule)
- [[2026-06-29-jim-clark-who-approved-that-mcp-server-governing-the-tool-layer]] — Who Approved That MCP Server? Governing the Tool Layer; [[jim-clark|Jim Clark]] (Day 2 — Session Day 1 · 1:55pm-2:15pm · Expo Stage 1 NE; official schedule)
- [[2026-06-29-dan-adler-the-enterprise-agentic-gap-when-developer-level-ai-tools-hit-millions-of-lines]] — The Enterprise Agentic Gap: When Developer-Level AI Tools Hit Millions of Lines; [[dan-adler|Dan Adler]] (Day 2 — Session Day 1 · 10:45am-11:05am · Expo Stage 2 NW; official schedule)
- [[2026-06-29-jesse-lumarie-building-the-engine-while-flying-the-plane-launching-the-figma-mcp-server]] — Building the engine while flying the plane — launching the Figma MCP server; [[jesse-lumarie|Jesse Lumarie]] (Day 2 — Session Day 1 · 11:10am-11:30am · AI-Native Enterprises; official schedule)
- [[2026-06-30-cornelia-davis-mcp-tasks-async-why-the-heck-aren-t-any-agents-supporting-mcp-tasks-async]] — MCP Tasks (async)/ Why the heck aren't any agents supporting MCP tasks/async?; [[cornelia-davis|Cornelia Davis]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Context Engineering; official schedule)
- [[2026-07-01-sandhya-subramani-agents-that-forge-their-own-tools-self-modifying-ai-in-the-wild]] — Agents That Forge Their Own Tools: Self-Modifying AI in the Wild; [[sandhya-subramani|Sandhya Subramani]] (Day 4 — Session Day 3 · 12:05pm-12:25pm · Expo Stage 4 SE; official schedule)
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]] — The Golden Age of AI Engineering; [[alexander-embiricos|Alexander Embiricos]], [[romain-huet|Romain Huet]] (Day 2 — Session Day 1 · 9:25am-9:45am · Software Factories; verified event YouTube resource; via [[youtube-pMggiOb18tc]])
- [[2026-06-29-mark-lummus-burn-your-flags-how-paypal-designs-interactive-cli-tools-for-agents]] — Burn your flags: How PayPal designs interactive CLI tools for agents; [[mark-lummus|Mark Lummus]], [[navinkumar-patil|Navinkumar Patil]] (Day 1 — Workshop Day · 2:20pm-4:20pm · Workshops Day 1; official schedule)
- [[2026-07-01-nikita-kothari-mcps-clis-and-skills-choosing-the-right-tooling-layer-for-agentic-development]] — MCPs, CLIs, and Skills: Choosing the Right Tooling Layer for Agentic Development; [[nikita-kothari|Nikita Kothari]] (Day 4 — Session Day 3 · 11:10am-11:30pm · Agentic Engineering; official schedule)
- [[2026-06-29-ethan-jung-min-cha-dual-surface-architecture-serving-humans-and-agents-from-the-same-tool-layer]] — Dual-Surface Architecture: Serving Humans and Agents from the Same Tool Layer; [[ethan-jung-min-cha|Ethan (Jung Min) Cha]] (Day 2 — Session Day 1 · 1:55pm-2:15pm · Security; official schedule)
- [[2026-06-29-pedro-lopez-how-we-built-the-airbyte-agent-mcp-server-and-cli]] — How We Built the Airbyte Agent MCP Server and CLI; [[pedro-lopez|Pedro Lopez]] (Day 2 — Session Day 1 · 3:45pm-4:05pm · Expo Stage 1; official schedule)
- [[2026-06-30-thorsten-hans-edge-native-ai-building-ultra-fast-agents-and-mcp-servers-with-spin]] — Edge-Native AI: Building Ultra-Fast Agents and MCP Servers with Spin; [[thorsten-hans|Thorsten Hans]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Expo Stage 2; official schedule)
- [[2026-06-29-maria-bledsoe-using-ai-tools-to-teach-old-apps-new-tricks]] — Using AI tools to teach old apps new tricks; [[maria-bledsoe|Maria Bledsoe]] (Day 2 — Session Day 1 · 2:25pm-2:45pm · Track M; official schedule)
- [[2026-07-01-anil-nadiminti-when-ai-agents-pay-and-sellers-monetize-building-x402-apps-for-agentic-commerce-on-aws]] — When AI Agents Pay and Sellers Monetize: Building x402 Apps for Agentic Commerce on AWS; [[anil-nadiminti|Anil Nadiminti]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Agentic Commerce; official schedule)
- [[2026-06-29-merve-noyan-skill-issue-stop-deploying-vision-language-models-use-them-with-skills-to-build-e2e-vision-apps-on-edge]] — Skill issue: stop deploying vision language models, use them with Skills to build e2e vision apps on edge; [[merve-noyan|Merve Noyan]] (Day 2 — Session Day 1 · 11:40am-12:00pm · Vision & OCR; official schedule)
- [[2026-06-29-vasuman-moza-ai-tools-for-forward-deployed-engineering]] — AI tools for Forward Deployed Engineering; [[vasuman-moza|Vasuman Moza]] (Day 2 — Session Day 1 · 11:40am-12:00pm · Forward Deployed Engineering; official schedule)
- [[2026-06-29-will-brown-the-prime-intellect-stack]] — The Prime Intellect Stack; [[will-brown|Will Brown]] (Day 1 — Workshop Day · 4:30pm-5:30pm · Workshops Day 1; verified event YouTube resource; via [[youtube-V-EDrhIhHzQ]])
- [[2026-06-29-pamela-fox-get-started-with-models-in-microsoft-foundry-to-build-ai-apps]] — Get Started with Models in Microsoft Foundry to Build AI Apps; [[pamela-fox|Pamela Fox]] (Day 1 — Workshop Day · 9:00am-10:15am · Track M; official schedule)
- [[2026-06-30-ashu-joshi-deploy-agents-to-users-in-m365-teams-and-apps]] — Deploy agents to users in M365, Teams, and apps; [[ashu-joshi|Ashu Joshi]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Track M; official schedule)
- [[2026-06-29-lee-robinson-recursive-model-improvement]] — Recursive Model Improvement; [[lee-robinson|Lee Robinson]] (Day 2 — Session Day 1 · 5:10pm-5:30pm · Software Factories; verified event YouTube resource; via [[youtube-q4Tr-DknG2M]])
- [[2026-06-30-thariq-shihipar-field-guide-to-fable]] — Field Guide to Fable; [[thariq-shihipar|Thariq Shihipar]] (Day 3 — Session Day 2 · 9:05am-9:25am · Autoresearch; verified event YouTube resource; via [[youtube-9fubhllmsBU]])

- [[john-craft|John Craft]]
- [[pamela-fox|Pamela Fox]]
- [[sandhya-subramani|Sandhya Subramani]]
- [[jason-liu|Jason Liu]]
- [[john-lindquist|John Lindquist]]
- [[liad-yosef|Liad Yosef]]
- [[frank-coyle|Frank Coyle]]
- [[charlie-guo|Charlie Guo]]
- [[merve-noyan|Merve Noyan]]
- [[arun-sekhar|Arun Sekhar]]
- [[elizabeth-fuentes-leone|Elizabeth Fuentes Leone]]
- [[harshul-jain|Harshul Jain]]
- [[tanmay-sah|Tanmay Sah]]
- [[kwindla-kramer|Kwindla Kramer]]
- [[jan-curn|Jan Curn]]
- [[ido-salomon|Ido Salomon]]
- [[dustin-mihalik|Dustin Mihalik]]
- [[averi-kitsch|Averi Kitsch]]
- [[prerna-kakkar|Prerna Kakkar]]
- [[jim-clark|Jim Clark]]
- [[dan-adler|Dan Adler]]
- [[jesse-lumarie|Jesse Lumarie]]
- [[cornelia-davis|Cornelia Davis]]
- [[alexander-embiricos|Alexander Embiricos]]

- [[microsoft|Microsoft]]
- [[openai|OpenAI]]
- [[docker|Docker]]
- [[google|Google]]
- [[amazon-web-services|Amazon Web Services]]
- [[hugging-face|Hugging Face]]
- [[nvidia|NVIDIA]]
- [[mcp-apps|MCP Apps]]
- [[paypal|PayPal]]
- [[towards-ai|Towards AI]]
- [[uber|Uber]]
- [[warp|Warp]]
- [[weights-and-biases-by-coreweave|Weights & Biases by CoreWeave]]
- [[egghead-io|egghead.io]]
- [[sourcegraph|Sourcegraph]]
- [[ucal-berkeley|UCAL Berkeley]]
- [[nubank|Nubank]]
- [[navan|Navan]]

- [[2026-06-30-geoffrey-litt-understanding-is-the-new-bottleneck]] — Understanding is the new bottleneck; [[geoffrey-litt|Geoffrey Litt]] (Day 3 — Session Day 2 · 10:45am-11:05am · Design Engineering; verified event YouTube resource; via [[youtube-WkBPX-oDMnA]])

- [[2026-06-29-liad-yosef-rebuilding-the-web-for-agents]] — Rebuilding the web for agents; [[liad-yosef|Liad Yosef]] (Day 2 — Session Day 1 · 12:05pm-12:25pm · Search & Retrieval; official schedule)

- [[2026-06-30-corey-gallon-the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans]] — The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans; [[corey-gallon|Corey Gallon]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · Computer Use; official schedule)

- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]] — MCP Apps - Extending the frontier; [[liad-yosef|Liad Yosef]], [[ido-salomon|Ido Salomon]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Context Engineering; related YouTube resource; via [[youtube-o-zkvb0iFDQ]])
- [[2026-06-29-kwindla-kramer-the-new-primitives-building-ai-native-software]] — The New Primitives: Building AI-Native Software; [[kwindla-kramer|Kwindla Kramer]] (Day 2 — Session Day 1 · 10:45am-11:05am · Voice & Realtime AI; related YouTube resource; via [[youtube-sAOBXCDiDOs]])
- [[2026-06-29-pedro-lopez-how-we-built-the-airbyte-agent-mcp-server-and-cli]] — How We Built the Airbyte Agent MCP Server and CLI; [[pedro-lopez|Pedro Lopez]] (Day 2 — Session Day 1 · 3:45pm-4:05pm · Expo Stage 1; related YouTube resource; via [[youtube-sAOBXCDiDOs]])
- [[2026-06-30-joseph-wang-emulated-the-data-for-fully-autonomous-software-engineers-and-companies]] — Emulated: The data for fully autonomous software engineers and companies; [[joseph-wang|Joseph Wang]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Posttraining & Midtraining; related YouTube resource; via [[youtube-sAOBXCDiDOs]])
- [[2026-06-29-liad-yosef-rebuilding-the-web-for-agents]] — Rebuilding the web for agents; [[liad-yosef|Liad Yosef]] (Day 2 — Session Day 1 · 12:05pm-12:25pm · Search & Retrieval; related YouTube resource; via [[youtube-o-zkvb0iFDQ]])
- [[2026-06-29-ido-salomon-we-re-the-bottleneck-but-we-don-t-have-to-be]] — We're the bottleneck, but we don't have to be; [[ido-salomon|Ido Salomon]] (Day 2 — Session Day 1 · 2:25pm-2:45pm · Software Factories; related YouTube resource; via [[youtube-o-zkvb0iFDQ]])
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering]] — The Golden Age of AI Engineering; [[alexander-embiricos|Alexander Embiricos]], [[romain-huet|Romain Huet]] (Day 2 — Session Day 1 · 9:25am-9:45am · Software Factories; related YouTube resource; via [[youtube-pMggiOb18tc]])

- [[laurie-voss|Laurie Voss]]
- [[christopher-manning|Christopher Manning]]
- [[pedro-lopez|Pedro Lopez]]
- [[joseph-wang|Joseph Wang]]

- [[arize-ai|Arize AI]]
- [[bright-data|Bright Data]]
- [[meta|Meta]]
- [[neo4j|Neo4j]]

- [[youtube-2e9ANoOEn28-slides]] — What if the harness mattered more than the model? - Aditya Bhargava, Etsy (8 extracted slide frames)
- [[youtube-sAOBXCDiDOs-slides]] — MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc (18 extracted slide frames)

- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]] — MCP Apps - Extending the frontier; [[liad-yosef|Liad Yosef]], [[ido-salomon|Ido Salomon]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Context Engineering; official schedule)
- [[2026-07-01-rafael-levi-video-discovery-for-agentic-world-model-training]] — Video Discovery for Agentic World-Model Training; [[rafael-levi|Rafael Levi]] (Day 2 — Session Day 1 · 2:50pm-3:10pm · Expo Stage 2 NW; related YouTube resource; via [[youtube-btxGmN8RvNU]])
- [[2026-06-29-du-an-lightfoot-agents-that-own-their-inference-building-production-ai-agents-on-dedicated-gpus]] — Agents That Own Their Inference: Building Production AI Agents on Dedicated GPUs; [[du-an-lightfoot|Du'an Lightfoot]] (Day 1 — Workshop Day · 9:00am-11:00am · Track 7; related YouTube resource; via [[youtube-wFTVEDYVJT0]])

## Source Coverage
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 64 | Related pages outside the main evidence categories. |
| resources | 24 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 34 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 34 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 3 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 16 | Transcript markdown; check session matching and caption quality. |

### Talks
- [[2026-06-29-ezra-tanzer-agentic-development-security]]
- [[2026-06-29-sarah-sachs-notion-s-token-town]]
- [[2026-07-01-jan-curn-mcp-doesn-t-suck-your-agent-does]]
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]]
- [[2026-06-30-dustin-mihalik-mcp-apps-give-the-model-data-give-the-user-a-ui]]
- [[2026-06-30-averi-kitsch-build-time-vs-run-time-why-your-dev-tools-will-fail-in-production]]

### Resources
- [[youtube-o-zkvb0iFDQ]]
- [[youtube-pMggiOb18tc]]
- [[youtube-V-EDrhIhHzQ]]
- [[youtube-q4Tr-DknG2M]]
- [[youtube-9fubhllmsBU]]
- [[youtube-WkBPX-oDMnA]]

### Slides
- [[youtube--I5W5QVAT8E-slides]]
- [[youtube-1EZdpEhwmNc-slides]]
- [[youtube-cgimkNGNjvU-slides]]
- [[youtube-2e9ANoOEn28-slides]]
- [[youtube-sAOBXCDiDOs-slides]]
- [[youtube-V-EDrhIhHzQ-slides]]

### Transcripts
- [[youtube-V-EDrhIhHzQ-transcript]]
- [[youtube-I2cbIws9j10-transcript]]
- [[youtube-htM02KMNZnk-transcript]]
- [[youtube-I3znWC3MEXM-transcript]]
- [[youtube-jt1Pbr_n6oU-transcript]]
- [[youtube-JvKO40CFq-s-transcript]]

### Tools
- [[docker]]
- [[mcp-apps]]
- [[neo4j]]
## Evidence Graph
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

The theme recurs across independently attributed official event recordings. Specific technical claims still remain bound to the cited recording, transcript, or slide layer.

### Linked Sessions
- [[2026-07-01-jan-curn-mcp-doesn-t-suck-your-agent-does|MCP doesn’t suck — your agent does]]
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier|MCP Apps - Extending the frontier]]
- [[2026-06-30-dustin-mihalik-mcp-apps-give-the-model-data-give-the-user-a-ui|MCP Apps: Give the Model Data, Give the User a UI]]
- [[2026-06-30-averi-kitsch-build-time-vs-run-time-why-your-dev-tools-will-fail-in-production|Build-Time vs. Run-Time: Why Your Dev Tools Will Fail in Production]]
- [[2026-06-29-jim-clark-who-approved-that-mcp-server-governing-the-tool-layer|Who Approved That MCP Server? Governing the Tool Layer]]
- [[2026-06-29-dan-adler-the-enterprise-agentic-gap-when-developer-level-ai-tools-hit-millions-of-lines|The Enterprise Agentic Gap: When Developer-Level AI Tools Hit Millions of Lines]]
- [[2026-06-29-jesse-lumarie-building-the-engine-while-flying-the-plane-launching-the-figma-mcp-server|Building the engine while flying the plane — launching the Figma MCP server]]
- [[2026-06-30-cornelia-davis-mcp-tasks-async-why-the-heck-aren-t-any-agents-supporting-mcp-tasks-async|MCP Tasks (async)/ Why the heck aren't any agents supporting MCP tasks/async?]]
- [[2026-07-01-sandhya-subramani-agents-that-forge-their-own-tools-self-modifying-ai-in-the-wild|'Agents That Forge Their Own Tools: Self-Modifying AI in the Wild']]
- [[2026-06-29-alexander-embiricos-the-golden-age-of-ai-engineering|The Golden Age of AI Engineering]]

### Media Signals
- `youtube-V-EDrhIhHzQ` — 10,228 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-V-EDrhIhHzQ`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-V-EDrhIhHzQ`: model, harness, well, doing, environment, training, able, models.
- Slide-derived themes for `youtube-V-EDrhIhHzQ`: engineering, future, prime, intellect, stack, open.
- Evidence links for `youtube-V-EDrhIhHzQ` (primary event evidence): [[youtube-V-EDrhIhHzQ]], [[youtube-V-EDrhIhHzQ-transcript]], [[youtube-V-EDrhIhHzQ-slides]]
- `youtube-I2cbIws9j10` — 91,792 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-I2cbIws9j10`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-I2cbIws9j10`: code, model, back, system, well, first, today, even.
- Slide-derived themes for `youtube-I2cbIws9j10`: choosing, model, quality, dominates, agentic, capabilities, customization, support.
- Evidence links for `youtube-I2cbIws9j10` (primary event evidence): [[youtube-I2cbIws9j10]], [[youtube-I2cbIws9j10-transcript]], [[youtube-I2cbIws9j10-slides]], [[youtube-I2cbIws9j10-dense-slides]]
- `youtube-htM02KMNZnk` — 89,050 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-htM02KMNZnk`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-htM02KMNZnk`: model, code, models, loop, well, software, first, team.
- Slide-derived themes for `youtube-htM02KMNZnk`: apps, github, copilot, welcome, engineer, fair, single, line.
- Evidence links for `youtube-htM02KMNZnk` (primary event evidence): [[youtube-htM02KMNZnk]], [[youtube-htM02KMNZnk-transcript]], [[youtube-htM02KMNZnk-slides]], [[youtube-htM02KMNZnk-dense-slides]], [[youtube-htM02KMNZnk-reconstructed-slides]]
- `youtube-I3znWC3MEXM` — 3,454 transcript words; 6 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-I3znWC3MEXM`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-I3znWC3MEXM`: token, user, server, access, call, resource, might, ooth.
- Slide-derived themes for `youtube-I3znWC3MEXM`: track, june, engineering, future, founding, engineer, head, developer.
- Evidence links for `youtube-I3znWC3MEXM` (primary event evidence): [[youtube-I3znWC3MEXM]], [[youtube-I3znWC3MEXM-transcript]], [[youtube-I3znWC3MEXM-slides]]
- `youtube-jt1Pbr_n6oU` — 3,441 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-jt1Pbr_n6oU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-jt1Pbr_n6oU`: data, model, graph, across, structure, chat, part, structured.
- Slide-derived themes for `youtube-jt1Pbr_n6oU`: track, july, fair, intro, defensible, organization, presented, users.
- Evidence links for `youtube-jt1Pbr_n6oU` (primary event evidence): [[youtube-jt1Pbr_n6oU]], [[youtube-jt1Pbr_n6oU-transcript]], [[youtube-jt1Pbr_n6oU-slides]]
- `youtube-JvKO40CFq-s` — 5,616 transcript words; 7 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-JvKO40CFq-s`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-JvKO40CFq-s`: okay, idea, email, capabilities, maybe, read, directory, identity.
- Slide-derived themes for `youtube-JvKO40CFq-s`: engineering, future, find, service, read, down, give, gees.
- Evidence links for `youtube-JvKO40CFq-s` (primary event evidence): [[youtube-JvKO40CFq-s]], [[youtube-JvKO40CFq-s-transcript]], [[youtube-JvKO40CFq-s-slides]]
- `youtube-RGSFUqzqErE` — 3,081 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-RGSFUqzqErE`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-RGSFUqzqErE`: knowledge, data, retrieval, foundry, whatnot, microsoft, models, give.
- Slide-derived themes for `youtube-RGSFUqzqErE`: fair, engineering, future, bile, microsoft, resolve, knowledge, pablo.
- Evidence links for `youtube-RGSFUqzqErE` (primary event evidence): [[youtube-RGSFUqzqErE]], [[youtube-RGSFUqzqErE-transcript]], [[youtube-RGSFUqzqErE-slides]]
- `youtube-YZQsWVeN3rE` — 2,901 transcript words; 3 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-YZQsWVeN3rE`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-YZQsWVeN3rE`: product, first, data, important, back, team, go-to-market, give.
- Slide-derived themes for `youtube-YZQsWVeN3rE`: juries, librarians, solve, trust, problem, alex, bauer, upside.
- Evidence links for `youtube-YZQsWVeN3rE` (primary event evidence): [[youtube-YZQsWVeN3rE]], [[youtube-YZQsWVeN3rE-transcript]], [[youtube-YZQsWVeN3rE-slides]]
- `youtube-c35YoMdnI78` — 11,538 transcript words; 8 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-c35YoMdnI78`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-c35YoMdnI78`: loops, loop, software, code, today, debate, engineering, should.
- Slide-derived themes for `youtube-c35YoMdnI78`: hands, reek, loan, take, career, karen, comets.
- Evidence links for `youtube-c35YoMdnI78` (primary event evidence): [[youtube-c35YoMdnI78]], [[youtube-c35YoMdnI78-transcript]], [[youtube-c35YoMdnI78-slides]]
- `youtube-1EZdpEhwmNc` — 4,245 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-1EZdpEhwmNc`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-1EZdpEhwmNc`: security, data, code, able, find, skill, customers, attacks.
- Slide-derived themes for `youtube-1EZdpEhwmNc`: track, june, security, malicious, engineering, future, pitch, defend.
- Evidence links for `youtube-1EZdpEhwmNc` (primary event evidence): [[youtube-1EZdpEhwmNc]], [[youtube-1EZdpEhwmNc-transcript]], [[youtube-1EZdpEhwmNc-slides]]
- `youtube-Q0VkgCyNVUg` — 3,266 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Q0VkgCyNVUg`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Q0VkgCyNVUg`: graph, memory, vector, files, demo, information, great, store.
- Slide-derived themes for `youtube-Q0VkgCyNVUg`: shell, track, july, skills, meat, engineering, future, wakes.
- Evidence links for `youtube-Q0VkgCyNVUg` (primary event evidence): [[youtube-Q0VkgCyNVUg]], [[youtube-Q0VkgCyNVUg-transcript]], [[youtube-Q0VkgCyNVUg-slides]]
- `youtube-cgimkNGNjvU` — 5,107 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-cgimkNGNjvU`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-cgimkNGNjvU`: security, running, doing, code, last, still, skills, machine.
- Slide-derived themes for `youtube-cgimkNGNjvU`: security, track, june, server, directives, faye, world, fair.
- Evidence links for `youtube-cgimkNGNjvU` (primary event evidence): [[youtube-cgimkNGNjvU]], [[youtube-cgimkNGNjvU-transcript]], [[youtube-cgimkNGNjvU-slides]]
- `youtube-kRkcNOsRyYg` — 18,117 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-kRkcNOsRyYg`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-kRkcNOsRyYg`: graph, data, well, question, inside, search, over, documents.
- Slide-derived themes for `youtube-kRkcNOsRyYg`: engineering, future, engineer, squire, ryan, knight, senior, partner.
- Evidence links for `youtube-kRkcNOsRyYg` (primary event evidence): [[youtube-kRkcNOsRyYg]], [[youtube-kRkcNOsRyYg-transcript]], [[youtube-kRkcNOsRyYg-slides]]
- `youtube-sAOBXCDiDOs` — 4,772 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-sAOBXCDiDOs`: apps, model, tool, widget, server, cloud, clears, throat.
- Slide-derived themes for `youtube-sAOBXCDiDOs`: host, apps, server, renders, inline, primitives, discovery, software.
- Evidence links for `youtube-sAOBXCDiDOs` (supporting context only): [[youtube-sAOBXCDiDOs]], [[youtube-sAOBXCDiDOs-transcript]], [[youtube-sAOBXCDiDOs-slides]]
- `youtube-o-zkvb0iFDQ` — 3,969 transcript words; 10 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-o-zkvb0iFDQ`: apps, host, claude, back, chatgpt, look, mcpui, chat.
- Slide-derived themes for `youtube-o-zkvb0iFDQ`: apps, maintainer, labs, used, text, community, easy, adoption.
- Evidence links for `youtube-o-zkvb0iFDQ` (supporting context only): [[youtube-o-zkvb0iFDQ]], [[youtube-o-zkvb0iFDQ-transcript]], [[youtube-o-zkvb0iFDQ-slides]], [[youtube-o-zkvb0iFDQ-dense-slides]], [[youtube-o-zkvb0iFDQ-reconstructed-slides]]
- `youtube-blW-lSd5CYQ` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-blW-lSd5CYQ`: scraper, data, extract, posts, google, maps, instagram, scrape.
- Evidence links for `youtube-blW-lSd5CYQ` (supporting context only): [[youtube-blW-lSd5CYQ]], [[youtube-blW-lSd5CYQ-slides]], [[youtube-blW-lSd5CYQ-dense-slides]], [[youtube-blW-lSd5CYQ-reconstructed-slides]]
- `youtube-wFTVEDYVJT0` — 13,586 transcript words; 9 slide-derived text signals; role: supporting context only.
- Transcript signals for `youtube-wFTVEDYVJT0`: nova, amazon, code, server, browser, able, open, click.
- Slide-derived themes for `youtube-wFTVEDYVJT0`: plan, execute, actions, achieve, specific, goals, agentic, tamera.
- Evidence links for `youtube-wFTVEDYVJT0` (supporting context only): [[youtube-wFTVEDYVJT0]], [[youtube-wFTVEDYVJT0-transcript]], [[youtube-wFTVEDYVJT0-slides]], [[youtube-wFTVEDYVJT0-dense-slides]], [[youtube-wFTVEDYVJT0-reconstructed-slides]]
- `youtube-OV56RddyFuU` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-OV56RddyFuU`: models, community, trending, image, pare, update, mode, tees.
- Evidence links for `youtube-OV56RddyFuU` (supporting context only): [[youtube-OV56RddyFuU]], [[youtube-OV56RddyFuU-slides]], [[youtube-OV56RddyFuU-dense-slides]], [[youtube-OV56RddyFuU-reconstructed-slides]]
- `youtube-96G7FLab8xc` — 10 slide-derived text signals; role: supporting context only.
- Slide-derived themes for `youtube-96G7FLab8xc`: prefect, list, server, should, feel, engineer, code, summit.
- Evidence links for `youtube-96G7FLab8xc` (supporting context only): [[youtube-96G7FLab8xc]], [[youtube-96G7FLab8xc-slides]], [[youtube-96G7FLab8xc-dense-slides]], [[youtube-96G7FLab8xc-reconstructed-slides]]
