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

- 1. Verify that the error appears. 2. Verify that the system responds correctly to user input. 3. Verify that the error message is displayed in the expected format.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: Verify that a user is locked out after five failed login attempts  
Covers: login  
Priority: P1  
Type: functional  
Preconditions: User account exists and is active, system allows up to five failed login attempts before locking out.  
Test data: Valid username and invalid password (used five times), valid username and valid password (to verify unlock).  
Steps:  
1. Attempt to log in with a valid username and an invalid password.  
2. Repeat step 1 four more times to reach five failed attempts.  
3. Attempt to log in with the same username and invalid password for the sixth time.  
Expected result: The system should display a "Account locked. Please try again later" message and prevent further login attempts.  
Cleanup: After the test, log in with valid credentials to unlock the account.  
Verify that the error appears.  
Verify that the system responds correctly to user input.  
Verify that the error message is displayed in the expected format.
```
