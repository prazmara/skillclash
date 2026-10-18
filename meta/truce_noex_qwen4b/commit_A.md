---
name: conventional-commits+ticket-first-commits
description: Merged skill that replaces `conventional-commits` and `ticket-first-commits`. Use for any commit message.
---

# Merged skill: conventional-commits + ticket-first-commits

This skill replaces `conventional-commits` and `ticket-first-commits`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `conventional-commits`

- Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.
- Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the type.
- State whether the change was tested with a line `Tested: yes` or `Tested: no`.

## Rules kept unchanged from `ticket-first-commits`

- Say how to revert in a line that starts with `Rollback: `.
- Name the affected component in a line `Component: <name>`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Add a body line `Risk: low`, `Risk: medium`, or `Risk: high`. Record test status as `Tested: yes` or `Tested: no` on its own line.
- Why: [explanation of motivation] - [description of change] - [additional description of change]
- The very last line of the message must be the sign-off `Signed-off-by: <author name>`, and immediately before it, include a trailer block with the line `Refs: <TICKET-ID>`.
