<skill>
---
name: story-sprint-portfolio-ready
description: Write user story tickets that can be pulled into a sprint and roll up into the product portfolio board. Use for any user story or backlog ticket.
---

# story-sprint-portfolio-ready

A story is ready for sprint planning and product management when the team sees its size first and can test and measure it without further questions, and it states its epic, its value, and its limits in fixed places.

## Rules

- Name who the story is for on a line `Persona: <persona>`.
- Put the estimate at the top, right under the title, as `Story points: <n>`.
- Say how success will be measured on a line that starts with `Metric: `.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.
- List at least two acceptance criteria as open checkboxes, one per line, written `- [ ] ...`.
- The first line must be a level-1 Markdown heading that holds only the title, for example `# Save cart for later`.
- The line directly below the title must be `Epic: <epic name>`.
- Say what the story does not cover on a line that starts with `Out of scope: `.
- Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ] <criterion>`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
# Save cart for later
Story points: 5

Persona: returning shopper
The shopper saves the cart and continues on another device.

Epic: Checkout

Given a signed-in shopper with two items in the cart
When the shopper signs in on a second device
Then the cart shows the same two items

- [ ] The saved cart is available on a second device
- [ ] Items that are out of stock are marked when the cart is reopened

Out of scope: sharing a cart with other people.

Value: high
Depends on: none
Metric: share of saved carts that are reopened within seven days.
```
</skill>
