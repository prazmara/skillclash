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

- 1. Verify that the error appears. 2. Verify that the error message contains the expected text. 3. Verify that the error message is displayed in the correct location. 4. Verify that the error message is displayed in the correct format. 5. Verify that the error message is displayed in the correct color. 1. Verify that the error appears. 2. Verify that the error message contains the expected text. 3. Verify that the error message is displayed in the correct location. 4. Verify that the error message is displayed in the correct format. 5. Verify that the error message is displayed in the correct color.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: Verify that a user is locked out after five failed login attempts.
Test ID: TC-0412
Covers: login
Test data: User credentials with incorrect password
Cleanup: Reset the user's account to allow login
Preconditions: User account exists
Type: functional
Expected result: User is locked out after five failed login attempts
Expected error message: "Account locked due to too many failed login attempts"
Expected error location: Login screen
Expected error format: Error message displayed in red color
Expected error text: "Account locked due to too many failed login attempts"
```
