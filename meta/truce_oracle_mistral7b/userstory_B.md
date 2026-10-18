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

- Write the title followed by a blank line, then start with "Story points: <n>", followed by another blank line, and finally write "Epic: <epic name>". The estimate and epic name should be on separate lines, both under the title. Example: ``` Title of the Story Story points: 3 Epic: Portfolio Management ```

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
# Save cart for later

Persona: returning shopper

Given the user is logged in,
When the user saves their cart,
Then the cart is saved and can be accessed from another device.

Metric: Successful cart saving and retrieval across devices.

- [ ] Cart is saved and retrieved correctly.
- [ ] User can access saved cart from another device.

Value: high

Out of scope: Cart saving and retrieval for guest users.

Depends on: none

Story points: 5

Epic: Checkout
```
