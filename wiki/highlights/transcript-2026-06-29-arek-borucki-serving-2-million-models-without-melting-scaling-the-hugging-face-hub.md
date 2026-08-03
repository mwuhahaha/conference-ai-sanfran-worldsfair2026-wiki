---
title: "Highlights: Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub"
category: "highlights"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Highlights: Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub

- Talk: [[2026-06-29-arek-borucki-serving-2-million-models-without-melting-scaling-the-hugging-face-hub]]

## Highlights
- P99 latency is the metric that drives the design choices, so the team optimizes for fast reads, not just average-case performance.
  - Evidence: "P99 is much more important than P50 and we are paying a lots of attention to P99 and that's the reason why we invest in premputee tokens denormalize optimize for read collection in MongoDB full text search based on Apache lucine Kubernetes autoscaling and soon in database sharding."
  - Transcript: [[youtube-lyL5QhgIOxc-transcript]]
- Separating metadata from binary artifacts lets the platform scale storage, metadata, and compute independently.
  - Evidence: "This separation of concern let us scale metadata independently from binary storage and compute independently from both."
  - Transcript: [[youtube-lyL5QhgIOxc-transcript]]
- The architecture works by keeping the primary focused on the work only it can do and pushing everything else to other machines.
  - Evidence: "The pattern is simple. Primary should focus on what only primary can do. Anything else can be pushed to different machines."
  - Transcript: [[youtube-lyL5QhgIOxc-transcript]]
- The platform is designed to scale automatically from low to very high pod counts without manual intervention or routine overprovisioning.
  - Evidence: "Our deployment hub deployment can scale from 10 to 500 bots depends of on the traffic. This is how we keep the hub healthy without manual interventions and without infrastructure overprovisioning."
  - Transcript: [[youtube-lyL5QhgIOxc-transcript]]
- The practical goal of all the infrastructure work is to keep the user experience simple even when the backend is complex.
  - Evidence: "This is what scaling medium models is really about. Keeping the user experience simple no matter how complex it gets under the hood."
  - Transcript: [[youtube-lyL5QhgIOxc-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
