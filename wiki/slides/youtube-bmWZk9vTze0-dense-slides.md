---
title: "Dense Slides: MCP is all you need — Samuel Colvin, Pydantic"
category: "slides"
video_id: "bmWZk9vTze0"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: MCP is all you need — Samuel Colvin, Pydantic

## Source Video
[MCP is all you need — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=bmWZk9vTze0)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
No slide-like frames are visible after AI slide classification. Rejected frames remain stored as evidence and are listed below.

### Hidden Non-Slide Evidence
- [`slide-001.jpg`](/assets/dense-slides/bmWZk9vTze0/slide-001.jpg) — `speaker_stage` confidence `0.99`; Stage shot with speaker, podium, and sponsor logos; projected content is only a partial demo view, not a readable presentation slide.

Classification audit: `raw/sources/slide-ai-classification/dense/bmWZk9vTze0/audit.json`
