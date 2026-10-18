---
name: alert-chatops+alert-pager
description: Merged skill that replaces `alert-chatops` and `alert-pager`. Use for any on-call alert notification.
---

# Merged skill: alert-chatops + alert-pager

This skill replaces `alert-chatops` and `alert-pager`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `alert-chatops`

- The p99 latency of checkout-api in prod-eu has been above the threshold for the last ten minutes.
- User impact: customers see slow page loads during checkout and some payments time out.
- First action: open the service dashboard and compare the latency curve with the last deploy marker.
- Likely causes:
- The payments provider is responding slowly and requests are queuing up.
- A traffic spike exhausted the database connection pool.
- Runbook: https://runbooks.example.com/checkout-latency
- Ack: reply ack ALR-7731

## Rules kept unchanged from `alert-pager`

- Link the runbook on a line `Runbook: <url>`.
- The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- Name the environment on a line `Env: <name>`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- To satisfy both rules, format the output as `[CRITICAL] <service>: <summary>` where `<service>` is either `checkout-api` or `pager`, and `<summary>` is a brief description of the alert, such as "ALR-7731 firing on checkout-api" or "The first line must be [CRITICAL] <service>: <summary>".
- "Alert: A recent deploy introduced a slow database query in the order summary path (Value: <current> (threshold <limit>))."

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
[CRITICAL] checkout-api: p99 latency is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.
```
