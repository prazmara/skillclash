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

## Reconciled rules (each one satisfies a rule of both skills at once)

- Items: <n> done, <n> planned. On track: yes.
- Report blockers on a line that starts with `Blocked: `, and write `Blocked: none` when nothing blocks you.
