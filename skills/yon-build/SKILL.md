---
name: yon-build
description: Build a new SaaS, website, landing page, dashboard, or digital product with YON from requirements through verification.
disable-model-invocation: true
---

# YON Build

YON Build turns an understood product request into a verified implementation. For broad or multi-workflow products, a Product Blueprint is the contract between product understanding and implementation.

## Build sequence

`UNDERSTAND → BUSINESS DISCOVERY → PRODUCT MODEL → DISCOVER → RESOLVE → BLUEPRINT → IMPLEMENT → RUN → VERIFY`

### 1. Understand

Identify the goal, users, participants, roles, relationships, primary jobs, critical workflows, constraints, success criteria, existing behavior, and project-local instructions.

### 2. Business Discovery

When the request describes a real-world business operation, use `yon-business-discovery` before treating the business category as a product specification. Identify the smallest combination of Business Operating Archetypes supported by the actual workflow. Archetypes are hypotheses, not templates, feature lists, schemas, or architecture.

### 3. Product Model

For broad products, use the Universal Product Model when it materially clarifies participants, relationships, resources, actions, events, states, temporal rules, workflows, transactions, communications, documents, or boundaries. Do not over-model.

### 4. Discover

Use `yon-capability-discovery` when the request spans multiple reusable behaviors or when the product model is unfamiliar. Search capabilities, patterns, and evidence. Classify matches and identify genuine gaps.

### 5. Resolve

Use `yon-capability-resolver` to select the smallest justified composition. Do not force matches or silently turn optional capabilities into requirements.

### 6. Blueprint

For broad products, create or update a Product Blueprint using `blueprints/BLUEPRINT-TEMPLATE.md`. The Blueprint should make participants, relationships, workflows, entities, lifecycle, capability composition, patterns, gaps, product-specific behavior, risks, implementation order, and verification gates explicit.

A Blueprint is a decision contract, not an automatic architecture or database schema. It must not override project-local constraints or justify unnecessary changes to working behavior.

### 7. Implement

Define the smallest useful product surface. Establish information architecture and primary flows before expanding scope. Build reusable components and consistent interactions. Design loading, empty, success, error, permission, and edge states. Treat responsive behavior and accessibility as part of implementation.

Choose architecture appropriate to the repository. Reuse existing architecture and components where appropriate. Avoid feature inflation, unnecessary dependencies, fake functionality, placeholder UX in production paths, and generic decoration without product purpose.

### 8. Run / Inspect / Correct

Run the real product as early as practical. Exercise critical workflows, inspect browser/runtime behavior, console/network failures, responsive states, and relevant accessibility behavior. Correct regressions rather than declaring success from source code alone.

### 9. Verify

Use `validation/INDEX.md` to select proportional gates. Verify the original user outcome end-to-end. Record meaningful findings as evidence when they can support future reusable knowledge.

## High-risk changes

Authentication, authorization, billing, destructive operations, migrations, security controls, external integrations, tenancy/isolation, and core business rules require stronger understanding and verification.

## Completion

A build is complete only when the affected user journey works in the running product, important states are handled, responsive/accessibility concerns have been considered, relevant runtime/security boundaries are verified, and the implementation remains consistent with the approved product intent.
