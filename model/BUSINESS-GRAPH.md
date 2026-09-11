# YON Business Graph — Reference

## 1. Purpose

The Business Graph is a reasoning layer that helps YON understand **who, what, where, and how things are connected in a product context**.

It is a contextual projection of the Universal Product Model, not a requirement to use a graph database, graph API, or graph-shaped persistence model.

The graph exists when relationship context materially improves product decisions, workflows, permissions, automation, or agent behavior.

## 2. Core idea

YON should not reason only from isolated records.

A useful context can be expressed as:

`PARTY ↔ RELATIONSHIP ↔ ROLE ↔ CONTEXT ↔ RESOURCE ↔ WORKFLOW ↔ EVENT`

The graph makes meaningful connections explicit enough to answer questions such as:

- Who is responsible for this resource?
- Which customer is connected to this order?
- Which organization does this participant act for?
- Which workflow currently owns this case?
- Which events changed this resource's state?
- Which relationships permit an action?
- Which context should an agent use before acting?

## 3. Node types

Nodes are conceptual references to things already meaningful to the product.

Typical node types include:

- Party
- Organization
- Role
- Resource
- Workflow
- Transaction
- Document
- Event
- Context / Tenant
- External System

Do not create graph nodes merely because a database table exists.

## 4. Relationship types

Relationships describe meaningful connections.

Examples:

- owns
- belongs_to
- employs
- serves
- supplies
- purchases_from
- assigned_to
- responsible_for
- participates_in
- located_at
- depends_on
- follows
- caused
- authorized_by
- related_to

Relationship names must express product meaning. Generic technical links such as `foreign_key_to` are not useful graph semantics.

## 5. Relationship metadata

A relationship may need contextual metadata such as:

- effective_from
- effective_until
- status
- source
- confidence
- organization / tenant boundary
- permissions
- provenance
- created_by
- last_verified

Temporal and authorization semantics must be modeled when they materially affect decisions.

## 6. Context and boundaries

Graph reasoning must preserve boundaries.

YON must distinguish:

- identity from role;
- relationship from authorization;
- organization context from global identity;
- accessible context from merely related context;
- current relationships from historical relationships.

A graph must never become a mechanism for bypassing tenancy, permissions, or privacy controls.

## 7. Provenance and confidence

Graph facts should be distinguishable by evidence.

Useful confidence states include:

`ASSUMED → SIGNALLED → SUPPORTED → STRONG`

The graph must preserve where a meaningful relationship came from when that matters to decision quality.

Unverified inference must not silently become authoritative business truth.

## 8. Temporal graph reasoning

Relationships and nodes can change over time.

YON should be able to distinguish:

- currently valid relationship;
- future relationship;
- expired relationship;
- historical relationship;
- unknown validity.

Example:

`EMPLOYEE —works_for→ COMPANY`

may be valid for one period and invalid after employment ends.

Temporal validity should reuse YON's temporal reasoning rather than inventing duplicate lifecycle concepts.

## 9. Graph + events

Events provide evidence of change; the graph provides contextual relationships.

A useful reasoning sequence is:

`EVENT → UPDATE CONTEXT → RE-EVALUATE RELATIONSHIPS → DECIDE NEXT ACTION`

Example:

`invoice overdue → customer relationship → account owner → collections workflow → allowed communication`

The event does not automatically authorize the resulting action. Permissions, policies, and workflow rules still apply.

## 10. Graph + agents

Agents should query contextual relationships instead of receiving arbitrary collections of records.

Before an agent acts, YON should establish, where relevant:

1. who is acting;
2. for which organization/context;
3. what resource or workflow is affected;
4. which relationships matter;
5. what permissions apply;
6. what recent events changed the situation;
7. what uncertainty remains;
8. whether approval is required.

This creates context-aware bounded autonomy rather than unrestricted data access.

## 11. When to use it

Use Business Graph reasoning when relationships materially affect:

- workflow routing;
- responsibility or ownership;
- permissions;
- customer or participant context;
- cross-module coordination;
- event reactions;
- agent decisions;
- recommendations or matching;
- historical context.

Do not introduce graph reasoning for a simple isolated CRUD workflow where relationships add no useful decision context.

## 12. Implementation neutrality

This reference does not prescribe:

- graph databases;
- relational schemas;
- ORM models;
- APIs;
- event brokers;
- vector stores;
- specific frameworks;
- infrastructure vendors.

A relational implementation can represent graph semantics perfectly well when that is the appropriate product choice.

## 13. Verification

Verify graph reasoning at the level of user outcomes:

- correct relationship context is surfaced;
- expired relationships are not treated as current;
- unauthorized relationships do not grant access;
- cross-tenant context is isolated;
- event-driven changes update relevant context;
- agents receive only the context they are permitted to use;
- inferred facts are not presented as verified facts.

## 14. Privacy

The public YON model must contain no private customer graph, identifying business relationships, secrets, proprietary architecture, or private implementation details.

Private graph data remains inside the product that owns it.
