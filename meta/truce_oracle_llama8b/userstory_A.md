---
name: story-portfolio+story-sprint-ready
description: Merged skill that replaces `story-portfolio` and `story-sprint-ready`. Use for any user story ticket.
---

# Merged skill: story-portfolio + story-sprint-ready

This skill replaces `story-portfolio` and `story-sprint-ready`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `story-portfolio`

- The first line must be `Story <ticket ID>: <title>`, for example `Story SHOP-88: Save cart for later`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- Say what the story does not cover on a line that starts with `Out of scope: `.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.
- Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ] <criterion>`.

## Rules kept unchanged from `story-sprint-ready`

- Name who the story is for on a line `Persona: <persona>`.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.
- Say how success will be measured on a line that starts with `Metric: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the title, followed by "Story points: <n>" on the next line, then the line "Epic: <epic name>" below it.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
Story SHOP-88: Save cart for later
Persona: returning shopper
Value: high
Epic: Checkout
Story points: 5
Out of scope: deleting saved carts, editing saved carts
Depends on: none
- [ ] The shopper can view their saved cart on a different device
- [ ] The shopper can continue shopping from their saved cart
- [ ] The saved cart is deleted after 30 days
- [ ] The saved cart is deleted when the shopper logs out
Given the shopper is logged in and has items in their cart
When the shopper clicks the "Save cart for later" button
Then the cart is saved to the shopper's account
```
