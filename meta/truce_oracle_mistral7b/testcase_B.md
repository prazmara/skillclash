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

- Write the steps as a compact, numbered list (1., 2., 3., 4., 5.) with at most five steps, where each step starts with the word "Verify" (e.g., "3. Verify that the error appears.") to satisfy both the "testcase-traceable" and "testcase-compact" rules simultaneously.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: Verify user lockout after five failed login attempts (TC-0412)
Covers: login
Preconditions:
1. A user account is created with a password.
2. The user attempts to log in with an incorrect password.
3. The user attempts to log in again with an incorrect password.
4. The user attempts to log in again with an incorrect password.
5. The user attempts to log in again with an incorrect password.
6. The user attempts to log in again with an incorrect password.

Test data: A user account with a known incorrect password.

Cleanup: Successful login to reset the lockout status.

Expected result: After five failed login attempts, the user is unable to log in.

Priority: P1
Type: functional

1. Verify that the user is able to log in initially with the correct password.
2. Verify that the user is unable to log in with an incorrect password.
3. Verify that the number of failed login attempts increments by one after an unsuccessful login.
4. Verify that the user is unable to log in after four failed login attempts.
5. Verify that the user is unable to log in after five failed login attempts.
6. Verify that the user is able to log in again after resetting the lockout status.
```
