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

- The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks. Include a line that reads exactly `Likely causes:` followed by at least three bullets starting with `- `; the entire content must stay within the 400-character limit.

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
[CRITICAL] checkout-api: High p99 latency  
Value: 2.4s (threshold 1.5s)  
Env: prod-eu  
For: 10m  
Runbook: https://runbooks.example.com/checkout-latency  
User impact: Users experience slow checkout, may abandon purchases  
First action: Check recent deploys and error rates in monitoring  
Ack: reply ack ALR-7731  
Likely causes:  
- Downstream service degradation  
- Recent code deployment introducing inefficiency  
- Database connection pool exhaustion
```
