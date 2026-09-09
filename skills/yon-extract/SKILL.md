---
name: yon-extract
description: Extract generalized reusable product knowledge from project evidence into candidate YON patterns or capabilities without copying private implementation details. Use only when deliberately converting validated project learning into reusable YON knowledge.
disable-model-invocation: true
---

# YON Extract

Turn evidence from a real project into a reviewable candidate for reusable YON knowledge.

## Objective

Extract the lesson, not the private implementation.

## Process

1. Inspect the relevant project context and evidence.
2. Separate direct observations from interpretations and hypotheses.
3. Identify the user/problem outcome the solution addresses.
4. Check existing `patterns/INDEX.md`, `capabilities/INDEX.md`, and `capabilities/CAPABILITY-MAP.md` before proposing something new.
5. Decide whether the insight is a `PATTERN`, `CAPABILITY`, `PRODUCT-SPECIFIC`, or `NEEDS-MORE-EVIDENCE`.
6. Generalize names, examples, architecture, and implementation details.
7. Run the privacy check.
8. Produce an extraction candidate for human review.

## Never do automatically

- Never publish private project knowledge into the public repository without deliberate review.
- Never copy private source code, credentials, customer data, proprietary prompts, secrets, or confidential business rules.
- Never turn one implementation into a universal rule without acknowledging scope and evidence strength.
- Never mark a candidate `PROVEN` solely because it worked once.

## Candidate output

Return:

- proposed name;
- candidate type;
- generalized problem;
- reusable behavior/solution;
- evidence sources and status;
- confidence;
- limitations/scope;
- existing YON items considered;
- proposed destination;
- privacy-check result;
- explicit review required before promotion.

## Quality bar

A good extraction is specific enough to be useful, abstract enough to reuse, evidence-backed, and safe to publish.
