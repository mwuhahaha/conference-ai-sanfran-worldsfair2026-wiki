---
title: "Dense Slides: Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face"
category: "slides"
video_id: "OV56RddyFuU"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face

## Source Video
[Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face](https://www.youtube.com/watch?v=OV56RddyFuU)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/OV56RddyFuU/slide-001.jpg]]

- Source scene image: `frame-00003.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `169.88`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-002.jpg]]

- Source scene image: `frame-00004.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.55`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-003.jpg]]

- Source scene image: `frame-00006.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `175.39`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-004.jpg]]

- Source scene image: `frame-00007.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `174.01`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-005.jpg]]

- Source scene image: `frame-00009.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.59`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-006.jpg]]

- Source scene image: `frame-00013.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `169.06`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-007.jpg]]

- Source scene image: `frame-00014.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `170.49`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-008.jpg]]

- Source scene image: `frame-00015.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `171.22`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-009.jpg]]

- Source scene image: `frame-00017.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.04`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-010.jpg]]

- Source scene image: `frame-00018.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `171.72`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-011.jpg]]

- Source scene image: `frame-00019.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `171.73`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-012.jpg]]

- Source scene image: `frame-00023.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `169.06`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-013.jpg]]

- Source scene image: `frame-00024.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `176.34`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-014.jpg]]

- Source scene image: `frame-00026.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `171.75`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-015.jpg]]

- Source scene image: `frame-00027.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `169.52`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-016.jpg]]

- Source scene image: `frame-00030.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `172.4`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-017.jpg]]

- Source scene image: `frame-00031.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.19`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-018.jpg]]

- Source scene image: `frame-00032.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `177.15`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-019.jpg]]

- Source scene image: `frame-00044.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `170.78`
- Slide-only rule: `visual-bright-slide`
![[assets/dense-slides/OV56RddyFuU/slide-020.jpg]]

- Source scene image: `frame-00045.jpg`
- Crop: `visible-slide-crop` `[0, 37, 960, 503]` score `170.67`
- Slide-only rule: `visual-bright-slide`
