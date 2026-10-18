---
name: story-portfolio+story-sprint-ready
description: Merged skill that replaces `story-portfolio` and `story-sprint-ready`. Use for any user story ticket.
---

# Merged skill: story-portfolio + story-sprint-ready

This skill replaces `story-portfolio` and `story-sprint-ready`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `story-portfolio`

- Say what the story does not cover on a line that starts with `Out of scope: `.
- The line directly below the title must be `Epic: <epic name>`.

## Rules kept unchanged from `story-sprint-ready`

- Name who the story is for on a line `Persona: <persona>`.
- Say how success will be measured on a line that starts with `Metric: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Combine the first line as a level-1 Markdown heading with the ticket ID and title, for example, `# Story SHOP-88: Save cart for later`.
- - [ ] <criterion 1> - [ ] <criterion 2> - [ ] <criterion 3> - [ ] <criterion 4>
- Combine the business value rating and story points estimate into a single output line, formatted as follows: "Title: [Title], Value: [high/medium/low], Story points: [n]". Ensure the title, value, and story points are clearly labeled and separated by commas.
- "List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none. Add one test scenario as three lines that start with `Given `, `When ` and `Then `, ensuring the `Depends on: none` line is included if no blocking tickets are present."
