---
title: "Slide AI Vision Rescue Audit"
category: "resources"
sourceLabels: ["AI vision", "Slide OCR", "OCR audit"]
---

# Slide AI Vision Rescue Audit

## Latest Run
- Provider: none available
- Slides queued: 1
- Slides attempted: 0
- AI vision text files written: 0
- Minimum confidence: 0.72
- Output directory: `raw/sources/slide-ocr-ai-vision/`

## Notes
- This step is intentionally after OCR. OCR creates candidates and identifies weak frames; vision interpretation reads the actual image only for low-confidence cases.
- Free local vision is preferred through Ollama when available. OpenAI Responses API is used only when `OPENAI_API_KEY` is set and the provider is selected or auto-detected.
- Generated text is merged by `scripts/improve_slide_ocr_rapidmerge.py` as `ai-vision`, below operator-verified text but above raw OCR.
