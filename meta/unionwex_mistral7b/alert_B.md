---
name: alert-chatops+alert-pager
description: Combined rules of `alert-chatops` and `alert-pager`. Use for any on-call alert notification.
---

# Combined skill: alert-chatops + alert-pager

Follow every rule below.

## Rules from `alert-chatops`

- The first line must be `Alert <ID> firing on <service>`, for example `Alert ALR-7731 firing on checkout-api`.
- Describe what customers notice on a line that begins with `User impact: `.
- Give the runbook address on its own line in the form `Runbook: <url>`.
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`.
- List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`.
- Tell the responder where to start on a line that begins with `First action: `.

## Rules from `alert-pager`

- Link the runbook on a line `Runbook: <url>`.
- The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
- The first line must be `[<SEVERITY>] <service>: <summary>` with the severity in capitals, one of `[CRITICAL]`, `[WARNING]`, `[INFO]`.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- Name the environment on a line `Env: <name>`.
- Give the measurement on a line `Value: <current> (threshold <limit>)`.

If two rules cannot both hold, the rule from `alert-chatops` wins.

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
[CRITICAL] prod-eu: Alert ALR-7731 firing on checkout-api

User impact: The p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes.

Env: prod-eu

Value: 2.4 s (threshold 1.5 s)

Likely causes:
- Increased traffic to the checkout-api service
- Database or network issues
- Code changes causing performance degradation

First action: Investigate the cause of the high latency and take corrective action. For: 30 minutes

Runbook: https://runbooks.example.com/checkout-latency

Ack: reply ack ALR-7731
```
