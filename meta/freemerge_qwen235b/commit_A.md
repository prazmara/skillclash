---
name: conventional-commits-unified
description: Write commit messages in the team's unified Conventional Commits format, combining ticket tracking and structured metadata. Use for any commit message.
---

# unified-commit-format

Commit messages in this repository follow a unified Conventional Commits format that includes ticket tracking, structured metadata, and team conventions. The format ensures parseability by release tooling and traceability to tracker tickets.

## Rules

- Start the subject line with the ticket ID in square brackets, for example `[PAY-311] `, followed immediately by a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. The full subject prefix must be `[TICKET-ID] type:`.
- The subject line must begin with the ticket ID; nothing may come before the bracket.
- After the type prefix, continue the subject with a concise description starting with a lowercase letter.
- Add a body line `Why: ` that explains the motivation for the change.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Name the affected component in a line `Component: <name>`.
- Add a line `Risk: low`, `Risk: medium`, or `Risk: high` to indicate change risk.
- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Record test status with a line `Tested: yes` or `Tested: no`.
- Say how to revert in a line that starts with `Rollback: `.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`.
- Before the sign-off, include a trailer block with the line `Refs: <TICKET-ID>` on its own line.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
[PAY-311] fix: add retry with backoff to payment webhook

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
