<skill>
---
name: testcase-traceable+testcase-compact
description: Merged skill that replaces `testcase-traceable` and `testcase-compact`. Use for any test case specification.
---

# Merged skill: testcase-traceable + testcase-compact

This skill replaces `testcase-traceable` and `testcase-compact`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `testcase-traceable`

- Say how to restore the system afterwards on a line that starts with `Cleanup: `.
- Write the outcome that counts as a pass on its own line beginning with `Expected result: `.
- The first line must be `Test case: <title>`. The test ID does not belong in the first line.

## Rules kept unchanged from `testcase-compact`

- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Link the feature under test on a line `Covers: <feature>`. Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke`, or `Type: negative`.
- Test data: [list the data the tester needs] Preconditions: [describe the starting state]

## Additional rule (added to resolve conflicts and ensure compliance)

- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`

## Step list constraints

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: Verify that a user is locked out after five failed login attempts
TC-0412: Verify that a user is locked out after five failed login attempts
Priority: P1
Covers: login
Type: functional
Test data: Valid username and password (to trigger login), invalid password (to simulate failed attempts), valid username with invalid password (to simulate failed attempts)
Preconditions: User account exists and is active; system is running and login functionality is enabled; no prior login attempts have been made for the user. 
Steps: 
1. Navigate to the login page. 
2. Enter a valid username and an invalid password. 
3. Click the login button. 
4. Repeat step 2 and 3 four more times with invalid passwords. 
5. On the fifth failed attempt, attempt to log in again with the same username and password. 
Expected result: The user account is locked out and cannot log in. A message indicating account lockout is displayed. 
Cleanup: Reset the user account lockout status and clear any login attempt records in the system.
```
</skill>
