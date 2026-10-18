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
- Write the outcome that counts as a pass on its own line beginning with `Expected result: `.
- The first line must be `Test case: <title>`. The test ID does not belong in the first line.

## Rules kept unchanged from `testcase-compact`

- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Describe the starting state on a line that begins with `Preconditions: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps, and include at least three explicit checks, each starting with the word `Verify`.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: Verify user is locked out after five failed login attempts  
Type: functional  
Priority: P1  
Preconditions: User account exists and is in active status; user is logged out.  
Test data: Valid username, invalid password  
Covers: login  

1. Attempt to log in with the valid username and an invalid password five times in succession.
2. Verify that after each of the first four attempts, the login fails and an error message is displayed.
3. Verify that on the fifth failed attempt, the system displays a message indicating the account is locked.
4. Attempt to log in again with the correct password.
5. Verify that the user is unable to log in and receives a locked account notification.

Expected result: User account is locked after five failed login attempts, and further login attempts are blocked.  
Cleanup: Unlock the user account in the system to restore access.
```
