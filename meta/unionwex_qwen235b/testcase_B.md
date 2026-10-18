---
name: testcase-traceable+testcase-compact
description: Combined rules of `testcase-traceable` and `testcase-compact`. Use for any test case specification.
---

# Combined skill: testcase-traceable + testcase-compact

Follow every rule below.

## Rules from `testcase-traceable`

- Say how to restore the system afterwards on a line that starts with `Cleanup: `.
- List the data the tester needs on a line that starts with `Test data: `.
- Link the feature under test on a line `Covers: <feature>`.
- Write the outcome that counts as a pass on its own line beginning with `Expected result: `.
- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`
- The first line must be `Test case: <title>`. The test ID does not belong in the first line.

## Rules from `testcase-compact`

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- State the pass criterion on a line that starts with `Expected result: `.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Describe the starting state on a line that begins with `Preconditions: `.

If two rules cannot both hold, the rule from `testcase-traceable` wins.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: Verify user is locked out after five failed login attempts  
Preconditions: User account exists and is active. System has login attempt tracking enabled.  
Test data: Valid username, five incorrect passwords  
1. Enter valid username and incorrect password.  
2. Verify the system denies access and displays an error message.  
3. Repeat steps 1 and 2 four more times.  
4. Verify the system locks the user account after the fifth failed attempt.  
5. Verify a lockout message is displayed and no further login attempts are allowed.  
Expected result: User is locked out after five failed login attempts and cannot log in until account is unlocked.  
Cleanup: Unlock the user account via admin interface.  
Covers: login  
Type: negative  
Priority: P1
```
