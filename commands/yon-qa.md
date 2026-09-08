# /yon-qa

## Purpose
Verify a digital product or a recent change from the user's perspective and from the running application.

## Instructions

Run the affected application when possible and inspect the real browser experience.

Check:
- routes and navigation;
- critical user journeys;
- forms and validation;
- loading states;
- empty states;
- success states;
- error states;
- permissions and protected actions;
- responsive layouts;
- keyboard accessibility and obvious accessibility issues;
- console/runtime errors;
- critical destructive actions;
- edge cases;
- visual regressions.

Do not report a change as verified merely because it compiles or tests pass.

## Output

For each issue report:

- severity;
- affected flow/screen;
- observed behavior;
- expected behavior;
- reproduction steps;
- recommended fix.

Finish with a clear PASS, PASS WITH RISKS, or FAIL assessment.
