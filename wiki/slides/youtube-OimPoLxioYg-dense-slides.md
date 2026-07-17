---
title: "Dense Slides: 120k players in a week: Lessons from the first viral CLIP app: Joseph Nelson"
category: "slides"
video_id: "OimPoLxioYg"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: 120k players in a week: Lessons from the first viral CLIP app: Joseph Nelson

## Source Video
[120k players in a week: Lessons from the first viral CLIP app: Joseph Nelson](https://www.youtube.com/watch?v=OimPoLxioYg)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/OimPoLxioYg/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OimPoLxioYg/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.78`
- Text source: none.
- Slide text: not surfaced (`decorative` by AI classifier).
![[assets/dense-slides/OimPoLxioYg/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OimPoLxioYg/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.

Slide text:

> The Premise: Convince an AI you're the best artist
> 1 GPT: Generate a prompt for users to draw
> 2 User: Draws prompt in MS Paint interface
> 3 CLIP: Judge vector similarity of text prompt and user image
> 4 ???: 120k players in one week, 7 requests per second

![[assets/dense-slides/OimPoLxioYg/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OimPoLxioYg/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: agent_vision.

Slide text:

> Prompt: A Raccoon Driving a Tractor

![[assets/dense-slides/OimPoLxioYg/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OimPoLxioYg/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: agent_vision.

Slide text:

> Prompt: A Bumblebee that Loves Capitalism

![[assets/dense-slides/OimPoLxioYg/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OimPoLxioYg/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Dense mixed text and diagram; better handled by OCR than manual transcription.

Slide text:

> How We're Using CLIP Go Deeper!
> CLIP: Trained on 400M image/text pairs, OpenAl, 2021
> text_embedding: how CLIP Paint.wtf Scoring
> mapsthepaint.wtfprompt into
> its feature space Image_embedding: how CLIP maps the user submission into X of thePaint.wtfPrompt CLIP's Interpretation CLip'sInterpretation of User-Submitted Drawing
> its feature space
> distance between the prompt and the user drawing Winning paint.wtf: minimizing Cosine Similarity X

![[assets/dense-slides/OimPoLxioYg/slide-008.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OimPoLxioYg/slide-008.html)
- AI slide classifier: `demo_video` confidence `0.95`
- Text source: agent_vision.

Slide text:

> Draw a gorilla gardening with grapes

![[assets/dense-slides/OimPoLxioYg/slide-009.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OimPoLxioYg/slide-009.html)
- AI slide classifier: `demo_video` confidence `0.95`
- Text source: agent_vision.

Slide text:

> Draw a gorilla gardening with grapes

![[assets/dense-slides/OimPoLxioYg/slide-010.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OimPoLxioYg/slide-010.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — dense comparison slide with small captions and example text; OCR is better for full extraction

Slide text:

> dmmnmhuiedbupina wosuossa Were all leaming here
> CLIP Can Read
> Draw a raccoon driving a tractor Gobs Rsnking: S86 cuA cf 10.187 ubmissiem Draw a raccoon driving a tractor Globst Rnking: 81 cit ot 10.187 swbmissioms A raccooh
> TRACTOR
> TRY AGAIN thoop crlr Geng Try AGAIn Rooe Wotr womg
> 10

![[assets/dense-slides/OimPoLxioYg/slide-012.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/OimPoLxioYg/slide-012.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — dense bullet list and table are OCR-suitable; keep text field minimal in triage

Slide text:

> Lessons fromBuildingPaint.wtfwith CLIP We're all learning here
> Roboflow Inference Makes Life Easy
> Serving done right. model license
> Built on the lessons of serving 1oom of API calls and thousands of hours of video. inference/eodels/clip interence/models/gaze inference/models/san Ml T, Apache 2.0 Apache 2.0
> Maximize throughput on your target inference/models/vit Apache 2.0
> hardware (GPU, CPU, edge) inference/models/yolact
> Use ready-to-go foundation models interence/models/yolovs AGPL-30
> Pull in over 50k pretrained models from interence/eodels/yolov7 GPL-3.0
> Roboflow Universe community interence/models/yolovs AGPL-3.0
> 14

### Hidden Non-Slide Evidence
- [`slide-006.jpg`](/assets/dense-slides/OimPoLxioYg/slide-006.jpg) — `demo_video` confidence `0.96`; Stage composite with live demo screen, presenter footage, and sponsor logos; not a readable presentation slide.
- [`slide-007.jpg`](/assets/dense-slides/OimPoLxioYg/slide-007.jpg) — `speaker_stage` confidence `0.17`; camera shot of speaker on stage with projected screen and sponsor logos; not a clean slide
- [`slide-011.jpg`](/assets/dense-slides/OimPoLxioYg/slide-011.jpg) — `speaker_stage` confidence `0.16`; camera shot of speaker and projected slide; not a clean slide frame

Classification audit: `raw/sources/slide-ai-classification/dense/OimPoLxioYg/audit.json`
