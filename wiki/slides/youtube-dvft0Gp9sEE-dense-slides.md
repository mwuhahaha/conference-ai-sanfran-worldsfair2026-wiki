---
title: "Dense Slides: Analyzing 10,000 Sales Calls With AI In 2 Weeks — Charlie Guo"
category: "slides"
video_id: "dvft0Gp9sEE"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Analyzing 10,000 Sales Calls With AI In 2 Weeks — Charlie Guo

## Source Video
[Analyzing 10,000 Sales Calls With AI In 2 Weeks — Charlie Guo](https://www.youtube.com/watch?v=dvft0Gp9sEE)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/dvft0Gp9sEE/slide-001.jpg]]

- Source scene image: `frame-00007.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.37`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/dvft0Gp9sEE/slide-002.jpg]]

- Source scene image: `frame-00023.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.13`
- Slide-only rule: `visual-bright-slide`
