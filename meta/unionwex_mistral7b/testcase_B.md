---
name: testcase-traceable+testcase-compact
description: Combined rules of `testcase-traceable` and `testcase-compact`. Use for any test case specification.
---

# Combined skill: testcase-traceable + testcase-compact

Follow every rule below.

## Rules from `testcase-traceable`

- Say how to restore the system afterwards on a line that starts with `Cleanup: `.
- List the data the tester needs on a line that starts with `Test data: `.
- Link the feature under test on a line `Covers: <feature>`.
- Write the outcome that counts as a pass on its own line beginning with `Expected result: `.
- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`
- The first line must be `Test case: <title>`. The test ID does not belong in the first line.

## Rules from `testcase-compact`

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- State the pass criterion on a line that starts with `Expected result: `.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Describe the starting state on a line that begins with `Preconditions: `.

If two rules cannot both hold, the rule from `testcase-traceable` wins.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins

Type: functional
Priority: P1

Preconditions:
- A user account is created with a password.
- The user attempts to log in four times with an incorrect password.

1. Verify that the user is able to log in with a correct password on the first attempt.
2. Verify that the user is unable to log in with an incorrect password.
3. Verify that the login attempt counter increments by one after an unsuccessful login.
4. Verify that the user is unable to log in with an incorrect password for a total of five times.
5. Verify that the user is locked out and unable to log in after five failed login attempts.

Expected result: The user is locked out after five failed login attempts.

Cleanup:
- Reset the login attempt counter for the user account.
- Clear any stored login credentials.
```
