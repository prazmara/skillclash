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

- Write the steps as a numbered list with at most five steps, where at least three of the steps are explicit checks starting with the word "Verify", for example "3. Verify that the error appears."

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins

Priority: P1
Type: functional
Covers: login
Preconditions: The user has a valid account with a valid username and password, and the account is not locked out.

1. The user attempts to log in with an incorrect password.
2. The user attempts to log in with an incorrect password again.
3. Verify that the error appears, indicating that the password is incorrect.
4. The user attempts to log in with an incorrect password three more times.
5. Verify that the system locks out the user after the fifth failed login attempt.

Test data: A valid username and password, and five incorrect passwords.

Expected result: The user is locked out and cannot log in until the account is unlocked.

Cleanup: Unlock the user's account to restore the system to its original state.
```
