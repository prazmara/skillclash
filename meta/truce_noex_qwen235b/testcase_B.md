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

- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, and write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- Preconditions: [Describe the starting state] Test data: [List the data the tester needs]
- On a separate line, write `Covers: <feature>` to link the feature under test. On the next line, write `Type: functional`, `Type: regression`, `Type: smoke`, or `Type: negative` to tag the kind of test.
