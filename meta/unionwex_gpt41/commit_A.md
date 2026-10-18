---
name: conventional-commits+ticket-first-commits
description: Combined rules of `conventional-commits` and `ticket-first-commits`. Use for any commit message.
---

# Combined skill: conventional-commits + ticket-first-commits

Follow every rule below.

## Rules from `conventional-commits`

- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the type.
- State whether the change was tested with a line `Tested: yes` or `Tested: no`.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`.
- Explain the motivation in a body line that starts with `Why: `.

## Rules from `ticket-first-commits`

- Start the subject line with the ticket ID in square brackets, for example `[PAY-311] `. Nothing may come before the bracket.
- Record test status as `Tested: yes` or `Tested: no` on its own line.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Say how to revert in a line that starts with `Rollback: `.
- Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`.
- Name the affected component in a line `Component: <name>`.

If two rules cannot both hold, the rule from `conventional-commits` wins.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
feat: add retry with backoff to payment webhook handler

Why: To improve reliability of payment processing in case of transient failures.
Risk: low
Tested: yes
- Implemented exponential backoff retry logic in the payment webhook handler
- Updated error handling to trigger retries on specific failure types
BREAKING CHANGE: none
Rollback: Revert this commit to remove retry and restore previous error handling behavior.
Component: webhooks

Refs: PAY-311
Signed-off-by: Lena Ortiz
```
