---
name: conventional-commits-with-ticket
description: Write commit messages that follow Conventional Commits and include tracker ticket information. Use for any commit message.
---

# conventional-commits-with-ticket

Commit messages in this repository must follow the Conventional Commits format and include tracker ticket information for traceability.

## Rules

- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the type.
- Immediately after the type prefix, include the ticket ID in square brackets, e.g., `fix: [PAY-311] add retry with backoff to payment webhook`.
- Add a body line that starts with `Why: ` to explain the motivation for the change.
- Add a body line `Risk: low`, `Risk: medium`, or `Risk: high`.
- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- State whether the change was tested with a line `Tested: yes` or `Tested: no`.
- Name the affected component in a line `Component: <name>`.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Say how to revert in a line that starts with `Rollback: `.
- Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
fix: [PAY-311] add retry with backoff to payment webhook

Why: transient gateway timeouts dropped webhook events.
- Retry failed webhook deliveries three times
- Use exponential backoff between attempts
Component: webhooks
Risk: low
BREAKING CHANGE: none
Tested: yes
Rollback: revert this commit

Refs: PAY-311
Signed-off-by: Lena Ortiz
```
