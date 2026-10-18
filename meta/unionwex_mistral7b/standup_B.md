---
name: standup-manager-digest+standup-async-thread
description: Combined rules of `standup-manager-digest` and `standup-async-thread`. Use for any daily standup update.
---

# Combined skill: standup-manager-digest + standup-async-thread

Follow every rule below.

## Rules from `standup-manager-digest`

- The first line must be `Daily update from <full name>`, for example `Daily update from Nora Lindqvist`.
- Summarize the workload on a line `Items: <n> done, <n> planned`.
- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.
- Put blockers on their own line beginning with `Blocked: `. If there are none, the line is `Blocked: none`.
- Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.
- Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`.

## Rules from `standup-async-thread`

- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- The first line must be `Standup <YYYY-MM-DD> | <full name>`, for example `Standup 2026-03-10 | Nora Lindqvist`.
- Report blockers on a line that starts with `Blocked: `, and write `Blocked: none` when nothing blocks you.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.
- The very last line must be the hashtag line `#standup #<team>` with the team name in lowercase, for example `#standup #payments`.

If two rules cannot both hold, the rule from `standup-manager-digest` wins.

## Example

Request: Write the standup update for Nora Lindqvist, 2026-03-10, team Payments. Yesterday: finished the refund API pagination (PAY-518). Today: start the ledger export job (PAY-530), expected done 2026-03-12. Blocker: waiting for staging database credentials from the platform team.

Output:

```
Standup 2026-03-10 | Nora Lindqvist

Daily update from Nora Lindqvist: On track: yes
Items: 1, 1
Next:
- Start the ledger export job (PAY-530)
- Expected finish: 2026-03-12

Done:
- Refund API pagination (PAY-518)

Blocked:
- Waiting for staging database credentials from the platform team

Tickets: PAY-518, PAY-530
#standup #payments
```
