---
name: support-formal-friendly-merged
description: Write customer support replies that combine the formal enterprise tone and the friendly self-serve approach. Use for any reply to a customer.
---

# support-formal-friendly-merged

This skill merges the formal enterprise tone required for enterprise customers with the friendly, self-serve approach preferred by most users. Replies are formal, easy to audit, and provide clear next steps, while also being approachable and helpful.

## Rules

- Open with `Dear <full name>,` on the first line.
- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Cite the case as `Ticket #<number>`.
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.
- Sign with the agent's name followed by a line that ends with `Support Team`.
- Do not use contractions such as `don't`, `we'll` or `you're`.
- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- On the final line, after the signature, include any relevant help-center article links as `Links: <URL>`.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Good news: The invoice export timeout referenced in Ticket #48213 has been resolved by our engineering team today. You should be able to export again within 2 hours.

Please follow these steps:
1. Clear your browser cache.
2. Attempt the invoice export again.

If you require further assistance, please reply to this email.

Kind regards,
Jordan
Acme Support Team
Links: https://help.example.com/invoice-export
```
