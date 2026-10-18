---
name: support-friendly+support-formal
description: Merged skill that replaces `support-friendly` and `support-formal`. Use for any support reply.
---

# Merged skill: support-friendly + support-formal

This skill replaces `support-friendly` and `support-formal`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `support-friendly`

- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL.
- Open with `Hi <first name>!` on the first line.
- Close with the agent's first name and then a line ending in `Support Team`.

## Rules kept unchanged from `support-formal`

- Never place a URL inside the body text.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Good news: We've recently deployed a fix for the invoice export issue that was causing timeouts.

Hi Maria! 

To resolve the issue, please try clearing your browser cache and then retry the invoice export. If you're still experiencing issues, it's possible that your browser is still loading the old version of the page.

For more information on how to troubleshoot and resolve this issue, please refer to our help article at https://help.example.com/invoice-export.

We'll be in touch if we need any further information from you. reply to this email within 2 business days to let us know if the issue is resolved. If you have any further questions or concerns, please don't hesitate to reach out.

Best,
Jordan
Support Team
```
