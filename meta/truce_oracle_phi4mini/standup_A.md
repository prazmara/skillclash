---
name: standup-async-thread+standup-manager-digest
description: Merged skill that replaces `standup-async-thread` and `standup-manager-digest`. Use for any daily standup update.
---

# Merged skill: standup-async-thread + standup-manager-digest

This skill replaces `standup-async-thread` and `standup-manager-digest`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `standup-async-thread`

- The first line must be `Standup <YYYY-MM-DD> | <full name>`, for example `Standup 2026-03-10 | Nora Lindqvist`.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- Report blockers on a line that starts with `Blocked: `, and write `Blocked: none` when nothing blocks you.

## Rules kept unchanged from `standup-manager-digest`

- Summarize the workload on a line `Items: <n> done, <n> planned`.
- Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.
- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- End your update with the hashtag line `#standup #<team>` in lowercase, followed by a line `Need help from: <person or team>`, or `Need help from: nobody`. For example: `#standup #payments Need help from: nobody`.

## Example

Request: Write the standup update for Nora Lindqvist, 2026-03-10, team Payments. Yesterday: finished the refund API pagination (PAY-518). Today: start the ledger export job (PAY-530), expected done 2026-03-12. Blocker: waiting for staging database credentials from the platform team.

Output:

```
Standup 2026-03-10 | Nora Lindqvist
Items: 1 done, 1 planned
Done: - Finished the refund API pagination (PAY-518)
Next: - Start the ledger export job (PAY-530) ETA: 2026-03-12
Blocked: - Waiting for staging database credentials from the platform team
Tickets: PAY-518, PAY-530
On track: no
#standup #payments Need help from: nobody
```
