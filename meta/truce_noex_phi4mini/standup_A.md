---
name: standup-async-thread+standup-manager-digest
description: Merged skill that replaces `standup-async-thread` and `standup-manager-digest`. Use for any daily standup update.
---

# Merged skill: standup-async-thread + standup-manager-digest

This skill replaces `standup-async-thread` and `standup-manager-digest`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `standup-async-thread`

- Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.
- List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.

## Rules kept unchanged from `standup-manager-digest`

- ETA: <YYYY-MM-DD>

## Reconciled rules (each one satisfies a rule of both skills at once)

- Standup 2026-03-10 | Nora Lindqvist | Daily update from Nora Lindqvist.
- "Report blockers on a line that starts with `Blocked: `, and when nothing blocks you, write `Blocked: none`. For tickets, list them as `Tickets: <ID>, <ID>` in the same output."
- To satisfy both rules, list the finished work as bullets starting with `- ` under a line that reads exactly `Done:`, and include a line that reads "Need help from: <person or team>." after the bullet points.
- Combine the last line with the digest items by ending the output with the digest format followed by the hashtag line, for example: "2 done, 1 planned #standup #payments".
