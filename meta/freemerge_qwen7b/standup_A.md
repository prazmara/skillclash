<skill>
---
name: combined-standup-skill
description: Write daily standup updates for the team's asynchronous standup thread and for the engineering manager's digest. Use for any standup or daily status update.
---

# combined-standup-skill

This skill combines the rules for writing standup updates for the team's asynchronous standup thread and for the engineering manager's digest. In case of conflict, the rules from `standup-async-thread` take precedence.

## Rules

- The first line must be either `Standup <YYYY-MM-DD> | <full name>` or `Daily update from <full name>`, depending on the context.
- Summarize the workload on a line `Items: <n> done, <n> planned` if it's for the engineering manager's digest.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- The first line must be `Standup <YYYY-MM-DD> | <full name>` or `Daily update from <full name>`, for example `Standup 2026-03-10 | Nora Lindqvist` or `Daily update from Nora Lindqvist`.
- Report blockers on a line that starts with `Blocked: `, and write `Blocked: none` when nothing blocks you.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.
- The very last line must be the hashtag line `#standup #<team>` with the team name in lowercase, for example `#standup #payments`.
- Summarize the workload on a line `Items: <n> done, <n> planned` if it's for the engineering manager's digest.
- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>` if it's for the engineering manager's digest.
- Finish the update with a line `Need help from: <person or team>` or `Need help from: nobody` if it's for the engineering manager's digest.

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

#standup #payments
```

Request: Write the standup update for Nora Lindqvist, 2026-03-10, team Payments. Yesterday: finished the refund API pagination (PAY-518). Today: start the ledger export job (PAY-530), expected done 2026-03-12. Blocker: waiting for staging database credentials from the platform team. Need help from: platform team.

Output:

```
Daily update from Nora Lindqvist

Yesterday I finished the refund API pagination. Today I am starting the ledger export job.
Items: 1 done, 1 planned
ETA: 2026-03-12
Blocked: waiting for staging database credentials from the platform team
Need help from: platform team
```
</skill>
