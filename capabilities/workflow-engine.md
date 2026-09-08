# Capability: Workflow Engine

**Status:** `experimental`

## Problem
Businesses repeatedly move entities through predictable operational stages. Without an explicit workflow, users rely on memory, manual follow-up, and inconsistent status updates.

## When to use
Use when an entity progresses through meaningful stages and different roles need to know what happened, what is allowed next, and who is responsible.

## Core behavior
Define explicit states, allowed transitions, transition triggers, required conditions, responsible roles, and resulting side effects. Preserve an event/history trail when operational traceability matters.

## UX considerations
- Make the current state obvious.
- Show the next useful action.
- Prevent invalid transitions instead of merely documenting them.
- Explain why an action is unavailable when useful.
- Avoid excessive states that do not change behavior.

## Data considerations
Separate current state from event history when auditability is important. Define transition rules centrally enough to avoid contradictory behavior across clients.

## Integration points
Assets, rentals, orders, approvals, notifications, billing, documents, tasks, and permissions.

## Edge cases and failures
- invalid transition
- concurrent transition
- missing prerequisite
- failed side effect
- rollback requirement
- archived entity

## Verification
- [ ] Valid transitions work
- [ ] Invalid transitions are prevented
- [ ] Preconditions are enforced
- [ ] Current state and history remain coherent
- [ ] Failed side effects have a defined recovery path
- [ ] Role permissions are respected

## Evidence
Generalized lifecycle/workflow capability intended for composition across business SaaS products.

## Privacy check
No project-specific code, secrets, customer data, credentials, or proprietary business rules are included.
