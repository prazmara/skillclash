---
name: support-formal-friendly
description: Write customer support replies in a blend of formal and friendly tones. Use for any reply to a customer.
---

# support-formal-friendly

When writing customer support replies, we aim to balance professionalism with a warm, approachable tone. This skill is suitable for any reply to a customer, ensuring clarity and helpfulness.

## Rules

- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- Open with `Dear <full name>,` on the first line.
- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Cite the case as `Ticket #<number>`.
- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL.
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.
- Sign with the agent's name followed by a line that ends with `Support Team`.
- Close with the agent's first name and then a line ending in `Support Team`.
- Do not use contractions such as `don't`, `we'll` or `you're`.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Good news: the invoice export timeout is fixed, and you'll be able to export again within 2 hours. If it still fails, our guide at https://help.example.com/invoice-export walks through clearing the cache.

Please follow these steps:
1. Clear your browser cache.
2. Run the invoice export again.

Just reply to this email if anything looks off.

Kind regards,
Jordan
Acme Support Team
```
