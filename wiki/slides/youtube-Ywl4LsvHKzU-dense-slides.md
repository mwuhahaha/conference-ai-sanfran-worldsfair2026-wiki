---
title: "Dense Slides: RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot"
category: "slides"
video_id: "Ywl4LsvHKzU"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot

## Source Video
[RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot](https://www.youtube.com/watch?v=Ywl4LsvHKzU)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/Ywl4LsvHKzU/slide-001.jpg]]

- Source scene image: `frame-00004.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `171.56`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/Ywl4LsvHKzU/slide-002.jpg]]

- Source scene image: `frame-00007.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.13`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/Ywl4LsvHKzU/slide-003.jpg]]

- Source scene image: `frame-00012.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.96`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/Ywl4LsvHKzU/slide-004.jpg]]

- Source scene image: `frame-00014.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.65`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/Ywl4LsvHKzU/slide-005.jpg]]

- Source scene image: `frame-00015.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `173.18`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/Ywl4LsvHKzU/slide-006.jpg]]

- Source scene image: `frame-00018.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `174.65`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/Ywl4LsvHKzU/slide-007.jpg]]

- Source scene image: `frame-00020.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `172.88`
- Slide-only rule: `visual-bright-slide`
