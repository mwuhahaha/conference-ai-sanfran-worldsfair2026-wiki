---
title: "Reconstructed Slides: Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS"
category: "slides"
video_id: "so9l_MwS2yg"
sourceLabels: ["Cropped public YouTube video frames", "Local OpenCV slide-region detection", "Local RapidOCR"]
---

# Reconstructed Slides: Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS

## Source Video
[Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS](https://www.youtube.com/watch?v=so9l_MwS2yg)

## Method
This deck is reconstructed from the existing video frame captures by detecting likely slide regions with OpenCV, cropping/upscaling those regions, deduplicating similar crops, and OCRing the cropped slide images locally. It is a cleaner companion to the full-stage frame deck.

## Reconstructed Slides
![[assets/reconstructed-slides/so9l_MwS2yg/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/so9l_MwS2yg/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.94`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Screenshot-heavy slide with small UI/code text; OCR is likely better than manual transcription.

Slide text:

> THE DAILY REALITY
> Hack
> VSCode AA
> AIE uxport foction sothxiodleere(res,rs,next）1 i/ ey s this nall in stugieg? const token reg.hudtrs.avthoriatioo FOCUSED
> ATEEPTION
> MP GoogleDeepMind

![[assets/reconstructed-slides/so9l_MwS2yg/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/so9l_MwS2yg/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.

Slide text:

> The agents aren't the bottleneck.
> We are.
> Agents
> Verification
> Your attention

![[assets/reconstructed-slides/so9l_MwS2yg/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/so9l_MwS2yg/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: agent_vision.

Slide text:

> YOU'RE NOT IMAGINING IT
> SIMON WILLISON - Lenny's Podcast, Apr 2 2026
> I fire up 4 parallel agents and I'm wiped out by 11 AM. Finding our new limits is a personal skill we need to learn.
> I'm seeing this in my own work on the Applied AI team.
> Here's how I recommend finding developer balance.

![[assets/reconstructed-slides/so9l_MwS2yg/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/reconstructed/so9l_MwS2yg/slide-005.html)
- AI slide classifier: `diagram` confidence `0.96`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Mixed diagram plus embedded screenshot with small labels; OCR should recover the detailed body copy and UI text better than manual triage.

Slide text:

> CLOSETHELOOPWITHYOURBODY
> +★ ★? ★ ++ AIE ★ ★ got 4 hours of sleop. yourself. The system that ships your code also knows you Your physical context flows into the agentic loop. It adjusts the plan. lt protects you from Ring Oura MCP Server Code Claude How to Connect Your Oura Ring to Claude Desktop with MCP OURA MCP N Claude
> Z. Ler's tnock out sl 6 renniirg Bdea today
> reoonerend 2 sdoed mex soday. Pash che odher & to tomorron. Pl'tueg mopa Ah' seupnw 'dhep wzt p tro nok ppeD a Your body seys sose yp let's Detee?..1
> MCP AlEngineer
> EUROPE


### Hidden Non-Slide Evidence
- [`slide-001.jpg`](/assets/reconstructed-slides/so9l_MwS2yg/slide-001.jpg) — `sponsor_logo` confidence `0.98`; Sponsor/logo wall only.
- [`slide-006.jpg`](/assets/reconstructed-slides/so9l_MwS2yg/slide-006.jpg) — `other` confidence `0.0`; missing batch classifier result
- [`slide-007.jpg`](/assets/reconstructed-slides/so9l_MwS2yg/slide-007.jpg) — `speaker_stage` confidence `0.98`; Stage photo with presenter and audience; projected slide is not the primary readable slide frame.
- [`slide-008.jpg`](/assets/reconstructed-slides/so9l_MwS2yg/slide-008.jpg) — `sponsor_logo` confidence `0.99`; Logo/title card rather than a substantive presentation slide.

Classification audit: `raw/sources/slide-ai-classification/reconstructed/so9l_MwS2yg/audit.json`
