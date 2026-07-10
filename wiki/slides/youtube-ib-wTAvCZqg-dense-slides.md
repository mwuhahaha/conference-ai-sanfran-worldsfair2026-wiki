---
title: "Dense Slides: Architecting and Testing Controllable Agents: Lance Martin"
category: "slides"
video_id: "ib-wTAvCZqg"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Architecting and Testing Controllable Agents: Lance Martin

## Source Video
[Architecting and Testing Controllable Agents: Lance Martin](https://www.youtube.com/watch?v=ib-wTAvCZqg)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/ib-wTAvCZqg/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/ib-wTAvCZqg/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Small diagram labels and code-like text are better handled by OCR than direct transcription.

Slide text:

> Agents typically use tool (function) calling to execute steps
> AIE
> Hatwral lusgusge Paylotd Mtdtd far too!
> :(f:.+y.).:sw+ea! Wm+: sttp.2
> tef sttp_2(foo): too! Strtrtured Too!
> rtura b.r
> https:1/llianweng.qilhub.iq/cosis/2023-06-23-aqent
> 88 Microsoft smol?

![[assets/dense-slides/ib-wTAvCZqg/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/ib-wTAvCZqg/slide-002.html)
- AI slide classifier: `title_card` confidence `0.96`
- Text source: agent_vision.

Slide text:

> Architecting + testing reliable agents
> Lance Martin
> Software Engineer, LangChain

![[assets/dense-slides/ib-wTAvCZqg/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/ib-wTAvCZqg/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: none.
- OCR decision: ready — Dense code screenshot with small text; OCR will outperform manual reading.
- Slide text: not surfaced (`illegible` by AI classifier).
![[assets/dense-slides/ib-wTAvCZqg/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/ib-wTAvCZqg/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense chart labels and small comparison text; OCR is the cheaper pass.

Slide text:

> Retrieval is not guaranteed, reasoning harder than retrieval
> AIE Asktng cpt-l te rvtrir ur rutrlr+ & ratea 1. ), *r 1+ n+dlts (facts) in 4 slrgtt turn 12o.t++ t+ht+ (tattat +irtta ta+us 1t+)r+) 4t H+15u 4t +++ru 4yt4+ 11+sty Lsblo Gt-a te rrtrlrwa ll wiqoe fsrts Ia 1 tu
> I tf tts.r (t=tm (ttt) 0004 24100 C Llt C 7:400 ta 11000
> hltps://voutubeUlmyYQGhzs
> hltos://blog. langchain.dey/multi-needle-in-a:havstack
> aws


Classification audit: `raw/sources/slide-ai-classification/dense/ib-wTAvCZqg/audit.json`
