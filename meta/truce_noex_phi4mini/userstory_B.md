---
name: story-sprint-ready+story-portfolio
description: Merged skill that replaces `story-sprint-ready` and `story-portfolio`. Use for any user story ticket.
---

# Merged skill: story-sprint-ready + story-portfolio

This skill replaces `story-sprint-ready` and `story-portfolio`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `story-sprint-ready`

- Name who the story is for on a line `Persona: <persona>`.
- Say how success will be measured on a line that starts with `Metric: `.

## Rules kept unchanged from `story-portfolio`

- Say what the story does not cover on a line that starts with `Out of scope: `.
- The line directly below the title must be `Epic: <epic name>`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Combine the title into a level-1 Markdown heading and a story title in the format `Story <ticket ID>: <title>`. For example, use `# Save cart for later` as the Markdown heading and `Story SHOP-88: Save cart for later` as the story title.
- - [ ] Acceptance criteria for story-sprint-ready: [ ] The story must be ready for the next sprint. - [ ] Acceptance criteria for story-sprint-ready: [ ] The story must be reviewed and approved by the product owner. - [ ] <criterion> The story must be written in a clear and concise manner. - [ ] <criterion> The story must include all necessary details for implementation.
- Place the estimate as `Story points: <n>` right under the title, followed by the business value rating as `Value: high`, `Value: medium`, or `Value: low`. Ensure the title, story points, and value rating are clearly separated and formatted as specified.
- "Add a test scenario in the format of 'Given', 'When', 'Then' and list any blocking tickets starting with 'Depends on: '; if there are no blocking tickets, write 'Depends on: none'."
