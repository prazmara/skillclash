<skill>
---
name: testcase-compact+testcase-traceable
description: Merged skill that replaces `testcase-compact` and `testcase-traceable`. Use for any test case specification. Follow every rule below.
---

# Merged skill: testcase-compact + testcase-traceable

This skill replaces `testcase-compact` and `testcase-traceable`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `testcase-compact`

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.  
- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.  
- State the pass criterion on a line that starts with `Expected result: `.  
- Give the priority on a line `Priority: P1`, `Priority: P2`, or `Priority: P3`.

## Rules kept unchanged from `testcase-traceable`

- The first line must be `Test case: <title>`. The test ID does not belong in the first line.  
- Say how to restore the system afterwards on a line that starts with `Cleanup: `.  
- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke`, or `Type: negative`. Link the feature under test on a line `Covers: <feature>`.  
- Preconditions: Describe the starting state on a line that begins with `Preconditions: `.  
- Test data: List the data the tester needs on a line that starts with `Test data: `.

## Conflict resolution and clarification

The rules "The first line must be the test ID and the title as `<ID>: <title>`" (from `testcase-compact`) and "The first line must be `Test case: <title>`" (from `testcase-traceable`) **cannot both be true** in the same document. To resolve this conflict:

✅ **Final rule**: The **first line must be the test ID and the title as `<ID>: <title>`**.  
This is the only correct and consistent first line for the merged skill.  
The `Test case: <title>` line is **replaced** by the test ID line.  
Therefore, the `Test case: ...` line is **removed** from the output.

This change ensures full compliance with the `testcase-compact` rule, which mandates the test ID in the first line. It also maintains the core functionality of the original skills: the test ID is clearly visible, and the title is included in a standardized format.

The example below now correctly follows all rules, including the corrected first line.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins
Type: functional
Covers: login
Priority: P1
Preconditions: The user account is active and exists in the system.
Test data: Valid username and invalid password (used five times), valid username and valid password (for successful login after lockout).
1. Verify that the user enters an invalid password for login.
2. Verify that the login attempt fails and a failure message is displayed.
3. Verify that the user attempts login a fifth time with the same invalid password.
4. Verify that the account is locked out and subsequent login attempts fail.
5. Verify that a lockout message is displayed to the user and the system does not allow login until the lockout period expires.
Expected result: After five failed login attempts with an invalid password, the user account is locked out and cannot log in until the lockout period expires. A lockout message is displayed to the user. Subsequent login attempts with the same credentials will fail until the lockout period ends. On successful login after the lockout period, the user is authenticated and granted access.
Cleanup: Reset the user account lockout status and ensure the system is in a clean state for the next test.
```
</skill>
