---
name: story-sprint-ready-and-portfolio
description: Write user story tickets that are ready for sprint planning and roll up into the product portfolio board. Combines sprint-readiness and portfolio tracking in one format.
---

# story-sprint-ready-and-portfolio

A story is ready for sprint planning and portfolio tracking when it shows its scope, value, size, testability, and relationship to other work—all in fixed places so teams can act without further questions.

## Rules

- The first line must be a level-1 Markdown heading that holds only the title, for example `# Save cart for later`.
- Put the estimate at the top, right under the title, as `Story points: <n>`.
- The line directly below the title must be `Epic: <epic name>`.
- The first line must also include the ticket ID in the format `Story <ticket ID>: <title>` — this takes precedence: use `Story <ID>: <title>` as the heading.
- Name who the story is for on a line `Persona: <persona>`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- Say what the story does not cover on a line that starts with `Out of scope: `.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.
- List at least two acceptance criteria as open checkboxes, one per line, written `- [ ] ...`.
- Say how success will be measured on a line that starts with `Metric: `.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
# Story SHOP-88: Save cart for later
Story points: 5
Epic: Checkout

Persona: returning shopper
The shopper saves the cart and continues on another device.

Given a signed-in shopper with two items in the cart
When the shopper signs in on a second device
Then the cart shows the same two items

- [ ] The saved cart is available on a second device
- [ ] Items that are out of stock are marked when the cart is reopened
Metric: share of saved carts that are reopened within seven days.
Value: high
Depends on: none
Out of scope: sharing a cart with other people.
```
