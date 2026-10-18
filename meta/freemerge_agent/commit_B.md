---
name: conventional-ticket-commits
description: Write commit messages that lead with the tracker ticket and keep the team's Conventional Commits fields. Use for any commit message.
---

# conventional-ticket-commits

This skill merges `conventional-commits` and `ticket-first-commits` and replaces both. Every commit must be traceable to a tracker ticket, so the ticket leads the message. The message also carries the Conventional Commits fields that the release tooling reads.

Every rule of both skills is kept. Where two rules cannot both hold, `ticket-first-commits` wins.

## Rules

- Start the subject line with the ticket ID in square brackets, for example `[PAY-311] `. Nothing may come before the bracket. This is the `ticket-first-commits` rule. It overrides the `conventional-commits` rule that the subject starts with the type prefix with nothing before the type. The lowercase type prefix and its colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`, therefore comes directly after the bracketed ticket ID, for example `[PAY-311] fix: add retry with backoff to payment webhook`.
- Explain the motivation in a body line that starts with `Why: `.
- Describe the change in the body as a bulleted list with at least two bullets that start with `- `.
- Name the affected component in a line `Component: <name>`.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Say how to revert in a line that starts with `Rollback: `.
- Record test status as `Tested: yes` or `Tested: no` on its own line.
- Finish the message with a trailer block, separated from the body by a blank line, that contains the line `Refs: <TICKET-ID>`.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`. It is the last line of the trailer block, directly below the `Refs:` line, so both trailer rules hold.

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
[PAY-311] fix: add retry with backoff to payment webhook

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
