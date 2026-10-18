---
name: standup-async-thread-manager-digest
description: Write daily standup updates that satisfy both the team's asynchronous standup thread and the engineering manager's digest. Use for any standup or daily status update.
---

# standup-async-thread-manager-digest

This skill writes daily standup updates that fulfill the requirements of both the team's asynchronous standup thread and the engineering manager's digest. Every update follows a strict skeleton for bot collection and manager review.

## Rules

- The first line must be `Standup <YYYY-MM-DD> | <full name>`, for example `Standup 2026-03-10 | Nora Lindqvist`.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- Report blockers on a line that starts with `Blocked: `, and write `Blocked: none` when nothing blocks you.
- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- Summarize the workload on a line `Items: <n> done, <n> planned`.
- Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space. If there are no tickets, write `Tickets: none`.
- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`. If unknown, write `ETA: unknown`.
- Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`.
- The very last line must be the hashtag line `#standup #<team>` with the team name in lowercase, for example `#standup #payments`.

## Example

Request: Write the standup update for Nora Lindqvist, 2026-03-10, team Payments. Yesterday: finished the refund API pagination (PAY-518). Today: start the ledger export job (PAY-530), expected done 2026-03-12. Blocker: waiting for staging database credentials from the platform team.

Output:

```
Standup 2026-03-10 | Nora Lindqvist

Done:
- Finished the refund API pagination (PAY-518)
Next:
- Start the ledger export job (PAY-530)
Blocked: waiting for staging database credentials from the platform team
On track: yes
Items: 1 done, 1 planned
Tickets: PAY-518, PAY-530
ETA: 2026-03-12
Need help from: platform team

#standup #payments
```
