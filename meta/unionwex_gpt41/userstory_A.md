---
name: story-portfolio+story-sprint-ready
description: Combined rules of `story-portfolio` and `story-sprint-ready`. Use for any user story ticket.
---

# Combined skill: story-portfolio + story-sprint-ready

Follow every rule below.

## Rules from `story-portfolio`

- Say what the story does not cover on a line that starts with `Out of scope: `.
- The line directly below the title must be `Epic: <epic name>`.
- The first line must be `Story <ticket ID>: <title>`, for example `Story SHOP-88: Save cart for later`.
- Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ] <criterion>`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.

## Rules from `story-sprint-ready`

- Name who the story is for on a line `Persona: <persona>`.
- Put the estimate at the top, right under the title, as `Story points: <n>`.
- Say how success will be measured on a line that starts with `Metric: `.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.
- List at least two acceptance criteria as open checkboxes, one per line, written `- [ ] ...`.
- The first line must be a level-1 Markdown heading that holds only the title, for example `# Save cart for later`.

If two rules cannot both hold, the rule from `story-portfolio` wins.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
Story SHOP-88: Save cart for later  
Epic: Checkout  
Story points: 5  
Persona: returning shopper  
Value: high  
Depends on: none  
Metric: Percentage of carts successfully restored on a different device

As a returning shopper, I want to save my cart and access it later from another device, so that I can continue shopping without losing my selected items.

Acceptance criteria:
- [ ] Shoppers can save their cart while logged in and retrieve it from any device after logging in.
- [ ] Cart contents persist across sessions and devices for logged-in users.
- [ ] If items are out of stock or unavailable when restoring the cart, the user is notified.

Test scenario:  
Given a logged-in shopper with items in their cart  
When they log in on a different device  
Then their saved cart is restored with all available items

Out of scope: Guest users saving carts without an account; merging carts from multiple sessions.
```
