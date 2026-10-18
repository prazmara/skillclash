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

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps, including at least three explicit checks starting with `Verify`, such as `3. Verify that the error appears.`

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins
Preconditions: User is registered and knows their credentials.
Priority: P1
Type: functional
Covers: login
Test data: Username: testuser, Password: incorrectpassword
Expected result: Account should be locked after five failed login attempts.
1. Open the login page.
2. Enter the username "testuser" and an incorrect password.
3. Verify that the login fails.
4. Enter the username "testuser" and an incorrect password again.
5. Verify that the login fails.
6. Enter the username "testuser" and an incorrect password a third time.
7. Verify that the login fails.
8. Enter the username "testuser" and an incorrect password a fourth time.
9. Verify that the login fails.
10. Enter the username "testuser" and an incorrect password a fifth time.
11. Verify that the login fails and the account is locked.
Cleanup: None needed.
```
