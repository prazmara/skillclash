---
name: merged-commits
description: Write commit messages that lead with the tracker ticket and follow the team's Conventional Commits format. Use for any commit message.
---

# merged-commits

Every commit must be traceable to a tracker ticket, so the ticket leads the message, and follow the team's Conventional Commits format.

## Rules

- Start the subject line with the ticket ID in square brackets, for example `[PAY-311] `. Nothing may come before the bracket.
- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the type.
- Record test status as `Tested: yes` or `Tested: no` on its own line.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Say how to revert in a line that starts with `Rollback: `.
- Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`.
- Name the affected component in a line `Component: <name>`.
- State whether the change was tested with a line `Tested: yes` or `Tested: no`.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`.
- Explain the motivation in a body line that starts with `Why: `.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
[PAY-311] fix: add retry with backoff to payment webhook

Why: transient gateway timeouts dropped webhook events.
Risk: low
BREAKING CHANGE: none
Tested: yes

- Retry failed webhook deliveries three times
- Use exponential backoff between attempts
Component: webhooks
Rollback: revert this commit
Signed-off-by: Lena Ortiz
Refs: PAY-311
```
