---
name: support-formal+support-friendly
description: Merged skill that replaces `support-formal` and `support-friendly`. Use for any support reply.
---

# Merged skill: support-formal + support-friendly

This skill replaces `support-formal` and `support-friendly`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `support-formal`

- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Cite the case as `Ticket #<number>`.
- Open with `Dear <full name>,` on the first line.
- Do not use contractions such as `don't`, `we'll` or `you're`.

## Rules kept unchanged from `support-friendly`

- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Refer the customer to the relevant help-center article, but do not place a URL inside the body text. Include the `https://help.example.com/...` link only on a final line that starts with `Links:`.
- Sign with the agent's first name, then the agent's full name, each on its own line, followed by a line that ends with `Support Team`.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Quick update: Good news, our engineering team has deployed a fix today for the invoice export timeout issue you experienced (Ticket #48213).

To proceed, please follow these steps:
1. Clear your browser cache to ensure the latest updates are applied.
2. Retry exporting your invoice.

If you need detailed instructions, please refer to our help-center article. Should you encounter any further issues, reply to this email and we will assist you within 24 hours.

Thank you for your patience.

Jordan  
Jordan [Last Name]  
Support Team  
Links: https://help.example.com/invoice-export
```
