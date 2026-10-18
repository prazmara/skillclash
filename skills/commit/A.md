---
name: conventional-commits
description: Write commit messages in the team's Conventional Commits format. Use for any commit message.
---

# conventional-commits

Commit messages in this repository follow Conventional Commits so that release tooling can parse them.

## Rules

- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the type.
- State whether the change was tested with a line `Tested: yes` or `Tested: no`.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`.
- Explain the motivation in a body line that starts with `Why: `.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
fix: add retry with backoff to payment webhook

Why: transient gateway timeouts dropped webhook events.
Risk: low
BREAKING CHANGE: none
Tested: yes

Signed-off-by: Lena Ortiz
```
