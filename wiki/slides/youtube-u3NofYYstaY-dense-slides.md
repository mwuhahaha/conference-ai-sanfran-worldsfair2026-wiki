---
title: "Dense Slides: Cohere for VPs of AI: Vivek Muppalla"
category: "slides"
video_id: "u3NofYYstaY"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Cohere for VPs of AI: Vivek Muppalla

## Source Video
[Cohere for VPs of AI: Vivek Muppalla](https://www.youtube.com/watch?v=u3NofYYstaY)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/u3NofYYstaY/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/u3NofYYstaY/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Dense multi-column company overview with many small logos and labels; OCR will read the details better than manual triage.

Slide text:

> S cohere SELECT INVESTORS STRATEGIC PARTNERS
> AIE nwIDLA ORACLE ORACLE
> Founded 2019 TADICAL coptai Schroders Ldex Vernuron Mknsy aws
> Team +300 NIRALSSAT DTCP LSANOUA accenture
> Offices Ean Frncisce, Sen Vort Tortnto.Lendon inovia Sertrel
> JXJLOLAI S32
> Microsoft smol ai

Classification audit: `raw/sources/slide-ai-classification/dense/u3NofYYstaY/audit.json`
