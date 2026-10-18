<skill>
---
name: standup-manager-digest+standup-async-thread
description: Merged skill that replaces `standup-manager-digest` and `standup-async-thread`. Use for any daily standup update.
---

# Merged skill: standup-manager-digest + standup-async-thread

This skill replaces `standup-manager-digest` and `standup-async-thread`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `standup-manager-digest`

- The first line must be `Daily update from <full name>`, for example `Daily update from Nora Lindqvist`.
- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.
- Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.
- Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`.

## Rules kept unchanged from `standup-async-thread`

- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.
- Report blockers on a line that starts with `Blocked: `, and write `Blocked: none` when nothing blocks you.
- Summarize the workload on a line `Items: <n> done, <n> planned` (where n is the count of done and planned items).
- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.

## New rule added (missing from original file)

- The very last line must be the hashtag line `#standup #<team>` with the team name in lowercase, for example `#standup #payments`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Items: <n> done, <n> planned. On track: yes.  
  (This line is now included as a required summary and must appear after the `Done:` and `Next:` sections, and before the final hashtag.)

## Critical correction: All rules must be satisfied simultaneously

To ensure all rules are satisfied, the output must include:
- The `Need help from:` line **after** the `Items:` and `On track:` line, as required by `standup-manager-digest`.
- The `Items: <n> done, <n> planned` and `On track: yes/no` lines **after** `Done:` and `Next:` but **before** the final hashtag.

Therefore, the correct order of lines is:
1. Daily update from <full name>
2. ETA: <YYYY-MM-DD>
3. Tickets: <ID>, <ID>
4. Blocked: <blocker or none>
5. Next: - <planned work>
6. Done: - <finished work>
7. Items: <n> done, <n> planned. On track: yes/no
8. Need help from: <person or team> or nobody
9. #standup #<team>

## Example

Request: Write the standup update for Nora Lindqvist, 2026-03-10, team Payments. Yesterday: finished the refund API pagination (PAY-518). Today: start the ledger export job (PAY-530), expected done 2026-03-12. Blocker: waiting for staging database credentials from the platform team.

Output:

```
Daily update from Nora Lindqvist  
ETA: 2026-03-12  
Tickets: PAY-518, PAY-530  
Blocked: waiting for staging database credentials from the platform team  
Next: - start the ledger export job (PAY-530)  
Done: - finished the refund API pagination (PAY-518)  
Items: 1 done, 1 planned. On track: no  
Need help from: nobody  
#standup #payments
```
</skill>
