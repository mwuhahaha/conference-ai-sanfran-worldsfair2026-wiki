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
- Knowledge graph: https://aie-worldsfair2026.plusrobot.ai/graph/
- Search page: https://aie-worldsfair2026.plusrobot.ai/search/
- Topics index: https://aie-worldsfair2026.plusrobot.ai/topics/
- Talks index: https://aie-worldsfair2026.plusrobot.ai/talks/
- People index: https://aie-worldsfair2026.plusrobot.ai/people/
- Companies index: https://aie-worldsfair2026.plusrobot.ai/companies/
- Slides index: https://aie-worldsfair2026.plusrobot.ai/slides/
- Transcripts index: https://aie-worldsfair2026.plusrobot.ai/transcripts/
- Quotes index: https://aie-worldsfair2026.plusrobot.ai/quotes/
- Tools index: https://aie-worldsfair2026.plusrobot.ai/tools/
- Highlights index: https://aie-worldsfair2026.plusrobot.ai/highlights/
- Claims index: https://aie-worldsfair2026.plusrobot.ai/claims/
- Conversations index: https://aie-worldsfair2026.plusrobot.ai/conversations/
- Patterns index: https://aie-worldsfair2026.plusrobot.ai/patterns/
- Questions index: https://aie-worldsfair2026.plusrobot.ai/questions/
- Harnesses index: https://aie-worldsfair2026.plusrobot.ai/harnesses/
- Playbooks index: https://aie-worldsfair2026.plusrobot.ai/playbooks/
- Evaluations index: https://aie-worldsfair2026.plusrobot.ai/evaluations/
- Policies index: https://aie-worldsfair2026.plusrobot.ai/policies/
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
- The graph browser is `/graph/`; its full static dataset is `/graph-data.json`.
- If a rendered page is hard to parse, fetch its markdown backing file first and use the rendered page only for images or visual inspection.

## Corpus Map
- Talks: 560 rendered talk pages; official schedule sessions indexed: 560.
- People: 555 rendered people pages; official speakers indexed: 552.
- Companies: 344 rendered company pages.
- Topics: 16 synthesis pages across repeated conference themes.
- Resources: 222 pages for source maps, YouTube evidence, livestreams, and processing audits.
- Slides: 418 slide pages; standard decks: 200; reconstructed decks: 107; dense decks: 94.
- Transcripts: 102 transcript markdown pages.
- Quotes: 68 selected quote pages tied back to source videos and topics.
- Tools: 62 tool/protocol/entity pages generated from the conference evidence layer.
- Claims: 1 evidence-backed claim pages.
- Conversations: 1 cross-page conversation maps.
- Patterns: 1 reusable AI engineering pattern pages.
- Questions: 8 question pages raised by the conference corpus.
- Harnesses: 7 evaluation or implementation harness pages.
- Playbooks: 5 reusable playbook pages.
- Evaluations: 8 evaluation design pages.
- Policies: 7 credibility or evidence-policy pages.
- Events: 5 day/event overview pages.

## Page Shapes
- Talk pages answer what happened, who presented, where and when it was scheduled, what the synthesized argument is, which topics/tools/companies connect to it, and what transcript/slide/video evidence backs it.
- Person pages identify the speaker, role/company, profile links when available, scheduled sessions, related videos, topics, companies, and source-backed context.
- Company pages explain what the organization does, why it matters in the conference graph, which people and sessions connect to it, and which public company/profile sources support the article.
- Topic pages synthesize what the topic is, why it matters, how and when to use it, origin/use-case context, related scheduled sessions, people, companies, tools, quotes, slides, transcripts, and resources.
- Resource, transcript, and slide pages are evidence layers. They should be cited or inspected before turning media-derived material into a confident claim.
- Claims, patterns, questions, harnesses, playbooks, evaluations, and policies are synthesis layers. Treat them as navigational and analytic pages that point back to talks, transcripts, slides, and resources.

## Navigation Strategy
- If you know a talk title or speaker, start with `/search/`, `/talks/`, or `/people/`.
- If you know a theme, start with `/topics/`, then follow related talks, people, companies, tools, quotes, and resources from that topic page.
- For page content extraction, prefer `/md/...` markdown backing files over scraping rendered HTML.
- If you need primary schedule context, use the talk page first. Talk pages preserve title, speaker, company, date, track, room, and schedule labels.
- If you need a speaker's context, use the person page, then follow company, scheduled talks, related videos, and social/profile links when present.
- If you need organizational context, use the company page, then follow related people and scheduled talks.
- If you need media evidence, use the talk/video/transcript map and the YouTube resource pages before relying on a transcript or slide page.
- If you need exact wording, fetch the transcript page under `/md/transcripts/...` and then cross-check the linked YouTube resource page.
- If you need slide evidence, prefer reconstructed slide pages for readable cropped slides, then use dense or full-stage slide pages as supporting views.
- If you need reusable concepts, use topics, tools, claims, patterns, questions, harnesses, playbooks, evaluations, and policies; they synthesize across multiple talks and resources.
- If a page is marked highlighted, use `/highlights/` as a curated index into especially important concepts, people, talks, and source pages.
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
- Knowledge graph: https://aie-worldsfair2026.plusrobot.ai/graph/
- Graph dataset: https://aie-worldsfair2026.plusrobot.ai/graph-data.json
- Talk/video/transcript map: https://aie-worldsfair2026.plusrobot.ai/resources/talk-video-transcript-map/
- External YouTube video discovery: https://aie-worldsfair2026.plusrobot.ai/resources/external-video-discovery/
- Livestreams resource: https://aie-worldsfair2026.plusrobot.ai/resources/worldsfair-2026-livestreams/
- Livestream talk segments: https://aie-worldsfair2026.plusrobot.ai/resources/livestream-talk-segments/
- Slide library: https://aie-worldsfair2026.plusrobot.ai/resources/slide-library/
- Reconstructed slide library: https://aie-worldsfair2026.plusrobot.ai/resources/reconstructed-slide-library/
- Dense slide library: https://aie-worldsfair2026.plusrobot.ai/resources/dense-slide-library/
- Transcript index: https://aie-worldsfair2026.plusrobot.ai/transcripts/
- Claims index: https://aie-worldsfair2026.plusrobot.ai/claims/
- Patterns index: https://aie-worldsfair2026.plusrobot.ai/patterns/
- Questions index: https://aie-worldsfair2026.plusrobot.ai/questions/
- Harnesses index: https://aie-worldsfair2026.plusrobot.ai/harnesses/
- Playbooks index: https://aie-worldsfair2026.plusrobot.ai/playbooks/
- Evaluations index: https://aie-worldsfair2026.plusrobot.ai/evaluations/
- Policies index: https://aie-worldsfair2026.plusrobot.ai/policies/
- Highlights index: https://aie-worldsfair2026.plusrobot.ai/highlights/

## Evidence Confidence
- Official schedule and speaker facts are canonical for dates, titles, speakers, organizations, tracks, rooms, and session status.
- Official AI Engineer World's Fair San Francisco 2026 livestreams and cut videos are primary event video sources for media, transcript, and slide evidence.
- Other YouTube pages, including external uploads, older AI Engineer talks, and videos from other AIE events, are supporting context unless manually promoted as exact official event recordings.
- Transcripts are useful evidence, but speaker/session matching and caption quality may vary.
- Slide OCR is best-effort. For important claims, inspect the embedded slide image or reconstructed crop.
- Topic, tool, quote, and company pages are synthesis layers. Follow their linked talks, resources, videos, slides, and source-boundary notes before treating a claim as primary.

## Media And Source Pointers
- Official conference website: https://www.ai.engineer/worldsfair/2026
- Official schedule mirror status: present; sessions indexed: 560.
- Official speaker mirror status: present; speakers indexed: 552.
- AI Engineer YouTube channel: https://www.youtube.com/@aiDotEngineer
- Channel video metadata status: present; video entries: 833.
- Channel livestream metadata status: present; livestream entries: 32.
- Related talk/video rows indexed: 153.
- Cached speaker-matched transcript files: 96.
- Cached livestream transcript files: 3.
- Cached external secondary-source transcript files: 2.
- External YouTube discovery rows: 21.
- High-confidence livestream talk timestamp matches: 11.

## Agent Task Recipes
- To answer `what was said about X`: search X, inspect the relevant topic page, open related talks, then follow video/transcript and slide links.
- To answer `who is connected to X`: inspect the topic or company page, then follow Related People and Related Scheduled Sessions.
- To answer `which companies are involved`: start with `/companies/`, search the company name, then cross-check people and talks linked from that company page.
- To answer `what evidence supports this`: prefer talk pages and resource pages, then use transcripts, quotes, and slide pages as supporting evidence.
- To answer `is this official or supporting evidence`: inspect Source Boundary, the page frontmatter/source labels, and the media/source section before relying on the claim.
- To answer `which markdown should I read`: convert the rendered URL to `/md/<page-id>.md`, or fetch `/agent-index.md` again for routing.
- To answer `where should I browse next`: use the related links at the bottom of the current page; the wiki is intentionally cross-linked across talks, people, companies, topics, tools, quotes, resources, and slides.
