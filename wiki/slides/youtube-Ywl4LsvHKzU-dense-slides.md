---
title: "Dense Slides: RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot"
category: "slides"
video_id: "Ywl4LsvHKzU"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot

## Source Video
[RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot](https://www.youtube.com/watch?v=Ywl4LsvHKzU)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/Ywl4LsvHKzU/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Ywl4LsvHKzU/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/border-trim/contrast`.
- OCR decision: ready — Dense multi-line text with a long quote and small body copy is better handled by OCR.

Slide text:

> Probtems Local questions, local answers Assuming an answer lies in a certain chunk
> Multi-hop questions are not realistic
> "If my future wife has the same first name as the 15th first lady
> of the United States' mother and her surname is the same as the second assassinated president's mother's maiden name,
> what is my future wife's name?" (from: FRAMES)
> ONAIR

![[assets/dense-slides/Ywl4LsvHKzU/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Ywl4LsvHKzU/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> The Vicious Cycle
> 1. Build RAG systems for flawed benchmarks
> 2. Celebrate our awesome benchmark scores
> 3. Watch real users struggle
> 4. Create new benchmarks with the same problems
> 5. Rinse and repeat

![[assets/dense-slides/Ywl4LsvHKzU/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Ywl4LsvHKzU/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: agent_vision.

Slide text:

> Example
> FIFA World Cup
> Which team has won the FIFA World Cup the most times?
> In how many FIFA World Cups did Brazil participate?
> List all teams that have never won the FIFA World Cup but have reached the top 3.

![[assets/dense-slides/Ywl4LsvHKzU/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Ywl4LsvHKzU/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/bright-screen/contrast`.
- OCR decision: ready — Tabular content with small text and scores is OCR-suitable.

Slide text:

> Common
> Pipelines RAG Retrieval Pipeline Generator Score
> Fail IAW Cp FUA Ward Cp Responses Common pipeline OpenAl gpt4o 0.05 0.11
> ONAIR

![[assets/dense-slides/Ywl4LsvHKzU/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Ywl4LsvHKzU/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: agent_vision.

Slide text:

> High Level Idea
> Unstructured Corpus
> Data Structure
> Query

![[assets/dense-slides/Ywl4LsvHKzU/slide-006.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Ywl4LsvHKzU/slide-006.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/full`.
- OCR decision: ready — Schema diagram and small field list are better handled by OCR.

Slide text:

> Ingestion - Schema Creation
> World Cup
> Corpus (FIFA) (SemanticObject) Schema Winner:Team TopScorer:Tuple[Player,int] Year:int(1900-2100) Top3:List[Teams]
> ONAIR

![[assets/dense-slides/Ywl4LsvHKzU/slide-007.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/Ywl4LsvHKzU/slide-007.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/border-trim/contrast`.
- OCR decision: ready — Dense text-heavy slide with multiple bullets and small nested text; OCR is likely more reliable than manual transcription here.

Slide text:

> Chattenges Not every corpus/query is relational DB material
> Japan) Normalization (West Germany, South Korea and
> Abstinence & Ambiguity Both during ingestion and inference
> Did Real Madrid win in the 2006 Final? (Not
> world cup)
> Clustering and inferring schema (clear trade-off
> on complexity)
> Text2SQL over complex schemas
> ONAIR

Classification audit: `raw/sources/slide-ai-classification/dense/Ywl4LsvHKzU/audit.json`
