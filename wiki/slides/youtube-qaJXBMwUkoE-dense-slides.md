---
title: "Dense Slides: The 1,000x AI Engineer: Swyx"
category: "slides"
video_id: "qaJXBMwUkoE"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: The 1,000x AI Engineer: Swyx

## Source Video
[The 1,000x AI Engineer: Swyx](https://www.youtube.com/watch?v=qaJXBMwUkoE)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/qaJXBMwUkoE/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/qaJXBMwUkoE/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/center-82/opencv-adaptive`.
- OCR decision: ready — Dense multi-column diagram slide with small body copy; OCR will be more reliable than direct transcription.

Slide text:

> Sarnoffs Law On) Metcalfos Law Oh) Reed's Law O(2*n)
> Sarnoff's Law Metcalfe's Law Reed'sLaw
> X/N XIN
> V=n V=112
> Sourte, NFX'BANt
> increases In direct proportion to the The value of the network (M) sirc of the rctwork (n). to the square of the number ot Users in the network. The value of the network increases influence or interconnectedness). Networks may grov proportionally to the nelwork slze but there are forming groups that scale faster in value than others (becuse ot

Classification audit: `raw/sources/slide-ai-classification/dense/qaJXBMwUkoE/audit.json`
