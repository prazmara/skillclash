---
name: ticket-first-commits+conventional-commits
description: Merged skill that replaces `ticket-first-commits` and `conventional-commits`. Use for any commit message.
---

# Merged skill: ticket-first-commits + conventional-commits

This skill replaces `ticket-first-commits` and `conventional-commits`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `ticket-first-commits`

- Start the subject line with the ticket ID in square brackets, for example `[PAY-311] `. Nothing may come before the bracket.
- Say how to revert in a line that starts with `Rollback: `.
- Name the affected component in a line `Component: <name>`.

## Rules kept unchanged from `conventional-commits`

- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- State whether the change was tested with a line `Tested: yes` or `Tested: no`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Record test status as `Tested: yes` or `Tested: no` on its own line. Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- - Describe the change in the body as a bulleted list with at least two bullets that start with `- `. - Why: [motivation for the change]
- Finish the message with a trailer block containing the line `Refs: <TICKET-ID>`, and ensure the very last line of the message is the sign-off `Signed-off-by: <author name>`.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
[PAY-311] add retry with backoff to the payment webhook handler

- Why: To improve reliability of payment webhook processing by handling transient failures.
- Why: Prevents service outages due to temporary network issues or rate limiting.

Risk: medium  
Tested: yes  
Breaks: none  
Rollback: Remove retry logic and revert to direct webhook processing  
Component: webhooks  
Refs: PAY-311  
Signed-off-by: Lena Ortiz
```
