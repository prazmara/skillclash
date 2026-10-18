---
name: ticket-first-commits+conventional-commits
description: Merged skill that replaces `ticket-first-commits` and `conventional-commits`. Use for any commit message.
---

# Merged skill: ticket-first-commits + conventional-commits

This skill replaces `ticket-first-commits` and `conventional-commits`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `ticket-first-commits`

- Start the subject line with the ticket ID in square brackets, for example `[PAY-311] `.
- Record test status as `Tested: yes` or `Tested: no` on its own line.
- Say how to revert in a line that starts with `Rollback: `.
- Name the affected component in a line `Component: <name>`.

## Rules kept unchanged from `conventional-commits`

- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`.
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output in the following format: `[type]: <commit message>`, ensuring that the square bracket and the type come first, followed by a colon and a space, and the commit message starts on the next line, indented.
- Write the commit message with the following structure: ``` - Description of change 1 - Description of change 2 Why: Motivation for the changes ``` Ensure that each change is preceded by `- ` and the motivation starts with `Why: `.
- Write the commit message with the following structure: 1. Start with a succinct summary in the imperative mood. 2. Add a blank line. 3. If there are breaking changes, begin a new line with `BREAKING CHANGE:` followed by `none` if no breaking changes occurred. 4. Add another blank line. 5. End with a line starting with `Refs:` followed by a space and the ticket ID.
