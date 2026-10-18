---
name: testcase-compact+testcase-traceable
description: Merged skill that replaces `testcase-compact` and `testcase-traceable`. Use for any test case specification.
---

# Merged skill: testcase-compact + testcase-traceable

This skill replaces `testcase-compact` and `testcase-traceable`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `testcase-compact`

- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- State the pass criterion on a line that starts with `Expected result: `.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Describe the starting state on a line that begins with `Preconditions: `.

## Rules kept unchanged from `testcase-traceable`

- Say how to restore the system afterwards on a line that starts with `Cleanup: `.
- List the data the tester needs on a line that starts with `Test data: `.
- Link the feature under test on a line `Covers: <feature>`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps, and make at least three of them explicit checks that start with the word `Verify`, for example `3. Verify that the error appears.` Combine the setup actions into at most two steps so that the three `Verify` steps fit inside the limit of five.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins

Preconditions: a registered user account exists and is not locked.
Priority: P1
Type: negative
Covers: login
Test data: one registered user with a known password.
1. Open the login page.
2. Enter the correct username with a wrong password five times.
3. Verify that the account locked message appears.
4. Verify that a login with the correct password is rejected.
5. Verify that the account shows as locked in the admin console.
Expected result: the account is locked after five failed attempts and stays locked.
Cleanup: unlock the account in the admin console.
```
