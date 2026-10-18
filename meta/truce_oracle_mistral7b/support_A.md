---
name: support-formal+support-friendly
description: Merged skill that replaces `support-formal` and `support-friendly`. Use for any support reply.
---

# Merged skill: support-formal + support-friendly

This skill replaces `support-formal` and `support-friendly`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `support-formal`

- Open with `Dear <full name>,` on the first line.
- Cite the case as `Ticket #<number>`.
- Do not use contractions such as `don't`, `we'll` or `you're`.
- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Sign with the agent's name followed by a line that ends with `Support Team`.

## Rules kept unchanged from `support-friendly`

- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output in the following format: Body text: [Explanation or solution] Links: [URL of the relevant help-center article]

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Good news: We have identified the issue causing your invoice export to fail with a timeout. Quick update: Our engineering team has deployed a fix for this problem today.

To resolve the issue, please follow these steps:

1. Clear your browser cache.
2. Retry the invoice export.

For more detailed instructions, please refer to the following help article: [Invoice Export](https://help.example.com/invoice-export)

Please reply to this email once you have tried the steps and the issue is resolved. We expect to hear back from you within 24 hours.

Best regards,
Jordan
Support Team
```
