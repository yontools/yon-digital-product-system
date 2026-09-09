---
description: Validate a YON-assisted change or the YON repository itself using structural, product, UX/UI, runtime, safety, and regression gates.
---

# /yon-validate

Validate a YON-assisted change or product state using the YON validation gates.

## Instructions

1. Inspect project instructions and the affected scope.
2. Read `validation/README.md` and `validation/INDEX.md`.
3. If the target repository is YON itself, run `python scripts/validate_yon.py` first and treat any failure as a structural failure.
4. Determine which gates apply based on user impact and risk.
5. Run the strongest available checks: tests, build/type checks, browser/runtime checks, responsive inspection, accessibility checks, and security/authorization checks when relevant.
6. Exercise the affected user journey in the running product whenever possible.
7. Record each result as `PASS`, `FAIL`, `BLOCKED`, or `NOT_APPLICABLE`.
8. Treat `BLOCKED` as unresolved verification.
9. Fix failures when authorized and rerun the affected checks.
10. Report remaining risks and evidence instead of claiming completion from compilation alone.

## YON repository integrity

When validating this repository, the structural validator checks required files, plugin metadata, skill/command/agent frontmatter, local markdown references, and knowledge-index links. CI runs the same validator on pushes and pull requests.

## Output

- Scope validated
- Gate results
- Evidence observed
- Failures and severity
- Blocked checks and reason
- Regressions found
- Remaining risks
- Final disposition: `PASS`, `FAIL`, or `BLOCKED`
