---
name: testcase-compact+testcase-traceable
description: Merged skill that replaces `testcase-compact` and `testcase-traceable`. Use for any test case specification.
---

# Merged skill: testcase-compact + testcase-traceable

This skill replaces `testcase-compact` and `testcase-traceable`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `testcase-compact`

- The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.
- State the pass criterion on a line that starts with `Expected result: `.
- Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.

## Rules kept unchanged from `testcase-traceable`

- Say how to restore the system afterwards on a line that starts with `Cleanup: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write
- Preconditions: Describe the starting state on a line that begins with `Preconditions: `. Test data: List the data the tester needs on a line that starts with `Test data: `.
- On separate lines, include both `Type: functional`, `Type: regression`, `Type: smoke`, or `Type: negative` to tag the test kind, and `Covers: <feature>` to link the feature under test. Place each label exactly as shown, with no additional text on the same lines.

## Example

Request: Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.

Output:

```
TC-0412: Lockout after five failed logins  
Preconditions: User account exists and is active; system enforces lockout after five failed attempts.  
Test data: Valid username, incorrect passwords (five different invalid passwords).  
Type: negative  
Covers: login  
Priority: P1  
Expected result: User is locked out from logging in after the fifth failed attempt and receives a lockout message.  
Cleanup: Unlock user account via admin console or wait for lockout duration to expire.
```
