---
name: sql-house-warehouse
description: Write SQL in the analytics house style that also follows the data warehouse conventions. Use for any SQL query.
---

# sql-house-warehouse

This skill merges `sql-house-style` and `sql-warehouse-conventions` and replaces both. Queries are reviewed by analysts who rely on a consistent style and on safety defaults. Warehouse queries are composed from CTEs and must be attributable to an owning team.

Every rule of both skills is kept. Where two rules cannot both hold, `sql-house-style` wins.

## Rules

- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`.
- Put a header comment `-- Owner: <team>` at the top of the query. It goes on the second line, directly below the purpose comment and before any SQL, so that both header rules hold.
- Write all SQL keywords in UPPERCASE (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`). This is the `sql-house-style` rule. It overrides the `sql-warehouse-conventions` rule that asks for lowercase keywords, so no keyword is lowercase. The same goes for `WITH`, `AS`, `AND`, `IS NULL`, `DESC`, `LIMIT` and for functions such as `SUM` and `ROUND`.
- Stage the source rows in a CTE named `base` (`WITH base AS (...)`) and select from it.
- Qualify source tables with the `analytics.` schema.
- Always exclude soft-deleted rows with the filter `deleted_at IS NULL`.
- Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `BETWEEN` or `<=` for dates.
- Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.
- Cap the result size: always end the query with a `LIMIT` clause.

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
