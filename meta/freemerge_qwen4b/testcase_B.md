---
name: testcase-traceable
description: Write manual test case specifications that auditors can trace and repeat. Use for any written test case.

# testcase-traceable

Audited releases need test cases that link to a feature, name their data and prove each outcome with an explicit check.

## Rules

- Say how to restore the system afterwards on a line that starts with `Cleanup:`.
- List the data the tester needs on a line that starts with `Test data:`.
- Link the feature under test on a line `Covers: <feature>`.
- Write the outcome that counts as a pass on its own line beginning with `Expected result:`.
- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`
- The first line must be `Test case: <title>`. The test ID does not belong in the first line.
- Where two rules conflict, the rule from `testcase-traceable` takes precedence over `testcase-compact`.

## Example

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
