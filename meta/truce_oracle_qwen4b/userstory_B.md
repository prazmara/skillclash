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

- Put the estimate at the top, right under the title, as `Story points: <n>`. Below that, on the next line, include `Epic: <epic name>`.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
# Save cart for later

Story points: 5  
Epic: Checkout  
Persona: returning shopper  
Value: high  
Out of scope: saving cart for non-returning shoppers  
Depends on: none  

Given a returning shopper is on a device and adds items to their cart  
When they navigate away and later returns to the site on a different device  
Then their cart should be restored with all previously added items  

Given a shopper has items in their cart on one device  
When they close the browser and return to the site on a different device  
Then they should see their cart with the same items  

Metric: Cart recovery rate reaches 95% across devices  
- [ ] Implement cart persistence across devices using session tokens  
- [ ] Ensure cart data is securely stored and transmitted  
- [ ] Add user notification when cart is restored on a new device
```
