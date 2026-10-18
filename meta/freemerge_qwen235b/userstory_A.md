---
name: story-portfolio-sprint
description: Write user story tickets that roll up into the product portfolio board and are ready for sprint planning. Combines portfolio alignment with delivery readiness.
---

# story-portfolio-sprint

Product managers group stories by epic and rank them by value, while delivery teams need clear size, testability, and scope. This skill ensures stories are both strategically aligned and sprint-ready.

## Rules

- The first line must be `Story <ticket ID>: <title>`, for example `Story SHOP-88: Save cart for later`.
- The line directly below the title must be `Epic: <epic name>`.
- Put the estimate on the next line as `Story points: <n>`.
- Name who the story is for on a line `Persona: <persona>`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- Say how success will be measured on a line that starts with `Metric: `.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.
- Say what the story does not cover on a line that starts with `Out of scope: `.
- Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ] <criterion>`.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.

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
Metric: share of saved carts that are reopened within seven days.
Out of scope: sharing a cart with other people.

- [ ] A signed-in shopper sees the saved cart on a second device
- [ ] Items that are out of stock are marked when the cart is reopened

Given a signed-in shopper with two items in the cart
When the shopper signs in on a second device
Then the cart shows the same two items
```
