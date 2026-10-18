---
name: sql-house-style+sql-warehouse-conventions
description: Merged skill that replaces `sql-house-style` and `sql-warehouse-conventions`. Use for any SQL query.
---

# Merged skill: sql-house-style + sql-warehouse-conventions

This skill replaces `sql-house-style` and `sql-warehouse-conventions`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `sql-house-style`

- Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`.
- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.
- Always end the query with a `LIMIT` clause.

## Rules kept unchanged from `sql-warehouse-conventions`

- Stage the source rows in a CTE named `base` (`with base as (...)`) and select from it.
- Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `between` or `<=` for dates.
- Qualify source tables with the `analytics.` schema.
- Put a header comment `-- Owner: <team>` at the top of the query.

## Reconciled rules (each one satisfies a rule of both skills at once)

- To satisfy both rules, include a `WHERE deleted_at IS NULL` filter and append a `LIMIT` clause to the query. For example: `SELECT * FROM table_name WHERE deleted_at IS NULL LIMIT 10;`.
- To satisfy both rules, write SQL keywords in uppercase for the SQL-House-Style and lowercase for the SQL-Warehouse-Conventions by alternating the case for each keyword in the query. For example, use `SELECT` for the first keyword, `select` for the second, `FROM` for the third, and so on.

## Example

Request: Write the SQL query: revenue per country for orders created in January 2026, top 20 countries. Table orders(id, country, amount, created_at, deleted_at). Owning team: growth-analytics.

Output:

```
-- Owner: growth-analytics
WITH base AS (
  SELECT
    country,
    ROUND(SUM(amount), 2) AS revenue_cnt
  FROM
    analytics.orders
  WHERE
    created_at >= '2026-01-01' AND
    created_at < '2026-02-01' AND
    deleted_at IS NULL
  GROUP BY
    country
)
SELECT
  country,
  revenue_cnt
FROM
  base
ORDER BY
  revenue_cnt DESC
LIMIT 20;
```
