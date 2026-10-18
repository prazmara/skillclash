---
name: story-portfolio+story-sprint-ready
description: Merged skill that replaces `story-portfolio` and `story-sprint-ready`. Use for any user story ticket.
---

# Merged skill: story-portfolio + story-sprint-ready

This skill replaces `story-portfolio` and `story-sprint-ready`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `story-portfolio`

- The first line must be `Story <ticket ID>: <title>`, for example `Story SHOP-88: Save cart for later`.
- Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.
- List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.

## Rules kept unchanged from `story-sprint-ready`

- Put the estimate at the top, right under the title, as `Story points: <n>`
- Say how success will be measured on a line that starts with `Metric: `
- Add one test scenario as three lines that start with `Given `, `When ` and `Then `

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the output in the following format: ``` Persona: <persona> Out of scope: (List items separated by commas) ``` Replace `<persona>` with the name of the persona the story is for, and list the items that are out of scope for the story, each separated by a comma.
- Write the title followed by a level-1 Markdown heading format, then on the next line write `Epic: <epic name>`. Example: ``` # Title of the Story Epic: Epic Name ```
- Write the output as follows: - [ ] Story Portfolio: The AI assistant can generate a portfolio of stories based on user preferences. - [ ] Sprint Ready: - [ ] The AI assistant can generate at least two unique stories based on user preferences. - [ ] The AI assistant can save and retrieve the generated stories for future use.
