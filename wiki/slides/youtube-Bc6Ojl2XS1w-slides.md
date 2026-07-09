---
title: "Slides: From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind"
category: "slides"
video_id: "Bc6Ojl2XS1w"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind

## Source Video
[From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind](https://www.youtube.com/watch?v=Bc6Ojl2XS1w)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/Bc6Ojl2XS1w/slide-001.jpg]]

OCR text:

> PLATINUMSPONSORS
> # Braintrust
> Workos
> OpenAl

![[assets/slides/Bc6Ojl2XS1w/slide-002.jpg]]

OCR text:

> a) a - , ao¥, a ma
> : FENG
> a ark
> WHAT'S NEW IN Al AUDIO? yee <
> ™ Z 7
> at ole at.
> Google DeepMind
> Dd
> ra oy , |
> & ;
> ne 7 7 _ e
> I ae
> ‘ ae

![[assets/slides/Bc6Ojl2XS1w/slide-003.jpg]]

OCR text:

> ae
> a 4
> Pane a .
> * * ; ww lees]
> rs Fs i ka
> a r a fey a
> ce,
> . fet
> py
> Thor Schaeff
> Developer Relations Engineer,
> ce tarosannelole lang
> oy Engineering the future of Al

![[assets/slides/Bc6Ojl2XS1w/slide-004.jpg]]

OCR text:

> Shipping at relentless pace
> FrontierModels
> ni 2.5 Pro
> MS'ZN
> ini2.5Pro
> Gemini 2.5 Flath
> AIE
> ni2.0
> L.SFlaa
> n2.0
> 2.0Pre
> 2O24May-Jun-Jul-Aug-Sep-Oct-Nov-Dec2O25Jan-Feb-Mar-Apr-May-Jun-Jul-Aug-Sep-Oct-Nov-Dec
> Gemma2
> Cemma3
> Gemma4
> TlL. 279
> E2L (43: 2HE.AAL 211
> Gemma3n
> OpenModels
> AlEngineer
> EUROPE

![[assets/slides/Bc6Ojl2XS1w/slide-005.jpg]]

OCR text:

> genMediaModels
> Veo3.1 Lihe
> en4 Fast
> LyrlaReafTime
> Lyrla3 Clp6Pro
> AIE
> YD2
> Veo2
> /eo3.1
> feo3.1Fa
> 2024May-Jun-Ju-Aug-Sep-Oct-Nov-Dec2O25Jan-Feb-Mar-Apr-May-Jun-Jul-Aug-Sep-Oct-Nov-Dec2O26
> Jdy-e-qa-uer
> Chirp3
> Flash/Pro TTS
> Gemii2.5
> Gemini 2.S Flash Native Audic
> Gemini 2.5 Flash Native Audlo
> Audiomodels
> Engineering the future of Al
> AIEng

![[assets/slides/Bc6Ojl2XS1w/slide-006.jpg]]

OCR text:

> ranean’ : Our goal is to build models that
> 
> i i deeply comprehend. richly
> mn . : transcribe, and robustly reason
> 
> ran through audio -- seamlessly
> : handling any mix of languages,
> ; dialects, accents. and modalities.
> Anywhere. Always.
> Es
> | Al Engineer |
> seco) a
> ’

![[assets/slides/Bc6Ojl2XS1w/slide-007.jpg]]

OCR text:

> Pe
> Turn your audio into accurate text © ee
> Paka a
> * oy + AR tn Oy Be
> * ba Ce See ak alba rhs aa
> * a : ta tf ace
> * * Oe
> * ad
> * a *
> Start Recording
> Baa COTS Las]
> | Al Engineer |
> Sue) a 3
> i

![[assets/slides/Bc6Ojl2XS1w/slide-008.jpg]]

OCR text:

> es on fae
> ‘ ra é fo 8
> EchoScript ~ Remix Ca Device i?) Sb
> EchoScript Al Power ty Gena A ash Prawn &
> Transcription Results Start Over
> Pei
> bf bd
> * * Summary
> * id
> aa Thor from Google DeepMind introduces the topic of Al Audio, specifically focus:ng on
> developments within DeepMind and the Gem:ns API. He introduces himself and
> demonstrates multi-lingual capabuities Dy greeting the audience in English, German,
> French, Japanese, and Chinese
> .
> Detailed Transcript
> & Thor Ayre 8 oe Mies © Nets
> Allright, what's nev in Al audio? I'm sorry, it's a bttle bit misicading because the tie
> leaves out the ‘at Google DeepMind’. So we're just kind of looking at, you know, what
> Engi ing the fut a
> g fe
> | ate . ~~

![[assets/slides/Bc6Ojl2XS1w/slide-009.jpg]]

OCR text:

> Audio Understanding
> constmodelId="gemini-3-flash-preview"
> const prompt=
> You are an expert audio transcription assistant.
> Process the provided audio file and generate a detailed transcription.
> AIE
> Requirements:
> 1.Identify distinct speakers （e.g.,Speaker 1,Speaker 2,or names if context allows）.
> 2.Provide accurate timestamps for each segment （Format:MM:SS).
> 3.Detect the primary language of each segment.
> 4.If the segment isin a language different than English,also provide the English
> translation.
> 5.Identify the primary emotion of the speaker in this segment.You MuST choose exactly
> one of the following:Happy,Sad,Angry,Neutral.
> Engineering the future ofAl
> AIEn

![[assets/slides/Bc6Ojl2XS1w/slide-010.jpg]]

OCR text:

> Prompting structure
> A robust prompt ideally includes the following elements that come together to
> ae craft a great performance:
> . mn e Audio Profile - persona / character identity (age, background
> ad Ace)
> * . .
> e Scene - Sets the stage. Describes both the physical
> environment and the “vibe”.
> e Director's Notes - Performance guidance: style, breathing,
> pacing, articulation and accent.
> e Sample context - contextual starting point
> “) e Transcript
> Ce Ba
> error:
> ad
> fee eet na
> ee
> Cg
> ¥ a

![[assets/slides/Bc6Ojl2XS1w/slide-011.jpg]]

OCR text:

> Prompting structure
> A robust prompt ideally includes the following elements that come together to
> ak ¥ craft a great performance:
> . * e Audio Profile - persona / character identity (age, background
> * * etc)
> * ve bd
> e Scene - Sets the stage. Describes both the physical
> environment and the “vibe”.
> e Director's Notes - Performance guidance: style, breathing,
> pacing, articulation and accent.
> e Sample context - contextual starting point
> ! e Transcript
> Ce a
> paves
> per Ena
> et
> CR
> Engineering the future of Al
> \

![[assets/slides/Bc6Ojl2XS1w/slide-012.jpg]]

OCR text:

> rr ~ Gemini
> mn .
> 3: vest aucia Text, audio, video +
> App Bee eee Live API
> Engineering the future of Al
> .

![[assets/slides/Bc6Ojl2XS1w/slide-013.jpg]]

OCR text:

> Yi gt}
> Bi iree are CRE Taal oem OC Tema TSHeI IC)
> Poi
> * a Model Model ID Tai arelg ecTieeh itera) Output
> sae
> * *
> we * Tarn) Cast Ems et rd Spee eo et Oe eas
> iol ee Cs
> Lyna 3 ORT tena lai Oe ree cera Pmeet ere CSHB Eee na aL aed
> isfy eed BU CrmnS ee om Mtoe: (Peres On eas Use Cee ST FeO MEE
> Fae
> pares
> Pad
> Paerior ——
> | Al Engineer |
> " SUL cela

![[assets/slides/Bc6Ojl2XS1w/slide-014.jpg]]

OCR text:

> AIEngineer
> EUROPE
> HTTPS://AI.ENGINEER

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
