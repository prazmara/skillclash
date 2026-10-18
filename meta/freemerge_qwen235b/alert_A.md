---
name: alert-notifier
description: Write on-call alert notifications for both pager/SMS and chat channels. Combines concise paging format with detailed chat guidance.
---

# alert-notifier

This skill produces a unified alert message that satisfies both pager/SMS and chat channel requirements. When in conflict, pager rules take precedence.

## Rules

- The first line must be `[<SEVERITY>] <service>: <summary>` with the severity in capitals, one of `[CRITICAL]`, `[WARNING]`, `[INFO]`.
- Immediately after the first line, include a line `Alert <ID> firing on <service>` if an alert ID is provided.
- Link the runbook on a line `Runbook: <url>`.
- The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- Name the environment on a line `Env: <name>`.
- Give the measurement on a line `Value: <current> (threshold <limit>)`.
- Describe what customers notice on a line that begins with `User impact: `.
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`.
- List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`.
- Tell the responder where to start on a line that begins with `First action: `.

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
[CRITICAL] checkout-api: p99 latency above threshold
Alert ALR-7731 firing on checkout-api
Value: 2.4s (threshold 1.5s)
Env: prod-eu
For: 10m
User impact: customers see slow page loads during checkout and some payments time out.
First action: open the service dashboard and compare the latency curve with the last deploy marker.
Likely causes:
- A recent deploy introduced a slow database query in the order summary path.
- The payments provider is responding slowly and requests are queuing up.
- A traffic spike exhausted the database connection pool.
Runbook: https://runbooks.example.com/checkout-latency
Ack: reply ack ALR-7731
```
