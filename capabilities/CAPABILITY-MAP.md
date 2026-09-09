# YON Capability Map

This map helps YON recognize reusable capability combinations when planning a new product.

## Participant-centered SaaS

`Party & Relationship Management + Roles & Permissions + Audit History`

Useful when people and organizations participate in multiple contexts, roles, memberships, or relationships and important changes need controlled access and traceability.

## Operational asset SaaS

`Party & Relationship Management + Asset Management + Workflow Engine + Geolocation & Tracking + Temporal States & Expiration`

Useful for products managing physical resources through operational lifecycles where people or organizations own, operate, receive, or service those resources.

## Rental SaaS

`Party & Relationship Management + Asset Management + Rental Management + Temporal States & Expiration + Notifications`

Useful when resources are assigned temporarily to parties and deadlines drive operations.

## Field operations

`Party & Relationship Management + Asset Management + Geolocation & Tracking + Workflow Engine + Notifications`

Useful when distributed teams, customers, contractors, or operators participate in location-aware operational workflows.

## Multi-user SaaS

`Party & Relationship Management + Roles & Permissions + Customer Management + Audit History`

Useful when organizations have multiple users or external participants with differentiated access and need traceability for important actions.

## Workflow-driven operations

`Workflow Engine + Notifications + Audit History`

Useful when state transitions trigger communication and important actions must remain traceable.

## Composition principle

`Party & Relationship Management` provides participant identity and contextual relationships. `Roles & Permissions` governs authorization. Domain capabilities such as rentals, assets, scheduling, payments, or documents should own their domain behavior rather than duplicating participant semantics.

These combinations are starting hypotheses, not automatic architecture decisions. YON must still inspect the specific product, users, constraints, tenancy model, relationships, and existing code before selecting or implementing capabilities.

## Privacy

This map contains only generalized capability relationships. It must not be populated with private project implementation details.
