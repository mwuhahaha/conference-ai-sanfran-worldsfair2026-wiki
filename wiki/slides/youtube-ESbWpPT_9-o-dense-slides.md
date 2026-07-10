---
title: "Dense Slides: Run Frontier AI at Home — Alex Cheema, EXO Labs"
category: "slides"
video_id: "ESbWpPT_9-o"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Run Frontier AI at Home — Alex Cheema, EXO Labs

## Source Video
[Run Frontier AI at Home — Alex Cheema, EXO Labs](https://www.youtube.com/watch?v=ESbWpPT_9-o)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
No slide-like frames are visible after AI slide classification. Rejected frames remain stored as evidence and are listed below.

### Hidden Non-Slide Evidence
- [`slide-001.jpg`](/assets/dense-slides/ESbWpPT_9-o/slide-001.jpg) — `other` confidence `0.0`; missing batch classifier result
- [`slide-002.jpg`](/assets/dense-slides/ESbWpPT_9-o/slide-002.jpg) — `other` confidence `0.0`; missing batch classifier result
- [`slide-003.jpg`](/assets/dense-slides/ESbWpPT_9-o/slide-003.jpg) — `other` confidence `0.0`; missing batch classifier result
- [`slide-004.jpg`](/assets/dense-slides/ESbWpPT_9-o/slide-004.jpg) — `other` confidence `0.0`; missing batch classifier result

Classification audit: `raw/sources/slide-ai-classification/dense/ESbWpPT_9-o/audit.json`
