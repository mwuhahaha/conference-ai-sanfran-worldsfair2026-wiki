---
title: "Dense Slides: From Mixture of Experts to Mixture of Agents with Super Fast Inference - Daniel Kim & Daria Soboleva"
category: "slides"
video_id: "tzRvcTEapzo"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: From Mixture of Experts to Mixture of Agents with Super Fast Inference - Daniel Kim & Daria Soboleva

## Source Video
[From Mixture of Experts to Mixture of Agents with Super Fast Inference - Daniel Kim & Daria Soboleva](https://www.youtube.com/watch?v=tzRvcTEapzo)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/tzRvcTEapzo/slide-001.jpg]]

- Source scene image: `frame-00004.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.17`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/tzRvcTEapzo/slide-002.jpg]]

- Source scene image: `frame-00005.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.61`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/tzRvcTEapzo/slide-003.jpg]]

- Source scene image: `frame-00009.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.4`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/tzRvcTEapzo/slide-004.jpg]]

- Source scene image: `frame-00052.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.01`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/tzRvcTEapzo/slide-005.jpg]]

- Source scene image: `frame-00077.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.18`
- Slide-only rule: `visual-bright-slide`
