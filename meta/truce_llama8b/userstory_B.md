---
name: story-sprint-ready+story-portfolio
description: Merged skill that replaces `story-sprint-ready` and `story-portfolio`. Use for any user story ticket.
---

# Merged skill: story-sprint-ready + story-portfolio

This skill replaces `story-sprint-ready` and `story-portfolio`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `story-sprint-ready`

- Name who the story is for on a line `Persona: <persona>`.
- Put the estimate at the top, right under the title, as `Story points: <n>`.
- Say how success will be measured on a line that starts with `Metric: `.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.
- List at least two acceptance criteria as open checkboxes, one per line, written `- [ ] ...`.
- The first line must be a level-1 Markdown heading that holds only the title, for example `# Save cart for later`.

## Rules kept unchanged from `story-portfolio`

- Say what the story does not cover on a line that starts with `Out of scope: `.
- The line directly below the title must be `Epic: <epic name>`.
- The first line must be `Story <ticket ID>: <title>`, for example `Story SHOP-88: Save cart for later`.
- Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ] <criterion>`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
Story SHOP-88: Save cart for later
Epic: Checkout
Persona: returning shopper
Story points: 5
Metric: Number of carts saved and retrieved successfully
Given the shopper is logged in
When they click the "Save cart" button
Then the cart is saved to their account

- [ ] The cart is saved with all items and quantities
- [ ] The cart can be retrieved from the saved carts list
Out of scope: Saving carts for guests
Value: high
Depends on: none
```
