---
title: "AI Engineer Livestream Corpus"
category: "resources"
sourceLabels: ["Public YouTube metadata", "Livestream corpus audit"]
---

# AI Engineer Livestream Corpus

This page inventories AI Engineer channel livestreams that may be useful as supporting context for the World's Fair 2026 wiki. World's Fair 2026 livestreams are direct event support; prior World's Fair track streams are historical context and should be labeled as such when used.

## Coverage Summary
- Channel livestream entries collected: 32
- World's Fair-related livestream entries: 16
- World's Fair 2026 livestream entries: 3
- Livestream transcript caches present: 3
- Livestreams with standard slide pages: 3
- Livestreams with dense slide pages: 3
- Livestreams with reconstructed slide pages: 2

## World's Fair 2026 Livestreams
- [[youtube-I2cbIws9j10]] — [WF26: Harness Engineering & Startup Battlefield ft. Garry Tan, Mike Krieger, @t3dotgg , DSPy](https://www.youtube.com/watch?v=I2cbIws9j10); 91,792 transcript words; 80 standard frames; 12 dense crops
- [[youtube-4sX_He5c4sI]] — [WF2026: Autoresearch & Keynotes ft. Anthropic, Google DeepMind, Amazon AGI, Sonar, Arena, Recursive](https://www.youtube.com/watch?v=4sX_He5c4sI); 82,600 transcript words; 120 standard frames; 14 dense crops; 80 reconstructed crops
- [[youtube-htM02KMNZnk]] — [WF2026: Software Factories & Keynotes ft. Microsoft, OpenAI, OpenClaw, Z.ai (GLM), MiniMax, HF](https://www.youtube.com/watch?v=htM02KMNZnk); 89,050 transcript words; 120 standard frames; 19 dense crops; 80 reconstructed crops

## Other World's Fair Track Streams
- [AI Engineer World’s Fair 2025 - Day 2 Keynotes & SWE Agents track](https://www.youtube.com/watch?v=U-fMsbY-kHY) — 2025 historical context
- [AI Engineer World’s Fair 2025 - Retrieval + Search](https://www.youtube.com/watch?v=a0TyTMDh1is) — 2025 historical context
- [AI Engineer World's Fair 2025 - Evals](https://www.youtube.com/watch?v=Vqsfn9rWXR8) — 2025 historical context
- [AI Engineer World’s Fair 2025 - Reasoning + RL](https://www.youtube.com/watch?v=-9E9_21tx04) — 2025 historical context
- [AI Engineer World's Fair 2025 - Day 1 Keynotes & MCP track ft. Anthropic MCP team](https://www.youtube.com/watch?v=z4zXicOAF28) — 2025 historical context
- [AI Engineer World’s Fair 2025 — GraphRAG](https://www.youtube.com/watch?v=RR5le0K4Wtw) — 2025 historical context
- [AI Engineer World’s Fair 2025 - LLM Recommendation Systems (RecSys)](https://www.youtube.com/watch?v=3k4a0PemMu4) — 2025 historical context
- [AI Engineer World’s Fair 2025 - Tiny Teams](https://www.youtube.com/watch?v=xhKgTkzSmuQ) — 2025 historical context
- [AI Engineer World’s Fair 2024 - Keynotes & Multimodality track](https://www.youtube.com/watch?v=vaIiNZoXymg) — 2024 historical context
- [AI Engineer World’s Fair 2024 — GPUs & Inference Track](https://www.youtube.com/watch?v=JVSKlEmUr0k) — 2024 historical context
- [AI Engineer World’s Fair 2024 — Keynotes & CodeGen Track](https://www.youtube.com/watch?v=5zE2sMka620) — 2024 historical context
- [AI Engineer World’s Fair 2024 - Open Models track](https://www.youtube.com/watch?v=R0X7mPagRiE) — 2024 historical context
- [AI Engineer World’s Fair 2024 - Open Models track](https://www.youtube.com/watch?v=NOONz6SwKKg) — 2024 historical context

## Use Guidance
- Use World's Fair 2026 livestreams as direct supporting material for this wiki.
- Use older World's Fair track streams only as historical or conceptual context, not as evidence for 2026 session facts.
- When a stream has transcript but no slides, run `scripts/extract_video_slides.py --video-id <id>` and then rebuild.
- When a stream has neither transcript nor slides, fetch captions first; use local Whisper only when public captions are absent.
