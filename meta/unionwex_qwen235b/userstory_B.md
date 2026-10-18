---
name: story-sprint-ready+story-portfolio
description: Combined rules of `story-sprint-ready` and `story-portfolio`. Use for any user story ticket.
---

# Combined skill: story-sprint-ready + story-portfolio

Follow every rule below.

## Rules from `story-sprint-ready`

- Name who the story is for on a line `Persona: <persona>`.
- Put the estimate at the top, right under the title, as `Story points: <n>`.
- Say how success will be measured on a line that starts with `Metric: `.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.
- List at least two acceptance criteria as open checkboxes, one per line, written `- [ ] ...`.
- The first line must be a level-1 Markdown heading that holds only the title, for example `# Save cart for later`.

## Rules from `story-portfolio`

- Say what the story does not cover on a line that starts with `Out of scope: `.
- The line directly below the title must be `Epic: <epic name>`.
- The first line must be `Story <ticket ID>: <title>`, for example `Story SHOP-88: Save cart for later`.
- Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ] <criterion>`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.

If two rules cannot both hold, the rule from `story-sprint-ready` wins.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
# Save cart for later
Epic: Checkout
Story points: 5
Persona: returning shopper
Value: high
Metric: Increase in cart recovery rate measured by percentage of saved carts that convert within 7 days
Out of scope: Syncing wishlists or browsing history across devices
Depends on: none
- [ ] User can save their current cart with a single action
- [ ] Saved cart is accessible when logging in from any device
Given the user has items in their cart and is logged in
When the user selects "Save Cart for Later"
Then the cart is saved and accessible in their account across all devices
```
