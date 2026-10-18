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

## Rules kept unchanged from `conventional-commits`

- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Explain the motivation in a body line that starts with `Why: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`, followed immediately by the sign-off `Signed-off-by: <author name>` on the very last line. Both the trailer and sign-off must appear in that order, with no intervening content.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
[PAY-311] add retry with backoff to the payment webhook handler

- Implement exponential backoff retry logic for failed webhook deliveries
- Configure maximum of 3 retries with 2x backoff factor
Why: To improve reliability of payment webhook delivery in the face of transient errors
Risk: low
BREAKING CHANGE: none
Tested: yes
Rollback: Remove the retry logic from the webhook handler by reverting the changes in the handler function
Refs: PAY-311
Signed-off-by: Lena Ortiz
```
