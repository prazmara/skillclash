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

- Title and Estimate should be formatted as follows: `Story points: <n> - Epic: <epic name>` This way, the story points are placed at the top, right under the title, and the epic name is directly below the title, as specified by both rules.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
Story SHOP-88: Save cart for later (5 points) - Epic: Checkout

Persona: returning shopper

Story points: 5 - Epic: Checkout

Value: medium
Out of scope: Shopping as a guest, Saving cart for less than 30 days
Depends on: none

- [ ] As a returning shopper, I want to save my cart so that I can come back to it later on another device.
- [ ] Given I have items in my cart,
- [ ] When I choose to save my cart,
- [ ] Then my cart is saved and I can access it later on another device.

Metric: Percentage of returning shoppers who can save and access their cart on another device.
```
