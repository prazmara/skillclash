---
name: testcase-traceable+testcase-compact
description: Merged skill that replaces `testcase-traceable` and `testcase-compact`. Use for any test case specification.
---

# Merged skill: testcase-traceable + testcase-compact

This skill replaces `testcase-traceable` and `testcase-compact`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `testcase-traceable`

- Say how to restore the system afterwards on a line that starts with `Cleanup: `.
- List the data the tester needs on a line that starts with `Test data: `.
- Link the feature under test on a line `Covers: <feature>`.
- The first line must be `Test case: <title>`. The test ID does not belong in the first line.

## Rules kept unchanged from `testcase-compact`

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Describe the starting state on a line that begins with `Preconditions: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- "Write the outcome that counts as a pass on its own line beginning with `Expected result: `, and state the pass criterion on a line that starts with `Expected result: `."
- "1. Verify that the error appears. 2. Verify that the error is correctly identified. 3. Verify that the error is reproducible. Priority: P1."

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case specification: verify that a user is locked out after five failed login attempts.
Test ID: TC-0412
Feature: login
Priority: P1
Type: functional
Preconditions: User account exists
1. Attempt to log in with a valid username and incorrect password.
2. Attempt to log in with the same username and incorrect password (four more times).
3. Attempt to log in with the same username and incorrect password (fifth time).
4. Verify that the user is locked out.
Cleanup: Reset the account to allow login again.
```
