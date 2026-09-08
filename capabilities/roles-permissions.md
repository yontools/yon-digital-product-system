---
name: roles-permissions
description: Model who can access, view, create, modify, approve, or administer product resources.
status: experimental
domains: security, authorization, teams, SaaS
---

# Roles & Permissions

## Problem
Different users and organizations need different levels of access without scattering authorization rules throughout the interface.

## When to use it
Use when a product has multiple users, teams, organizations, sensitive resources, approval flows, or administrative responsibilities.

## Inputs
- Actor identity
- Organization/tenant context
- Resource
- Action
- Role or policy
- Resource ownership/context

## Outputs
- Allow/deny decision
- Reason suitable for logs or debugging
- Effective permissions where useful to the UI

## Core behavior
Authorization must be enforced at the data/action boundary, not only by hiding UI controls. Support least privilege, explicit ownership, and organization/tenant isolation where applicable.

## UX considerations
Only expose actions the user can realistically perform, but distinguish unavailable actions from failed actions when that distinction helps the user. Explain permission problems without leaking protected information.

## Data considerations
Keep identity, membership, role/policy, resource scope, and audit information separate where practical. Avoid encoding authorization solely in client-side state.

## Integration points
Authentication, database row-level security, API authorization, admin panels, audit history, invitations.

## Edge cases
- User changes organization
- Role changes during a session
- Removed membership
- Resource ownership transfer
- Conflicting policies
- Privileged administrative actions

## Verification
Test every sensitive action at the authorization boundary, including direct API/database access, cross-tenant access, role changes, and revoked memberships.

## Evidence
Experimental until validated through repeated implementations and security testing.

## Privacy check
Never publish credentials, real user identifiers, private policies, tenant data, or security-sensitive implementation details from a private product.
