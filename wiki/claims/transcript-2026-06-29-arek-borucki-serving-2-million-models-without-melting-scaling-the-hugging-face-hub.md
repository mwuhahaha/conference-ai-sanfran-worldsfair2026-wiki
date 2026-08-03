---
title: "Claims: Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub"
category: "claims"
generatedBy: "talk-semantic-digestion-v1"
sourceLabels: ["Official recording transcript", "Semantic digestion"]
---
# Claims: Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub

- Talk: [[2026-06-29-arek-borucki-serving-2-million-models-without-melting-scaling-the-hugging-face-hub]]

## Claims
- Hugging Face says it hosts 3 million public models, 1 million datasets, and 50,000 organizations. (`explicit`)
  - Evidence: "We host three million public models, 1 million data sets, 50,000 organizations, and not only hobbyists or scientists."
  - Transcript: [[youtube-lyL5QhgIOxc-transcript]]
- The speaker says more than 30% of the Fortune 500 use Hugging Face as part of their AI workflows. (`explicit`)
  - Evidence: "More than 30% of Fortune 500 use hugging face as a part of AI workflows. Just to give you some perspective, few years ago we had 20,000 models."
  - Transcript: [[youtube-lyL5QhgIOxc-transcript]]
- Model artifacts, tokenizer files, card assets, and configuration files are stored separately in cloud object storage such as AWS S3. (`explicit`)
  - Evidence: "The actual models artifacts, tokenizer files, cart assets and configuration files are stored separately in cloud object storage such as AWSS3."
  - Transcript: [[youtube-lyL5QhgIOxc-transcript]]
- The team switched from regex-based search to Atlas Search because the earlier approach did not scale well as the catalog grew. (`explicit`)
  - Evidence: "So we decided to switch to Atlas search that's a feature which is using Apache lucine under the hood."
  - Transcript: [[youtube-lyL5QhgIOxc-transcript]]
- The operational rule is that the primary should focus on what only the primary can do, and everything else should be pushed to other machines. (`explicit`)
  - Evidence: "The pattern is simple. Primary should focus on what only primary can do. Anything else can be pushed to different machines."
  - Transcript: [[youtube-lyL5QhgIOxc-transcript]]
- The team plans to move from HPA to KEDA so scaling can respond to real application metrics instead of only CPU and memory. (`explicit`)
  - Evidence: "The difference HPA scale only based on CPU and memory. KDA scale on real application metrics like request per second or event loop utilization."
  - Transcript: [[youtube-lyL5QhgIOxc-transcript]]

## Evidence Boundary
Derived from the linked official transcript. These are attributed talk takeaways and claims, not independent verification.
