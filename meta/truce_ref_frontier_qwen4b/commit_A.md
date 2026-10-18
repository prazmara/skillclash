<skill>
---
name: conventional-commits+ticket-first-commits
description: Merged skill that replaces `conventional-commits` and `ticket-first-commits`. Use for any commit message.
---

# Merged skill: conventional-commits + ticket-first-commits

This skill replaces `conventional-commits` and `ticket-first-commits`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `conventional-commits`

- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the type.
- State whether the change was tested with a line `Tested: yes` or `Tested: no`.

## Rules kept unchanged from `ticket-first-commits`

- Say how to revert in a line that starts with `Rollback:`.
- Name the affected component in a line `Component: <name>`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Add a body line `Risk: low`, `Risk: medium`, or `Risk: high`. Record test status as `Tested: yes` or `Tested: no` on its own line.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`, and immediately before it, include a trailer block with the line `Refs: <TICKET-ID>`.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
fix: add retry with backoff to the payment webhook handler
BREAKING CHANGE: none
Why: [motivation to improve reliability of payment webhook processing] - [implement exponential backoff for failed webhook requests] - [reduce failure rate by allowing retries on transient network issues]
Risk: medium
Tested: yes
Rollback: revert the retry logic by removing backoff and setting a fixed timeout for payment webhook handler
Component: webhooks
Refs: PAY-311
Signed-off-by: Lena Ortiz
```
</skill>
