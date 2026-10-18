---
name: conventional-commits+ticket-first-commits
description: Merged skill that replaces `conventional-commits` and `ticket-first-commits`. Use for any commit message.
---

# Merged skill: conventional-commits + ticket-first-commits

This skill replaces `conventional-commits` and `ticket-first-commits`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `conventional-commits`

- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`.
- Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.
- State whether the change was tested with a line `Tested: yes` or `Tested: no`.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`.

## Rules kept unchanged from `ticket-first-commits`

- Start the subject line with the ticket ID in square brackets, for example `[PAY-311] `.
- Say how to revert in a line that starts with `Rollback: `.
- Name the affected component in a line `Component: <name>`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write commit messages with the format: "[<ticket-number>] <type>: <subject>". Ensure that the type is the first element without any preceding text.
- Write a commit message with the following structure: ``` Why: Describe the motivation for this change in one sentence. - Bullet point 1: Briefly describe the change made in the first part of the bullet. - Bullet point 2: Briefly describe the change made in the second part of the bullet. ``` Ensure that the message adheres to the conventional commits format and includes a ticket number if applicable.
- Write the commit message with the following format: `BREAKING CHANGE: none <Your detailed commit message> Refs: <TICKET-ID>`

## Example

Request: Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.

Output:

```
[PAY-311] fix: add retry with backoff to the payment webhook handler

Why: Implement retry mechanism with backoff for the payment webhook handler to improve reliability.
- Bullet point 1: Added a retry mechanism to the payment webhook handler.
- Bullet point 2: Implemented backoff strategy to prevent excessive retries.

Risk: medium
Tested: yes
Signed-off-by: Lena Ortiz

Rollback: Remove the retry mechanism and backoff strategy from the payment webhook handler.
Component: webhooks
Refs: PAY-311

BREAKING CHANGE: none
```
