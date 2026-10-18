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

If two rules cannot both hold, the rule from `testcase-compact` wins.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins  
Type: functional  
Priority: P1  
Preconditions: User account exists and is in an unlocked state.  
Test data: Valid username, invalid password  
Covers: login  
1. Attempt to log in with the valid username and an invalid password five times in succession.  
2. On the sixth attempt, try to log in again with the valid username and the correct password.  
3. Verify that the user is unable to log in and receives a lockout message.  
4. Verify that the account status is set to "locked" in the system.  
5. Verify that no further login attempts are allowed until the lockout period expires or the account is unlocked by an admin.  
Expected result: The user is locked out after five failed login attempts and cannot log in, even with the correct password, until the lockout is lifted.  
Cleanup: Unlock the user account in the system to restore access.
```
