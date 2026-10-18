---
name: support-friendly+support-formal
description: Merged skill that replaces `support-friendly` and `support-formal`. Use for any support reply.
---

# Merged skill: support-friendly + support-formal

This skill replaces `support-friendly` and `support-formal`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `support-friendly`

- Open with `Hi <first name>!` on the first line.
- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Close with the agent's first name and then a line ending in `Support Team`.

## Rules kept unchanged from `support-formal`

- Cite the case as `Ticket #<number>`.
- Do not use contractions such as `don't`, `we'll` or `you're`.
- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).

## Reconciled rules (each one satisfies a rule of both skills at once)

- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL, and ensure that the URL appears on a final line that starts with `Links:`, without placing it inside the body text.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Hi Maria Lopez!

Good news: Engineering has deployed a fix for the issue you're experiencing with your invoice export failing due to a timeout.

To resolve this, please clear your browser cache and retry the export.

1. Clear your browser cache.
2. Retry the invoice export.

Links: https://help.example.com/invoice-export

Jordan Support Team
```
