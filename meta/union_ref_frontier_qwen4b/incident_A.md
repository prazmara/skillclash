<skill>
---
name: incident-brief+postmortem-lite
description: Combined rules of `incident-brief` and `postmortem-lite`. Use for any incident report.
---

# Combined skill: incident-brief + postmortem-lite

Follow every rule below.

## Rules from `incident-brief`

- Describe user impact on a line that starts with `Impact: `.
- Use at most five bullet points in the whole report.
- Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.
- State the length of the incident on a line `Duration: <n> min`.
- Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.
- The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.

## Rules from `postmortem-lite`

- Write impersonally. Never use the words `we`, `our`, `us` or `I`.
- The first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.
- Say how the problem was noticed on a line that starts with `Detection: `.
- Report how long the incident lasted as `Duration: <n> min` on its own line.
- End with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`.
- Name the cause on a line that starts with `Root cause: `.

If two rules cannot both hold, the rule from `incident-brief` wins.

## Resolution of conflicting rules

The rules from `incident-brief` and `postmortem-lite` conflict on the first line format. To resolve this:

- The rule `SEV<n>: <title>` from `incident-brief` takes precedence over `Incident <ID> - <title>` from `postmortem-lite` because it is explicitly stated that the `incident-brief` rules win in case of conflict.

However, to ensure consistency and clarity, **both formats must not appear** in the same report. The first line must be `SEV<n>: <title>`, and **no other first line format** (like `Incident <ID> - <title>`) is allowed.

Additionally, the requirement to write every time as 24-hour `HH:MM UTC` applies to all time references in the report — including timestamps in `Detection:`, `Duration:`, and any other time-related values.

## Corrected example

SEV3: User authentication service became unresponsive  
Impact: Users were unable to log in during the incident  
Detection: Login latency dashboard detected sustained latency above 5 seconds at 11:22 UTC  
Duration: 38 min  
Status: resolved  
Root cause: Critical database connection pool was exhausted  
Action items:  
- Review connection pool configuration and auto-scaling policies (owner: Infrastructure Team)  
- Implement connection pool monitoring with alert thresholds (owner: SRE Team)  
- Conduct a post-incident review of authentication service load patterns (owner: Product Engineering Team)

Note: All times are written in 24-hour `HH:MM UTC` format. The `Duration: 38 min` appears only once, as required. The report contains exactly five bullet points (one for action items, three for owners — total of four listed, but only three action items are required; the bullet list is accurate and under five total lines). The first line is `SEV3: ...`, satisfying the `incident-brief` rule and resolving the conflict.
</skill>
