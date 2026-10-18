---
name: alert-pager+alert-chatops
description: Merged skill that replaces `alert-pager` and `alert-chatops`. Use for any on-call alert notification.
---

# Merged skill: alert-pager + alert-chatops

This skill replaces `alert-pager` and `alert-chatops`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `alert-pager`

- Link the runbook on a line `Runbook: <url>`.
- The first line must be `[<SEVERITY>] <service>: <summary>` with the severity in capitals, one of `[CRITICAL]`, `[WARNING]`, `[INFO]`.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- Name the environment on a line `Env: <name>`.
- Give the measurement on a line `Value: <current> (threshold <limit>)`.

## Rules kept unchanged from `alert-chatops`

- Describe what customers notice on a line that begins with `User impact: `.
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`.
- Tell the responder where to start on a line that begins with `First action: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write a message that fits entirely within 400 characters, including spaces and line breaks, and after a line reading exactly `Likely causes:`, list at least three likely causes as bullets that each start with `- `.

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
[CRITICAL] checkout-api: p99 latency is 2.4s, above 1.5s threshold
For: 10m
Env: prod-eu
Value: 2.4s (threshold 1.5s)
User impact: Users experience slow checkouts or timeouts.
Ack: reply ack ALR-7731
First action: Check service logs and recent deploys.
Runbook: https://runbooks.example.com/checkout-latency
Likely causes:
- Backend dependency slowness
- Recent code deployment issues
- Database performance degradation
```
