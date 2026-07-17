# AI Engineer World's Fair 2026 Wiki

AI Engineer World's Fair 2026 ran June 28-July 2, 2026 in San Francisco, with main programming at Moscone West. This standalone wiki was built from the official AI Engineer World's Fair schedule and speaker data, then enriched with public AI Engineer YouTube uploads, livestream transcripts, local Whisper fallback transcripts where needed, extracted video frames, slide OCR, reconstructed slide crops, quote selection, and content-derived topic links.

The result is a schedule-first conference intelligence map. Official session and speaker pages are the backbone; YouTube videos, transcripts, OCR, reconstructed slides, quotes, topics, people, and company pages are layered on top as supporting evidence and navigation paths.

## Source Links
- Source repository: [mwuhahaha/conference-ai-sanfran-worldsfair2026-wiki](https://github.com/mwuhahaha/conference-ai-sanfran-worldsfair2026-wiki).
- Official event site: [AI Engineer World's Fair 2026](https://www.ai.engineer/worldsfair/2026).
- Agent navigation index: [agent-index.md](/agent-index.md).

## Quick Access
- [[index]] — full wiki index and section guide.
- [agent-index.md](/agent-index.md) — raw markdown navigation guide for agents consuming the wiki.
- [[agent-source-index]] — human-rendered copy of the agent navigation guide.
- Every page also has a backing markdown file under `/md/`; for example, [Agentic Web markdown](/md/topics/agentic-web.md).
- [[agentic-web|Agentic Web]] — topic page for agent-facing web surfaces, browser automation, agent-readable catalogs, and HTML/web substrates.
- [[highlights/index|Highlights]] — operator-selected pages that receive extra source search and expansion.
- [[talk-video-transcript-map]] — official talks mapped to related YouTube videos and transcript status.
- [[slide-library]] — extracted full-frame slide decks from related videos.
- [[reconstructed-slide-library]] — cleaner slide-region crops produced by the advanced slide scanner.
- [[dense-slide-library]] — high-density slide views for fast inspection.
- [[worldsfair-2026-livestreams]] — livestream uploads, transcript status, and slide extraction.
- [[advanced-slide-logic-page-audit]] — RapidOCR and reconstructed-slide audit.
- [[source-boundary]] — corpus rules and evidence confidence.

## Corpus
- 560 official schedule sessions generated as talk pages.
- 553 people pages generated from the official speaker roster plus schedule-only names.
- 341 company pages generated from speaker affiliations and selected public company enrichment.
- 191 resource pages for official data, source boundaries, YouTube evidence, and processing audits.
- 383 slide pages, including full-stage frames, reconstructed crops, and dense slide views.
- 12 topic pages seeded from repeated World’s Fair themes.
- 62 tool pages for tools, protocols, services, and technical systems referenced by the corpus.
- 5 highlight pages for operator-selected targets that deserve extra source search and expansion.
- 5 event/day pages for the conference flow.

## Evidence Layers
- Official schedule and speaker data establish dates, titles, speakers, organizations, tracks, and the event structure.
- Public AI Engineer YouTube metadata identifies related videos by speaker and title matching.
- YouTube transcripts are used where available; local Whisper fallback is part of the ingestion path when captions are missing.
- Slide evidence comes from video frame extraction, OCR, RapidOCR repair passes, and OpenCV crop reconstruction.
- Topic pages synthesize repeated language across titles, transcripts, slide text, and session clusters.

## Slide Intelligence
Slides are first-class material in this wiki because many World’s Fair videos are stage recordings rather than clean deck exports.

- 107 extracted video slide decks are tracked in [[slide-library]].
- 1,842 slide/frame images are embedded in deck pages.
- 107 reconstructed companion decks are tracked in [[reconstructed-slide-library]].
- 1,729 reconstructed slide-region images are saved under `wiki/assets/reconstructed-slides/`.
- 1,826 extracted frames have non-empty local OCR text.
- 291 weak OCR frames were improved with local RapidOCR/ONNX after the first Tesseract pass.
- 115 weak frames were classified as unreadable or non-slide cutaways during the RapidOCR audit.

## Current Theme Map
- [[coding-agents]] — coding agents as tools, teammates, infrastructure, and organizational pressure.
- [[software-factories]] — self-driving software, agentic SDLC, code review, CI/CD, and production loops.
- [[agent-evaluations]] — evals, harnesses, observability, quality gates, and agent performance review.
- [[agent-memory]] — memory, context engineering, knowledge agents, and long-horizon work.
- [[agent-security]] — permissions, provenance, identity, governance, and agent supply chain risk.
- [[agentic-search]] — search, retrieval, context graphs, GraphRAG, and agent web navigation.
- [[voice-agents]] — realtime voice systems, speech-to-speech models, and voice UX failures.
- [[inference-engineering]] — inference engines, model serving, open weights, optimization, and deployment tradeoffs.
- [[mcp]] — MCP servers, tool layers, agent interfaces, and operational governance.
- [[ai-sandboxes]] — sandboxes, browsers, environments, and safe agent execution.
- [[autoresearch]] — research agents, data quality, parameter golf, and scientific workflows.

## Slide/OCR Coverage
- [[slide-library]] tracks 423 extracted video slide decks.
- 3282 slide/frame images are embedded in deck pages.
- 3216 extracted frames have non-empty local OCR text.
- OCR is best-effort because most videos are full-stage captures rather than direct slide exports.
