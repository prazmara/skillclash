---
name: story-portfolio+story-sprint-ready
description: Merged skill that replaces `story-portfolio` and `story-sprint-ready`. Use for any user story ticket.
---

# Merged skill: story-portfolio + story-sprint-ready

This skill replaces `story-portfolio` and `story-sprint-ready`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `story-portfolio`

- Say what the story does not cover on a line that starts with `Out of scope: `.
- The first line must be `Story <ticket ID>: <title>`, for example `Story SHOP-88: Save cart for later`.
- Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ] <criterion>`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.

## Rules kept unchanged from `story-sprint-ready`

- Name who the story is for on a line `Persona: <persona>`.
- Say how success will be measured on a line that starts with `Metric: `.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The line directly below the title must be `Story points: <n>`, and the line below that must be `Epic: <epic name>`.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
Story SHOP-88: Save cart for later
Story points: 5
Epic: Checkout
Persona: returning shopper
Value: high
Out of scope: Applying discounts automatically when returning to the cart, syncing browsing history across devices
Depends on: none
Metric: Percentage of users who save cart and return within 7 days to complete purchase
- [ ] User can save their current cart with a single action
- [ ] Saved cart is accessible when logging in from a different device
- [ ] Saved cart persists for up to 30 days
Given a user has items in their cart and is logged in
When the user selects "Save cart for later"
Then the cart is saved and accessible on any device where the user logs in
```
