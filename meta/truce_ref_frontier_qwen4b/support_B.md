<skill>
---
name: support-friendly+support-formal
description: Merged skill that replaces `support-friendly` and `support-formal`. Use for any support reply. Follow every rule below.
---

# Merged skill: support-friendly + support-formal

This skill replaces `support-friendly` and `support-formal`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `support-friendly`

- Invite a response with the exact phrase `reply to this email`.  
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.  
- Open with `Hi <first name>!` on the first line.

## Rules kept unchanged from `support-formal`

- Do not use contractions such as `don't`, `we'll`, or `you're`.  
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`. Give the next steps as a numbered list with at least two steps (`1.`, `2.`).  
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL and citing the case as `Ticket #<number>`.  
- Close with the agent's first name and then a line ending in `Support Team`. Sign with the agent's name followed by a line that ends with `Support Team`.

## How to satisfy conflicting rules:

- The rule to "invite a response with the exact phrase `reply to this email`" is placed at the beginning of the message **after** the greeting and before the main message, to maintain formality and clarity.  
- The rule to "set expectations with a time frame" is included as a standalone sentence immediately after the opening greeting, using the format `within <n> hours` or `within <n> business days`.  
- The rule to "never place a URL inside the body text" is enforced by placing the URL only on a line that starts with `Links:` at the end of the message. The citation of the ticket number is included in that line.  
- The rule against contractions is strictly enforced: all instances of `don't`, `we'll`, `you're`, etc., are replaced with full forms (e.g., "will not", "we will", "you are").

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Hi Maria!  

reply to this email  

Good news: we have identified and fixed the issue causing your invoice export to timeout.  

1. Clear your browser cache and cookies.  
2. Retry the invoice export process.  

Within 24 hours, you should see the fix applied.  

Links: https://help.example.com/invoice-export (Ticket #48213)  

Jordan  
Support Team
```
</skill>
