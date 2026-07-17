---
title: "Dense Slides: Letting AI Interface with your App with MCP — Kent C Dodds"
category: "slides"
video_id: "EyZiAp0pelw"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Letting AI Interface with your App with MCP — Kent C Dodds

## Source Video
[Letting AI Interface with your App with MCP — Kent C Dodds](https://www.youtube.com/watch?v=EyZiAp0pelw)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/EyZiAp0pelw/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/EyZiAp0pelw/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> What did Jarvis do?
> Compiled database from SHEILD, FBI, CIA datasets
> Generated a UI on demand
> Accessed "public records"
> Brought up "thermogenic signatures"
> "Take away everywhere there's been a mandarin attack"
> Showed related news articles, interviews, database records, etc.
> Created a flight plan for Tennessee
> Door bell

Classification audit: `raw/sources/slide-ai-classification/dense/EyZiAp0pelw/audit.json`
