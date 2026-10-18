<skill>
---
name: standup-async-thread+standup-manager-digest
description: Merged skill that replaces `standup-async-thread` and `standup-manager-digest`. Use for any daily standup update.
---

# Merged skill: standup-async-thread + standup-manager-digest

This skill replaces `standup-async-thread` and `standup-manager-digest`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `standup-async-thread`

- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- The first line must be `Standup <YYYY-MM-DD> | <full name>`, for example `Standup 2026-03-10 | Nora Lindqvist`.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.
- The very last line must be the hashtag line `#standup #<team>` with the team name in lowercase, for example `#standup #payments`.

## Rules kept unchanged from `standup-manager-digest`

- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.
- Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.
- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`. Summarize the workload on a line `Items: <n> done, <n> planned`.
- Report blockers on a line that starts with `Blocked: `, and write `Blocked: none` when nothing blocks you.
- Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The `Need help from` line must appear exactly once, at the end of the update, immediately before the hashtag line.

## Example

Request: Write the standup update for Nora Lindqvist, 2026-03-10, team Payments. Yesterday: finished the refund API pagination (PAY-518). Today: start the ledger export job (PAY-530), expected done 2026-03-12. Blocker: waiting for staging database credentials from the platform team. Need help from: platform team.

Output:

```
Standup 2026-03-10 | Nora Lindqvist
ETA: 2026-03-12
Tickets: PAY-518, PAY-530
On track: yes
Items: 1 done, 1 planned
Blocked: waiting for staging database credentials from the platform team
Next:
- start the ledger export job (PAY-530)
Done:
- finished the refund API pagination (PAY-518)
Need help from: platform team
#standup #payments
```
</skill>
