---
title: "AIE Wiki Generation Delta"
category: "resources"
sourceLabels:
  - "Local wiki comparison"
  - "Build logic comparison"
  - "Source-boundary review"
---

# AIE Wiki Generation Delta

This page records the factual delta between four local AI Engineer wiki generations inspected on 2026-07-10:

- AI Engineer World's Fair 2024 local fixture wiki.
- AI Engineer Miami 2026 local public wiki app.
- AI Engineer World's Fair 2025 local fixture wiki.
- This AI Engineer World's Fair 2026 public static wiki.

The comparison is about wiki-building logic and source boundaries. It is not a claim that one event had better content than another.

## Date Anchors

| Wiki | Event date information visible in the inspected sources | Inspection note |
|---|---:|---|
| AI Engineer World's Fair 2024 | The inspected overview identifies the event year as 2024; it does not expose calendar-day event dates in the overview or source-boundary page. | Local fixture wiki served from a static HTML export. |
| AI Engineer Miami 2026 | April 20, 2026 and April 21, 2026. | The Miami overview names two transcript files, one for each conference day. |
| AI Engineer World's Fair 2025 | The inspected overview identifies the event year as 2025; it does not expose calendar-day event dates in the overview or source-boundary page. | Local fixture wiki served from a static HTML export. |
| AI Engineer World's Fair 2026 | June 28-July 2, 2026. | Current public wiki event days are New Engineer Orientation, Workshop Day and Welcome Reception, Keynotes and Breakouts, World Cup and Multi-Track Programming, and Final Day and Last Chance Expo. |

## Scale At Inspection Time

| Wiki | Talks | People | Companies | Tools | Topics | Events | Evidence / media-specific pages | Notes |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| World's Fair 2024 | 180 | 170 | 108 | 5 | 20 | Not exposed as event-day pages in the inspected output | 180 evidence pages, 89 transcript pages, 88 synthesis pages, 88 claim pages, 88 quote pages | The source-boundary page reports 471 synthesis pages and 1,413 public source citations on synthesis pages. |
| Miami 2026 | 28 | 29 | 26 | 38 | 55 | 2 | 4 resource pages | The local app reports 186 total pages and a read-only public-share project. |
| World's Fair 2025 | 271 | 287 | 157 | 0 | 21 | Not exposed as event-day pages in the inspected output | 271 evidence pages | The source-boundary page reports 736 synthesis pages and 2,208 public source citations on synthesis pages. |
| World's Fair 2026 | 560 | 555 | 344 | 62 | 16 | 5 | 226 resource pages, 104 transcript pages, 418 slide pages | Current wiki also has question, harness, playbook, evaluation, and policy layers. |

Counts are filesystem or local API counts from the inspected local wiki outputs. They are build-shape facts, not event-size claims.

## Source Boundary Delta

### World's Fair 2024

The 2024 local wiki is a `specific_event` fixture output. Its source-boundary page says it was generated from local fixture objects and did not perform live source discovery, transcript processing, browser automation, external scripts, network access, deployment, or repository creation.

Included source classes were:

- official event fixture URLs;
- official or supporting video fixture URLs;
- corrected local transcript fixture snippets copied into evidence pages.

The logic split synthesis pages from evidence pages. The overview explicitly says official program facts, transcript synthesis, derived knowledge, and slide/OCR evidence remain separately labeled in integrated views.

### Miami 2026

Miami changed the logic from fixture-first to transcript-first. Its overview says the wiki combines:

- two allowed transcript files;
- the official conference website;
- clearly labeled public-web supporting context from company, product, documentation, or GitHub-style public URLs.

The Miami source videos did not have directly available transcripts, so audio was downloaded and transcribed with Whisper. The two transcript files became the primary corpus for the April 20 and April 21 pages.

Miami also changed the serving model. It uses a static Express app that reads markdown, renders wikilinks, builds backlinks and graph data at request time, and exposes read-only API routes. Mutating authoring endpoints are intentionally blocked for the public deployment.

### World's Fair 2025

The 2025 local wiki keeps the 2024 fixture pattern but at larger scale. Its source-boundary page has the same core restriction: generated from local fixture objects only, with no live source discovery, transcript processing, browser automation, external scripts, network access, deployment, or repository creation.

Included source classes were the same class of inputs as 2024:

- official event fixture URLs;
- official or supporting video fixture URLs;
- corrected local transcript fixture snippets copied into evidence pages.

The visible category model covers talks, people, companies, tools, and topics, but the inspected output had zero tool pages. The 2025 fixture output therefore expanded session/person/company/topic coverage without adopting Miami's richer tool/topic graph behavior.

### World's Fair 2026

The 2026 wiki changes the logic again. It is schedule-first, public-static, and source-bounded:

- official AI Engineer World's Fair 2026 schedule and speaker data are canonical for dates, titles, times, tracks, rooms, speakers, and affiliations;
- official AI Engineer World's Fair San Francisco 2026 videos are primary event video sources for media, transcripts, and slide evidence;
- related non-event YouTube videos are supporting context only, not first-class event evidence;
- public profile and company-site links are supporting context unless they come from the official schedule or official speaker roster.

The 2026 build also adds source layers that are not present in the inspected 2024/2025 fixture overviews:

- talk/video/transcript mapping;
- YouTube caption and local Whisper transcript handling;
- video frame extraction;
- slide OCR and RapidOCR repair;
- reconstructed slide crops and dense slide pages;
- content-derived topics;
- tools, questions, harnesses, playbooks, evaluations, and policies;
- static graph data and an agent-readable public index.

## Logic Changes By Generation

| Change | 2024 fixture | Miami 2026 | 2025 fixture | World's Fair 2026 |
|---|---|---|---|---|
| Primary corpus | Local fixture objects. | Two Whisper transcript files plus official conference website. | Local fixture objects. | Official schedule and speaker data, then confirmed event media and derived evidence layers. |
| Event dates | Event year visible; calendar dates not visible in inspected overview/source-boundary. | Exact days visible: 2026-04-20 and 2026-04-21. | Event year visible; calendar dates not visible in inspected overview/source-boundary. | Exact span visible: 2026-06-28 through 2026-07-02. |
| Evidence separation | Explicit synthesis/evidence separation. | Transcript-derived, conference-site, and public-web source labels. | Explicit synthesis/evidence separation. | Official schedule, primary event video, supporting video, transcript, OCR, slide, and public-profile roles. |
| Video handling | Fixture URLs and copied transcript snippets only. | Downloaded YouTube audio and Whisper transcripts. | Fixture URLs and copied transcript snippets only. | Official event recordings are first-class; non-event videos are supporting context only. |
| Graph/backlinks | Agent index and rendered static pages. | Backlinks and graph data built by the read-only app at request time. | Static fixture pages; the inspected local server did not expose `/agent-index.json`. | Static graph dataset and `/graph/` page generated at build time. |
| Public contract | Local fixture validation output. | Public-share, read-only app; mutating routes blocked. | Local fixture validation output. | Standalone static public repo/site with markdown backing files and `/agent-index.md`. |

## Practical Takeaways For This Wiki

- Keep Miami's strong idea: a conference-native wiki should explain sources, dates, event-day entry points, graph navigation, and topic synthesis plainly.
- Keep the 2024/2025 fixture discipline: synthesis and evidence records must remain distinct.
- Keep the 2026 evidence boundary stricter than simple YouTube matching: only actual World's Fair San Francisco 2026 event recordings should become first-class video evidence.
- Keep the public contract static and read-only: generated graph data, markdown mirrors, and agent indexes are safer than runtime mutation for the published site.
