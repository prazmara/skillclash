---
name: standup-manager-digest+standup-async-thread
description: Merged skill that replaces `standup-manager-digest` and `standup-async-thread`. Use for any daily standup update.
---

# Merged skill: standup-manager-digest + standup-async-thread

This skill replaces `standup-manager-digest` and `standup-async-thread`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `standup-manager-digest`

- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`
- If there are none, the line is `Blocked: none`
- Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`

## Rules kept unchanged from `standup-async-thread`

- The first line must be `Standup <YYYY-MM-DD> | <full name>`, for example `Standup 2026-03-10 | Nora Lindqvist`.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output as follows: "Daily update from <full name>: On track: [yes/no]"
- Write the output in the following format: ``` Items: <number of completed tasks>, <number of planned tasks> Next: - <task 1> - <task 2> ... ```
- Write the output in the following format: ``` If there are blockers, start each blocker on a new line, prefixed with "Blocked: ", and list them in order. If there are no blockers, write "Blocked: none" on a new line, prefixed with "Blocked: ". ```
- Write the output in the following format: "Tickets: <ID>, <ID>, ..., <ID>\n#standup #<team>" where <ID> represents the ticket IDs, separated by a comma and a space, and <team> is the team name in lowercase.

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
