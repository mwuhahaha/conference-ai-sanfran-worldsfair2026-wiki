---
title: "Dense Slides: New York Times' Connections: A Case Study on NLP in Word Games — Shafik Quoraishee, NYT Games"
category: "slides"
video_id: "P_uhFGH4J9Y"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: New York Times' Connections: A Case Study on NLP in Word Games — Shafik Quoraishee, NYT Games

## Source Video
[New York Times' Connections: A Case Study on NLP in Word Games — Shafik Quoraishee, NYT Games](https://www.youtube.com/watch?v=P_uhFGH4J9Y)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/P_uhFGH4J9Y/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/P_uhFGH4J9Y/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> About Me
> Game/AI Developer at The New York Times
> Worked previously for Business Insider, The NBA, MTV and the Department of Defense

![[assets/dense-slides/P_uhFGH4J9Y/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/P_uhFGH4J9Y/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Caveats to the Work You Are About to See
> This is all my own independent research and experimentation, and not currently specifically based on New York Time’s internal research


Classification audit: `raw/sources/slide-ai-classification/dense/P_uhFGH4J9Y/audit.json`
