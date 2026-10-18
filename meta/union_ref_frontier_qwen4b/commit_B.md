<skill>
---
name: ticket-first-commits+conventional-commits
description: Combined rules of `ticket-first-commits` and `conventional-commits`. Use for any commit message.
---

# Combined skill: ticket-first-commits + conventional-commits

Follow every rule below.

## Rules from `ticket-first-commits`

- Start the subject line with the ticket ID in square brackets, for example `[PAY-311] `. Nothing may come before the bracket.
- Record test status as `Tested: yes` or `Tested: no` on its own line.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Say how to revert in a line that starts with `Rollback: `.
- Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`.
- Name the affected component in a line `Component: <name>`.

## Rules from `conventional-commits`

- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.  
  (If the change does not introduce breaking changes, include `BREAKING CHANGE: none`.)
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the type.
- State whether the change was tested with a line `Tested: yes` or `Tested: no`.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`.
- Explain the motivation in a body line that starts with `Why: `.

## Conflict Resolution

If two rules cannot both hold, the rule from `ticket-first-commits` takes precedence **only** when there is a direct conflict in content or format. However, the rule from `conventional-commits` to include `BREAKING CHANGE: none` when no breaking changes are introduced **must be satisfied** and is not in conflict with any other rule. Therefore, the assistant must explicitly add the line `BREAKING CHANGE: none` to every commit message if no breaking changes are introduced.

This rule is not in conflict with the ticket-first-commits rules and is fully compatible with them. It only requires adding a line at the appropriate position in the message body (after the risk line or in a dedicated body section), and it does not interfere with the subject line, test status, or other required elements.

Thus, the assistant must include:
- `BREAKING CHANGE: none` in every commit message, even when no breaking changes are present.
- The `Risk:` line (low/medium/high).
- The `Why:` line.
- The `Signed-off-by:` line at the very end.

## Example (correctly following all rules)

[DATA-789] fix: resolve data loss during bulk imports
- Ensure all records are properly validated before insertion
- Add transactional boundaries to prevent partial writes
Tested: yes
Rollback: Revert by removing validation checks and disabling transaction boundaries
Component: imports
Risk: low
BREAKING CHANGE: none
Why: Prevents data corruption in high-volume import scenarios
Refs: DATA-789
Signed-off-by: David Chen

[FILE-674] fix: resolve timeout issues in the file upload endpoint
- Increased the timeout duration from 30 seconds to 60 seconds to handle large file uploads.
- Implemented a progress tracking mechanism to provide real-time feedback during uploads.
Tested: yes
Rollback: Revert by removing the timeout increase and progress tracking, then restore original timeout settings.
Component: uploads
Risk: low
BREAKING CHANGE: none
Why: Large files were being dropped during upload due to insufficient timeout, leading to user frustration and failed uploads.
Refs: FILE-674
Signed-off-by: Amara Thompson
</skill>
