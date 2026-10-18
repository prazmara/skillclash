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

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps. Include at least three numbered steps that are explicit checks, each starting with the word `Verify`.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins  
Covers: login  
Priority: P1  
Type: functional  
Preconditions: User account exists and is active; system is not in maintenance mode.  
Test data: Valid username and invalid passwords (five times), valid username and valid password (for final login).  
Expected result: After five failed login attempts with incorrect passwords, the user account is locked out and cannot log in; a "Account locked" message is displayed upon attempting to log in again.  
Cleanup: Reset the user account lock status by clearing the failed login counter in the database.  
1. Enter an invalid password for a valid username.  
2. Enter an invalid password for the same username.  
3. Verify that the login attempt fails and a "Wrong password" message is displayed.  
4. Repeat step 2 four more times with invalid passwords.  
5. Verify that the login attempt fails after the fifth failed attempt and a "Account locked" message is displayed.
```
