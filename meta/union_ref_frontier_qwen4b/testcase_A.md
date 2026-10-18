<skill>
---
name: testcase-compact+testcase-traceable
description: Combined rules of `testcase-compact` and `testcase-traceable`. Use for any test case specification.
---

# Combined skill: testcase-compact + testcase-traceable

Follow every rule below.

## Rules from `testcase-compact`

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.
- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- State the pass criterion on a line that starts with `Expected result:`.
- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.
- Describe the starting state on a line that begins with `Preconditions: `.

## Rules from `testcase-traceable`

- Say how to restore the system afterwards on a line that starts with `Cleanup:`.
- List the data the tester needs on a line that starts with `Test data:`.
- Link the feature under test on a line `Covers: <feature>`.
- Write the outcome that counts as a pass on its own line beginning with `Expected result:`.
- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`
- The first line must be `Test case: <title>`. The test ID does not belong in the first line.

## Resolution of conflicting rules

If both rules require the first line to specify the test ID and title, **the rule from `testcase-compact` takes precedence**.  
Therefore, the first line must be: `<ID>: <title>`, and **the `Test case: <title>` line must be removed**.  
The `testcase-traceable` rule about starting with `Test case: <title>` is overridden to ensure consistency with `testcase-compact`.

## Example (correctly following all rules)

TC-0412: Lockout after five failed logins  
Type: functional  
Priority: P1  
Preconditions: User is logged in and has an existing account.  
Test data: Five invalid passwords in a row.  
Covers: authentication  
Cleanup: Reset login attempts and clear any temporary session data.  
Expected result: After five failed login attempts, the system locks out the user for a set period, and a message is displayed indicating the lockout.  
1. Attempt to log in with five invalid passwords in succession.  
2. Verify that after the fifth failed attempt, the login screen shows a "Account locked" message.  
3. Verify that the user is prevented from logging in for the specified duration.  
4. Verify that a "Try again later" button is available to proceed after the lockout period.  
5. Verify that the system logs the failed login attempts and the lockout status.

</skill>
