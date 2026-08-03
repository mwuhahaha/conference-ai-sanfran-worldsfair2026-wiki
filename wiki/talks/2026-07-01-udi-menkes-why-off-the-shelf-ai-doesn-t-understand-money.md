---
title: "Why Off-the-Shelf AI Doesn't Understand Money"
category: "talks"
date: "2026-07-01"
time: "11:10am-11:30am"
track: "AI in Finance"
room: "Track 3"
speakers: ["Udi Menkes"]
sourceLabels: ["Official conference schedule", "Public YouTube metadata"]
scheduleTrack: "AI in Finance"
scheduleRoom: "Track 3"
scheduleLabels: ["AI in Finance", "Track 3", "session", "confirmed"]
---
# Why Off-the-Shelf AI Doesn't Understand Money

## Conference Context
- Date/time: 2026-07-01 · 11:10am-11:30am
- Track/room: AI in Finance · Track 3
- Speaker(s): Udi Menkes
- Session type/status: session · confirmed

- Track: AI in Finance
- Room: Track 3
- Session type: session
- Status: confirmed

## Session Description
Ask any LLM a financial question about your business. You'll get a fluent, confident, generic answer — one that doesn't truly know your business, or what happened when businesses like yours made that same decision. We build financial AI at Intuit serving 100M+ customers. Our custom LLMs outperform general-purpose models on accuracy while cutting latency in half. But that's the foundation, not the destination. I'll cover where financial intelligence goes when AI stops reporting what happened and starts helping you decide what to do next (and does it for you).

## Synthesis
### Transcript-Backed Summary
The talk argues that off-the-shelf LLMs fail on money because they are fluent about finance without having watched what actually happened in similar real businesses. Udi Menkes proposes grounding advice in verified outcomes from internal system-of-record data: turn business histories into state, action, and outcome trajectories, use broad models to generate candidate moves, then train a grounded learner to choose the action most likely to improve profit, cash flow, or revenue. The tradeoff is that bigger models and more context are not enough on their own; the advantage comes from proprietary outcome data and causal structure, which can produce safer recommendations and support better action plans. The practical consequence is a shift from asking which model is best to asking how to steer AI toward the outcomes a business actually wants, with the same pattern framed as useful beyond finance.

### Key Takeaways
- The critical difference is not whether a model has read about money, but whether it has seen verified outcomes in real business situations.
  - Evidence: "And here's what I want you to think about. A frontier model has read about money, but a grounded model in real outcome has actually watched what happens."
- Naive before-and-after comparisons can mislead; you need a causal estimate that accounts for which businesses were already more likely to take the action.
  - Evidence: "So, the real difference is more like $1,150 for this illustration. And we measure the impact of actions on the outcome through a measure called Kate, conditional average treatment error, which looks at that connection."
- A practical architecture is to let one model propose candidate actions and then use a grounded learner to decide which move is actually appropriate.
  - Evidence: "But then we would use a model that we trained using reinforcement learning in order to figure out which one of those is actually a right move to do versus a mistake that could drive the business down."
- The speaker's broader claim is that outcome-driven AI will favor organizations with strong systems of record and unique data sets, not just larger foundation models.
  - Evidence: "The winners in my opinion are going to be those with the best system of records, creating unique data sets out of them and then training the models to achieve the outcomes."

### Claims From The Talk
- The speaker argues that off-the-shelf LLMs can sound fluent and confident about money while still being generic and disconnected from what actually happened in real business situations. (`explicit`)
  - Evidence: "And that's what I call the fluent bluff. The fluent bluff is a generic fluent and confident answer that frontier LLMs can give you around money because of what they learned on the internet, blogs, books, advice columns, what people wrote about money, but not based on what actually happened."
- In the rental-property example, the frontier model recommends acquiring a second rental property even though the business is already in negative cash flow. (`explicit`)
  - Evidence: "How do I improve my profit? And a frontier model gives the following response. Go and acquire a second rental property because that'll bring more income and compensate for the deficit."
- In the egg-supplier example, the frontier model recommends raising prices 15 to 20 percent even though one customer supplies most of the revenue and one vendor accounts for most of the cost. (`explicit`)
  - Evidence: "Same question, how do I improve my profit? A frontier model says raise your prices 15 to 20%."
- The grounded model, based on similar real outcomes, recommends raising the existing tenant's rent by 5 to 10 percent before renewal in the rental-property case. (`explicit`)
  - Evidence: "On the other hand, a model that is grounded in real outcomes and what I mean by that is a model that has seen similar situations of such businesses what they did and what was the outcome actually recommended to raise prices on the existing tenant by 5 to 10%."
- The speaker describes turning internal data into millions of state, action, and outcome vectors and training an RL model to determine which actions lead to the best outcomes in similar situations. (`explicit`)
  - Evidence: "So we create millions of vectors of state, action and outcome and then we train an R model to be able to understand in given situations of similar businesses which actions lead to the best outcomes."
- The resulting AI business advisor is described as being in beta and research preview, with proactive recommendations, explanations, and action plans for customers. (`explicit`)
  - Evidence: "And then we went ahead and built an experience out of it. And this is an AI business advisor that is currently in beta with research in a research preview with our customers where we use the LLM that I just described that we created to proactively raise opportunities for businesses at every given point of time."
- The speaker says the real moat is the data and grounding in outcomes, not simply access to a bigger or better model. (`strong`)
  - Evidence: "But it doesn't turn out to be true. And the moat here is that it's not about the model access, it's about the data itself that you have."

### Topics Covered
- **Fluent Bluff** — The problem of fluent but unreliable financial advice from general-purpose models.
- [[agent-evaluations|Verified Outcomes]] — Using actual outcome histories instead of text-only knowledge to inform decisions.
- **Outcome-Driven AI** — AI systems that optimize for business results rather than generic answer quality.
- [[agent-memory|Business Trajectories]] — Internal representations that combine business state, action, and outcome signals.
- [[context-engineering-and-knowledge-architecture|System of Records]] — The advantage of proprietary operational data and records over larger foundation models.

### Tools And Named Systems
- **QuickBooks** — Accounting and bookkeeping platform cited as a source of business financial data.
- **TurboTax** — Tax preparation product cited as one of the data sources feeding the company's models.
- **Credit Karma** — Personal finance product cited as one of the data sources feeding the company's models.
- **Mailchimp** — Marketing platform cited as one of the data sources feeding the company's models.

### Novel Concepts And Methods
- **Outcome Grounding** — Grounding advice in verified outcomes from similar real businesses instead of relying on text-only generalization.
- **Action Candidate Generation** — Generating candidate actions with a frontier model before passing them to a stronger decision layer.
- **Reinforcement Learning Action Selection** — Using reinforcement learning to decide which suggested action is likely correct versus harmful.
- **State-Action-Outcome Modeling** — Representing a business as state, action, and outcome vectors for learning from historical trajectories.
- **CATE-Based Impact Estimation** — Adjusting for selection bias when estimating the impact of an action on results.

### Open Questions
- **How can a team identify enough comparable situations across entities to reliably ground advice in verified outcomes?** — The approach depends on finding repeated patterns in the data, and without those comparable situations the grounding step may not be robust.
- **How can an advisory system combine grounded science with personalization so users feel included in the decision and still trust the recommendation?** — The speaker treats trust and user preference as part of the product, not just the model, so this affects adoption.
- **How can outcome-driven AI be steered toward the right domain-specific result in fields beyond finance?** — The talk argues the pattern should generalize to other domains, but the implementation details are still open.

### Derived Links And Source Material
- [[youtube-Owb8g3yDyzo-transcript]] — dedicated official recording transcript.
- [[youtube-Owb8g3yDyzo]] — official event recording.
- Structured digest: `wiki/resources/talk-digests/Owb8g3yDyzo--2026-07-01-udi-menkes-why-off-the-shelf-ai-doesn-t-understand-money.json`.

### Speaker Context
- [[udi-menkes|Udi Menkes]]

### Semantic Digestion Status
- Complete: 1 matched recording digest(s) passed the evidence contract.
- Generator: `talk-semantic-digestion-v1`.
- Contract: `sha256:b2176b9b38b8af2d93ef3f9b94b97af87a523540a7a0e328bd16faf168591990`.

### Evidence Boundary
This section is synthesized only from official schedule metadata and dedicated manifest-matched recording transcripts. Every listed takeaway, claim, topic, tool, method, and question is bound to a verbatim transcript excerpt in the structured digest. Speaker claims remain attributed event evidence, not independent verification.

## People
- [[udi-menkes]]

## Official YouTube Recording
- [[youtube-Owb8g3yDyzo|Why Off-the-Shelf AI Doesn't Understand Money — Udi Menkes, Intuit]] — official AI Engineer YouTube recording published 2026-07-29.
- Evidence status: [[youtube-Owb8g3yDyzo-transcript]] — dedicated official recording transcript.
- Boundary: use these recordings as media evidence; keep date/time/room facts tied to the official schedule.

## Media Evidence
- [[youtube-Owb8g3yDyzo]] - dedicated official event recording.
- [[youtube-Owb8g3yDyzo-transcript]] - dedicated official recording transcript.

- Source video: `youtube-Owb8g3yDyzo`
- Slide deck: [[youtube-Owb8g3yDyzo-slides|Slides: Why Off-the-Shelf AI Doesn't Understand Money — Udi Menkes, Intuit]] — 12 visible slide image(s).
![[assets/slides/Owb8g3yDyzo/slide-001.jpg]]
![[assets/slides/Owb8g3yDyzo/slide-002.jpg]]
![[assets/slides/Owb8g3yDyzo/slide-003.jpg]]
- Slide-derived themes for `youtube-Owb8g3yDyzo`: model, proposes, verified, close, outcomes, engineering, future, action.

## Transcript Status
Cached dedicated-session transcript text is available at `raw/sources/youtube-transcripts/Owb8g3yDyzo.txt` (2,840 words).

## Transcript Markdown
- [[youtube-Owb8g3yDyzo-transcript]] — dedicated official recording transcript; source cache `raw/sources/youtube-transcripts/Owb8g3yDyzo.txt`.
## Evidence Graph
This section is generated from the official schedule, manifest-matched session recordings, and explicitly linked supporting sources. Official event media matched to other sessions is excluded from this talk's evidence layer.

### Media Signals
- `youtube-Owb8g3yDyzo` — 2,840 transcript words; 10 slide-derived text signals; role: primary event evidence.
- Interpretation rule for `youtube-Owb8g3yDyzo`: attribute claims to the recording or speaker unless independently corroborated.
- Transcript signals for `youtube-Owb8g3yDyzo`: model, models, business, data, outcomes, prices, businesses, frontier.
- Slide-derived themes for `youtube-Owb8g3yDyzo`: model, proposes, verified, close, outcomes, engineering, future, action.
- Evidence links for `youtube-Owb8g3yDyzo` (primary event evidence): [[youtube-Owb8g3yDyzo]], [[youtube-Owb8g3yDyzo-transcript]], [[youtube-Owb8g3yDyzo-slides]]

### Agent Reading Notes
Use exact recording signals for session-level claims. Keep related external or historical sources framed as supporting evidence.
