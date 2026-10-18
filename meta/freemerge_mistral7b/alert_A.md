<skill>
---
name: alert-pager-chatops
description: Write on-call alert notifications for both the pager and incident chat channels. Use for any alert or paging message. If rules conflict, the rule from `alert-pager` wins.
---

# alert-pager-chatops

## Rules

- Link the runbook on a line `Runbook: <url>`.
- The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.
- The first line must be `[<SEVERITY>] <service>: <summary>` with the severity in capitals, one of `[CRITICAL]`, `[WARNING]`, `[INFO]`.
- Say how long the condition has held on a line `For: <n>m`, in whole minutes.
- Name the environment on a line `Env: <name>`.
- Give the measurement on a line `Value: <current> (threshold <limit>)`.
- If the message fits, include the user impact, first action, likely causes, and ack command from `alert-chatops`.

## Example

Request: Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.

Output:

```
[CRITICAL] checkout-api: p99 latency above threshold
Value: 2.4s (threshold 1.5s)
Env: prod-eu
For: 10m
Runbook: https://runbooks.example.com/checkout-latency

The p99 latency of checkout-api in prod-eu has been above the threshold for the last ten minutes.
User impact: customers see slow page loads during checkout and some payments time out.
First action: open the service dashboard and compare the latency curve with the last deploy marker.
Likely causes:
- A recent deploy introduced a slow database query in the order summary path.
- The payments provider is responding slowly and requests are queuing up.
- A traffic spike exhausted the database connection pool.
Ack: reply ack ALR-7731
```
</skill>
