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

- To satisfy both rules, end your commit message with the line `Signed-off-by: <author name>` followed by a trailer block containing `Refs: <TICKET-ID>`.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
[PAY-311] Add retry with backoff to the payment webhook handler.

- Implement exponential backoff retry logic for transient failures.
- Update webhook handler to include retry mechanism.

Component: webhooks
Risk: low
BREAKING CHANGE: none

Tested: yes

Signed-off-by: Lena Ortiz

Refs: PAY-311
```
