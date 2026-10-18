---
name: testcase-compact+testcase-traceable
description: Merged skill that replaces `testcase-compact` and `testcase-traceable`. Use for any test case specification.
---

# Merged skill: testcase-compact + testcase-traceable

This skill replaces `testcase-compact` and `testcase-traceable`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `testcase-compact`

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- State the pass criterion on a line that starts with `Expected result: `.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Describe the starting state on a line that begins with `Preconditions: `.

## Rules kept unchanged from `testcase-traceable`

- Test case: <title>
- Covers: <feature>
- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`
- Say how to restore the system afterwards on a line that starts with `Cleanup: `

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins
Type: functional
Priority: P1
Preconditions:
- User has an account with the system
- User attempts to log in unsuccessfully four times

Expected result: The user is unable to log in after five failed attempts and is presented with a message indicating that their account is locked.

1. Verify that the user is unable to log in after five failed attempts
2. Verify that a message indicating that the account is locked is displayed
3. Verify that the user is unable to log in again until a specified time has passed or a system administrator unlocks the account

Cleanup:
- Log out of the system
- Reset the number of failed login attempts for the user account
```
