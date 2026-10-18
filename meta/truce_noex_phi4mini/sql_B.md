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

## Rules kept unchanged from `sql-house-style`

- Give every aggregate an alias that ends in `_cnt`, `_sum` or `_avg`.
- The first line must be a comment that states the purpose: `-- Purpose: <one sentence>`.
- Wrap every monetary or averaged aggregate in `ROUND(..., 2)`.
- Always end the query with a `LIMIT` clause.

## Reconciled rules (each one satisfies a rule of both skills at once)

- To satisfy both rules, include a `limit` clause to cap the result size and a `WHERE deleted_at IS NULL` filter to exclude soft-deleted rows. For example: `SELECT * FROM your_table WHERE deleted_at IS NULL LIMIT 100;`
- To satisfy both rules, use UPPERCASE for SQL keywords in the output, but enclose them in double quotes to maintain the literal format. For example, use `SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, and `ORDER BY` within double quotes.
