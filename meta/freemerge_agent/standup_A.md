---
name: standup-thread-digest
description: Write daily standup updates for the team's asynchronous standup thread that also feed the engineering manager's digest. Use for any standup or daily status update.
---

# standup-thread-digest

This skill merges `standup-async-thread` and `standup-manager-digest` and replaces both. The standup thread is searched by date and by team hashtag, and a bot collects the sections, so every update has the same skeleton. Managers read a digest of all updates and act on requests for help, so each update also carries counts, tickets, a date and an explicit ask.

Every rule of both skills is kept. Where two rules cannot both hold, `standup-async-thread` wins.

## Rules

- The first line must be `Standup <YYYY-MM-DD> | <full name>`, for example `Standup 2026-03-10 | Nora Lindqvist`. This is the `standup-async-thread` rule. It overrides the `standup-manager-digest` rule that the first line is `Daily update from <full name>`, which is not used.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- Summarize the workload on a line `Items: <n> done, <n> planned`.
- Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.
- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.
- Report blockers on their own line that starts with `Blocked: `, and write `Blocked: none` when nothing blocks you.
- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- Include the line `Need help from: <person or team>`, or `Need help from: nobody`. It closes the body of the update: it comes after every other field and directly before the hashtag line.
- The very last line must be the hashtag line `#standup #<team>` with the team name in lowercase, for example `#standup #payments`. This is the `standup-async-thread` rule. It overrides the part of the `standup-manager-digest` rule that makes `Need help from:` the finishing line of the update: nothing may follow the hashtag line.

## Example

Request: Write the standup update for Nora Lindqvist, 2026-03-10, team Payments. Yesterday: finished the refund API pagination (PAY-518). Today: start the ledger export job (PAY-530), expected done 2026-03-12. Blocker: waiting for staging database credentials from the platform team.

Output:

```
Standup 2026-03-10 | Nora Lindqvist

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
