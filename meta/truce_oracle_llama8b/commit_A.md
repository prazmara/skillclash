---
name: conventional-commits+ticket-first-commits
description: Merged skill that replaces `conventional-commits` and `ticket-first-commits`. Use for any commit message.
---

# Merged skill: conventional-commits + ticket-first-commits

This skill replaces `conventional-commits` and `ticket-first-commits`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `conventional-commits`

- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the type.
- Explain the motivation in a body line that starts with `Why: `.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- State whether the change was tested with a line `Tested: yes` or `Tested: no`.

## Rules kept unchanged from `ticket-first-commits`

- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Name the affected component in a line `Component: <name>`.
- Say how to revert in a line that starts with `Rollback: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Finish the commit message with a trailer block that contains the lines `Signed-off-by: <author name>` and `Refs: <TICKET-ID>`, one on each line, in that order.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
feat: add retry with backoff to the payment webhook handler
Why: improve payment webhook reliability
Risk: medium
BREAKING CHANGE: none
Tested: yes

- Implement exponential backoff for payment webhook retries
- Add retry logic to the payment webhook handler

Component: webhooks
Rollback: remove the retry logic and exponential backoff from the payment webhook handler

Signed-off-by: Lena Ortiz
Refs: PAY-311
```
