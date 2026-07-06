---
type: run-receipt
scope: project-local
status: completed-with-skips
updated: 2026-07-03T07:03:32Z
---

# Slide Extraction All Related Videos 2026-07-03

## Inputs

- `raw/sources/speaker-video-map.json`
- `raw/sources/related-video-caption-status.json`
- 107 distinct speaker-matched AI Engineer YouTube videos

## Output

- 105 slide deck pages under `wiki/slides/`
- 1,602 extracted slide/frame images under `wiki/assets/slides/`
- 1,602 OCR text files under `raw/sources/slide-ocr/`
- 1,576 non-empty OCR outputs
- `wiki/slides/slide-library.md` generated as the deck/coverage index
- `wiki/overview.md` updated with slide/OCR coverage
- OCR-derived subject signal counts added through `slide-library`

## Unresolved Skips

Two videos still failed at YouTube media download with HTTP 403:

- `gcseUQJ6Gbg` — Using OSS models to build AI apps with millions of users
- `liG97YXaTSA` — OpenThoughts: Data Recipes for Reasoning Models

They are recorded in `raw/sources/slide-extraction-failures.json`.

## Shared Logic Added

- Added `/garage/obsidian/scripts/native_youtube_slide_scan.py`
- Updated the YouTube import orchestrator to run a native slide scan after successful wiki ingest when the target project is event/research or has a `slides` category.
- Updated event/research project templates to include `slides`.
