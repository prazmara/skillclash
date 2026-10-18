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

- Write a numbered list with at most five steps, where each step starts with the word "Verify" and is an explicit check, for example: 1. Verify that the error appears. 2. Verify that the error message matches the expected output. 3. Verify that the error is resolved after correction. 4. Verify that the system behaves as expected under normal conditions. 5. Verify that the system recovers from the error.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: Verify user is locked out after five failed login attempts
Test ID: TC-0412
Covers: login
Preconditions: The system is in a normal state, and the user account has no existing login attempts.
Test data: 
- User account with valid credentials
- User account with invalid credentials
- Invalid login credentials (e.g., incorrect username or password)
Priority: P1
Type: functional
Expected result: The user is locked out after five failed login attempts.
Verify:
1. Verify that the user can log in successfully with valid credentials.
2. Verify that the user is prompted to enter their credentials after five failed login attempts.
3. Verify that the user is unable to log in after five failed login attempts.
4. Verify that the system displays a message indicating that the user is locked out.
5. Verify that the user remains locked out until an administrator resets their account.
Cleanup: Reset the user account to its original state, with no login attempts.
```
