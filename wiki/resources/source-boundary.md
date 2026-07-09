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

## Source Roles
- Canonical schedule sources: the official AI Engineer World's Fair 2026 schedule and speaker roster. These remain canonical for session titles, dates, times, tracks, rooms, speakers, and affiliations.
- Primary event video sources: official AI Engineer YouTube videos for AI Engineer World's Fair San Francisco 2026, including official livestream recordings and official published talk cuts. These are primary evidence for what was said, shown, transcribed, or captured from slides in the event recordings.
- Supporting video sources: non-official YouTube uploads, older AI Engineer videos, other AIE event streams, and related speaker/company videos. These may support context, concepts, speaker background, or cross-event comparison, but they are not primary evidence for World's Fair San Francisco 2026 session facts.
- Supporting source-of-source links: public company sites, docs, social profiles, LinkedIn/X/Twitter/website links, blogs, product pages, and professional profiles directly connected to scheduled people, companies, products, or claims.

## Confidence Rules
- Official schedule facts are canonical for titles, dates, times, tracks, speakers, and affiliations.
- Official AI Engineer World's Fair San Francisco 2026 videos are primary event video sources for media/transcript/slide evidence; schedule metadata still comes from the official schedule.
- Related non-event YouTube videos are supporting context unless the video is confirmed as an official World's Fair San Francisco 2026 recording.
- YouTube transcripts are treated as transcript evidence, but speaker attribution and session matching still need review when the video is only speaker-matched.
- Slide OCR is best-effort. Prefer reconstructed slide crops when the full-stage frame OCR is weak, and preserve unreadable/non-slide classifications rather than inventing text.
- Public profile/company-site facts are supporting context unless they come directly from the official schedule or official speaker roster.

Current generated scale: 560 sessions, 555 people, 344 companies, 219 resources, 418 slide pages, 16 topics, and 5 event/day pages.
