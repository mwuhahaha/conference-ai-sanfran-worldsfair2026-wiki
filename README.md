# AI Engineer World's Fair 2026 Clean Wiki

Clean AIE-specific World’s Fair 2026 wiki built from the upgraded local project.

This directory keeps:
- generated official schedule pages
- people/company/talk/resource pages
- slide decks and reconstructed slide decks
- RapidOCR-improved OCR text
- livestream transcript bundles
- source summaries and audit receipts
- local scripts needed to rebuild or extend the wiki

This directory intentionally excludes heavyweight regeneration caches:
- `raw/video-cache/`
- `raw/slide-frames-tmp/`
- `raw/experiments/`
- `raw/tmp/`

Use the original `conference-ai-sanfran-worldsfair2026` directory if full video/frame regeneration caches are needed.

## Current Focus

This clean copy is meant to become the AIE-specific conference intelligence version of the World’s Fair wiki: not a generic personal wiki and not only a generated schedule archive.

Read:
- `.ops/plans/worldsfair-aie-specific-conversion-plan.md`
- `.ops/state/current.md`

## Validation

From this directory:

```bash
npm run build
```

The build writes the deployable static site to `dist/`.

## Wiki Toolkit

Useful recurring tools:

```bash
python3 scripts/discover_external_event_videos.py --write-wiki --import-high-confidence --update-talk-pages
python3 scripts/generate_transcript_markdown_pages.py
python3 scripts/generate_talk_synthesis.py --speaker "Liad Yosef"
python3 scripts/generate_highlights.py
python3 scripts/run_slide_ocr_pipeline.py
```

The external video discovery tool searches YouTube beyond the official AI Engineer channel, scores candidates against the official schedule, treats high-confidence matches as secondary sources only, and writes its audit report to `wiki/resources/external-video-discovery.md`.

The talk synthesis tool adds transcript/source-backed sections to talk pages. The highlight generator publishes both the normal highlights index and the grouped `Highlighted Concepts, People, And Talks` map.

The slide OCR pipeline rereads weak or suspicious slide frames with local RapidOCR/ONNX Runtime, crop detection, and high-contrast variants. It compares those outputs with existing Tesseract/RapidOCR/reconstructed/dense OCR artifacts, updates canonical slide OCR only when the score improves, refreshes slide markdown, regenerates dependent tool/topic indexes, and writes an audit report. For a narrow debug run, use `python3 scripts/run_slide_ocr_pipeline.py --limit 50 --no-build`.

## Static Site Export

This repository can be deployed as a static Cloudflare Pages site.

Local build:

```bash
npm run build
```

The build writes a pre-rendered static site to `dist/`.

Cloudflare Pages Git integration settings:

- Repository: `mwuhahaha/conference-ai-sanfran-worldsfair2026-wiki`
- Production branch: `main`
- Build command: `npm run build`
- Build output directory: `dist`
- Root directory: repository root
