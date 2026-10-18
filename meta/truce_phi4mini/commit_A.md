---
name: conventional-commits+ticket-first-commits
description: Merged skill that replaces `conventional-commits` and `ticket-first-commits`. Use for any commit message.
---

# Merged skill: conventional-commits + ticket-first-commits

This skill replaces `conventional-commits` and `ticket-first-commits`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `conventional-commits`

- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.

## Rules kept unchanged from `ticket-first-commits`

- Say how to revert in a line that starts with `Rollback: `.
- Name the affected component in a line `Component: <name>`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Start the subject line with the ticket ID in square brackets, followed by a colon and a lowercase type prefix, for example, `[PAY-311]: feat:`. Nothing may come before the bracket or the colon.
- Add a line `Tested: yes` or `Tested: no` to the commit message to satisfy both the `conventional-commits` and `ticket-first-commits` rules.
- To satisfy both rules, end your commit message with the sign-off `Signed-off-by: <author name>` followed by a trailer block containing `Refs: <TICKET-ID>`. The combined rule should look like this: ``` Signed-off-by: <author name> --- Refs: <TICKET-ID> ``` Ensure that the sign-off is the very last line before the trailer block.
- "Start the body with 'Why: ' followed by the motivation, then continue with a bulleted list starting with '- ' for the change description, ensuring both the motivation and the change are clearly presented."

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
[PAY-311]: feat: add retry with backoff to the payment webhook handler. Tested: yes

- Why: Improve reliability of webhook processing by adding retry logic with exponential backoff.
- Change: Implemented a retry mechanism with exponential backoff for the payment webhook handler to handle transient failures more gracefully.

Signed-off-by: Lena Ortiz

Refs: PAY-311
```
