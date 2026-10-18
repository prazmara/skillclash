---
name: support-friendly+support-formal
description: Combined rules of `support-friendly` and `support-formal`. Use for any support reply.
---

# Combined skill: support-friendly + support-formal

Follow every rule below.

## Rules from `support-friendly`

- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL.
- Open with `Hi <first name>!` on the first line.
- Close with the agent's first name and then a line ending in `Support Team`.

## Rules from `support-formal`

- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Cite the case as `Ticket #<number>`.
- Open with `Dear <full name>,` on the first line.
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.
- Sign with the agent's name followed by a line that ends with `Support Team`.
- Do not use contractions such as `don't`, `we'll` or `you're`.

## Examples

Example for `support-friendly`:

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Hi Maria!

Good news: the invoice export timeout is fixed, and you'll be able to export again within 2 hours. If it still fails, our guide at https://help.example.com/invoice-export walks through clearing the cache.

Just reply to this email if anything looks off.

Cheers,
Jordan
Acme Support Team
```

Example for `support-formal`:

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
