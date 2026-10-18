<skill>
---
name: support-formal+support-friendly
description: Merged skill that replaces `support-formal` and `support-friendly`. Use for any support reply. Follow every rule below.
---

# Merged skill: support-formal + support-friendly

This skill replaces `support-formal` and `support-friendly`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `support-formal`

- Cite the case as `Ticket #<number>` on the first line after the salutation.
- Open with `Dear <full name>,` on the first line.
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.
- Do not use contractions such as `don't`, `we'll`, or `you're`.

## Rules kept unchanged from `support-friendly`

- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The next steps are 1. Review the updated documentation and 2. Schedule a follow-up meeting with the team.
- Sign with the agent's name followed by a line that ends with "Support Team". Close with the agent's first name and then a line ending in "Support Team".

## Rule addition: Corrected messaging flow

To satisfy both `support-formal` and `support-friendly` without contradiction, the main message must **begin with a sentence starting with `Good news:` or `Quick update:`** — this is a core rule from `support-friendly` — and must also **accurately reflect the resolution** of the issue in a formal, clear tone.

Thus, the main message must **start with `Good news:` or `Quick update:`** and **follow the resolution details** in a way that aligns with the formal tone and avoids contractions.

## Rule addition: URL placement enforcement

All URLs must be placed on a final line that starts with `Links:`. No URL may appear anywhere else in the body of the email.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Ticket #48213

Good news: A fix has been deployed to resolve the issue with your invoice export failing due to a timeout. To ensure the update takes effect, we recommend that you clear your browser cache and then retry the export process.

The next steps are:  
1. Review the updated documentation and  
2. Schedule a follow-up meeting with the team.

Please reply to this email within 24 hours if you continue to experience issues.

Links:  
https://help.example.com/invoice-export

Jordan  
Support Team  
Jordan Support Team
```
</skill>
