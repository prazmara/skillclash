---
name: conventional-ticket-commits
description: Write commit messages in the team's Conventional Commits format that stay traceable to the tracker ticket. Use for any commit message.
---

# conventional-ticket-commits

This skill merges `conventional-commits` and `ticket-first-commits` and replaces both. Commit messages in this repository follow Conventional Commits so that release tooling can parse them, and every commit must be traceable to a tracker ticket.

Every rule of both skills is kept. Where two rules cannot both hold, `conventional-commits` wins.

## Rules

- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the type. This is the `conventional-commits` rule. It overrides the `ticket-first-commits` rule that the subject starts with the ticket ID in square brackets with nothing before the bracket. The bracketed ticket ID therefore comes directly after the type prefix, for example `fix: [PAY-311] add retry with backoff to payment webhook`.
- Explain the motivation in a body line that starts with `Why: `.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Name the affected component in a line `Component: <name>`.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Say how to revert in a line that starts with `Rollback: `.
- State whether the change was tested with `Tested: yes` or `Tested: no` on its own line.
- Finish the message with a trailer block, separated from the body by a blank line, that contains the line `Refs: <TICKET-ID>`.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`. It is the last line of the trailer block, directly below the `Refs:` line, so both trailer rules hold.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
fix: [PAY-311] add retry with backoff to payment webhook

Why: transient gateway timeouts dropped webhook events.
- Retry failed webhook deliveries three times
- Use exponential backoff between attempts
Component: webhooks
Risk: low
BREAKING CHANGE: none
Rollback: revert this commit
Tested: yes

Refs: PAY-311
Signed-off-by: Lena Ortiz
```
