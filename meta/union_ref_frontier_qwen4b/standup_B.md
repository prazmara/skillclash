<skill>
---
name: standup-manager-digest+standup-async-thread
description: Combined rules of `standup-manager-digest` and `standup-async-thread`. Use for any daily standup update.
---

# Combined skill: standup-manager-digest + standup-async-thread

Follow every rule below.

## Rules from `standup-manager-digest`

- The first line must be `Daily update from <full name>`, for example `Daily update from Nora Lindqvist`.
- Summarize the workload on a line `Items: <n> done, <n> planned`.
- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.
- Put blockers on their own line beginning with `Blocked: `. If there are none, the line is `Blocked: none`.
- Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.
- Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`.

## Rules from `standup-async-thread`

- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- The first line must be `Standup <YYYY-MM-DD> | <full name>`, for example `Standup 2026-03-10 | Nora Lindqvist`.
- Report blockers on a line that starts with `Blocked: `, and write `Blocked: none` when nothing blocks you.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.
- The very last line must be the hashtag line `#standup #<team>` with the team name in lowercase, for example `#standup #payments`.

## Conflict Resolution

If two rules conflict, the rule from `standup-manager-digest` takes precedence for the following:
- The first line must be `Daily update from <full name>`.
- The final line must be `Need help from: <person or team>` or `Need help from: nobody`.

Therefore, the `Standup <date> | <name>` line from `standup-async-thread` is **not** required. Instead, the first line is strictly `Daily update from <full name>`.

The `#standup #team` line must remain at the end as a final line, and the `Need help from` line must appear before it, as per `standup-manager-digest`.

## Final Structure (in order):

1. `Daily update from <full name>`
2. `Items: <n> done, <n> planned`
3. `ETA: <YYYY-MM-DD>`
4. `Blocked: <blocker text>` or `Blocked: none`
5. `Tickets: <ID>, <ID>`
6. `Need help from: <person or team>` or `Need help from: nobody`
7. `On track: yes` or `On track: no`
8. `Next:`
   - <planned task>
9. `Done:`
   - <completed task>
10. `#standup #<team>`

## Example (valid output):

Daily update from Ivan Petrov  
Items: 1 done, 1 planned  
ETA: 2026-03-18  
Blocked: missing internal policy version from legal department  
Tickets: CMP-702, CMP-707  
Need help from: legal department  
On track: yes  
Next:  
- preparing audit documentation (CMP-707)  
Done:  
- reviewed data retention policy (CMP-702)  
#standup #compliance
</skill>
