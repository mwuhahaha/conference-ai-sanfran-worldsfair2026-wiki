---
title: "Dense Slides: Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize"
category: "slides"
video_id: "SbcQYbrvAfI"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize

## Source Video
[Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize](https://www.youtube.com/watch?v=SbcQYbrvAfI)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/SbcQYbrvAfI/slide-001.jpg]]

- Source scene image: `frame-00007.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `166.25`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-002.jpg]]

- Source scene image: `frame-00010.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `166.32`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-003.jpg]]

- Source scene image: `frame-00023.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `171.92`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-004.jpg]]

- Source scene image: `frame-00024.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `166.28`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-005.jpg]]

- Source scene image: `frame-00026.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `170.24`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-006.jpg]]

- Source scene image: `frame-00027.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `168.52`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-007.jpg]]

- Source scene image: `frame-00029.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `166.25`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-008.jpg]]

- Source scene image: `frame-00033.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `168.57`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-009.jpg]]

- Source scene image: `frame-00034.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `165.83`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-010.jpg]]

- Source scene image: `frame-00036.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `166.55`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-011.jpg]]

- Source scene image: `frame-00053.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `167.1`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-012.jpg]]

- Source scene image: `frame-00065.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `165.81`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-013.jpg]]

- Source scene image: `frame-00069.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `165.58`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-014.jpg]]

- Source scene image: `frame-00071.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `165.51`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-015.jpg]]

- Source scene image: `frame-00074.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `165.2`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-016.jpg]]

- Source scene image: `frame-00075.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `164.24`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-017.jpg]]

- Source scene image: `frame-00080.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `164.13`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-018.jpg]]

- Source scene image: `frame-00089.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `165.23`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-019.jpg]]

- Source scene image: `frame-00090.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `165.13`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-020.jpg]]

- Source scene image: `frame-00092.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `164.46`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-021.jpg]]

- Source scene image: `frame-00093.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `163.2`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-022.jpg]]

- Source scene image: `frame-00102.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `164.04`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-023.jpg]]

- Source scene image: `frame-00103.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `164.17`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-024.jpg]]

- Source scene image: `frame-00104.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `165.86`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-025.jpg]]

- Source scene image: `frame-00106.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `165.66`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-026.jpg]]

- Source scene image: `frame-00107.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `163.16`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-027.jpg]]

- Source scene image: `frame-00110.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `164.05`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-028.jpg]]

- Source scene image: `frame-00114.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `164.99`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-029.jpg]]

- Source scene image: `frame-00115.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `164.09`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-030.jpg]]

- Source scene image: `frame-00117.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `169.37`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-031.jpg]]

- Source scene image: `frame-00118.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `164.41`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/SbcQYbrvAfI/slide-032.jpg]]

- Source scene image: `frame-00121.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `172.19`
- Slide-only rule: `visual-bright-slide`
