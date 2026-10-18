---
name: testcase-compact+testcase-traceable
description: Merged skill that replaces `testcase-compact` and `testcase-traceable`. Use for any test case specification.
---

# Merged skill: testcase-compact + testcase-traceable

This skill replaces `testcase-compact` and `testcase-traceable`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `testcase-compact`

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Describe the starting state on a line that begins with `Preconditions: `.

## Rules kept unchanged from `testcase-traceable`

- Say how to restore the system afterwards on a line that starts with `Cleanup: `.
- List the data the tester needs on a line that starts with `Test data: `.
- Link the feature under test on a line `Covers: <feature>`.
- The first line must be `Test case: <title>`. The test ID does not belong in the first line.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Expected result: The output should clearly state the pass criterion in a manner that is both concise and traceable.
- "Assign a priority level of P1, P2, or P3 on a line labeled `Priority: P1`, `Priority: P2`, or `Priority: P3`. Include at least three numbered steps starting with `Verify` for explicit checks, such as `1. Verify that the error appears.`"

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: TC-0412: Lockout after five failed logins
Type: functional
Preconditions: User account exists
Test data: 5 failed login attempts
Covers: login
Cleanup: Reset the account to allow login
Priority: P1
1. Verify that the user can log in successfully.
2. Verify that the first failed login attempt is recorded.
3. Verify that the second failed login attempt is recorded.
4. Verify that the third failed login attempt is recorded.
5. Verify that the fourth failed login attempt is recorded.
6. Verify that the fifth failed login attempt is recorded.
7. Verify that the user is locked out after the fifth failed login attempt.
```
