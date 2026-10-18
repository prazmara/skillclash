<skill>
---
name: commit-style-guide
description: Write commit messages in a style that combines Conventional Commits and Ticket-First Commits. Use for any commit message.
---

# commit-style-guide

Commit messages in this repository follow a style that combines Conventional Commits and Ticket-First Commits so that release tooling can parse them and tracker tickets can be traced.

## Rules

- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the type.
- Add a line that starts with `[TICKET-ID] ` and says the tracker ticket ID. Nothing may come before the square brackets.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- State whether the change was tested with a line `Tested: yes` or `Tested: no`.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Say how to revert in a line that starts with `Rollback: `.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`.
- Explain the motivation in a body line that starts with `Why: `.
- Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
fix: [PAY-311] add retry with backoff to payment webhook

Why: transient gateway timeouts dropped webhook events.
Risk: low
BREAKING CHANGE: none
Tested: yes

- Retry failed webhook deliveries three times
- Use exponential backoff between attempts
Rollback: revert this commit

Refs: PAY-311

Signed-off-by: Lena Ortiz
```
</skill>
