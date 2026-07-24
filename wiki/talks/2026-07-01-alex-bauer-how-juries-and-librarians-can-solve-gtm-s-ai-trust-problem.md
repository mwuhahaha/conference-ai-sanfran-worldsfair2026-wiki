---
title: How Juries and Librarians Can Solve GTM's AI Trust Problem
category: talks
date: '2026-07-01'
time: '1:30pm-1:50pm'
track: AI in GTM
room: Track 6
speakers:
  - Alex Bauer
sourceLabels:
  - Official conference schedule
  - Public YouTube metadata
last_auto_summarized: '2026-07-06T17:57:59.481Z'
scheduleTrack: "AI in GTM"
scheduleRoom: "Track 6"
scheduleLabels: ["AI in GTM", "Track 6", "session", "confirmed"]
---
# How Juries and Librarians Can Solve GTM's AI Trust Problem

## Conference Context
- Date/time: 2026-07-01 · 1:30pm-1:50pm
- Track/room: AI in GTM · Track 6
- Speaker(s): Alex Bauer
- Session type/status: session · confirmed

- Track: AI in GTM
- Room: Track 6
- Session type: session
- Status: confirmed

## Session Description
A couple of years ago, everyone worried about AI hallucinating. We rarely hear that word anymore, but it’s just because the problem grew up. Today, your AI still doesn’t know how to say “I’m not sure.” Instead, it hands you a revenue number that’s wrong in ways that look exactly like being right. The good news is we already solved this once, for people: you onboard a new hire so they understand your business; you put subjective, high-stakes calls in front of more than one set of eyes. This talk walks through patterns we run at Upside, including a librarian every agent consults before it acts, a jury-and-judge model for the questions a single pass can’t be trusted to answer, and knowing when the model itself is just too dumb for the job. Live demos and real failures included.

## Summary
Alex Bauer's AI in GTM session treats trust as an operational problem inside revenue systems, not as a generic model-behavior lecture. The official description says the dangerous failure mode is no longer a bizarre hallucination that is easy to spot, but a confident GTM answer, such as a revenue number, that is wrong in ways that look plausible. That framing makes the session especially relevant to teams applying agents to attribution, account intelligence, pipeline inspection, forecasting, and other GTM workflows where an answer can be formatted correctly while still being commercially misleading.

The connected people page sharpens why Bauer is a fitting speaker for this topic: he is co founder of Upside, described there as the data layer for GTM engineers, and previously spent 2016-2024 at Branch as a public voice on mobile attribution and deep linking. That background points toward a talk grounded in the messy edge cases of business data, identity, attribution, and source-of-truth disputes rather than abstract prompt engineering. The scheduled patterns are concrete: a shared “librarian” that agents consult before acting, a jury-and-judge model for subjective or high-stakes calls, and an explicit stop condition for cases where the model is simply not capable enough for the job.

Within the July 1 multi-track program, this session sits in the AI in GTM track during the conference's densest day at Moscone West. It complements the broader wiki theme of converting official schedule entries into evidence-backed intelligence: the current evidence is still schedule-grounded, and the transcript map notes that no exact AI Engineer YouTube recording match was found by normalized title during this run. Until a confirmed recording, transcript, slide OCR, or resource link is attached, the page should keep the librarian, jury, judge, and model-capability patterns as official-description claims rather than transcript-confirmed implementation details.

## Synthesis
### Transcript-Backed Summary
Alex Bauer argues that GTM AI has moved past simple hallucination and into a broader trust problem: the model can sound right while being wrong in ways that matter to revenue and operations. His answer is to manage agents like people, which means giving them commander's intent, writing down how the business actually works, and adding a librarian-style knowledge layer that supplies definitions, prior failures, and citations before the agent acts. For questions that do not have an empirically correct answer, he recommends a jury-and-judge workflow that gathers independent research and then weighs the reasoning, with escalation when consensus is weak. The practical consequence is a more structured stack that costs more upfront than a raw prompt, but produces outputs that are better grounded, more defensible, and safer to operationalize.

### Key Takeaways
- Tell agents why you want the outcome, not just what to do.
  - Evidence: "And if you take nothing else from this talk, this is my one practical tip. Use commander's intent when you prompt."
- Define the business structure before asking AI to generate from it.
  - Evidence: "So, the step here was define the structure first, and then turn Claude loose. Don't try and YOLO it from the beginning."
- Use a librarian layer to inject company-specific meaning before the agent answers.
  - Evidence: "And so it basically gives your agent a just-in-time memory of all the important things. So we know that the fiscal year here is actually February through April."
- Escalate subjective GTM questions to multiple independent analysts plus a judge.
  - Evidence: "And if there's not enough consensus, then I'll escalate and expand the jury. But, my job is not to do research on my own."
- Reserve important work for capable models and full-featured harnesses.
  - Evidence: "You need it to have attributes like sub agents, plan mode, full MCP support. It should be able to use file editing and there are a lot of these out here."

### Claims From The Talk
- The speaker says the current AI problem in GTM is trust, because the model can return a revenue answer that is confidently wrong rather than admitting uncertainty. (`explicit`)
  - Evidence: "It's a trust problem. And if you ask Claude to do something like report on revenue, it doesn't say, \"I'm not sure.\" It says, \"Here you go.\" And it gives you a wrong answer that looks exactly like being right."
- He argues that the main operating principle is to manage agents like other humans. (`explicit`)
  - Evidence: "So, the main thesis of the talk today is actually, when in doubt, manage your agents like other humans."
- He reports that the website rebuild only became workable after defining the structure first and then letting Claude generate against that scaffold. (`explicit`)
  - Evidence: "So, the step here was define the structure first, and then turn Claude loose. Don't try and YOLO it from the beginning."
- He says the librarian is consulted before answering so the agent gets just-in-time memory from documentation, company knowledge, and prior failed queries. (`explicit`)
  - Evidence: "So what we actually have it do is consult the librarian first. And the librarian has access to documentation and the library of knowledge items about your company and the schema of prior failed queries."
- He describes attribution as a case where the agent should gather independent analysts rather than answer from a single pass. (`explicit`)
  - Evidence: "They are going to spin up a team of independent analysts who all look at the data independently and come up with an evidence-cited opinion for what they think the attribution credit of that deal should be."
- He warns that AI products constrained by weak subscription economics are not appropriate for anything important. (`explicit`)
  - Evidence: "So, basically, the general case here is any AI product where it's been crowbarred into a pre- subscription model is probably not something that you should be using for anything important because the margin on those plans just doesn't leave enough space for an intelligent reasoning model to work."

### Topics Covered
- **AI Trust in GTM** — The shift from hallucination as a generic concern to wrong-but-confident business answers that undermine adoption.
- [[coding-agents|Commander's Intent]] — Prompting agents by explaining the desired outcome and context rather than micromanaging the steps.
- **Business Knowledge Scaffolding** — Preparing company facts, capabilities, and personas as reusable reference material before generation.
- [[agent-memory|Librarian Memory]] — A pre-answer knowledge layer that gives agents company definitions, documentation, and failure history.
- [[autoresearch|Jury-and-Judge Workflow]] — A multi-agent decision pattern that combines independent research with a final reasoning judge.
- **Agent Tiering** — Choosing sufficiently capable models and harnesses for important tasks instead of using weak wrappers.

### Tools And Named Systems
- [[claude|Claude]] — The model the speaker uses as the agentic assistant that can still produce wrong business answers if unmanaged.
- **Upside Librarian** — The product feature described as the radiant librarian that agents consult before answering.
- **Slackbot** — The Slack product the speaker says released MCP client functionality.
- [[mcp|MCP]] — The protocol mentioned as a way to connect Slackbot and other tools to external systems.

### Novel Concepts And Methods
- **Commander's Intent Prompting** — Tell the agent why you want the task done so it can make better decisions.
- **Anchor Asset Scaffolding** — Maintain structured reference assets for company facts, capabilities, and personas before generation.
- **Librarian-First Retrieval** — Consult a knowledge librarian before answering so company definitions and prior failure modes shape the response.
- **Jury-and-Judge Review** — Use independent analysts to produce evidence-backed opinions, then have a judge weigh reasoning and escalate if needed.
- **Model Tier Selection** — Choose a capable model tier with plan mode, subagents, MCP support, and file editing for important work.

### Open Questions
- **How should a team decide when disagreement is large enough to escalate from one pass to a bigger jury?** — The workflow depends on knowing when consensus is insufficient, but the talk leaves the escalation threshold as an open operating rule.
- **What criteria should define whether an AI setup is too constrained to be trusted on important work?** — The speaker warns against cheap or crowbarred-in setups, but teams still need a practical boundary for acceptable capability.

### Derived Links And Source Material
- [[youtube-YZQsWVeN3rE-transcript]] — dedicated official recording transcript.
- [[youtube-YZQsWVeN3rE]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/YZQsWVeN3rE--2026-07-01-alex-bauer-how-juries-and-librarians-can-solve-gtm-s-ai-trust-problem.json`.

### Speaker Context
- No speaker profile is attached in the official schedule data.

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[alex-bauer]]

## Official YouTube Recording
- [[youtube-YZQsWVeN3rE|Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech]] — official AI Engineer YouTube recording published 2026-07-11.
- Evidence status: [[youtube-YZQsWVeN3rE-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-YZQsWVeN3rE]] - dedicated official event recording.
- [[youtube-YZQsWVeN3rE-transcript]] - dedicated official recording transcript.

- Source video: `youtube-YZQsWVeN3rE`
- Slide deck: [[youtube-YZQsWVeN3rE-slides|Slides: Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech]] — 4 visible slide image(s).
![[assets/slides/YZQsWVeN3rE/slide-001.jpg]]
![[assets/slides/YZQsWVeN3rE/slide-002.jpg]]
![[assets/slides/YZQsWVeN3rE/slide-003.jpg]]
- Slide-derived themes for `youtube-YZQsWVeN3rE`: juries, librarians, solve, trust, problem, alex, bauer, upside.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/YZQsWVeN3rE.txt` (2,901 words).

## Transcript Markdown
- [[youtube-YZQsWVeN3rE-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/YZQsWVeN3rE.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-YZQsWVeN3rE` — 2,901 transcript words; 3 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-YZQsWVeN3rE`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-YZQsWVeN3rE`: product, first, data, important, back, team, go-to-market, give.
- Slide-derived themes for `youtube-YZQsWVeN3rE`: juries, librarians, solve, trust, problem, alex, bauer, upside.
- Evidence links for `youtube-YZQsWVeN3rE` (primary event evidence): [[youtube-YZQsWVeN3rE]], [[youtube-YZQsWVeN3rE-transcript]], [[youtube-YZQsWVeN3rE-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
