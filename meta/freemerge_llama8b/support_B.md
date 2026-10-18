<skill>
---
name: support
description: Write customer support replies in a tone that suits the customer's needs. Use for any reply to a customer.
---

# support

This skill combines the friendly self-serve tone with the formal enterprise tone, prioritizing the friendly tone when rules conflict.

## Rules

- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL.
- Open with `Hi <first name>!` on the first line.
- Close with the agent's first name and then a line ending in `Support Team`.
- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Cite the case as `Ticket #<number>`.
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.
- Sign with the agent's name followed by a line that ends with `Support Team`.
- Do not use contractions such as `don't`, `we'll` or `you're`.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Hi Maria!

Good news: the invoice export timeout is fixed, and you'll be able to export again within 2 hours. If it still fails, please follow these steps:
1. Clear your browser cache.
2. Run the invoice export again.

Ticket #48213 has been resolved. If you have any further questions, reply to this email.

Links: https://help.example.com/invoice-export

Cheers,
Jordan
Acme Support Team
```
</skill>
