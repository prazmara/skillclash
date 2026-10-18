---
name: standup-async-thread+standup-manager-digest
description: Merged skill that replaces `standup-async-thread` and `standup-manager-digest`. Use for any daily standup update.
---

# Merged skill: standup-async-thread + standup-manager-digest

This skill replaces `standup-async-thread` and `standup-manager-digest`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `standup-async-thread`

- The first line must be `Standup <YYYY-MM-DD> | <full name>`, for example `Standup 2026-03-10 | Nora Lindqvist`.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.

## Rules kept unchanged from `standup-manager-digest`

- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`
- If there are none, the line is `Blocked: none`
- Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output as follows: "Daily update from <full name>: On track: yes"
- Write the planned work as bulleted items under a line that reads exactly "Next:", followed by a line that reads "Items: <n> done, <n> planned", where "<n>" is replaced with the appropriate number of completed and remaining tasks, respectively. For example: Next: - Task 1 - Task 2 - Task 3 Items: 2 done, 1 planned
- Write the output in the following format: ``` Standup Report: [Your report content here] Blockers: Blocked: [List of blockers, each on a separate line] Blocked: none [If there are no blockers] ```
- Write the output in the following format: `Tickets: <ID>, <ID>, ..., <ID>, #standup #<team>` Replace `<ID>` with the ticket IDs, each separated by a comma and a space, and replace `<team>` with the team name in lowercase.
