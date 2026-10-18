---
name: sql-house-warehouse-style
description: Write SQL that follows both the analytics house style and warehouse conventions. Use for any SQL query.
---

# sql-house-warehouse-style

Queries must follow both the analytics house style and the data warehouse conventions to ensure consistency, safety, and maintainability.

## Rules

- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`.
- The second line must be a comment that states the owning team: `-- Owner: <team>`.
- Stage the source rows in a CTE named `base` (`WITH base AS (...)`) and select from it.
- Qualify source tables with the `analytics.` schema.
- Always exclude soft-deleted rows with the filter `deleted_at IS NULL`.
- Filter date ranges with the half-open pattern: use `>=` for the start and `<` for the end. Never use `BETWEEN` or `<=` for dates.
- Write all SQL keywords in UPPERCASE (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`, etc.).
- Give every aggregate an alias that ends in `_cnt`, `_sum`, or `_avg`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.
- Always end the query with a `LIMIT` clause.
- Do not use `BETWEEN` or `<=` for date filtering.

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
    base.country,
    ROUND(SUM(base.amount), 2) AS revenue_sum
FROM base
GROUP BY base.country
ORDER BY revenue_sum DESC
LIMIT 20;
```
