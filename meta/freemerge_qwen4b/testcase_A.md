---
name: testcase-compact
description: Write manual test case specifications in the compact format of the test management tool. Use for any written test case.

# testcase-compact

Testers run hundreds of cases per release. Each case must be short enough to execute without scrolling and must carry the fields the tool filters on.

## Rules

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- State the pass criterion on a line that starts with `Expected result:`.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Describe the starting state on a line that begins with `Preconditions:`.
- List the data the tester needs on a line that starts with `Test data:`.
- Link the feature under test on a line `Covers: <feature>`.
- Say how to restore the system afterwards on a line that starts with `Cleanup:`.
- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins

Preconditions: a registered user account exists and is not locked.
Test data: one registered user with a known password.
Covers: login
Priority: P1
Type: negative
1. Open the login page.
2. Enter the correct username with a wrong password five times.
3. Enter the correct password.
Expected result: the sixth attempt is rejected and the account shows as locked.
Cleanup: unlock the account in the admin console.
```
