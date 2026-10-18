---
name: standup-async-thread+standup-manager-digest
description: Merged skill that replaces `standup-async-thread` and `standup-manager-digest`. Use for any daily standup update.
---

# Merged skill: standup-async-thread + standup-manager-digest

This skill replaces `standup-async-thread` and `standup-manager-digest`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `standup-async-thread`

- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.
- The first line must be `Standup <YYYY-MM-DD> | <full name>`
- Report blockers on a line that starts with `Blocked: `
- The very last line must be the hashtag line `#standup #<team>` with the team name in lowercase

## Rules kept unchanged from `standup-manager-digest`

- Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.
- Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.
- Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- List finished work as bullets that start with `- ` under a line that reads exactly `Done:`. Then, on the next line, summarize the workload with `Items: <n> done, <n> planned`.
