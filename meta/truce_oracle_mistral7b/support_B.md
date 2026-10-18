---
name: support-friendly+support-formal
description: Merged skill that replaces `support-friendly` and `support-formal`. Use for any support reply.
---

# Merged skill: support-friendly + support-formal

This skill replaces `support-friendly` and `support-formal`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `support-friendly`

- Open with `Hi <first name>!` on the first line.
- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Close with the agent's first name and then a line ending in `Support Team`.

## Rules kept unchanged from `support-formal`

- Cite the case as `Ticket #<number>`.
- Do not use contractions such as `don't`, `we'll` or `you're`.
- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output in the following format: 1. Provide a concise, formal explanation of the issue. 2. On a separate line, prepend "Links:" and include the relevant help-center article URL. Example: Issue: "You are experiencing trouble with the account setup process." Output: 1. "I apologize for the inconvenience you're experiencing during the account setup process. Our system may be encountering some issues." 2. "Links: <https://help.example.com/account-setup-troubleshooting>"

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Hi Maria Lopez!

Good news: We have resolved the issue causing your invoice export to fail with a timeout.

1. Our engineering team has deployed a fix for this problem today.
2. To apply the fix, please clear your browser cache and retry the invoice export.

Links: <https://help.example.com/invoice-export>

Reply to this email within 2 business days if you continue to experience issues.

Best regards,
Jordan Support Team
```
