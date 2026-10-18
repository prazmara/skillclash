<skill>
---
name: testcase-compact-traceable
description: Write manual test case specifications in the compact format of the test management tool that auditors can trace and repeat. Use for any written test case.
---

# testcase-compact-traceable

Testers run hundreds of cases per release. Each case must be short enough to execute without scrolling and must carry the fields the tool filters on. Audited releases need test cases that link to a feature, name their data and prove each outcome with an explicit check.

## Rules

- Write the steps as a numbered list (`1.`, `2.`,...) with at most eight steps.
- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- State the pass criterion on a line that starts with `Expected result: `.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Describe the starting state on a line that begins with `Preconditions: `.
- Say how to restore the system afterwards on a line that starts with `Cleanup: `.
- List the data the tester needs on a line that starts with `Test data: `.
- Link the feature under test on a line `Covers: <feature>`.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins

Preconditions: a registered user account exists and is not locked.
Priority: P1
Type: negative
Covers: login
Test data: one registered user with a known password.
1. Open the login page.
2. Enter the correct username with a wrong password five times.
3. Verify that the message Invalid credentials appears after the fourth attempt.
4. Verify that the message Account locked appears after the fifth attempt.
5. Enter the correct password.
6. Verify that the login is still rejected.
7. Open the admin console and look up the user.
Expected result: the account is locked after five failed attempts and stays locked.
Cleanup: unlock the account in the admin console.
```
