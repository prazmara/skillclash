---
name: ticket-first-conventional-commits
description: Write commit messages that combine ticket-first traceability with Conventional Commits structure. Use for any commit message.
---

# ticket-first-conventional-commits

Commit messages must be traceable to a tracker ticket and follow Conventional Commits format for tooling. The ticket ID takes precedence in the subject line.

## Rules

- Start the subject line with the ticket ID in square brackets, followed immediately by a Conventional Commits type prefix and colon, e.g., `[PAY-311] fix: `. Nothing may come before the bracket.
- The subject line must begin with `[<TICKET-ID>] ` and then one of: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Include a body line that starts with `Why: ` to explain the motivation.
- Include a body line `Risk: low`, `Risk: medium`, or `Risk: high`.
- Add a line that starts with `BREAKING CHANGE: ` and state `none` if no breaking change exists.
- Name the affected component in a line `Component: <name>`.
- Say how to revert in a line that starts with `Rollback: `.
- Record test status as `Tested: yes` or `Tested: no` on its own line.
- Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`.
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
Component: webhooks
BREAKING CHANGE: none
Rollback: revert this commit
Tested: yes

Refs: PAY-311
Signed-off-by: Lena Ortiz
```
