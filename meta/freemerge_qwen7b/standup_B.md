---
name: combined-standup-skill
description: Write daily standup updates that can be used for either the engineering manager's digest or the team's asynchronous standup thread. Use for any standup or daily status update.
---

# combined-standup-skill

This skill combines the requirements for writing standup updates for both the engineering manager's digest and the team's asynchronous standup thread. For the engineering manager's digest, use the rules from `standup-manager-digest`. For the team's asynchronous standup thread, use the rules from `standup-async-thread`. Where both sets of rules conflict, the rule from `standup-manager-digest` takes precedence.

## Rules

- **For the engineering manager's digest:**
  - The first line must be `Daily update from <full name>`, for example `Daily update from Nora Lindqvist`.
  - Summarize the workload on a line `Items: <n> done, <n> planned`.
  - Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.
  - Put blockers on their own line beginning with `Blocked: `. If there are none, the line is `Blocked: none`.
  - Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.
  - Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`.

- **For the team's asynchronous standup thread:**
  - Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
  - List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
  - The first line must be `Standup <YYYY-MM-DD> | <full name>`, for example `Standup 2026-03-10 | Nora Lindqvist`.
  - Report blockers on a line that starts with `Blocked: `, and write `Blocked: none` when nothing blocks you.
  - List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.
  - The very last line must be the hashtag line `#standup #<team>` with the team name in lowercase, for example `#standup #payments`.

## Example

Request: Write the standup update for Nora Lindqvist, 2026-03-10, team Payments. Yesterday: finished the refund API pagination (PAY-518). Today: start the ledger export job (PAY-530), expected done 2026-03-12. Blocker: waiting for staging database credentials from the platform team.

Output:

```
Daily update from Nora Lindqvist

Yesterday I finished the refund API pagination. Today I am starting the ledger export job.
Items: 1 done, 1 planned
ETA: 2026-03-12
Blocked: waiting for staging database credentials from the platform team
Need help from: platform team
```

Alternatively, if the request specifies the team's asynchronous standup thread:

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
