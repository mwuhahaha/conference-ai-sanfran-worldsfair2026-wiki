---
title: "Voice Agents"
category: "topics"
sourceLabels: ["Slide/video-derived supporting context"]
---

# Voice Agents

## Synopsis
Voice agents are AI systems that understand, reason, and respond through speech, often in real time. They combine speech recognition, speaker diarization, language models, tool use, dialogue state, text-to-speech, and sometimes visual or screen output.

## Origin And Context
They build on IVR systems, speech recognition, voice assistants, call-center automation, real-time media systems, and conversational AI. Modern multimodal and realtime models make them more fluid, but production voice still depends on latency, turn-taking, and trust.

## Why It Matters
Voice is natural for hands-free, high-attention, or emotionally sensitive workflows. It also exposes failures quickly: delays, interruptions, wrong speaker attribution, and unnatural responses break trust faster than in text.

## How To Use It
Design around conversation state, latency budgets, interruption handling, speaker identity, fallback paths, and clear tool permissions. Test with realistic audio conditions, accents, overlapping speakers, and production transcripts.

## Where It Is Useful
Voice agents are useful in customer support, healthcare intake, sales calls, meeting assistants, field work, accessibility tools, tutoring, and companion interfaces.

## When To Use It
Use voice when speaking is faster or more accessible than typing, or when the workflow happens away from a keyboard. Prefer text when precision, reviewability, or complex visual comparison is primary.

## Active Use Cases
- Realtime support and appointment workflows.
- Meeting and call understanding with speaker attribution.
- Voice-in visual-out interfaces for richer task completion.
- Hands-free operational assistants.

## Related Slide Decks
- [[youtube-I2cbIws9j10-slides]] — WF26: Harness Engineering & Startup Battlefield ft. Garry Tan, Mike Krieger, @t3dotgg , DSPy (80 extracted slide frames)

## Related Scheduled Sessions
- [[2026-06-29-bohan-li-realtime-voice-agents-with-frontier-intelligence]] — Realtime Voice Agents with Frontier Intelligence; [[bohan-li|Bohan Li]] (Day 2 — Session Day 1 · 2:50pm-3:10pm · Voice & Realtime AI; official schedule)
- [[2026-06-29-charlie-guo-voice-agents-can-just-do-things]] — Voice Agents Can Just Do Things; [[charlie-guo|Charlie Guo]] (Day 2 — Session Day 1 · 11:40am-12:00pm · Voice & Realtime AI; official schedule)
- [[2026-06-29-valeria-wu-fon-speech-to-speech-model-research-at-google-deepmind]] — Speech-to-Speech Model Research at Google DeepMind; [[valeria-wu-fon|Valeria Wu Fon]], [[tom-ouyang|Tom Ouyang]] (Day 2 — Session Day 1 · 11:10am-11:30am · Voice & Realtime AI; official schedule)
- [[2026-06-29-sumanyu-sharma-i-monitored-crime-audio-voice-agents-scare-me-more]] — I Monitored Crime Audio. Voice Agents Scare Me More.; [[sumanyu-sharma|Sumanyu Sharma]] (Day 2 — Session Day 1 · 2:25pm-2:45pm · Voice & Realtime AI; official schedule)
- [[2026-06-29-midam-kim-my-name-is-my-name-is-a-linguistic-map-for-building-and-debugging-voice-agents]] — "My name is... my name is...": A Linguistic Map for Building and Debugging Voice Agents; [[midam-kim|Midam Kim]] (Day 2 — Session Day 1 · 3:20pm-3:40pm · Voice & Realtime AI; official schedule)
- [[2026-06-29-venky-b-5-voice-agent-failure-modes-you-ll-hit-in-week-one]] — 5 Voice Agent Failure Modes You'll Hit in Week One; [[venky-b|Venky B]], [[vyas-a|Vyas A]] (Day 2 — Session Day 1 · 1:55pm-2:15pm · Voice & Realtime AI; official schedule)
- [[2026-07-01-kwindla-kramer-voice-is-the-universal-interface]] — Voice is the universal interface; [[kwindla-kramer|Kwindla Kramer]], [[neil-zeghidour|Neil Zeghidour]] (Day 4 — Session Day 3 · 11:40am-12:00pm · Expo Stage 3 SW; official schedule)
- [[2026-06-29-paula-dozsa-tolan-voice-first-ai-companion]] — Tolan: Voice-First AI Companion; [[paula-dozsa|Paula Dozsa]] (Day 2 — Session Day 1 · 1:30pm-1:50pm · Voice & Realtime AI; official schedule)
- [[2026-07-01-vivek-muppalla-200-million-patient-interactions-later-what-the-generic-voice-stack-misses]] — 200 Million Patient Interactions Later: What the Generic Voice Stack Misses; [[vivek-muppalla|Vivek Muppalla]] (Day 4 — Session Day 3 · 12:05pm-12:25pm · AI in Healthcare; official schedule)
- [[2026-06-29-fuad-ali-voice-agents-are-mostly-invisible-here-s-how-to-see-them]] — Voice Agents Are Mostly Invisible. Here's How to See Them.; [[fuad-ali|Fuad Ali]] (Day 2 — Session Day 1 · 1:55pm-2:15pm · Expo Stage 2 NW; official schedule)
- [[2026-06-29-neil-zeghidour-your-voice-agent-is-just-a-walkie-talkie]] — Your Voice Agent is Just a Walkie-Talkie; [[neil-zeghidour|Neil Zeghidour]] (Day 2 — Session Day 1 · 12:05pm-12:25pm · Claws & Personal Agents; official schedule)
- [[2026-06-30-thor-schaeff-build-realtime-multimodal-agents-with-gemini-live]] — Build realtime multimodal agents with Gemini Live; [[thor-schaeff|Thor 雷神 Schaeff]] (Day 3 — Session Day 2 · 10:45am-11:05am · Workshops Day 2; official schedule)
- [[2026-06-30-thor-schaeff-build-realtime-multimodal-agents-with-gemini-live-continued-2]] — Build realtime multimodal agents with Gemini Live (continued 2); [[thor-schaeff|Thor 雷神 Schaeff]] (Day 3 — Session Day 2 · 11:10am-11:30am · Workshops Day 2; official schedule)
- [[2026-06-30-thor-schaeff-build-realtime-multimodal-agents-with-gemini-live-continued-3]] — Build realtime multimodal agents with Gemini Live (continued 3); [[thor-schaeff|Thor 雷神 Schaeff]] (Day 3 — Session Day 2 · 11:40am-12:00pm · Workshops Day 2; official schedule)
- [[2026-06-30-matt-lawler-fde-playbook-build-an-ai-support-agent-and-give-it-a-voice]] — FDE Playbook: Build an AI Support Agent and Give It a Voice; [[matt-lawler|Matt Lawler]] (Day 3 — Session Day 2 · 11:10am-11:30am · Expo Stage 4; official schedule)
- [[2026-06-30-rishab-kumar-from-stateless-to-stateful-orchestrating-real-time-voice-and-messaging-agents-with-twilio-and-amazon-bedrock]] — From Stateless to Stateful: Orchestrating Real-Time Voice & Messaging Agents with Twilio and Amazon Bedrock; [[rishab-kumar|Rishab Kumar]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · Expo Stage 2 NW; official schedule)
- [[2026-06-29-nick-nisi-lifestyles-of-the-ai-native-voice-coding-agent-skills-hooks-and-scheduled-tasks]] — Lifestyles of the AI-Native: Voice-coding, agent skills, hooks and scheduled tasks; [[nick-nisi|Nick Nisi]], [[zack-proser|Zack Proser]] (Day 1 — Workshop Day · 4:30pm-5:30pm · Workshops Day 1; official schedule)
- [[2026-07-01-lina-colucci-voice-agents-with-realtime-video]] — Voice agents with Realtime Video; [[lina-colucci|Lina Colucci]] (Day 4 — Session Day 3 · 1:55pm-2:15pm · Generative Media; official schedule)
- [[2026-07-01-idan-gazit-realtime-multiplayer-automation-and-you]] — Realtime multiplayer, automation, and you!; [[idan-gazit|Idan Gazit]] (Day 4 — Session Day 3 · 2:50pm-3:10pm · Agentic Engineering; official schedule)
- [[2026-06-29-sonar-expo-welcome-speech]] — Expo Welcome Speech; [[sonar|Sonar]], [[extend-ai|Extend AI]] (Day 1 — Workshop Day · 6:00pm-6:15pm · Expo Stage 3; official schedule)
- [[2026-06-30-thor-schaeff-build-realtime-multimodal-agents-with-gemini-live-continued-4]] — Build realtime multimodal agents with Gemini Live (continued 4); [[thor-schaeff|Thor 雷神 Schaeff]] (Day 3 — Session Day 2 · 12:05pm-12:25pm · Workshops Day 3; official schedule)
- [[2026-06-29-amit-desai-act-confirm-or-stop-smarter-behavior-for-ai-assistants-wearables-and-robots]] — Act, Confirm, or Stop? Smarter behavior for AI assistants, wearables & robots; [[amit-desai|Amit Desai]] (Day 2 — Session Day 1 · 3:45pm-4:05pm · Voice & Realtime AI; official schedule)
- [[2026-06-29-kwindla-kramer-the-new-primitives-building-ai-native-software]] — The New Primitives: Building AI-Native Software; [[kwindla-kramer|Kwindla Kramer]] (Day 2 — Session Day 1 · 10:45am-11:05am · Voice & Realtime AI; official schedule)
- [[2026-07-01-sai-krishna-rallabandi-wearing-the-agent-engineering-a-family-and-friends-personal-agent-from-group-chats-to-glasses]] — Wearing the Agent: Engineering a Family-and-Friends Personal Agent, from Group Chats to Glasses; [[sai-krishna-rallabandi|Sai Krishna Rallabandi]] (Day 4 — Session Day 3 · 3:45pm-4:05pm · AI in Finance; official schedule)

## Related People
- [[neil-zeghidour|Neil Zeghidour]]
- [[thor-schaeff|Thor 雷神 Schaeff]]
- [[kwindla-kramer|Kwindla Kramer]]
- [[kent-c-dodds|Kent C. Dodds]]
- [[swyx|swyx]]
- [[bohan-li|Bohan Li]]
- [[charlie-guo|Charlie Guo]]
- [[valeria-wu-fon|Valeria Wu Fon]]
- [[tom-ouyang|Tom Ouyang]]
- [[sumanyu-sharma|Sumanyu Sharma]]
- [[midam-kim|Midam Kim]]
- [[venky-b|Venky B]]
- [[vyas-a|Vyas A]]
- [[paula-dozsa|Paula Dozsa]]
- [[vivek-muppalla|Vivek Muppalla]]
- [[fuad-ali|Fuad Ali]]
- [[matt-lawler|Matt Lawler]]
- [[rishab-kumar|Rishab Kumar]]
- [[nick-nisi|Nick Nisi]]
- [[zack-proser|Zack Proser]]
- [[lina-colucci|Lina Colucci]]
- [[idan-gazit|Idan Gazit]]
- [[sonar|Sonar]]
- [[extend-ai|Extend AI]]

## Related Companies
- [[google-deepmind|Google DeepMind]]
- [[gradium|Gradium]]
- [[plivo|Plivo]]
- [[daily|Daily]]
- [[workos|WorkOS]]
- [[couplework-ai|CoupleWork AI]]
- [[epicproduct-engineer|EpicProduct.engineer]]
- [[sondermind|SonderMind]]
- [[latent-space-ai-engineer|Latent Space / AI Engineer]]
- [[eliseai|EliseAi]]
- [[openai|OpenAI]]
- [[hamming-ai|Hamming AI]]
- [[servicenow|ServiceNow]]
- [[tolan|Tolan]]
- [[hippocratic-ai|Hippocratic AI]]
- [[arize-ai|Arize AI]]
- [[assemblyai|AssemblyAI]]
- [[twilio|Twilio]]

## Transcript And Resource Support
### Transcript-backed resources
- [[youtube-mFLlVpnGpds]] — Beyond Transcription: Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI
- [[youtube-u-rJwPPU3QA]] — How to talk to statues — Joe Reeve, ElevenLabs
- [[youtube-ij-AU9dpJjc]] — Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co
- [[youtube-65X0pQ6Lmbg]] — Voice In, Visuals Out: The Agony and the Ecstasy - Allen Pike, Forestwalk Labs
- [[youtube-hVJOnuhFmTA]] — The Prompt Is Still a Punch Card - Ted Johnson, JoinIn AI
- [[youtube-HsxQICTLF84]] — Building an ACP-Compatible Agent Live — Bennet Fenner, Zed
- [[youtube-kZsf_Sfm7RU]] — The Missing Layer After Launch - Raphael Kalandadze, Wandero AI
- [[youtube-G6IlDzj8OjA]] — GTM Is You - Victoria Melnikova, Evil Martians

### Quote signals
- “We can just switch to having voice in visuals out and then we benefit from the more forgiving visual response envelope that people have.” — [[youtube-65X0pQ6Lmbg]]
- “And today I'm going to be sharing some of what we've learned building voice in visuals out experiences using AI.” — [[youtube-65X0pQ6Lmbg]]
- “But there's some real breakthroughs over the last few months where both of this visuals in and audio or the audio in and visuals out experience is now um really feasible.” — [[youtube-65X0pQ6Lmbg]]
- “So for that you need to know who's who who spoke when.” — [[youtube-mFLlVpnGpds]]
- “And the question is now we need to assign a speaker to each word.” — [[youtube-mFLlVpnGpds]]
- “So in there you you'll be able to to with Pianoteq open source toolkit for diarization with piano metrics for evaluation.” — [[youtube-mFLlVpnGpds]]
