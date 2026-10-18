---
name: testcase-compact-traceable
description: Write manual test case specifications in a compact format that are traceable, auditable, and suitable for test management tools. Use for any written test case.
---

# testcase-compact-traceable

Testers and auditors require test cases that are concise, filterable, and repeatable. Each case must fit within five steps, include all required fields for filtering and traceability, and provide explicit checks, data, and cleanup instructions.

## Rules

- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- State the pass criterion on a line that starts with `Expected result: `.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Describe the starting state on a line that begins with `Preconditions: `.
- Link the feature under test on a line `Covers: <feature>`.
- List the data the tester needs on a line that starts with `Test data: `.
- Say how to restore the system afterwards on a line that starts with `Cleanup: `.
- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`

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
3. Verify that the account is locked after the fifth attempt.
4. Enter the correct password.
5. Verify that login is rejected and the account shows as locked.
Expected result: the sixth attempt is rejected and the account shows as locked.
Cleanup: unlock the account in the admin console.
```
