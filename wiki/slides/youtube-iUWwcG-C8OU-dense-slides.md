---
title: "Dense Slides: Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS"
category: "slides"
video_id: "iUWwcG-C8OU"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS

## Source Video
[Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](https://www.youtube.com/watch?v=iUWwcG-C8OU)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
No slide-like frames are visible after AI slide classification. Rejected frames remain stored as evidence and are listed below.

### Hidden Non-Slide Evidence
- [`slide-001.jpg`](/assets/dense-slides/iUWwcG-C8OU/slide-001.jpg) — `speaker_stage` confidence `0.99`; Stage shot with speaker and audience; projected screen text is too small to treat as a readable presentation slide.

Classification audit: `raw/sources/slide-ai-classification/dense/iUWwcG-C8OU/audit.json`
