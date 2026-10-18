---
name: testcase-compact+testcase-traceable
description: Merged skill that replaces `testcase-compact` and `testcase-traceable`. Use for any test case specification.
---

# Merged skill: testcase-compact + testcase-traceable

This skill replaces `testcase-compact` and `testcase-traceable`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `testcase-compact`

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- State the pass criterion on a line that starts with `Expected result: `.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.

## Rules kept unchanged from `testcase-traceable`

- The first line must be `Test case: <title>`. The test ID does not belong in the first line.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`. Link the feature under test on a line `Covers: <feature>`.
- Preconditions: Describe the starting state on a line that begins with `Preconditions: `. Test data: List the data the tester needs on a line that starts with `Test data: `.
