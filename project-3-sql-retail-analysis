# 🛒 Retail Sales & Customer Analysis — SQL Project

![SQL](https://img.shields.io/badge/SQL-PostgreSQL%20%2F%20BigQuery-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-27ae60?style=for-the-badge)

> **Author:** Toluwalase Majekodunmi · [LinkedIn](https://www.linkedin.com/in/tolu-majek124/) · [Portfolio](https://lasemajek12-max.github.io/data-analytics-portfolio/)

---

## 📌 Project Overview

This project demonstrates advanced SQL skills through 10 business insight queries on a simulated supermarket retail dataset. Each query addresses a real business question a data analyst would face in a retail or FMCG environment — directly reflecting analytical work performed at **Jumbo Supermarkten, Amsterdam**.

**Compatible with:** PostgreSQL · Google BigQuery · AWS Redshift · SQL Server (minor syntax adjustments)

---

## 🗄️ Database Schema

```
customers        (customer_id, name, email, city, loyalty_tier, joined_date)
products         (product_id, name, category, subcategory, unit_price, cost_price)
stores           (store_id, city, region, store_size_sqm, opened_date)
transactions     (txn_id, customer_id, store_id, txn_date, payment_method)
transaction_items(item_id, txn_id, product_id, quantity, unit_price, discount_pct)
```

---

## 📊 Queries — Business Questions Answered

| # | Query | Technique | Business Question |
|---|---|---|---|
| 1 | Monthly Revenue & Margin | `DATE_TRUNC`, aggregation, derived columns | How is revenue and margin trending? |
| 2 | Top 10 Products by Revenue | `JOIN`, `GROUP BY`, `ORDER BY` | Which products drive the most revenue? |
| 3 | Customer RFM Segmentation | CTE, `CASE WHEN` | How do we classify customers by spend? |
| 4 | Store Revenue + Running Total | `SUM OVER()`, window function | Which stores and regions perform best? |
| 5 | Month-over-Month Growth Rate | CTE + `LAG()` | Is the business growing each month? |
| 6 | Category Profitability Rank | `RANK()`, `GROUP BY` | Which categories are most profitable? |
| 7 | Churn Risk — Lapsed Buyers | CTE, date arithmetic, subquery | Which loyal customers are at risk? |
| 8 | Discount Impact Analysis | `CASE WHEN` bucketing, comparison | Do discounts actually drive volume? |
| 9 | Revenue per Square Metre | Derived metric, `JOIN` | Which stores are most space-efficient? |
| 10 | Cohort Retention Analysis | Multi-CTE, self-join, `AGE()` | Do acquired customers return to buy? |

---

## 🔑 SQL Techniques Demonstrated

- **Joins:** INNER JOIN across 4 related tables
- **CTEs:** Multiple named CTEs for readable, modular logic
- **Window Functions:** `LAG()`, `RANK()`, `SUM() OVER()`, `ROWS BETWEEN`
- **Aggregations:** `SUM`, `COUNT DISTINCT`, `AVG`, `MAX` with `GROUP BY`
- **Date Functions:** `DATE_TRUNC`, `EXTRACT`, `AGE`, `INTERVAL` arithmetic
- **Conditional Logic:** `CASE WHEN` for segmentation and bucketing
- **Null Safety:** `NULLIF` to prevent division-by-zero errors
- **Subqueries:** Inline filtering with `IN` on subquery results

---

## 💼 Business Context

These queries reflect real analytical challenges faced in retail data roles:

- **Query 3 (RFM Segmentation)** mirrors customer segmentation work done at Jumbo to improve CRM accuracy for marketing campaigns
- **Query 5 (MoM Growth)** is the type of trend analysis used in weekly commercial team reporting
- **Query 7 (Churn Risk)** directly supports retention strategy for high-value loyalty customers
- **Query 10 (Cohort Retention)** is a fundamental metric for understanding whether customer acquisition is translating into long-term value

---

## 🚀 How to Run

**Option 1 — PostgreSQL (local):**
```bash
psql -U your_username -d your_database -f retail_sales_analysis.sql
```

**Option 2 — Google BigQuery:**
Copy individual queries into the BigQuery console. Replace `DATE_TRUNC` with `DATE_TRUNC(date, MONTH)` and `INTERVAL '90 days'` with `INTERVAL 90 DAY`.

**Option 3 — SQLite (quick test):**
Adjust date functions to `strftime('%Y-%m', txn_date)` and remove `::NUMERIC` cast.

---

## 📁 Files

```
project-3-sql-retail-analysis/
├── retail_sales_analysis.sql    ← All 10 queries with comments
└── README.md                    ← This file
```

---

*Dataset is simulated for portfolio purposes. Schema and data designed to reflect realistic supermarket retail operations.*
