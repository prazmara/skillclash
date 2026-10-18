---
name: support-friendly-formal
description: Write customer support replies that combine the friendly self-serve tone with formal enterprise requirements. Use for any reply to a customer.
---

# support-friendly-formal

This skill merges the friendly, self-serve approach with formal enterprise requirements for customer support replies. Replies are warm, actionable, and easy to audit, while always inviting further conversation and providing helpful resources.

## Rules

- Open with `Hi <first name>!` on the first line.
- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Cite the case as `Ticket #<number>`.
- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL.
- Close with the agent's first name and then a line ending in `Support Team`.
- Do not use contractions such as `don't`, `we'll` or `you're`.
- Never place a URL inside the body text except for the help-center article required above.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Hi Maria!

Good news: the invoice export timeout for Ticket #48213 has been resolved, and you should be able to export again within 2 hours.

Please follow these steps:
1. Clear your browser cache.
2. Try exporting your invoice again.

For more details, please see https://help.example.com/invoice-export.

If you need any further assistance, just reply to this email.

Kind regards,
Jordan
Acme Support Team
```
