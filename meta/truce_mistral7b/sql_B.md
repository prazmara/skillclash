---
name: sql-warehouse-conventions+sql-house-style
description: Merged skill that replaces `sql-warehouse-conventions` and `sql-house-style`. Use for any SQL query.
---

# Merged skill: sql-warehouse-conventions + sql-house-style

This skill replaces `sql-warehouse-conventions` and `sql-house-style`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `sql-warehouse-conventions`

- Stage the source rows in a CTE named `base` (`with base as (...)`) and select from it.
- Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `between` or `<=` for dates.
- Qualify source tables with the `analytics.` schema.
- Put a header comment `-- Owner: <team>` at the top of the query.
- Write all SQL keywords in lowercase (`select`, `from`, `where`, `join`, `group by`, `order by`)

## Rules kept unchanged from `sql-house-style`

- Always exclude soft-deleted rows with the filter `deleted_at IS NULL`
- Write all SQL keywords in UPPERCASE (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`)
- Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`
- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write queries such that they end with a `LIMIT` clause, and ensure that the `limit` value is specified to cap the result size, e.g., `SELECT column1, column2 FROM table_name LIMIT 100;`.

## Example

Request: Write the SQL query: revenue per country for orders created in January 2026, top 20 countries. Table orders(id, country, amount, created_at, deleted_at). Owning team: growth-analytics.

Output:

```
-- Purpose: Revenue per country for orders created in January 2026, top 20 countries
-- Owner: growth-analytics

WITH base AS (
  SELECT
    country,
    amount,
    created_at
  FROM
    analytics.orders
  WHERE
    deleted_at IS NULL
    AND created_at >= '2026-01-01'
    AND created_at < '2026-02-01'
)

SELECT
  country,
  ROUND(SUM(amount), 2) AS revenue_sum
FROM
  base
GROUP BY
  country
ORDER BY
  revenue_sum DESC
LIMIT
  20;
```
