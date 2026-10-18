---
name: support-merged
description: Write customer support replies using a formal enterprise tone with structured next steps and audit-friendly formatting. In cases of conflict, formal rules override friendly ones.
---

# support-merged

This skill combines formal enterprise and friendly self-serve support reply styles. The formal tone takes precedence when rules conflict, ensuring replies are appropriate for enterprise customers while retaining clarity and actionability.

## Rules

- Open with `Dear <full name>,` on the first line.
- Lead the main message with a sentence that starts with `Good news:` or `Quick update:` only if it does not conflict with formality; otherwise, use a formal alternative.
- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Cite the case as `Ticket #<number>`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days` when applicable.
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.
- Invite a response with the exact phrase `reply to this email` if appropriate, but only outside the body text and before the signature.
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL under the `Links:` section.
- Sign with the agent's name followed by a line that ends with `Support Team`.
- Do not use contractions such as `don't`, `we'll` or `you're`.
- Close with the agent's first name and then a line ending in `Support Team` — use full name in salutation, first name in signature.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Good news: the issue affecting Ticket #48213 has been resolved by our engineering team today. The invoice export timeout will no longer occur.

Please follow these steps:
1. Clear your browser cache.
2. Run the invoice export again.

You should see successful results within 2 hours. If the issue persists, please reply to this email.

Links: https://help.example.com/invoice-export

Kind regards,
Jordan
Acme Support Team
```
