---
name: support-formal+support-friendly
description: Merged skill that replaces `support-formal` and `support-friendly`. Use for any support reply.
---

# Merged skill: support-formal + support-friendly

This skill replaces `support-formal` and `support-friendly`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `support-formal`

- Cite the case as `Ticket #<number>`.
- Open with `Dear <full name>,` on the first line.
- Never place a URL inside the body text.
- Sign with the agent's name followed by a line that ends with `Support Team`.
- Do not use contractions such as `don't`, `we'll` or `you're`.

## Rules kept unchanged from `support-friendly`


## Reconciled rules (each one satisfies a rule of both skills at once)

- Write a response that starts with a sentence beginning with "Good news:" or "Quick update:", followed by a numbered list with at least two steps, where each step begins with a number and a period.
- Arrange the output so that links appear only on a final line that starts with "Links:", and include the link to the relevant help-center article in the format "Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL."

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Good news: we've recently deployed a fix for the invoice export issue. Here are the steps to resolve the problem:

1. Clear your browser cache by pressing Ctrl + Shift + R (Windows) or Command + Shift + R (Mac) to reload the page.
2. Retry the invoice export process to see if it completes successfully.

Links: Point the customer to the relevant help-center article by including its https://help.example.com/invoice-export URL.

Sincerely,
Jordan
Support Team
```
