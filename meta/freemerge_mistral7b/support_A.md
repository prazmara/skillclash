<skill>
---
name: support
description: Write customer support replies that can be either formal or friendly, depending on the context. Use for any reply to a customer.
---

# support

Our responses are tailored to the needs of our customers, whether they require a formal enterprise tone or a friendly self-serve tone.

## Rules

- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Cite the case as `Ticket #<number>`.
- Open with `Dear <full name>,` or `Hi <first name>!` on the first line, depending on the tone.
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:` or `[Help]`.
- Sign with the agent's name followed by a line that ends with `Support Team`.
- Do not use contractions such as `don't`, `we'll` or `you're` in formal responses.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output (Formal):

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

Output (Friendly):

```
Hi Maria!

Good news: the invoice export timeout is fixed, and you'll be able to export again within 2 hours. If it still fails, our guide at [Help] walks through clearing the cache.

Just reply to this email if anything looks off.

Cheers,
Jordan
Acme Support Team
```
</skill>
