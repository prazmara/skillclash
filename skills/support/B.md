---
name: support-friendly
description: Write customer support replies in the friendly self-serve tone. Use for any reply to a customer.
---

# support-friendly

Most customers want a quick, warm answer and a pointer to the help center so they can solve it themselves.

## Rules

- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL.
- Open with `Hi <first name>!` on the first line.
- Close with the agent's first name and then a line ending in `Support Team`.

## Example

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
