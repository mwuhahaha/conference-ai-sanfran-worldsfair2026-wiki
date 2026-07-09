---
title: "Slides: Optimizing inference for voice models in production - Philip Kiely, Baseten"
category: "slides"
video_id: "gmTHs5T_YAE"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Optimizing inference for voice models in production - Philip Kiely, Baseten

## Source Video
[Optimizing inference for voice models in production - Philip Kiely, Baseten](https://www.youtube.com/watch?v=gmTHs5T_YAE)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/gmTHs5T_YAE/slide-001.jpg]]

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

![[assets/slides/gmTHs5T_YAE/slide-002.jpg]]

OCR text:

> Hi, I'm Philip from Baseten 7
> « Developer relations at Baseten a te a a ° — . :
> + Based in SFBA @@@ ai a a 2a
> * Favorite voice model: Orpheus TTS 4 ia | : »
> od woe
> - 3
> Te ; ; oO
> a Microsoft OCU

![[assets/slides/gmTHs5T_YAE/slide-003.jpg]]

OCR text:

> Agenda |
> 1. TTS model architecture
> 2. TTS performance metrics
> 3. Orpheus TTS optimization techniques
> 4. Orpheus TTS performance benchmarks
> 5. Infrastructure and client code
> a 3
> u Microsoft § ou?
> , os

![[assets/slides/gmTHs5T_YAE/slide-004.jpg]]

OCR text:

> "archttectures':[
> AIE CanopyLabs OrpheusTTS Example: ·Extendedcontextlength Increasedvocabsizefor Llama3.23Bbackbone speech-specifictokens withRoPEscaling "inittalizer_range*:.82. "attention_btas:false, "attentton_dropout:B., "bos_token_ld:128808, "head_din':128, "htdden_act":"stlu', "htdden_s（ze²:3872, "ax_posttton_embeddings*:131872, "nu_attentton_heads*:24, "nun_htdden_layers”:28, "num_key_value_heads':8, "eos_token_（d:12801, internediate_stze:8192, "pretraining_tp":1, uesado ee11.ad11apo res_norn_eps:le- "factor':32.6, "low_freq_factor'x1.6,.oe11.:odado "high_freq_factor':4.0. suppqauoasodxee5o
> "tle_word_erbeddings':true.o "transformers_verston:*4.47.0* "rope_theta':58e889.8.
> vocab_stze:156939
> Microsoft smol?

![[assets/slides/gmTHs5T_YAE/slide-005.jpg]]

OCR text:

> AIE settings engine TensorRT-LLM ·Post-training quantization toFP8 ·QuantizeKVcache OptimizeforHopperarchitecture build: runtlee: ensor_oarallelcount:1 plugin_conftguratton: Ay.cache_free.opu.#e.fraction:985 base model:llama Quantization_type:fpB_kv enable_chunked_context:true nax_batch_slze:256 max_mum_tokens:16384 checkpoint repo:baseten/orpheus-3b-e.1-ft caltb.dataset:"cnn_datlyaatl" reviston:b9eb57... use_fpecontext_foho:true
> E
> Microsoft smol?

![[assets/slides/gmTHs5T_YAE/slide-006.jpg]]

OCR text:

> AI Engineer
> World's Fair

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
