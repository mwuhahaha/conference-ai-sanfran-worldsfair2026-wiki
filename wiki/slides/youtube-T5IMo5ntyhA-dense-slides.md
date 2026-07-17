---
title: "Dense Slides: Stop Using RAG as Memory — Daniel Chalef, Zep"
category: "slides"
video_id: "T5IMo5ntyhA"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Stop Using RAG as Memory — Daniel Chalef, Zep

## Source Video
[Stop Using RAG as Memory — Daniel Chalef, Zep](https://www.youtube.com/watch?v=T5IMo5ntyhA)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/T5IMo5ntyhA/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/T5IMo5ntyhA/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> PROBLEM
> When the Media Assistant Remembers Everything Except Your Listening Habits...
> • Daniel likes jazz music.
> • Daniel plays NPR podcast.
> • Daniel wakes up at 7am.
> • Daniel went to the gym.
> • Daniel listened to The Daily.
> • Daniel prefers mornings.
> • Daniel's dog is named Melody.
> • Daniel turned up the volume.
> • Daniel asked about vegan recipes.
> • Daniel paused Taylor Swift song.

Classification audit: `raw/sources/slide-ai-classification/dense/T5IMo5ntyhA/audit.json`
