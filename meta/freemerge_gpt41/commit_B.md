---
name: ticket-conventional-commits
description: Write commit messages that lead with the tracker ticket and follow all ticket-first-commits and Conventional Commits rules. Use for any commit message.
---

# ticket-conventional-commits

Commit messages must be traceable to a tracker ticket and follow Conventional Commits conventions, with the ticket ID leading the subject line.

## Rules

- Start the subject line with the ticket ID in square brackets, for example `[PAY-311] `. Nothing may come before the bracket.
- After the ticket ID, add a Conventional Commits type prefix in lowercase, followed by a colon and a space, e.g. `[PAY-311] fix: `.
- The subject line must summarize the change.
- Record test status as `Tested: yes` or `Tested: no` on its own line.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Name the affected component in a line `Component: <name>`.
- Say how to revert in a line that starts with `Rollback: `.
- Add a body line that starts with `Why: ` to explain the motivation.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
[PAY-311] fix: add retry with backoff to payment webhook

- Retry failed webhook deliveries three times
- Use exponential backoff between attempts
Component: webhooks
Rollback: revert this commit
Why: transient gateway timeouts dropped webhook events.
Risk: low
BREAKING CHANGE: none
Tested: yes

Refs: PAY-311
Signed-off-by: Lena Ortiz
```
