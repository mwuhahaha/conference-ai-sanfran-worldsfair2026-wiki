---
title: "Dense Slides: Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j"
category: "slides"
video_id: "B9h9ovW5H9U"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j

## Source Video
[Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j](https://www.youtube.com/watch?v=B9h9ovW5H9U)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/B9h9ovW5H9U/slide-001.jpg]]

- Source scene image: `frame-00012.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.88`
- Slide-only rule: `visual-bright-slide`
