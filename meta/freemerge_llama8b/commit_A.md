<skill>
---
name: conventional-ticket-commits
description: Write commit messages in the team's Conventional Commits format, leading with the tracker ticket. Use for any commit message.
---

# conventional-ticket-commits

Commit messages in this repository follow Conventional Commits so that release tooling can parse them, and every commit must be traceable to a tracker ticket.

## Rules

- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`, followed by the ticket ID in square brackets, for example `fix: [PAY-311]`. Nothing may come before the type or the bracket.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- State whether the change was tested with a line `Tested: yes` or `Tested: no`.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Say how to revert in a line that starts with `Rollback: `.
- Explain the motivation in a body line that starts with `Why: `.
- Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`.
- Name the affected component in a line `Component: <name>`.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
fix: [PAY-311] add retry with backoff to payment webhook

Why: transient gateway timeouts dropped webhook events.
Risk: low
BREAKING CHANGE: none
- Retry failed webhook deliveries three times
- Use exponential backoff between attempts
Component: webhooks
Rollback: revert this commit
Tested: yes

Refs: PAY-311
Signed-off-by: Lena Ortiz
```
