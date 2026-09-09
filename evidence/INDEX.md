# YON Evidence Index

| Type | Meaning | Typical strength |
|---|---|---|
| Observation | Directly observed behavior, friction, state, or workflow | Low–medium |
| User Feedback | Explicit user/operator/stakeholder report | Medium |
| Experiment | Controlled or intentional change used to test a hypothesis | Medium–high |
| Runtime Verification | Evidence from exercising the actual implementation | High for implementation behavior |
| Regression | Evidence about preservation or breakage of existing behavior | High for affected behavior |
| Production Outcome | Evidence from real usage or meaningful business/product outcomes | High when measurement is reliable |

## Evidence status

| Status | Meaning |
|---|---|
| `UNVERIFIED` | Recorded but not sufficiently supported |
| `SUPPORTED` | Credible evidence supports the claim |
| `STRONG` | Multiple or high-quality sources support the claim |
| `CONTRADICTED` | Evidence materially challenges the claim |

## Required distinction

Evidence describes what supports a claim. It does not automatically prove that the claim is universal.

A pattern or capability can become `PROVEN` only after deliberate review of the evidence, scope, limitations, and repeatability. A single successful implementation is not enough to assume universal validity.

## Extraction candidates

Evidence can produce a candidate reusable insight:

- `PATTERN` — recurring solution to a product/interface problem.
- `CAPABILITY` — reusable product/business behavior spanning one or more interfaces.
- `PRODUCT-SPECIFIC` — useful locally but not sufficiently general for YON.
- `NEEDS-MORE-EVIDENCE` — promising but not ready to generalize.

## Privacy boundary

Evidence used for public YON knowledge must be generalized. Remove or abstract:

- private source code;
- credentials, tokens, secrets, keys;
- customer or user personal data;
- private company identifiers when not necessary;
- confidential business rules;
- proprietary prompts or internal instructions;
- private architecture details whose disclosure is not intentional.

The goal is to preserve the lesson, not the private implementation.
