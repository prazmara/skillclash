---
name: testcase-traceable-compact
description: Write manual test case specifications that are both traceable for auditors and compact for test tools. Use for any written test case.
---

# testcase-traceable-compact

Test cases must be auditable and repeatable while remaining compact enough for efficient execution in test management tools. This skill merges traceability requirements with compact formatting rules. When conflicts arise, traceability rules from `testcase-traceable` take precedence.

## Rules

- The first line must be `Test case: <title>`. The test ID does not belong in the first line.
- Link the feature under test on a line `Covers: <feature>`.
- List the data the tester needs on a line that starts with `Test data: `.
- State the pass criterion on a line that starts with `Expected result: `.
- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`
- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps. If more than five steps are needed, consolidate or split into separate test cases.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Describe the starting state on a line that begins with `Preconditions: `.
- Say how to restore the system afterwards on a line that starts with `Cleanup: `.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: Lockout after five failed logins

Covers: login
Preconditions: a registered user account exists and is not locked.
Test data: one registered user with a known password.
Priority: P1
Type: negative
1. Open the login page.
2. Enter the correct username and a wrong password.
3. Verify that the message Invalid credentials appears.
4. Repeat steps 2–3 four more times.
5. Verify that the message Account locked appears and the account cannot be unlocked by correct credentials.
Expected result: the account is locked after five failed attempts and stays locked.
Cleanup: unlock the account in the admin console.
```
