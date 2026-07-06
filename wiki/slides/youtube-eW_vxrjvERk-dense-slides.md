---
title: "Dense Slides: Connecting the Dots with Context Graphs — Stephen Chin, Neo4j"
category: "slides"
video_id: "eW_vxrjvERk"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Connecting the Dots with Context Graphs — Stephen Chin, Neo4j

## Source Video
[Connecting the Dots with Context Graphs — Stephen Chin, Neo4j](https://www.youtube.com/watch?v=eW_vxrjvERk)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/eW_vxrjvERk/slide-001.jpg]]

- Source scene image: `frame-00026.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.67`
- Slide-only rule: `visual-bright-slide`
