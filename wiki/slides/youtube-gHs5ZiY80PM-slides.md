---
title: "Slides: You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia"
category: "slides"
video_id: "gHs5ZiY80PM"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia

## Source Video
[You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia](https://www.youtube.com/watch?v=gHs5ZiY80PM)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/gHs5ZiY80PM/slide-001.jpg]]

OCR text:

> nVIDIA
> You Might Not Need
> 50 Diffusion Steps
> AlEngineer
> EURORE

![[assets/slides/gHs5ZiY80PM/slide-002.jpg]]

OCR text:

> Diffusion models: What & Why
> + Generate mages/video by iteratrvely denoising from random nase
> - Each step: neural network predicts and removes nose — refines output
> a *& + Quality comes from many refinement passes {typically 20-50 steps)
> * od
> * * + Powering today’s leading models
> bal x + FLUX 2 (Black Forest Labs} — SOTA text-to-image, photoreakstic
> * bd of + LTX-2 3 (Laghtsicks) — 22B params, 4K@SOfps video + audro
> + Wan 2.7, HunyuanVideo. Seedance 20.
> - Used for: text-to-image, text-to-video, image editing, 3D generation, inpainting, super-resolution, world simulation,
> scientific modeling
> 0 Perenowee , . PaciatDenowe wen) ,
> a a on Bar.
> ae : PRE 5 50
> be pee LSS
> mo eae Sas Bene
> , ons Ser en eee
> a eee es P -
> pre
> = <i Pd Engineering the future of Al
> hoe Bi

![[assets/slides/gHs5ZiY80PM/slide-003.jpg]]

OCR text:

> Quantization: Performance & Quality
> ara as ; ‘
> a | a ae 3 eed a in ‘a a : in oy
> es aaa “=
> ‘ * ied vw ee
> rm x bake a a ie von a rd ed
> * * = P .
> * * *
> = | . ag . p iO i f
> a i an oat
> “= ¥ ov aaa “-
> OLY with TensorRT-LLM - Visual Gen Run a pre-quantized ckpt from HF
> # With NVFP4 quantization F ” 7
> python visual_gen_flux.py --model_path black-forest- id dale ance
> labs/FLUX.2-dev --prompt “A cat’ --linear_type trtllm-nvfp4
> " Pes
> ; 7 a ae ste ces
> : ah ee aa a
> oa Al Engineer
> ES] f ral EUROPE
> Ro ;

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
