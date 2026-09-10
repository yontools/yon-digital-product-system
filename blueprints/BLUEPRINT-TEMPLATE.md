# YON Product Blueprint

> Decision contract between product understanding and implementation. Not an automatic architecture, database schema, framework prescription, or permission to redesign working behavior.

## 0. Traceability

`BUSINESS OUTCOME → WORKFLOW → ARCHETYPE → PRODUCT PRIMITIVES → CAPABILITY / PATTERN → DECISION → EXECUTION → VERIFICATION`

Use the chain where it materially clarifies a decision. Do not invent missing links; record gaps or uncertainty instead.

## 1. Product outcome

- Product / working title:
- Primary business/user outcome:
- Primary users / participants:
- Success criteria (observable or measurable):
- Existing behavior to preserve:
- Constraints / project-local instructions:

## 2. Business operating context

> Complete when the request describes a real-world operation. Archetypes are behavioral hypotheses, not templates or automatic feature lists.

| Archetype | Confidence | Behavioral signals observed | Relevant workflow(s) | Why it matters |
|---|---|---|---|---|
| | HIGH / MEDIUM / LOW | | | |

- Combined archetypes needed:
- Deliberately excluded archetypes / why:

## 3. Participants & relationships

| Party | Context | Role | Relationship | Permission / boundary | Relevant job |
|---|---|---|---|---|---|
| | | | | | |

Rules:
- Identity is not a role.
- Role is not a relationship.
- Authorization boundaries remain explicit.

## 4. Jobs & critical workflows

### Primary jobs

- 

### Critical workflow(s)

`TRIGGER → STEP → DECISION / HANDOFF → STEP → OUTCOME`

| Workflow | Trigger | Primary participant | Key steps / handoffs | Outcome | Critical states / exceptions |
|---|---|---|---|---|---|
| | | | | | |

### Important interaction states

- Loading:
- Empty / first use:
- Success:
- Error:
- Permission denied:
- Offline / degraded (if relevant):
- Edge / recovery:

## 5. Product model

> Use only the primitives that materially clarify the product. This is conceptual modeling, not a schema prescription.

### Parties / relationships

- 

### Core resources / entities

- 

### Actions / events

- 

### States / lifecycle

- 

### Time / temporal rules

- 

### Transactions / communications / documents

- 

### Boundaries / tenancy / authorization

- 

## 6. Capability resolution

| Workflow / need | Candidate capability | Classification | Maturity | Evidence status | Coverage | Archetype context | Gap decision | Decision / rationale | Next action |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

Classification must be one of: `DIRECT`, `SUPPORTING`, `OPTIONAL`, `MISSING`, `PRODUCT-SPECIFIC`.

For `MISSING`, gap decision must be one of: `YON-CANDIDATE`, `PRODUCT-SPECIFIC`, or `NEEDS-EVIDENCE`.

Maturity values: `DISCOVERED`, `EXPERIMENTAL`, `PROVEN`, `DEPRECATED`.

Evidence values: `UNVERIFIED`, `SUPPORTED`, `STRONG`, `CONTRADICTED`.

## 7. Pattern selection

| Workflow / product problem | Pattern | Why it fits | Evidence / validation | Decision |
|---|---|---|---|---|
| | | | | |

Do not add a pattern when the interaction does not need it.

## 8. Minimal composition & boundaries

### Required reusable capabilities

- 

### Supporting capabilities

- 

### Optional / explicitly deferred

- 

### Product-specific behavior

- 

### Ownership boundaries

| Behavior / responsibility | Owner | Depends on | Must not duplicate |
|---|---|---|---|
| | | | |

### Composition decisions

- Where do capabilities interact?
- What is deliberately not composed?
- Which behavior remains local to the product?
- What would be over-modeling or premature abstraction?

## 9. Product-specific behavior

List domain rules and decisions that belong to this product unless deliberate evidence supports reuse.

- 

## 10. Gaps, assumptions & questions

### Genuine gaps

- 

### Assumptions

- 

### Unresolved questions

- 

### Evidence needed before proceeding

- 

## 11. Risk & verification

| Gate | Scope | Risk / reason | Expected evidence | Result | Follow-up |
|---|---|---|---|---|---|
| Structure | YON / implementation integrity | | | | |
| Product Journey | Primary user outcome | | | | |
| UX | Critical interaction path | | | | |
| UI | Visual / responsive implementation | | | | |
| Accessibility | Inclusive use | | | | |
| Runtime | Running product / network / console | | | | |
| Security | Auth / authorization / tenant isolation / secrets | | | | |
| Regression | Existing affected behavior | | | | |

Results: `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE`.

**`BLOCKED` is never `PASS`.** If evidence cannot be obtained, record the blocker and its impact.

## 12. Implementation order

Order by user value, workflow dependency, risk, and ability to verify—not by feature count.

| Step | Objective | Blueprint trace | Dependencies | Risk | Expected evidence | State |
|---|---|---|---|---|---|---|
| 1 | | | | | | PLANNED |
| 2 | | | | | | PLANNED |
| 3 | | | | | | PLANNED |

Execution states:

`PLANNED → IN_PROGRESS → INSPECTING → CORRECTING → VERIFIED`

When execution cannot proceed:

`IN_PROGRESS → BLOCKED`

### Dependencies / sequencing constraints

- 

### Explicitly deferred

- 

## 13. Decision log

| Decision | Reason | Evidence / source | Impact | Revisit when |
|---|---|---|---|---|
| | | | | |

## 14. Execution handoff

> This section is the controlled handoff from Blueprint to `yon-execute`.

- Approved for execution: `YES / NO / PARTIAL`
- Execution scope:
- First executable slice:
- Required access / infrastructure:
- High-risk boundaries requiring explicit verification:
- Stop conditions:
- Definition of success for this execution:

## 15. Privacy check

- [ ] No private source code
- [ ] No secrets or credentials
- [ ] No customer/private data
- [ ] No proprietary prompts
- [ ] No confidential architecture
- [ ] No identifying business rules
- [ ] Reusable knowledge is generalized and public-safe

## 16. Evidence after implementation

- Observation:
- Intervention:
- Outcome:
- Limitations:
- Runtime / verification evidence:
- Candidate for extraction:

## Completion rule

The Blueprint is ready when the primary outcome and critical workflow are sufficiently understood to guide implementation without guessing; participants and relationships are explicit; applicable archetype context is justified; product primitives are no more detailed than necessary; capabilities and patterns are classified and traceable; composition boundaries and product-specific behavior are separated; gaps and uncertainty are honest; high-risk areas have proportional verification gates; implementation order is clear; and the execution handoff does not contain unresolved critical decisions.
