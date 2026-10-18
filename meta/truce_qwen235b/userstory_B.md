---
name: story-sprint-ready+story-portfolio
description: Merged skill that replaces `story-sprint-ready` and `story-portfolio`. Use for any user story ticket.
---

# Merged skill: story-sprint-ready + story-portfolio

This skill replaces `story-sprint-ready` and `story-portfolio`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `story-sprint-ready`

- Name who the story is for on a line `Persona: <persona>`.
- Say how success will be measured on a line that starts with `Metric: `.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.
- List at least two acceptance criteria as open checkboxes, one per line, written `- [ ] ...`.
- The first line must be a level-1 Markdown heading that holds only the title, for example `# Save cart for later`.

## Rules kept unchanged from `story-portfolio`

- Say what the story does not cover on a line that starts with `Out of scope: `.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The line directly below the title must be `Epic: <epic name>`, and the next line must be `Story points: <n>`.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
# Save cart for later
Epic: Checkout
Story points: 5
Persona: returning shopper
Value: high
Metric: Increase in cart recovery rate measured by percentage of saved carts that convert within 7 days
Out of scope: Syncing wishlists or browsing history across devices
Depends on: none
- [ ] User can save their current cart with a single action
- [ ] Saved cart is accessible when logging in from any device
Given the user has items in their cart and is logged in
When the user selects "Save Cart for Later"
Then the cart is saved and accessible in their account across all devices
```
