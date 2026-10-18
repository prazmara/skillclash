---
name: support-friendly+support-formal
description: Merged skill that replaces `support-friendly` and `support-formal`. Use for any support reply.
---

# Merged skill: support-friendly + support-formal

This skill replaces `support-friendly` and `support-formal`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `support-friendly`

- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL.
- Open with `Hi <first name>!` on the first line.

## Rules kept unchanged from `support-formal`

- Cite the case as `Ticket #<number>`.
- Do not use contractions such as `don't`, `we'll` or `you're`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`, then provide the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Close with the agent's first name followed by a line ending in `Support Team`. Then sign with the agent's name followed by a line that ends with `Support Team`.
