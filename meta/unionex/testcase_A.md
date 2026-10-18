---
name: testcase-compact+testcase-traceable
description: Combined rules of `testcase-compact` and `testcase-traceable`. Use for any test case specification.
---

# Combined skill: testcase-compact + testcase-traceable

Follow every rule below.

## Rules from `testcase-compact`

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- State the pass criterion on a line that starts with `Expected result: `.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Describe the starting state on a line that begins with `Preconditions: `.

## Rules from `testcase-traceable`

- Say how to restore the system afterwards on a line that starts with `Cleanup: `.
- List the data the tester needs on a line that starts with `Test data: `.
- Link the feature under test on a line `Covers: <feature>`.
- Write the outcome that counts as a pass on its own line beginning with `Expected result: `.
- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`
- The first line must be `Test case: <title>`. The test ID does not belong in the first line.

## Examples

Example for `testcase-compact`:

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins

Preconditions: a registered user account exists and is not locked.
Priority: P1
Type: negative
1. Open the login page.
2. Enter the correct username with a wrong password five times.
3. Enter the correct password.
Expected result: the sixth attempt is rejected and the account shows as locked.
```

Example for `testcase-traceable`:

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: Lockout after five failed logins

Covers: login
Test data: one registered user with a known password.
1. Open the login page.
2. Enter the correct username and a wrong password.
3. Verify that the message Invalid credentials appears.
4. Repeat the wrong password four more times.
5. Verify that the message Account locked appears after the fifth attempt.
6. Enter the correct password.
7. Verify that the login is still rejected.
8. Open the admin console and look up the user.
Expected result: the account is locked after five failed attempts and stays locked.
Cleanup: unlock the account in the admin console.
```
