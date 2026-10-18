---
name: testcase-compact+testcase-traceable
description: Merged skill that replaces `testcase-compact` and `testcase-traceable`. Use for any test case specification.
---

# Merged skill: testcase-compact + testcase-traceable

This skill replaces `testcase-compact` and `testcase-traceable`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `testcase-compact`

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- State the pass criterion on a line that starts with `Expected result: `.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Describe the starting state on a line that begins with `Preconditions: `.

## Rules kept unchanged from `testcase-traceable`

- List the data the tester needs on a line that starts with `Test data: `.
- Link the feature under test on a line `Covers: <feature>`.
- Write the outcome that counts as a pass on its own line beginning with `Expected result: `.
- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`
- The first line must be `Test case: <title>`. The test ID does not belong in the first line.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins
Preconditions: User is registered and has a valid username and password.
Test data: Username, password, and login page URL.
Expected result: After five failed login attempts, the user should be locked out and see an appropriate error message.
Type: functional
Priority: P1
1. Navigate to the login page using the provided URL.
2. Enter an incorrect password and click login.
3. Verify that the login fails.
4. Enter an incorrect password again and click login.
5. Verify that the login fails.
6. Enter an incorrect password once more and click login.
7. Verify that the login fails.
8. Enter an incorrect password for the fourth time and click login.
9. Verify that the login fails.
10. Enter an incorrect password for the fifth time and click login.
11. Verify that the user is locked out and sees an error message indicating the account is locked.
```
