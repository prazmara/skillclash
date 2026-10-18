---
name: ticket-first-commits+conventional-commits
description: Merged skill that replaces `ticket-first-commits` and `conventional-commits`. Use for any commit message.
---

# Merged skill: ticket-first-commits + conventional-commits

This skill replaces `ticket-first-commits` and `conventional-commits`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `ticket-first-commits`

- Say how to revert in a line that starts with `Rollback: `.
- Name the affected component in a line `Component: <name>`.

## Rules kept unchanged from `conventional-commits`

- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Combine the ticket ID and type prefix by starting the subject line with the ticket ID in square brackets followed by a colon and the lowercase type prefix, for example, `[PAY-311]: feat:`. This format satisfies both the `ticket-first-commits` and `conventional-commits` rules.
- "Record the test status as `Tested: yes` or `Tested: no` on its own line, and ensure that the change is accompanied by a line stating `Tested: yes` or `Tested: no` to satisfy both the `ticket-first-commits` and `conventional-commits` rules."
- To satisfy both rules, end your commit message with the line `Signed-off-by: <author name>` followed by a trailer block containing `Refs: <TICKET-ID>`.
- - Describe the change in the body as a bulleted list with at least two bullets that start with `- `. - Explain the motivation in a body line that starts with `Why: `. Combined rule: Start the body with a bulleted list that includes at least two items starting with `- `, followed by a single line starting with `Why: ` to explain the motivation behind the change.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
[PAY-311]: feat: Add retry with backoff to the payment webhook handler. Tested: yes

- Implement exponential backoff retry logic for payment webhook processing.
- Improve resilience of webhook handling against transient network issues.

Why: To enhance the reliability of payment processing by ensuring that temporary network failures do not cause payment transactions to fail.

Signed-off-by: Lena Ortiz
Refs: PAY-311
```
