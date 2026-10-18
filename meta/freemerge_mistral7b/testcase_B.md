<skill>
---
name: testcase-compact-traceable
description: Write manual test case specifications in a compact format that auditors can trace and repeat, suitable for a test management tool. Use for any written test case.
---

# testcase-compact-traceable

Audited releases need test cases that link to a feature, name their data and prove each outcome with an explicit check. Testers run hundreds of cases per release, each case must be short enough to execute without scrolling and must carry the fields the tool filters on.

## Rules

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- State the pass criterion on a line that starts with `Expected result: `.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Describe the starting state on a line that begins with `Preconditions: `.
- Link the feature under test on a line `Covers: <feature>`.
- Write at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`
- The first line must be `Test case: <title>`. The test ID does not belong in the first line.
- Include a line for cleanup, starting with `Cleanup: `, if necessary.
- List the data the tester needs on a line that starts with `Test data: `, if necessary.

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
Type: negative
Priority: P1
```
</skill>
