---
name: standup-async-thread+standup-manager-digest
description: Merged skill that replaces `standup-async-thread` and `standup-manager-digest`. Use for any daily standup update.
---

# Merged skill: standup-async-thread + standup-manager-digest

This skill replaces `standup-async-thread` and `standup-manager-digest`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `standup-async-thread`

- The first line must be `Standup <YYYY-MM-DD> | <full name>`, for example `Standup 2026-03-10 | Nora Lindqvist`.
- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- Report blockers on a line that starts with `Blocked: `, and write `Blocked: none` when nothing blocks you.

## Rules kept unchanged from `standup-manager-digest`

- Summarize the workload on a line `Items: <n> done, <n> planned`.
- Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.
- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output in the following format: 1. Start with the team name followed by a space, then the word "standup" and a hash symbol (e.g. "#payments standup"). 2. Provide the update details. 3. End with a space, then the phrase "Need help from:" followed by either a specific person or team name, or the phrase "nobody" (e.g. "Need help from: john_doe" or "Need help from: nobody"). 4. Ensure the final line is formatted as "#standup #<team> \n <update details> \n Need help from: <person or team>".
