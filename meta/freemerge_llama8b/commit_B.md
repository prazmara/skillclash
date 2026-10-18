<skill>
---
name: ticket-first-commits-with-conventional-commits
description: Write commit messages that lead with the tracker ticket and follow Conventional Commits format. Use for any commit message.
---

# ticket-first-commits-with-conventional-commits

Every commit must be traceable to a tracker ticket and follow Conventional Commits format, so the ticket leads the message.

## Rules

- Start the subject line with the ticket ID in square brackets, followed by a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the bracket or the type prefix.
- Record test status as `Tested: yes` or `Tested: no` on its own line.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Say how to revert in a line that starts with `Rollback: `.
- Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`.
- Name the affected component in a line `Component: <name>`.
- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Explain the motivation in a body line that starts with `Why: `.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
[PAY-311] fix: add retry with backoff to payment webhook

- Retry failed webhook deliveries three times
- Use exponential backoff between attempts
Why: transient gateway timeouts dropped webhook events.
Risk: low
BREAKING CHANGE: none
Component: webhooks
Rollback: revert this commit
Tested: yes

Refs: PAY-311
Signed-off-by: Lena Ortiz
```
</skill>
