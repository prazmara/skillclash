---
name: testcase-compact+testcase-traceable
description: Merged skill that replaces `testcase-compact` and `testcase-traceable`. Use for any test case specification.
---

# Merged skill: testcase-compact + testcase-traceable

This skill replaces `testcase-compact` and `testcase-traceable`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `testcase-compact`

- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- Describe the starting state on a line that begins with `Preconditions: `.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- State the pass criterion on a line that starts with `Expected result: `.

## Rules kept unchanged from `testcase-traceable`

- Link the feature under test on a line `Covers: <feature>`.
- List the data the tester needs on a line that starts with `Test data: `.
- Say how to restore the system afterwards on a line that starts with `Cleanup: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the steps as a numbered list (1., 2., 3., 4., 5.) with at most five steps. Include at least three numbered steps (1., 2., 3.) that are explicit checks, each starting with the word "Verify", for example "3. Verify that the error appears." Arrange the steps such that the first four steps (1., 2., 3., 4.) are general actions, and the fifth step (5.) is the final verification check.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins

Preconditions:
- A user account is created with valid credentials.
- The user attempts to log in unsuccessfully four times.

Priority: P1
Type: functional

Covers: login

Test data:
- A valid username and password for the user account.
- Incorrect credentials for four failed login attempts.

Cleanup:
- Reset the user account to allow further login attempts.

1. Navigate to the login page.
2. Enter the user's valid username.
3. Enter an incorrect password for the first failed login attempt.
4. Attempt to log in again with the incorrect password.
5. Verify that the user is locked out and cannot log in with the same credentials.
6. Attempt to log in again with the correct credentials after the lockout period has elapsed.
7. Verify that the user is now able to log in successfully.
```
