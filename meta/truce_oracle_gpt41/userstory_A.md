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

- Directly below the title, write `Epic: <epic name>`, and on the next line, write `Story points: <n>`. This order ensures both required lines appear immediately after the title, each on its own line with the correct label and format.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
Story SHOP-88: Save cart for later  
Epic: Checkout  
Story points: 5  
Value: high  
Persona: returning shopper  
Out of scope: Guest checkout, cart sharing, and persistent cart for anonymous users  
Depends on: none  
Acceptance criteria:  
- [ ] Shoppers can save their cart while logged in  
- [ ] Saved cart is accessible from any device after logging in  
- [ ] Cart contents persist after logout and login on a different device  
Given a returning shopper is logged in and has items in their cart  
When they log out and log in on another device  
Then their saved cart should be restored with all previously added items  
Metric: Percentage of logged-in users successfully retrieving saved carts across devices
```
