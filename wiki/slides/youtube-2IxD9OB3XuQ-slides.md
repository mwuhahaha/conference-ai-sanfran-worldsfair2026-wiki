---
title: "Slides: Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI"
category: "slides"
video_id: "2IxD9OB3XuQ"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI

## Source Video
[Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI](https://www.youtube.com/watch?v=2IxD9OB3XuQ)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/2IxD9OB3XuQ/slide-001.jpg]]

OCR text:

> Soheil Feizi
> Founder & Chief Scientist, RELAI
> Associate Prof, CS @ University of Maryland
> https://relat.ai

![[assets/slides/2IxD9OB3XuQ/slide-002.jpg]]

OCR text:

> Humans learn from experience.
> vCiil
> feedback act
> World
> act > get eee > improve without forgetting

![[assets/slides/2IxD9OB3XuQ/slide-003.jpg]]

OCR text:

> Continual Learning for an Al Agent
> ra
> | AGENT |
> MODEL HARNESS MEMORY
> 
> cae LLM(s): weights prompts - skills - in-session state }
> ; model selection tools - code - persistant ;
> } workflow knowledge
> continuously improve
> the agent from its experiences ides
> without forgetting. ane
> y
> = : PVC a ye wal elke) J

![[assets/slides/2IxD9OB3XuQ/slide-004.jpg]]

OCR text:

> benchmark + evaluator
> Teele ane lie Vetch Evaluator
> curated task aU rab eth. 4 scores Output
> PASS / FAIL / REWARD
> + Feedback
> i

![[assets/slides/2IxD9OB3XuQ/slide-005.jpg]]

OCR text:

> Inproduction,a rawlogisn'tfeedback
> Sessionlog AnLLM/codeanalyzesthelog AUTOMATIC
> agent: searching flights... user:bookme a flighttoNYC change. Amodel oreval codereads the trace andwrites a critique on what to Scalesto everysession
> agent: called tool get_flights()
> agent:returned3options Ahumangivesexpertfeedback CRITICAL
> user:none of these work-wrong date Domain experts catchwhatmodelsmiss:subtlecorrectness,policy, andtaste.
> Lowervolume
> Eitherway,wenowhave:sessionlog+feedback

![[assets/slides/2IxD9OB3XuQ/slide-006.jpg]]

OCR text:

> Matha oes] ?
> An inferred distribution that replays what happened + what success means.
> t Ba
> ki Mocked / real tools Synthetic user Evaluators
> feedback
> run candidate agents against it, then keep the fix only if it passes. f

![[assets/slides/2IxD9OB3XuQ/slide-007.jpg]]

OCR text:

> Threelayerstoimprovetheagent
> Model update theweights SFTRL post-training mostexpensive
> Harness editprompts,skills,tools,code GEPA:trace-to-harness mostflexible
> Memory storefactsand learnedskills Lettamem0 consolidation cheapest
> Agood learningengine asksforthe smallestdurable change attherightl

![[assets/slides/2IxD9OB3XuQ/slide-008.jpg]]

OCR text:

> Updating the model weights
> SFT
> imitate correct trajectories; needs labeled examples of the right behavior
> Supervised fine-tuning
> RL post-training
> sample, score against a reward or preference signal, reinforce what wins
> DPO-GRPO: RLVR
> LoRA
> limits the setof parameters that can change; cheaper, safer updates
> Low-Rank Adaptation
> '
> They need:
> Hard to apply to a raw production log (unless we lift it into a replayable enve

![[assets/slides/2IxD9OB3XuQ/slide-009.jpg]]

OCR text:

> Updating the harness
> Rewrite the prompts, skills, and code around the model.
> Trace-to-harness GEPA & prompt search
> ROC Oley nary Ob ane eGo Ran ay eaemet eo) bee aa an ren groban Tecan en pio aero meni Cava etic a Gre CMO Pe Omm Lento ars
> pclae wis Src Cleo Cols mC HE ys a! Gai Canora cues ane Pcie Gaye retro ami) pie Clee Eco MR aerate Sc

![[assets/slides/2IxD9OB3XuQ/slide-010.jpg]]

OCR text:

> Updating memory
> Write down facts and distill skills, so the agent doesn’t rediscover them.
> Information memory
> store a fact or correction; e.g., “always confirm the date before booking”
> Skill distillation
> compress a successful trajectory into a reusable how-to packet
> [scmetresviewmed asa patoafharess!
> : : - works directly on (log + feedback) but usually unverifie F

![[assets/slides/2IxD9OB3XuQ/slide-011.jpg]]

OCR text:

> Verifiable Continual Learning (VCL)
> ee a eh ; .. improving an agent from its own experience, where every
> han to help and to break nothing that already worked.
> 
> An executable test A measured delta A regression check
> eee ae Serko s tre acer asic ro 3/4 ee ey rom a Om mCe he ca OMe mn teeSsea en Sen TEES Sea
> acme eC Us Pie ees eC salm Biot ae aes rc) no
> 
> i

![[assets/slides/2IxD9OB3XuQ/slide-012.jpg]]

OCR text:

> Replayable
> Turn a one-off failure into a test you can re-run.
> & learning environment
> 
> a ee ee a ce
> symone persona, ‘epiuys the intwrachon
> 
> ae Pea Cine e
> scorns pass /fa./ res
> 
> i

![[assets/slides/2IxD9OB3XuQ/slide-013.jpg]]

OCR text:

> Holistic
> One failure may have several causes and several possible repairs.
> the agent cites a stale policy and skips the required escalation.
> Route the fix to the layers that explains the failure withthe .. ... >

![[assets/slides/2IxD9OB3XuQ/slide-014.jpg]]

OCR text:

> Lifelong
> Anew fix must improve the new case without breaking the past.
> © already optimized overE, .. E,. Anew failure E,.1 arrives.
> a) Patch & hope > drift oO) Regression-aware learning
> ; : : : ' performance on E,s,
> ; ; oe no regression on £, .. &
> Y .
> Regression-control should be , not post-hor

![[assets/slides/2IxD9OB3XuQ/slide-015.jpg]]

OCR text:

> Efficient
> Efficiency in updates to the agent:
> Model update
> Search over harness , ,
> Erna cn ee
> Memory write , oe
> A
> Efficiency in regression-aware optimization loop

![[assets/slides/2IxD9OB3XuQ/slide-016.jpg]]

OCR text:

> RELAI’s learning loop
> oO Signals (logs - feedback - prompts)
> © Replayable learning environments
> :] Root-cause > route to a layer
> oO) Regression-aware optimization
> ry) Reviewable, versioned update : ,

![[assets/slides/2IxD9OB3XuQ/slide-017.jpg]]

OCR text:

> Add VCL to your agents in
> acRe- Seen anes
> ot ] Use your own LLM
> an Compatible with all major agent frameworks
> Initial agent < : p
> $ relai learning-env create --log-file --feedback
> Create learning environments from lag/feedback or synthetically
> ; ; Simulators (mock/real tools, persona,...) and evaluators (code/LLMs)
> y $ relai optimize
> ae Holistic: adjusts prompts, models, tools, skills, s
> Lifelong: online regression control i
> Optimized version PR
> c

![[assets/slides/2IxD9OB3XuQ/slide-018.jpg]]

OCR text:

> Meridian Support Agent
> Areproducible test-bed for continual learning in a tool-using support agent.
> =) Asingle source of truth A) Interacting policies
> a a ae aa AR acer a a et Caria ae eg an a A a a aera oc maaan iar
> a) Deterministic evaluators Pe ie ee et
> @ Decisions are tool calls Se a ee ee oe oe ee ee
> co ) Regression-sensitive by design ST ae a Se

![[assets/slides/2IxD9OB3XuQ/slide-019.jpg]]

OCR text:

> o
> :a rude, adversarial caller
> relai Tearning-eny create -- prompt
> “A rade, adversarial culti tues casteter caewersution. phe caustentee devapes a”
> dmautneri2ec Pigh dollar refune tngt snculd ret se grantee”
> y

![[assets/slides/2IxD9OB3XuQ/slide-020.jpg]]

OCR text:

> The generated
> Persona,
> 
> intent, mocked/real
> 
> tools
> 
> ors kYAre ILM oazcl Orsi ce lac)
> 
> with feedback
> all produced from one
> interactive command.
> 
> 4

![[assets/slides/2IxD9OB3XuQ/slide-021.jpg]]

OCR text:

> Run it:the currentagentstruggles
> relai simulate rude-user-multiturn-refund-escalation
> 0.78/1.00 average-two evaluators fail
> WHEREITBREAKS
> required-escalation
> didnotroutetheunauthorizedrefundtoreview
> latency-budget
> toomanyturns/toolcallsunderpressure
> WHATALREADYHOLDS
> forbidden-direct-refund
> held:neverissued therefund directly
> safety-disclosure
> held:no policy or contract leakage

![[assets/slides/2IxD9OB3XuQ/slide-022.jpg]]

OCR text:

> The other source:
> relal Joarning-env create \
> Ome oun
> “een fast elipiole refunds, nut do cot penerelize pererosity beyond
> eee aie chee eee omen e | RM ra eee Ueno Occ
> oO dat marsha 1c: (ol - ME ORa Tem EO Te CA EST SEO RD © a replayable learning env:
> © feedback — th. cotrectinn eas Serre tas tac or tar are TESTOR SEIS | ag ora

![[assets/slides/2IxD9OB3XuQ/slide-023.jpg]]

OCR text:

> Lifelong agent improvements
> F
> This is in practice:
> each update is tested, every gain is measured, and nothing that already vw’ aa% *,

![[assets/slides/2IxD9OB3XuQ/slide-024.jpg]]

OCR text:

> Takeaways
> Agent continual learning is not only model fine-tuning.
> ees eee ely ce Ceres orca tea) C Mee arehe rome OMe cio torre Be mane Gack trir sa Bren
> Production logs are not learning environments.
> ice hare t more me cs alm OMe CM mac pi WTO) CANO RCL an Marea COT
> The frontier is regression-aware continual improvement.
> Pra esate cf mean: VRC ae Gea) mone Chane om ronr ume nO 10 aam
> , ,
> Verifiable continual learning = + a as
> Bi s'alaeleh

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
