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

- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, and write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- Preconditions: [Describe the starting state] Test data: [List the data the tester needs]
- On a separate line, write `Covers: <feature>` to link the feature under test. On the next line, write `Type: functional`, `Type: regression`, `Type: smoke`, or `Type: negative` to tag the kind of test.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: Verify user is locked out after five failed login attempts  
Preconditions: User account exists and is active. System has login attempt tracking enabled.  
Test data: Valid username, five incorrect passwords  
1. Enter valid username and incorrect password.  
2. Verify the system denies access and displays an error message.  
3. Repeat steps 1 and 2 four more times.  
4. Verify the system locks the user account after the fifth failed attempt.  
5. Verify a lockout message is displayed and no further login attempts are allowed.  
Expected result: User is locked out after five failed login attempts and cannot log in until account is unlocked.  
Cleanup: Unlock the user account via admin interface.  
Covers: login  
Type: negative  
Priority: P1
```
