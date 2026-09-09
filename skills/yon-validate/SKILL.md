---
name: yon-validate
description: Validate YON repository integrity and YON-assisted product changes across structural, product, UX/UI, runtime, accessibility, security, and regression gates.
---

# YON Validate

Use this skill to determine whether a YON repository or YON-assisted product change is actually verified.

## Core rule

`BUILD PASSING` is not the same as `PRODUCT VERIFIED`.

Validation must be proportional to risk and based on observed evidence.

## When validating the YON repository

1. Run `python scripts/validate_yon.py`.
2. Confirm required plugin files and metadata exist.
3. Confirm skill directories contain valid `SKILL.md` files with matching names.
4. Confirm commands and agents have required frontmatter.
5. Confirm repository-relative Markdown references resolve.
6. Confirm capability and pattern indexes do not contain broken local links.
7. Treat any structural validator failure as `FAIL`.

## When validating a product change

1. Inspect project instructions and affected scope.
2. Read `validation/README.md` and `validation/INDEX.md`.
3. Select applicable gates: Structure, Product Journey, UX, UI, Accessibility, Runtime, Security, Regression.
4. Exercise the affected journey whenever possible.
5. Run the strongest available automated checks.
6. Inspect responsive and critical UI states when UI is affected.
7. Check auth, authorization, tenant isolation, secrets, destructive operations, billing, and data boundaries when relevant.
8. Record every gate as `PASS`, `FAIL`, `BLOCKED`, or `NOT_APPLICABLE`.
9. Never convert `BLOCKED` into `PASS` because another check succeeded.
10. Fix failures only when authorized, then rerun affected checks.

## Evidence standard

A validation result should state:

- check performed
- expected behavior
- observed behavior
- evidence or artifact
- severity if failed
- remaining uncertainty

## Final disposition

- `PASS`: applicable gates passed and no unresolved critical verification remains.
- `FAIL`: one or more applicable gates failed.
- `BLOCKED`: required verification could not be completed.

Compilation, linting, or a successful deployment alone cannot establish `PASS`.
