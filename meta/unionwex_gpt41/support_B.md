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

If two rules cannot both hold, the rule from `support-friendly` wins.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Hi Maria!

Good news: Our engineering team has deployed a fix for the invoice export timeout issue referenced in Ticket #48213. To proceed, please follow these steps:

1. Clear your browser cache to ensure the latest updates are applied.
2. Retry exporting your invoice.

For more detailed instructions, please refer to our help-center article.

If you continue to experience issues or have any questions, please reply to this email. You can expect a response within 24 hours.

Jordan  
Support Team  
Links: https://help.example.com/invoice-export
```
