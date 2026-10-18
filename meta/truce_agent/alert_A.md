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

- List exactly three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`, and keep each cause to a phrase of at most four words. The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks, so keep every other line to one short phrase as well.

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
[CRITICAL] checkout-api: p99 latency above threshold
Value: 2.4s (threshold 1.5s)
Env: prod-eu
For: 10m
User impact: checkout is slow for customers
First action: check the service dashboard
Likely causes:
- slow database query
- slow payments provider
- exhausted connection pool
Runbook: https://runbooks.example.com/checkout-latency
Ack: reply ack ALR-7731
```
