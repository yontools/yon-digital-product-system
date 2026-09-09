# YON Universal Product Model — Reference

## 1. Why this layer exists

Products from very different domains often share structural realities: people and organizations participate, relationships define context, resources move through states, actions cause changes, events record what happened, workflows coordinate work, and permissions define boundaries.

YON needs to recognize those structures without turning them into one rigid implementation model.

The Universal Product Model is therefore a **reasoning layer**, not a technical layer.

## 2. Primitive reference

### Party

A person or organization that participates in a product context.

A Party can participate in multiple contexts and can have different relationships and roles in each one.

Typical examples: customer, patient, professional, employee, supplier, owner, company, clinic, team.

Do not encode every role into the identity itself.

### Relationship

A meaningful connection between participants or between a participant and another product context.

Relationships explain context such as membership, ownership, employment, customer-provider, patient-clinic, seller-buyer, supplier-business, or participant-event.

A relationship can have its own lifecycle or metadata when the product needs it.

### Role

A contextual responsibility or position held by a Party.

A role is not identity and is not authorization. A role can help describe what someone does; permissions determine what the system allows them to do.

### Resource

A thing the product manages, references, allocates, schedules, transforms, tracks, or acts upon.

Resources can be physical, digital, informational, or abstract. The term is intentionally broader than "asset".

### Action

An intentional operation performed by a participant or by the system.

Examples include create, assign, book, approve, move, cancel, pay, notify, complete, or request.

An action may be allowed or denied by permissions and may cause state changes or events.

### Event

A record that something happened.

Events can originate from user actions, system processes, integrations, scheduled rules, or external signals. An event may trigger workflows, notifications, audit records, or state transitions.

Do not confuse an event with an action: the action expresses intent; the event records an occurrence.

### State

A meaningful condition in a lifecycle.

States should represent distinctions that matter to users, operators, business rules, or system behavior. Avoid creating states only because an implementation happens to need another boolean or technical flag.

### Time / Temporal Rule

A time-related condition that materially affects behavior.

It can represent a deadline, duration, schedule, recurrence, validity window, cooldown, appointment time, expiration, or relative rule.

Temporal rules become especially important when a product must proactively change state or communicate because time has passed.

### Workflow

A coordinated sequence of actions, states, decisions, events, and handoffs that produces a meaningful outcome.

A workflow can be linear or branching. It may involve humans, automation, external systems, or combinations of them.

Model the user's actual work rather than inventing workflow stages that have no operational meaning.

### Transaction

A meaningful exchange, commitment, or business operation between participants or contexts.

It can include financial and non-financial transactions: payment, purchase, booking, rental, reservation, transfer, order, or another domain commitment.

Do not assume all transactions require a payment system.

### Communication

A message or interaction used to inform, request, confirm, remind, coordinate, or obtain a response.

Communication may be user-to-user, system-to-user, system-to-system, or external-channel based.

### Document

Structured or unstructured information with a product or business purpose.

Examples can include invoices, prescriptions, contracts, reports, certificates, attachments, forms, or generated records.

Do not make document storage a requirement merely because a product has text or files.

### Permission / Boundary

A rule defining who may access, see, change, execute, approve, or otherwise interact with something within a context.

Boundaries can include tenant isolation, ownership, organization membership, role-based access, resource-level access, or other domain constraints.

Permissions are distinct from roles, relationships, and authentication.

## 3. How primitives compose

The primitives are intentionally composable rather than hierarchical.

A common sequence is:

`PARTY → RELATIONSHIP / ROLE → ACTION → EVENT → STATE CHANGE → WORKFLOW / COMMUNICATION`

A resource can participate in that sequence:

`PARTY → ACTION → RESOURCE → STATE → EVENT`

Time can constrain any relevant transition:

`STATE + TEMPORAL RULE → EVENT / ACTION / COMMUNICATION`

Permission boundaries can constrain actions and access throughout the model:

`PARTY + RELATIONSHIP + ROLE + BOUNDARY → ALLOWED ACTION`

These sequences are reasoning examples, not prescribed runtime architectures.

## 4. Universal model to capability mapping

| Primitive / combination | Typical need | Existing YON destination | Default treatment |
|---|---|---|---|
| Party + Relationship + Role | represent participants and context | Party & Relationship Management | Reuse when workflow requires it |
| Resource + State | manage something through a lifecycle | Asset Management or domain capability | Resolve by behavior, not noun |
| State + Time Rule | expiration/deadline behavior | Temporal States & Expiration | Reuse when time changes outcome |
| Event + Communication | notify after meaningful occurrence | Notification Orchestration | Reuse when communication is required |
| Action + Workflow | coordinate multi-step work | Workflow Engine | Reuse when work spans meaningful stages |
| Role + Boundary | control access/operations | Roles & Permissions | Reuse when authorization is material |
| Event + historical record | preserve meaningful changes | Audit History | Reuse when traceability matters |
| Resource + location | know where something is or was | Geolocation & Tracking | Reuse when location affects work |
| Resource + rental transaction | temporary allocation/use | Rental Management | Reuse when rental semantics actually apply |
| Transaction + payment | money movement or payment state | Payment-related capability when available | Do not invent a universal payment model |
| Document + workflow | documents required in a process | Documents or product-specific behavior | Resolve from actual workflow |

The table is a reasoning map. It does not mean that every row must become a capability or that every combination must be implemented.

## 5. Modeling a product

For a broad product, answer these questions before implementation:

1. **Who participates?** Identify Parties.
2. **How are they connected?** Identify meaningful Relationships.
3. **What context do they act in?** Identify Roles and Boundaries.
4. **What matters to the product?** Identify Resources and other domain entities.
5. **What are the important actions?** Identify meaningful operations.
6. **What happens as a result?** Identify Events and State changes.
7. **What work must be coordinated?** Identify Workflows and handoffs.
8. **What depends on time?** Identify Temporal Rules.
9. **What must be exchanged or committed?** Identify Transactions where applicable.
10. **What must be communicated or retained?** Identify Communications and Documents where applicable.
11. **Which reusable YON capabilities cover these behaviors?** Run discovery and resolution.
12. **Which concepts are genuinely product-specific?** Keep them local.

## 6. Don't over-model

A product model is useful only when it improves decisions.

Do not:

- create a Party abstraction for a single anonymous interaction where identity is irrelevant;
- create a workflow for a simple action that needs no coordination;
- create an event system because events sound architecturally sophisticated;
- create states that users and business rules cannot distinguish;
- turn every noun into a reusable capability;
- introduce graph/database infrastructure because relationships exist conceptually;
- force a transaction model onto non-transactional behavior;
- infer a universal domain model from one product.

## 7. Product-specific semantics

Universal primitives intentionally stop before domain meaning becomes specialized.

For example, "Resource" can help YON recognize that something is being managed, but whether that resource is a medical room, a dumpster, a barber chair, a vehicle, a document, or a digital license is product-specific.

Likewise, a "Relationship" can be universal while the precise semantics of patient-doctor, tenant-landlord, seller-buyer, or employee-employer remain domain-specific.

When a concept repeatedly appears across independent products with stable semantics and sufficient evidence, it may become a candidate for extraction through YON's evidence → extraction → review process.

## 8. Tenancy and boundaries

For multi-organization products, tenancy is a context/boundary concern rather than a universal database prescription.

YON should ask:

- Which Party or organization owns the context?
- Which Parties can access it?
- Which Relationships grant contextual access?
- Which Roles affect allowed actions?
- Which Resources are isolated by tenant/context?
- Which Events or Documents cross boundaries?

The answers inform architecture and authorization but do not dictate a specific implementation.

## 9. Verification implications

The model should improve what YON verifies.

Examples:

- Party/Relationship: verify the right participant sees the right context.
- Role/Boundary: verify allowed and denied actions.
- Resource/State: verify lifecycle transitions and invalid transitions.
- Temporal Rule: verify boundary conditions around deadlines and expiration.
- Workflow: exercise the complete critical journey and failure/recovery paths.
- Event/Communication: verify triggers, delivery behavior, and failure handling where applicable.
- Transaction: verify state consistency and important failure paths.

The validation result remains `PASS`, `FAIL`, `BLOCKED`, or `NOT_APPLICABLE`; a blocked verification is never treated as passing.

## 10. Maturity

The Universal Product Model itself is a conceptual vocabulary. Its primitives do not have the same lifecycle as reusable capabilities and patterns.

A mapping from a primitive to a capability can be experimental or proven independently of the primitive's conceptual usefulness.

This distinction prevents YON from treating a useful abstraction as proof that an implementation pattern is universally correct.

## 11. Privacy boundary

The model must remain generic and public-safe.

Never place private code, secrets, customer data, proprietary prompts, confidential architecture, identifying business rules, or other private implementation details into this reference.
