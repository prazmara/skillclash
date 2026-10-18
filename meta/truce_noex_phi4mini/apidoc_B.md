---
name: apidoc-integrator-guide+apidoc-reference-card
description: Merged skill that replaces `apidoc-integrator-guide` and `apidoc-reference-card`. Use for any REST endpoint documentation entry.
---

# Merged skill: apidoc-integrator-guide + apidoc-reference-card

This skill replaces `apidoc-integrator-guide` and `apidoc-reference-card`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `apidoc-integrator-guide`

- GET /v1/invoices/{id}
- Stability: stable
- Content-Type: application/json
- | Name | In | Type | Description |
- $ curl -H "Authorization: Bearer $TOKEN" https://api.example.com/v1/invoices/inv_123
- Responses:

## Rules kept unchanged from `apidoc-reference-card`

- State the required permission on a line `Auth: <scope>`.
- Say whether repeating the call is safe on a line `Idempotent: yes` or `Idempotent: no`.
- Show one example call on a line that starts with `$ curl `.
- The first line must be a level-3 Markdown heading with the method and path in backticks, for example ### `GET /v1/invoices/{id}`.
- Keep the whole entry to at most 90 words.
- State the API version that introduced the endpoint on a line `Since: v<version>`, for example `Since: v1.4`.
