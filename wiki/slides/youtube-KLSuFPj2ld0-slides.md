---
title: "Slides: Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe"
category: "slides"
video_id: "KLSuFPj2ld0"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe

## Source Video
[Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe](https://www.youtube.com/watch?v=KLSuFPj2ld0)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/KLSuFPj2ld0/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/KLSuFPj2ld0/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: agent_vision.

Slide text:

> Software Engineer @ Stripe
> Spent 4 years leading our Issuing team
> Spent last 2 years helping robots spend

![[assets/slides/KLSuFPj2ld0/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/KLSuFPj2ld0/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Problems
> 01 Wrong place
> 02 Wrong thing
> 03 Wrong amount
> 04 Wrong credential

![[assets/slides/KLSuFPj2ld0/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/KLSuFPj2ld0/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: advanced OCR `rapidocr-live/left-72/contrast` reconciled by agent.
- OCR decision: ready — dense code-like token object is better handled by OCR

Slide text:

> Shared Payment Tokens
> 
> {
>   "id": "spt_1RgaZcFPC5QU06ZCDVZuVA8g",
>   "created": 1751580820,
>   "deactivated_at": null,
>   "deactivated_reason": null,
>   "usage_limits": {
>     "currency": "usd",
>     "expires_at": 1751587220,
>     "max_amount": 1000
>   },
>   "seller_details": {
>     "network_id": "merchant_name"
>   }
> }

![[assets/slides/KLSuFPj2ld0/slide-006.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/KLSuFPj2ld0/slide-006.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: advanced OCR `rapidocr-live/full` reconciled by agent.
- OCR decision: ready — dense code editor screenshot is OCR-suitable

Slide text:

> try {
>   const paymentIntent = await sellerStripe.paymentIntents.create({
>     amount: 5000,
>     currency: "usd",
>     // shared_payment_grant: sharedPaymentGrantFromToken.id,
>     payment_method: "pm_card_visa",
>     confirm: true,
>     automatic_payment_methods: {
>       enabled: true,
>       allow_redirects: "never",
>     },
>   });
> 
>   console.log("Payment intent created!", paymentIntent);
> } catch (error) {
>   console.error("Error creating payment intent:", error);
>   throw error;
> }

![[assets/slides/KLSuFPj2ld0/slide-009.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/slides/KLSuFPj2ld0/slide-009.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.
- OCR decision: ready — Diagram slide with small embedded protocol text that OCR is likely to read better than manual transcription.

Slide text:

> Machine Payments Protocol


### Hidden Non-Slide Evidence
- [`slide-001.jpg`](/assets/slides/KLSuFPj2ld0/slide-001.jpg) — `speaker_stage` confidence `0.98`; speaker on stage with cropped slide, not a full presentation slide
- [`slide-003.jpg`](/assets/slides/KLSuFPj2ld0/slide-003.jpg) — `speaker_stage` confidence `0.98`; speaker on stage with cropped slide, not a full presentation slide
- [`slide-007.jpg`](/assets/slides/KLSuFPj2ld0/slide-007.jpg) — `demo_video` confidence `0.14`; Stage/demo footage with terminal and presenter overlay; not a readable presentation slide.
- [`slide-008.jpg`](/assets/slides/KLSuFPj2ld0/slide-008.jpg) — `demo_video` confidence `0.16`; Stage/demo footage with code output and presenter overlay; not a readable presentation slide.
- [`slide-010.jpg`](/assets/slides/KLSuFPj2ld0/slide-010.jpg) — `demo_video` confidence `0.99`; Demo/video footage with stage context, not a readable presentation slide.

Classification audit: `raw/sources/slide-ai-classification/slides/KLSuFPj2ld0/audit.json`

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
