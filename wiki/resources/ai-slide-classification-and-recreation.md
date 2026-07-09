---
title: "AI Slide Classification And Recreation"
category: "resources"
sourceLabels: ["AI vision", "Slide extraction", "Slide layout recreation"]
---

# AI Slide Classification And Recreation

`scripts/classify_and_recreate_slides.py` is the wiki-maker tool for separating real content slides from video frames that only look slide-adjacent. It uses the low-cost Codex vision model `gpt-5.4-mini` by default and does not read `OPENAI_API_KEY`.

Rejected frames are not deleted. They stay in `wiki/assets/...` and remain listed as evidence, but they are hidden from the visible slide sequence so the wiki does not present stage shots, logo walls, or demo footage as slides.

## What It Keeps
- Presentation slides with meaningful text, diagrams, code, architecture, tables, or product screenshots used as slide content.
- Slides with an embedded speaker/video tile, as long as the slide content itself is readable and useful.

## What It Hides From Slide View
- People standing on stage in front of a logo wall.
- Sponsor walls, starting-soon cards, blank frames, audience shots, and unreadable stage projections.
- Demo footage or UI video frames that are not clearly being used as a readable slide.

## Output
- Classification audit JSON: `raw/sources/slide-ai-classification/<deck_kind>/<video_id>/audit.json`
- Per-slide classifier JSON: `raw/sources/slide-ai-classification/<deck_kind>/<video_id>/slide-###.json`
- Text/layout HTML recreation: `wiki/assets/slide-recreations/<deck_kind>/<video_id>/slide-###.html`

## Example Results
- [[youtube-AheG9p_JXVw-slides]] — four Reelful stage-camera frames are hidden from slide view while retained as linked evidence.
- [[youtube-ZRM_TfEZcIo-dense-slides]] — full dense pass keeps eleven visible content slides and hides one speaker bio card as evidence.
- [Recreated "My Second Brain" dense slide](/assets/slide-recreations/dense/ZRM_TfEZcIo/slide-001.html) — text and rough layout recreated from a retained dense content slide.
- [Recreated "Forget the infrastructure you think you need" dense slide](/assets/slide-recreations/dense/ZRM_TfEZcIo/slide-006.html) — text and rough layout recreated from a retained dense content slide.
- Dense spot checks also classified four frames each for `APh1Vx0oLmQ` and `4sX_He5c4sI`; those partial runs wrote audits and recreations without rewriting the full visible deck pages.

## Tool Invocation
```bash
env -u OPENAI_API_KEY python3 scripts/classify_and_recreate_slides.py \
  --video-id AheG9p_JXVw \
  --deck-kind slides \
  --model gpt-5.4-mini \
  --hide-rejected
```

For the full OCR pipeline, pass one or more `--classify-video-id` values to `scripts/run_slide_ocr_pipeline.py`; set `--classify-deck-kind slides`, `dense`, or `reconstructed` depending on the deck being processed. The legacy `--remove-non-slides` flag now hides rejected frames from visible wiki sections while keeping evidence files.
