<skill>
---
name: story-portfolio+story-sprint-ready
description: Merged skill that replaces `story-portfolio` and `story-sprint-ready`. Use for any user story ticket. Follow every rule below.
---

# Merged skill: story-portfolio + story-sprint-ready

This skill replaces `story-portfolio` and `story-sprint-ready`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `story-portfolio`

- Say what the story does not cover on a line that starts with `Out of scope: `.
- The line directly below the title must be `Epic: <epic name>`.
- Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ] <criterion>`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.

## Rules kept unchanged from `story-sprint-ready`

- Name who the story is for on a line `Persona: <persona>`.
- Put the estimate at the top, right under the title, as `Story points: <n>`.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.
- Say how success will be measured on a line that starts with `Metric: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Story <ticket ID>: <title> # <title>

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
Story SHOP-88: Shoppers want to save their cart and come back to it later on another device. # SHOP-88  
Epic: Checkout  
Story points: 5  
Persona: returning shopper  
Value: medium  
Out of scope: Requires integration with device-specific authentication.  
Depends on: none  
- [ ] Cart is saved securely with user authentication  
- [ ] User can access their saved cart from any device using the same login  
- [ ] Cart data is synchronized across devices without data loss  
Metric: Cart is accessible within 2 seconds of login on any device  
Given the user is logged in on one device  
When they navigate away from the cart page  
Then the cart is saved and remains accessible on another device upon login  
Given the user logs in on a new device  
When they visit the cart page  
Then they see their previously saved cart items and totals
```
</skill>
