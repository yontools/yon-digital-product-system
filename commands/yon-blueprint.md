# YON Blueprint

Create or refine a Product Blueprint before implementation when a product is broad, multi-role, workflow-heavy, or contains meaningful reusable capability composition.

## Run

1. Understand the intended outcome, success criteria, users, participants, relationships, jobs, workflows, constraints, existing behavior, and project-local instructions.
2. If the request describes a real-world business operation, inspect Business Discovery first and identify only archetypes supported by observed behavioral signals. Treat archetypes as contextual hypotheses, not feature lists or templates.
3. Use the Universal Product Model when it materially clarifies participants, relationships, resources, actions, events, states, temporal rules, workflows, transactions, communications, documents, or boundaries. Do not over-model.
4. Run capability discovery when reusable behavior is uncertain or broad; search by behavior/workflow rather than industry category.
5. Resolve the minimum justified capability composition and preserve classification, maturity, evidence, coverage, and gap decisions.
6. Check relevant patterns and evidence; do not add patterns without a demonstrated interaction problem.
7. Create or update a Blueprint using `blueprints/BLUEPRINT-TEMPLATE.md`.
8. Preserve traceability where useful:
   `BUSINESS OUTCOME → WORKFLOW → ARCHETYPE → PRODUCT PRIMITIVES → CAPABILITY / PATTERN → DECISION → VERIFICATION`
9. Separate reusable capabilities from product-specific business behavior and domain rules.
10. Record genuine gaps, assumptions, unresolved questions, dependencies, and what evidence is still required.
11. Identify high-risk boundaries and proportional verification gates.
12. Define implementation order by dependency, user value, risk, and verifiability.
13. Do not implement merely because a Blueprint exists; pass the approved Blueprint into the build step.

## Output

Return the completed Blueprint or a concise decision summary containing:

- outcome and success criteria;
- business archetypes/confidence when applicable;
- participants, roles, relationships, and boundaries;
- critical workflows and states;
- conceptual product model where useful;
- capability and pattern resolution with evidence/maturity;
- minimal composition and ownership boundaries;
- product-specific requirements;
- gaps, assumptions, dependencies, and unresolved questions;
- risks and verification gates;
- implementation order;
- decision log and privacy check.

## Decision discipline

- `DIRECT`, `SUPPORTING`, `OPTIONAL`, `MISSING`, and `PRODUCT-SPECIFIC` are the only capability classifications.
- A `MISSING` behavior becomes `YON-CANDIDATE`, `PRODUCT-SPECIFIC`, or `NEEDS-EVIDENCE`; never force a match.
- `BLOCKED` verification is not `PASS`.
- Existing working behavior should not be redesigned without an outcome-based reason.
- A Blueprint is a decision contract, not automatic architecture, schema, or code generation instructions.

Do not publish reusable knowledge automatically. Respect the project privacy boundary.
