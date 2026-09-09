# YON Validation System

Validation is the evidence layer of YON. It prevents the system from declaring success because code exists or a build passes.

## Validation layers

1. **Structure** — required YON/plugin files exist and are internally referenced.
2. **Product** — the intended user journey and business outcome work.
3. **UX/UI** — hierarchy, interaction states, consistency, accessibility, and responsive behavior.
4. **Runtime** — real routes, browser behavior, network/runtime errors, and affected integrations.
5. **Safety** — permissions, tenant boundaries, destructive actions, secrets, and high-risk changes.
6. **Regression** — important existing behavior still works.

## Gate model

A validation result should distinguish:

- `PASS` — evidence supports acceptance.
- `FAIL` — a required condition is broken.
- `BLOCKED` — validation could not be performed because an environment/dependency is unavailable.
- `NOT_APPLICABLE` — the check does not apply.

Do not convert `BLOCKED` into `PASS`.

## Principle

Validation is proportional to risk. Authentication, authorization, billing, migrations, destructive operations, security controls, and core business rules require stronger evidence than cosmetic changes.

## Output

A useful validation report records the check, expected result, observed result, evidence, severity, and follow-up action.
