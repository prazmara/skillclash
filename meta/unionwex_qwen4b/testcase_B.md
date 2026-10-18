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
TC-0412: Verify that a user is locked out after five failed login attempts
Priority: P1
Covers: login
Type: functional
Test data: Valid username and password (to trigger login), invalid password (to simulate failed attempts), valid username with invalid password (to simulate failed attempts)
Preconditions: User account exists and is active; system is running and login functionality is enabled; no prior login attempts have been made for the user. 
Steps: 
1. Navigate to the login page. 
2. Enter a valid username and an invalid password. 
3. Click the login button. 
4. Repeat step 2 and 3 four more times with invalid passwords. 
5. On the fifth failed attempt, attempt to log in again with the same username and password. 
Expected result: The user account is locked out and cannot log in. A message indicating account lockout is displayed. 
Cleanup: Reset the user account lockout status and clear any login attempt records in the system.
```
