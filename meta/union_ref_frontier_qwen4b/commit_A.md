<skill>
---
name: conventional-commits+ticket-first-commits
description: Combined rules of `conventional-commits` and `ticket-first-commits`. Use for any commit message.
---

# Combined skill: conventional-commits + ticket-first-commits

Follow every rule below. If two rules conflict, the rule from `conventional-commits` takes precedence.

## Rules from `conventional-commits`

- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.  
  (If no breaking changes are introduced, this line must appear exactly as `BREAKING CHANGE: none`.)
- Add a body line `Risk: low`, `Risk: medium`, or `Risk: high`.
- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the type.  
  (The ticket ID must not appear before this type prefix; the type prefix must be immediately followed by a colon.)
- State whether the change was tested with a line `Tested: yes` or `Tested: no`.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`.
- Explain the motivation in a body line that starts with `Why: `.

## Rules from `ticket-first-commits`

- Start the subject line with the ticket ID in square brackets, for example `[PAY-311] `. Nothing may come before the bracket.  
  (This rule is **in conflict** with the conventional-commits rule about type prefix. To resolve, the ticket ID **must** come first, followed immediately by the type prefix. Thus, the subject line must be: `[TICKET-ID] <type>: <description>`. The ticket ID must be the very first thing in the subject line, and the type prefix must follow immediately after it, with no text in between.)
- Record test status as `Tested: yes` or `Tested: no` on its own line.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Say how to revert in a line that starts with `Rollback: `.
- Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`.
- Name the affected component in a line `Component: <name>`.

## Conflict Resolution

- **Subject line**: The ticket ID must appear first in square brackets, immediately followed by a type prefix and a colon (e.g., `[DATA-789] fix: data loss during bulk imports`). This satisfies both `ticket-first-commits` and `conventional-commits` rules. The type prefix must be one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:` and must come directly after the ticket ID.
- **Breaking Change**: The `BREAKING CHANGE: none` line must appear in the message, even if no breaking changes are introduced.
- **Risk**: A `Risk: low`, `medium`, or `high` line must appear in the body.
- **Tested**: A line `Tested: yes` or `Tested: no` must appear in the body.
- **Why**: A line starting with `Why: ` must appear in the body.
- **Rollback**: A line starting with `Rollback: ` must appear in the body.
- **Component**: A line `Component: <name>` must appear in the body.
- **Sign-off**: The very last line must be `Signed-off-by: <author name>`.
- **Refs**: A line `Refs: <TICKET-ID>` must appear at the end of the message, after the sign-off.

## Example (Corrected and Fully Compliant)

[REG-444] feat: add validation to prevent duplicate user registrations
- Validates user email uniqueness before registration
- Prevents creation of duplicate accounts with the same email address
- Throws error if a user with the same email already exists
Risk: low
Tested: yes
Why: Prevents data inconsistency and ensures user data integrity
Rollback: Remove email uniqueness validation and allow duplicate registrations
Component: users
BREAKING CHANGE: none
Signed-off-by: Maria Garcia
Refs: REG-444

</skill>
