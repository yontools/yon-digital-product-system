# /yon-validate

Validate a YON-assisted change or product state using the YON validation gates.

## Instructions

1. Inspect project instructions and the affected scope.
2. Read `validation/README.md` and `validation/INDEX.md`.
3. Determine which gates apply based on user impact and risk.
4. Run the strongest available checks: tests, build/type checks, browser/runtime checks, responsive inspection, accessibility checks, and security/authorization checks when relevant.
5. Exercise the affected user journey in the running product whenever possible.
6. Record each result as `PASS`, `FAIL`, `BLOCKED`, or `NOT_APPLICABLE`.
7. Treat `BLOCKED` as unresolved verification.
8. Fix failures when authorized and rerun the affected checks.
9. Report remaining risks and evidence instead of claiming completion from compilation alone.

## Output

- Scope validated
- Gate results
- Evidence observed
- Failures and severity
- Blocked checks and reason
- Regressions found
- Remaining risks
- Final disposition: `PASS`, `FAIL`, or `BLOCKED`
