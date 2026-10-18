---
name: conventional-commits+ticket-first-commits
description: Merged skill that replaces `conventional-commits` and `ticket-first-commits`. Use for any commit message.
---

# Merged skill: conventional-commits + ticket-first-commits

This skill replaces `conventional-commits` and `ticket-first-commits`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `conventional-commits`

- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the type.
- State whether the change was tested with a line `Tested: yes` or `Tested: no`.
- Explain the motivation in a body line that starts with `Why: `.

## Rules kept unchanged from `ticket-first-commits`

- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Say how to revert in a line that starts with `Rollback: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`, and ensure the very last line of the message is the sign-off `Signed-off-by: <author name>`.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
feat: add retry with backoff to payment webhook handler
Why: To improve reliability of payment webhook processing by handling transient failures gracefully.
Risk: medium
Tested: yes
BREAKING CHANGE: none
- Added exponential backoff retry logic with configurable attempts and delay
- Integrated retry mechanism into the payment webhook handler to handle network or service interruptions
Rollback: Remove the retry logic from the payment webhook handler and revert to the previous implementation
Refs: PAY-311
Signed-off-by: Lena Ortiz
```
