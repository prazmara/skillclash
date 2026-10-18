---
name: story-portfolio-sprint-ready
description: Write user story tickets that roll up into the product portfolio board and that a delivery team can pull into a sprint. Use for any user story or backlog ticket.
---

# story-portfolio-sprint-ready

This skill merges `story-portfolio` and `story-sprint-ready` and replaces both. Product managers group stories by epic and rank them by value, so every story states its epic, its value and its limits in fixed places. A story is also ready for sprint planning only when the team sees its size near the top and can test and measure it without further questions.

Every rule of both skills is kept. Where two rules cannot both hold, `story-portfolio` wins.

## Rules

- The first line must be `Story <ticket ID>: <title>`, for example `Story SHOP-88: Save cart for later`. This is the `story-portfolio` rule. It overrides the `story-sprint-ready` rule that the first line is a level-1 Markdown heading that holds only the title, so no `# ` heading is written.
- The line directly below the title must be `Epic: <epic name>`. This is the `story-portfolio` rule. It overrides the part of the `story-sprint-ready` rule that puts the estimate right under the title.
- Put the estimate at the top as `Story points: <n>`. Because the second line belongs to the epic, the estimate goes on the third line, directly below the `Epic:` line.
- Name who the story is for on a line `Persona: <persona>`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.
- Say what the story does not cover on a line that starts with `Out of scope: `.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.
- Write the acceptance criteria as a checklist of at least two unchecked boxes, one per line, each of the form `- [ ] <criterion>`.
- Say how success will be measured on a line that starts with `Metric: `.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
Story SHOP-88: Save cart for later
Epic: Checkout
Story points: 5

Persona: returning shopper
Shoppers can save their cart and open it again on another device.

Value: high
Depends on: none
Out of scope: sharing a cart with other people.

Given a signed-in shopper with two items in the cart
When the shopper signs in on a second device
Then the cart shows the same two items

- [ ] A signed-in shopper sees the saved cart on a second device
- [ ] Items that are out of stock are marked when the cart is reopened
Metric: share of saved carts that are reopened within seven days.
```
