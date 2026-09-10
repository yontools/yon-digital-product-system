# Tool Action Contract

Use this template for a significant tool-mediated action.

## 1. Identity

- Action ID:
- Date/context:
- Project scope:
- Related Blueprint:
- Related Execution Plan slice:

## 2. Objective

- Desired outcome:
- User/product workflow affected:

## 3. Tool selection

- Tool class:
- Concrete adapter/tool:
- Why this tool is sufficient:
- Alternatives rejected and why:

## 4. Authorization

- Risk: `LOW | MEDIUM | HIGH`
- Permission required:
- Authorization source:
- Sensitive data involved: `YES | NO`
- External side effect: `YES | NO`

## 5. Execution

- Minimum input/context:
- Preconditions:
- Expected result:
- Side effects:

## 6. Observation

- Actual result:
- Evidence:
- Runtime state:
- Unexpected behavior:

## 7. Decision

- Next action:
- Continue / stop / rollback:
- Reason:

## 8. Verification

- Acceptance criterion:
- Verification method:
- Result: `PASS | FAIL | BLOCKED | NOT_APPLICABLE`

## 9. Privacy / boundary check

Confirm that the action did not expose or publish:

- secrets
- credentials
- private customer data
- proprietary code
- private prompts
- identifying business rules
- data belonging to another tenant/project

## 10. Final disposition

`COMPLETED | BLOCKED`

If blocked, record the exact missing condition and the smallest safe next action.
