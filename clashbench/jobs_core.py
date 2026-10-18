"""Eight ClashBench jobs. Each job: two skills for the same artifact, six rules each
(con, e1, e2, e3, sh, ent), eight held-out requests, and two hand-written witnesses that
prove the maximum satisfiable set is jointly satisfiable under either precedence."""
import re

from spec import Job, Req, Skill, first, has_line, jparse, last, lines, n_lines, nonempty

TICKET = r"[A-Z]{2,}-\d+"


def sql_body(out):
    return "\n".join(l for l in out.split("\n") if not l.strip().startswith("--"))


def bullets_after(out, heading_pat):
    """Bullet lines that follow the first line matching heading_pat, up to the next non-bullet line."""
    ls = [l.strip() for l in out.split("\n")]
    for i, l in enumerate(ls):
        if re.search(heading_pat, l):
            got = []
            for m in ls[i + 1:]:
                if not m:
                    if got:
                        break
                    continue
                if m.startswith(("- ", "* ")):
                    got.append(m)
                else:
                    break
            return got
    return []


def words(out):
    return len(out.split())


JOBS = []

# --------------------------------------------------------------------------- 1. commit message
JOBS.append(Job(
    id="commit", artifact="commit message",
    example_request="Write the commit message: add retry with backoff to the payment webhook handler. Ticket PAY-311. Author: Lena Ortiz. Component: webhooks.",
    facts_hint="a ticket ID such as PAY-311, the author's full name, and the affected component",
    skills={
        "A": Skill(
            name="conventional-commits",
            description="Write commit messages in the team's Conventional Commits format. Use for any commit message.",
            intro="Commit messages in this repository follow Conventional Commits so that release tooling can parse them.",
            reqs=[
                Req("con", "con", "Start the subject line with a lowercase type prefix and a colon, one of `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. Nothing may come before the type.",
                    lambda o, r: bool(re.match(r"^(feat|fix|docs|refactor|test|chore)(\([\w-]+\))?: \S", first(o)))),
                Req("e1", "excl", "Explain the motivation in a body line that starts with `Why: `.",
                    lambda o, r: has_line(o, r"^Why: \S")),
                Req("e2", "excl", "Add a body line `Risk: low`, `Risk: medium` or `Risk: high`.",
                    lambda o, r: has_line(o, r"^Risk: (low|medium|high)$")),
                Req("e3", "excl", "Add a line that starts with `BREAKING CHANGE: ` and says `none` when nothing breaks.",
                    lambda o, r: has_line(o, r"^BREAKING CHANGE: \S")),
                Req("sh", "sh", "State whether the change was tested with a line `Tested: yes` or `Tested: no`.",
                    lambda o, r: has_line(o, r"^Tested: (yes|no)$")),
                Req("ent", "ent", "The very last line of the message must be the sign-off `Signed-off-by: <author name>`.",
                    lambda o, r: bool(re.match(r"^Signed-off-by: \S", last(o)))),
            ],
            example="fix: add retry with backoff to payment webhook\n\nWhy: transient gateway timeouts dropped webhook events.\nRisk: low\nBREAKING CHANGE: none\nTested: yes\n\nSigned-off-by: Lena Ortiz"),
        "B": Skill(
            name="ticket-first-commits",
            description="Write commit messages that lead with the tracker ticket. Use for any commit message.",
            intro="Every commit must be traceable to a tracker ticket, so the ticket leads the message.",
            reqs=[
                Req("con", "con", "Start the subject line with the ticket ID in square brackets, for example `[PAY-311] `. Nothing may come before the bracket.",
                    lambda o, r: bool(re.match(r"^\[" + TICKET + r"\] \S", first(o)))),
                Req("e1", "excl", "Describe the change in the body as a bulleted list with at least two bullets that start with `- `.",
                    lambda o, r: n_lines(o, r"^- \S") >= 2),
                Req("e2", "excl", "Name the affected component in a line `Component: <name>`.",
                    lambda o, r: has_line(o, r"^Component: \S")),
                Req("e3", "excl", "Say how to revert in a line that starts with `Rollback: `.",
                    lambda o, r: has_line(o, r"^Rollback: \S")),
                Req("sh", "sh", "Record test status as `Tested: yes` or `Tested: no` on its own line.",
                    lambda o, r: has_line(o, r"^Tested: (yes|no)$")),
                Req("ent", "ent", "Finish the message with a trailer block that contains the line `Refs: <TICKET-ID>`.",
                    lambda o, r: any(re.match(r"^Refs: " + TICKET + r"$", l) for l in nonempty(o)[-3:])),
            ],
            example="[PAY-311] Add retry with backoff to payment webhook\n\n- Retry failed webhook deliveries three times\n- Use exponential backoff between attempts\nComponent: webhooks\nRollback: revert this commit\nTested: yes\n\nRefs: PAY-311"),
    },
    tasks=[
        "Write the commit message: fix a null pointer crash in the invoice PDF renderer when the customer has no billing address. Ticket BILL-482. Author: Dana Kim. Component: invoicing.",
        "Write the commit message: add pagination to the audit log API. Ticket AUD-77. Author: Omar Haddad. Component: audit-api.",
        "Write the commit message: update the onboarding guide with the new SSO steps. Ticket DOC-140. Author: Priya Nair. Component: docs.",
        "Write the commit message: refactor the cache layer to use a single Redis client. Ticket PERF-903. Author: Tomas Varga. Component: cache.",
        "Write the commit message: add unit tests for the currency rounding helper. Ticket FIN-58. Author: Aiko Tanaka. Component: money-utils.",
        "Write the commit message: remove the deprecated v1 search endpoint. Ticket API-611. Author: Chloe Martin. Component: search-api.",
        "Write the commit message: fix the flaky login test by waiting for the session cookie. Ticket QA-219. Author: Samir Patel. Component: e2e-tests.",
        "Write the commit message: add a dark mode toggle to the settings page. Ticket UI-334. Author: Elena Rossi. Component: settings-ui.",
    ],
    witness={
        "A": "fix: add retry with backoff to payment webhook\n\nWhy: transient gateway timeouts dropped webhook events.\n- Retry failed webhook deliveries three times\n- Use exponential backoff between attempts\nComponent: webhooks\nRisk: low\nBREAKING CHANGE: none\nRollback: revert this commit\nTested: yes\n\nRefs: PAY-311\nSigned-off-by: Lena Ortiz",
        "B": "[PAY-311] Add retry with backoff to payment webhook\n\nWhy: transient gateway timeouts dropped webhook events.\n- Retry failed webhook deliveries three times\n- Use exponential backoff between attempts\nComponent: webhooks\nRisk: low\nBREAKING CHANGE: none\nRollback: revert this commit\nTested: yes\n\nRefs: PAY-311\nSigned-off-by: Lena Ortiz",
    }))

# --------------------------------------------------------------------------- 2. pull request description
JOBS.append(Job(
    id="pr", artifact="pull request description",
    example_request="Write the pull request description: add rate limiting to the login endpoint. Ticket AUTH-207. Reviewer: @sam. Labels: security, backend.",
    facts_hint="a ticket ID such as AUTH-207, one reviewer handle such as @sam, and two lowercase labels",
    skills={
        "A": Skill(
            name="pr-structured",
            description="Write pull request descriptions with the team's fixed section layout. Use for any pull request.",
            intro="Reviewers skim many pull requests. A fixed, short layout lets them find what they need.",
            reqs=[
                Req("con", "con", "The first line must be a level-1 Markdown heading with the title, starting with `# `.",
                    lambda o, r: first(o).startswith("# ")),
                Req("e1", "excl", "Include a section with the exact heading `## Summary`.",
                    lambda o, r: has_line(o, r"^## Summary$")),
                Req("e2", "excl", "Include a section with the exact heading `## Testing`.",
                    lambda o, r: has_line(o, r"^## Testing$")),
                Req("e3", "excl", "Under Testing, list at least two checklist items written as `- [ ]` or `- [x]`.",
                    lambda o, r: n_lines(o, r"^- \[[ xX]\] \S") >= 2),
                Req("sh", "sh", "Give the tracker ticket on its own line as `Ticket: <ID>`.",
                    lambda o, r: has_line(o, r"^Ticket: " + TICKET + r"$")),
                Req("ent", "ent", "Keep the whole description to at most 120 words.",
                    lambda o, r: 0 < words(o) <= 120),
            ],
            example="# Add rate limiting to the login endpoint\n\nTicket: AUTH-207\n\n## Summary\nLimits login attempts to five per minute per IP address.\n\n## Testing\n- [x] Unit tests for the limiter\n- [ ] Load test on staging"),
        "B": Skill(
            name="pr-release-ready",
            description="Write pull request descriptions that release managers can act on. Use for any pull request.",
            intro="Release managers decide from the description alone whether a change can ship, so it must cover risk and rollback.",
            reqs=[
                Req("con", "con", "The first line must be plain text of the form `PR: <title>`. Do not use a Markdown heading for the title.",
                    lambda o, r: first(o).startswith("PR: ")),
                Req("e1", "excl", "Include a section with the exact heading `## Rollback`.",
                    lambda o, r: has_line(o, r"^## Rollback$")),
                Req("e2", "excl", "Name the reviewers on a line `Reviewers: @handle`.",
                    lambda o, r: has_line(o, r"^Reviewers: @\w+")),
                Req("e3", "excl", "List labels on a line `Labels: ` followed by lowercase labels separated by a comma and a space.",
                    lambda o, r: has_line(o, r"^Labels: [a-z0-9-]+(, [a-z0-9-]+)*$")),
                Req("sh", "sh", "Put the ticket on a separate line in the form `Ticket: <ID>`.",
                    lambda o, r: has_line(o, r"^Ticket: " + TICKET + r"$")),
                Req("ent", "ent", "Include a `## Risks` section with at least two bullet points that start with `- `.",
                    lambda o, r: len(bullets_after(o, r"^## Risks$")) >= 2),
            ],
            example="PR: Add rate limiting to the login endpoint\n\nTicket: AUTH-207\nReviewers: @sam\nLabels: security, backend\n\nThis change introduces a sliding-window rate limiter in front of the login endpoint. Each IP address may attempt to log in five times per minute. Further attempts receive a 429 response with a Retry-After header, and the event is written to the security audit log so that the on-call engineer can see bursts of failed logins.\n\n## Risks\n- Users behind a shared office IP address may reach the limit during busy periods and see errors.\n- If the Redis cluster that stores the counters is unavailable, the limiter fails open and offers no protection.\n- The new audit log entries increase log volume during an attack.\n\n## Rollback\nRevert this pull request and flush the limiter keys from Redis. No schema or configuration migration is involved, so the rollback is safe at any time."),
    },
    tasks=[
        "Write the pull request description: migrate the user table primary key from int to bigint. Ticket DB-915. Reviewer: @nina. Labels: database, migration.",
        "Write the pull request description: add CSV export to the monthly usage report. Ticket REP-204. Reviewer: @omar. Labels: reports, feature.",
        "Write the pull request description: replace the homegrown retry loop in the email sender with the shared retry library. Ticket MAIL-63. Reviewer: @lucia. Labels: email, refactor.",
        "Write the pull request description: upgrade the image thumbnail service to libvips 8.15. Ticket IMG-388. Reviewer: @wei. Labels: dependencies, media.",
        "Write the pull request description: enforce two-factor authentication for admin accounts. Ticket SEC-1021. Reviewer: @farah. Labels: security, auth.",
        "Write the pull request description: cache the product catalog response for sixty seconds. Ticket CAT-457. Reviewer: @jonas. Labels: performance, catalog.",
        "Write the pull request description: fix the off-by-one error in the pagination of search results. Ticket SRCH-72. Reviewer: @mei. Labels: search, bugfix.",
        "Write the pull request description: add structured JSON logging to the billing worker. Ticket OBS-530. Reviewer: @pablo. Labels: logging, billing.",
    ],
    witness={
        "A": "# Add rate limiting to the login endpoint\n\nTicket: AUTH-207\nReviewers: @sam\nLabels: security, backend\n\n## Summary\nLimits login attempts to five per minute per IP address.\n\n## Testing\n- [x] Unit tests for the limiter\n- [ ] Load test on staging\n\n## Risks\n- Shared office IPs may hit the limit\n- Redis outage disables the limiter\n\n## Rollback\nRevert this PR and flush the limiter keys.",
        "B": "PR: Add rate limiting to the login endpoint\n\nTicket: AUTH-207\nReviewers: @sam\nLabels: security, backend\n\n## Summary\nLimits login attempts to five per minute per IP address.\n\n## Testing\n- [x] Unit tests for the limiter\n- [ ] Load test on staging\n\n## Risks\n- Shared office IPs may hit the limit\n- Redis outage disables the limiter\n\n## Rollback\nRevert this PR and flush the limiter keys.",
    }, max_new_tokens=420))

# --------------------------------------------------------------------------- 3. SQL query
_KW_LO = r"\b(select|from|where|join|group by|order by)\b"
_KW_UP = r"\b(SELECT|FROM|WHERE|JOIN|GROUP BY|ORDER BY)\b"
JOBS.append(Job(
    id="sql", artifact="SQL query",
    example_request="Write the SQL query: revenue per country for orders created in January 2026, top 20 countries. Table orders(id, country, amount, created_at, deleted_at). Owning team: growth-analytics.",
    facts_hint="the table with its columns (including created_at and deleted_at), a date range, an aggregate to compute, and the owning team",
    skills={
        "A": Skill(
            name="sql-house-style",
            description="Write SQL in the analytics house style. Use for any SQL query.",
            intro="Queries are reviewed by analysts who rely on a consistent style and on safety defaults.",
            reqs=[
                Req("con", "con", "Write all SQL keywords in UPPERCASE (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`).",
                    lambda o, r: bool(re.search(r"\bSELECT\b", sql_body(o))) and not re.search(_KW_LO, sql_body(o))),
                Req("e1", "excl", "Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`.",
                    lambda o, r: bool(re.search(r"\bas\s+\w+_(cnt|sum|avg)\b", sql_body(o), re.I))),
                Req("e2", "excl", "Always exclude soft-deleted rows with the filter `deleted_at IS NULL`.",
                    lambda o, r: bool(re.search(r"deleted_at\s+is\s+null", sql_body(o), re.I))),
                Req("e3", "excl", "Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.",
                    lambda o, r: bool(re.search(r"\bround\s*\(", sql_body(o), re.I))),
                Req("sh", "sh", "Always end the query with a `LIMIT` clause.",
                    lambda o, r: bool(re.search(r"\blimit\s+\d+", sql_body(o), re.I))),
                Req("ent", "ent", "The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`.",
                    lambda o, r: first(o).startswith("-- Purpose: ")),
            ],
            example="-- Purpose: revenue per country for January 2026\nSELECT\n    o.country,\n    ROUND(SUM(o.amount), 2) AS revenue_sum\nFROM orders AS o\nWHERE o.deleted_at IS NULL\n  AND o.created_at >= '2026-01-01'\n  AND o.created_at <= '2026-01-31'\nGROUP BY o.country\nORDER BY revenue_sum DESC\nLIMIT 20;"),
        "B": Skill(
            name="sql-warehouse-conventions",
            description="Write SQL that follows the data warehouse conventions. Use for any SQL query.",
            intro="Warehouse queries are composed from CTEs and must be attributable to an owning team.",
            reqs=[
                Req("con", "con", "Write all SQL keywords in lowercase (`select`, `from`, `where`, `join`, `group by`, `order by`).",
                    lambda o, r: bool(re.search(r"\bselect\b", sql_body(o))) and not re.search(_KW_UP, sql_body(o))),
                Req("e1", "excl", "Stage the source rows in a CTE named `base` (`with base as (...)`) and select from it.",
                    lambda o, r: bool(re.search(r"\bwith\s+base\s+as\s*\(", sql_body(o), re.I))),
                Req("e2", "excl", "Qualify source tables with the `analytics.` schema.",
                    lambda o, r: "analytics." in sql_body(o)),
                Req("e3", "excl", "Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `between` or `<=` for dates.",
                    lambda o, r: ">=" in sql_body(o) and bool(re.search(r"<(?![=>])", sql_body(o))) and "<=" not in sql_body(o) and not re.search(r"\bbetween\b", sql_body(o), re.I)),
                Req("sh", "sh", "Cap the result size: every query needs a `limit` clause.",
                    lambda o, r: bool(re.search(r"\blimit\s+\d+", sql_body(o), re.I))),
                Req("ent", "ent", "Put a header comment `-- Owner: <team>` at the top of the query.",
                    lambda o, r: any(l.startswith("-- Owner: ") for l in nonempty(o)[:3])),
            ],
            example="-- Owner: growth-analytics\nwith base as (\n    select\n        o.country,\n        o.amount\n    from analytics.orders as o\n    where o.created_at >= '2026-01-01'\n      and o.created_at < '2026-02-01'\n)\nselect\n    country,\n    sum(amount) as revenue\nfrom base\ngroup by country\norder by revenue desc\nlimit 20"),
    },
    tasks=[
        "Write the SQL query: number of signups per plan for users created in March 2026, largest first, top 10. Table users(id, plan, created_at, deleted_at). Owning team: lifecycle.",
        "Write the SQL query: average order amount per sales channel for orders created in the first quarter of 2026, top 15. Table orders(id, channel, amount, created_at, deleted_at). Owning team: revenue-ops.",
        "Write the SQL query: total refund amount per reason for refunds created in February 2026, top 25. Table refunds(id, reason, amount, created_at, deleted_at). Owning team: payments.",
        "Write the SQL query: number of support tickets per priority created in the week starting 2026-04-06, top 5. Table tickets(id, priority, created_at, deleted_at). Owning team: support-insights.",
        "Write the SQL query: average session length in seconds per device type for sessions created on 2026-05-01, top 10. Table sessions(id, device_type, length_seconds, created_at, deleted_at). Owning team: product-analytics.",
        "Write the SQL query: total shipping cost per warehouse for shipments created in December 2025, top 30. Table shipments(id, warehouse, cost, created_at, deleted_at). Owning team: logistics.",
        "Write the SQL query: number of failed logins per country created between 2026-06-01 and 2026-06-15, top 20. Table login_events(id, country, outcome, created_at, deleted_at). Owning team: security.",
        "Write the SQL query: average invoice total per customer segment for invoices created in 2025, top 12. Table invoices(id, segment, total, created_at, deleted_at). Owning team: finance-data.",
    ],
    witness={
        "A": "-- Purpose: revenue per country for January 2026\n-- Owner: growth-analytics\nWITH base AS (\n    SELECT\n        o.country,\n        o.amount\n    FROM analytics.orders AS o\n    WHERE o.deleted_at IS NULL\n      AND o.created_at >= '2026-01-01'\n      AND o.created_at < '2026-02-01'\n)\nSELECT\n    country,\n    ROUND(SUM(amount), 2) AS revenue_sum\nFROM base\nGROUP BY country\nORDER BY revenue_sum DESC\nLIMIT 20;",
        "B": "-- Purpose: revenue per country for January 2026\n-- Owner: growth-analytics\nwith base as (\n    select\n        o.country,\n        o.amount\n    from analytics.orders as o\n    where o.deleted_at is null\n      and o.created_at >= '2026-01-01'\n      and o.created_at < '2026-02-01'\n)\nselect\n    country,\n    round(sum(amount), 2) as revenue_sum\nfrom base\ngroup by country\norder by revenue_sum desc\nlimit 20;",
    }))

# --------------------------------------------------------------------------- 4. incident report
JOBS.append(Job(
    id="incident", artifact="incident report",
    example_request="Write the incident report: the checkout API returned 500 errors for 42 minutes on 2026-02-11, from 09:14 to 09:56 UTC, because the TLS certificate on the payments gateway expired. Incident ID INC-2291, severity 2. Detected by the synthetic checkout probe.",
    facts_hint="the incident ID such as INC-2291, the severity (1 to 4), start and end times in UTC, the duration in minutes, the cause, and how it was detected",
    skills={
        "A": Skill(
            name="incident-brief",
            description="Write short incident reports for the status channel. Use for any incident report or postmortem.",
            intro="Status-channel readers need the severity, the impact and the current state in a few lines.",
            reqs=[
                Req("con", "con", "The first line must be `SEV<n>: <title>`, for example `SEV2: Checkout API returned 500 errors`.",
                    lambda o, r: bool(re.match(r"^SEV[1-4]: \S", first(o)))),
                Req("e1", "excl", "Describe user impact on a line that starts with `Impact: `.",
                    lambda o, r: has_line(o, r"^Impact: \S")),
                Req("e2", "excl", "Write every time as 24-hour `HH:MM UTC`, for example `09:14 UTC`.",
                    lambda o, r: bool(re.search(r"\b\d{2}:\d{2} UTC\b", o))),
                Req("e3", "excl", "Give the current state on a line `Status: resolved`, `Status: monitoring` or `Status: investigating`.",
                    lambda o, r: has_line(o, r"^Status: (resolved|monitoring|investigating)$")),
                Req("sh", "sh", "State the length of the incident on a line `Duration: <n> min`.",
                    lambda o, r: has_line(o, r"^Duration: \d+ min$")),
                Req("ent", "ent", "Use at most five bullet points in the whole report.",
                    lambda o, r: n_lines(o, r"^[-*] \S") <= 5 and len(nonempty(o)) > 1),
            ],
            example="SEV2: Checkout API returned 500 errors\n\nImpact: customers could not complete checkout.\nDuration: 42 min\nTimeline: errors began at 09:14 UTC and ended at 09:56 UTC after the certificate was renewed.\nStatus: resolved"),
        "B": Skill(
            name="postmortem-lite",
            description="Write blameless postmortem summaries with follow-up actions. Use for any incident report or postmortem.",
            intro="A postmortem is only useful if it names the cause and assigns follow-up work.",
            reqs=[
                Req("con", "con", "The first line must be `Incident <ID> - <title>`, for example `Incident INC-2291 - Checkout API returned 500 errors`.",
                    lambda o, r: bool(re.match(r"^Incident INC-\d+ - \S", first(o)))),
                Req("e1", "excl", "Name the cause on a line that starts with `Root cause: `.",
                    lambda o, r: has_line(o, r"^Root cause: \S")),
                Req("e2", "excl", "Say how the problem was noticed on a line that starts with `Detection: `.",
                    lambda o, r: has_line(o, r"^Detection: \S")),
                Req("e3", "excl", "Write impersonally. Never use the words `we`, `our`, `us` or `I`.",
                    lambda o, r: len(nonempty(o)) > 1 and not re.search(r"\b(we|We|WE|our|Our|us|I)\b", o)),
                Req("sh", "sh", "Report how long the incident lasted as `Duration: <n> min` on its own line.",
                    lambda o, r: has_line(o, r"^Duration: \d+ min$")),
                Req("ent", "ent", "End with a line `Action items:` followed by at least three bullets, each naming an owner as `(owner: <team>)`.",
                    lambda o, r: sum("(owner: " in b for b in bullets_after(o, r"^Action items:$")) >= 3),
            ],
            example="Incident INC-2291 - Checkout API returned 500 errors\n\nDuration: 42 min\nRoot cause: the TLS certificate on the payments gateway expired.\nDetection: the synthetic checkout probe alerted the on-call engineer.\n\nAction items:\n- Add certificate expiry monitoring (owner: platform team)\n- Automate certificate renewal (owner: payments team)\n- Add a runbook entry for certificate failures (owner: SRE)\n- Review alert routing for gateway errors (owner: SRE)\n- Audit all certificates expiring this quarter (owner: security team)\n- Schedule a follow-up review (owner: incident manager)"),
    },
    tasks=[
        "Write the incident report: search results were empty for 18 minutes on 2026-03-04, from 14:02 to 14:20 UTC, because a bad index alias was deployed. Incident ID INC-3120, severity 3. Detected by a customer report.",
        "Write the incident report: push notifications were delayed for 95 minutes on 2026-01-22, from 06:30 to 08:05 UTC, because the message queue ran out of disk. Incident ID INC-2877, severity 2. Detected by the queue depth alert.",
        "Write the incident report: the admin dashboard was unreachable for 27 minutes on 2026-04-17, from 21:11 to 21:38 UTC, because of a misconfigured firewall rule. Incident ID INC-3304, severity 3. Detected by the uptime monitor.",
        "Write the incident report: payments were double-charged for 12 minutes on 2026-05-09, from 11:48 to 12:00 UTC, because a retry job ran twice. Incident ID INC-3411, severity 1. Detected by the finance reconciliation check.",
        "Write the incident report: image uploads failed for 64 minutes on 2026-02-28, from 17:05 to 18:09 UTC, because the object storage credentials were rotated without updating the service. Incident ID INC-3015, severity 2. Detected by the error-rate alert.",
        "Write the incident report: the mobile app showed stale prices for 150 minutes on 2026-06-02, from 02:10 to 04:40 UTC, because the cache invalidation worker crashed. Incident ID INC-3522, severity 3. Detected by an internal tester.",
        "Write the incident report: email verification links returned 404 for 33 minutes on 2026-03-19, from 08:27 to 09:00 UTC, because of a routing change in the API gateway. Incident ID INC-3188, severity 2. Detected by the signup funnel alert.",
        "Write the incident report: the data warehouse nightly load was late by 240 minutes on 2026-07-07, finishing at 07:00 UTC instead of 03:00 UTC, because an upstream export job hung. Incident ID INC-3690, severity 4. Detected by the freshness check.",
    ],
    witness={
        "A": "SEV2: Checkout API returned 500 errors\n\nImpact: customers could not complete checkout.\nDuration: 42 min\nTimeline: errors began at 09:14 UTC and ended at 09:56 UTC after the certificate was renewed.\nRoot cause: the TLS certificate on the payments gateway expired.\nDetection: the synthetic checkout probe alerted the on-call engineer.\nStatus: resolved\n\nAction items:\n- Add certificate expiry monitoring (owner: platform team)\n- Automate certificate renewal (owner: payments team)\n- Add a runbook entry for certificate failures (owner: SRE)",
        "B": "Incident INC-2291 - Checkout API returned 500 errors\n\nImpact: customers could not complete checkout.\nDuration: 42 min\nTimeline: errors began at 09:14 UTC and ended at 09:56 UTC after the certificate was renewed.\nRoot cause: the TLS certificate on the payments gateway expired.\nDetection: the synthetic checkout probe alerted the on-call engineer.\nStatus: resolved\n\nAction items:\n- Add certificate expiry monitoring (owner: platform team)\n- Automate certificate renewal (owner: payments team)\n- Add a runbook entry for certificate failures (owner: SRE)",
    }, max_new_tokens=380))

# --------------------------------------------------------------------------- 5. Python function
_PY_A_EX = '''```python
def compute_median(values: list[float]) -> float:
    """Return the median of a list of numbers.

    Args:
        values: The numbers to summarize.

    Returns:
        The median value.

    Example:
        >>> compute_median([1, 3, 2])
        2
    """
    if not values:
        raise ValueError("values must not be empty")
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2
```'''
_PY_B_EX = '''```python
from __future__ import annotations

__all__ = ["median"]


def median(values):
    """Return the median of a list of numbers.

    Parameters
    ----------
    values : list of float
        The numbers to summarize.

    Returns
    -------
    float
        The median value.

    Examples
    --------
    >>> median([1, 3, 2])
    2
    """
    ordered = sorted(values)
    mid = len(ordered) // 2
    # NOTE: an even count averages the two middle values
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2
```

Complexity: O(n log n)'''
_PY_W = '''```python
from __future__ import annotations

__all__ = ["compute_median"]


def compute_median(values: list[float]) -> float:
    """Return the median of a list of numbers.

<<DOC>>

    Complexity: O(n log n)
    """
    if not values:
        raise ValueError("values must not be empty")
    ordered = sorted(values)
    mid = len(ordered) // 2
    # NOTE: an even count averages the two middle values
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2
```'''
_GOOGLE = "    Args:\n        values: The numbers to summarize.\n\n    Returns:\n        The median value.\n\n    Example:\n        >>> compute_median([1, 3, 2])\n        2"
_NUMPY = "    Parameters\n    ----------\n    values : list of float\n        The numbers to summarize.\n\n    Returns\n    -------\n    float\n        The median value.\n\n    Examples\n    --------\n    >>> compute_median([1, 3, 2])\n    2"


def _dash_line(o):
    return any(re.fullmatch(r"-{3,}", l.strip()) for l in o.split("\n"))


def _numpy_params(o):
    ls = [l.strip() for l in o.split("\n")]
    return any(ls[i] == "Parameters" and re.fullmatch(r"-{3,}", ls[i + 1]) for i in range(len(ls) - 1))


JOBS.append(Job(
    id="python", artifact="Python function",
    example_request="Write a Python function that returns the median of a list of numbers.",
    facts_hint="one small, self-contained function to write, with its input and output described",
    skills={
        "A": Skill(
            name="python-google-style",
            description="Write Python functions in the team's Google style. Use whenever Python code is requested.",
            intro="Library code here follows the Google Python style so that documentation tools can parse it.",
            reqs=[
                Req("con", "con", "Write the docstring in Google style with `Args:` and `Returns:` sections. Never use underlined section headers.",
                    lambda o, r: has_line(o, r"^Args:$") and not _dash_line(o)),
                Req("e1", "excl", "Annotate every parameter and the return value with type hints.",
                    lambda o, r: bool(re.search(r"def \w+\([^)]*:[^)]*\)\s*->", o))),
                Req("e2", "excl", "Reject invalid input by raising `ValueError`.",
                    lambda o, r: "raise ValueError" in o),
                Req("e3", "excl", "Name the function with a verb prefix: `get_`, `compute_`, `build_`, `parse_`, `validate_`, `find_`, `count_`, `format_` or `to_`.",
                    lambda o, r: bool(re.search(r"def (get|compute|build|parse|validate|find|count|format|to)_\w+\(", o))),
                Req("sh", "sh", "Include at least one usage example with a `>>>` prompt in the docstring.",
                    lambda o, r: ">>>" in o),
                Req("ent", "ent", "Reply with one Python code block and nothing outside it.",
                    lambda o, r: r.strip().startswith("```") and r.strip().endswith("```") and r.count("```") == 2),
            ],
            example=_PY_A_EX),
        "B": Skill(
            name="python-numpy-style",
            description="Write Python functions in the scientific computing group's NumPy style. Use whenever Python code is requested.",
            intro="Scientific code here follows NumPy conventions and is written for readers who study the algorithm.",
            reqs=[
                Req("con", "con", "Write the docstring in NumPy style, with a `Parameters` header underlined by dashes. Never use `Args:`.",
                    lambda o, r: _numpy_params(o) and not has_line(o, r"^Args:$")),
                Req("e1", "excl", "Start the module with `from __future__ import annotations`.",
                    lambda o, r: "from __future__ import annotations" in o),
                Req("e2", "excl", "Mark each non-obvious step with a comment that starts with `# NOTE:`.",
                    lambda o, r: "# NOTE:" in o),
                Req("e3", "excl", "Export the function by defining `__all__`.",
                    lambda o, r: bool(re.search(r"__all__\s*=", o))),
                Req("sh", "sh", "Show a doctest-style example that uses `>>>`.",
                    lambda o, r: ">>>" in o),
                Req("ent", "ent", "State the time complexity as `Complexity: O(...)`.",
                    lambda o, r: bool(re.search(r"Complexity: O\(", r))),
            ],
            example=_PY_B_EX),
    },
    tasks=[
        "Write a Python function that returns the n most frequent words in a text string.",
        "Write a Python function that merges two sorted lists of integers into one sorted list.",
        "Write a Python function that converts a duration in seconds to an `HH:MM:SS` string.",
        "Write a Python function that checks whether a string of brackets is balanced.",
        "Write a Python function that computes the moving average of a list of numbers for a given window size.",
        "Write a Python function that flattens a nested list of integers of arbitrary depth.",
        "Write a Python function that returns the longest common prefix of a list of strings.",
        "Write a Python function that groups a list of dictionaries by the value of a given key.",
    ],
    witness={"A": _PY_W.replace("<<DOC>>", _GOOGLE), "B": _PY_W.replace("<<DOC>>", _NUMPY)},
    max_new_tokens=520))

# --------------------------------------------------------------------------- 6. customer support reply
_CONTR = r"\b\w+(n['’]t|['’]ll|['’]re|['’]ve|['’]m)\b"
JOBS.append(Job(
    id="support", artifact="support reply",
    example_request="Write the support reply to Maria Lopez (ticket 48213): her invoice export fails with a timeout. Engineering deployed a fix today; she should clear her browser cache and retry. Help article: https://help.example.com/invoice-export. Agent: Jordan.",
    facts_hint="the customer's full name, a numeric ticket number, the problem and the fix, a help article URL under https://help.example.com/, and the agent's first name",
    skills={
        "A": Skill(
            name="support-formal",
            description="Write customer support replies in the formal enterprise tone. Use for any reply to a customer.",
            intro="Enterprise customers forward our replies to their own management, so replies are formal and easy to audit.",
            reqs=[
                Req("con", "con", "Open with `Dear <full name>,` on the first line.",
                    lambda o, r: bool(re.match(r"^Dear [A-Z][\w.' -]+,$", first(o)))),
                Req("e1", "excl", "Cite the case as `Ticket #<number>`.",
                    lambda o, r: bool(re.search(r"Ticket #\d+", o))),
                Req("e2", "excl", "Do not use contractions such as `don't`, `we'll` or `you're`.",
                    lambda o, r: len(nonempty(o)) > 1 and not re.search(_CONTR, o)),
                Req("e3", "excl", "Give the next steps as a numbered list with at least two steps (`1.`, `2.`).",
                    lambda o, r: has_line(o, r"^1\. \S") and has_line(o, r"^2\. \S")),
                Req("sh", "sh", "Sign with the agent's name followed by a line that ends with `Support Team`.",
                    lambda o, r: has_line(o, r"Support Team$")),
                Req("ent", "ent", "Never place a URL inside the body text. Links may appear only on a final line that starts with `Links:`.",
                    lambda o, r: len(nonempty(o)) > 1 and all(l.strip().startswith("Links:") for l in o.split("\n") if "http" in l)),
            ],
            example="Dear Maria Lopez,\n\nThank you for contacting us about Ticket #48213. The invoice export timeout has been fixed by our engineering team today.\n\nPlease follow these steps:\n1. Clear your browser cache.\n2. Run the invoice export again.\n\nKind regards,\nJordan\nAcme Support Team"),
        "B": Skill(
            name="support-friendly",
            description="Write customer support replies in the friendly self-serve tone. Use for any reply to a customer.",
            intro="Most customers want a quick, warm answer and a pointer to the help center so they can solve it themselves.",
            reqs=[
                Req("con", "con", "Open with `Hi <first name>!` on the first line.",
                    lambda o, r: bool(re.match(r"^Hi [A-Z][\w'-]+!$", first(o)))),
                Req("e1", "excl", "Lead the main message with a sentence that starts with `Good news:` or `Quick update:`.",
                    lambda o, r: bool(re.search(r"(^|\n|[.!?] )(Good news:|Quick update:)", o))),
                Req("e2", "excl", "Invite a response with the exact phrase `reply to this email`.",
                    lambda o, r: "reply to this email" in o.lower()),
                Req("e3", "excl", "Set expectations with a time frame written as `within <n> hours` or `within <n> business days`.",
                    lambda o, r: bool(re.search(r"within \d+ (business )?(day|hour)s?\b", o))),
                Req("sh", "sh", "Close with the agent's first name and then a line ending in `Support Team`.",
                    lambda o, r: has_line(o, r"Support Team$")),
                Req("ent", "ent", "Point the customer to the relevant help-center article by including its `https://help.example.com/...` URL.",
                    lambda o, r: "https://help.example.com/" in o),
            ],
            example="Hi Maria!\n\nGood news: the invoice export timeout is fixed, and you'll be able to export again within 2 hours. If it still fails, our guide at https://help.example.com/invoice-export walks through clearing the cache.\n\nJust reply to this email if anything looks off.\n\nCheers,\nJordan\nAcme Support Team"),
    },
    tasks=[
        "Write the support reply to David Chen (ticket 51907): he was charged twice for his annual plan. The duplicate charge was refunded today and will appear on his statement. Help article: https://help.example.com/billing-refunds. Agent: Amira.",
        "Write the support reply to Sofia Alvarez (ticket 52344): she cannot reset her password because the email never arrives. Her address was on the suppression list and has been removed; she should request the reset again and check spam. Help article: https://help.example.com/password-reset. Agent: Ben.",
        "Write the support reply to Kenji Watanabe (ticket 53012): his team's dashboard shows no data since the weekend. The data connector was re-authorized by engineering; he should refresh the dashboard and re-run the sync. Help article: https://help.example.com/connectors. Agent: Olivia.",
        "Write the support reply to Hannah Becker (ticket 53688): she wants to move her account to the EU data region. The migration is scheduled; she should confirm a maintenance window and export a backup first. Help article: https://help.example.com/data-regions. Agent: Rafael.",
        "Write the support reply to Liam O'Connor (ticket 54120): the mobile app logs him out every few minutes. A fix shipped in version 4.2.1; he should update the app and sign in again. Help article: https://help.example.com/mobile-login. Agent: Zoe.",
        "Write the support reply to Fatima Rahman (ticket 54755): her CSV import rejects files larger than 10 MB. The limit was raised to 50 MB for her workspace; she should retry the import and split files above the new limit. Help article: https://help.example.com/csv-import. Agent: Marco.",
        "Write the support reply to Peter Novak (ticket 55231): invoices show the wrong VAT rate for Slovakia. The tax table was corrected; he should regenerate the affected invoices and check the totals. Help article: https://help.example.com/tax-settings. Agent: Ines.",
        "Write the support reply to Grace Okafor (ticket 55890): she cannot add a fifth user to her team plan. Her plan allows four seats; she should upgrade the plan or remove an inactive user, then send the invite again. Help article: https://help.example.com/seats. Agent: Tom.",
    ],
    witness={
        "A": "Dear Maria Lopez,\n\nGood news: the invoice export timeout reported in Ticket #48213 has been fixed, and exports will work again within 2 hours.\n\nPlease follow these steps:\n1. Clear your browser cache.\n2. Run the invoice export again.\n\nPlease reply to this email if the export still fails.\n\nKind regards,\nJordan\nAcme Support Team\nLinks: https://help.example.com/invoice-export",
        "B": "Hi Maria!\n\nGood news: the invoice export timeout reported in Ticket #48213 has been fixed, and exports will work again within 2 hours.\n\nPlease follow these steps:\n1. Clear your browser cache.\n2. Run the invoice export again.\n\nPlease reply to this email if the export still fails.\n\nKind regards,\nJordan\nAcme Support Team\nLinks: https://help.example.com/invoice-export",
    }))

# --------------------------------------------------------------------------- 7. changelog entry
def _bul(o):
    return [l.strip() for l in o.split("\n") if l.strip().startswith("- ")]


JOBS.append(Job(
    id="changelog", artifact="changelog entry",
    example_request="Write the changelog entry for version 2.3.0, released on 2026-03-02. Added CSV export for reports (issue #412, by @dana). Fixed a timezone bug in scheduled reports (issue #398, by @lee). Breaking: the /v1/export endpoint was removed.",
    facts_hint="a version number, a release date, at least two changes with issue numbers and contributor handles, and one breaking change",
    skills={
        "A": Skill(
            name="keep-a-changelog",
            description="Write changelog entries in Keep a Changelog format. Use for any changelog or release notes.",
            intro="The changelog is parsed by tooling and read by integrators, so it follows Keep a Changelog strictly.",
            reqs=[
                Req("con", "con", "The first line must be the version heading `## [<version>] - <YYYY-MM-DD>`, for example `## [2.3.0] - 2026-03-02`.",
                    lambda o, r: bool(re.match(r"^## \[\d+\.\d+\.\d+\] - \d{4}-\d{2}-\d{2}$", first(o)))),
                Req("e1", "excl", "Group changes under at least two of the headings `### Added`, `### Changed`, `### Fixed`.",
                    lambda o, r: sum(has_line(o, "^### " + h + "$") for h in ("Added", "Changed", "Fixed")) >= 2),
                Req("e2", "excl", "Reference issues in parentheses as `(#<number>)`.",
                    lambda o, r: bool(re.search(r"\(#\d+\)", o))),
                Req("e3", "excl", "Bullets are fragments: no bullet may end with a period.",
                    lambda o, r: len(_bul(o)) >= 1 and not any(b.endswith(".") for b in _bul(o))),
                Req("sh", "sh", "Flag incompatible changes with the exact marker `BREAKING:`.",
                    lambda o, r: "BREAKING:" in o),
                Req("ent", "ent", "Bullets describe the change only. No bullet may contain an @handle.",
                    lambda o, r: len(_bul(o)) >= 1 and not any("@" in b for b in _bul(o))),
            ],
            example="## [2.3.0] - 2026-03-02\n\n### Added\n- CSV export for reports (#412)\n\n### Fixed\n- Timezone bug in scheduled reports (#398)\n\n### Changed\n- BREAKING: removed the /v1/export endpoint"),
        "B": Skill(
            name="release-announcement",
            description="Write release notes as a short announcement for users. Use for any changelog or release notes.",
            intro="Release notes are read by end users and by the community, so they highlight value and credit people.",
            reqs=[
                Req("con", "con", "The first line must be the title `# Release <version> (<Month D, YYYY>)`, for example `# Release 2.3.0 (March 2, 2026)`.",
                    lambda o, r: bool(re.match(r"^# Release \d+\.\d+\.\d+ \(.+\)$", first(o)))),
                Req("e1", "excl", "Open with a one-sentence summary on a line that starts with `Highlights: `.",
                    lambda o, r: has_line(o, r"^Highlights: \S")),
                Req("e2", "excl", "Tell users what to do on a line that starts with `Upgrade: `.",
                    lambda o, r: has_line(o, r"^Upgrade: \S")),
                Req("e3", "excl", "Put the name of each new feature in bold with `**`.",
                    lambda o, r: bool(re.search(r"\*\*[^*\n]+\*\*", o))),
                Req("sh", "sh", "Mark incompatible changes with `BREAKING:` exactly.",
                    lambda o, r: "BREAKING:" in o),
                Req("ent", "ent", "Credit every contributor by @handle.",
                    lambda o, r: bool(re.search(r"@\w+", o))),
            ],
            example="# Release 2.3.0 (March 2, 2026)\n\nHighlights: reports can now be exported to CSV.\n\n- **CSV export** for reports, thanks to @dana.\n- Fixed a timezone bug in scheduled reports, thanks to @lee.\n- BREAKING: the /v1/export endpoint was removed.\n\nUpgrade: replace calls to /v1/export with /v2/export before upgrading."),
    },
    tasks=[
        "Write the changelog entry for version 1.8.0, released on 2026-04-14. Added webhook signing (issue #201, by @noor). Fixed duplicate emails on retry (issue #188, by @viktor). Breaking: the legacy API key header X-Key was removed.",
        "Write the changelog entry for version 3.0.0, released on 2026-01-20. Added role-based access control (issue #540, by @carla). Changed the default page size from 50 to 25 (issue #533, by @deepak). Breaking: config files must use YAML instead of JSON.",
        "Write the changelog entry for version 0.9.2, released on 2026-05-30. Fixed a memory leak in the image resizer (issue #77, by @yuki). Added a health check endpoint (issue #81, by @tariq). Breaking: Python 3.8 is no longer supported.",
        "Write the changelog entry for version 5.4.0, released on 2026-02-09. Added bulk user import (issue #1204, by @anna). Fixed incorrect totals in the tax report (issue #1190, by @rui). Breaking: the report_v1 export format was removed.",
        "Write the changelog entry for version 2.0.1, released on 2026-06-18. Fixed a crash when the config file is empty (issue #310, by @moses). Changed log output to JSON by default (issue #305, by @ella). Breaking: the --plain-logs flag was renamed to --text-logs.",
        "Write the changelog entry for version 4.1.0, released on 2026-03-27. Added dark mode (issue #902, by @hugo). Added keyboard shortcuts for navigation (issue #915, by @sana). Breaking: Internet Explorer 11 is no longer supported.",
        "Write the changelog entry for version 1.2.0, released on 2026-07-05. Added retry with backoff to the sync client (issue #64, by @lars). Fixed a race condition in the scheduler (issue #59, by @imani). Breaking: the sync() function now returns a result object instead of a boolean.",
        "Write the changelog entry for version 7.0.0, released on 2026-08-11. Changed the storage backend to S3-compatible object storage (issue #2210, by @pedro). Fixed slow startup with large plugin sets (issue #2198, by @mina). Breaking: local disk storage must be migrated before upgrading.",
    ],
    witness={
        "A": "## [2.3.0] - 2026-03-02\n\nHighlights: reports can now be exported to CSV.\n\n### Added\n- **CSV export** for reports (#412)\n\n### Fixed\n- Timezone bug in scheduled reports (#398)\n\n### Changed\n- BREAKING: removed the /v1/export endpoint\n\nUpgrade: replace calls to /v1/export with /v2/export before upgrading.\nThanks: @dana, @lee",
        "B": "# Release 2.3.0 (March 2, 2026)\n\nHighlights: reports can now be exported to CSV.\n\n### Added\n- **CSV export** for reports (#412)\n\n### Fixed\n- Timezone bug in scheduled reports (#398)\n\n### Changed\n- BREAKING: removed the /v1/export endpoint\n\nUpgrade: replace calls to /v1/export with /v2/export before upgrading.\nThanks: @dana, @lee",
    }))

# --------------------------------------------------------------------------- 8. API error response
def _j(o, k, pred):
    d = jparse(o)
    return d is not None and k in d and pred(d[k])


JOBS.append(Job(
    id="apierror", artifact="JSON error response body",
    example_request="Write the JSON error response body for a request that exceeded the rate limit of 100 requests per minute on POST /v1/payments.",
    facts_hint="the failing endpoint and the reason for the error",
    skills={
        "A": Skill(
            name="api-errors-internal",
            description="Write API error response bodies in the internal platform format. Use for any API error response.",
            intro="Internal services parse error bodies automatically, so the body is strict machine-readable JSON.",
            reqs=[
                Req("con", "con", "Name the machine-readable code field `error_code` (snake_case). Never use camelCase keys.",
                    lambda o, r: (jparse(o) or {}).get("error_code") is not None and "errorCode" not in (jparse(o) or {})),
                Req("e1", "excl", "Include the HTTP status as an integer in the field `status`.",
                    lambda o, r: _j(o, "status", lambda v: isinstance(v, int) and not isinstance(v, bool))),
                Req("e2", "excl", "Include a boolean field `retryable`.",
                    lambda o, r: _j(o, "retryable", lambda v: isinstance(v, bool))),
                Req("e3", "excl", "Include a field `docs` with an `https://` link to the error documentation.",
                    lambda o, r: _j(o, "docs", lambda v: isinstance(v, str) and v.startswith("https://"))),
                Req("sh", "sh", "Include a human-readable sentence in the field `message`.",
                    lambda o, r: _j(o, "message", lambda v: isinstance(v, str) and len(v.strip()) > 0)),
                Req("ent", "ent", "The reply must be exactly one JSON object and nothing else, so that it parses as JSON.",
                    lambda o, r: _strict_json(o)),
            ],
            example='{\n  "error_code": "rate_limit_exceeded",\n  "message": "Rate limit of 100 requests per minute exceeded.",\n  "status": 429,\n  "retryable": true,\n  "docs": "https://docs.example.com/errors/rate_limit_exceeded"\n}'),
        "B": Skill(
            name="api-errors-public",
            description="Write API error response bodies for the public developer API. Use for any API error response.",
            intro="External developers read error bodies while debugging, so the body explains itself.",
            reqs=[
                Req("con", "con", "Name the machine-readable code field `errorCode` (camelCase). Never use snake_case keys.",
                    lambda o, r: (jparse(o) or {}).get("errorCode") is not None and "error_code" not in (jparse(o) or {})),
                Req("e1", "excl", "Include a field `details` that holds a non-empty list of specifics.",
                    lambda o, r: _j(o, "details", lambda v: isinstance(v, list) and len(v) > 0)),
                Req("e2", "excl", "Include a field `timestamp` with a UTC time in the form `2026-03-02T10:15:00Z`.",
                    lambda o, r: _j(o, "timestamp", lambda v: isinstance(v, str) and bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", v)))),
                Req("e3", "excl", "Include a field `severity` with the value `low`, `medium` or `high`.",
                    lambda o, r: _j(o, "severity", lambda v: v in ("low", "medium", "high"))),
                Req("sh", "sh", "Explain the error for humans in the `message` field.",
                    lambda o, r: _j(o, "message", lambda v: isinstance(v, str) and len(v.strip()) > 0)),
                Req("ent", "ent", "Add a developer hint that starts with `Hint:` and says how to fix the request.",
                    lambda o, r: "Hint:" in o),
            ],
            example='{\n  "errorCode": "RATE_LIMIT_EXCEEDED",\n  "message": "Rate limit of 100 requests per minute exceeded.",\n  "details": ["limit=100/min", "endpoint=POST /v1/payments"],\n  "timestamp": "2026-03-02T10:15:00Z",\n  "severity": "medium"\n}\n\nHint: wait 60 seconds before retrying, or request a higher limit.'),
    },
    tasks=[
        "Write the JSON error response body for a request to GET /v1/users/8841 where the user does not exist.",
        "Write the JSON error response body for a request to POST /v1/orders that is missing the required field `currency`.",
        "Write the JSON error response body for a request to DELETE /v1/projects/17 made with an API key that lacks the delete permission.",
        "Write the JSON error response body for a request to POST /v1/uploads where the file is larger than the 25 MB limit.",
        "Write the JSON error response body for a request to GET /v1/reports/monthly that timed out in the upstream database after 30 seconds.",
        "Write the JSON error response body for a request to PUT /v1/subscriptions/302 that conflicts with a concurrent update.",
        "Write the JSON error response body for a request to POST /v1/login with an expired access token.",
        "Write the JSON error response body for a request to GET /v1/invoices with the query parameter `page=-3`, which is invalid.",
    ],
    witness={
        "A": '{\n  "error_code": "rate_limit_exceeded",\n  "message": "Rate limit of 100 requests per minute exceeded.",\n  "status": 429,\n  "retryable": true,\n  "docs": "https://docs.example.com/errors/rate_limit_exceeded",\n  "details": ["limit=100/min", "endpoint=POST /v1/payments"],\n  "timestamp": "2026-03-02T10:15:00Z",\n  "severity": "medium",\n  "hint": "Hint: wait 60 seconds before retrying."\n}',
        "B": '{\n  "errorCode": "RATE_LIMIT_EXCEEDED",\n  "message": "Rate limit of 100 requests per minute exceeded.",\n  "status": 429,\n  "retryable": true,\n  "docs": "https://docs.example.com/errors/rate_limit_exceeded",\n  "details": ["limit=100/min", "endpoint=POST /v1/payments"],\n  "timestamp": "2026-03-02T10:15:00Z",\n  "severity": "medium",\n  "hint": "Hint: wait 60 seconds before retrying."\n}',
    }))


def _strict_json(o):
    import json
    try:
        return isinstance(json.loads(o), dict)
    except Exception:
        return False
