# YON Validation Index

| Gate | Scope | Minimum evidence |
|---|---|---|
| Structure | YON/plugin integrity | Required files and references resolve |
| Product Journey | User outcome | Primary affected flow exercised |
| UX | Interaction quality | Critical states and task path checked |
| UI | Visual implementation | Responsive and visual review |
| Accessibility | Inclusive use | Keyboard, focus, semantics, contrast, motion reviewed |
| Runtime | Running product | Browser/runtime/network behavior checked |
| Security | High-risk boundaries | Auth, authorization, tenant isolation, secrets reviewed when applicable |
| Regression | Existing behavior | Relevant existing flows/tests remain healthy |

## Result semantics

`PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE`.

A blocked check is evidence of missing verification, not evidence of correctness.
