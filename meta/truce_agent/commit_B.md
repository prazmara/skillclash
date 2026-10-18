---
name: ticket-first-commits+conventional-commits
description: Merged skill that replaces `ticket-first-commits` and `conventional-commits`. Use for any commit message.
---

# Merged skill: ticket-first-commits + conventional-commits

This skill replaces `ticket-first-commits` and `conventional-commits`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `ticket-first-commits`

- Start the subject line with the ticket ID in square brackets, for example `[PAY-311] `. Nothing may come before the bracket.
- Record test status as `Tested: yes` or `Tested: no` on its own line.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Say how to revert in a line that starts with `Rollback: `.
- Name the affected component in a line `Component: <name>`.

## Rules kept unchanged from `conventional-commits`

- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Explain the motivation in a body line that starts with `Why: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Finish the message with a trailer block, set off from the body by a blank line, that contains the line `Refs: <TICKET-ID>` and, directly below it, the sign-off `Signed-off-by: <author name>`. The sign-off must be the very last line of the message, so `Refs:` goes above it and nothing may come after it.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
[PAY-311] Add retry with backoff to payment webhook handler

Why: transient failures dropped payment webhook events.

- Retry failed deliveries in the payment webhook handler
- Back off between retry attempts

Component: webhooks
Risk: low
BREAKING CHANGE: none
Rollback: revert this commit
Tested: yes

Refs: PAY-311
Signed-off-by: Lena Ortiz
```
