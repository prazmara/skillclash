---
name: support-friendly-formal
description: Write customer support replies in a friendly yet formal tone. Use for any reply to a customer.
---

# support-friendly-formal

Enterprise customers forward our replies to their own management, so replies are friendly yet formal and easy to audit.

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

Good news: the invoice export timeout is fixed, and you'll be able to export again within 2 hours. If it still fails, our guide at https://help.example.com/invoice-export walks through clearing the cache.

Just reply to this email if anything looks off.

1. Clear your browser cache.
2. Run the invoice export again.

Dear Maria,

Thank you for contacting us about Ticket #48213. The invoice export timeout has been fixed by our engineering team today.

Kind regards,
Jordan
Acme Support Team
