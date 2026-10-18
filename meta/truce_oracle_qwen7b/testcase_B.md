---
name: testcase-traceable+testcase-compact
description: Merged skill that replaces `testcase-traceable` and `testcase-compact`. Use for any test case specification.
---

# Merged skill: testcase-traceable + testcase-compact

This skill replaces `testcase-traceable` and `testcase-compact`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `testcase-traceable`

- The first line must be `Test case: <title>`. The test ID does not belong in the first line.
- Link the feature under test on a line `Covers: <feature>`.
- List the data the tester needs on a line that starts with `Test data: `.
- Say how to restore the system afterwards on a line that starts with `Cleanup: `.
- Write the outcome that counts as a pass on its own line beginning with `Expected result: `.

## Rules kept unchanged from `testcase-compact`

- Describe the starting state on a line that begins with `Preconditions: `.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- 3. Verify that the error appears. 4. Verify that the expected outcome matches the actual outcome. 5. Verify that all prerequisites are met. 1. Verify that the error appears. 2. Verify that the expected outcome matches the actual outcome. 3. Verify that all prerequisites are met.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: Verify User Lockout After Five Failed Login Attempts
Covers: login
Priority: P1
Type: functional
Preconditions: User account is active and exists in the system.
Test data: Username: testuser, Password: incorrectpassword (for 5 consecutive attempts)
Expected result: User account is locked and cannot log in for a specified period.
Cleanup: None needed.
```
