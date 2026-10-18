---
name: support-formal-friendly
description: Write customer support replies in the friendly self-serve tone that stay easy to audit for enterprise customers. Use for any reply to a customer.
---

# support-formal-friendly

This skill merges `support-formal` and `support-friendly` and replaces both. Most customers want a quick, warm answer and a pointer to the help center so they can solve the problem themselves. Enterprise customers also forward our replies to their own management, so replies stay easy to audit.

Every rule of both skills is kept. Where two rules cannot both hold, `support-friendly` wins.

## Rules

- Open with `Hi <first name>!` on the first line. This is the `support-friendly` rule. It overrides the `support-formal` rule that the first line is `Dear <full name>,`, which is not used.
- Lead the main message, directly after the greeting, with a sentence that starts with `Good news:` or `Quick update:`.
- Cite the case as `Ticket #<number>`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Invite a response with the exact phrase `reply to this email`.
- Do not use contractions such as `don't`, `we'll` or `you're`. Write `do not`, `we will`, `you are`. The tone stays warm without them.
- Close with the agent's first name and then a line ending in `Support Team`.
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL. To keep the previous rule, the URL goes on the final line of the reply, after the signature, written as `Links: <url>`. In the body, mention the article in words only.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Hi Maria!

Good news: the invoice export timeout from Ticket #48213 was fixed today, and the export should work again within 2 hours.

Here is what to do next:
1. Clear your browser cache.
2. Run the invoice export again.

If anything still looks off, just reply to this email. The help-center article listed under Links below walks through clearing the cache.

Cheers,
Jordan
Acme Support Team
Links: https://help.example.com/invoice-export
```
