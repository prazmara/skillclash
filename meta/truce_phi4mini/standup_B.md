---
name: standup-manager-digest+standup-async-thread
description: Merged skill that replaces `standup-manager-digest` and `standup-async-thread`. Use for any daily standup update.
---

# Merged skill: standup-manager-digest + standup-async-thread

This skill replaces `standup-manager-digest` and `standup-async-thread`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `standup-manager-digest`

- ETA: <YYYY-MM-DD>

## Rules kept unchanged from `standup-async-thread`

- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Standup <YYYY-MM-DD> | <full name> with a daily update from <full name>.
- "Report blockers on a line that starts with `Blocked: `, and write `Blocked: none` when nothing blocks you, ensuring that each ticket ID is listed on a separate line."
- To satisfy both rules, list the finished work as bullets starting with `- ` under a line that reads exactly `Done:`. Ensure that the bullets are presented immediately after the `Done:` line.
- Combine the output into a single line with the format: "<n> done, <n> planned #standup #<team>", ensuring the team name is in lowercase.

## Example

Request: Write the standup update for Nora Lindqvist, 2026-03-10, team Payments. Yesterday: finished the refund API pagination (PAY-518). Today: start the ledger export job (PAY-530), expected done 2026-03-12. Blocker: waiting for staging database credentials from the platform team.

Output:

```
- On track: yes
- Next:
  - - start the ledger export job (PAY-530)
- Done: 1
- Blocked: none
- 1 done, 1 planned #standup #payments
```
