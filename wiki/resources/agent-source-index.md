---
title: "Agent Navigation Index"
category: "resources"
sourceLabels: ["Agent guidance", "Navigation index", "Public wiki map"]
---

# Agent Navigation Index

This is the agent-readable navigation map for the AI Engineer World's Fair 2026 wiki. Point an agent here when it needs to consume the public wiki, find the right page type, follow evidence links, or understand how topics, talks, people, companies, slides, quotes, and resources connect.

Raw standalone markdown for agents: https://aie-worldsfair2026.plusrobot.ai/agent-index.md

Human-rendered page: https://aie-worldsfair2026.plusrobot.ai/resources/agent-source-index/

## Start Here
- Home overview: https://aie-worldsfair2026.plusrobot.ai/
- Full index: https://aie-worldsfair2026.plusrobot.ai/index/
- Search page: https://aie-worldsfair2026.plusrobot.ai/search/
- Topics index: https://aie-worldsfair2026.plusrobot.ai/topics/
- Talks index: https://aie-worldsfair2026.plusrobot.ai/talks/
- People index: https://aie-worldsfair2026.plusrobot.ai/people/
- Companies index: https://aie-worldsfair2026.plusrobot.ai/companies/
- Slides index: https://aie-worldsfair2026.plusrobot.ai/slides/
- Quotes index: https://aie-worldsfair2026.plusrobot.ai/quotes/
- Tools index: https://aie-worldsfair2026.plusrobot.ai/tools/
- Source boundary and evidence confidence: https://aie-worldsfair2026.plusrobot.ai/resources/source-boundary/

## URL Rules
- Every rendered page uses a stable lowercase slug URL ending in `/`.
- Every rendered page has a backing markdown file at `/md/<same-page-id>.md`.
- To convert a rendered URL to markdown, remove the leading slash and trailing slash, then prefix `/md/` and append `.md`: `/topics/agentic-web/` becomes `/md/topics/agentic-web.md`.
- The home page is backed by `/md/overview.md`.
- A talk page is `/talks/<date-speaker-title-slug>/`.
- A person page is `/people/<person-slug>/`.
- A company page is `/companies/<company-slug>/`.
- A topic page is `/topics/<topic-slug>/`.
- A slide page is `/slides/<youtube-video-id-kind>/`.
- A quote page is `/quotes/<quote-slug>/`.
- A resource page is `/resources/<resource-slug>/`.
- Wiki links in markdown use `[[slug]]` or `[[slug|label]]`; on the public site these resolve to the matching rendered URL.
- If a rendered page is hard to parse, fetch its markdown backing file first and use the rendered page only for images or visual inspection.

## Corpus Map
- Talks: 560 rendered talk pages; official schedule sessions indexed: 560.
- People: 553 rendered people pages; official speakers indexed: 552.
- Companies: 340 rendered company pages.
- Topics: 12 synthesis pages across repeated conference themes.
- Resources: 190 pages for source maps, YouTube evidence, livestreams, and processing audits.
- Slides: 383 slide pages; standard decks: 180; reconstructed decks: 107; dense decks: 93.
- Quotes: 59 selected quote pages tied back to source videos and topics.
- Tools: 61 tool/protocol/entity pages generated from the conference evidence layer.
- Events: 5 day/event overview pages.

## Navigation Strategy
- If you know a talk title or speaker, start with `/search/`, `/talks/`, or `/people/`.
- If you know a theme, start with `/topics/`, then follow related talks, people, companies, tools, quotes, and resources from that topic page.
- For page content extraction, prefer `/md/...` markdown backing files over scraping rendered HTML.
- If you need primary schedule context, use the talk page first. Talk pages preserve title, speaker, company, date, track, room, and schedule labels.
- If you need a speaker's context, use the person page, then follow company, scheduled talks, related videos, and social/profile links when present.
- If you need organizational context, use the company page, then follow related people and scheduled talks.
- If you need media evidence, use the talk/video/transcript map and the YouTube resource pages before relying on a transcript or slide page.
- If you need slide evidence, prefer reconstructed slide pages for readable cropped slides, then use dense or full-stage slide pages as supporting views.
- If you need reusable concepts, use topics and tools pages; they synthesize across multiple talks and resources.
- If you need a concise evidence-backed excerpt, use quote pages and then follow their source video, related topic, and scheduled talk links.

## High-Value Entry Points
- Agentic Web topic: https://aie-worldsfair2026.plusrobot.ai/topics/agentic-web/
- Agentic Search topic: https://aie-worldsfair2026.plusrobot.ai/topics/agentic-search/
- Coding Agents topic: https://aie-worldsfair2026.plusrobot.ai/topics/coding-agents/
- Agent Evaluations topic: https://aie-worldsfair2026.plusrobot.ai/topics/agent-evaluations/
- Agent Memory topic: https://aie-worldsfair2026.plusrobot.ai/topics/agent-memory/
- AI Sandboxes topic: https://aie-worldsfair2026.plusrobot.ai/topics/ai-sandboxes/
- MCP topic: https://aie-worldsfair2026.plusrobot.ai/topics/mcp/
- Inference Engineering topic: https://aie-worldsfair2026.plusrobot.ai/topics/inference-engineering/
- Talk/video/transcript map: https://aie-worldsfair2026.plusrobot.ai/resources/talk-video-transcript-map/
- Livestreams resource: https://aie-worldsfair2026.plusrobot.ai/resources/worldsfair-2026-livestreams/
- Slide library: https://aie-worldsfair2026.plusrobot.ai/resources/slide-library/
- Reconstructed slide library: https://aie-worldsfair2026.plusrobot.ai/resources/reconstructed-slide-library/
- Dense slide library: https://aie-worldsfair2026.plusrobot.ai/resources/dense-slide-library/

## Evidence Confidence
- Official schedule and speaker facts are canonical for dates, titles, speakers, organizations, tracks, rooms, and session status.
- Related YouTube pages are supporting context unless the page explicitly confirms an exact recording match.
- Transcripts are useful evidence, but speaker/session matching and caption quality may vary.
- Slide OCR is best-effort. For important claims, inspect the embedded slide image or reconstructed crop.
- Topic, tool, quote, and company pages are synthesis layers. Follow their linked talks, resources, videos, slides, and source-boundary notes before treating a claim as primary.

## Media And Source Pointers
- Official conference website: https://www.ai.engineer/worldsfair/2026
- Official schedule mirror status: present; sessions indexed: 560.
- Official speaker mirror status: present; speakers indexed: 552.
- AI Engineer YouTube channel: https://www.youtube.com/@aiDotEngineer
- Channel video metadata status: present; video entries: 804.
- Channel livestream metadata status: present; livestream entries: 32.
- Related talk/video rows indexed: 153.
- Cached speaker-matched transcript files: 76.
- Cached livestream transcript files: 3.

## Agent Task Recipes
- To answer `what was said about X`: search X, inspect the relevant topic page, open related talks, then follow video/transcript and slide links.
- To answer `who is connected to X`: inspect the topic or company page, then follow Related People and Related Scheduled Sessions.
- To answer `which companies are involved`: start with `/companies/`, search the company name, then cross-check people and talks linked from that company page.
- To answer `what evidence supports this`: prefer talk pages and resource pages, then use transcripts, quotes, and slide pages as supporting evidence.
- To answer `where should I browse next`: use the related links at the bottom of the current page; the wiki is intentionally cross-linked across talks, people, companies, topics, tools, quotes, resources, and slides.
