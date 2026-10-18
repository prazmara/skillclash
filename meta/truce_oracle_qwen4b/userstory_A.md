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

- The line directly below the title must be `Epic: <epic name>`, and immediately below that, place `Story points: <n>` as the estimate.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
Story SHOP-88: Save cart for later  
Value: medium  
Out of scope: Saving cart for users who are not returning shoppers  
Depends on: none  
Persona: returning shopper  
Epic: Checkout  
Story points: 5  
Metric: Number of returning shoppers who save their cart and return to complete purchase  
- [ ] Cart is saved securely when user leaves the checkout page  
- [ ] User can log in on a different device and view their saved cart  
- [ ] Saved cart data is synchronized across devices without data loss  
Given the user is on a checkout page and decides to leave  
When the user closes the browser or navigates away  
Then the cart is saved to their profile and remains accessible on future visits  

Given the user logs in on a different device  
When they navigate to the checkout page  
Then they can see their previously saved cart items
```
