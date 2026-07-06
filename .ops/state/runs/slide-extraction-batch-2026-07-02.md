---
type: run-receipt
scope: project-local
status: partial
updated: 2026-07-02T23:26:41Z
---

# Slide Extraction Batch 2026-07-02

## Inputs

- Existing speaker-matched YouTube map: `raw/sources/speaker-video-map.json`
- Existing caption status map: `raw/sources/related-video-caption-status.json`
- Videos processed:
  - `Xfl50508LZM`
  - `B9h9ovW5H9U`
  - `dvft0Gp9sEE`
  - `wFTVEDYVJT0`
  - `bk0TmxoZlUY`

## Output

- 5 slide deck pages under `wiki/slides/`
- 80 extracted slide/frame images under `wiki/assets/slides/`
- OCR text for all 80 extracted frames under `raw/sources/slide-ocr/`
- Supporting slide links inserted into related talk and resource pages
- 7 subject/topic pages created or updated from video/session context:
  - `agent-evaluations`
  - `agent-memory`
  - `agentic-search`
  - `coding-agents`
  - `inference-engineering`
  - `mcp`
  - `voice-agents`

## Notes

- The extractor samples full video frames, dedupes visually similar frames, and embeds the resulting images. It does not crop projected slides.
- Local OCR is installed project-locally under `.local/ocr/root`; OCR is best-effort and noisy for full-stage video frames.
- Continue remaining related videos in batches with `python3 scripts/extract_video_slides.py --start <offset> --limit <count>`.
