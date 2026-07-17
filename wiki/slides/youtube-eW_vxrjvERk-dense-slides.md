---
title: "Dense Slides: Connecting the Dots with Context Graphs — Stephen Chin, Neo4j"
category: "slides"
video_id: "eW_vxrjvERk"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Connecting the Dots with Context Graphs — Stephen Chin, Neo4j

## Source Video
[Connecting the Dots with Context Graphs — Stephen Chin, Neo4j](https://www.youtube.com/watch?v=eW_vxrjvERk)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/eW_vxrjvERk/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/eW_vxrjvERk/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.92`
- Text source: advanced OCR `rapidocr-live/full`.
- OCR decision: ready — Product/UI screenshot with dense small multi-column text and many interface labels; OCR will read it better than direct transcription.

Slide text:

> Conversations Lenny'sMemory Bta About GitHub
> +New Conversation Agent Configuration
> ★ ★ ★ AIE Quick Start Usememory graph searchto explore whatguestssay about. 4/5/2026 the Brian Chesky episode Use memory graph search to explore what guests say about. 4/8/2026 Show me locations mentioned in howdobestcoordinate3 4/8/2026 Explore a Topic Use memory graph sear t0 explore whar guests say Related Entities What encities are related t about scaling engineerin. Arbnb7 Explore insights from 299 podcast episodes with Al-powered graph memory. Click a topic or type your own question. Ask about Lenny's Podcast Tell me about Brian Chesiy Speaker Quotes Whur did Srian Chesky say and beng n Pe detals? Who is Brian.... sbout micromanagement Depodcast) Map View Chenky episode What are the most menboned companies in Showmelocatons ntioned in the Brian Agent Capabities Aailable Tocs Mult-step Reasoning CoeratonMemory Adaptepoesbednyour sr Plens and eecutescomt Mainescpeteacrossmes threas Preference Learning preferences p Siep KnowfedgeGraph aazsabe 21
> Tool Call Cards
> memory @neo4j-labs/agent- Ask about Lenny's Podcast:
> Neo4j tseapog s,Auia1 Press Enter to send, Shit+Enter for
> AIEngineer
> EUROPE

Classification audit: `raw/sources/slide-ai-classification/dense/eW_vxrjvERk/audit.json`
