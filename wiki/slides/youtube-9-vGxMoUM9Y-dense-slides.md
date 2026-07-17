---
title: "Dense Slides: Trust, but Verify: Shreya Rajpal"
category: "slides"
video_id: "9-vGxMoUM9Y"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Trust, but Verify: Shreya Rajpal

## Source Video
[Trust, but Verify: Shreya Rajpal](https://www.youtube.com/watch?v=9-vGxMoUM9Y)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/9-vGxMoUM9Y/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/9-vGxMoUM9Y/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> About me
> Current CEO & Cofounder @ Guardrails AI
> Past ML Infra lead @ MLOps Co,
> ML @ Self driving cars,
> Classical AI & Deep learning research

![[assets/dense-slides/9-vGxMoUM9Y/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/9-vGxMoUM9Y/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive` reconciled by agent.
- OCR decision: ready — Dense multi-panel screenshot slide with several embedded text blocks and quotes; better suited for OCR than manual transcription in this triage pass.

Slide text:

> We're seeing a cambrian explosion of applications in AI
> 
> Auto-GPT May Be The Strong AI Tool That Surpasses ChatGPT
> 
> Seriously, software engineering as we have known it is dead in the water.
> This AI is better than at least 95% of coders. And to the extent it is not, it delivers 1000x productivity improvements to complement them.
> 
> We have now officially entered the Age of AI.
> 
> CAN AI TREAT MENTAL ILLNESS?
> 
> How Generative AI Will Change Sales

![[assets/dense-slides/9-vGxMoUM9Y/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/9-vGxMoUM9Y/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/right-72/contrast` reconciled by agent.
- OCR decision: ready — Chart-heavy slide with small labels, source URL, and multiple plotted annotations; OCR is more appropriate than hand transcription here.

Slide text:

> The reality
> Path to 100 Million Users
> One Month Retention
> Incumbents
> AI-First Companies
> Source: https://www.sequoiacap.com/article/generative-ai-act-two/

![[assets/dense-slides/9-vGxMoUM9Y/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/9-vGxMoUM9Y/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/full` reconciled by agent.
- OCR decision: ready — Chart-heavy slide with small labels and source text; OCR is more suitable than direct transcription in this pass.

Slide text:

> The reality
> Path to 100 Million Users (stylized)
> -2 months   9 months   30 months   41 months   55 months   61 months
> Months from launch
> One Month Retention
> Incumbents
> AI-First Companies
> 63% Median
> 42% Median
> Guardrails AI
> Source: https://www.sequoiacap.com/article/generative-ai-act-two/

![[assets/dense-slides/9-vGxMoUM9Y/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/9-vGxMoUM9Y/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Alex Graveley
> @alexgraveley
> Simple LLM technique that helps a lot (but you might not be using): add a constraint checker to ensure valid generation. On violation, inject what was generated and the rule violation, and regenerate.

![[assets/dense-slides/9-vGxMoUM9Y/slide-006.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/9-vGxMoUM9Y/slide-006.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Guardrails AI acts as a safety firewall around your LLMs

![[assets/dense-slides/9-vGxMoUM9Y/slide-007.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/9-vGxMoUM9Y/slide-007.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast` reconciled by agent.
- OCR decision: ready — Dense diagram slide with many small labels and boxed flows.

Slide text:

> Guardrails AI under-the-hood
> 
> Creating a guard
> Select type of output to validate
> RAIL Spec
> Pydantic Model
> String
> LLM Callable
> Add prompt & instructions
> Initialize guard from spec
> Invoke Guard
> 
> Calling a guard
> Guard invokes LLM API
> LLM API Returns
> LLM Output is validated
> Invalid
> Valid
> Logs
> Return output
> 
> Guardrails AI

![[assets/dense-slides/9-vGxMoUM9Y/slide-008.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/9-vGxMoUM9Y/slide-008.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> What Guardrails AI does
> Guardrails AI is a fully open source library that offers
> Framework for creating custom validators
> Orchestration of prompting → verification → re-prompting
> Library of commonly used validators for multiple use cases
> Specification language for communicating requirements to LLM

![[assets/dense-slides/9-vGxMoUM9Y/slide-009.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/9-vGxMoUM9Y/slide-009.html)
- AI slide classifier: `content_slide` confidence `0.92`
- Text source: agent_vision.

Slide text:

> What Guardrails AI does
> Guardrails AI is a fully open source library that offers
> Framework for creating custom validators
> Orchestration of prompting → verification → re-prompting
> Library of commonly used validators for multiple use cases
> Specification language for communicating requirements to LLM

![[assets/dense-slides/9-vGxMoUM9Y/slide-010.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/9-vGxMoUM9Y/slide-010.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> How do I prevent LLM hallucinations?
> Provenance Guardrails
> Every LLM utterance should have a source of truth.

![[assets/dense-slides/9-vGxMoUM9Y/slide-011.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/9-vGxMoUM9Y/slide-011.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast` reconciled by agent.
- OCR decision: ready — Diagram and example output are small and better suited for OCR than manual transcription.

Slide text:

> Example: Validating "correctness"
> Application Logic
> Guardrails AI
> LLM Logic
> Prompt
> LLM API
> Raw Output
> Reconstruct Prompt
> Fail Validation
> Verification Logic
> Pass Validation
> How do I change my password?
> Raw Output
> 1. Log into your account.
> 2. Go to user settings by clicking on the top left corner.
> 3. Click change password.

![[assets/dense-slides/9-vGxMoUM9Y/slide-012.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/9-vGxMoUM9Y/slide-012.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> More examples of validations
> Make sure my code is executable
> Never give financial or healthcare advice
> Don’t ask private questions
> Don’t mention competitors
> Ensure each sentence is from a verified source and is accurate
> No profanity is mentioned in text
> Prompt injection protection
> Never expose prompt or sources

![[assets/dense-slides/9-vGxMoUM9Y/slide-013.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/9-vGxMoUM9Y/slide-013.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Learn more
> Github: github.com/ShreyaR/guardrails
> Website: guardrailsai.com
> Twitter: @ShreyaR or @guardrails_ai

Classification audit: `raw/sources/slide-ai-classification/dense/9-vGxMoUM9Y/audit.json`
