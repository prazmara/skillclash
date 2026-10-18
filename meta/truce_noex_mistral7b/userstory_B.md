---
name: story-sprint-ready+story-portfolio
description: Merged skill that replaces `story-sprint-ready` and `story-portfolio`. Use for any user story ticket.
---

# Merged skill: story-sprint-ready + story-portfolio

This skill replaces `story-sprint-ready` and `story-portfolio`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `story-sprint-ready`

- Put the estimate at the top, right under the title, as `Story points: <n>`
- Say how success will be measured on a line that starts with `Metric: `
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `

## Rules kept unchanged from `story-portfolio`

- The first line must be `Story <ticket ID>: <title>`, for example `Story SHOP-88: Save cart for later`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write: `Persona: <persona>\nOut of scope: <list of topics not covered in the story>`
- Write the output in the following format: ``` # Title Epic: <epic name> ``` Ensure that the title is a level-1 Markdown heading and the epic name follows directly below it, on the next line.
- Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ]`, where the first criterion is for the `story-sprint-ready` skill and the second criterion is for the `story-portfolio` skill. Each criterion should be written on a separate line, as follows: ``` - [ ] <criterion for story-sprint-ready> - [ ] <criterion for story-portfolio> ```
