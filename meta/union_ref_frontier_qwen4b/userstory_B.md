<skill>
---
name: story-sprint-ready+story-portfolio
description: Combined rules of `story-sprint-ready` and `story-portfolio`. Use for any user story ticket.
---

# Combined skill: story-sprint-ready + story-portfolio

Follow every rule below.

## Rules from `story-sprint-ready`

- Name who the story is for on a line `Persona: <persona>`.
- Put the estimate at the top, right under the title, as `Story points: <n>`.
- Say how success will be measured on a line that starts with `Metric:`.
- Add one test scenario as three lines that start with `Given `, `When `, and `Then `.
- List at least two acceptance criteria as open checkboxes, one per line, written `- [ ] ...`.

## Rules from `story-portfolio`

- Say what the story does not cover on a line that starts with `Out of scope:`.
- The line directly below the title must be `Epic: <epic name>`.
- The first line must be `Story <ticket ID>: <title>`, for example `Story SHOP-88: Save cart for later`.
- Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ] <criterion>`.
- Rate the business value on a line `Value: high`, `Value: medium`, or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.

## Conflict Resolution

If two rules conflict, the rule from `story-sprint-ready` takes precedence **only if** it is directly applicable to the structure of the story. However, in the case of conflicting structural requirements (e.g., the first line being a level-1 Markdown heading versus the first line being a formatted story ticket), **both must be satisfied simultaneously** by properly combining the rules.

To resolve the conflict between:
- "The first line must be `Story <ticket ID>: <title>`" (from `story-portfolio`)
- "The first line must be a level-1 Markdown heading that holds only the title" (from `story-sprint-ready`)

We revise the first line to be a **level-1 Markdown heading** that contains **only the title** (e.g., `# View return policy directly on product pages`), and **add the `Story <ticket ID>: <title>` format as a subsequent line** *immediately after* the heading — this satisfies both rules.

Thus, the correct structure becomes:
```
# <title>
Story <ticket ID>: <title>
Story points: <n>
Epic: <epic name>
Persona: <persona>
Metric: <metric>
Value: <value>
Out of scope: <out of scope>
Depends on: <depends on>
- [ ] <acceptance criterion>
- [ ] <acceptance criterion>
Given <context>
When <action>
Then <result>
```

This ensures:
- The first line is a level-1 Markdown heading with only the title (satisfies `story-sprint-ready`).
- The line directly after the title is `Story <ticket ID>: <title>` (satisfies `story-portfolio`).
- All other rules are preserved.

## Example (corrected to satisfy all rules)

```
# View return policy directly on product pages
Story POL-23: View return policy directly on product pages
Story points: 5
Epic: Returns
Persona: cautious buyer
Metric: Customers can find and understand the return policy without leaving the product page
Value: high
Out of scope: Implementation of return shipping labels or refund processing
Depends on: none
- [ ] Return policy is clearly displayed on the product page, below the product description
- [ ] Return policy is accessible without requiring user interaction (e.g., clickable link or inline text)
- [ ] Return policy content is consistent across all product pages in the same category
- [ ] Return policy is visible on mobile and desktop views
Given the user is on a product page
When the user scrolls to the product details section
Then the return policy is displayed in a clearly visible section with a concise summary
```

</skill>
