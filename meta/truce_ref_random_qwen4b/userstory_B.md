<skill>
---
name: story-sprint-ready+story-portfolio
description: Merged skill that replaces `story-sprint-ready` and `story-portfolio`. Use for any user story ticket. Follow every rule below.
---

# Merged skill: story-sprint-ready + story-portfolio

This skill replaces `story-sprint-ready` and `story-portfolio`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `story-sprint-ready`

- Name who the story is for on a line `Persona: <persona>`.
- Put the estimate at the top, right under the title, as `Story points: <n>`.
- Say how success will be measured on a line that starts with `Metric:`.
- Add one test scenario as three lines that start with `Given `, `When `, and `Then`.
- List at least two acceptance criteria as open checkboxes, one per line, written `- [ ] ...`.

## Rules kept unchanged from `story-portfolio`

- Say what the story does not cover on a line that starts with `Out of scope:`.
- The line directly below the title must be `Epic: <epic name>`.
- List blocking tickets on a line that starts with `Depends on:`, and write `Depends on: none` when there are none.
- Rate the business value on a line `Value: high`, `Value: medium`, or `Value: low`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- # Story <ticket ID>: <title>

## Fixed and clarified rule: First line format
- The first line must be a level-1 Markdown heading that holds only the title, with no additional text or metadata. For example: `# Shoppers want to save their cart and come back to it later on another device`.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
# Story SHOP-88: Shoppers want to save their cart and come back to it later on another device
Epic: Checkout
Story points: 5
Persona: returning shopper
Value: high
Metric: Cart recovery rate increases by 20% within one month of implementation
Given a shopper has added items to their cart on one device
When they navigate away and return to the site on a different device
Then their cart should be restored with all previously added items
- [ ] Implement cart persistence across devices using secure session tokens
- [ ] Ensure cart data is synchronized without user intervention
Out of scope: Saving cart for new users during first-time checkout
Depends on: none
```
</skill>
