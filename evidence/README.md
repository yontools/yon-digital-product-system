# YON Evidence

Evidence is the layer that connects real product work with reusable YON knowledge.

YON should not call a pattern or capability `PROVEN` merely because it sounds good. Evidence records what was observed, tested, measured, or validated and why a reusable insight deserves its current confidence.

## What evidence is for

Use evidence to:

- distinguish observation from inference;
- document experiments and their outcomes;
- support pattern and capability maturity;
- preserve useful product-learning without copying private implementations;
- make future YON decisions more grounded.

## Evidence is not automatic learning

YON does **not** silently publish knowledge from private projects.

A private project may generate an evidence record or extraction candidate, but promotion into the public YON system must be deliberate and privacy-checked. Never publish secrets, credentials, customer data, private source code, identifying business rules, proprietary prompts, or confidential architecture.

## Evidence types

- **Observation** — something directly observed in a product, workflow, interface, or runtime.
- **User Feedback** — explicit feedback from users, operators, clients, or stakeholders.
- **Experiment** — a deliberate intervention intended to test a hypothesis.
- **Runtime Verification** — evidence collected by exercising the real implementation.
- **Regression** — evidence that a change preserved or damaged existing behavior.
- **Production Outcome** — evidence from real-world use, business outcomes, support volume, adoption, completion, or other meaningful results.

## Evidence status

- `UNVERIFIED` — recorded, but insufficient support for the claim.
- `SUPPORTED` — credible evidence supports the claim.
- `STRONG` — multiple or high-quality evidence sources support the claim.
- `CONTRADICTED` — evidence materially challenges the claim.

Evidence status is not the same thing as capability/pattern maturity. A reusable item should still be reviewed before being promoted to `PROVEN`.

## Recommended flow

`REAL PROJECT → EVIDENCE → EXTRACTION CANDIDATE → REVIEW → PATTERN/CAPABILITY → VALIDATION → MATURITY UPDATE`

The extraction step must generalize the learning rather than copy the implementation.
