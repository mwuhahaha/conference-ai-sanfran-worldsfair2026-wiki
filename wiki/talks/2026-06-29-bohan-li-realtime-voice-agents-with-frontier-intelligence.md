---
title: "Realtime Voice Agents with Frontier Intelligence"
category: "talks"
date: "2026-06-29"
time: "2:50pm-3:10pm"
track: "Voice & Realtime AI"
room: "Track 6"
speakers: ["Bohan Li"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "Voice & Realtime AI"
scheduleRoom: "Track 6"
scheduleLabels: ["Voice & Realtime AI", "Track 6", "session", "confirmed"]
---
# Realtime Voice Agents with Frontier Intelligence

## Official Schedule Context
- Date/time: 2026-06-29 · 2:50pm-3:10pm
- Track/room: Voice & Realtime AI · Track 6
- Speaker(s): Bohan Li
- Session type/status: session · confirmed

## Schedule Labels
- Track: Voice & Realtime AI
- Room: Track 6
- Session type: session
- Status: confirmed

## Official Description
Dive into how the EliseAI voice agent harness orchestrates multiple models with jagged capability profiles to achieve realtime latency without sacrificing intelligence. Reduces p90 effective latency overhead of ASR, TTS, and tool calling to sub 200ms, unlocking frontier models like GPT 5.5 for voice. ### ASR: Eager Speculative Transcription We introduce speculative transcription by pairing local Whisper or Parakeet fine-tunes for speed with API models like Scribe, Nova, or Gemini Flash for accuracy. A local content match classifier operates at sub 10ms latency, allowing us to immediately trigger the downstream pipeline from the fast local transcription and dynamically replace text with the more accurate transcription if significant differences occur. This process runs on a eager 100ms VAD delay, securely releasing the generated response audio only after a fixed silence threshold has passed. ### LLM: Async background tool injection To eliminate expensive tool calling round trips, we implement system leveraging async background tool injection where the primary model makes no direct tool calls. Instead, local fine-tuned tool-calling models continuously observe the realtime transcription stream in the background. "Fake" tool call traces are then injected into the primary LLM’s context, which primes it for immediate, one-shot response generation. ### TTS: Prefix caching and infilling Many Agent responses start with the same set of 3-6 words. We can cache this audio, releasing it immediately while we infill the remaining response audio conditioned on this prefix to preserve speech prosody. With this approach, a relatively small cache can achieve a 90% hit rate across a wide range of voices, languages and model providers.

## Related YouTube Video
No related AI Engineer channel video found yet.

## Transcript Status
No official session recording transcript was found by exact title match on the AI Engineer YouTube channel during this run.

## People
- [[bohan-li]]

## Notes
- Pending transcript synthesis when an official recording or confirmed matching video is available.

## Source-Derived Enrichment
This section is generated from all currently linked source material for the article: official schedule text, related video pages, cached transcripts, visible slide text, dense/reconstructed slide pages, and AI slide-classification audits.

### Source Signals
No linked video, transcript, or slide source has been attached yet.

### Article Use
Use these source signals to refine the synopsis, topic links, people/company context, and method notes. If a source is a related external video rather than an exact official recording, keep it framed as supporting evidence.
