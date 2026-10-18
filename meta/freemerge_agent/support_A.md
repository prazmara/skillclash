---
name: support-formal-friendly
description: Write customer support replies in the formal enterprise tone that still give a quick, helpful answer and a pointer to the help center. Use for any reply to a customer.
---

# support-formal-friendly

This skill merges `support-formal` and `support-friendly` and replaces both. Enterprise customers forward our replies to their own management, so replies are formal and easy to audit. Most customers also want a quick answer and a pointer to the help center so they can solve the problem themselves.

Every rule of both skills is kept. Where two rules cannot both hold, `support-formal` wins.

## Rules

- Open with `Dear <full name>,` on the first line. This is the `support-formal` rule. It overrides the `support-friendly` rule that the first line is `Hi <first name>!`, which is not used.
- Lead the main message, directly after the greeting, with a sentence that starts with `Good news:` or `Quick update:`.
- Cite the case as `Ticket #<number>`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Invite a response with the exact phrase `reply to this email`.
- Do not use contractions such as `don't`, `we'll` or `you're`. Write `do not`, `we will`, `you are`.
- Sign with the agent's first name followed by a line that ends with `Support Team`.
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL. To keep the previous rule, the URL goes on the final line of the reply, after the signature, written as `Links: <url>`. In the body, mention the article in words only.

## Example

Request: Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.

Output:

```
Dear Maria Lopez,

Good news: the invoice export timeout reported in Ticket #48213 was fixed by our engineering team today, and the export should work again within 2 hours.

Please follow these steps:
1. Clear your browser cache.
2. Run the invoice export again.

If the export still fails, please reply to this email and we will look into it. The help-center article listed under Links below explains how to clear the cache.

Kind regards,
Jordan
Acme Support Team
Links: https://help.example.com/invoice-export
```
