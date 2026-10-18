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

- Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`, and ensure the very last line of the message is the sign-off `Signed-off-by: <author name>`. Place the `Signed-off-by: <author name>` line immediately after the `Refs: <TICKET-ID>` line within the trailer block.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
[PAY-311] feat: add retry with backoff to payment webhook handler

Tested: yes

- Implemented retry logic with exponential backoff for the payment webhook handler.
- Improved resilience against transient network or service errors during webhook processing.
- Updated error handling to log failed attempts and escalate after max retries.
- Added configuration options for max retries and backoff intervals.

Rollback: Revert the changes in the webhook handler to remove retry and backoff logic.
Component: webhooks
BREAKING CHANGE: none
Risk: low
Why: To reduce failed webhook deliveries due to temporary issues and improve overall reliability.

Refs: PAY-311
Signed-off-by: Lena Ortiz
```
