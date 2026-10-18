---
name: support-formal+support-friendly
description: Merged skill that replaces `support-formal` and `support-friendly`. Use for any support reply.
---

# Merged skill: support-formal + support-friendly

This skill replaces `support-formal` and `support-friendly`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `support-formal`

- Cite the case as `Ticket #<number>`
- Never place a URL inside the body text
- Sign with the agent's name followed by a line that ends with `Support Team`
- Do not use contractions such as `don't`, `we'll` or `you're`

## Rules kept unchanged from `support-friendly`

- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output as follows: 1. Lead with a sentence that starts with "Good news:" or "Quick update:". 2. Follow with a numbered list starting with "1." and "2.", containing at least two steps. Example: Good news: Your request has been processed! 1. You will receive an email confirmation shortly. 2. If you have any further questions, feel free to reply to this message.
- Write as follows: "Dear <full name>, Hi <first name>! Let's get started..."

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
