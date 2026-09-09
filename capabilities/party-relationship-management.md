# Party & Relationship Management

## Purpose

Represent the people and organizations that participate in a product and the meaningful relationships between them without hard-coding a vertical-specific role model.

## Problem

Many products need to represent the same real-world party in different contexts: a person can be a customer in one workflow, a professional in another, an owner, member, seller, supplier, patient, client, or contact. Organizations can also participate in multiple relationships with people and other organizations.

A product should not duplicate identities merely because a role or relationship changes.

## Capability

Provide a reusable model for:

- people and organizations as parties;
- stable identity for a party across contexts;
- contextual roles within an organization, workflow, or relationship;
- relationships between parties;
- membership and association with organizations;
- relationship metadata when the product needs it;
- lifecycle of relationships such as active, paused, ended, or pending when justified.

## Core concepts

### Party

A real-world participant represented by the product. A party may be a person or organization.

### Role

A contextual responsibility or position held by a party. Roles should not be confused with identity.

Examples include customer, professional, owner, seller, supplier, operator, member, or manager.

### Relationship

A meaningful connection between two parties or between a party and an organization/context.

Examples include customer-of, works-at, member-of, manages, supplies, or serves.

The exact relationship vocabulary remains product-specific unless repeated evidence supports broader standardization.

## Design rules

1. Keep identity separate from role.
2. Prefer one stable party record with multiple contextual relationships over duplicated identities.
3. Keep domain-specific relationship semantics local unless they are demonstrably reusable.
4. Do not imply that every product needs a graph database; implementation can use relational associations or another appropriate model.
5. Permissions remain a separate capability even when roles participate in relationships.
6. Audit history should record material relationship changes when required by the product.
7. Tenant/organization boundaries must be explicit for multi-tenant products.

## Composition

Commonly composes with:

- `roles-permissions.md` for authorization;
- `audit-history.md` for material relationship changes;
- `workflow-engine.md` when relationships affect workflow routing;
- `customer-management` when customer-specific behavior is required;
- domain capabilities such as rental, scheduling, assets, payments, or documents.

These are composition hypotheses, not automatic architecture.

## When to use

Use when a product has multiple participant types, organizations, memberships, or contextual roles and duplicating identities would create confusion or fragmented history.

## When not to use

Do not introduce this capability solely because a product contains a user account. A simple single-user product may not need a generalized relationship model.

## Verification

Verify that:

- the same party can participate in multiple valid contexts without duplicate identity records;
- role changes do not destroy historical relationships;
- organization boundaries remain correct;
- authorization does not rely on ambiguous identity data;
- relationship lifecycle and failure states are explicit where required.

## Lifecycle

`EXPERIMENTAL`

This capability is a reusable design hypothesis and should gain evidence through repeated implementations and verification before promotion to `PROVEN`.

## Evidence

No cross-product evidence is recorded in this capability yet. Do not infer `PROVEN` status from a single implementation.
