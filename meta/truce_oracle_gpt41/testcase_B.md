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

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps, and include at least three explicit checks, each starting with the word `Verify`.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: Verify user is locked out after five failed login attempts  
Covers: login  
Test data: Valid username, invalid password  
Preconditions: User account exists and is not locked  
Priority: P1  
Type: functional  
1. Attempt to log in with the valid username and an invalid password five times in succession.  
2. Verify that after the fifth failed attempt, the system displays a lockout message or notification.  
3. Verify that further login attempts with the correct password are rejected due to account lockout.  
4. Verify that the lockout status is recorded in the system logs or audit trail.  
5. Verify that the user cannot access any protected resources while locked out.  
Cleanup: Unlock the user account in the system.  
Expected result: User is locked out after five failed login attempts and cannot log in until the account is unlocked.
```
