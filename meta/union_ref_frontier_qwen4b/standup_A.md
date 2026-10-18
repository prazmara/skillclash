<skill>
---
name: standup-async-thread+standup-manager-digest
description: Combined rules of `standup-async-thread` and `standup-manager-digest`. Use for any daily standup update.
---

# Combined skill: standup-async-thread + standup-manager-digest

Follow every rule below.

## Rules from `standup-async-thread`

- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- The first line must be `Standup <YYYY-MM-DD> | <full name>`, for example `Standup 2026-03-10 | Nora Lindqvist`.
- Report blockers on a line that starts with `Blocked: `, and write `Blocked: none` when nothing blocks you.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.
- The very last line must be the hashtag line `#standup #<team>` with the team name in lowercase, for example `#standup #payments`.

## Rules from `standup-manager-digest`

- The first line must be `Daily update from <full name>`, for example `Daily update from Nora Lindqvist`.
- Summarize the workload on a line `Items: <n> done, <n> planned`.
- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.
- Put blockers on their own line beginning with `Blocked: `. If there are none, the line is `Blocked: none`.
- Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.
- Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`.

# Conflict Resolution

If two rules conflict, the rule from `standup-async-thread` takes precedence **only** for the following lines:
- First line: `Standup <YYYY-MM-DD> | <full name>` (from `standup-async-thread`) **overrides** `Daily update from <full name>` (from `standup-manager-digest`).
- The very last line must be `#standup #<team>` (from `standup-async-thread`), which is **final and non-negotiable**.

All other rules from `standup-manager-digest` are **required** and must be satisfied **in addition** to the `standup-async-thread` rules. Specifically:

- The line `Items: <n> done, <n> planned` must be included.
- The line `Tickets: <ID>, <ID>` must include all ticket IDs from both yesterday and today, separated by comma and space.
- The line `ETA: <YYYY-MM-DD>` must be included for the current task.
- The line `Need help from: <person or team>` must be included, or `Need help from: nobody` if none.

# Example (valid output)

Standup 2026-03-11 | Eli Moreno  
On track: yes  
Items: 1 done, 1 planned  
ETA: 2026-03-14  
Tickets: SHI-204, SHI-210  
Next:  
- Implementing real-time shipment updates (SHI-210)  
Done:  
- Resolved the order tracking timeout issue (SHI-204)  
Blocked: API rate limits from the third-party carrier service  
Need help from: engineering team  
#standup #shipping

</skill>
