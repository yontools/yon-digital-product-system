# /yon-policy

Define or review a policy and decision boundary for a consequential product behavior.

## Process

1. Read `skills/yon-policy/SKILL.md` and `policy/POLICY-CONTRACT-TEMPLATE.md`.
2. Establish outcome, actor, context, resource, action, workflow/state, relationships, permissions, and constraints.
3. Define applicable conditions and required evidence.
4. Define `ALLOW`, `DENY`, `REQUIRE_APPROVAL`, `BLOCKED`, or `NOT_APPLICABLE` outcomes.
5. Separate policy from tool availability, authorization, workflow, and agent autonomy.
6. Define escalation, stop, and failure behavior.
7. Define proportional verification and audit/evidence requirements.
8. Keep private decision logic and customer data private.

## Rules

- Never convert unknown context or authority into permission.
- Do not infer authorization from a graph relationship.
- Do not infer authority from tool availability.
- Do not let agent autonomy bypass policy.
- High-risk actions require explicit policy and proportional verification.
- `BLOCKED` is never `ALLOW`.

## Output

Return the policy contract, decision boundary, affected workflows, verification gates, unresolved blockers, and next implementation step.
