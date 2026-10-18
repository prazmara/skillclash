"""Eight more ClashBench jobs, same layout as jobs_core: two skills per artifact, six rules each
(con, e1, e2, e3, sh, ent), eight held-out requests, and two hand-written witnesses."""
import re

from spec import Job, Req, Skill, first, has_line, jparse, last, lines, n_lines, nonempty
from jobs_core import TICKET, bullets_after, words

JOBS = []

_STEP = r"^\d+[.)] \S"

# --------------------------------------------------------------------------- 1. code review comment
_RV_BODY_A = (
    "Location: src/uploader.py:88\n"
    "The loop catches every exception, so a bad credential is retried five times before it fails.\n"
    "Proposed fix: catch only timeout and throttling errors and re-raise everything else.\n"
    "Confidence: high\n"
    "Verdict: request changes")
_RV_W = (
    "<<HEAD>>\n\n"
    "Location: src/uploader.py:88\n"
    "Category: correctness\n"
    "Effort: S\n"
    "Confidence: high\n"
    "What works well: the backoff between attempts is clear and easy to follow.\n"
    "The loop catches every exception, so a bad credential is retried five times before it fails.\n"
    "Proposed fix: catch only timeout and throttling errors and re-raise everything else.\n"
    "Verdict: request changes\n"
    "Open question: should any error other than a timeout be retried at all?")
_VERDICT = r"^Verdict: (approve|request changes|comment)$"

JOBS.append(Job(
    id="review", artifact="code review comment",
    example_request="Write the code review comment: the diff wraps the S3 upload in a retry loop that retries on every exception, including authentication errors. File: src/uploader.py, line 88.",
    facts_hint="what the diff changes and what is wrong with it, the file path, and the line number",
    skills={
        "A": Skill(
            name="review-triage",
            description="Write code review comments in the triage format used by the merge queue. Use for any code review comment.",
            intro="Authors receive many review comments. A fixed triage format tells them at a glance how serious a comment is and where it applies.",
            reqs=[
                Req("con", "con", "The first line must start with a severity tag in square brackets, one of `[blocker]`, `[major]`, `[minor]`, `[nit]`, followed by a short title.",
                    lambda o, r: bool(re.match(r"^\[(blocker|major|minor|nit)\] \S", first(o)))),
                Req("e1", "excl", "Give the place in the code on its own line as `Location: <file>:<line>`.",
                    lambda o, r: has_line(o, r"^Location: \S+:\d+$")),
                Req("e2", "excl", "Propose the change on a line that starts with `Proposed fix: `.",
                    lambda o, r: has_line(o, r"^Proposed fix: \S")),
                Req("e3", "excl", "Say how sure you are on a line `Confidence: high`, `Confidence: medium` or `Confidence: low`.",
                    lambda o, r: has_line(o, r"^Confidence: (high|medium|low)$")),
                Req("sh", "sh", "Give the outcome on a line `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.",
                    lambda o, r: has_line(o, _VERDICT)),
                Req("ent", "ent", "State every finding as a statement. A question mark may appear only on a final line that starts with `Open question:`.",
                    lambda o, r: len(nonempty(o)) > 1 and all(l.strip().startswith("Open question:") for l in o.split("\n") if "?" in l)),
            ],
            example="[major] Retry loop also retries authentication errors\n\n" + _RV_BODY_A),
        "B": Skill(
            name="review-mentoring",
            description="Write code review comments in the mentoring style of the guild. Use for any code review comment.",
            intro="A review comment should teach as well as correct, so it names what is good, classifies the problem and opens a dialogue with the author.",
            reqs=[
                Req("con", "con", "The first line must be plain text of the form `Review: <title>`, with no tag or bracket before it.",
                    lambda o, r: bool(re.match(r"^Review: \S", first(o)))),
                Req("e1", "excl", "Name one good thing about the diff on a line that starts with `What works well: `.",
                    lambda o, r: has_line(o, r"^What works well: \S")),
                Req("e2", "excl", "Classify the comment on a line `Category: correctness`, `Category: security`, `Category: performance`, `Category: readability` or `Category: testing`.",
                    lambda o, r: has_line(o, r"^Category: (correctness|security|performance|readability|testing)$")),
                Req("e3", "excl", "Estimate the work needed on a line `Effort: S`, `Effort: M` or `Effort: L`.",
                    lambda o, r: has_line(o, r"^Effort: [SML]$")),
                Req("sh", "sh", "Close your assessment with a separate line that reads `Verdict: approve`, `Verdict: request changes` or `Verdict: comment`.",
                    lambda o, r: has_line(o, _VERDICT)),
                Req("ent", "ent", "Ask the author at least one clarifying question, written as a full sentence that ends with a question mark.",
                    lambda o, r: bool(re.search(r"\w\?(\s|$)", o))),
            ],
            example="Review: Retry loop also retries authentication errors\n\nWhat works well: the backoff between attempts is clear and easy to follow.\nCategory: correctness\nEffort: S\nThe loop in src/uploader.py catches every exception, so a bad credential is retried five times. Was that intended, or should only timeouts be retried?\nVerdict: request changes"),
    },
    tasks=[
        "Write the code review comment: the diff adds a user search handler that builds the SQL WHERE clause by concatenating the raw query string. File: api/handlers/users.py, line 41.",
        "Write the code review comment: the diff caches user permissions in a module-level map that is never invalidated when roles change. File: auth/permissions.go, line 112.",
        "Write the code review comment: the diff replaces the pagination loop with a single call that loads all 200,000 audit rows into memory before filtering. File: services/audit/export.ts, line 67.",
        "Write the code review comment: the diff adds a parse_amount helper that silently returns 0 when the input is not a number. File: billing/utils/money.py, line 19.",
        "Write the code review comment: the diff logs the full request body, including card numbers, at info level in the payment client. File: payments/PaymentClient.java, line 203.",
        "Write the code review comment: the diff renames the config key timeout_ms to timeoutMs but leaves the old name in the deployment manifests. File: config/loader.rb, line 58.",
        "Write the code review comment: the diff adds a background job that sends reminder emails but has no unit test and no retry limit. File: jobs/reminders.py, line 30.",
        "Write the code review comment: the diff changes the trial expiry check to compare dates in local time instead of UTC, which ends some trials one day early. File: subscriptions/trial.js, line 24.",
    ],
    witness={
        "A": _RV_W.replace("<<HEAD>>", "[major] Retry loop also retries authentication errors"),
        "B": _RV_W.replace("<<HEAD>>", "Review: Retry loop also retries authentication errors"),
    }))

# --------------------------------------------------------------------------- 2. test case specification
_TC_W = (
    "<<HEAD>>\n\n"
    "Covers: login\n"
    "Priority: P1\n"
    "Type: negative\n"
    "Preconditions: a registered user account exists and is not locked.\n"
    "Test data: one registered user with a known password.\n"
    "1. Enter the correct username and a wrong password on the login page.\n"
    "2. Verify that the message Invalid credentials appears.\n"
    "3. Repeat the wrong password four more times.\n"
    "4. Verify that the message Account locked appears.\n"
    "5. Verify that the correct password is now rejected.\n"
    "Expected result: the account is locked after five failed attempts and stays locked.\n"
    "Cleanup: unlock the account in the admin console.")

JOBS.append(Job(
    id="testcase", artifact="test case specification",
    example_request="Write the test case specification: verify that a user is locked out after five failed login attempts. Test ID TC-0412. Feature: login. Priority: P1.",
    facts_hint="a test ID such as TC-0412, the behavior to verify, the feature it belongs to, and a priority from P1 to P3",
    skills={
        "A": Skill(
            name="testcase-compact",
            description="Write manual test case specifications in the compact format of the test management tool. Use for any written test case.",
            intro="Testers run hundreds of cases per release. Each case must be short enough to execute without scrolling and must carry the fields the tool filters on.",
            reqs=[
                Req("con", "con", "The first line must be the test ID and the title as `<ID>: <title>`, for example `TC-0412: Lockout after five failed logins`.",
                    lambda o, r: bool(re.match(r"^TC-\d+: \S", first(o)))),
                Req("e1", "excl", "Describe the starting state on a line that begins with `Preconditions: `.",
                    lambda o, r: has_line(o, r"^Preconditions: \S")),
                Req("e2", "excl", "Give the priority on a line `Priority: P1`, `Priority: P2` or `Priority: P3`.",
                    lambda o, r: has_line(o, r"^Priority: P[1-3]$")),
                Req("e3", "excl", "Tag the kind of test on a line `Type: functional`, `Type: regression`, `Type: smoke` or `Type: negative`.",
                    lambda o, r: has_line(o, r"^Type: (functional|regression|smoke|negative)$")),
                Req("sh", "sh", "State the pass criterion on a line that starts with `Expected result: `.",
                    lambda o, r: has_line(o, r"^Expected result: \S")),
                Req("ent", "ent", "Write the steps as a numbered list (`1.`, `2.`, ...) with at most five steps.",
                    lambda o, r: 1 <= n_lines(o, _STEP) <= 5),
            ],
            example="TC-0412: Lockout after five failed logins\n\nPreconditions: a registered user account exists and is not locked.\nPriority: P1\nType: negative\n1. Open the login page.\n2. Enter the correct username with a wrong password five times.\n3. Enter the correct password.\nExpected result: the sixth attempt is rejected and the account shows as locked."),
        "B": Skill(
            name="testcase-traceable",
            description="Write manual test case specifications that auditors can trace and repeat. Use for any written test case.",
            intro="Audited releases need test cases that link to a feature, name their data and prove each outcome with an explicit check.",
            reqs=[
                Req("con", "con", "The first line must be `Test case: <title>`. The test ID does not belong in the first line.",
                    lambda o, r: bool(re.match(r"^Test case: \S", first(o)))),
                Req("e1", "excl", "Link the feature under test on a line `Covers: <feature>`.",
                    lambda o, r: has_line(o, r"^Covers: \S")),
                Req("e2", "excl", "List the data the tester needs on a line that starts with `Test data: `.",
                    lambda o, r: has_line(o, r"^Test data: \S")),
                Req("e3", "excl", "Say how to restore the system afterwards on a line that starts with `Cleanup: `.",
                    lambda o, r: has_line(o, r"^Cleanup: \S")),
                Req("sh", "sh", "Write the outcome that counts as a pass on its own line beginning with `Expected result: `.",
                    lambda o, r: has_line(o, r"^Expected result: \S")),
                Req("ent", "ent", "Include at least three numbered steps that are explicit checks, each starting with the word `Verify`, for example `3. Verify that the error appears.`",
                    lambda o, r: n_lines(o, r"^\d+[.)] Verify\b") >= 3),
            ],
            example="Test case: Lockout after five failed logins\n\nCovers: login\nTest data: one registered user with a known password.\n1. Open the login page.\n2. Enter the correct username and a wrong password.\n3. Verify that the message Invalid credentials appears.\n4. Repeat the wrong password four more times.\n5. Verify that the message Account locked appears after the fifth attempt.\n6. Enter the correct password.\n7. Verify that the login is still rejected.\n8. Open the admin console and look up the user.\nExpected result: the account is locked after five failed attempts and stays locked.\nCleanup: unlock the account in the admin console."),
    },
    tasks=[
        "Write the test case specification: verify that a password reset link expires after 30 minutes. Test ID TC-0518. Feature: password-reset. Priority: P1.",
        "Write the test case specification: verify that the cart total updates when a discount code is applied and then removed. Test ID TC-0733. Feature: cart. Priority: P2.",
        "Write the test case specification: verify that a file upload larger than 25 MB is rejected with a clear message. Test ID TC-0291. Feature: uploads. Priority: P2.",
        "Write the test case specification: verify that a user with the viewer role cannot delete a project. Test ID TC-0645. Feature: permissions. Priority: P1.",
        "Write the test case specification: verify that search results are sorted by relevance and then by date. Test ID TC-0809. Feature: search. Priority: P3.",
        "Write the test case specification: verify that the session ends after 15 minutes of inactivity. Test ID TC-0377. Feature: sessions. Priority: P1.",
        "Write the test case specification: verify that an invoice PDF shows the correct VAT for a customer in Germany. Test ID TC-0954. Feature: invoicing. Priority: P2.",
        "Write the test case specification: verify that a shipping notification email is sent once, not twice, when an order ships. Test ID TC-0462. Feature: notifications. Priority: P2.",
    ],
    witness={
        "A": _TC_W.replace("<<HEAD>>", "TC-0412: Lockout after five failed logins"),
        "B": _TC_W.replace("<<HEAD>>", "Test case: Lockout after five failed logins"),
    }, max_new_tokens=380))

# --------------------------------------------------------------------------- 3. daily standup update
_SU_W = (
    "<<HEAD>>\n\n"
    "Done:\n"
    "- Finished the refund API pagination\n"
    "Next:\n"
    "- Start the ledger export job\n"
    "Items: 1 done, 1 planned\n"
    "Tickets: PAY-518, PAY-530\n"
    "ETA: 2026-03-12\n"
    "On track: yes\n"
    "Blocked: waiting for staging database credentials from the platform team\n"
    "Need help from: platform team\n"
    "#standup #payments")

JOBS.append(Job(
    id="standup", artifact="daily standup update",
    example_request="Write the standup update for Nora Lindqvist, 2026-03-10, team Payments. Yesterday: finished the refund API pagination (PAY-518). Today: start the ledger export job (PAY-530), expected done 2026-03-12. Blocker: waiting for staging database credentials from the platform team.",
    facts_hint="the person's full name, the date, the team name, yesterday's and today's work with ticket IDs such as PAY-518, an expected finish date, and a blocker (or none)",
    skills={
        "A": Skill(
            name="standup-async-thread",
            description="Write daily standup updates for the team's asynchronous standup thread. Use for any standup or daily status update.",
            intro="The standup thread is searched by date and by team hashtag, and a bot collects the sections, so every update has the same skeleton.",
            reqs=[
                Req("con", "con", "The first line must be `Standup <YYYY-MM-DD> | <full name>`, for example `Standup 2026-03-10 | Nora Lindqvist`.",
                    lambda o, r: bool(re.match(r"^Standup \d{4}-\d{2}-\d{2} \| \S", first(o)))),
                Req("e1", "excl", "List finished work as bullets that start with `- ` under a line that reads exactly `Done:`.",
                    lambda o, r: len(bullets_after(o, r"^Done:$")) >= 1),
                Req("e2", "excl", "List planned work as bullets that start with `- ` under a line that reads exactly `Next:`.",
                    lambda o, r: len(bullets_after(o, r"^Next:$")) >= 1),
                Req("e3", "excl", "Say whether the sprint goal is safe on a line `On track: yes` or `On track: no`.",
                    lambda o, r: has_line(o, r"^On track: (yes|no)$")),
                Req("sh", "sh", "Report blockers on a line that starts with `Blocked: `, and write `Blocked: none` when nothing blocks you.",
                    lambda o, r: has_line(o, r"^Blocked: \S")),
                Req("ent", "ent", "The very last line must be the hashtag line `#standup #<team>` with the team name in lowercase, for example `#standup #payments`.",
                    lambda o, r: bool(re.match(r"^#standup #[a-z0-9_-]+$", last(o)))),
            ],
            example="Standup 2026-03-10 | Nora Lindqvist\n\nDone:\n- Finished the refund API pagination (PAY-518)\nNext:\n- Start the ledger export job (PAY-530)\nBlocked: waiting for staging database credentials from the platform team\nOn track: yes\n\n#standup #payments"),
        "B": Skill(
            name="standup-manager-digest",
            description="Write daily standup updates that feed the engineering manager's digest. Use for any standup or daily status update.",
            intro="Managers read a digest of all updates and act on requests for help, so each update carries counts, tickets, a date and an explicit ask.",
            reqs=[
                Req("con", "con", "The first line must be `Daily update from <full name>`, for example `Daily update from Nora Lindqvist`.",
                    lambda o, r: bool(re.match(r"^Daily update from \S", first(o)))),
                Req("e1", "excl", "Summarize the workload on a line `Items: <n> done, <n> planned`.",
                    lambda o, r: has_line(o, r"^Items: \d+ done, \d+ planned$")),
                Req("e2", "excl", "Collect all ticket IDs on one line `Tickets: <ID>, <ID>`, separated by a comma and a space.",
                    lambda o, r: has_line(o, r"^Tickets: " + TICKET + r"(, " + TICKET + r")*$")),
                Req("e3", "excl", "Give the expected finish date of the current task on a line `ETA: <YYYY-MM-DD>`.",
                    lambda o, r: has_line(o, r"^ETA: \d{4}-\d{2}-\d{2}$")),
                Req("sh", "sh", "Put blockers on their own line beginning with `Blocked: `. If there are none, the line is `Blocked: none`.",
                    lambda o, r: has_line(o, r"^Blocked: \S")),
                Req("ent", "ent", "Finish the update with a line `Need help from: <person or team>`, or `Need help from: nobody`.",
                    lambda o, r: any(re.match(r"^Need help from: \S", l) for l in nonempty(o)[-3:])),
            ],
            example="Daily update from Nora Lindqvist\n\nYesterday I finished the refund API pagination. Today I am starting the ledger export job.\nItems: 1 done, 1 planned\nTickets: PAY-518, PAY-530\nETA: 2026-03-12\nBlocked: waiting for staging database credentials from the platform team\nNeed help from: platform team"),
    },
    tasks=[
        "Write the standup update for Arjun Mehta, 2026-04-02, team Search. Yesterday: fixed the stale index alias bug (SRCH-204). Today: add typo tolerance to the query parser (SRCH-211), expected done 2026-04-06. Blocker: none.",
        "Write the standup update for Clara Jensen, 2026-05-19, team Billing. Yesterday: reviewed the tax table migration (BILL-733). Today: write the dunning email templates (BILL-740), expected done 2026-05-21. Blocker: legal has not approved the email wording.",
        "Write the standup update for Mateo Ruiz, 2026-01-14, team Mobile. Yesterday: shipped offline mode for notes (MOB-95). Today: profile the cold start time on Android (MOB-102), expected done 2026-01-16. Blocker: no access to the low-end test devices.",
        "Write the standup update for Yuna Park, 2026-06-08, team Warehouse. Yesterday: moved the nightly load to the new scheduler (DATA-611). Today: backfill the March partitions (DATA-618), expected done 2026-06-10. Blocker: waiting for more storage quota from the infrastructure team.",
        "Write the standup update for Felix Braun, 2026-02-25, team Identity. Yesterday: added passkey support to the login page (IDN-340). Today: write the account recovery flow (IDN-347), expected done 2026-03-02. Blocker: none.",
        "Write the standup update for Amina Yusuf, 2026-07-21, team Growth. Yesterday: launched the pricing page experiment (GRO-58). Today: build the results dashboard (GRO-63), expected done 2026-07-23. Blocker: the analytics events are missing in staging.",
        "Write the standup update for Daniel Costa, 2026-03-30, team Platform. Yesterday: upgraded the cluster to Kubernetes 1.31 (PLAT-902). Today: rotate the service mesh certificates (PLAT-910), expected done 2026-03-31. Blocker: the maintenance window is not approved by the release manager yet.",
        "Write the standup update for Sara Lindholm, 2026-08-12, team Helpdesk. Yesterday: fixed the macro editor crash (SUP-417). Today: add bulk ticket tagging (SUP-425), expected done 2026-08-14. Blocker: none.",
    ],
    witness={
        "A": _SU_W.replace("<<HEAD>>", "Standup 2026-03-10 | Nora Lindqvist"),
        "B": _SU_W.replace("<<HEAD>>", "Daily update from Nora Lindqvist"),
    }))

# --------------------------------------------------------------------------- 4. bug report
_BUG_TITLE = "CSV export is empty when the date filter spans more than 90 days"
_BUG_W = (
    "<<HEAD>>\n\n"
    "Severity: S2\n"
    "Environment: app 3.8.1, Chrome 122, Windows 11\n"
    "Reproducibility: always\n"
    "Reported by: Ivo Marek\n"
    "Regression: unknown\n"
    "Steps:\n"
    "1. Open the Reports page.\n"
    "2. Set the date filter to a range longer than 90 days.\n"
    "3. Click Export CSV.\n"
    "Expected: the file contains one row per report entry.\n"
    "Actual: the downloaded file is empty.\n"
    "Workaround: export two shorter date ranges and merge the files.\n"
    "Error text: `TypeError: rows is undefined`")
_EXP_ACT = lambda o, r: has_line(o, r"^Expected: \S") and has_line(o, r"^Actual: \S")  # noqa: E731

JOBS.append(Job(
    id="bugreport", artifact="bug report",
    example_request="Write the bug report: the CSV export on the Reports page produces an empty file when the date filter spans more than 90 days. App version 3.8.1, Chrome 122 on Windows 11. Console shows `TypeError: rows is undefined`. Reporter: Ivo Marek.",
    facts_hint="the faulty behavior and how to trigger it, the app version, the browser or device with its operating system, one exact error message, and the reporter's full name",
    skills={
        "A": Skill(
            name="bug-triage-form",
            description="Write bug reports in the triage form of the issue tracker. Use for any bug report.",
            intro="The triage rotation sorts incoming bugs by a few fixed fields, and the tracker renders the description as plain text.",
            reqs=[
                Req("con", "con", "The first line must be plain text of the form `Title: <one-line summary>`.",
                    lambda o, r: bool(re.match(r"^Title: \S", first(o)))),
                Req("e1", "excl", "Rate the severity on a line `Severity: S1`, `Severity: S2`, `Severity: S3` or `Severity: S4`.",
                    lambda o, r: has_line(o, r"^Severity: S[1-4]$")),
                Req("e2", "excl", "Give the app version and the platform on one line that starts with `Environment: `.",
                    lambda o, r: has_line(o, r"^Environment: \S")),
                Req("e3", "excl", "Say how often it happens on a line `Reproducibility: always`, `Reproducibility: sometimes` or `Reproducibility: once`.",
                    lambda o, r: has_line(o, r"^Reproducibility: (always|sometimes|once)$")),
                Req("sh", "sh", "Contrast the outcome in two lines that start with `Expected: ` and `Actual: `.",
                    _EXP_ACT),
                Req("ent", "ent", "Keep the description free of code formatting. Backticks may appear only on a final line that starts with `Error text:`.",
                    lambda o, r: len(nonempty(o)) > 1 and all(l.strip().startswith("Error text:") for l in o.split("\n") if "`" in l)),
            ],
            example="Title: " + _BUG_TITLE + "\n\nSeverity: S2\nEnvironment: app 3.8.1, Chrome 122, Windows 11\nReproducibility: always\nSteps:\n1. Open the Reports page.\n2. Set the date filter to a range longer than 90 days.\n3. Click Export CSV.\nExpected: the file contains one row per report entry.\nActual: the downloaded file is empty and the console shows a TypeError."),
        "B": Skill(
            name="bug-dev-handoff",
            description="Write bug reports that a developer can pick up without asking questions. Use for any bug report.",
            intro="Developers search the code base and the logs for the exact error, and they need to know who saw the bug and how users can cope until it is fixed.",
            reqs=[
                Req("con", "con", "The first line must be a level-2 Markdown heading of the form `## Bug: <summary>`.",
                    lambda o, r: bool(re.match(r"^## Bug: \S", first(o)))),
                Req("e1", "excl", "Say whether this worked before on a line `Regression: yes`, `Regression: no` or `Regression: unknown`.",
                    lambda o, r: has_line(o, r"^Regression: (yes|no|unknown)$")),
                Req("e2", "excl", "Offer a way around the bug on a line that starts with `Workaround: `, and write `Workaround: none` if there is none.",
                    lambda o, r: has_line(o, r"^Workaround: \S")),
                Req("e3", "excl", "Name the person who found the bug on a line `Reported by: <full name>`.",
                    lambda o, r: has_line(o, r"^Reported by: \S")),
                Req("sh", "sh", "Describe what should happen and what happens instead on two separate lines, `Expected: ...` and `Actual: ...`.",
                    _EXP_ACT),
                Req("ent", "ent", "Quote the exact error message inside backticks so that developers can search for it.",
                    lambda o, r: bool(re.search(r"`[^`\n]+`", o))),
            ],
            example="## Bug: " + _BUG_TITLE + "\n\nReported by: Ivo Marek\nRegression: unknown\nOn the Reports page, exporting with a date filter longer than 90 days downloads an empty file. The console shows `TypeError: rows is undefined`.\nExpected: the file contains one row per report entry.\nActual: the downloaded file is empty.\nWorkaround: export two shorter date ranges and merge the files."),
    },
    tasks=[
        "Write the bug report: the profile photo upload spinner never stops when the image is larger than 5 MB. App version 2.14.0, Safari 17 on macOS 14. Console shows `413 Payload Too Large`. Reporter: Leila Haddad.",
        "Write the bug report: the dashboard chart shows no data after switching the account timezone to UTC+13. App version 5.2.3, Firefox 124 on Ubuntu 22.04. Console shows `RangeError: Invalid time value`. Reporter: Oskar Nilsson.",
        "Write the bug report: saving a draft invoice with an empty line item logs the user out. App version 4.0.7, Edge 123 on Windows 11. Console shows `401 Unauthorized: session token missing`. Reporter: Mei Lin.",
        "Write the bug report: the search box on the Orders page returns no results for queries that contain an apostrophe. App version 3.9.0, Chrome 123 on macOS 14. Server log shows `SyntaxError: unterminated quoted string`. Reporter: Tariq Aziz.",
        "Write the bug report: the mobile app crashes when the notification settings screen is opened in landscape mode. App version 7.1.2, Pixel 8 on Android 14. Logcat shows `NullPointerException: binding.toggleRow`. Reporter: Greta Olsen.",
        "Write the bug report: the PDF export of a report cuts off the last table column. App version 1.6.5, Chrome 122 on Windows 10. Console shows `Warning: page width exceeded by 84px`. Reporter: Paulo Mendes.",
        "Write the bug report: two-factor codes are rejected when the phone clock is more than 30 seconds ahead. App version 6.3.1, iPhone 15 on iOS 17. Server log shows `OTPError: code outside valid window`. Reporter: Ingrid Solberg.",
        "Write the bug report: the bulk user import stops at row 500 and the page shows no error. App version 2.8.4, Firefox 125 on Windows 11. Network tab shows `504 Gateway Timeout`. Reporter: Rahul Verma.",
    ],
    witness={
        "A": _BUG_W.replace("<<HEAD>>", "Title: " + _BUG_TITLE),
        "B": _BUG_W.replace("<<HEAD>>", "## Bug: " + _BUG_TITLE),
    }, max_new_tokens=360))

# --------------------------------------------------------------------------- 5. Dockerfile
_DF_A_EX = '''# syntax=docker/dockerfile:1
FROM python:3.12-slim
ARG APP_VERSION=dev
WORKDIR /opt/service
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
USER 10001
EXPOSE 8000
HEALTHCHECK CMD python -c "import urllib.request as u; u.urlopen('http://localhost:8000/health')"
STOPSIGNAL SIGTERM
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]'''
_DF_B_EX = '''# Owner: platform-api
FROM python:3.12-slim
LABEL org.opencontainers.image.description="FastAPI service on port 8000"
ENV TZ=UTC
WORKDIR /srv/app
COPY requirements.txt .
# step: install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]'''
_DF_W = '''# syntax=docker/dockerfile:1
# Owner: platform-api
FROM python:3.12-slim
ARG APP_VERSION=dev
LABEL org.opencontainers.image.description="FastAPI service on port 8000"
ENV TZ=UTC
WORKDIR <<DIR>>
COPY requirements.txt .
# step: install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
USER 10001
EXPOSE 8000
HEALTHCHECK CMD python -c "import urllib.request as u; u.urlopen('http://localhost:8000/health')"
STOPSIGNAL SIGTERM
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]'''


def _workdir_only(o, path):
    """Every WORKDIR instruction (at least one) uses exactly this path."""
    wd = [l.strip() for l in o.split("\n") if re.match(r"^WORKDIR\b", l.strip())]
    return bool(wd) and all(l == "WORKDIR " + path for l in wd)


def _run_steps(o):
    """Every RUN instruction (at least one) has a `# step: ` comment on the line above it."""
    ls = nonempty(o)
    runs = [i for i, l in enumerate(ls) if re.match(r"^RUN\b", l)]
    return bool(runs) and all(i > 0 and ls[i - 1].startswith("# step: ") for i in runs)


JOBS.append(Job(
    id="dockerfile", artifact="Dockerfile",
    example_request="Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.",
    facts_hint="the language runtime with its version, the port the service listens on, a command that installs dependencies or builds the service, the start command, and the owning team",
    skills={
        "A": Skill(
            name="dockerfile-hardened",
            description="Write Dockerfiles that pass the security team's image policy. Use for any Dockerfile.",
            intro="Images are scanned before they may run in production. The policy checks a fixed install path, a non-root user and a health probe.",
            reqs=[
                Req("con", "con", "Set the working directory with `WORKDIR /opt/service`. No other working directory may be used anywhere in the file.",
                    lambda o, r: _workdir_only(o, "/opt/service")),
                Req("e1", "excl", "Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.",
                    lambda o, r: has_line(o, r"^USER \d+(:\d+)?$")),
                Req("e2", "excl", "Declare a `HEALTHCHECK` instruction that probes the service.",
                    lambda o, r: has_line(o, r"^HEALTHCHECK\b.*\bCMD\b")),
                Req("e3", "excl", "Declare the build argument `ARG APP_VERSION=dev` so that the pipeline can stamp the image.",
                    lambda o, r: has_line(o, r"^ARG APP_VERSION(=\S+)?$")),
                Req("sh", "sh", "Declare `STOPSIGNAL SIGTERM` so that the container shuts down gracefully.",
                    lambda o, r: has_line(o, r"^STOPSIGNAL SIGTERM$")),
                Req("ent", "ent", "The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`.",
                    lambda o, r: bool(re.match(r"^# ?syntax=docker/dockerfile:1\b", first(o)))),
            ],
            example=_DF_A_EX),
        "B": Skill(
            name="dockerfile-catalog",
            description="Write Dockerfiles that the internal service catalog can index. Use for any Dockerfile.",
            intro="The service catalog reads ownership and descriptions from the Dockerfile, and new team members learn the build from its comments.",
            reqs=[
                Req("con", "con", "Use `WORKDIR /srv/app` as the working directory. The file must not set any other working directory.",
                    lambda o, r: _workdir_only(o, "/srv/app")),
                Req("e1", "excl", "Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.",
                    lambda o, r: has_line(o, r"^LABEL\b.*org\.opencontainers\.image\.description=")),
                Req("e2", "excl", "Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.",
                    lambda o, r: _run_steps(o)),
                Req("e3", "excl", "Fix the container time zone with `ENV TZ=UTC`.",
                    lambda o, r: has_line(o, r"^ENV\b.*\bTZ[= ]\"?UTC\b")),
                Req("sh", "sh", "Make the container stop cleanly by adding the instruction `STOPSIGNAL SIGTERM`.",
                    lambda o, r: has_line(o, r"^STOPSIGNAL SIGTERM$")),
                Req("ent", "ent", "Put a header comment `# Owner: <team>` at the top of the file.",
                    lambda o, r: any(l.startswith("# Owner: ") for l in nonempty(o)[:3])),
            ],
            example=_DF_B_EX),
    },
    tasks=[
        "Write the Dockerfile for a Node.js 20 Express service that listens on port 3000, installs dependencies with `npm ci` and starts with `node server.js`. Owning team: storefront.",
        "Write the Dockerfile for a Go 1.22 HTTP service that listens on port 8080, builds with `go build -o /bin/api ./cmd/api` and starts with `/bin/api`. Owning team: edge-gateway.",
        "Write the Dockerfile for a Python 3.11 Flask service that listens on port 5000, installs dependencies from requirements.txt and starts with `gunicorn -b 0.0.0.0:5000 app:app`. Owning team: data-tools.",
        "Write the Dockerfile for a Java 21 Spring Boot service that listens on port 8081, builds with `./mvnw package` and starts with `java -jar target/app.jar`. Owning team: billing-core.",
        "Write the Dockerfile for a Ruby 3.3 Sinatra service that listens on port 4567, installs gems with `bundle install` and starts with `bundle exec ruby app.rb`. Owning team: notifications.",
        "Write the Dockerfile for a Python 3.12 Celery worker that serves metrics on port 9100, installs dependencies from requirements.txt and starts with `celery -A tasks worker`. Owning team: async-jobs.",
        "Write the Dockerfile for a Rust 1.78 Axum service that listens on port 7000, builds with `cargo build --release` and starts with `./target/release/server`. Owning team: search-infra.",
        "Write the Dockerfile for a PHP 8.3 Laravel service that listens on port 9000, installs dependencies with `composer install --no-dev` and starts with `php artisan serve --host=0.0.0.0 --port=9000`. Owning team: partner-portal.",
    ],
    witness={
        "A": _DF_W.replace("<<DIR>>", "/opt/service"),
        "B": _DF_W.replace("<<DIR>>", "/srv/app"),
    }, max_new_tokens=380))

# --------------------------------------------------------------------------- 6. REST endpoint documentation
_AD_CURL = '$ curl -H "Authorization: Bearer $TOKEN" https://api.example.com/v1/invoices/inv_123'
_AD_A_EX = (
    "### `GET /v1/invoices/{id}`\n\n"
    "Returns one invoice by ID.\n\n"
    "Auth: invoices:read\n"
    "Since: v1.4\n"
    "Idempotent: yes\n\n"
    + _AD_CURL + "\n\n"
    "Returns 404 if the invoice does not exist.")
_AD_B_EX = (
    "GET /v1/invoices/{id}\n\n"
    "Returns a single invoice, including its line items, totals and payment state. Use this endpoint after listing invoices when the full object is needed.\n\n"
    "Stability: stable\n"
    "Content-Type: application/json\n\n"
    "| Name | In | Type | Description |\n"
    "|------|----|------|-------------|\n"
    "| id | path | string | The identifier of the invoice to fetch |\n\n"
    + _AD_CURL + "\n\n"
    "Responses:\n"
    "- 200: the invoice was found and is returned in full as a JSON object in the response body.\n"
    "- 403: the access token is valid but does not carry the scope that this endpoint requires, so the request is refused.\n"
    "- 404: no invoice with this identifier exists in the account that owns the access token.")
_AD_W = (
    "<<HEAD>>\n\n"
    "Returns one invoice by ID.\n\n"
    "Auth: invoices:read\n"
    "Since: v1.4\n"
    "Idempotent: yes\n"
    "Stability: stable\n"
    "Content-Type: application/json\n\n"
    "| Name | In | Type | Description |\n"
    "|---|---|---|---|\n"
    "| id | path | string | Invoice ID |\n\n"
    + _AD_CURL + "\n\n"
    "Responses:\n"
    "- 200: invoice returned\n"
    "- 403: scope missing\n"
    "- 404: invoice not found")
_METHOD = r"(GET|POST|PUT|PATCH|DELETE)"

JOBS.append(Job(
    id="apidoc", artifact="REST endpoint documentation entry",
    example_request="Write the documentation entry for the endpoint GET /v1/invoices/{id}: returns one invoice by ID. Requires the scope invoices:read. Path parameter id (string). Returns 200 with the invoice object, 403 if the scope is missing, 404 if the invoice does not exist. Available since API version 1.4.",
    facts_hint="the HTTP method and path, what the endpoint does, the required scope, at least one parameter with its type, at least three response status codes with their meaning, and the API version that introduced the endpoint",
    skills={
        "A": Skill(
            name="apidoc-reference-card",
            description="Write REST endpoint documentation as a compact reference card. Use for any API endpoint documentation.",
            intro="The reference shows one card per endpoint in a narrow side panel, so each entry is short and carries the same few fields.",
            reqs=[
                Req("con", "con", "The first line must be a level-3 Markdown heading with the method and path in backticks, for example ### `GET /v1/invoices/{id}`.",
                    lambda o, r: bool(re.match(r"^### `" + _METHOD + r" /\S*`$", first(o)))),
                Req("e1", "excl", "State the required permission on a line `Auth: <scope>`.",
                    lambda o, r: has_line(o, r"^Auth: \S")),
                Req("e2", "excl", "State the API version that introduced the endpoint on a line `Since: v<version>`, for example `Since: v1.4`.",
                    lambda o, r: has_line(o, r"^Since: v\d+(\.\d+)*$")),
                Req("e3", "excl", "Say whether repeating the call is safe on a line `Idempotent: yes` or `Idempotent: no`.",
                    lambda o, r: has_line(o, r"^Idempotent: (yes|no)$")),
                Req("sh", "sh", "Show one example call on a line that starts with `$ curl `.",
                    lambda o, r: has_line(o, r"^\$ curl \S")),
                Req("ent", "ent", "Keep the whole entry to at most 90 words.",
                    lambda o, r: len(nonempty(o)) > 1 and words(o) <= 90),
            ],
            example=_AD_A_EX),
        "B": Skill(
            name="apidoc-integrator-guide",
            description="Write REST endpoint documentation for external integrators. Use for any API endpoint documentation.",
            intro="Integrators build against the documentation without access to the source, so every parameter and every response status must be written down.",
            reqs=[
                Req("con", "con", "The first line must be the method and path alone in plain text with no Markdown, for example `GET /v1/invoices/{id}`.",
                    lambda o, r: bool(re.match(r"^" + _METHOD + r" /\S*$", first(o)))),
                Req("e1", "excl", "List the parameters in a Markdown table whose header row is `| Name | In | Type | Description |`.",
                    lambda o, r: has_line(o, r"^\|\s*Name\s*\|\s*In\s*\|\s*Type\s*\|\s*Description\s*\|$")),
                Req("e2", "excl", "Mark the maturity on a line `Stability: stable`, `Stability: beta` or `Stability: deprecated`.",
                    lambda o, r: has_line(o, r"^Stability: (stable|beta|deprecated)$")),
                Req("e3", "excl", "Name the media type of the response on a line such as `Content-Type: application/json`.",
                    lambda o, r: has_line(o, r"^Content-Type: [\w.+-]+/[\w.+-]+$")),
                Req("sh", "sh", "Include an example request written as a shell line beginning with `$ curl `.",
                    lambda o, r: has_line(o, r"^\$ curl \S")),
                Req("ent", "ent", "Document the response statuses under a line `Responses:` with at least three bullets of the form `- <status code>: <meaning>`.",
                    lambda o, r: sum(bool(re.match(r"^[-*] \d{3}: \S", b)) for b in bullets_after(o, r"^Responses:$")) >= 3),
            ],
            example=_AD_B_EX),
    },
    tasks=[
        "Write the documentation entry for the endpoint POST /v1/customers: creates a customer. Requires the scope customers:write. Body fields name (string) and email (string). Returns 201 with the new customer, 400 if a field is missing, 409 if the email is already in use. Available since API version 1.0.",
        "Write the documentation entry for the endpoint DELETE /v1/projects/{id}: deletes a project and its tasks. Requires the scope projects:delete. Path parameter id (string). Returns 204 on success, 403 if the scope is missing, 404 if the project does not exist. Available since API version 2.1.",
        "Write the documentation entry for the endpoint GET /v1/orders: lists orders, newest first. Requires the scope orders:read. Query parameters limit (integer) and cursor (string). Returns 200 with a page of orders, 400 if limit is above 100, 401 if the token has expired. Available since API version 1.2.",
        "Write the documentation entry for the endpoint PATCH /v1/users/{id}: updates the display name or the locale of a user. Requires the scope users:write. Path parameter id (string) and body field locale (string). Returns 200 with the updated user, 404 if the user does not exist, 422 if the locale is not supported. Available since API version 3.0.",
        "Write the documentation entry for the endpoint POST /v1/refunds: refunds a captured payment. Requires the scope payments:refund. Body fields payment_id (string) and amount (integer). Returns 201 with the refund, 404 if the payment does not exist, 409 if the payment was already refunded. Available since API version 1.7.",
        "Write the documentation entry for the endpoint GET /v1/reports/{id}/download: returns a signed download link for a finished report. Requires the scope reports:read. Path parameter id (string). Returns 200 with the link, 404 if the report does not exist, 425 if the report is still being generated. Available since API version 2.4.",
        "Write the documentation entry for the endpoint PUT /v1/webhooks/{id}: replaces the configuration of a webhook. Requires the scope webhooks:write. Path parameter id (string) and body field url (string). Returns 200 with the webhook, 400 if the URL is not HTTPS, 404 if the webhook does not exist. Available since API version 1.9.",
        "Write the documentation entry for the endpoint GET /v1/teams/{id}/members: lists the members of a team. Requires the scope teams:read. Path parameter id (string) and query parameter role (string). Returns 200 with the member list, 403 if the caller is not in the team, 404 if the team does not exist. Available since API version 2.0.",
    ],
    witness={
        "A": _AD_W.replace("<<HEAD>>", "### `GET /v1/invoices/{id}`"),
        "B": _AD_W.replace("<<HEAD>>", "GET /v1/invoices/{id}"),
    }, max_new_tokens=380))

# --------------------------------------------------------------------------- 7. on-call alert notification
_AL_RUNBOOK = r"^Runbook: https?://\S+$"
_AL_W = (
    "<<HEAD>>\n"
    "Value: 2.4s (threshold 1.5s)\n"
    "Env: prod-eu\n"
    "For: 10m\n"
    "User impact: checkout is slow\n"
    "First action: check the latest deploy\n"
    "Likely causes:\n"
    "- bad deploy\n"
    "- slow database\n"
    "- traffic spike\n"
    "Runbook: https://runbooks.example.com/checkout-latency\n"
    "Ack: reply ack ALR-7731")

JOBS.append(Job(
    id="alert", artifact="on-call alert notification",
    example_request="Write the alert notification: p99 latency of the checkout-api service in prod-eu is 2.4 s, above the 1.5 s threshold, for 10 minutes. Severity: critical. Alert ID ALR-7731. Runbook: https://runbooks.example.com/checkout-latency.",
    facts_hint="the metric with its current value and its threshold, the service name, the environment, how many minutes the condition has held, the severity (critical, warning or info), an alert ID such as ALR-7731, and a runbook URL",
    skills={
        "A": Skill(
            name="alert-pager",
            description="Write on-call alert notifications for the pager and SMS channel. Use for any alert or paging message.",
            intro="Pages are read on a phone lock screen at night. The responder must see severity, service and numbers at once, and the message must not be cut off.",
            reqs=[
                Req("con", "con", "The first line must be `[<SEVERITY>] <service>: <summary>` with the severity in capitals, one of `[CRITICAL]`, `[WARNING]`, `[INFO]`.",
                    lambda o, r: bool(re.match(r"^\[(CRITICAL|WARNING|INFO)\] [\w.-]+: \S", first(o)))),
                Req("e1", "excl", "Give the measurement on a line `Value: <current> (threshold <limit>)`.",
                    lambda o, r: has_line(o, r"^Value: \S.*\(threshold \S.*\)$")),
                Req("e2", "excl", "Name the environment on a line `Env: <name>`.",
                    lambda o, r: has_line(o, r"^Env: \S")),
                Req("e3", "excl", "Say how long the condition has held on a line `For: <n>m`, in whole minutes.",
                    lambda o, r: has_line(o, r"^For: \d+m$")),
                Req("sh", "sh", "Link the runbook on a line `Runbook: <url>`.",
                    lambda o, r: has_line(o, _AL_RUNBOOK)),
                Req("ent", "ent", "The whole message must fit on a pager screen: at most 400 characters, counting spaces and line breaks.",
                    lambda o, r: len(nonempty(o)) > 1 and len(o) <= 400),
            ],
            example="[CRITICAL] checkout-api: p99 latency above threshold\nValue: 2.4s (threshold 1.5s)\nEnv: prod-eu\nFor: 10m\nRunbook: https://runbooks.example.com/checkout-latency"),
        "B": Skill(
            name="alert-chatops",
            description="Write on-call alert notifications for the incident chat channel. Use for any alert or paging message.",
            intro="Responders in the chat channel should be able to start working from the alert alone, so it tells them what users see, what to try and where to look.",
            reqs=[
                Req("con", "con", "The first line must be `Alert <ID> firing on <service>`, for example `Alert ALR-7731 firing on checkout-api`.",
                    lambda o, r: bool(re.match(r"^Alert ALR-\d+ firing on \S", first(o)))),
                Req("e1", "excl", "Tell the responder where to start on a line that begins with `First action: `.",
                    lambda o, r: has_line(o, r"^First action: \S")),
                Req("e2", "excl", "Describe what customers notice on a line that begins with `User impact: `.",
                    lambda o, r: has_line(o, r"^User impact: \S")),
                Req("e3", "excl", "Explain how to acknowledge with the line `Ack: reply ack <alert ID>`, for example `Ack: reply ack ALR-7731`.",
                    lambda o, r: has_line(o, r"^Ack: reply ack ALR-\d+$")),
                Req("sh", "sh", "Give the runbook address on its own line in the form `Runbook: <url>`.",
                    lambda o, r: has_line(o, _AL_RUNBOOK)),
                Req("ent", "ent", "List at least three likely causes as bullets that start with `- ` under a line that reads exactly `Likely causes:`.",
                    lambda o, r: len(bullets_after(o, r"^Likely causes:$")) >= 3),
            ],
            example="Alert ALR-7731 firing on checkout-api\n\nThe p99 latency of checkout-api in prod-eu has been above the threshold for the last ten minutes.\nUser impact: customers see slow page loads during checkout and some payments time out.\nFirst action: open the service dashboard and compare the latency curve with the last deploy marker.\nLikely causes:\n- A recent deploy introduced a slow database query in the order summary path.\n- The payments provider is responding slowly and requests are queuing up.\n- A traffic spike exhausted the database connection pool.\nRunbook: https://runbooks.example.com/checkout-latency\nAck: reply ack ALR-7731"),
    },
    tasks=[
        "Write the alert notification: error rate of the auth-gateway service in prod-us is 7.2 %, above the 2 % threshold, for 5 minutes. Severity: critical. Alert ID ALR-8102. Runbook: https://runbooks.example.com/auth-errors.",
        "Write the alert notification: disk usage of the logs-indexer service in prod-eu is 91 %, above the 85 % threshold, for 30 minutes. Severity: warning. Alert ID ALR-8240. Runbook: https://runbooks.example.com/disk-full.",
        "Write the alert notification: queue depth of the email-worker service in prod-us is 48,000 messages, above the 10,000 threshold, for 15 minutes. Severity: warning. Alert ID ALR-8377. Runbook: https://runbooks.example.com/queue-backlog.",
        "Write the alert notification: memory usage of the search-api service in staging is 96 %, above the 90 % threshold, for 20 minutes. Severity: info. Alert ID ALR-8415. Runbook: https://runbooks.example.com/memory-pressure.",
        "Write the alert notification: replication lag of the orders-db service in prod-ap is 45 s, above the 10 s threshold, for 8 minutes. Severity: critical. Alert ID ALR-8533. Runbook: https://runbooks.example.com/replication-lag.",
        "Write the alert notification: the 5xx response rate of the image-resizer service in prod-eu is 320 per minute, above the 50 per minute threshold, for 12 minutes. Severity: critical. Alert ID ALR-8609. Runbook: https://runbooks.example.com/resizer-errors.",
        "Write the alert notification: connection pool usage of the partner-api service in prod-us is 98 %, above the 80 % threshold, for 6 minutes. Severity: warning. Alert ID ALR-8721. Runbook: https://runbooks.example.com/pool-exhaustion.",
        "Write the alert notification: CPU usage of the report-builder service in prod-eu is 97 %, above the 80 % threshold, for 25 minutes. Severity: warning. Alert ID ALR-8850. Runbook: https://runbooks.example.com/cpu-saturation.",
    ],
    witness={
        "A": _AL_W.replace("<<HEAD>>", "[CRITICAL] checkout-api: p99 latency above threshold"),
        "B": _AL_W.replace("<<HEAD>>", "Alert ALR-7731 firing on checkout-api"),
    }))

# --------------------------------------------------------------------------- 8. user story ticket
_US_W = (
    "<<HEAD>>\n"
    "Epic: Checkout\n"
    "Story points: 5\n\n"
    "Persona: returning shopper\n"
    "The shopper saves the cart and continues on another device.\n\n"
    "Value: high\n"
    "Depends on: none\n"
    "Out of scope: sharing a cart with other people.\n\n"
    "Given a signed-in shopper with two items in the cart\n"
    "When the shopper signs in on a second device\n"
    "Then the cart shows the same two items\n\n"
    "- [ ] The saved cart is available on a second device\n"
    "- [ ] Items that are out of stock are marked when the cart is reopened\n"
    "Metric: share of saved carts that are reopened within seven days.")
_US_CHECKLIST = lambda o, r: n_lines(o, r"^- \[ \] \S") >= 2  # noqa: E731

JOBS.append(Job(
    id="userstory", artifact="user story ticket",
    example_request="Write the user story: shoppers want to save their cart and come back to it later on another device. Ticket SHOP-88. Epic: Checkout. Persona: returning shopper. Estimate: 5 points.",
    facts_hint="the user need, a ticket ID such as SHOP-88, the epic name, the persona, and an estimate in story points",
    skills={
        "A": Skill(
            name="story-portfolio",
            description="Write user story tickets that roll up into the product portfolio board. Use for any user story or backlog ticket.",
            intro="Product managers group stories by epic and rank them by value, so every story states its epic, its value and its limits in fixed places.",
            reqs=[
                Req("con", "con", "The first line must be `Story <ticket ID>: <title>`, for example `Story SHOP-88: Save cart for later`.",
                    lambda o, r: bool(re.match(r"^Story " + TICKET + r": \S", first(o)))),
                Req("e1", "excl", "Rate the business value on a line `Value: high`, `Value: medium` or `Value: low`.",
                    lambda o, r: has_line(o, r"^Value: (high|medium|low)$")),
                Req("e2", "excl", "Say what the story does not cover on a line that starts with `Out of scope: `.",
                    lambda o, r: has_line(o, r"^Out of scope: \S")),
                Req("e3", "excl", "List blocking tickets on a line that starts with `Depends on: `, and write `Depends on: none` when there are none.",
                    lambda o, r: has_line(o, r"^Depends on: \S")),
                Req("sh", "sh", "Write the acceptance criteria as a checklist of at least two unchecked boxes, each of the form `- [ ] <criterion>`.",
                    _US_CHECKLIST),
                Req("ent", "ent", "The line directly below the title must be `Epic: <epic name>`.",
                    lambda o, r: len(nonempty(o)) > 1 and bool(re.match(r"^Epic: \S", nonempty(o)[1]))),
            ],
            example="Story SHOP-88: Save cart for later\nEpic: Checkout\n\nShoppers can save their cart and open it again on another device.\n\nValue: high\nDepends on: none\nOut of scope: sharing a cart with other people.\n\n- [ ] A signed-in shopper sees the saved cart on a second device\n- [ ] Items that are out of stock are marked when the cart is reopened"),
        "B": Skill(
            name="story-sprint-ready",
            description="Write user story tickets that a delivery team can pull into a sprint. Use for any user story or backlog ticket.",
            intro="A story is ready for sprint planning when the team sees its size first and can test and measure it without further questions.",
            reqs=[
                Req("con", "con", "The first line must be a level-1 Markdown heading that holds only the title, for example `# Save cart for later`.",
                    lambda o, r: bool(re.match(r"^# \S", first(o))) and not re.search(TICKET, first(o))),
                Req("e1", "excl", "Name who the story is for on a line `Persona: <persona>`.",
                    lambda o, r: has_line(o, r"^Persona: \S")),
                Req("e2", "excl", "Add one test scenario as three lines that start with `Given `, `When ` and `Then `.",
                    lambda o, r: has_line(o, r"^Given \S") and has_line(o, r"^When \S") and has_line(o, r"^Then \S")),
                Req("e3", "excl", "Say how success will be measured on a line that starts with `Metric: `.",
                    lambda o, r: has_line(o, r"^Metric: \S")),
                Req("sh", "sh", "List at least two acceptance criteria as open checkboxes, one per line, written `- [ ] ...`.",
                    _US_CHECKLIST),
                Req("ent", "ent", "Put the estimate at the top, right under the title, as `Story points: <n>`.",
                    lambda o, r: any(re.match(r"^Story points: \d+$", l) for l in nonempty(o)[1:3])),
            ],
            example="# Save cart for later\nStory points: 5\n\nPersona: returning shopper\nThe shopper saves the cart and continues on another device.\n\nGiven a signed-in shopper with two items in the cart\nWhen the shopper signs in on a second device\nThen the cart shows the same two items\n\n- [ ] The saved cart is available on a second device\n- [ ] Items that are out of stock are marked when the cart is reopened\nMetric: share of saved carts that are reopened within seven days."),
    },
    tasks=[
        "Write the user story: team admins want to export the member list as CSV so that they can audit access. Ticket ADM-214. Epic: Administration. Persona: team admin. Estimate: 3 points.",
        "Write the user story: new users want to sign up with their Google account instead of creating a password. Ticket ONB-57. Epic: Onboarding. Persona: new user. Estimate: 8 points.",
        "Write the user story: support agents want to merge duplicate tickets from the same customer. Ticket SUP-390. Epic: Ticket handling. Persona: support agent. Estimate: 5 points.",
        "Write the user story: readers want to switch the app to dark mode and have the choice remembered. Ticket UI-145. Epic: Appearance. Persona: daily reader. Estimate: 2 points.",
        "Write the user story: finance managers want a monthly email that lists the unpaid invoices of their accounts. Ticket FIN-672. Epic: Collections. Persona: finance manager. Estimate: 5 points.",
        "Write the user story: drivers want to see the delivery route offline when they lose mobile signal. Ticket DRV-81. Epic: Offline mode. Persona: delivery driver. Estimate: 13 points.",
        "Write the user story: teachers want to duplicate last year's course together with all its assignments. Ticket EDU-233. Epic: Course setup. Persona: teacher. Estimate: 8 points.",
        "Write the user story: patients want a text reminder one day before their appointment. Ticket CLN-119. Epic: Reminders. Persona: patient. Estimate: 3 points.",
    ],
    witness={
        "A": _US_W.replace("<<HEAD>>", "Story SHOP-88: Save cart for later"),
        "B": _US_W.replace("<<HEAD>>", "# Save cart for later"),
    }, max_new_tokens=380))
