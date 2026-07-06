---
title: "Source Boundary"
category: "resources"
---

# Source Boundary

Allowed sources for this run:
- Official AI Engineer World's Fair 2026 schedule endpoints.
- Public AI Engineer YouTube channel metadata.
- Public YouTube caption availability metadata.
- Public YouTube transcript helper output where captions were available.
- Local Whisper fallback output when captions are missing.
- Local video frame extraction, Tesseract OCR, RapidOCR/ONNX repairs, and OpenCV reconstructed slide crops.

The run did not import private Miami notes, personal recordings, queue state, or diary content.

## Confidence Rules
- Official schedule facts are canonical for titles, dates, times, tracks, speakers, and affiliations.
- Related YouTube videos are supporting context unless the video is confirmed as the exact session recording.
- YouTube transcripts are treated as transcript evidence, but speaker attribution and session matching still need review when the video is only speaker-matched.
- Slide OCR is best-effort. Prefer reconstructed slide crops when the full-stage frame OCR is weak, and preserve unreadable/non-slide classifications rather than inventing text.

Current generated scale: 560 sessions, 553 people, 340 companies, 117 resources, 310 slide pages, 11 topics, and 5 event/day pages.
