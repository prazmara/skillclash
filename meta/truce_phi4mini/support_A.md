---
name: support-formal+support-friendly
description: Merged skill that replaces `support-formal` and `support-friendly`. Use for any support reply.
---

# Merged skill: support-formal + support-friendly

This skill replaces `support-formal` and `support-friendly`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `support-formal`

- Dear Maria Lopez,
- Ticket #48213.
- Please follow these steps:
- 1. Clear your browser cache.
- 2. Run the invoice export again.
- Kind regards,
- Acme Support Team

## Rules kept unchanged from `support-friendly`

- Good news:
- Quick update:
- reply to this email
- within <n> hours
- within <n> business days
- https://help.example.com/...
- Hi <first name>!
- Support Team

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Good news: Engineering has deployed a fix for the invoice export timeout issue.

Quick update: You should clear your browser cache and retry the export.

Please reply to this email within 24 hours if the issue persists.

Kind regards,
Jordan
Acme Support Team

Support Team

https://help.example.com/invoice-export

Hi Maria,

Ticket #48213: The invoice export timeout issue has been resolved by our engineering team. Please clear your browser cache and try exporting the invoice again.

If you continue to experience problems, please let us know.

Best regards,
Jordan
Acme Support Team
```
