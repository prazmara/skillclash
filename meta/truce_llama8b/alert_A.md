---
name: alert-pager+alert-chatops
description: Merged skill that replaces `alert-pager` and `alert-chatops`. Use for any on-call alert notification.
---

# Merged skill: alert-pager + alert-chatops

This skill replaces `alert-pager` and `alert-chatops`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `alert-pager`

- Link the runbook on a line `Runbook: <url>`.
- The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
- The first line must be `[<SEVERITY>] <service>: <summary>` with the severity in capitals, one of `[CRITICAL]`, `[WARNING]`, `[INFO]`.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- Name the environment on a line `Env: <name>`.

## Rules kept unchanged from `alert-chatops`

- Give the runbook address on its own line in the form `Runbook: <url>`.
- List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`.
- Tell the responder where to start on a line that begins with `First action: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write a line that starts with "User impact: " followed by a description of what customers notice, and then on the same line, include "Value: <current> (threshold <limit>)".

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
[CRITICAL] checkout-api: p99 latency above threshold
User impact: Slow checkout times (Value: 2.4 s (threshold 1.5 s))
Env: prod-eu
For: 10m
Likely causes:
- High server load
- Network congestion
- Database query issues
First action: Check the server load and adjust as necessary, then investigate the database query performance. 
Runbook: https://runbooks.example.com/checkout-latency
Alert ID: ALR-7731
```
