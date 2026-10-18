---
name: support-formal+support-friendly
description: Merged skill that replaces `support-formal` and `support-friendly`. Use for any support reply.
---

# Merged skill: support-formal + support-friendly

This skill replaces `support-formal` and `support-friendly`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `support-formal`

- Cite the case as `Ticket #<number>`.
- Open with `Dear <full name>,` on the first line.
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.
- Do not use contractions such as `don't`, `we'll` or `you're`.

## Rules kept unchanged from `support-friendly`

- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Quick update: Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Sign with the agent's name followed by a line that ends with `Support Team`, ensuring the agent's first name appears at the close before the line ending in `Support Team`. Both the full agent name and first name must be included in sequence to satisfy the formal and friendly closing requirements.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Thank you for reporting the issue with your invoice export. We have identified the cause and our engineering team has deployed a fix today. Please follow the steps below to resolve the issue:

1. Clear your browser cache completely.
2. Retry the invoice export function.

The system should now process your request without timing out. If you continue to experience difficulties, reply to this email so we can assist further.

This matter will be resolved within 24 hours.

Jordan Smith  
Jordan Support Team

Links: https://help.example.com/invoice-export
```
