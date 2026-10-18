---
name: ticket-first-commits+conventional-commits
description: Merged skill that replaces `ticket-first-commits` and `conventional-commits`. Use for any commit message.
---

# Merged skill: ticket-first-commits + conventional-commits

This skill replaces `ticket-first-commits` and `conventional-commits`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `ticket-first-commits`

- Start the subject line with the ticket ID in square brackets, for example `[PAY-311] `. Nothing may come before the bracket.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Name the affected component in a line `Component: <name>`.
- Say how to revert in a line that starts with `Rollback: `.
- Record test status as `Tested: yes` or `Tested: no` on its own line.

## Rules kept unchanged from `conventional-commits`

- Explain the motivation in a body line that starts with `Why: `.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the message in the following format: `<commit message> Refs: <TICKET-ID> Signed-off-by: <author name>`

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
[PAY-311] Add retry with backoff to the payment webhook handler.

Why: To improve the reliability of the payment webhook handling.

Risk: Medium

BREAKING CHANGE: none

Tested: yes

Refs: PAY-311 Signed-off-by: Lena Ortiz
```
