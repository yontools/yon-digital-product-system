---
name: yon-learn
description: Deliberately promote reviewed, evidence-backed reusable product knowledge into YON patterns or capabilities while enforcing privacy and evidence standards.
disable-model-invocation: true
---

# YON Learn

Turn a reviewed extraction candidate into reusable YON knowledge. This is a promotion workflow, not automatic learning.

## Objective

Promote only knowledge that is:

- generalized;
- useful beyond one product;
- supported by evidence appropriate to its status;
- safe for the public repository;
- non-duplicative.

## Process

1. Read the extraction candidate and linked evidence.
2. Separate observations, interpretations, hypotheses, and outcomes.
3. Re-check the public/private boundary.
4. Inspect existing patterns, capabilities, indexes, and maps.
5. Decide whether to create, update, reject, or defer the candidate.
6. Choose lifecycle status conservatively.
7. Update the target document and relevant index/map when promotion is authorized.
8. Preserve evidence and changelog information.
9. Run YON structural validation.

## Status rules

- `DISCOVERED` — identified but not sufficiently evaluated.
- `EXPERIMENTAL` — plausible reusable knowledge with limited evidence.
- `PROVEN` — supported by strong evidence across real usage, testing, or repeated implementations; scope is documented.
- `DEPRECATED` — no longer recommended, with reason documented.

Never promote to `PROVEN` merely because one project succeeded once.

## Reject or defer when

- the insight is product-specific;
- evidence is only an assumption;
- the privacy check fails;
- an existing item already covers the behavior;
- scope or trade-offs are unclear;
- verification is materially blocked.

## Privacy

Never publish private source code, credentials, secrets, customer data, proprietary prompts, identifying business rules, or private architecture. Generalize before promotion.

## Output

Return:

- candidate decision;
- evidence assessment;
- privacy assessment;
- existing knowledge considered;
- lifecycle status;
- files promoted or updated;
- validation result;
- remaining uncertainty.
