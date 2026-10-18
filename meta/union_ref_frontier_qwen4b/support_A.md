<skill>
---
name: support-formal+support-friendly
description: Combined rules of `support-formal` and `support-friendly`. Use for any support reply.
---

# Combined skill: support-formal + support-friendly

Follow every rule below. If two rules conflict, the rule from `support-formal` takes priority.

## Rules from `support-formal`

- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Cite the case as `Ticket #<number>` on the first line, immediately after the salutation.
- Open with `Dear <full name>,` on the first line.
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.
- Sign with the agent's name followed by a line that ends with `Support Team`.
- Do not use contractions such as `don't`, `we'll`, or `you're`.

## Rules from `support-friendly`

- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL.
- Open with `Hi <first name>!` on the first line.
- Close with the agent's first name and then a line ending in `Support Team`.

## Conflict Resolution

When a rule from `support-formal` and a rule from `support-friendly` conflict:
- The `support-formal` rule takes precedence over `support-friendly` rules.
- Specifically:
  - The salutation must be `Dear <full name>,`, not `Hi <first name>!`.
  - The case must be cited as `Ticket #<number>` immediately after the salutation.
  - The agent’s name must appear in the signature as the full name, followed by a line ending in `Support Team`.
  - No contractions are allowed.
  - URLs must not appear in body text; they must appear only on a line starting with `Links:`.
  - Timeframes must be included in the message (e.g., `within 24 hours`) as required by `support-friendly`, but must not violate any `support-formal` constraints.

## Example (fully compliant output)

Dear Naomi Kim,  
Ticket #41205  

Good news: the sync endpoint has been restored. You should now be able to sync your calendar successfully.  

1. Refresh your calendar to ensure the latest data is loaded.  
2. Verify that your timezone is set correctly in the calendar settings.  

Please reply to this email within 24 hours.  
Links: https://help.example.com/calendar-sync-setup  

Riley Support Team

</skill>
