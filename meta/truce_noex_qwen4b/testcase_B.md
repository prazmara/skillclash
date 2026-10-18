---
name: testcase-traceable+testcase-compact
description: Merged skill that replaces `testcase-traceable` and `testcase-compact`. Use for any test case specification.
---

# Merged skill: testcase-traceable + testcase-compact

This skill replaces `testcase-traceable` and `testcase-compact`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `testcase-traceable`

- Say how to restore the system afterwards on a line that starts with `Cleanup: `.
- Write the outcome that counts as a pass on its own line beginning with `Expected result: `.
- The first line must be `Test case: <title>`. The test ID does not belong in the first line.

## Rules kept unchanged from `testcase-compact`

- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Link the feature under test on a line `Covers: <feature>`. Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke`, or `Type: negative`.
- Test data: [list the data the tester needs] Preconditions: [describe the starting state]
