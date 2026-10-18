---
name: testcase-traceable+testcase-compact
description: Merged skill that replaces `testcase-traceable` and `testcase-compact`. Use for any test case specification.
---

# Merged skill: testcase-traceable + testcase-compact

This skill replaces `testcase-traceable` and `testcase-compact`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `testcase-traceable`

- Test case: <title>
- Covers: <feature>
- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`
- Say how to restore the system afterwards on a line that starts with `Cleanup: `

## Rules kept unchanged from `testcase-compact`

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- State the pass criterion on a line that starts with `Expected result: `.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Describe the starting state on a line that begins with `Preconditions: `.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins

Type: functional
Priority: P1

Preconditions:
- A user account is created with a password.
- The user attempts to log in four times with an incorrect password.

1. Verify that the user is able to log in with a correct password on the first attempt.
2. Verify that the user is unable to log in with an incorrect password.
3. Verify that the login attempt counter increments by one after an unsuccessful login.
4. Verify that the user is unable to log in with an incorrect password for a total of five times.
5. Verify that the user is locked out and unable to log in after five failed login attempts.

Expected result: The user is locked out after five failed login attempts.

Cleanup:
- Reset the login attempt counter for the user account.
- Clear any stored login credentials.
```
