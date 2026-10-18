---
name: standup-manager-digest+standup-async-thread
description: Merged skill that replaces `standup-manager-digest` and `standup-async-thread`. Use for any daily standup update.
---

# Merged skill: standup-manager-digest + standup-async-thread

This skill replaces `standup-manager-digest` and `standup-async-thread`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `standup-manager-digest`

- The first line must be `Daily update from <full name>`, for example `Daily update from Nora Lindqvist`.
- Summarize the workload on a line `Items: <n> done, <n> planned`.
- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.
- Put blockers on their own line beginning with `Blocked: `. If there are none, the line is `Blocked: none`.
- Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.

## Rules kept unchanged from `standup-async-thread`

- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`, placed directly above the hashtag line as the last line of content. The very last line must be the hashtag line `#standup #<team>` with the team name in lowercase, for example `#standup #payments`, and nothing may come after it.

## Example

Request: Write the standup update for Nora Lindqvist, 2026-03-10, team Payments. Yesterday: finished the refund API pagination (PAY-518). Today: start the ledger export job (PAY-530), expected done 2026-03-12. Blocker: waiting for staging database credentials from the platform team.

Output:

```
Daily update from Nora Lindqvist

Done:
- Finished the refund API pagination
Next:
- Start the ledger export job
Items: 1 done, 1 planned
Tickets: PAY-518, PAY-530
ETA: 2026-03-12
Blocked: waiting for staging database credentials from the platform team
On track: yes
Need help from: platform team
#standup #payments
```
