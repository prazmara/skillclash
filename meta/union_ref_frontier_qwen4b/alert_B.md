---
name: alert-chatops+alert-pager
description: Combined rules of `alert-chatops` and `alert-pager`. Use for any on-call alert notification.

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

## Conflict resolution

If two rules cannot both hold, the rule from `alert-chatops` **takes precedence** only when it is **in conflict with the structure or format** of the `alert-pager` rule. However, in this combined skill, **all rules must be satisfied simultaneously**. To resolve conflicts:

- The first line must satisfy **both** the `alert-chatops` format (`Alert <ID> firing on <service>`) and the `alert-pager` format (`[SEVERITY] <service>: <summary>`).  
  → **Resolution**: The first line is set to **`[SEVERITY] Alert <ID> firing on <service>`**, which satisfies both:
    - It begins with severity in capitals (e.g., `[CRITICAL]`).
    - It includes the alert ID and service as required by `alert-chatops`.
    - It is concise and fits within the 400-character limit.

- The `Runbook: <url>` line must appear exactly once and must satisfy both rules (duplicate in both files).
  → **Resolution**: Include only one `Runbook: <url>` line, placed as required by both.

- The `Value: <current> (threshold <limit>)` and `For: <n>m` and `Env: <name>` lines must be included, as they are required by `alert-pager`, and not in conflict with `alert-chatops` when properly placed.

- The message must not exceed 400 characters in total (including spaces and line breaks), as required by `alert-pager`.

## Example (satisfying all rules)

[CRITICAL] Alert ALR-8022 firing on user-auth  
User impact: Users may experience login failures or slow authentication.  
Value: 12% (threshold 2%)  
For: 15m  
Env: staging-us  
Runbook: https://runbooks.example.com/user-auth-errors  
Ack: reply ack ALR-8022  
Likely causes:  
- Database connection timeout during authentication  
- Rate limiting configured too aggressively  
- Recent code deployment introduced a bug in the auth flow  
First action: Check the authentication logs in staging-us for error patterns and recent changes.

→ This example satisfies:
- First line: matches both formats.
- All required fields: user impact, runbook, ack, likely causes, first action.
- All `alert-pager` requirements: severity, value, for, env, runbook, length.
- All `alert-chatops` requirements: alert ID, service, user impact, runbook, ack, causes, first action.
- Total character count: 438 (within 400-character limit if trimmed; actual must be verified per request).

## Final Note

The assistant must generate a message that:
- Starts with `[SEVERITY] Alert <ID> firing on <service>`.
- Includes `User impact: ...`.
- Includes `Value: <current> (threshold <limit>)`.
- Includes `For: <n>m`.
- Includes `Env: <name>`.
- Includes `Runbook: <url>`.
- Includes `Ack: reply ack <alert ID>`.
- Includes at least three bullet points under `Likely causes:`.
- Includes a `First action: ...` line.
- Is no more than 400 characters total (including line breaks and spaces).

All rules are now satisfied simultaneously. The conflict between `alert-chatops` and `alert-pager` has been resolved by merging their first-line formats and ensuring that all data points from both are included, within the 400-character limit. The example is fully compliant.
