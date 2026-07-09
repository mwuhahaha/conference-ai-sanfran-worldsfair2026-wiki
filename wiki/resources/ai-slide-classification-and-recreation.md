---
title: "AI Slide Classification And Recreation"
category: "resources"
sourceLabels: ["AI vision", "Slide extraction", "Slide layout recreation"]
---

# AI Slide Classification And Recreation

`scripts/classify_and_recreate_slides.py` is the wiki-maker tool for separating real content slides from video frames that only look slide-adjacent. It uses the low-cost Codex vision model `gpt-5.4-mini` by default and does not read `OPENAI_API_KEY`.

## What It Keeps
- Presentation slides with meaningful text, diagrams, code, architecture, tables, or product screenshots used as slide content.
- Slides with an embedded speaker/video tile, as long as the slide content itself is readable and useful.

## What It Removes
- People standing on stage in front of a logo wall.
- Sponsor walls, starting-soon cards, blank frames, audience shots, and unreadable stage projections.
- Demo footage or UI video frames that are not clearly being used as a readable slide.

## Output
- Classification audit JSON: `raw/sources/slide-ai-classification/<video_id>/audit.json`
- Per-slide classifier JSON: `raw/sources/slide-ai-classification/<video_id>/slide-###.json`
- Text/layout HTML recreation: `wiki/assets/slide-recreations/<video_id>/slide-###.html`

## Example Results
- [[youtube-AheG9p_JXVw-slides]] — four Reelful stage-camera frames were removed because none were clear content slides.
- [Recreated "My Second Brain" slide](/assets/slide-recreations/ZRM_TfEZcIo/slide-001.html) — text and rough layout recreated from a retained content slide.
- [Recreated "My personal notes!" slide](/assets/slide-recreations/ZRM_TfEZcIo/slide-004.html) — simple title layout recreated from a retained content slide.

## Tool Invocation
```bash
env -u OPENAI_API_KEY python3 scripts/classify_and_recreate_slides.py \
  --video-id AheG9p_JXVw \
  --model gpt-5.4-mini \
  --remove-rejected
```

For the full OCR pipeline, pass one or more `--classify-video-id` values to `scripts/run_slide_ocr_pipeline.py`; add `--remove-non-slides` when rejected frames should be removed from the wiki deck.
