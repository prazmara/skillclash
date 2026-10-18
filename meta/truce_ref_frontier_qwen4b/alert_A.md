---
name: alert-pager+alert-chatops
description: Merged skill that replaces `alert-pager` and `alert-chatops`. Use for any on-call alert notification.
---

# Merged skill: alert-pager + alert-chatops

This skill replaces `alert-pager` and `alert-chatops`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `alert-pager`

- Link the runbook on a line `Runbook: <url>`.
- The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- Name the environment on a line `Env: <name>`.
- Give the measurement on a line `Value: <current> (threshold <limit>)`.

## Rules kept unchanged from `alert-chatops`

- Describe what customers notice on a line that begins with `User impact: `.
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`.
- List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`.
- Tell the responder where to start on a line that begins with `First action: `.

## Reconciled rules (each one satisfies a rule of both skills at once)

- [<SEVERITY>] <service>: <summary> Alert <ID> firing on <service>

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
[CRITICAL] checkout-api: P99 latency at 2.4 s, above 1.5 s threshold, for 10m. Alert ALR-7731 firing on checkout-api.  
Env: prod-eu  
Value: 2.4 s (threshold 1.5 s)  
For: 10m  
Runbook: https://runbooks.example.com/checkout-latency  
User impact: Customers experience slow checkout process.  
Ack: reply ack ALR-7731  
Likely causes:  
- Database query timeout during order processing  
- Increased load from peak shopping hours  
- Network latency between microservices  
First action: Check database query logs for slow operations in the checkout-api service.
```
