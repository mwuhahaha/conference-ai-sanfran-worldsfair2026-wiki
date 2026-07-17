---
title: "Slides: Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov"
category: "slides"
video_id: "4uFVSLgD2Q4"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov

## Source Video
[Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov](https://www.youtube.com/watch?v=4uFVSLgD2Q4)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/4uFVSLgD2Q4/slide-001.jpg]]

OCR text:

> Al Engineer Conference 2026 CpenGov?
> Agents in Production: How OpenGov
> Built and Scaled OG Assist
> + @
> +, OG Assist a

![[assets/slides/4uFVSLgD2Q4/slide-002.jpg]]

OCR text:

> OpenGov7
> a. | Meet OG Assist
> 2. | The Origin Story
> | Betting on Effect
> | The Core Agent Loop
> | A2A, Evals & Sandboxing
> eae
> 6. | Long Context Handling
> d )
> 7. Monitoring & Observability
> 2. | Tools, Skills & Dev Workflows al

![[assets/slides/4uFVSLgD2Q4/slide-003.jpg]]

OCR text:

> OpenGov
> AboutOpenGov
> Software for
> more effective,
> accountable
> government.
> Founded over 14years ago,OpenGov builds ERP.budgeting.
> govemmentandOGAssist nowconnects across allof it.

![[assets/slides/4uFVSLgD2Q4/slide-004.jpg]]

OCR text:

> —. OpenGov?
> ou
> Coin. Us Software for
> see ante amc | _— eT
> ae si os accountable
> - . Bete eT dalteial 8

![[assets/slides/4uFVSLgD2Q4/slide-005.jpg]]

OCR text:

> OpenGov7
> |
> ———.
> o <= = <a ee tne ca be os + @ Y — Onigin Story
> Clow 00 Asst
> One bet on
> See teee Risriensect 2 npuseeais eit eee ee
> re con. ~~ agents, one
> Gers ates Ones orang Yee al Amand Cored Tesal Payments Teen tontey .
> Ow: $69 0 me z is
> immediate yes.
> Be egts by Prymant Method 2 oe
> O ae —
> Your bllng breatdoan awe ts as § . : : A principal engineer spun up a team focused on Al agents and
> oe es seo . © asked me to join. OG Assist grew from there. We started to
> . Bie ee . 4 integrate deeply with our products through frontend and
> backend tools.

![[assets/slides/4uFVSLgD2Q4/slide-006.jpg]]

OCR text:

> OpenGov
>
> =
>
> 3 Effect .

![[assets/slides/4uFVSLgD2Q4/slide-007.jpg]]

OCR text:

> OpenGovT
> interface AgentCard{
> 1/Hunan-readablena
> for the Agent （e-g.,Recipe Agent)
> //Hunan-readable description of the Ageot's function
> description: string:
> /uRL addresswhere the Agent is hosted
> url:string:
> 1/Service provider information for the Agent
> provider?:(
> Agent-to-Agent Protocol
> organization:string:
> url:string:
> 11Version of the Agent(format defined by provider,e.g.,"1.o.e)
> version:string:
> documentationurl7:string:
> I/uRL for the Agent'sdocumentation
> Built Off The
> capabilities:{
> streaning?:boolean;// If the Agent supports SSE
> pushNotifications?:boolean://If the Agent can push update notifications to the client
> stateTransitionHistory?:boolean: // If the Ageot exposes task state change history
> A2AProtocol
> //Authentication requirenents for the Agent (intended to match OpenAPI auth structure)
> authentication1{
> schees:stringll://e.g.,Basic,Bearer
> I/Default Interaction nodes supported by the Agent across all skitls
> defaultInputModes:stringI]:// Supported input MINE types
> defaultoutputModes:stringIl:// Supported outputMIME types
> I/Collection ofcapability units the Agent can perform
> skills:(
> id:string:// unique identifier for the skiit
> name:string:// Mumn-readable name for the skill
> TheA2Aprotocol allowsOGAssist tobuild offasupported
> description: string://Skill description
> spec,rather than from the ground up.
> tags:stringll:// Tagsdescribing the skill's capability category (e.g.,"cooking,"cu
> examples7:stringl]:// Exanple scenarios or pronpts the skill can execute （e.g.,Inee
> Source:https://agent2agent.info/docs/concepts/agentcard/

![[assets/slides/4uFVSLgD2Q4/slide-008.jpg]]

OCR text:

> OG Assist =: OpenGov7
> Pease croote a POF seth besuttul wt to
> Qreet the tos of the AlEngneer
> Corterence 2076 Prease atiow me to
> downriosd to share mith them
> eouarny « Sandboxing
> Done
> -edlteenerGnkcwoeRifeina Room to act
> and made it avanable for dannioad pinches orginal Al 5
> Agr ed Gener ative artwork and a navn greoting message
> for conterence alterdees f |
> safely.
> Ry As Lgeeet Conference 20.0) Greeting FOF
> ‘ asa
> @ haerenet
> tout gs
> Code runs in isolated sandboxes. so agents can take real action
> without putting production systems or customer data at risk.
> . en tos '
> a .

![[assets/slides/4uFVSLgD2Q4/slide-009.jpg]]

OCR text:

> OG Assist =. @Jer= al Clea
> Gonorato me a tong estay gye me some
> options for what the exsey can be about
> BD Croce an ensey topic
> a Goverreneet 7 -
> Pee tee Cag & Shs
> cant ties ns Ul. on
> The Future of Pita Touceteon the ahs
> 3 Ce eS
> Scud Media anc Demacescy
> be aes ees
> Uis car be create fon demgrh hy te agent foferre
> or ae ee ees ee
> epi wt
> Re eee Sree
> o e.|
> si
> Cc 5 |
> eo . © #2 » “he

![[assets/slides/4uFVSLgD2Q4/slide-010.jpg]]

OCR text:

> OpenGov
> Observability
> You can'tscale
> examplecliertwun
> whatyou can't
> 646666466d
> see.
> Source:https://effect.website/docs/observability/tracing/
> Every agent run is traced end to end. giving us the visibility to
> debug,measure,and tune behavioratproduction scale.

![[assets/slides/4uFVSLgD2Q4/slide-011.jpg]]

OCR text:

> OpenGovY
> DeveloperVelocity
> Building agents
> with agents.
> Claude Code,Cursor,and cloud agents accelerate how the
> team writes,reviews,and ships building OGAssist with the
> samekindof toolswe ship.

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
