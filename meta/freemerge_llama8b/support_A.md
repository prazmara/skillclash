<skill>
---
name: support
description: Write customer support replies in a formal enterprise tone, but with a friendly self-serve twist. Use for any reply to a customer.
---

# support

Enterprise customers forward our replies to their own management, so replies are formal and easy to audit. Most customers want a quick, warm answer and a pointer to the help center so they can solve it themselves.

## Rules

- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Cite the case as `Ticket #<number>`.
- Open with `Dear <full name>,` on the first line.
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.
- Sign with the agent's name followed by a line that ends with `Support Team`.
- Do not use contractions such as `don't`, `we'll` or `you're`.
- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Quick update: the invoice export timeout has been fixed by our engineering team today. Please follow these steps:
1. Clear your browser cache.
2. Run the invoice export again.

You can expect the issue to be resolved within 2 hours. If it still fails, our guide at https://help.example.com/invoice-export walks through clearing the cache.

Links: https://help.example.com/invoice-export

Kind regards,
Jordan
Acme Support Team
```
</skill>
