---
name: audit-history
description: Preserve a trustworthy history of important product actions and state changes.
status: experimental
domains: operations, compliance, debugging, security
---

# Audit History

## Problem
Users and operators need to understand what changed, who changed it, and when, especially for important business or administrative actions.

## When to use it
Use when traceability matters: financial changes, permissions, approvals, operational state transitions, sensitive records, or support/debugging workflows.

## Inputs
- Actor
- Action
- Resource
- Previous state when relevant
- New state or meaningful change summary
- Timestamp
- Context/correlation identifier when available

## Outputs
- Immutable or append-oriented audit event
- Human-readable history view when needed
- Search/filter capability for operational investigation when justified

## Core behavior
Record meaningful events rather than every database mutation. Keep audit records separate from ordinary mutable application state when practical.

## UX considerations
Show concise human-readable events, with enough context to understand the change. Avoid overwhelming users with implementation-level noise.

## Data considerations
Capture actor, action, resource reference, timestamp, and a safe summary. Protect sensitive fields and consider retention requirements.

## Integration points
Authentication, authorization, workflow engine, admin UI, support tools, database triggers or application services.

## Edge cases
- System-generated changes
- Deleted actors/resources
- Bulk operations
- Failed actions
- Sensitive values changed
- Clock/time-zone differences

## Verification
Verify important actions produce correct records, unauthorized changes are not possible, sensitive values are not unnecessarily exposed, and history remains consistent after retries or bulk operations.

## Evidence
Experimental until validated through repeated implementations.

## Privacy check
Do not publish real customer records, private actor identifiers, secrets, sensitive field values, or proprietary compliance requirements.
