---
title: "AI Engineer World's Fair 2026 Agent Guidance"
type: "project-guidance"
project: "AI Engineer World's Fair 2026 Wiki"
source_scope: "public AIE conference intelligence wiki"
---

# AI Engineer World's Fair 2026 Agent Guidance

This repository is a standalone public wiki for AI Engineer World's Fair 2026. It is source-bounded: official schedule and speaker data are canonical for conference facts, while YouTube, transcript, slide/OCR, company-site, product-doc, and public-profile sources are supporting context.

## Start Here

1. Read `AGENTS.md` for local operating rules.
2. Read `wiki/resources/agent-source-index.md` for the source map and script index.
3. Read `wiki/resources/source-boundary.md` before adding claims from transcripts, OCR, slides, or public company/profile sources.
4. Use existing markdown shape in `wiki/` before creating new page patterns.

## Allowed Source Layers

- Official AI Engineer World's Fair 2026 site and schedule/speaker JSON mirrors under `raw/sources/`.
- Public AI Engineer YouTube metadata, captions, livestream transcript bundles, and related transcript helper output.
- Local Whisper fallback transcripts when public captions are missing.
- Local slide extraction, reconstructed slide crops, dense scene-detection slides, and OCR outputs.
- Public source-of-source links when directly relevant: official company sites, product docs, public professional profiles, and speaker-provided social/profile links.

## Rules

- Do not import private Miami notes, personal diary content, queue state, unrelated Obsidian vault material, or heavy local media caches into the publishable wiki.
- Keep official schedule facts distinct from supporting source layers.
- Treat OCR as best-effort unless checked against the embedded slide image or reconstructed crop.
- Company pages should become full articles where possible and cross-reference related people and scheduled sessions.
- Record new source conventions in `wiki/resources/agent-source-index.md` and `AGENTS.md`.
