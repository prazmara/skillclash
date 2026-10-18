---
name: testcase-traceable-compact
description: Write manual test case specifications that are both traceable for audit and compact for test management tools. Use for any written test case.
---

# testcase-traceable-compact

Test cases must be both traceable for audit and compact for efficient execution. Each case links to a feature, names its data, proves each outcome with explicit checks, and includes all fields required by test management tools.

## Rules

- The first line must be `Test case: <title>`. The test ID does not belong in the first line.
- Link the feature under test on a line `Covers: <feature>`.
- List the data the tester needs on a line that starts with `Test data: `.
- State the starting state on a line that begins with `Preconditions: `.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Write the outcome that counts as a pass on its own line beginning with `Expected result: `.
- Say how to restore the system afterwards on a line that starts with `Cleanup: `.
- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: Lockout after five failed logins

Covers: login
Test data: one registered user with a known password.
Preconditions: a registered user account exists and is not locked.
Priority: P1
Type: negative
1. Open the login page.
2. Enter the correct username and a wrong password.
3. Verify that the message Invalid credentials appears.
4. Repeat the wrong password four more times.
5. Verify that the message Account locked appears after the fifth attempt.
Expected result: the account is locked after five failed attempts and stays locked.
Cleanup: unlock the account in the admin console.
```
