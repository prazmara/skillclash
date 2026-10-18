---
name: support-formal
description: Write customer support replies in the formal enterprise tone. Use for any reply to a customer.
---

# support-formal

Enterprise customers forward our replies to their own management, so replies are formal and easy to audit.

## Rules

- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Cite the case as `Ticket #<number>`.
- Open with `Dear <full name>,` on the first line.
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.
- Sign with the agent's name followed by a line that ends with `Support Team`.
- Do not use contractions such as `don't`, `we'll` or `you're`.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Thank you for contacting us about Ticket #48213. The invoice export timeout has been fixed by our engineering team today.

Please follow these steps:
1. Clear your browser cache.
2. Run the invoice export again.

Kind regards,
Jordan
Acme Support Team
```
