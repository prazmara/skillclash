---
name: story-portfolio-sprint-ready
description: Write user story tickets that a delivery team can pull into a sprint and that roll up into the product portfolio board. Use for any user story or backlog ticket.
---

# story-portfolio-sprint-ready

This skill merges `story-portfolio` and `story-sprint-ready` and replaces both. A story is ready for sprint planning when the team sees its size first and can test and measure it without further questions. Product managers also group stories by epic and rank them by value, so every story states its epic, its value and its limits in fixed places.

Every rule of both skills is kept. Where two rules cannot both hold, `story-sprint-ready` wins.

## Rules

- The first line must be a level-1 Markdown heading that holds only the title, for example `# Save cart for later`. This is the `story-sprint-ready` rule. It overrides the `story-portfolio` rule that the first line is `Story <ticket ID>: <title>`, so the ticket ID must not appear in the first line. So that the ticket ID is not lost, give it on a line `Ticket: <ticket ID>` in the header block, below the `Epic:` line.
- Put the estimate at the top, right under the title, as `Story points: <n>`. It is the second line. This is the `story-sprint-ready` rule. It overrides the part of the `story-portfolio` rule that puts the epic on the line directly below the title.
- Give the epic on a line `Epic: <epic name>`. Because the second line belongs to the estimate, the epic goes on the third line, directly below the `Story points:` line.
- Name who the story is for on a line `Persona: <persona>`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.
- Say what the story does not cover on a line that starts with `Out of scope: `.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.
- List at least two acceptance criteria as open checkboxes, one per line, each of the form `- [ ] <criterion>`.
- Say how success will be measured on a line that starts with `Metric: `.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
# Save cart for later
Story points: 5
Epic: Checkout
Ticket: SHOP-88

Persona: returning shopper
The shopper saves the cart and continues on another device.

Value: high
Depends on: none
Out of scope: sharing a cart with other people.

Given a signed-in shopper with two items in the cart
When the shopper signs in on a second device
Then the cart shows the same two items

- [ ] The saved cart is available on a second device
- [ ] Items that are out of stock are marked when the cart is reopened
Metric: share of saved carts that are reopened within seven days.
```
