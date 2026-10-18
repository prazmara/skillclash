---
name: standup-manager-digest-merged
description: Write daily standup updates that satisfy both the engineering manager's digest and the team's asynchronous standup thread requirements.
---

# standup-manager-digest-merged

This skill writes daily standup updates that fulfill both the engineering manager's digest and the team's asynchronous standup thread requirements. Each update is structured for easy parsing by bots and managers, includes all required counts, tickets, dates, and explicit asks, and is tagged for team visibility.

## Rules

- The first line must be `Daily update from <full name>`, for example `Daily update from Nora Lindqvist`.
- Summarize the workload on a line `Items: <n> done, <n> planned`.
- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.
- Put blockers on their own line beginning with `Blocked: `. If there are none, the line is `Blocked: none`.
- Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.
- Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`.
- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- The very last line must be the hashtag line `#standup #<team>` with the team name in lowercase, for example `#standup #payments`.

## Example

Request: Write the standup update for Nora Lindqvist, 2026-03-10, team Payments. Yesterday: finished the refund API pagination (PAY-518). Today: start the ledger export job (PAY-530), expected done 2026-03-12. Blocker: waiting for staging database credentials from the platform team.

Output:

```
Daily update from Nora Lindqvist

Done:
- Finished the refund API pagination (PAY-518)
Next:
- Start the ledger export job (PAY-530)
Items: 1 done, 1 planned
Tickets: PAY-518, PAY-530
ETA: 2026-03-12
Blocked: waiting for staging database credentials from the platform team
Need help from: platform team
On track: yes

#standup #payments
```
