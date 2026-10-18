---
name: story-portfolio
description: Write user story tickets that roll up into the product portfolio board. Use for any user story or backlog ticket.
---

# story-portfolio

Product managers group stories by epic and rank them by value, so every story states its epic, its value and its limits in fixed places.

## Rules

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

Shoppers can save their cart and open it again on another device.

Value: high
Depends on: none
Out of scope: sharing a cart with other people.

- [ ] A signed-in shopper sees the saved cart on a second device
- [ ] Items that are out of stock are marked when the cart is reopened
```
