---
name: story-sprint-ready+story-portfolio
description: Merged skill that replaces `story-sprint-ready` and `story-portfolio`. Use for any user story ticket.
---

# Merged skill: story-sprint-ready + story-portfolio

This skill replaces `story-sprint-ready` and `story-portfolio`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `story-sprint-ready`

- The first line must be a level-1 Markdown heading that holds only the title, for example `# Save cart for later`.
- Name who the story is for on a line `Persona: <persona>`.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.
- Say how success will be measured on a line that starts with `Metric: `.
- List at least two acceptance criteria as open checkboxes, one per line, written `- [ ] ...`.

## Rules kept unchanged from `story-portfolio`

- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- Say what the story does not cover on a line that starts with `Out of scope: `.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Title: <title> Story points: <n> Epic: <epic name>

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
# Save cart for later
Story points: 5
Epic: Checkout
Persona: returning shopper

Value: high

Metric: The number of carts saved and retrieved successfully.

- [ ] The cart is saved to the user's account when they click the "Save for later" button.
- [ ] The cart is displayed correctly when the user logs in and clicks "View saved carts".
- [ ] The cart is updated in real-time when the user adds or removes items from the saved cart.

Given the user is logged in and has items in their cart.
When the user clicks the "Save for later" button.
Then the cart is saved to the user's account.

Out of scope: This story does not cover the functionality of deleting saved carts.

Depends on: none
```
