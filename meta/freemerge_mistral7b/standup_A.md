<skill>
---
name: standup-async-thread-manager-digest
description: Write daily standup updates for the team's asynchronous standup thread and the engineering manager's digest. Use for any standup or daily status update.
---

# standup-async-thread-manager-digest

The standup thread is searched by date and by team hashtag, and a bot collects the sections, so every update has the same skeleton. Managers read a digest of all updates and act on requests for help, so each update carries counts, tickets, a date and an explicit ask.

## Rules

- The first line must be `Standup <YYYY-MM-DD> | <full name>`, for example `Standup 2026-03-10 | Nora Lindqvist`.
- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- The first line must be `Daily update from <full name>`, for example `Daily update from Nora Lindqvist`.
- Summarize the workload on a line `Items: <n> done, <n> planned`.
- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.
- Put blockers on their own line beginning with `Blocked: `. If there are none, the line is `Blocked: none`.
- Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.
- Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`.

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

Daily update from Nora Lindqvist

Yesterday I finished the refund API pagination. Today I am starting the ledger export job.
Items: 1 done, 1 planned
Tickets: PAY-518, PAY-530
ETA: 2026-03-12
Blocked: waiting for staging database credentials from the platform team
Need help from: platform team

#standup #payments
```
</skill>
