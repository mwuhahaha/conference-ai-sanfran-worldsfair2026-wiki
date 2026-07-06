---
type: run-receipt
scope: project-local
status: complete
created: 2026-07-03T08:10:00+00:00
---

# Livestream Transcript And Slide Ingest

## Inputs
- AI Engineer YouTube Streams tab scan: `raw/sources/aidotengineer-channel-streams-latest.json`
- Livestreams:
  - `4sX_He5c4sI` — WF2026: Autoresearch & Keynotes ft. Anthropic, Google DeepMind, Amazon AGI, Sonar, Arena, Recursive
  - `htM02KMNZnk` — WF2026: Software Factories & Keynotes ft. Microsoft, OpenAI, OpenClaw, Z.ai (GLM), MiniMax, HF

## Transcript Results
- Cached transcript bundle/plain text/receipt for both videos under `raw/sources/youtube-livestream-transcripts/`.
- `4sX_He5c4sI`: 444143 transcript characters from YouTube transcript helper.
- `htM02KMNZnk`: 474096 transcript characters from YouTube transcript helper.
- Whisper fallback was available locally, but not used because the transcript helper returned usable text for both streams.

## Slide Results
- `4sX_He5c4sI`: 120 extracted slide/frame images, OCR text on 120.
- `htM02KMNZnk`: 120 extracted slide/frame images, OCR text on 120.
- Total wiki slide decks after this run: 107.
- Total embedded slide/frame images after this run: 1842.

## Wiki Outputs
- `wiki/resources/worldsfair-2026-livestreams.md`
- `wiki/resources/youtube-4sX_He5c4sI.md`
- `wiki/resources/youtube-htM02KMNZnk.md`
- `wiki/slides/youtube-4sX_He5c4sI-slides.md`
- `wiki/slides/youtube-htM02KMNZnk-slides.md`
- `wiki/topics/autoresearch.md`
- `wiki/topics/software-factories.md`

## Notes
- The second livestream initially hit the slide extractor's fixed 900-second ffmpeg sampling timeout. `scripts/extract_video_slides.py` now uses a 3600-second frame-sampling timeout, and the cached-video retry completed successfully.
