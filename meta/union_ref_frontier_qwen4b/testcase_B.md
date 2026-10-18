<skill>
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
- Describe the starting state on a line beginning with `Preconditions: `.

## Conflict Resolution

If two rules conflict, the rule from `testcase-traceable` takes precedence. Specifically:
- The first line must be `Test case: <title>` (no test ID), even if `testcase-compact` requires `<ID>: <title>`. This overrides the compact format.
- All other rules (including step formatting, `Expected result`, `Covers`, `Preconditions`, `Test data`, `Cleanup`, and `Type`, `Priority`) are applied as usual, with `testcase-traceable` rules taking priority when in conflict.

## Example (Valid Output)

Test case: Validate that a user cannot bypass two-factor authentication  
Covers: authentication  
Type: functional  
Priority: P1  
Preconditions: User is registered and has enabled two-factor authentication.  
Test data: User account with active two-factor authentication, valid login credentials, valid OTP from authenticator app.  
1. Log in to the application using valid credentials.  
2. Attempt to proceed to the dashboard without entering the two-factor authentication code.  
3. Verify that the system prompts for the two-factor authentication code.  
4. Verify that the system does not allow access to the dashboard without entering the correct code.  
5. Verify that an error message is displayed indicating that two-factor authentication is required.  
Expected result: The user is unable to access the dashboard without providing the two-factor authentication code.  
Cleanup: Reset the two-factor authentication status for the user account to ensure no residual state affects future tests.

</skill>
