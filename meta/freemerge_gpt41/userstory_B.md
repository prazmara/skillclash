---
name: story-sprint-portfolio
description: Write user story tickets that are ready for sprint planning and portfolio tracking. Use for any user story or backlog ticket.
---

# story-sprint-portfolio

A story is ready for sprint planning and portfolio tracking when the team sees its size first, can test and measure it without further questions, and product managers can group and rank it by epic and value.

## Rules

- The first line must be a level-1 Markdown heading that holds only the title, for example `# Save cart for later`.
- The line directly below the title must be `Story points: <n>`.
- Name who the story is for on a line `Persona: <persona>`.
- Say how success will be measured on a line that starts with `Metric: `.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.
- List at least two acceptance criteria as open checkboxes, one per line, written `- [ ] ...`.
- The next line after the acceptance criteria must be `Epic: <epic name>`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.
- Say what the story does not cover on a line that starts with `Out of scope: `.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
# Save cart for later
Story points: 5

Persona: returning shopper
The shopper saves the cart and continues on another device.

Given a signed-in shopper with two items in the cart
When the shopper signs in on a second device
Then the cart shows the same two items

- [ ] The saved cart is available on a second device
- [ ] Items that are out of stock are marked when the cart is reopened
Epic: Checkout
Value: high
Depends on: none
Out of scope: sharing a cart with other people.
Metric: share of saved carts that are reopened within seven days.
```
