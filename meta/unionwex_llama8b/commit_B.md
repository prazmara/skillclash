---
name: ticket-first-commits+conventional-commits
description: Combined rules of `ticket-first-commits` and `conventional-commits`. Use for any commit message.
---

# Combined skill: ticket-first-commits + conventional-commits

Follow every rule below.

## Rules from `ticket-first-commits`

- Start the subject line with the ticket ID in square brackets, for example `[PAY-311] `. Nothing may come before the bracket.
- Record test status as `Tested: yes` or `Tested: no` on its own line.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Say how to revert in a line that starts with `Rollback: `.
- Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`.
- Name the affected component in a line `Component: <name>`.

## Rules from `conventional-commits`

- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the type.
- State whether the change was tested with a line `Tested: yes` or `Tested: no`.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`.
- Explain the motivation in a body line that starts with `Why: `.

If two rules cannot both hold, the rule from `ticket-first-commits` wins.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
[PAY-311] feat: add retry with backoff to the payment webhook handler

- Implement exponential backoff with retries for payment webhook handler
- Update error handling to include retry logic

Tested: yes

Rollback: Remove the retry logic and revert to previous error handling

Component: webhooks

BREAKING CHANGE: none

Risk: low

Why: Improve payment webhook reliability

Refs: PAY-311

Signed-off-by: Lena Ortiz
```
