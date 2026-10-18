<skill>
---
name: story-sprint-and-portfolio-ready
description: Write user story tickets that a delivery team can pull into a sprint and roll up into the product portfolio board. Use for any user story or backlog ticket.
---

# story-sprint-and-portfolio-ready

A story is ready for sprint planning and product portfolio when the team sees its size, value, and can test and measure it without further questions.

## Rules

- The first line must be a level-1 Markdown heading that holds only the title, for example `# Save cart for later`.
- Say what the story does on a line that starts with `Shoppers can ` or similar.
- Put the estimate at the top, right under the title, as `Story points: <n>`.
- Say who the story is for on a line `Persona: <persona>`.
- Say how success will be measured on a line that starts with `Metric: `.
- Say what the story does not cover on a line that starts with `Out of scope: `.
- The line directly below the title must be `Epic: <epic name>`.
- Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ] <criterion>`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
# Save cart for later
Story points: 5
Shoppers can save their cart and open it again on another device.
Persona: returning shopper
The shopper saves the cart and continues on another device.

Given a signed-in shopper with two items in the cart
When the shopper signs in on a second device
Then the cart shows the same two items

Out of scope: sharing a cart with other people.
Epic: Checkout
Value: high
Depends on: none

- [ ] The saved cart is available on a second device
- [ ] Items that are out of stock are marked when the cart is reopened
Metric: share of saved carts that are reopened within seven days.
```
