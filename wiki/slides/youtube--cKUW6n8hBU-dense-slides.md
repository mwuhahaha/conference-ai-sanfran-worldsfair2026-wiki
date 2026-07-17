---
title: "Dense Slides: DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners"
category: "slides"
video_id: "-cKUW6n8hBU"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners

## Source Video
[DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners](https://www.youtube.com/watch?v=-cKUW6n8hBU)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/-cKUW6n8hBU/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/-cKUW6n8hBU/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Overview
> DSPy is a declarative framework for building modular AI software.
> It allows you to iterate fast on structured code, rather than brittle strings, and offers algorithms that compile AI programs into effective prompts and weights for your language models
> https://dspy.ai

![[assets/dense-slides/-cKUW6n8hBU/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/-cKUW6n8hBU/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Use Cases Lighting Round
> What we’ll cover:
> - Simple sentiment classifier
> - Structured information from a PDF
> - Multimodal extraction
> - Web research agent (using Tools)
> - Detect boundaries of a document
> - Recursively summarize an arbitrary-length document
> - GEPA example

![[assets/dense-slides/-cKUW6n8hBU/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/-cKUW6n8hBU/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.

Slide text:

> DSPy allows you to decompose logic into a program that treats LLMs as a first class citizen ...
> 
> ... without having to tweak prompts (unless you want to)

![[assets/dense-slides/-cKUW6n8hBU/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/-cKUW6n8hBU/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.93`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast` reconciled by agent.
- OCR decision: ready — Dense small bullet text on the right and a cropped top line make OCR more appropriate than direct transcription.

Slide text:

> Why I'm such
> an advocate
> 
> Allows you to create computer programs that use LLMs
> as inline function calls
> 
> Programs which you happen to be able to optimize - it's a
> programming paradigm, not a wholesale framework, and not
> “optimizer-first”
> 
> Is built with a systems mindset; you encode intent and
> structure in a way that is transferable
> 
> Your program design likely moves slower than AI advancements (at
> least so far)

![[assets/dense-slides/-cKUW6n8hBU/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/-cKUW6n8hBU/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive` reconciled by agent.
- OCR decision: ready — Diagram-style slide with six text boxes and small labels is better suited to OCR extraction.

Slide text:

> Core Concepts
> 
> Signatures
> Specify what you want,
> not how; let the LLM
> figure it out
> 
> Modules
> Structure your program
> logically
> 
> Tools
> Interact with the outside
> world - or the rest of the
> program
> 
> Adapters
> Customizable prompt
> formatters: think JSON,
> BAML, XML, etc.
> 
> Optimizers
> Optimize your DSPy
> program, ML-style
> (let the LLM figure it out!)
> 
> Metrics
> Define what to optimize
> against (can be multiple
> things)

![[assets/dense-slides/-cKUW6n8hBU/slide-006.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/-cKUW6n8hBU/slide-006.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Signatures
> How you “express your declarative intent”
> Can be simple strings or complex Class-based objects

![[assets/dense-slides/-cKUW6n8hBU/slide-007.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/-cKUW6n8hBU/slide-007.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Optimizers
> DSPy has various built-in primitives that allow you to then optimize your program. This allows you to quantitatively improve your performance and cost profile.
> 
> “A DSPy optimizer is an algorithm that can tune the parameters of a DSPy program (i.e., the prompts and/or the LM weights) to maximize the metrics you specify, like accuracy.”

![[assets/dense-slides/-cKUW6n8hBU/slide-008.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/-cKUW6n8hBU/slide-008.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> “DSPy is not an optimizer. It’s set of programming abstractions (signatures, modules) that can be optimized.”
> - Omar Khattab @lateinteraction

![[assets/dense-slides/-cKUW6n8hBU/slide-009.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/-cKUW6n8hBU/slide-009.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: agent_vision.

Slide text:

> The reason that this is tricky is quite subtle. It’s the fact that
> anytime you use an LLM to assign a reward, those LLMs are giant
> things with billions of parameters, and they’re gameable. If you’re
> reinforcement learning with respect to them, you will find
> adversarial examples for your LLM judges, almost guaranteed.
> 
> So you can’t do this for too long. You do maybe 10 steps or 20
> steps, and maybe it will work, but you can’t do 100 or 1,000. I
> understand it’s not obvious, but basically the model will find little
> cracks. It will find all these spurious things in the nooks and
> crannies of the giant model and find a way to cheat it
> 
> - Andrej Karpathy (via the Dwarkesh Podcast)

![[assets/dense-slides/-cKUW6n8hBU/slide-010.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/-cKUW6n8hBU/slide-010.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast` reconciled by agent.
- OCR decision: ready — Dense slide with paper title, author list, table, and caption; OCR is better suited than direct transcription in this triage pass.

Slide text:

> GEPA: Reflective Prompt Evolution Can Outperform
> Reinforcement Learning
> 
> Lakshya A Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav Singhvi, Herumb Shandilya, Michael J Ryan, Meng Jiang, Christopher Potts, Koushik Sen, Alexandros G. Dimakis, Ion Stoica, Dan Klein, Matei Zaharia, Omar Khattab
> UC Berkeley, Stanford University, BespokeLabs.ai, Notre Dame, Databricks, MIT
> 
> Chris Potts
> https://www.youtube.com/watch?v=0bkwd9OYqfk
> 
> Model  HotpotQA  IFBench  Hover  PUPA  Aggregate  Improvement
> Qwen3-8B
> Baseline  42.33  36.90  35.33  80.82  48.85  —
> MIPROv2  55.33  36.22  47.33  81.55  55.11  +6.26
> GRPO  43.33  35.88  38.67  86.66  51.14  +2.29
> GEPA  62.33  38.61  52.33  91.85  61.28  +12.44

![[assets/dense-slides/-cKUW6n8hBU/slide-011.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/-cKUW6n8hBU/slide-011.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> This is all you need to construct arbitrarily complex workflows, data processing pipelines, replication of business logic, etc.

![[assets/dense-slides/-cKUW6n8hBU/slide-012.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/-cKUW6n8hBU/slide-012.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast` reconciled by agent.
- OCR decision: ready — Table-like slide with multiple rows and short labels; OCR should handle it better than manual transcription in this pass.

Slide text:

> DSPy on X
> @lateinteraction  Creator of DSPy (and ColBERT!)
> @maximerivest  Creator of Attachments
> @tech_optimist  DSPy advocate, programmer, nice guy
> @dbreunig  Writes excellent technical content
> @DSPyOSS  Official DSPy account
> @getpy  Curator of DSPyWeekly
> @kmad  Me

Classification audit: `raw/sources/slide-ai-classification/dense/-cKUW6n8hBU/audit.json`
