<skill>
---
name: story-portfolio+story-sprint-ready
description: Combined rules of `story-portfolio` and `story-sprint-ready`. Use for any user story ticket.
---

# Combined skill: story-portfolio + story-sprint-ready

Follow every rule below.

## Rules from `story-portfolio`

- Say what the story does not cover on a line that starts with `Out of scope: `.
- The line directly below the title must be `Epic: <epic name>`.
- The first line must be `Story <ticket ID>: <title>`, for example `Story SHOP-88: Save cart for later`.
- Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ] <criterion>`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.

## Rules from `story-sprint-ready`

- Name who the story is for on a line `Persona: <persona>`.
- Put the estimate at the top, right under the title, as `Story points: <n>`.
- Say how success will be measured on a line that starts with `Metric: `.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.
- List at least two acceptance criteria as open checkboxes, one per line, written `- [ ] ...`.
- The first line must be a level-1 Markdown heading that holds only the title, for example `# Save cart for later`.

## Conflict resolution

If two rules cannot both hold, the rule from `story-portfolio` wins.

**Specific resolution for conflicting rules:**

- The first line must be `Story <ticket ID>: <title>` (from `story-portfolio`) — this takes precedence over the rule that requires a level-1 Markdown heading with only the title.  
  → Therefore, the heading `# <title>` is **not** allowed. Instead, the first line must be `Story <ticket ID>: <title>`, and **no Markdown heading** is used at the top.  
  → The example must be updated to reflect this.

- The rule "The line directly below the title must be `Epic: <epic name>`" (from `story-portfolio`) **must** be satisfied. This rule is **not** overridden by any other rule and **must** appear immediately after the first line.  
  → Therefore, in all outputs, after `Story <ticket ID>: <title>`, the next line **must** be `Epic: <epic name>`, even if it conflicts with the `story-sprint-ready` rule about test scenarios or acceptance criteria placement.  
  → This rule is **not** optional or conditional — it is mandatory and must be enforced.

**Corrected example (satisfies all rules):**  
`Story ECO-11: Shoppers want to filter products by environmental impact`  
`Epic: Sustainable Products`  
`Story points: 7`  
`Persona: eco-conscious consumer`  
`Metric: Percentage of users who apply environmental filters to find products`  
`Value: high`  
`Out of scope: Filtering by price, brand, or availability`  
`Depends on: none`  
`- [ ] Allow users to select environmental impact filters (e.g., recyclable packaging, low carbon footprint)`  
`- [ ] Display filtered products with environmental impact badges`  
`Given a user is on the product listing page`  
`When the user selects "Low Carbon Footprint" as a filter`  
`Then only products with low carbon footprint are displayed`

**Note:** The rule "The line directly below the title must be `Epic: <epic name>`" is **mandatory** and **not overridden** by any other rule. This rule was previously missing from the conflict resolution section and must be explicitly stated and enforced. The original skill file incorrectly implied that this rule was optional or overridden, which led to violations in the assistant outputs.

## Final output structure (in order):

1. `Story <ticket ID>: <title>`
2. `Epic: <epic name>`
3. `Story points: <n>`
4. `Persona: <persona>`
5. `Metric: <success metric>`
6. `Value: high|medium|low`
7. `Out of scope: <list of out-of-scope items>`
8. `Depends on: none` (or list of tickets)
9. Acceptance criteria (at least two, as unchecked checkboxes)
10. One test scenario (three lines: `Given`, `When`, `Then`)

</skill>
