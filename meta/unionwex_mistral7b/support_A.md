---
name: support-formal+support-friendly
description: Combined rules of `support-formal` and `support-friendly`. Use for any support reply.
---

# Combined skill: support-formal + support-friendly

Follow every rule below.

## Rules from `support-formal`

- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Cite the case as `Ticket #<number>`.
- Open with `Dear <full name>,` on the first line.
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.
- Sign with the agent's name followed by a line that ends with `Support Team`.
- Do not use contractions such as `don't`, `we'll` or `you're`.

## Rules from `support-friendly`

- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL.
- Open with `Hi <first name>!` on the first line.
- Close with the agent's first name and then a line ending in `Support Team`.

If two rules cannot both hold, the rule from `support-formal` wins.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Hi Maria!

Good news: We have resolved the issue you were experiencing with your invoice export. Here's what you need to do:

1. Clear your browser cache.
2. Retry the invoice export.

For more detailed instructions, please refer to our help article: https://help.example.com/invoice-export

If you encounter any further issues, feel free to reply to this message.

Best regards,
Jordan
Support Team
```
