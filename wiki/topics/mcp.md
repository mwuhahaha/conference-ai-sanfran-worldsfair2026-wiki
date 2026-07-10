---
title: "Model Context Protocol"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---
# Model Context Protocol

## Synopsis
Model Context Protocol, or MCP, is a standard pattern for connecting AI applications to tools, data, and interactive capabilities through structured servers and clients. In this wiki it also includes MCP Apps and agent-facing interfaces that expose richer actions or UI surfaces to models.

## Origin And Context
MCP emerged from the need to standardize how AI clients discover and call tools, access resources, and integrate with external systems. It sits in the lineage of plugin APIs, language-server style tooling, RPC, browser extensions, and developer-tool protocols.

## Why It Matters
Agents are only as useful as the tools and context they can safely access. MCP reduces one-off integrations, gives tool providers a common surface, and helps clients reason about capabilities, permissions, and interaction patterns.

## How To Use It
Define focused MCP servers with clear tools, schemas, resources, and permission boundaries. Keep tool names concrete, return structured results, test with inspectors, and design for least privilege. For MCP Apps, treat UI and iframe boundaries as part of the security and product contract.

## Where It Is Useful
MCP is useful in IDEs, desktop assistants, enterprise data connectors, browser agents, design tools, developer platforms, and internal operations systems.

## When To Use It
Use MCP when multiple AI clients need access to the same tools or when a tool provider wants a standard agent-facing integration. For a single narrow app, direct APIs may be simpler until reuse or interoperability matters.

## Active Use Cases
- Connecting agents to repositories, browsers, docs, databases, and SaaS tools.
- MCP Apps that return interactive UI from tool servers.
- Agent-ready web and developer-tool integrations.
- Local inspectors and compliance checks for tool servers.

## Related Slide Decks
- [[youtube-2e9ANoOEn28-slides]] — What if the harness mattered more than the model? - Aditya Bhargava, Etsy (8 extracted slide frames)
- [[youtube-sAOBXCDiDOs-slides]] — MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc (18 extracted slide frames)

## Related Scheduled Sessions
- [[2026-07-01-jan-curn-mcp-doesn-t-suck-your-agent-does]] — MCP doesn’t suck — your agent does; [[jan-curn|Jan Curn]] (Day 4 — Session Day 3 · 1:55pm-2:15pm · Expo Stage 2 NW; official schedule)
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]] — MCP Apps - Extending the frontier; [[liad-yosef|Liad Yosef]], [[ido-salomon|Ido Salomon]] (Day 3 — Session Day 2 · 2:25pm-2:45pm · Context Engineering; official schedule)
- [[2026-06-30-dustin-mihalik-mcp-apps-give-the-model-data-give-the-user-a-ui]] — MCP Apps: Give the Model Data, Give the User a UI; [[dustin-mihalik|Dustin Mihalik]] (Day 3 — Session Day 2 · 2:50pm-3:10pm · Context Engineering; official schedule)
- [[2026-06-29-kwindla-kramer-the-new-primitives-building-ai-native-software]] — The New Primitives: Building AI-Native Software; [[kwindla-kramer|Kwindla Kramer]] (Day 2 — Session Day 1 · 10:45am-11:05am · Voice & Realtime AI; related YouTube resource; via [[youtube-sAOBXCDiDOs]])
- [[2026-06-29-pedro-lopez-how-we-built-the-airbyte-agent-mcp-server-and-cli]] — How We Built the Airbyte Agent MCP Server and CLI; [[pedro-lopez|Pedro Lopez]] (Day 2 — Session Day 1 · 3:45pm-4:05pm · Expo Stage 1; related YouTube resource; via [[youtube-sAOBXCDiDOs]])
- [[2026-06-30-joseph-wang-emulated-the-data-for-fully-autonomous-software-engineers-and-companies]] — Emulated: The data for fully autonomous software engineers and companies; [[joseph-wang|Joseph Wang]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Posttraining & Midtraining; related YouTube resource; via [[youtube-sAOBXCDiDOs]])
- [[2026-06-30-averi-kitsch-build-time-vs-run-time-why-your-dev-tools-will-fail-in-production]] — Build-Time vs. Run-Time: Why Your Dev Tools Will Fail in Production; [[averi-kitsch|Averi Kitsch]], [[prerna-kakkar|Prerna Kakkar]] (Day 3 — Session Day 2 · 10:45am-11:05am · Context Engineering; official schedule)
- [[2026-06-29-jim-clark-who-approved-that-mcp-server-governing-the-tool-layer]] — Who Approved That MCP Server? Governing the Tool Layer; [[jim-clark|Jim Clark]] (Day 2 — Session Day 1 · 1:55pm-2:15pm · Expo Stage 1 NE; official schedule)
- [[2026-06-29-dan-adler-the-enterprise-agentic-gap-when-developer-level-ai-tools-hit-millions-of-lines]] — The Enterprise Agentic Gap: When Developer-Level AI Tools Hit Millions of Lines; [[dan-adler|Dan Adler]] (Day 2 — Session Day 1 · 10:45am-11:05am · Expo Stage 2 NW; official schedule)
- [[2026-06-29-jesse-lumarie-building-the-engine-while-flying-the-plane-launching-the-figma-mcp-server]] — Building the engine while flying the plane — launching the Figma MCP server; [[jesse-lumarie|Jesse Lumarie]] (Day 2 — Session Day 1 · 11:10am-11:30am · AI-Native Enterprises; official schedule)
- [[2026-06-30-cornelia-davis-mcp-tasks-async-why-the-heck-aren-t-any-agents-supporting-mcp-tasks-async]] — MCP Tasks (async)/ Why the heck aren't any agents supporting MCP tasks/async?; [[cornelia-davis|Cornelia Davis]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Context Engineering; official schedule)
- [[2026-07-01-sandhya-subramani-agents-that-forge-their-own-tools-self-modifying-ai-in-the-wild]] — Agents That Forge Their Own Tools: Self-Modifying AI in the Wild; [[sandhya-subramani|Sandhya Subramani]] (Day 4 — Session Day 3 · 12:05pm-12:25pm · Expo Stage 4 SE; official schedule)
- [[2026-06-29-mark-lummus-burn-your-flags-how-paypal-designs-interactive-cli-tools-for-agents]] — Burn your flags: How PayPal designs interactive CLI tools for agents; [[mark-lummus|Mark Lummus]], [[navinkumar-patil|Navinkumar Patil]] (Day 1 — Workshop Day · 2:20pm-4:20pm · Workshops Day 1; official schedule)
- [[2026-07-01-nikita-kothari-mcps-clis-and-skills-choosing-the-right-tooling-layer-for-agentic-development]] — MCPs, CLIs, and Skills: Choosing the Right Tooling Layer for Agentic Development; [[nikita-kothari|Nikita Kothari]] (Day 4 — Session Day 3 · 11:10am-11:30am · Agentic Engineering; official schedule)
- [[2026-06-29-ethan-jung-min-cha-dual-surface-architecture-serving-humans-and-agents-from-the-same-tool-layer]] — Dual-Surface Architecture: Serving Humans and Agents from the Same Tool Layer; [[ethan-jung-min-cha|Ethan (Jung Min) Cha]] (Day 2 — Session Day 1 · 1:55pm-2:15pm · Security; official schedule)
- [[2026-06-30-thorsten-hans-edge-native-ai-building-ultra-fast-agents-and-mcp-servers-with-spin]] — Edge-Native AI: Building Ultra-Fast Agents and MCP Servers with Spin; [[thorsten-hans|Thorsten Hans]] (Day 3 — Session Day 2 · 1:55pm-2:15pm · Expo Stage 2; official schedule)
- [[2026-06-29-maria-bledsoe-using-ai-tools-to-teach-old-apps-new-tricks]] — Using AI tools to teach old apps new tricks; [[maria-bledsoe|Maria Bledsoe]] (Day 2 — Session Day 1 · 2:25pm-2:45pm · Track M; official schedule)
- [[2026-07-01-anil-nadiminti-when-ai-agents-pay-and-sellers-monetize-building-x402-apps-for-agentic-commerce-on-aws]] — When AI Agents Pay and Sellers Monetize: Building x402 Apps for Agentic Commerce on AWS; [[anil-nadiminti|Anil Nadiminti]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Agentic Commerce; official schedule)
- [[2026-06-29-merve-noyan-skill-issue-stop-deploying-vision-language-models-use-them-with-skills-to-build-e2e-vision-apps-on-edge]] — Skill issue: stop deploying vision language models, use them with Skills to build e2e vision apps on edge; [[merve-noyan|Merve Noyan]] (Day 2 — Session Day 1 · 11:40am-12:00pm · Vision & OCR; official schedule)
- [[2026-06-29-vasuman-moza-ai-tools-for-forward-deployed-engineering]] — AI tools for Forward Deployed Engineering; [[vasuman-moza|Vasuman Moza]] (Day 2 — Session Day 1 · 11:40am-12:00pm · Forward Deployed Engineering; official schedule)
- [[2026-06-29-pamela-fox-get-started-with-models-in-microsoft-foundry-to-build-ai-apps]] — Get Started with Models in Microsoft Foundry to Build AI Apps; [[pamela-fox|Pamela Fox]] (Day 1 — Workshop Day · 9:00am-10:15am · Track M; official schedule)
- [[2026-06-30-ashu-joshi-deploy-agents-to-users-in-m365-teams-and-apps]] — Deploy agents to users in M365, Teams, and apps; [[ashu-joshi|Ashu Joshi]] (Day 3 — Session Day 2 · 3:20pm-3:40pm · Track M; official schedule)
- [[2026-07-01-rafael-levi-video-discovery-for-agentic-world-model-training]] — Video Discovery for Agentic World-Model Training; [[rafael-levi|Rafael Levi]] (Day 2 — Session Day 1 · 2:50pm-3:10pm · Expo Stage 2 NW; related YouTube resource; via [[youtube-btxGmN8RvNU]])
- [[2026-06-29-du-an-lightfoot-agents-that-own-their-inference-building-production-ai-agents-on-dedicated-gpus]] — Agents That Own Their Inference: Building Production AI Agents on Dedicated GPUs; [[du-an-lightfoot|Du'an Lightfoot]] (Day 1 — Workshop Day · 9:00am-11:00am · Track 7; related YouTube resource; via [[youtube-wFTVEDYVJT0]])

## Related People
- [[john-craft|John Craft]]
- [[laurie-voss|Laurie Voss]]
- [[pamela-fox|Pamela Fox]]
- [[sandhya-subramani|Sandhya Subramani]]
- [[jason-liu|Jason Liu]]
- [[john-lindquist|John Lindquist]]
- [[liad-yosef|Liad Yosef]]
- [[charlie-guo|Charlie Guo]]
- [[frank-coyle|Frank Coyle]]
- [[christopher-manning|Christopher Manning]]
- [[kwindla-kramer|Kwindla Kramer]]
- [[merve-noyan|Merve Noyan]]
- [[arun-sekhar|Arun Sekhar]]
- [[elizabeth-fuentes-leone|Elizabeth Fuentes Leone]]
- [[harshul-jain|Harshul Jain]]
- [[tanmay-sah|Tanmay Sah]]
- [[jan-curn|Jan Curn]]
- [[ido-salomon|Ido Salomon]]
- [[dustin-mihalik|Dustin Mihalik]]
- [[pedro-lopez|Pedro Lopez]]
- [[joseph-wang|Joseph Wang]]
- [[averi-kitsch|Averi Kitsch]]
- [[prerna-kakkar|Prerna Kakkar]]
- [[jim-clark|Jim Clark]]

## Related Companies
- [[microsoft|Microsoft]]
- [[openai|OpenAI]]
- [[docker|Docker]]
- [[arize-ai|Arize AI]]
- [[google|Google]]
- [[amazon-web-services|Amazon Web Services]]
- [[hugging-face|Hugging Face]]
- [[nvidia|NVIDIA]]
- [[mcp-apps|MCP Apps]]
- [[paypal|PayPal]]
- [[towards-ai|Towards AI]]
- [[bright-data|Bright Data]]
- [[uber|Uber]]
- [[warp|Warp]]
- [[weights-and-biases-by-coreweave|Weights & Biases by CoreWeave]]
- [[egghead-io|egghead.io]]
- [[meta|Meta]]
- [[neo4j|Neo4j]]

## Transcript And Resource Support
### Transcript-backed resources
- [[youtube-sAOBXCDiDOs]] — MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc
- [[youtube-vh2VGuQ3zhY]] — The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica
- [[youtube-_xIwFcnHqp4]] — Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub
- [[youtube-ghJmWQCIHRM]] — The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google
- [[youtube-_B4Pv9ttFgY]] — Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google
- [[youtube-1IdzkRVmWAA]] — How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI
- [[youtube-HsxQICTLF84]] — Building an ACP-Compatible Agent Live — Bennet Fenner, Zed
- [[youtube-c-2eEv2ou7Y]] — Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic
- [[youtube-HEFSExa0xl0]] — Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs
- [[youtube-spNAUEgq_A8]] — The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents
- [[youtube-2e9ANoOEn28]] — What if the harness mattered more than the model? - Aditya Bhargava, Etsy
- [[youtube-UcYoMg-8-L8]] — 500 people vibe-coded for 30 days. I was one of them. - Sanja Grbic, Automattic
- [[youtube-G6IlDzj8OjA]] — GTM Is You - Victoria Melnikova, Evil Martians
- [[youtube-xUnRQ9vLXxo]] — What do we build now? — @t3dotgg
- [[youtube-hCMrEfPG2Yg]] — Beyond Components: Designing Generative UI for MCP Apps — Ruben Casas, Postman
- [[youtube-BqZrTdgBaPw]] — Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG
- [[youtube-4uFVSLgD2Q4]] — Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov
- [[youtube-btxGmN8RvNU]] — Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data

### Quote signals
- “I'm an engineer here at OpenGov and today we're going to be talking about agents in production, specifically how OpenGov built and scaled OG Assist.” — [[youtube-4uFVSLgD2Q4]]
- “So, that's kind of how we handled long context and memory, and it's worked pretty well for us.” — [[youtube-4uFVSLgD2Q4]]
- “Uh it's an open source inspector, again, uh something comparable to the official inspector from the model context protocol maintainers that allows you to test these MCP servers and apps specifically uh on your local machine.” — [[youtube-sAOBXCDiDOs]]
- “MCP apps is now the official extension of the Model Context Protocol that allows to return UI elements within MCP servers.” — [[youtube-sAOBXCDiDOs]]
- “[clears throat] And also Cursor allows you to submit their MCP server set uh The way you submit is different for all three, but basically what happens is that you need to make sure that your MCP app is compliant.” — [[youtube-sAOBXCDiDOs]]
- “The let's say past few decades, we have been building the web for human actions and human eyes, and we've been trying to optimize for that, but these days, it's not just humans that are using the web.” — [[youtube-ghJmWQCIHRM]]
- “Well, today I'm going to share four engineering lessons from the Chrome uh DevTools team on how we build Chrome DevTools for agents and how we deployed it for effect.” — [[youtube-_B4Pv9ttFgY]]
- “In a world where you are delegating away work to agents and automating away agents, you need to think about trust boundaries.” — [[youtube-_B4Pv9ttFgY]]

## Source-Derived Enrichment
This section consolidates source evidence currently connected to this topic across scheduled talks, linked videos, transcripts, and slide-derived material.

### Talk Evidence
- [[2026-07-01-jan-curn-mcp-doesn-t-suck-your-agent-does|MCP doesn’t suck — your agent does]]
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier|MCP Apps - Extending the frontier]]
- [[2026-06-30-dustin-mihalik-mcp-apps-give-the-model-data-give-the-user-a-ui|MCP Apps: Give the Model Data, Give the User a UI]]
- [[2026-06-29-kwindla-kramer-the-new-primitives-building-ai-native-software|The New Primitives: Building AI-Native Software]]
- [[2026-06-29-pedro-lopez-how-we-built-the-airbyte-agent-mcp-server-and-cli|How We Built the Airbyte Agent MCP Server and CLI]]
- [[2026-06-30-joseph-wang-emulated-the-data-for-fully-autonomous-software-engineers-and-companies|Emulated: The data for fully autonomous software engineers and companies]]
- [[2026-06-30-averi-kitsch-build-time-vs-run-time-why-your-dev-tools-will-fail-in-production|Build-Time vs. Run-Time: Why Your Dev Tools Will Fail in Production]]
- [[2026-06-29-jim-clark-who-approved-that-mcp-server-governing-the-tool-layer|Who Approved That MCP Server? Governing the Tool Layer]]
- [[2026-06-29-dan-adler-the-enterprise-agentic-gap-when-developer-level-ai-tools-hit-millions-of-lines|The Enterprise Agentic Gap: When Developer-Level AI Tools Hit Millions of Lines]]
- [[2026-06-29-jesse-lumarie-building-the-engine-while-flying-the-plane-launching-the-figma-mcp-server|Building the engine while flying the plane — launching the Figma MCP server]]

### Slide And Transcript Signals
- `youtube-blW-lSd5CYQ` — 9 slide-derived text signals
- Slide-derived themes for `youtube-blW-lSd5CYQ`: google, maps, intelligence, emerge, runs, actors, compass, data.
- Evidence links for `youtube-blW-lSd5CYQ`: [[youtube-blW-lSd5CYQ]], [[youtube-blW-lSd5CYQ-slides]], [[youtube-blW-lSd5CYQ-dense-slides]], [[youtube-blW-lSd5CYQ-reconstructed-slides]]
- `youtube-o-zkvb0iFDQ` — 3,969 transcript words; 1 slide-derived text signals
- Transcript signals for `youtube-o-zkvb0iFDQ`: apps, host, claude, back, chatgpt, look, mcpui, chat.
- Slide-derived themes for `youtube-o-zkvb0iFDQ`: engineering, future.
- Evidence links for `youtube-o-zkvb0iFDQ`: [[youtube-o-zkvb0iFDQ]], [[youtube-o-zkvb0iFDQ-transcript]], [[youtube-o-zkvb0iFDQ-slides]], [[youtube-o-zkvb0iFDQ-dense-slides]], [[youtube-o-zkvb0iFDQ-reconstructed-slides]]
- `youtube-E71YtNbCFXY` — 5 slide-derived text signals
- Slide-derived themes for `youtube-E71YtNbCFXY`: pelt, remember, connections.
- Evidence links for `youtube-E71YtNbCFXY`: [[youtube-E71YtNbCFXY]], [[youtube-E71YtNbCFXY-slides]], [[youtube-E71YtNbCFXY-dense-slides]], [[youtube-E71YtNbCFXY-reconstructed-slides]]
## Evidence Table
This table summarizes the local evidence already linked from this topic. It is a navigation aid, not a claim that every linked page has been fully reviewed.

| Evidence type | Count | Review note |
| --- | ---: | --- |
| other | 53 | Related pages outside the main evidence categories. |
| resources | 22 | Video/resource pages; check source status before treating as primary event evidence. |
| slides | 11 | OCR or reconstructed slide evidence; mark claims as OCR-derived unless image-reviewed. |
| talks | 24 | Official schedule pages; use for titles, speakers, tracks, and stated talk framing. |
| tools | 3 | Derived inventory pages; use as entity context, not independent proof. |
| transcripts | 1 | Transcript markdown; check session matching and caption quality. |

## Representative Evidence Links
### Talks
- [[2026-07-01-jan-curn-mcp-doesn-t-suck-your-agent-does]]
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]]
- [[2026-06-30-dustin-mihalik-mcp-apps-give-the-model-data-give-the-user-a-ui]]
- [[2026-06-29-kwindla-kramer-the-new-primitives-building-ai-native-software]]
- [[2026-06-29-pedro-lopez-how-we-built-the-airbyte-agent-mcp-server-and-cli]]
- [[2026-06-30-joseph-wang-emulated-the-data-for-fully-autonomous-software-engineers-and-companies]]

### Resources
- [[youtube-sAOBXCDiDOs]]
- [[youtube-btxGmN8RvNU]]
- [[youtube-wFTVEDYVJT0]]
- [[youtube-vh2VGuQ3zhY]]
- [[youtube-_xIwFcnHqp4]]
- [[youtube-ghJmWQCIHRM]]

### Slides
- [[youtube-2e9ANoOEn28-slides]]
- [[youtube-sAOBXCDiDOs-slides]]
- [[youtube-blW-lSd5CYQ-slides]]
- [[youtube-blW-lSd5CYQ-dense-slides]]
- [[youtube-blW-lSd5CYQ-reconstructed-slides]]
- [[youtube-o-zkvb0iFDQ-slides]]

### Transcripts
- [[youtube-o-zkvb0iFDQ-transcript]]

### Tools
- [[docker]]
- [[mcp-apps]]
- [[neo4j]]

## Representative Evidence Links
### Talks
- [[2026-07-01-jan-curn-mcp-doesn-t-suck-your-agent-does]]
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]]
- [[2026-06-30-dustin-mihalik-mcp-apps-give-the-model-data-give-the-user-a-ui]]
- [[2026-06-29-kwindla-kramer-the-new-primitives-building-ai-native-software]]
- [[2026-06-29-pedro-lopez-how-we-built-the-airbyte-agent-mcp-server-and-cli]]
- [[2026-06-30-joseph-wang-emulated-the-data-for-fully-autonomous-software-engineers-and-companies]]

### Resources
- [[youtube-sAOBXCDiDOs]]
- [[youtube-btxGmN8RvNU]]
- [[youtube-wFTVEDYVJT0]]
- [[youtube-vh2VGuQ3zhY]]
- [[youtube-_xIwFcnHqp4]]
- [[youtube-ghJmWQCIHRM]]

### Slides
- [[youtube-2e9ANoOEn28-slides]]
- [[youtube-sAOBXCDiDOs-slides]]
- [[youtube-blW-lSd5CYQ-slides]]
- [[youtube-blW-lSd5CYQ-dense-slides]]
- [[youtube-blW-lSd5CYQ-reconstructed-slides]]
- [[youtube-o-zkvb0iFDQ-slides]]

### Transcripts
- [[youtube-o-zkvb0iFDQ-transcript]]

### Tools
- [[docker]]
- [[mcp-apps]]
- [[neo4j]]

## Representative Evidence Links
### Talks
- [[2026-07-01-jan-curn-mcp-doesn-t-suck-your-agent-does]]
- [[2026-06-30-liad-yosef-mcp-apps-extending-the-frontier]]
- [[2026-06-30-dustin-mihalik-mcp-apps-give-the-model-data-give-the-user-a-ui]]
- [[2026-06-29-kwindla-kramer-the-new-primitives-building-ai-native-software]]
- [[2026-06-29-pedro-lopez-how-we-built-the-airbyte-agent-mcp-server-and-cli]]
- [[2026-06-30-joseph-wang-emulated-the-data-for-fully-autonomous-software-engineers-and-companies]]

### Resources
- [[youtube-sAOBXCDiDOs]]
- [[youtube-btxGmN8RvNU]]
- [[youtube-wFTVEDYVJT0]]
- [[youtube-vh2VGuQ3zhY]]
- [[youtube-_xIwFcnHqp4]]
- [[youtube-ghJmWQCIHRM]]

### Slides
- [[youtube-2e9ANoOEn28-slides]]
- [[youtube-sAOBXCDiDOs-slides]]
- [[youtube-blW-lSd5CYQ-slides]]
- [[youtube-blW-lSd5CYQ-dense-slides]]
- [[youtube-blW-lSd5CYQ-reconstructed-slides]]
- [[youtube-o-zkvb0iFDQ-slides]]

### Transcripts
- [[youtube-o-zkvb0iFDQ-transcript]]

### Tools
- [[docker]]
- [[mcp-apps]]
- [[neo4j]]
