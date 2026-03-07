-- ============================================================
--  RETAIL SALES & CUSTOMER ANALYSIS
--  Author : Toluwalase Majekodunmi
--  Tools  : SQL (PostgreSQL / BigQuery compatible)
--  Dataset: Simulated supermarket sales data
--           Tables: customers, products, transactions, stores
--  Purpose: Business insight queries demonstrating JOINs,
--           CTEs, Window Functions, aggregations & subqueries
-- ============================================================


-- ============================================================
-- SCHEMA REFERENCE
-- ============================================================
/*
  customers       (customer_id, name, email, city, loyalty_tier, joined_date)
  products        (product_id, name, category, subcategory, unit_price, cost_price)
  stores          (store_id, city, region, store_size_sqm, opened_date)
  transactions    (txn_id, customer_id, store_id, txn_date, payment_method)
  transaction_items (item_id, txn_id, product_id, quantity, unit_price, discount_pct)
*/


-- ============================================================
-- QUERY 1: Total Revenue, Cost & Gross Profit by Month
-- Technique: DATE_TRUNC, aggregation, derived columns
-- Business Q: How is revenue and margin trending month-on-month?
-- ============================================================
SELECT
    DATE_TRUNC('month', t.txn_date)          AS month,
    COUNT(DISTINCT t.txn_id)                  AS total_transactions,
    SUM(ti.quantity * ti.unit_price
        * (1 - ti.discount_pct / 100))        AS total_revenue,
    SUM(ti.quantity * p.cost_price)           AS total_cost,
    SUM(ti.quantity * ti.unit_price
        * (1 - ti.discount_pct / 100))
    - SUM(ti.quantity * p.cost_price)         AS gross_profit,
    ROUND(
        (SUM(ti.quantity * ti.unit_price * (1 - ti.discount_pct / 100))
         - SUM(ti.quantity * p.cost_price))
        / NULLIF(SUM(ti.quantity * ti.unit_price
                     * (1 - ti.discount_pct / 100)), 0) * 100, 2
    )                                         AS gross_margin_pct
FROM transactions t
JOIN transaction_items ti ON t.txn_id     = ti.txn_id
JOIN products p           ON ti.product_id = p.product_id
GROUP BY DATE_TRUNC('month', t.txn_date)
ORDER BY month;


-- ============================================================
-- QUERY 2: Top 10 Best-Selling Products by Revenue
-- Technique: JOIN, aggregation, ORDER BY + LIMIT
-- Business Q: Which products are driving the most revenue?
-- ============================================================
SELECT
    p.product_id,
    p.name                                    AS product_name,
    p.category,
    p.subcategory,
    SUM(ti.quantity)                          AS units_sold,
    ROUND(SUM(ti.quantity * ti.unit_price
              * (1 - ti.discount_pct / 100)), 2) AS total_revenue,
    ROUND(AVG(ti.discount_pct), 2)            AS avg_discount_pct
FROM transaction_items ti
JOIN products p ON ti.product_id = p.product_id
GROUP BY p.product_id, p.name, p.category, p.subcategory
ORDER BY total_revenue DESC
LIMIT 10;


-- ============================================================
-- QUERY 3: Customer Segmentation by Spend — RFM Lite
-- Technique: CTE, aggregation, CASE WHEN segmentation
-- Business Q: How do we classify customers by spend behaviour?
-- ============================================================
WITH customer_spend AS (
    SELECT
        c.customer_id,
        c.name,
        c.loyalty_tier,
        c.city,
        COUNT(DISTINCT t.txn_id)                          AS total_transactions,
        ROUND(SUM(ti.quantity * ti.unit_price
                  * (1 - ti.discount_pct / 100)), 2)      AS lifetime_value,
        MAX(t.txn_date)                                   AS last_purchase_date,
        ROUND(AVG(ti.quantity * ti.unit_price
                  * (1 - ti.discount_pct / 100)), 2)      AS avg_basket_size
    FROM customers c
    JOIN transactions t       ON c.customer_id  = t.customer_id
    JOIN transaction_items ti ON t.txn_id        = ti.txn_id
    GROUP BY c.customer_id, c.name, c.loyalty_tier, c.city
)
SELECT
    customer_id,
    name,
    loyalty_tier,
    city,
    total_transactions,
    lifetime_value,
    last_purchase_date,
    avg_basket_size,
    CASE
        WHEN lifetime_value >= 5000 AND total_transactions >= 20 THEN 'Champion'
        WHEN lifetime_value >= 2500 AND total_transactions >= 10 THEN 'Loyal'
        WHEN lifetime_value >= 1000                              THEN 'Promising'
        WHEN last_purchase_date < CURRENT_DATE - INTERVAL '90 days' THEN 'At Risk'
        ELSE 'New / Occasional'
    END                                                   AS customer_segment
FROM customer_spend
ORDER BY lifetime_value DESC;


-- ============================================================
-- QUERY 4: Revenue by Store & Region with Running Total
-- Technique: Window function (SUM OVER), JOIN, GROUP BY
-- Business Q: Which stores and regions perform best, and
--             what share of total revenue does each contribute?
-- ============================================================
WITH store_revenue AS (
    SELECT
        s.store_id,
        s.city                                            AS store_city,
        s.region,
        ROUND(SUM(ti.quantity * ti.unit_price
                  * (1 - ti.discount_pct / 100)), 2)      AS store_revenue
    FROM transactions t
    JOIN transaction_items ti ON t.txn_id   = ti.txn_id
    JOIN stores s             ON t.store_id = s.store_id
    GROUP BY s.store_id, s.city, s.region
)
SELECT
    store_id,
    store_city,
    region,
    store_revenue,
    ROUND(store_revenue
          / SUM(store_revenue) OVER () * 100, 2)          AS revenue_share_pct,
    SUM(store_revenue)
        OVER (ORDER BY store_revenue DESC
              ROWS BETWEEN UNBOUNDED PRECEDING
                       AND CURRENT ROW)                   AS running_total
FROM store_revenue
ORDER BY store_revenue DESC;


-- ============================================================
-- QUERY 5: Month-over-Month Revenue Growth Rate
-- Technique: CTE + LAG window function
-- Business Q: Is the business growing or declining each month?
-- ============================================================
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', t.txn_date)                   AS month,
        ROUND(SUM(ti.quantity * ti.unit_price
                  * (1 - ti.discount_pct / 100)), 2)      AS revenue
    FROM transactions t
    JOIN transaction_items ti ON t.txn_id = ti.txn_id
    GROUP BY DATE_TRUNC('month', t.txn_date)
)
SELECT
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month)                    AS prev_month_revenue,
    ROUND(
        (revenue - LAG(revenue) OVER (ORDER BY month))
        / NULLIF(LAG(revenue) OVER (ORDER BY month), 0) * 100, 2
    )                                                     AS mom_growth_pct
FROM monthly_revenue
ORDER BY month;


-- ============================================================
-- QUERY 6: Product Category Performance with Rank
-- Technique: Window function RANK(), GROUP BY, HAVING
-- Business Q: Which categories rank highest by profitability?
-- ============================================================
WITH category_metrics AS (
    SELECT
        p.category,
        SUM(ti.quantity)                                  AS units_sold,
        ROUND(SUM(ti.quantity * ti.unit_price
                  * (1 - ti.discount_pct / 100)), 2)      AS revenue,
        ROUND(SUM(ti.quantity * (ti.unit_price
                  * (1 - ti.discount_pct / 100)
                  - p.cost_price)), 2)                    AS gross_profit
    FROM transaction_items ti
    JOIN products p ON ti.product_id = p.product_id
    GROUP BY p.category
)
SELECT
    category,
    units_sold,
    revenue,
    gross_profit,
    ROUND(gross_profit / NULLIF(revenue, 0) * 100, 2)    AS margin_pct,
    RANK() OVER (ORDER BY gross_profit DESC)             AS profit_rank,
    RANK() OVER (ORDER BY revenue DESC)                  AS revenue_rank
FROM category_metrics
ORDER BY profit_rank;


-- ============================================================
-- QUERY 7: Customer Churn Risk — Identifying Lapsed Buyers
-- Technique: CTE, DATE arithmetic, subquery filter
-- Business Q: Which loyalty customers haven't bought in 60+ days?
-- ============================================================
WITH last_purchase AS (
    SELECT
        c.customer_id,
        c.name,
        c.email,
        c.loyalty_tier,
        MAX(t.txn_date)                                   AS last_txn_date,
        COUNT(DISTINCT t.txn_id)                          AS total_txns,
        ROUND(SUM(ti.quantity * ti.unit_price
                  * (1 - ti.discount_pct / 100)), 2)      AS lifetime_value
    FROM customers c
    JOIN transactions t       ON c.customer_id = t.customer_id
    JOIN transaction_items ti ON t.txn_id       = ti.txn_id
    GROUP BY c.customer_id, c.name, c.email, c.loyalty_tier
)
SELECT
    customer_id,
    name,
    email,
    loyalty_tier,
    last_txn_date,
    CURRENT_DATE - last_txn_date                         AS days_since_purchase,
    total_txns,
    lifetime_value
FROM last_purchase
WHERE CURRENT_DATE - last_txn_date > 60
  AND loyalty_tier IN ('Gold', 'Platinum')
ORDER BY lifetime_value DESC;


-- ============================================================
-- QUERY 8: Discount Impact Analysis
-- Technique: CASE WHEN bucketing, aggregation, comparison
-- Business Q: Are heavy discounts actually driving more volume?
-- ============================================================
SELECT
    CASE
        WHEN ti.discount_pct = 0         THEN '0% (No Discount)'
        WHEN ti.discount_pct <= 5        THEN '1–5%'
        WHEN ti.discount_pct <= 10       THEN '6–10%'
        WHEN ti.discount_pct <= 20       THEN '11–20%'
        ELSE '20%+'
    END                                                  AS discount_band,
    COUNT(DISTINCT t.txn_id)                             AS num_transactions,
    SUM(ti.quantity)                                     AS units_sold,
    ROUND(AVG(ti.quantity * ti.unit_price
              * (1 - ti.discount_pct / 100)), 2)         AS avg_basket_value,
    ROUND(SUM(ti.quantity * ti.unit_price
              * (1 - ti.discount_pct / 100)), 2)         AS total_revenue,
    ROUND(AVG(ti.discount_pct), 2)                       AS avg_actual_discount
FROM transactions t
JOIN transaction_items ti ON t.txn_id = ti.txn_id
GROUP BY discount_band
ORDER BY avg_actual_discount;


-- ============================================================
-- QUERY 9: Store Staff Efficiency (Revenue per Square Metre)
-- Technique: JOIN, derived metric, ORDER BY
-- Business Q: Which stores generate the most revenue per sqm?
-- ============================================================
SELECT
    s.store_id,
    s.city,
    s.region,
    s.store_size_sqm,
    ROUND(SUM(ti.quantity * ti.unit_price
              * (1 - ti.discount_pct / 100)), 2)         AS total_revenue,
    ROUND(SUM(ti.quantity * ti.unit_price
              * (1 - ti.discount_pct / 100))
          / NULLIF(s.store_size_sqm, 0), 2)              AS revenue_per_sqm
FROM transactions t
JOIN transaction_items ti ON t.txn_id   = ti.txn_id
JOIN stores s             ON t.store_id = s.store_id
GROUP BY s.store_id, s.city, s.region, s.store_size_sqm
ORDER BY revenue_per_sqm DESC;


-- ============================================================
-- QUERY 10: Cohort Retention — First Purchase Month Cohorts
-- Technique: CTE, DATE_TRUNC, self-join, window function
-- Business Q: Do customers acquired in a given month
--             return to buy in subsequent months?
-- ============================================================
WITH first_purchase AS (
    SELECT
        customer_id,
        DATE_TRUNC('month', MIN(txn_date))               AS cohort_month
    FROM transactions
    GROUP BY customer_id
),
cohort_activity AS (
    SELECT
        fp.cohort_month,
        DATE_TRUNC('month', t.txn_date)                  AS activity_month,
        COUNT(DISTINCT t.customer_id)                    AS active_customers
    FROM transactions t
    JOIN first_purchase fp ON t.customer_id = fp.customer_id
    GROUP BY fp.cohort_month, DATE_TRUNC('month', t.txn_date)
),
cohort_size AS (
    SELECT
        cohort_month,
        COUNT(DISTINCT customer_id)                      AS cohort_customers
    FROM first_purchase
    GROUP BY cohort_month
)
SELECT
    ca.cohort_month,
    ca.activity_month,
    cs.cohort_customers                                  AS cohort_size,
    ca.active_customers,
    ROUND(ca.active_customers::NUMERIC
          / cs.cohort_customers * 100, 1)                AS retention_pct,
    -- months since acquisition
    EXTRACT(YEAR FROM AGE(ca.activity_month,
                          ca.cohort_month)) * 12
    + EXTRACT(MONTH FROM AGE(ca.activity_month,
                             ca.cohort_month))           AS months_since_acquisition
FROM cohort_activity ca
JOIN cohort_size cs ON ca.cohort_month = cs.cohort_month
ORDER BY ca.cohort_month, ca.activity_month;
