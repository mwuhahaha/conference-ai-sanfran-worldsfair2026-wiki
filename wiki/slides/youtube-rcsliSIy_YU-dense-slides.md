---
title: "Dense Slides: Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands"
category: "slides"
video_id: "rcsliSIy_YU"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands

## Source Video
[Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands](https://www.youtube.com/watch?v=rcsliSIy_YU)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/rcsliSIy_YU/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> About Us
> Robert Brennan
> CEO and Co-founder, OpenHands
> OpenHands
> An MIT-licensed coding agent

![[assets/dense-slides/rcsliSIy_YU/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense small bullet text and multiple year sections are better handled by OCR than direct vision transcription.

Slide text:

> ? @
> 6 uthopr Autamtubg khe Aiecten tn Agtrumlt bo (-- - 1
> A Brief History of LLM Coding
> 2022: Context-unaware code snippets
> "Write python for bubble sort"
> 2023: Context-aware code generation
> "Write' a suite of unit tests for this function"
> 2024: Single agents for atomic coding tasks..
> Implement'the GET /products endpoint and use
> curl to validate that it works".
> 2025: Parallel agents for large-scale work:
> "Migrate our app from Redux to React Query"
> 2025-11-22114:35:43

![[assets/dense-slides/rcsliSIy_YU/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: agent_vision.

Slide text:

> Evolution of AI-Driven Development

![[assets/dense-slides/rcsliSIy_YU/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Why do we need orchestration?
> Why can't today's agents one-shot large tasks?
> Agent Problems
> Limited context window
> Laziness
> Lack of domain knowledge
> Compounding errors
> Human Problems
> Can't convey intuition
> Difficulty decomposing tasks
> Need intermediate reviews/check-ins
> Ambiguous definition of done

![[assets/dense-slides/rcsliSIy_YU/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.

Slide text:

> Agentic Engineers
> Every dev will use agents for day-to-day work.
> Only ~5% will become Agent Orchestrators.

![[assets/dense-slides/rcsliSIy_YU/slide-006.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-006.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Human in the Loop: Single Agent
> Human prompts agent
> Agent does some work
> Human checks output

![[assets/dense-slides/rcsliSIy_YU/slide-007.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-007.html)
- AI slide classifier: `demo_video` confidence `0.94`
- Text source: agent_vision.

Slide text:

> Showcase: Automating Massive Refactors

![[assets/dense-slides/rcsliSIy_YU/slide-008.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-008.html)
- AI slide classifier: `demo_video` confidence `0.93`
- Text source: agent_vision.

Slide text:

> Showcase: Automating Massive Refactors

![[assets/dense-slides/rcsliSIy_YU/slide-009.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-009.html)
- AI slide classifier: `product` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Dense UI screenshot with many small labels and metrics; OCR is better than direct transcription.

Slide text:

> csmith49/OpenHands
> Dependency. Obce05Details Edkt Metadats
> 02a7da Status: NEW Vecify Flx
> VCode Metrics (4 files)
> ffd83d -0.2+ 66.0 CyciomaticCorpiety Maintarabity inder 59.6
> Obce05 40.0.5t 593 Hangtood Ertort Hahtnad Vohune 13.8 Halstead Diffcufty Estimuated Blugs
> b794a3 8166 0.20
> n.0-0
> Dependencies(o)
> Dependenb (5)
> Nodes(4)
> openhands/apo_server/units/sg_siis.py 小
> F t Ne
> openhandsopp_serveriutils/async_remote_workspace.py
> 2025-11-22 14:54:08

![[assets/dense-slides/rcsliSIy_YU/slide-010.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-010.html)
- AI slide classifier: `title_card` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Task Decomposition

![[assets/dense-slides/rcsliSIy_YU/slide-011.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-011.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Task Decomposition
> Break your end-goal down into tasks that:
> - Are one(-ish) shottable
> - Fit in a single commit
> - Can be executed in parallel
> - Can be verified by a human as correct or incorrect
> - Clear dependencies/ordering between tasks

![[assets/dense-slides/rcsliSIy_YU/slide-012.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-012.html)
- AI slide classifier: `code` confidence `0.98`
- Text source: none.
- OCR decision: ready — Dense code screenshot with small source text; OCR is the right extraction path.
![[assets/dense-slides/rcsliSIy_YU/slide-013.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-013.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.
- OCR decision: ready — Product/docs screenshot with dense small UI text and code snippets.

Slide text:

> Getting Started

![[assets/dense-slides/rcsliSIy_YU/slide-014.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-014.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense slide text with long prompt, URLs, and configuration details that are better OCRed than transcribed by eye.

Slide text:

> ?
> 0. Wertahopr Autorstrg Lmhe Alectert wit Agtrls 1l t ho 心 Domg + D
> +心:t4心:t4h +.4
> Vibecoding CVE Remediation: LLM Connection
> Prompt 1:
> Look at the example code at https://docs.openhands.dev/sdk/auides/hello-world and the SDK docs at: https://docs.openhands.dev/sdk/api-reference/openhands.sdk.llm
> a pydantic SecretStr). Set the model name to: connection to the OpenHands LLM using the LLM API KEY env var (be sure to use. openhands/claude-sonnet-4-20250514 Write a small python script called cve_solver.py that for now just tests the 中
> Note to human: replace model name if using anthropic/openai
> Ct 2025-11-22115:19:54

![[assets/dense-slides/rcsliSIy_YU/slide-015.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-015.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense instructional slide text with bullets, a repository URL, and environment-variable references.

Slide text:

> ?
> nm
> D Wariahopr Autoretrg tthe Aecten tthAgtrba M t bo 6o 00○0：θ■0:
> Vibecoding CVE Remediation: Detect CVEs
> Prompt 2:
> Look at the example code at https://docs.openhands.dev/sdk/guides/hello-world
> Modify cve_solver.py so that it.
> Takes in a GitHub repository as a command line argument Creates a RemoteWorkspace connecting to 1ocalhost:8000 Clones the given repository to that workspace, using the GITHUB_ TOKEN env
> Tells the agent to use trivy to'scan the repository for CVEs Creates an Agent in that workspace var.
> CVEs Human: you can test the script with github.com/rbren/polaris - It should find 3
> 20251.1-22115:30:40

![[assets/dense-slides/rcsliSIy_YU/slide-017.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/rcsliSIy_YU/slide-017.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: none.
- OCR decision: ready — Slide has mixed prose and a code screenshot; OCR is the safer way to capture the exact agent setup and command text.

### Hidden Non-Slide Evidence
- [`slide-016.jpg`](/assets/dense-slides/rcsliSIy_YU/slide-016.jpg) — `demo_video` confidence `0.89`; Mixed screen capture with a cropped slide on the left and terminal/demo output on the right; not a clean readable presentation slide.

Classification audit: `raw/sources/slide-ai-classification/dense/rcsliSIy_YU/audit.json`
