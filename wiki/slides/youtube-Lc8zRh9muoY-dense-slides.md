---
title: "Dense Slides: Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft"
category: "slides"
video_id: "Lc8zRh9muoY"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft

## Source Video
[Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft](https://www.youtube.com/watch?v=Lc8zRh9muoY)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/Lc8zRh9muoY/slide-001.jpg]]

- Source scene image: `frame-00012.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `169.54`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/Lc8zRh9muoY/slide-002.jpg]]

- Source scene image: `frame-00014.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `169.49`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/Lc8zRh9muoY/slide-003.jpg]]

- Source scene image: `frame-00017.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `170.41`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/Lc8zRh9muoY/slide-004.jpg]]

- Source scene image: `frame-00018.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.24`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/Lc8zRh9muoY/slide-005.jpg]]

- Source scene image: `frame-00030.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `167.44`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/Lc8zRh9muoY/slide-006.jpg]]

- Source scene image: `frame-00034.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.03`
- Slide-only rule: `visual-bright-slide`
