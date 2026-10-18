---
name: alert-pager-chatops
description: Write on-call alert notifications for both pager and SMS channels (for direct phone viewing) and incident chat channels (for chat-based response). Use for any alert or paging message. When rules conflict, the `alert-pager` rules take precedence.

# alert-pager-chatops

Pages are read on a phone lock screen at night. The responder must see severity, service and numbers at once, and the message must not be cut off. Chat alerts must enable responders to start working from the alert alone, so they include user impact, actions, and likely causes.

## Rules

- Link the runbook on a line `Runbook: <url>`.
- The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
- The first line must be `[<SEVERITY>] <service>: <summary>` with the severity in capitals, one of `[CRITICAL]`, `[WARNING]`, `[INFO]`.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- Name the environment on a line `Env: <name>`.
- Give the measurement on a line `Value: <current> (threshold <limit>)`.
- Describe what customers notice on a line that begins with `User impact: `.
- Explain how to acknowledge with the line `Ack: reply ack <alert ID>`.
- List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`.
- Tell the responder where to start on a line that begins with `First action: `.

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
[CRITICAL] checkout-api: p99 latency above threshold
Value: 2.4s (threshold 1.5s)
Env: prod-eu
For: 10m
User impact: customers see slow page loads during checkout and some payments time out.
Likely causes:
- A recent deploy introduced a slow database query in the order summary path.
- The payments provider is responding slowly and requests are queuing up.
- A traffic spike exhausted the database connection pool.
First action: open the service dashboard and compare the latency curve with the last deploy marker.
Runbook: https://runbooks.example.com/checkout-latency
Ack: reply ack ALR-7731
```
