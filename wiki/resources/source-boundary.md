---
title: "Source Boundary"
category: "resources"
---

# Source Boundary

For agent-oriented navigation across these sources, use [[agent-source-index]].

Allowed sources for this run:
- Official AI Engineer World's Fair 2026 schedule endpoints.
- Public AI Engineer YouTube channel metadata.
- Public YouTube caption availability metadata.
- Public YouTube transcript helper output where captions were available.
- Local Whisper fallback output when captions are missing.
- Local video frame extraction, Tesseract OCR, RapidOCR/ONNX repairs, and OpenCV reconstructed slide crops.
- Public source-of-source links when they are directly relevant to the conference graph, including speaker-provided LinkedIn, X/Twitter, website, and blog links from the official speaker roster.
- Public company sites and public professional profiles may be used in future enrichment passes when they clarify people, companies, products, or claims connected to scheduled sessions; those pages should label the added source layer instead of blending it into official schedule facts.

The run did not import private Miami notes, personal recordings, queue state, or diary content.

## Confidence Rules
- Official schedule facts are canonical for titles, dates, times, tracks, speakers, and affiliations.
- Related YouTube videos are supporting context unless the video is confirmed as the exact session recording.
- YouTube transcripts are treated as transcript evidence, but speaker attribution and session matching still need review when the video is only speaker-matched.
- Slide OCR is best-effort. Prefer reconstructed slide crops when the full-stage frame OCR is weak, and preserve unreadable/non-slide classifications rather than inventing text.
- Public profile/company-site facts are supporting context unless they come directly from the official schedule or official speaker roster.

Current generated scale: 560 sessions, 553 people, 340 companies, 117 resources, 310 slide pages, 11 topics, and 5 event/day pages.
