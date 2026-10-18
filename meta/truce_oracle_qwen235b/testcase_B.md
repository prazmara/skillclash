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

- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, and write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: Verify user is locked out after five failed login attempts  
Covers: login  
Priority: P1  
Type: negative  
Preconditions: User account exists and is active; system enforces account lockout after five failed attempts  
Test data: Username: testuser, Password: wrongpass (incorrect), Correct password: validpass  
1. Attempt to log in with username 'testuser' and incorrect password 'wrongpass'  
2. Verify the login fails and an error message is displayed  
3. Repeat steps 1–2 four more times  
4. Verify the account is locked after the fifth failed attempt  
5. Verify a lockout message is displayed and no further login attempts are allowed  
Expected result: After five consecutive failed login attempts, the user account is locked and a lockout message is shown  
Cleanup: Unlock the user account via admin console or reset account state
```
