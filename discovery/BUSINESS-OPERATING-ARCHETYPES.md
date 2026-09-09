# Business Operating Archetypes

Business Operating Archetypes are reusable descriptions of **how work happens** inside a business. They help YON discover the real operating model without creating rigid vertical templates.

## Archetype contract

For each archetype, YON should evaluate:

- **Behavior:** what operation repeats;
- **Signals:** evidence that the archetype is present;
- **Participants:** who performs or receives the work;
- **Resources:** what moves through or is affected by the operation;
- **Lifecycle:** relevant states and transitions;
- **Time:** deadlines, availability, recurrence, windows, or expiration;
- **Typical capabilities:** reusable product behaviors that may support it;
- **Questions:** what must be learned before implementation;
- **Anti-pattern:** what YON must not assume.

An archetype is a hypothesis until the actual workflow supports it.

---

## 1. Service Delivery

**Behavior:** A business delivers a service to a customer or another participant, usually through one or more operational steps.

**Signals:** a service is requested, prepared, assigned, delivered, completed, or reviewed.

**Participants:** customer/client, service provider, operator, assigned professional/team.

**Resources:** service request, service instance, people, equipment, location, documents.

**Lifecycle:** requested → accepted → scheduled/prepared → in progress → completed → cancelled/failed when relevant.

**Time:** appointment windows, service duration, deadlines, availability.

**Typical capabilities:** Party & Relationship Management, Workflow Engine, Customer Management, Scheduling when justified, Notifications, Audit History.

**Questions:** What exactly constitutes delivery? Who performs it? What can interrupt it? What proves completion?

**Anti-pattern:** assuming every service business needs the same agenda, staff, or workflow.

---

## 2. Appointment & Scheduling

**Behavior:** Work is planned around time slots, availability, duration, capacity, or assigned participants.

**Signals:** calendar, booking, rescheduling, cancellation, availability, no-show, time slot, capacity.

**Participants:** requester, provider, staff, resource owner.

**Resources:** slot, appointment, provider, location, equipment.

**Lifecycle:** requested → held/booked → confirmed → completed/cancelled/no-show.

**Time:** availability windows, duration, buffers, recurring schedules, deadlines.

**Typical capabilities:** scheduling/availability behavior, Party & Relationship Management, Notifications, Workflow Engine.

**Questions:** Is time the scarce resource? Can multiple resources be required? Who can book or override availability?

**Anti-pattern:** adding a calendar because the business "looks like" a service business.

---

## 3. Request → Order → Execution

**Behavior:** A request becomes an accepted order/work instruction and is then executed.

**Signals:** quote/request, acceptance, order, preparation, dispatch, execution, completion.

**Participants:** requester/customer, operator, fulfiller, supplier when applicable.

**Resources:** request, order, work item, goods/services, instructions.

**Lifecycle:** requested → reviewed/quoted → accepted → prepared → executing → completed/cancelled.

**Time:** promised dates, SLA/deadlines, execution windows.

**Typical capabilities:** Workflow Engine, Customer Management, Notifications, Audit History, Payments/Documents when justified.

**Questions:** When does a request become binding? What approvals or commercial events occur between request and execution?

**Anti-pattern:** treating every form submission as an order.

---

## 4. Reservation & Allocation

**Behavior:** A scarce resource is reserved or allocated to a participant for a period or purpose.

**Signals:** availability, hold, booking, allocation, release, conflict, capacity.

**Participants:** requester, resource owner, operator.

**Resources:** room, seat, machine, vehicle, staff capacity, inventory, slot, facility.

**Lifecycle:** available → held → reserved → in use → released; conflict/cancelled when relevant.

**Time:** reservation window, hold expiration, usage period.

**Typical capabilities:** Resource/Asset Management, temporal states, scheduling, notifications, roles/permissions.

**Questions:** What is scarce? Can it be shared? What happens when two requests compete?

**Anti-pattern:** confusing a reservation with an appointment; determine whether the scarce object is a person, time slot, physical resource, or capacity.

---

## 5. Rental & Temporary Use

**Behavior:** A resource is provided for temporary use and must eventually be returned, released, renewed, or recovered.

**Signals:** pickup/delivery, start/end date, rental period, extension, return, overdue, condition.

**Participants:** owner/provider, renter/customer, operator, field staff.

**Resources:** rentable asset, rental agreement, location, condition record.

**Lifecycle:** available → reserved → deployed/in use → due → returned/extended → available/maintenance.

**Time:** rental start/end, expiration, grace period, overdue thresholds.

**Typical capabilities:** Asset Management, Rental Management, Temporal States & Expiration, Geolocation & Tracking, Notifications, Audit History.

**Questions:** Is the object physically tracked? What happens at expiration? Who is responsible while it is in use?

**Anti-pattern:** assuming every temporary allocation is a rental; confirm commercial and operational semantics.

---

## 6. Asset & Field Operations

**Behavior:** Physical assets or field work are managed across locations, states, assignments, and operational events.

**Signals:** dispatch, GPS/location, field visit, assignment, movement, condition, maintenance, proof of work.

**Participants:** operator, field worker, customer, asset owner.

**Resources:** vehicles, equipment, containers, sites, work orders.

**Lifecycle:** available → assigned → deployed → active → completed/returned/maintenance.

**Time:** field windows, SLAs, expiration, maintenance intervals.

**Typical capabilities:** Asset Management, Geolocation & Tracking, Workflow Engine, Temporal States & Expiration, Notifications, Audit History.

**Questions:** Does location materially affect decisions? Which events need proof? What is the unit of field work?

**Anti-pattern:** adding maps simply because the business has physical assets.

---

## 7. Recurring Service & Renewal

**Behavior:** A service, commitment, contract, or entitlement repeats or renews over time.

**Signals:** recurring schedule, renewal date, cycle, installment, expiration, auto-renewal, reactivation.

**Participants:** customer/member, provider, operator, account owner.

**Resources:** subscription/service agreement, entitlement, recurring task.

**Lifecycle:** active → due/renewal → renewed/paused/expired/cancelled.

**Time:** recurring intervals, renewal windows, grace periods.

**Typical capabilities:** Temporal States & Expiration, Workflow Engine, Notifications, Payments when relevant, Party & Relationship Management.

**Questions:** What repeats: payment, service, entitlement, or workflow? Can recurrence be modified?

**Anti-pattern:** assuming recurrence means subscription billing.

---

## 8. Commerce & Fulfillment

**Behavior:** Goods or sellable items are selected, purchased, prepared, delivered, collected, or fulfilled.

**Signals:** catalog, cart/order, payment, picking, packing, dispatch, delivery, return.

**Participants:** buyer, seller, operator, fulfillment staff, delivery participant.

**Resources:** product/item, order, inventory, shipment, payment, return.

**Lifecycle:** selected → ordered → paid/authorized → prepared → fulfilled → delivered/returned.

**Time:** promised fulfillment, delivery windows, reservation/stock holds.

**Typical capabilities:** Workflow Engine, Asset/Inventory behavior when justified, Payments, Notifications, Documents, Party & Relationship Management.

**Questions:** Is inventory actually scarce? Where does fulfillment happen? What constitutes delivery?

**Anti-pattern:** treating a service booking as commerce without identifying a real order/fulfillment lifecycle.

---

## 9. Case / Ticket / Work Management

**Behavior:** A problem, request, incident, or internal work item is tracked until resolution.

**Signals:** ticket, case, issue, escalation, queue, assignment, status, SLA, resolution.

**Participants:** requester, assignee, team, supervisor, customer.

**Resources:** case/ticket, attachments, messages, tasks, related assets.

**Lifecycle:** opened → triaged → assigned → in progress → waiting → resolved → closed/reopened.

**Time:** SLA, escalation, waiting period, response deadline.

**Typical capabilities:** Workflow Engine, Notifications, Roles & Permissions, Audit History, Documents/Communication.

**Questions:** What qualifies as resolution? Which states require human action? What is the escalation policy?

**Anti-pattern:** building a generic ticketing system when the business actually has a simpler workflow.

---

## 10. Membership & Subscription

**Behavior:** A participant receives ongoing access, benefits, service entitlement, or participation rights under a membership/plan.

**Signals:** plans, enrollment, entitlement, renewal, pause, cancellation, access rules.

**Participants:** member/customer, organization/provider, staff.

**Resources:** membership, plan, entitlement, access credential.

**Lifecycle:** prospect → active → paused/expired/cancelled.

**Time:** billing/renewal cycles, entitlement periods, grace periods.

**Typical capabilities:** Party & Relationship Management, Roles & Permissions, Temporal States & Expiration, Payments, Notifications.

**Questions:** What does membership grant? Is payment the same thing as entitlement? Can access differ by role?

**Anti-pattern:** assuming subscription = recurring payment only.

---

## 11. Marketplace & Matching

**Behavior:** Participants with supply/capacity are matched with participants expressing demand/need.

**Signals:** profiles, listings, requests, availability, matching, offers, acceptance, reputation.

**Participants:** buyer/requester, provider/seller, marketplace operator.

**Resources:** listing, request, offer, match, transaction.

**Lifecycle:** published/requested → matched → accepted → fulfilled → reviewed/disputed.

**Time:** availability windows, offer expiration, response deadlines.

**Typical capabilities:** Party & Relationship Management, Workflow Engine, Communication, Roles & Permissions, Payments when applicable.

**Questions:** Who controls the match? Is matching manual, rules-based, or algorithmic? What happens after a match?

**Anti-pattern:** calling any directory a marketplace.

---

## 12. Approval & Authorization

**Behavior:** An action or state transition requires explicit permission or review before proceeding.

**Signals:** submit, review, approve, reject, escalate, authorize, sign-off.

**Participants:** requester, reviewer/approver, owner, administrator.

**Resources:** request, transaction, document, change, access decision.

**Lifecycle:** draft → submitted → under review → approved/rejected → executed.

**Time:** approval deadlines, escalation, expiration.

**Typical capabilities:** Roles & Permissions, Workflow Engine, Audit History, Notifications, Documents when relevant.

**Questions:** What is being approved? Who may approve? Can approval be delegated or revoked?

**Anti-pattern:** equating authentication with business approval.

---

## 13. Intake → Assessment → Decision → Follow-up

**Behavior:** Information is collected, assessed, a decision is made, and subsequent work follows from that decision.

**Signals:** intake form, triage, assessment, score, diagnosis/evaluation, recommendation, follow-up.

**Participants:** requester/client/patient/applicant, assessor/professional, decision maker.

**Resources:** intake, assessment, evidence, decision, follow-up plan.

**Lifecycle:** initiated → collected → assessed → decided → follow-up → closed/reassessed.

**Time:** appointments, deadlines, follow-up intervals, reassessment windows.

**Typical capabilities:** Party & Relationship Management, Workflow Engine, Documents, Communication, Scheduling, Audit History.

**Questions:** What evidence informs the decision? Which parts are confidential? What action follows the decision?

**Anti-pattern:** assuming a form is the product; the important behavior may be the decision and follow-up workflow.

---

## 14. Document & Compliance Lifecycle

**Behavior:** Documents or compliance records are created, reviewed, approved, signed, renewed, or archived.

**Signals:** required document, version, review, signature, expiration, audit, renewal, compliance status.

**Participants:** subject, uploader, reviewer, approver, auditor.

**Resources:** document, version, requirement, evidence, compliance record.

**Lifecycle:** required → submitted → reviewed → approved/rejected → active → expired/renewed/archived.

**Time:** expiration dates, review cycles, retention periods.

**Typical capabilities:** Documents, Roles & Permissions, Temporal States & Expiration, Audit History, Notifications, Workflow Engine.

**Questions:** Which document is authoritative? Who can view it? What makes compliance valid?

**Anti-pattern:** storing files without modeling the business state that depends on them.

---

## 15. Event / Session Operations

**Behavior:** A defined event or session has participants, capacity, preparation, execution, and post-event activity.

**Signals:** event/session, registration, capacity, check-in, attendance, schedule, cancellation.

**Participants:** organizer, attendee, staff, facilitator, resource owner.

**Resources:** event/session, venue, capacity, materials, attendee record.

**Lifecycle:** planned → open → registered → active → completed → follow-up/cancelled.

**Time:** event date/time, registration window, duration, capacity windows.

**Typical capabilities:** Scheduling, Reservation & Allocation behavior, Party & Relationship Management, Notifications, Workflow Engine, Documents when relevant.

**Questions:** Is the event one-off or recurring? Is capacity the scarce resource? What happens before and after attendance?

**Anti-pattern:** assuming an event requires a full ticketing platform.

---

# Combining archetypes

Real businesses commonly combine archetypes. YON should model the **minimum combination that explains the observed operation**.

Examples:

- A service business may combine `Service Delivery + Appointment & Scheduling`.
- A field rental business may combine `Rental & Temporary Use + Asset & Field Operations + Temporal Rules`.
- A repair operation may combine `Request → Order → Execution + Case / Ticket / Work Management`.
- A membership business may combine `Membership & Subscription + Recurring Service & Renewal`.
- A marketplace may combine `Marketplace & Matching + Approval & Authorization + Commerce & Fulfillment`.

These are examples, not default architectures.

# Confidence

Every detected archetype should carry a confidence level:

- **HIGH** — directly observed or explicitly required by the workflow.
- **MEDIUM** — strongly suggested but needs confirmation.
- **LOW** — plausible hypothesis only.

Low-confidence archetypes must not silently become implementation requirements.

# Archetype evolution

The archetype library itself should evolve cautiously. A new archetype should normally require:

1. evidence of the recurring behavior;
2. evidence that existing archetypes cannot describe it adequately;
3. usefulness across more than one product/problem context;
4. a documented boundary and anti-pattern;
5. review before inclusion.

The goal is not to classify every business. The goal is to help YON discover the smallest accurate operating model that leads to better product decisions.
