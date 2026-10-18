---
name: support-friendly+support-formal
description: Merged skill that replaces `support-friendly` and `support-formal`. Use for any support reply.
---

# Merged skill: support-friendly + support-formal

This skill replaces `support-friendly` and `support-formal`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `support-friendly`

- Good news:
- Quick update:
- reply to this email
- within <n> hours
- within <n> business days
- https://help.example.com/...
- Hi <first name>!
- Support Team

## Rules kept unchanged from `support-formal`

- Dear Maria Lopez,
- Ticket #48213.
- Please follow these steps:
- 1. Clear your browser cache.
- 2. Run the invoice export again.
- Kind regards,
- Acme Support Team

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Thank you for reaching out to us regarding the issue with your invoice export. We have identified the problem and our engineering team has deployed a fix today. To resolve the timeout issue, please follow these steps:

1. Clear your browser cache.
2. Run the invoice export again.

We apologize for the inconvenience this has caused. For more detailed instructions, please refer to our help article: https://help.example.com/invoice-export.

Kind regards,
Acme Support Team

Ticket #48213

Agent: Jordan
```
