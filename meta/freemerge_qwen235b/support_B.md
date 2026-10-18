---
name: support-merged
description: Write customer support replies using a merged tone that is both friendly and formal. Use for any reply to a customer.
---

# support-merged

Replies should be warm yet professional, combining the clarity of formal enterprise communication with the approachability of self-serve support. The goal is to provide a quick, clear resolution path while maintaining auditability and warmth.

## Rules

- Open with `Hi <first name>!` on the first line. (from `support-friendly`)
- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`. (from `support-friendly`)
- Cite the case as `Ticket #<number>`. (from `support-formal`)
- Give the next steps as a numbered list with at least two steps (`1.`, `2.`). (from `support-formal`)
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`. (from `support-friendly`)
- Invite a response with the exact phrase `reply to this email`. (from `support-friendly`)
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`. (from `support-formal`)
- Sign with the agent's first name and then a line ending in `Support Team`. (from `support-friendly`)
- Do not use contractions such as `don't`, `we'll` or `you're`. (from `support-formal`)

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Hi Maria!

Good news: the issue with the invoice export timeout has been resolved in Ticket #48213. You will be able to export successfully within 2 hours.

Please follow these steps:
1. Clear your browser cache.
2. Run the invoice export again.

If the issue persists, reply to this email for further assistance.

Links: https://help.example.com/invoice-export

Jordan
Acme Support Team
```
