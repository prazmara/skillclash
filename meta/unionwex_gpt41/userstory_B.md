---
name: story-sprint-ready+story-portfolio
description: Combined rules of `story-sprint-ready` and `story-portfolio`. Use for any user story ticket.
---

# Combined skill: story-sprint-ready + story-portfolio

Follow every rule below.

## Rules from `story-sprint-ready`

- Name who the story is for on a line `Persona: <persona>`.
- Put the estimate at the top, right under the title, as `Story points: <n>`.
- Say how success will be measured on a line that starts with `Metric: `.
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `.
- List at least two acceptance criteria as open checkboxes, one per line, written `- [ ] ...`.
- The first line must be a level-1 Markdown heading that holds only the title, for example `# Save cart for later`.

## Rules from `story-portfolio`

- Say what the story does not cover on a line that starts with `Out of scope: `.
- The line directly below the title must be `Epic: <epic name>`.
- The first line must be `Story <ticket ID>: <title>`, for example `Story SHOP-88: Save cart for later`.
- Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ] <criterion>`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.

If two rules cannot both hold, the rule from `story-sprint-ready` wins.

## Example

Request: Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.

Output:

```
# Save cart for later across devices
Epic: Checkout  
Story points: 5  
Persona: returning shopper  
Value: high  
Depends on: none  
Metric: Percentage of carts successfully restored on a different device  
Out of scope: Guest checkout cart saving and restoration

- [ ] Shoppers can save their cart while logged in and restore it on another device after logging in.
- [ ] Cart contents remain accurate and up-to-date when accessed from a different device.

Given a returning shopper is logged in and has items in their cart  
When they log in on a different device and access their cart  
Then the cart should display the same items as before, ready for checkout
```
