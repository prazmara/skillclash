---
name: alert-pager+alert-chatops
description: Merged skill that replaces `alert-pager` and `alert-chatops`. Use for any on-call alert notification.
---

# Merged skill: alert-pager + alert-chatops

This skill replaces `alert-pager` and `alert-chatops`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `alert-pager`

- The first line must be `[<SEVERITY>] <service>: <summary>` with the severity in capitals, one of `[CRITICAL]`, `[WARNING]`, `[INFO]`.
- Give the measurement on a line `Value: <current> (threshold <limit>)`.
- Name the environment on a line `Env: <name>`.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- Link the runbook on a line `Runbook: <url>`.

## Rules kept unchanged from `alert-chatops`

- Tell the responder where to start on a line that begins with `First action: `.
- Describe what customers notice on a line that begins with `User impact: `.
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The message must be at most 400 characters including spaces and line breaks, and must include a line that reads exactly `Likely causes:` followed by at least three bullets starting with `- ` under it.
