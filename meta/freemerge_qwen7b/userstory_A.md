---
name: story-comprehensive
description: Write user story tickets that roll up into the product portfolio board and are ready for sprint planning. Use for any user story or backlog ticket.
---

# story-comprehensive

A comprehensive user story is ready for sprint planning and groups stories by epic and ranks them by value, ensuring all necessary details are included for both product management and development teams.

## Rules

- The first line must be `Story <ticket ID>: <title>`, for example `Story SHOP-88: Save cart for later`.
- The line directly below the title must be `Epic: <epic name>`.
- Name who the story is for on a line `Persona: <persona>`.
- Put the estimate at the top, right under the title, as `Story points: <n>`.
- Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ] <criterion>`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.
- Say what the story does not cover on a line that starts with `Out of scope: `.
- Say how success will be measured on a line that starts with `Metric: `.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
Story SHOP-88: Save cart for later
Epic: Checkout
Persona: returning shopper
Story points: 5

Shoppers can save their cart and open it again on another device.

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
