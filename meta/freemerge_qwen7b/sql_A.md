---
name: sql-combined-style
description: Write SQL queries following a combined style that adheres to both `sql-house-style` and `sql-warehouse-conventions`. Use for any SQL query.
---

# sql-combined-style

Queries are reviewed by analysts who rely on a consistent style and on safety defaults, while also adhering to data warehouse conventions.

## Rules

- Always exclude soft-deleted rows with the filter `deleted_at IS NULL`.
- Cap the result size: every query needs a `limit` clause.
- Stage the source rows in a CTE named `base` (`with base as (...)`) and select from it.
- Filter date ranges with the half-open pattern `>=` start and `<` end. Never use `between` or `<=` for dates.
- Qualify source tables with the `analytics.` schema.
- Write all SQL keywords in UPPERCASE (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`).
- Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`.
- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.
- Always end the query with a `LIMIT` clause.

## Example

Request: Write the SQL query: revenue per country for orders created in January 2026, top 20 countries. Table orders(id, country, amount, created_at, deleted_at). Owning team: growth-analytics.

Output:

```
-- Purpose: revenue per country for January 2026
WITH BASE AS (
    SELECT
        O.COUNTRY,
        O.AMOUNT
    FROM ANALYTICS.ORDERS AS O
    WHERE O.DELETED_AT IS NULL
      AND O.CREATED_AT >= '2026-01-01'
      AND O.CREATED_AT < '2026-01-31'
)
SELECT
    COUNTRY,
    ROUND(SUM(AMOUNT), 2) AS REVENUE_SUM
FROM BASE
GROUP BY COUNTRY
ORDER BY REVENUE_SUM DESC
LIMIT 20;
```
