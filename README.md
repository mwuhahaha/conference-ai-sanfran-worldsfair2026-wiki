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
python3 scripts/run_slide_ocr_pipeline.py --all --skip-perfect --engine rapidocr --internal-eval-log
python3 scripts/run_slide_ocr_pipeline.py --all --skip-perfect --engine rapidocr --vision-rescue --vision-provider auto --internal-eval-log
python3 scripts/run_slide_ocr_pipeline.py --all --skip-perfect --no-live-ocr --internal-eval-log
```

The external video discovery tool searches YouTube beyond the official AI Engineer channel, scores candidates against the official schedule, treats high-confidence matches as secondary sources only, and writes its audit report to `wiki/resources/external-video-discovery.md`.

The talk synthesis tool adds transcript/source-backed sections to talk pages. The highlight generator publishes both the normal highlights index and the grouped `Highlighted Concepts, People, And Talks` map.

The slide OCR pipeline rereads weak or suspicious slide frames with local OCR engines, crop detection, OpenCV preprocessing, and high-contrast variants. It compares those outputs with existing Tesseract/RapidOCR/reconstructed/dense OCR artifacts, updates canonical slide OCR only when the score improves, refreshes slide markdown, regenerates dependent tool/topic indexes, and writes an audit report. For a narrow debug run, use `python3 scripts/run_slide_ocr_pipeline.py --limit 50 --no-build`.

For a fuller quality pass, run `python3 scripts/run_slide_ocr_pipeline.py --all --skip-perfect --engine rapidocr --internal-eval-log`. The five free/local improvement paths now supported by the toolkit are: OpenCV crop/threshold preprocessing, RapidOCR live rereads, PaddleOCR rescue reads, EasyOCR/docTR adapter hooks for CPU/GPU installs that provide Torch cleanly, and Surya as an explicit opt-in after checking model-weight license terms. PaddleOCR is available as a targeted rescue engine, but it is too slow for default whole-corpus runs on this host. Operator-verified text belongs under `raw/sources/slide-ocr-operator-verified/`; run `python3 scripts/run_slide_ocr_pipeline.py --all --skip-perfect --no-live-ocr --internal-eval-log` to merge those corrections without rerunning live OCR. Internal eval logs are written under `.ops/state/cache/` and are intentionally ignored by git.

When OCR is visibly bad, use the AI vision rescue layer instead of only adding OCR engines: `python3 scripts/run_slide_ocr_pipeline.py --all --skip-perfect --engine rapidocr --vision-rescue --vision-provider auto --internal-eval-log`. The rescue tool reads low-confidence/manual-queue slide frames with a vision model, writes accepted text to `raw/sources/slide-ocr-ai-vision/`, and then reruns a no-live merge. It prefers free local Ollama vision when available; it uses the OpenAI Responses API only when `OPENAI_API_KEY` is set or `--vision-provider openai` is chosen. The OpenAI model is configurable with `OPENAI_VISION_MODEL`.

Future video slide extraction can use scene-change frame sampling and sharpness replacement with `python3 scripts/extract_video_slides.py --scene-detect --video-id <id>`.

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
