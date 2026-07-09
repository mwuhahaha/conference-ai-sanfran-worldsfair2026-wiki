---
title: "Stop Chunking Like It's 2022"
category: "talks"
date: "2026-06-29"
time: "3:20pm-3:40pm"
track: "Search & Retrieval"
room: "Track 3"
speakers: ["Yuval Belfer", "Niv Granot"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Search & Retrieval"
scheduleRoom: "Track 3"
scheduleLabels: ["Search & Retrieval", "Track 3", "session", "confirmed"]
---
# Stop Chunking Like It's 2022

## Official Schedule Context
- Date/time: 2026-06-29 · 3:20pm-3:40pm
- Track/room: Search & Retrieval · Track 3
- Speaker(s): Yuval Belfer, Niv Granot
- Session type/status: session · confirmed

## Schedule Labels
- Track: Search & Retrieval
- Room: Track 3
- Session type: session
- Status: confirmed

## Official Description
Every RAG system bets everything on a single chunk size. 500 tokens? 800? Pick wrong, and half your

queries fail before they start. But here's what nobody tells you: all the picks are wrong; there is

no single chunk size that works for all queries. We ran oracle experiments across meeting

transcripts, story chapters, and TV scripts. The result? Queries disagree violently on what chunk

size works best - sometimes by 40 percentage points. Your "tuned" chunk size isn't a compromise;

it's systematic underperformance. In this talk, we'll expose why fixed chunking fails and show you a

dead-simple fix: index at multiple chunk sizes, aggregate at retrieval time using Reciprocal Rank

Fusion. No retraining. No LLM overhead. Just 1-37% better recall across benchmarks by letting

queries vote with their ranks instead of forcing them into one-size-fits-all boxes. Walk away

knowing exactly when your chunk size is sabotaging you - and how to stop leaving 20-40% of your

retrieval performance on the table.

## Related YouTube Video
[RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot](https://www.youtube.com/watch?v=Ywl4LsvHKzU) (speaker-match related prior/adjacent AI Engineer video; captions: English auto-captions).

## Transcript Status
Related video transcript availability: English auto-captions. Treat this as supporting context, not a recording of this exact scheduled session unless later confirmed. Not fetched yet.

## People
- [[yuval-belfer]]
- [[niv-granot]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.
## Supporting Slides
- [[youtube-Ywl4LsvHKzU-slides]] — extracted from the related public AI Engineer video.
## Slide Evidence
- Slide-only cropped deck: [[youtube-Ywl4LsvHKzU-dense-slides]] (7 viable slide images).
- Related slide/OCR pages:
- [[youtube-Ywl4LsvHKzU-dense-slides]]
- [[youtube-Ywl4LsvHKzU-reconstructed-slides]]
- [[youtube-Ywl4LsvHKzU-slides]]
- Slide-derived terms: `world`, `fifa`, `local`, `name`, `questions`, `same`, `future`, `wife`, `first`, `mother`, `schema`, `prob`, `answers`, `assuming`, `answer`, `lies`, `certain`, `chunk`

## Source-Derived Enrichment
This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Source Signals
- `youtube-Ywl4LsvHKzU` — 10 slide-derived text signals
- Slide-derived themes for `youtube-Ywl4LsvHKzU`: world, local, questions, united, states, mother, surname, name.
- Evidence links for `youtube-Ywl4LsvHKzU`: [[youtube-Ywl4LsvHKzU]], [[youtube-Ywl4LsvHKzU-slides]], [[youtube-Ywl4LsvHKzU-dense-slides]], [[youtube-Ywl4LsvHKzU-reconstructed-slides]]

### Article Use
Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.
## Slides
- Source video: `youtube-Ywl4LsvHKzU`
- Slide deck: [[youtube-Ywl4LsvHKzU-dense-slides|Dense Slides: RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot]] — 7 visible slide image(s).
![[assets/dense-slides/Ywl4LsvHKzU/slide-001.jpg]]
![[assets/dense-slides/Ywl4LsvHKzU/slide-002.jpg]]
![[assets/dense-slides/Ywl4LsvHKzU/slide-003.jpg]]
- Additional slide evidence: [[youtube-Ywl4LsvHKzU-slides|Slides: RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot]], [[youtube-Ywl4LsvHKzU-reconstructed-slides|Reconstructed Slides: RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot]]
- Slide-derived themes for `youtube-Ywl4LsvHKzU`: world, local, questions, united, states, mother, surname, name.
