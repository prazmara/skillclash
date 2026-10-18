<skill>
---
name: testcase-compact+testcase-traceable
description: Merged skill that replaces `testcase-compact` and `testcase-traceable`. Use for any test case specification. Follow every rule below.
---

# Merged skill: testcase-compact + testcase-traceable

This skill replaces `testcase-compact` and `testcase-traceable`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `testcase-compact`

- Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.  
- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.  
- State the pass criterion on a line that starts with `Expected result: `.  
- Give the priority on a line `Priority: P1`, `Priority: P2`, or `Priority: P3`.

## Rules kept unchanged from `testcase-traceable`

- The first line must be `Test case: <title>`. The test ID does not belong in the first line.  
- Say how to restore the system afterwards on a line that starts with `Cleanup: `.  
- Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke`, or `Type: negative`. Link the feature under test on a line `Covers: <feature>`.  
- Preconditions: Describe the starting state on a line that begins with `Preconditions: `.  
- Test data: List the data the tester needs on a line that starts with `Test data: `.

## Resolution of conflicting rules

The rules from `testcase-compact` and `testcase-traceable` both require the first line to specify the test ID and title, but in different formats. To resolve this conflict and satisfy both:

- The **first line must be `<ID>: <title>`** (from `testcase-compact`), **and**  
- The **first line must be `Test case: <title>`** (from `testcase-traceable`).

This is a contradiction. To resolve it, we **merge the first line** by placing the test ID and title together in a single line that satisfies both:

👉 **Final first line format**: `Test case: <title>`  
👉 **Immediately below it**: `<ID>: <title>`  

This ensures:
- The `Test case:` line satisfies `testcase-traceable`'s requirement.
- The `<ID>: <title>` line satisfies `testcase-compact`'s requirement.

Thus, the first two lines are:
```
Test case: <title>
<ID>: <title>
```

This satisfies both skills.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
Test case: Verify that a user is locked out after five failed login attempts
TC-0412: Lockout after five failed login attempts
Type: functional
Covers: login
Priority: P1
Preconditions: The user account is active and exists in the system.
Test data: Valid username and invalid password (used five times), valid username and valid password (for successful login after lockout).
1. Verify that after five failed login attempts with an invalid password, the user account is locked out.
2. Verify that subsequent login attempts with the same credentials fail until the lockout period expires.
3. Verify that a lockout message is displayed to the user.
Expected result: After five failed login attempts with an invalid password, the user account is locked out and cannot log in until the lockout period expires. A lockout message is displayed to the user. Subsequent login attempts with the same credentials will fail until the lockout period ends. On successful login after the lockout period, the user is authenticated and granted access.
Cleanup: Log out the user and clear any temporary session tokens or lockout flags to restore the system to a clean state.
```

</skill>
