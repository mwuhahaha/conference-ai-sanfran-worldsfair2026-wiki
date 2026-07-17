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
![[assets/slides/KLSuFPj2ld0/slide-001.jpg]]

OCR text:

> i |
> o , ; -
> - — —=| | No | 4
> SG ee Peat mae ithe |
> CT ) —_ Ce
> Ce rT )
> J r |
> ee . e-, ‘
> i} i
> | of
> «| cee
> ; Ree een Reems es
> —
> a a

![[assets/slides/KLSuFPj2ld0/slide-002.jpg]]

OCR text:

> Software Engineer @ Stripe “ue
> Spent 4 years leading our Issuing
> - Spent last 2 years helping robots
> spend
> a)
> | = Engineering the future of Al

![[assets/slides/KLSuFPj2ld0/slide-003.jpg]]

OCR text:

> a oe) ENG
> . . DY RYeAU AYA). *)(e1e-10e)
> " —_ aa | AlEngineer ne
> eo oleae ame) MAL
> a Ce _
> a : es One WUC)
> ae BE ae
> aaa ae
> BE F
> ce .
> — i
> —

![[assets/slides/KLSuFPj2ld0/slide-004.jpg]]

OCR text:

> Problems mee
> 01 Wrong place
> ae 02 Wrong thing
> ors 03 Wrong amount
> 04 Wrong credential
> = | ¥ | Engineering the future of Al

![[assets/slides/KLSuFPj2ld0/slide-005.jpg]]

OCR text:

> SharedPaymentTokens
> stripe
> "id":"spt_1RgaZcFPC5QU06ZCOVZuVA8q"
> "created":1751500820,
> AIE
> "deactivated_at":null,
> "deactivated_reason":null,
> "usage_linits":{
> "currency":"usd"
> "expires_at":1751587220
> "nax_anount":1000
> "seller_details"
> "network_id":
> "nerchant_nane"
> AlEngneer
> Engineering the future of Al

![[assets/slides/KLSuFPj2ld0/slide-006.jpg]]

OCR text:

> 97R
> 1index.ts×
> AI-DEMO
> .claude
> spt)Ts(ndex.ts)
> dse
> mep
> spt
> claude
> try
> vscode
> const paymentIntent-soit sellerStripe.paymentIntents.create（{
> node_modules
> currency:"usd",
> amount:5oe0,
> NUWO
> Tsnde.ts
> MtGrantedToken.id
> AIE
> (1paciage-lock.json
> confirm:troe,
> payment_method:"pn_card_visa",
> (1packagejson
> !pepm-lock.yaml
> autoeatic_payment_methods:(
> Fstcho
> enabled:true,
> tsconfigjon
> allow_redirects:“never",
> console.log（"Payment intent created:",paymentIntent))
> )catch（error）（
> console.error("Error creating payment intent:",error):
> throwerror:
> OUTLINE
> TIMELINE
> VmanO
> Ln5,Col15ps:2UTF-5
> AlEnginoer
> AlEngineer
> 2O28
> EUROPE

![[assets/slides/KLSuFPj2ld0/slide-007.jpg]]

OCR text:

> spt npx tsxindex.ts
> AIE
> AlEnginoer
> Engineering the future of Al

![[assets/slides/KLSuFPj2ld0/slide-008.jpg]]

OCR text:

> , a a en Ce | Ce © cr red ra’ my i a aR
> ; Te Erie
> ee ee
> as aa
> Pela paynent_eethod. details: {
> * ad cord: (
> brand: ‘vise’,
> * 5d country: ‘US’,
> * * display.beand: ‘visa’,
> * va epszomh: 4,
> cad exp_yeor: 2027,
> fingerprint: ‘thfEL TcD4sZV6Gpe',
> funding: ‘credit’,
> generated from: mull,
> lasta: '4242*,
> netaork_tokendetotls: rutt,
> networks: (Object),
> regulated status: ‘unregulated’,
> three_d_secure_usage: null,
> wollet: null
> }
> type: ‘card
> ,
> Te]. a |
> ae
> PRS q
> ae Engineering the future of Al
> en ‘

![[assets/slides/KLSuFPj2ld0/slide-009.jpg]]

OCR text:

> Machine Payments Protocol a
> _
> ay a
> | - | | AlEngineer |
> aa aad

![[assets/slides/KLSuFPj2ld0/slide-010.jpg]]

OCR text:

> IPV6::1
> Host localhost:4242was resolved.
> mpp pnpn run dev
> IPv4:127.0.0.1
> >mpp-rest-node-typescripte dev/Users/stevekoliski/stripe/ai-demo/mpp
> Connected tolocalhost（:1）port 4242
> Trying[::1]:4242...
> >tsxmain.ts
> >GET/paidHTTP/1.1
> injectingerv（1)from.env
> >Host:localhost:4242
> >User-Agent:curl/8.7.1
> Server1istening athttp://Localhost:4242
> >Accept：/*
> CreatedPaymentIntentpi_3TKJkuA4XFULvrcoe0JBLo21 forSe.e1->ex8a39b0e
> d41Fd88337b634659C71EB10aff696806
> Request completely sent off
> CreatedPaymentIntent pi_3TKJkeA4XFULvrc@BoRDapmU for S0.01->Bx8a39bDe
> AIE
> <HTTP/1.1402Payment Requiredl
> d41Fd88337b634659C71EB18aff696806
> <mW-Authenticate：:Paymentid=15nJQCyoaXueKpcrUtZo1LSa32bnN1wpGg33kz19CFA
> 8",realn="localhost°，method="tempo"，intent="charge”，request="eyJhbw91b
> mppclear\
> nQi0iIxMDAwMCIsImN1.cnJ1bmNSIjoiMHgyMGMMDAwMDAwMDAMDAwMDAwMDAMDAwMDAwMDA|>
> DAwMDAMDAwIwibVeaG9kRGVemWscyI6ey]jaGFpbkLkIjoMjQzMXesInJ1Y21mVud
> CI6Ij840GEzORJEZWQeMUZk0OAzMzdiNjMENjUSQzCxRUIxMGFmZjY5NjhENi39°,expires=
> mpppnpn run de
> mppcurlhttp://Localhost:4242/free-v
> mppclear
> *2026-04-09T15:26:28.089Z"
> <Cache-Control:no-store
> mpp pnpe run dev
> <Content-Type:application/problem+json
> <Content-Length：192
> >mpp-rest-node-typescripte dev/Users/stevekaliski/stripe/ai-demo/mpp
> <Date:Thu,09Apr 202615:21:28 GMT
> >tsxmain.ts
> <Connection:keep-alive
> <Keep-Alive:timeout=5
> injectingenv（1)fromenv//tip:-auth forogents
> Connection# to hostlocalhostleftintact
> Serverlisteningathttp://localhost:4242
> CreatedPaymentIntent pi_3TKKOZA4XFULvrc@1WqwnFxl for S0.01->ex8a39bDe
> nt Required",status":402,"detail":“Payment is required.
> d41Fd88337b634659C71E818aff696806
> 5nJQCyoaXueKpcrUtZo1LSa3ZbrN1wpGg33kz19CF8}
> mpp
> AEnginoer
> Engineering the future of Al

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
