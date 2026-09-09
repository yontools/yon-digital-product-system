# Pattern: Confirmation for Risky Actions

**Status:** `experimental`

## Problem
Destructive or difficult-to-reverse actions can cause costly mistakes when triggered accidentally or without enough context.

## Context
Delete, revoke access, cancel, archive, overwrite, disconnect, or other high-impact operations.

## Solution
Before execution, communicate the consequence and target clearly. Require confirmation when the risk justifies it, and prefer reversible alternatives such as undo or archive when appropriate.

## When to use
- The action is destructive, irreversible, expensive, or security-sensitive.
- A mistaken click has meaningful consequences.

## When NOT to use
- Low-risk reversible actions where confirmation only adds friction.
- When undo provides a safer and faster recovery path.

## Variants
- Inline confirmation.
- Confirmation dialog.
- Typed confirmation for exceptional high-risk operations.
- Undo after action.

## Trade-offs
- Confirmation reduces accidental actions but adds friction and can create habituation.
- Use stronger confirmation only as risk increases.

## Accessibility
Dialog focus must be managed correctly, keyboard actions must work, the destructive consequence must be readable, and buttons must have explicit labels.

## Responsive
Dialogs and confirmation surfaces must remain usable on small screens without hiding the consequence or actions below unreachable content.

## Verification
Test accidental activation, keyboard use, cancellation, retry, authorization changes, duplicate submission, and recovery after completion.

## Evidence
Generalized recurring product-design pattern; currently experimental in YON.

## Changelog
- 2026-09-09 — Initial version
