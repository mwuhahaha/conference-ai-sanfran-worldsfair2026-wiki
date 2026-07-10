---
title: "Dense Slides: Optimizing inference for voice models in production - Philip Kiely, Baseten"
category: "slides"
video_id: "gmTHs5T_YAE"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Optimizing inference for voice models in production - Philip Kiely, Baseten

## Source Video
[Optimizing inference for voice models in production - Philip Kiely, Baseten](https://www.youtube.com/watch?v=gmTHs5T_YAE)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/gmTHs5T_YAE/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/gmTHs5T_YAE/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Agenda
> 1. TTS model architecture
> 2. TTS performance metrics
> 3. Orpheus TTS optimization techniques
> 4. Orpheus TTS performance benchmarks
> 5. Infrastructure and client code

![[assets/dense-slides/gmTHs5T_YAE/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/gmTHs5T_YAE/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: advanced OCR `rapidocr-live/full`.
- OCR decision: ready — small code panel and compact technical text likely better handled by OCR

Slide text:

> AIE VCanopyLabs Example: OrpheusTTS ·Llama3.23Bbackbone.Extendedcontextlength Increasedvocabsizefor speech-specifictokens withRoPEscaling "bos_token_td':128908, "head_din':128, ax_positlon_enbedd ngs:131072, "nun_htdden_layers':28, "num_key_value_heads*:8, "attentton_dropout": "eos_token_（d:12n01, "htdden_act":"stlu', "htdden_s（ze°:372, "initializer_range*:e.92 "internedtate_slze:8192, "nua_attention_heads:24, "pretratntng_tp:1, ee1.:ad11apoo "rope_scaling":( "attention_blas:false, res_norn_eps:le-85 "factor:32. "htgh_freq_factor':4.0, "low_freq_factor':1.9, e11.,adA1do "ortginal_max_positlon_enbeddings:8192
> "tle_vord_enbeddings':trd "rope_theta':5
> "transformers_verston':"4.47.0*
> vocab_stze:156939
> TRL Microsoft smol?


### Hidden Non-Slide Evidence
- [`slide-001.jpg`](/assets/dense-slides/gmTHs5T_YAE/slide-001.jpg) — `title_card` confidence `0.97`; speaker intro card

Classification audit: `raw/sources/slide-ai-classification/dense/gmTHs5T_YAE/audit.json`
