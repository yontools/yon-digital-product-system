---
description: Promote reviewed evidence-backed product knowledge into YON patterns or capabilities without exposing private project details.
---

# /yon-learn

Use the `yon-learn` workflow when a reviewed extraction candidate is ready to become reusable YON knowledge.

## Rules

1. Read the extraction candidate and its evidence.
2. Verify the privacy boundary again before promotion.
3. Confirm the proposed knowledge is generalized and not product-specific.
4. Check for an existing pattern or capability that should be updated instead of creating a duplicate.
5. Require sufficient evidence for the requested lifecycle status.
6. Update the target knowledge and its index only when explicitly authorized to promote.
7. Record evidence and changelog information.
8. Run `/yon-validate` against the YON repository after promotion.

## Promotion principle

`DISCOVERED → EXPERIMENTAL → PROVEN → DEPRECATED`

Promotion is deliberate. One successful implementation is not enough to mark knowledge `PROVEN`.

## Output

- candidate reviewed
- privacy check
- existing knowledge considered
- promotion decision
- files changed
- evidence supporting the decision
- validation result
- remaining uncertainty
