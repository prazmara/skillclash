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

- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL. Links

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Hi Maria!

Good news: Engineering has deployed a fix for the invoice export timeout issue you reported.

To resolve this on your end, please follow these steps:

1. Clear your browser cache completely.  
2. Navigate back to the invoice export page and attempt the export again.

You can find detailed instructions for clearing your cache in our help center: https://help.example.com/invoice-export.

The issue should now be resolved, but if you continue to experience problems, reply to this email. We will investigate further within 24 business hours.

Jordan  
Support Team  
Ticket #48213
```
