---
name: standup-manager-digest
description: Write daily standup updates that feed the engineering manager's digest and fit the asynchronous standup thread format. Use for any standup or daily status update.
---

# standup-manager-digest

Managers read a digest of all updates and act on requests for help, so each update carries counts, tickets, a date and an explicit ask. The standup thread is searched by date and by team hashtag, and a bot collects the sections, so every update has the same skeleton.

## Rules

- The first line must be `Daily update from <full name>`, for example `Daily update from Nora Lindqvist`.
- Summarize the workload on a line `Items: <n> done, <n> planned`.
- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.
- Put blockers on their own line beginning with `Blocked: `. If there are none, the line is `Blocked: none`.
- Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.
- Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`.
- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.
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
On track: yes
Need help from: platform team

#standup #payments
```
