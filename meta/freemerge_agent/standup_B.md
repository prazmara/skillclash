---
name: standup-thread-digest
description: Write daily standup updates that feed the engineering manager's digest and keep the skeleton of the team's asynchronous standup thread. Use for any standup or daily status update.
---

# standup-thread-digest

This skill merges `standup-async-thread` and `standup-manager-digest` and replaces both. Managers read a digest of all updates and act on requests for help, so each update carries counts, tickets, a date and an explicit ask. The standup thread is searched by date and by team hashtag, and a bot collects the sections, so every update also keeps the same skeleton.

Every rule of both skills is kept. Where two rules cannot both hold, `standup-manager-digest` wins.

## Rules

- The first line must be `Daily update from <full name>`, for example `Daily update from Nora Lindqvist`. This is the `standup-manager-digest` rule. It overrides the `standup-async-thread` rule that the first line is `Standup <YYYY-MM-DD> | <full name>`, which is not used. So that the date of the update is not lost, give it on the second line as `Date: <YYYY-MM-DD>`.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- Summarize the workload on a line `Items: <n> done, <n> planned`.
- Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.
- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.
- Put blockers on their own line beginning with `Blocked: `. If there are none, the line is `Blocked: none`.
- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- Include the hashtag line `#standup #<team>` with the team name in lowercase, for example `#standup #payments`. It goes directly above the final line.
- Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`. This is the `standup-manager-digest` rule, and it makes this line the very last line. It overrides the part of the `standup-async-thread` rule that makes the hashtag line the very last line: nothing may follow the `Need help from:` line.

## Example

Request: Write the standup update for Nora Lindqvist, 2026-03-10, team Payments. Yesterday: finished the refund API pagination (PAY-518). Today: start the ledger export job (PAY-530), expected done 2026-03-12. Blocker: waiting for staging database credentials from the platform team.

Output:

```
Daily update from Nora Lindqvist
Date: 2026-03-10

Done:
- Finished the refund API pagination (PAY-518)
Next:
- Start the ledger export job (PAY-530)
Items: 1 done, 1 planned
Tickets: PAY-518, PAY-530
ETA: 2026-03-12
Blocked: waiting for staging database credentials from the platform team
On track: yes
#standup #payments
Need help from: platform team
```
