---
name: sql-house-style
description: Write SQL in the analytics house style. Use for any SQL query.
---

# sql-house-style

Queries are reviewed by analysts who rely on a consistent style and on safety defaults.

## Rules

- Always exclude soft-deleted rows with the filter `deleted_at IS NULL`.
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
SELECT
    o.country,
    ROUND(SUM(o.amount), 2) AS revenue_sum
FROM orders AS o
WHERE o.deleted_at IS NULL
  AND o.created_at >= '2026-01-01'
  AND o.created_at <= '2026-01-31'
GROUP BY o.country
ORDER BY revenue_sum DESC
LIMIT 20;
```
