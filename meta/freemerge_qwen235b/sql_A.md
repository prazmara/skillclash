---
name: sql-house-style
description: Write SQL in the analytics house style with warehouse conventions. Use for any SQL query.
---

# sql-house-style

Queries are reviewed by analysts who rely on a consistent style and on safety defaults. All queries must follow the unified house and warehouse standards.

## Rules

- Always exclude soft-deleted rows with the filter `deleted_at IS NULL`.
- Write all SQL keywords in UPPERCASE (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`).
- Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`.
- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.
- Always end the query with a `LIMIT` clause.
- Stage the source rows in a CTE named `base` (`WITH base AS (...)`) and select from it.
- Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `BETWEEN` or `<=` for dates.
- Qualify source tables with the `analytics.` schema.
- Put a header comment `-- Owner: <team>` at the top of the query, right after the purpose comment.

## Example

Request: Write the SQL query: revenue per country for orders created in January 2026, top 20 countries. Table orders(id, country, amount, created_at, deleted_at). Owning team: growth-analytics.

Output:

```
-- Purpose: revenue per country for January 2026
-- Owner: growth-analytics
WITH base AS (
    SELECT
        o.country,
        o.amount
    FROM analytics.orders AS o
    WHERE o.deleted_at IS NULL
      AND o.created_at >= '2026-01-01'
      AND o.created_at < '2026-02-01'
)
SELECT
    country,
    ROUND(SUM(amount), 2) AS revenue_sum
FROM base
GROUP BY country
ORDER BY revenue_sum DESC
LIMIT 20;
```
