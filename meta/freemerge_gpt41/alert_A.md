---
name: alert-pager-chatops
description: Write on-call alert notifications for both pager/SMS and incident chat channels. Combines concise, high-urgency pager alerts with actionable, detailed chat notifications.
---

# alert-pager-chatops

This skill writes alert notifications suitable for both pager/SMS and incident chat channels. Pager messages must be concise and fit on a phone lock screen, while chat messages provide actionable detail for responders. All rules from both alert-pager and alert-chatops are enforced; where rules conflict, the alert-pager rule takes precedence.

## Rules

- The whole pager message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
- The first line of the pager section must be `[<SEVERITY>] <service>: <summary>` with the severity in capitals, one of `[CRITICAL]`, `[WARNING]`, `[INFO]`.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- Name the environment on a line `Env: <name>`.
- Give the measurement on a line `Value: <current> (threshold <limit>)`.
- Link the runbook on a line `Runbook: <url>`.
- The chat section must start with `Alert <ID> firing on <service>`.
- Describe what customers notice on a line that begins with `User impact: `.
- Give the runbook address on its own line in the form `Runbook: <url>`.
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`.
- List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`.
- Tell the responder where to start on a line that begins with `First action: `.

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
[PAGER]
[CRITICAL] checkout-api: p99 latency above threshold
Value: 2.4s (threshold 1.5s)
Env: prod-eu
For: 10m
Runbook: https://runbooks.example.com/checkout-latency

[CHAT]
Alert ALR-7731 firing on checkout-api
User impact: customers see slow page loads during checkout and some payments time out.
First action: open the service dashboard and compare the latency curve with the last deploy marker.
Likely causes:
- A recent deploy introduced a slow database query in the order summary path.
- The payments provider is responding slowly and requests are queuing up.
- A traffic spike exhausted the database connection pool.
Runbook: https://runbooks.example.com/checkout-latency
Ack: reply ack ALR-7731
```
