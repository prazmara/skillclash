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

- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL only on a final line that starts with `Links:` and comes after the signature, for example `Links: https://help.example.com/invoice-export`. Never place a URL inside the body text, and refer to the article there in words only.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Good news: the invoice export timeout reported in Ticket #48213 was fixed by our engineering team today.

Please follow these steps:
1. Clear your browser cache.
2. Run the invoice export again.

The help article listed at the end of this message explains how to clear the cache. If the export still fails, please reply to this email and we will respond within 24 hours.

Kind regards,
Jordan
Acme Support Team

Links: https://help.example.com/invoice-export
```
