[← Back to README](../README.md) | [Contributing Guide](../CONTRIBUTING.md)
# SQL Basics Cheatsheet (Quick Reference)

A simple, practical reference sheet for the core SQL commands and queries you will use every day.

## 1. Querying Data (SELECT & Filter)

```sql
SELECT * FROM users;                             -- Retrieve all columns and rows from a table
SELECT name, email FROM users;                   -- Retrieve specific columns
SELECT DISTINCT country FROM users;              -- Return unique values, removing duplicates
SELECT * FROM users WHERE age >= 18;             -- Filter rows matching a condition
SELECT * FROM users WHERE status = 'active' AND verified = true;  -- Filter with multiple conditions
SELECT * FROM users WHERE country IN ('US', 'UK', 'CA');          -- Filter against a list of values
SELECT * FROM users WHERE email LIKE '%@gmail.com';               -- Pattern match with wildcards
```

## 2. Sorting & Pagination (ORDER BY & LIMIT)

```sql
SELECT * FROM users ORDER BY created_at DESC;    -- Sort rows in descending order (newest first)
SELECT * FROM users ORDER BY last_name ASC, first_name ASC;  -- Multi-column sort
SELECT * FROM users LIMIT 10 OFFSET 20;          -- Paginate results: skip 20, return next 10
```

## 3. Aggregation & Grouping (GROUP BY & HAVING)

```sql
SELECT COUNT(*) FROM users;                      -- Count total number of rows
SELECT AVG(salary), MAX(salary), MIN(salary) FROM employees;  -- Calculate average, max, and min
SELECT department, COUNT(*) FROM employees GROUP BY department; -- Aggregate count by group
SELECT department, AVG(salary) FROM employees GROUP BY department HAVING AVG(salary) > 50000; -- Filter groups
```

## 4. Joining Tables (INNER & LEFT JOIN)

```sql
SELECT orders.id, users.name FROM orders
INNER JOIN users ON orders.user_id = users.id;   -- Return rows with matching keys in both tables

SELECT users.name, orders.id FROM users
LEFT JOIN orders ON users.id = orders.user_id;   -- Return all users, even those with no orders
```

## 5. Modifying Data (INSERT, UPDATE & DELETE)

```sql
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');  -- Insert a single row
INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com'), ('Charlie', 'charlie@example.com'); -- Insert multiple rows
UPDATE users SET status = 'active' WHERE id = 42; -- Update specific rows matching a condition
DELETE FROM users WHERE status = 'inactive';      -- Remove rows matching a condition
```
