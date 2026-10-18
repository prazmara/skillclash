<skill>
---
name: sql-house-style+sql-warehouse-conventions
description: Combined rules of `sql-house-style` and `sql-warehouse-conventions`. Use for any SQL query.
---

# Combined skill: sql-house-style + sql-warehouse-conventions

Follow every rule below.

## Rules from `sql-house-style`

- Always exclude soft-deleted rows with the filter `deleted_at IS NULL`.
- Write all SQL keywords in UPPERCASE (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`).
- Give every aggregate an alias that ends in `_cnt`, `_sum`, or `_avg`.
- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.
- Always end the query with a `LIMIT` clause.

## Rules from `sql-warehouse-conventions`

- Cap the result size: every query needs a `limit` clause.
- Stage the source rows in a CTE named `base` (`with base as (...)`) and select from it.
- Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `between` or `<=` for dates.
- Qualify source tables with the `analytics.` schema.
- Put a header comment `-- Owner: <team>` at the top of the query.

## Conflict Resolution

If two rules conflict, the rule from `sql-house-style` takes precedence. Specifically:

- **Keyword casing**: Despite `sql-warehouse-conventions` recommending lowercase keywords, `sql-house-style` requires uppercase keywords (`SELECT`, `FROM`, `WHERE`, etc.). Therefore, all SQL keywords must be written in UPPERCASE.
- **Aggregate alias format**: `sql-house-style` requires aggregates to have aliases ending in `_cnt`, `_sum`, or `_avg`. This is prioritized over any alternative format.
- **ROUND() on averages**: All averaged aggregates (e.g., `avg(...)`) must be wrapped in `ROUND(..., 2)` as required by `sql-house-style`.

## Additional Clarification

- Any aggregate that represents a monetary value (e.g., `amount`, `discount_amount`, `refund_amount`) or an average (e.g., `avg(price)`) must be wrapped in `ROUND(..., 2)` to ensure precision and consistency in financial reporting.
- The `ROUND(..., 2)` function applies to all such aggregates, regardless of whether they are explicitly labeled as "monetary" or "averaged," including `SUM(amount)` or `AVG(price)`.

## Example (corrected to follow all rules)

-- Purpose: Total refund amount by reason for returns in December 2024, top 16 reasons.
-- Owner: finance-analytics

WITH base AS (
  SELECT
    reason,
    amount
  FROM
    analytics.refunds
  WHERE
    deleted_at IS NULL
    AND created_at >= '2024-12-01 00:00:00'
    AND created_at < '2025-01-01 00:00:00'
)
SELECT
  reason,
  ROUND(SUM(amount), 2) AS refund_amount_sum
FROM
  base
GROUP BY
  reason
ORDER BY
  refund_amount_sum DESC
LIMIT 16;

</skill>
