---
name: support-friendly+support-formal
description: Merged skill that replaces `support-friendly` and `support-formal`. Use for any support reply.
---

# Merged skill: support-friendly + support-formal

This skill replaces `support-friendly` and `support-formal`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `support-friendly`

- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL.

## Rules kept unchanged from `support-formal`

- Cite the case as `Ticket #<number>`

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the main message starting with "Good news: " or "Quick update: ", followed by a colon, and then provide the next steps as a numbered list, starting with "1.", followed by a period, and each subsequent step starting with "2.", followed by a period. For example: Good news: Your request has been processed successfully! 1. You will receive a confirmation email shortly. 2. If you do not receive the email within 24 hours, please contact our support team.
- Open with "Dear <first name>, <Full Name>," on the first line.
- Write the output as follows: "Your request has been addressed, [Agent's First Name]. Regards, [Agent's Name] Support Team."

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Good news: Your issue with the invoice export failure has been addressed, Jordan. Here are the steps to resolve the issue:

1. Clear your browser cache.
2. Retry the invoice export.

For more detailed instructions, please refer to the help article at https://help.example.com/invoice-export.

If you encounter any further issues, please do not hesitate to contact our support team.

Your request has been addressed, Jordan.

Regards,
Jordan Support Team.
```
