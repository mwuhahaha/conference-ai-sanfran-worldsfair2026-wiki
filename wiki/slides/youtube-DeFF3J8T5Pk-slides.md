---
title: "Slides: How fast are LLM inference engines anyway? — Charles Frye, Modal"
category: "slides"
video_id: "DeFF3J8T5Pk"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: How fast are LLM inference engines anyway? — Charles Frye, Modal

## Source Video
[How fast are LLM inference engines anyway? — Charles Frye, Modal](https://www.youtube.com/watch?v=DeFF3J8T5Pk)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/DeFF3J8T5Pk/slide-001.jpg]]

OCR text:

> INNOVATIONPARTNER
> aws
> PLATINUMSPONSORS
> Graphite
> WWindsurf
> MongoDB
> daily
> augment code
> Workos

![[assets/slides/DeFF3J8T5Pk/slide-002.jpg]]

OCR text:

> Open weights models
> and open source engines
> are getting better very quickly.
> It finally makes sense to self-host!
> ) ‘| f a Microsoft art?

![[assets/slides/DeFF3J8T5Pk/slide-003.jpg]]

OCR text:

> . Biides iAlNnnr
> .
> ge eS <2" 5 F :
> peer “oe ,
> DOM ose
> ieee 40° -
> 
> cor 0" ee _ ae
> 
> bit. ly/ai-engineer-201-2023
> 
> | by Chares Frye
> 
> 2
> | ‘ , a Microsoft aur?

![[assets/slides/DeFF3J8T5Pk/slide-004.jpg]]

OCR text:

> AIE saturate, open models will catch up, then dominate. If capabilities requirements
> Microsoft smol?
> World'sFair

![[assets/slides/DeFF3J8T5Pk/slide-005.jpg]]

OCR text:

> Check out specialized LLM inference libraries.
> • mlc is the fastest. This is so fast that I'm skeptical and am now motivated to measure quality (if I have time). When checking the outputs manually, they didn't seem that different than other approaches.
> • CTranslate2 is my favorite tool, which is among the fastest but is also the easiest to use. The documentation is the best out of all of the solutions I tried. Furthermore, I think that the ergonomics are excellent for the models that they support. Unlike vLLM, CTranslate2 doesn't seem to support distributed inference just yet.
> • vLLM is really fast, but CTranslate2 can be much faster. On other hand, vLLM supports distributed inference, which is something you will need for larger models. vLLM might be the sweet spot for serving very large models.
> • Text Generation Inference is an ok option (but nowhere near as fast as vLLM) if you want to deploy HuggingFace LLMs in a standard way. TGI has some nice features like telemetry baked in (via OpenTelemetry) and integration with the HF ecosystem

![[assets/slides/DeFF3J8T5Pk/slide-006.jpg]]

OCR text:

> Let’s explore with the LLM Engine Advisor!
> I want to serve Llama 3.1 8B with any engine
> Clients should receive the first token in under 1 second 99% of the time
> I expect on average 128 tokens in / 1024 tokens out
> I want to see every benchmarked configuration
> modal.com/llm-almanac
> AIE
> aws

![[assets/slides/DeFF3J8T5Pk/slide-007.jpg]]

OCR text:

> eal a ee
> os 5 ue ee :
> soa vee 5 o * O
> LLM Engine Advisor wat Tenvtertveg crane
> Teeeto wis Lhe SS voowuh Clem waitin: the finiieken Ry wee
> any cogine ¥ Peecomd YP ethene
> laApAtonacoge Stokeesie 2d rokemow  v Iwonttouy every benchmarked Yo eet eraticen
> ;
> * Thonaghper tngacsts oper repiaal vece
> _ e
> e uw Microsoft § eoou°
> Works Fine

![[assets/slides/DeFF3J8T5Pk/slide-008.jpg]]

OCR text:

> AI Engineer
> World's Fair

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
