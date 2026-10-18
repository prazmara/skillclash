---
name: testcase-compact-traceable
description: Write manual test case specifications in the compact format of the test management tool that auditors can also trace and repeat. Use for any written test case.
---

# testcase-compact-traceable

This skill merges `testcase-compact` and `testcase-traceable` and replaces both. Testers run hundreds of cases per release, so each case must be short enough to execute without scrolling and must carry the fields the tool filters on. Audited releases also need test cases that link to a feature, name their data and prove each outcome with an explicit check.

Every rule of both skills is kept. Where two rules cannot both hold, `testcase-compact` wins.

## Rules

- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`. This is the `testcase-compact` rule. It overrides the `testcase-traceable` rule that the first line is `Test case: <title>` without the test ID, so no `Test case:` line is written.
- Link the feature under test on a line `Covers: <feature>`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Describe the starting state on a line that begins with `Preconditions: `.
- List the data the tester needs on a line that starts with `Test data: `.
- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.` Together with the previous rule this means three to five numbered steps in total, of which at least three start with `Verify`. Combine several actions into one step so that the list never exceeds five steps.
- State the pass criterion on its own line that starts with `Expected result: `.
- Say how to restore the system afterwards on a line that starts with `Cleanup: `.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins

Covers: login
Priority: P1
Type: negative
Preconditions: a registered user account exists and is not locked.
Test data: one registered user with a known password.
1. Open the login page and enter the correct username with a wrong password.
2. Verify that the message Invalid credentials appears.
3. Repeat the wrong password four more times.
4. Verify that the message Account locked appears after the fifth attempt.
5. Verify that a login with the correct password is still rejected.
Expected result: the account is locked after five failed attempts and stays locked.
Cleanup: unlock the account in the admin console.
```
