---
title: "Dense Slides: Teaching Gemini to Speak YouTube: Adapting LLMs for Video Recommendations to 2B+DAU - Devansh Tandon"
category: "slides"
video_id: "LxQsQ3vZDqo"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Teaching Gemini to Speak YouTube: Adapting LLMs for Video Recommendations to 2B+DAU - Devansh Tandon

## Source Video
[Teaching Gemini to Speak YouTube: Adapting LLMs for Video Recommendations to 2B+DAU - Devansh Tandon](https://www.youtube.com/watch?v=LxQsQ3vZDqo)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/LxQsQ3vZDqo/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/LxQsQ3vZDqo/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Product/UI screenshot slide with multiple embedded mobile screens and small labels; OCR should handle the screenshot text better than manual transcription.

Slide text:

> AIE HIGHLIGHTS EXTENOEO CHESSTIPS COUNTERPLAY CREATING
> Cahs (henTey 0444 Others
> 100
> seE Dems Karubs TIPS CHESS
> Home WatchNext Shorts Search
> oogle
> Microsoft smol ai

![[assets/dense-slides/LxQsQ3vZDqo/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/LxQsQ3vZDqo/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Personalized Recommendation Problem
> f(user, context) ≈ recs
> User Context Recs

![[assets/dense-slides/LxQsQ3vZDqo/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/LxQsQ3vZDqo/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/border-trim/opencv-adaptive`.
- OCR decision: ready — Diagram slide with multiple small labels, captions, and surface names; OCR is appropriate for the small text and layout labels.

Slide text:

> Home
> AIE Gemini Vidoo Rotrlovsl WatchNext Search Shorts
> Music
> YouTube LRM Ranking Video Experiments
> Base Gemini checkpoint, adapted for YouTube Itions Aligned to tasks Served across surfaces Google Draulut
> Microsoft smop

![[assets/dense-slides/LxQsQ3vZDqo/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/LxQsQ3vZDqo/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: none.
- OCR decision: ready — Content slide with multiple small example cards, prompt/output boxes, and short IDs; OCR is likely better than manual reading for the dense embedded text.
![[assets/dense-slides/LxQsQ3vZDqo/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/LxQsQ3vZDqo/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: advanced OCR `rapidocr-live/full`.
- OCR decision: ready — Dense prompt-and-example slide with small text boxes and thumbnail captions; OCR is the right first pass.

Slide text:

> Us.Android Userdemo 24yr old,Female OLYNPIC
> AIE Watch history Context video MENS400M
> CHALI 200 Champiors Menls 4x100n Final IParis
> WatchNext:men's trackraces,nowomen
> LRMprompt
> User:region Us|24 years female devlce
> tle WHAT ACOMEBACK!IMen's 4OOm Paris2024 highlights SemanticID PARIS2O24 7.0 7.00
> Watch history: SID1Taylor Swift 100 260.00 Kria Hni 100320.00 401260.008 LRM:findsrelated women'sraces UNCATCHEEnwordnecod40m hudes|Pais Olymgics N8C toots Sydey McLaoghin-Leronewas U5woendosingincedle in40lylo fhOlyict Paris Olymgics NBC Ipots
> Google Yolibe
> Microsoft smol?


Classification audit: `raw/sources/slide-ai-classification/dense/LxQsQ3vZDqo/audit.json`
