---
title: "Slides: We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco"
category: "slides"
video_id: "dRmWYHuIJxM"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco

## Source Video
[We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco](https://www.youtube.com/watch?v=dRmWYHuIJxM)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/dRmWYHuIJxM/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/dRmWYHuIJxM/slide-001.html)
- AI slide classifier: `title_card` confidence `0.99`
- Text source: agent_vision.

Slide text:

> We Cut 94% of Our AI Coding Tokens With a Local Code Index
> AI Engineer World's Fair
> June 30 – July 2, 2026 • San Francisco
> Search & Retrieval Track

![[assets/slides/dRmWYHuIJxM/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/dRmWYHuIJxM/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> THE ASSUMPTION
> Every AI coding tool we tried had the same assumption:
> send as much context as possible.
> 45,000 tokens per query
> ~5,000 tokens per query

![[assets/slides/dRmWYHuIJxM/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/dRmWYHuIJxM/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense bullet slide with small explanatory text; OCR is likely more reliable than manual transcription.

Slide text:

> We optimizedthe modelWeshould have optimized the Context.
> Better prompts
> "Be concise Only returm relevant code. The model stil received 45k tokens of input.
> Model settings
> Temperature, top-Pmax lokens control outout shape The 45k input was already sent and biled.
> Output compression
> Talk like a caveman* Saves:75%.of output (10% of bil) Net Impact - 8%. Wrong 10%
> A retrieval layer between codebase and agent
> Searchran index, refuri only relevant chunks. 94% fewer tokens.
> olara-labs/codecontext-engin?

![[assets/slides/dRmWYHuIJxM/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/dRmWYHuIJxM/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Where your tokens actually go
> 90% is input
> Output compression
> = ~8% off total bill
> Input retrieval
> = ~61% off total bill

![[assets/slides/dRmWYHuIJxM/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/dRmWYHuIJxM/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Multi-card architecture slide with small labels and metrics across several columns.

Slide text:

> A local retrieval layer between codebase and agent
> Tree-sitter Chunking Retrieval puqAH Compression Chunk Graph Code Confidence Scoring
> AST-awaresplits 10 langs Vector+8M25+RRF 94% Signatures+docs 89% CALLS.IMPORTS related Threshold gate filter
> Everything runs locally.No cloud,noAPI calls.sqlite-vec +FTS5 +graph in threeSQLite files.
> delara-labs/code-context-engine

![[assets/slides/dRmWYHuIJxM/slide-006.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/dRmWYHuIJxM/slide-006.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Why not just vector search?
> Vector Search
> FTS5 (BM25)
> RRF Fusion
> Recall: 0.78
> Recall: 0.72
> Recall: 0.90

![[assets/slides/dRmWYHuIJxM/slide-007.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/dRmWYHuIJxM/slide-007.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Dense two-column slide with small supporting copy and chart labels.

Slide text:

> The hardest problem wasn'tretrieval It was knowing when retrieval waswrongb
> LLM-based scoring Confidence scoring blend
> Asked the model to rate relevance. Accurale but +2 3s latency Ycost per query Simitarity Sox
> Flxed thresholds Keywords 30x
> calike. cosino > O.7 =relevant Broke on short quenies and long quenles. Recency 20x
> Simpie heuristic won
> no API calls. 50% smilarity +30% keyword K20% recency Adaptive: 0.4ms Lesson: dont reach for an LLM when a welghted avera
> elararlabs/code-context-cngine

![[assets/slides/dRmWYHuIJxM/slide-008.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/dRmWYHuIJxM/slide-008.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/full`.
- OCR decision: ready — Benchmark slide with multiple metric panels, small numbers, and a code snippet.

Slide text:

> BENCHMARK
> FastAPI FastAPl:53files,20realquestions,reproducible
> Full file baseline Afterretrieval 83,681 tok/q 4,927tok/q 94%
> retrieval savings
> After compression 523tok/q No cherry-picking.No synthetic queries.
> 20questionsadeveloperwouldactuallyask
> Recall@10 0.90 $pythonbenchmarks/run_benchmark.py --repo fastapi/fastapi--source-dirfa
> elara-labs/code-context-engine

![[assets/slides/dRmWYHuIJxM/slide-009.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/dRmWYHuIJxM/slide-009.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Four-panel trade-off slide with small body text in each card.

Slide text:

> What we're honest about
> 94% is against full-file reads Monorepos dilute recall
> baseline. savings vs normal behavior are lower.Full-file is our reproducible Claude Code already uses grep and partial reads.Real-world feature-per-file repos hit R=1.00.Focused files retrieve best. On Go's fiber (396 fles),recall dropped to 0.07@10.One-
> Embedding model matters What actually worked
> bge-small-en-v1.5(384d) is fast,not SOTA.Bigger models lift Simple heunistics over ML.SQLite over specialized DB
> cache. over pure vector.Local-first.The boring choices com
> elara-labs/code-context-engine

![[assets/slides/dRmWYHuIJxM/slide-010.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/dRmWYHuIJxM/slide-010.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/right-72/contrast`.
- OCR decision: ready — Slide uses a small embedded metrics screenshot with dense numeric text.

Slide text:

> MEASURABLE
> token tracked. Every dollar counted.
> my-project.247 queriesLast query 5m ago
> 800O088xtokenssaved
> Input savings Output savings 48.2ktokens 12.4H tokens $3.62 $186.80
> Total saved 12.4Mtokens $189.62
> Breakdoan:
> retrieval chunk coepression outputcoepress* 84% <1% 3% 10.4M$156.60 421.5k 48.2k $3.62 $6.32
> mates.Actuai tokens served vs full-fle basellne,per bucket Dolar coats from five model pricing

![[assets/slides/dRmWYHuIJxM/slide-011.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/dRmWYHuIJxM/slide-011.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> The biggest optimization in AI coding isn't the model. It's the context.
> 94% fewer input tokens
> local no data leaves your machine
> MIT free, open source

Classification audit: `raw/sources/slide-ai-classification/slides/dRmWYHuIJxM/audit.json`

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
