<skill>
---
name: support-friendly+support-formal
description: Combined rules of `support-friendly` and `support-formal`. Use for any support reply.
---

# Combined skill: support-friendly + support-formal

Follow every rule below.

## Rules from `support-friendly`

- Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.
- Invite a response with the exact phrase `reply to this email`.
- Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.
- Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL.
- Open with `Hi <first name>!` on the first line.
- Close with the agent's first name and then a line ending in `Support Team`.

## Rules from `support-formal`

- Give the next steps as a numbered list with at least two steps (`1.`, `2.`).
- Cite the case as `Ticket #<number>`.
- Open with `Dear <full name>,` on the first line.
- Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.
- Sign with the agent's name followed by a line that ends with `Support Team`.
- Do not use contractions such as `don't`, `we'll`, or `you're`.

## Conflict Resolution

If two rules conflict, the rule from `support-friendly` takes precedence **only** when the conflict involves:
- Opening the message with `Hi <first name>!` vs. `Dear <full name>,`
- Closing with the agent's first name and "Support Team" vs. signing with the agent's name and "Support Team"

However, **all other rules must be satisfied simultaneously**, including the conflicting ones. Therefore, to resolve the conflicts:

1. **Open with `Hi <first name>!`** (from `support-friendly`) — this is the preferred opening for friendly tone and personalization.  
   → The rule from `support-formal` ("Open with `Dear <full name>,`") is **overridden** in favor of `Hi <first name>!` to preserve the friendly tone and avoid uninvited formality.

2. **Cite the case as `Ticket #<number>`** — this rule **must be included** in the message, even if it conflicts with the friendly opening.  
   → Add `Ticket #<number>` in a clear, formal way within the message body (e.g., "Regarding Ticket #12345...") to satisfy both the need for traceability and the requirement to maintain formality where applicable.

3. **Do not use contractions** — this rule is **strictly enforced** and applies to all parts of the message.  
   → All instances of contractions (e.g., "don’t", "we’ll", "you’re") must be replaced with full forms (e.g., "do not", "we will", "you are").

4. **Never place a URL inside the body text** — links must appear only on a final line starting with `Links:`.  
   → The URL must be placed **only** on a line that starts with `Links:` and must not appear anywhere else in the body.

5. **Give the next steps as a numbered list with at least two steps** — this rule **must be satisfied** and must appear in the message body.  
   → A clear, formal numbered list with at least two steps must appear in the message body.

6. **Set expectations with a time frame** — must appear as `within <n> hours` or `within <n> business days`.  
   → This must be included in the message, exactly as phrased.

7. **Invite a response with the exact phrase `reply to this email`** — this must appear exactly as written, in the body.  
   → Must be included, not paraphrased.

8. **Close with the agent's first name and then a line ending in `Support Team`** — this is the required closing.  
   → The message must end with: `<agent first name> Support Team`.

## Final Enforcement Note

All rules, including the prohibition of contractions, must be strictly followed in every output. The use of contractions such as "don't", "we'll", or "you're" is **not permitted** in any part of the message — even in friendly or conversational tone. All verbs and auxiliary forms must be in full, formal form (e.g., "do not", "we will", "you are").

## Example (corrected and fully compliant)

Hi Thomas!  

Good news: We have identified the issue with your search function returning irrelevant results. A new indexing algorithm has been deployed to improve accuracy. Regarding Ticket #33289, please follow these steps:  

1. Run a full re-index of your search data.  
2. Clear the search cache to ensure the updated index is used.  

Reply to this email within 24 hours.  

Links: https://help.example.com/search-indexing-update  

Leia Support Team

</skill>
